"""Live terminal viewer for combat simulation.

Orchestrates event playback, display rendering, and keyboard input.
"""

import sys
from pathlib import Path
from typing import Any

# Platform-specific imports
if sys.platform != "win32":
    import termios
    import tty

from rich.console import Console
from rich.live import Live

from simulator.core.combat import CombatSimulator
from simulator.core.deck import Deck
from simulator.visualization.display import SimulationDisplay
from simulator.visualization.event_player import EventPlayer, PlaybackState


class LiveViewer:
    """Main live simulation viewer.
    
    Coordinates:
    - Event playback from simulation
    - Display rendering with Rich
    - Keyboard input handling
    - Auto-pause on milestones
    """

    def __init__(
        self,
        duration_minutes: float = 30.0,
        initial_speed: int = 1,
        auto_pause_milestones: bool = True,
    ):
        """Initialize live viewer.
        
        Args:
            duration_minutes: Simulation duration
            initial_speed: Initial speed multiplier
            auto_pause_milestones: Auto-pause on pack milestones
        """
        self.duration_minutes = duration_minutes
        self.initial_speed = initial_speed
        self.auto_pause_milestones = auto_pause_milestones
        
        # Create console with better Unicode support for Windows
        self.console = Console(force_terminal=True, legacy_windows=False)
        self.display = SimulationDisplay(self.console)
        self.display.duration = duration_minutes
        
        self.event_player: EventPlayer | None = None
        self.simulation_results: dict[str, Any] | None = None
        
        # Terminal settings for keyboard input
        self.old_terminal_settings: Any = None
        
        # State tracking for auto-pause
        self.packs_seen: set[int] = set()
        
    def run(self, deck: Deck) -> None:
        """Run live simulation view.
        
        Args:
            deck: Deck to simulate with
        """
        try:
            # Run simulation to get events
            self.console.print("[yellow]Running simulation...[/yellow]")
            sim = CombatSimulator()
            self.simulation_results = sim.simulate(
                duration_minutes=self.duration_minutes,
                deck=deck,
            )
            
            # Extract events
            events = self.simulation_results.get("events", [])
            if not events:
                self.console.print("[red]No events generated from simulation[/red]")
                return
                
            self.console.print(f"[green]Loaded {len(events)} events[/green]")
            self.console.print("[dim]Press Q to quit at any time[/dim]\n")
            
            # Set up event player
            self.event_player = EventPlayer(
                events=events,
                on_event=self._handle_event,
                on_complete=self._handle_complete,
                initial_speed=self.initial_speed,
            )
            
            # Set up keyboard input
            self._setup_terminal()
            
            # Start event playback
            self.event_player.start()
            
            # Run display loop
            self._display_loop()
            
        finally:
            # Clean up
            self._restore_terminal()
            if self.event_player:
                self.event_player.stop()
                
    def _setup_terminal(self) -> None:
        """Set up terminal for non-blocking keyboard input."""
        if sys.platform != "win32":
            # Unix-like systems
            import termios
            import tty
            self.old_terminal_settings = termios.tcgetattr(sys.stdin)
            tty.setcbreak(sys.stdin.fileno())
        # Windows: No special setup needed, will use msvcrt in _check_keyboard
        
    def _restore_terminal(self) -> None:
        """Restore terminal to original settings."""
        if sys.platform != "win32" and self.old_terminal_settings:
            import termios
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_terminal_settings)
            
    def _check_keyboard(self) -> str | None:
        """Check for keyboard input (non-blocking).
        
        Returns:
            Key pressed or None
        """
        if sys.platform == "win32":
            # Windows
            import msvcrt
            if msvcrt.kbhit():
                return msvcrt.getch().decode("utf-8", errors="ignore")
        else:
            # Unix-like
            import select
            if select.select([sys.stdin], [], [], 0)[0]:
                return sys.stdin.read(1)
        return None
        
    def _display_loop(self) -> None:
        """Main display loop with keyboard input."""
        import time
        
        with Live(
            self.display.render(),
            console=self.console,
            refresh_per_second=10,  # Reduced to avoid overwhelming display
            transient=False,  # Keep display visible
        ) as live:
            while self.event_player and self.event_player.state not in [
                PlaybackState.STOPPED,
                PlaybackState.COMPLETED,
            ]:
                # Update state from current simulation time (not just on events)
                self._update_display_from_current_time()
                
                # Update playback state indicators
                self.display.set_playback_state(
                    self.event_player.state == PlaybackState.PAUSED,
                    self.event_player.speed
                )
                
                # Update display
                live.update(self.display.render())
                
                # Check keyboard
                key = self._check_keyboard()
                if key:
                    self._handle_keypress(key)
                    
                # Sleep to control refresh rate
                # Longer sleep at higher speeds to avoid display spam
                sleep_time = 0.1 if self.event_player.speed >= 5 else 0.05
                time.sleep(sleep_time)
                
            # Final update
            live.update(self.display.render())
            
        # Show summary after playback completes
        if self.simulation_results:
            self._show_summary()
            
    def _handle_keypress(self, key: str) -> None:
        """Handle keyboard input.
        
        Args:
            key: Key that was pressed
        """
        if not self.event_player:
            return
            
        key = key.lower()
        
        # Speed controls
        if key == "1":
            self.event_player.set_speed(1)
            self.display.set_playback_state(self.event_player.state == PlaybackState.PAUSED, 1)
        elif key == "2":
            self.event_player.set_speed(2)
            self.display.set_playback_state(self.event_player.state == PlaybackState.PAUSED, 2)
        elif key == "3":
            self.event_player.set_speed(5)
            self.display.set_playback_state(self.event_player.state == PlaybackState.PAUSED, 5)
        elif key == "4":
            self.event_player.set_speed(10)
            self.display.set_playback_state(self.event_player.state == PlaybackState.PAUSED, 10)
            
        # Pause/resume
        elif key == " ":
            is_paused = self.event_player.toggle_pause()
            self.display.set_playback_state(is_paused, self.event_player.speed)
            
        # Step forward
        elif key in ["n", "\x1b[C"]:  # N or right arrow
            self.event_player.step_forward()
            
        # Quit
        elif key in ["q", "\x1b"]:  # Q or ESC
            self.event_player.stop()
            
    def _update_display_from_current_time(self) -> None:
        """Update display state from current simulation time."""
        if not self.simulation_results or not self.event_player:
            return
            
        current_sim_time = self.event_player.current_sim_time
        
        # Calculate current state from events directly for real-time accuracy
        essence = 0.0
        essence_rate = 0.0
        attack = 0
        defense = 0
        
        # Player state (new combat system)
        player_hp = 100.0
        player_max_hp = 100.0
        player_deaths = 0
        furthest_enemy = 0
        
        # Track enemy state
        enemy_number = 0
        enemy_hp = 0.0
        enemy_max_hp = 0.0
        enemy_attack = 0
        enemy_defense = 0
        enemy_spawn_time = 0.0
        attack_at_spawn = 0
        
        # Process all events up to current time
        last_enemy_spawn = None
        last_victory = None
        last_combat_tick = None  # Track most recent combat tick for enemy HP
        
        for event in self.simulation_results.get("events", []):
            event_time = event.get("time", 0)
            if event_time > current_sim_time:
                break
                
            event_type = event.get("type", "")
            data = event.get("data", {})
            
            # Process event
            if event_type == "draw":
                # Update attack/defense from card draws
                attack += data.get("attack", 0)
                defense += data.get("defense", 0)
                # Update essence rate from generators
                essence_rate += data.get("essence_rate", 0)
                # Add burst essence
                essence += data.get("essence_burst", 0)
                
            elif event_type == "enemy_spawn":
                last_enemy_spawn = event
                last_victory = None  # Clear previous victory
                last_combat_tick = None  # Clear previous combat ticks
                enemy_spawn_time = event_time
                attack_at_spawn = attack  # Capture attack at spawn time
                # Track player HP from spawn event
                player_hp = data.get("player_hp", player_hp)
                
            elif event_type == "combat_tick":
                # Track latest combat tick for enemy HP
                last_combat_tick = event
                # Update player HP from combat tick
                player_hp = data.get("player_hp", player_hp)
                
            elif event_type == "victory":
                last_victory = event
                # Keep last_enemy_spawn so we can access enemy stats
                # Update player HP from victory event
                player_hp = data.get("player_hp", player_hp)
                # Reset attack/defense after victory (new combat system)
                attack = 0
                defense = 0
                
            elif event_type == "death":
                # Player died - track death and reset state
                player_deaths += 1
                player_hp = player_max_hp
                attack = 0
                defense = 0
                essence_rate = 0.0
                furthest_enemy = data.get("furthest_enemy", furthest_enemy)
        
        # Calculate essence from rate over time
        # Essence accumulates continuously based on rate
        if essence_rate > 0:
            # Calculate total essence generated up to current time
            # We need to integrate the rate changes over time
            temp_rate = 0.0
            last_time = 0.0
            temp_essence = essence  # Start with burst essence
            
            for event in self.simulation_results.get("events", []):
                event_time = event.get("time", 0)
                if event_time > current_sim_time:
                    break
                    
                # Accumulate essence from previous rate
                if temp_rate > 0:
                    time_delta = event_time - last_time
                    temp_essence += temp_rate * time_delta
                
                # Update rate if this is a draw event with generator
                if event.get("type") == "draw":
                    rate_bonus = event.get("data", {}).get("essence_rate", 0)
                    if rate_bonus > 0:
                        temp_rate += rate_bonus
                        
                last_time = event_time
            
            # Add essence from last event to current time
            if temp_rate > 0:
                time_delta = current_sim_time - last_time
                temp_essence += temp_rate * time_delta
                
            essence = temp_essence
        
        # Determine current enemy state
        if last_enemy_spawn:
            # We have enemy spawn info (may be alive or defeated)
            data = last_enemy_spawn.get("data", {})
            enemy_number = data.get("enemy_number", 0)
            enemy_max_hp = data.get("max_health", 0)
            
            # Get per-tick rates from spawn event
            atk_per_tick = data.get("atk_per_tick", 0)
            def_per_tick = data.get("def_per_tick", 0)
            
            # Check if we have combat tick data for real-time HP and ATK/DEF
            if last_combat_tick:
                # Use actual enemy HP, ATK, DEF from most recent combat tick
                tick_data = last_combat_tick.get("data", {})
                enemy_hp = tick_data.get("enemy_hp", 0.0)
                # BUG FIX: Get enemy_attack and enemy_defense from combat_tick event
                # These are already calculated as atk_per_tick * ticks_elapsed
                enemy_attack = tick_data.get("enemy_attack", 0)
                enemy_defense = tick_data.get("enemy_defense", 0)
            elif last_victory:
                # Victory means enemy is defeated
                victory_enemy = last_victory.get("data", {}).get("enemy_number", 0)
                if victory_enemy == enemy_number:
                    enemy_hp = 0.0
                    enemy_attack = 0
                    enemy_defense = 0
                else:
                    # Not yet in combat (shouldn't happen but fallback)
                    enemy_hp = enemy_max_hp
                    enemy_attack = 0
                    enemy_defense = 0
            else:
                # Enemy just spawned, no combat ticks yet
                enemy_hp = enemy_max_hp
                # ATK/DEF start at 0 and grow each tick
                enemy_attack = 0
                enemy_defense = 0
            
        self.display.update_state(
            time=current_sim_time,
            essence=essence,
            essence_rate=essence_rate,
            attack=attack,
            defense=defense,
            enemy_number=enemy_number,
            enemy_hp=enemy_hp,
            enemy_max_hp=max(enemy_max_hp, 1.0),
            enemy_attack=enemy_attack,
            enemy_defense=enemy_defense,
            player_hp=player_hp,
            player_max_hp=player_max_hp,
            player_deaths=player_deaths,
            furthest_enemy=furthest_enemy,
        )
    
    def _handle_event(self, event: dict) -> None:
        """Handle simulation event for display.
        
        Args:
            event: Event from simulation
        """
        # Just add event to display log
        # State updates happen in _update_display_from_current_time
        self.display.add_event(event)
        
        # Check for auto-pause conditions
        event_type = event.get("type", "unknown")
        if self.auto_pause_milestones and event_type == "pack_affordable":
            pack_num = event.get("data", {}).get("pack_number")
            if pack_num and pack_num not in self.packs_seen:
                self.packs_seen.add(pack_num)
                if self.event_player:
                    self.event_player.pause()
                    self.display.set_playback_state(True, self.event_player.speed)
                    
    def _handle_complete(self) -> None:
        """Handle simulation playback completion."""
        # Nothing special to do here, summary will be shown in display loop
        pass
        
    def _show_summary(self) -> None:
        """Show post-simulation summary screen."""
        if not self.simulation_results:
            return
            
        # Extract data
        duration = self.simulation_results.get("duration_minutes", 0)
        final_essence = self.simulation_results.get("final_essence", 0)
        final_rate = self.simulation_results.get("player_essence_rate", 0)
        enemies_defeated = self.simulation_results.get("enemies_defeated", 0)
        enemies_encountered = self.simulation_results.get("enemies_encountered", 0)
        cards_drawn = self.simulation_results.get("cards_drawn", 0)
        total_damage = self.simulation_results.get("total_damage_dealt", 0)
        pack_times = self.simulation_results.get("pack_affordable_times", {})
        
        # New combat system data
        player_hp = self.simulation_results.get("player_hp", 0)
        player_max_hp = self.simulation_results.get("player_max_hp", 100)
        player_deaths = self.simulation_results.get("player_deaths", 0)
        furthest_enemy = self.simulation_results.get("furthest_enemy", 0)
        
        # Check if died to a boss
        death_enemy = None
        if enemies_defeated < enemies_encountered:
            death_enemy = enemies_defeated + 1
            
        # Render summary
        summary = self.display.render_summary(
            duration=duration,
            final_essence=final_essence,
            final_rate=final_rate,
            enemies_defeated=enemies_defeated,
            enemies_encountered=enemies_encountered,
            cards_drawn=cards_drawn,
            total_damage=total_damage,
            pack_times=pack_times,
            death_enemy=death_enemy,
            player_hp=player_hp,
            player_max_hp=player_max_hp,
            player_deaths=player_deaths,
            furthest_enemy=furthest_enemy,
        )
        
        self.console.print("\n")
        self.console.print(summary)
        
        # Wait for user input
        self.console.print("\nPress [C] for charts, [R] to replay, or [Q] to quit: ", end="")
        
        # Simple blocking input for summary
        try:
            choice = input().strip().lower()
            if choice == "c":
                self._generate_charts()
            elif choice == "r":
                self.console.print("[yellow]Replay not yet implemented[/yellow]")
            # Q or anything else exits
        except (KeyboardInterrupt, EOFError):
            pass
            
    def _generate_charts(self) -> None:
        """Generate visualization charts."""
        if not self.simulation_results:
            return
            
        try:
            from simulator.analysis.visualization import save_all_charts
            from simulator.core.cards import STARTER_DECK_CARDS
            from simulator.core.deck import Deck
            
            deck = Deck(name="Starter Deck", cards=STARTER_DECK_CARDS, tier="arcane")
            output_dir = Path("output")
            
            self.console.print("[yellow]Generating charts...[/yellow]")
            saved_files = save_all_charts(self.simulation_results, deck, str(output_dir))
            self.console.print(f"[green]Saved {len(saved_files)} chart files to {output_dir}/[/green]")
            
        except Exception as e:
            self.console.print(f"[red]Error generating charts: {e}[/red]")

