"""Display rendering for live simulation view using Rich library."""

from collections import deque
from typing import Any

from rich.align import Align
from rich.console import Console, Group, RenderableType
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TextColumn
from rich.table import Table
from rich.text import Text


class SimulationDisplay:
    """Renders live simulation state using Rich library.
    
    Creates a terminal UI with:
    - Top status bar (time, essence, enemy stats)
    - Center card highlight area
    - Event log
    - Pack affordability status
    - Control hints
    """

    def __init__(self, console: Console | None = None):
        """Initialize display.
        
        Args:
            console: Rich console to use (creates new if None)
        """
        # Force UTF-8 encoding and disable legacy Windows mode for better Unicode support
        self.console = console or Console(force_terminal=True, legacy_windows=False)
        
        # Current state
        self.current_time = 0.0
        self.duration = 30.0
        self.essence = 0.0
        self.essence_rate = 0.0
        self.attack = 0
        self.defense = 0
        
        # Player state (new combat system)
        self.player_hp = 100.0
        self.player_max_hp = 100.0
        self.player_deaths = 0
        self.furthest_enemy = 0
        
        # Enemy state
        self.enemy_number = 0
        self.enemy_hp = 0
        self.enemy_max_hp = 0
        self.enemy_attack = 0
        self.enemy_defense = 0
        
        # Recent events
        self.event_log: deque[dict[str, Any]] = deque(maxlen=20)
        
        # Last drawn card (for highlight)
        self.last_card: dict[str, Any] | None = None
        self.card_display_time = 0.0
        
        # Pack affordability tracking
        self.pack_status: dict[int, float | None] = {1: None, 2: None, 3: None, 4: None}
        
        # Playback state
        self.is_paused = False
        self.speed = 1
        
    def update_state(
        self,
        time: float,
        essence: float,
        essence_rate: float,
        attack: int,
        defense: int,
        enemy_number: int,
        enemy_hp: float,
        enemy_max_hp: float,
        enemy_attack: int,
        enemy_defense: int,
        player_hp: float = 100.0,
        player_max_hp: float = 100.0,
        player_deaths: int = 0,
        furthest_enemy: int = 0,
    ) -> None:
        """Update current simulation state.
        
        Args:
            time: Current simulation time (seconds)
            essence: Current essence
            essence_rate: Essence generation rate
            attack: Accumulated attack
            defense: Accumulated defense
            enemy_number: Current enemy number
            enemy_hp: Current enemy HP
            enemy_max_hp: Enemy max HP
            enemy_attack: Enemy attack
            enemy_defense: Enemy defense
            player_hp: Current player HP
            player_max_hp: Maximum player HP
            player_deaths: Number of deaths
            furthest_enemy: Furthest enemy reached
        """
        self.current_time = time
        self.essence = essence
        self.essence_rate = essence_rate
        self.attack = attack
        self.defense = defense
        self.enemy_number = enemy_number
        self.enemy_hp = max(0, enemy_hp)
        self.enemy_max_hp = enemy_max_hp
        self.enemy_attack = enemy_attack
        self.enemy_defense = enemy_defense
        self.player_hp = player_hp
        self.player_max_hp = player_max_hp
        self.player_deaths = player_deaths
        self.furthest_enemy = furthest_enemy
        
    def add_event(self, event: dict) -> None:
        """Add event to log and handle card display.
        
        Args:
            event: Event dict with time, type, data
        """
        event_type = event.get("type", "unknown")
        event_time = event.get("time", 0)
        data = event.get("data", {})
        
        # Update last card if this is a draw event
        if event_type == "draw":
            self.last_card = data
            self.card_display_time = event_time
        
        # Show reshuffle in card display area
        elif event_type == "reshuffle":
            # Create a special "card" for reshuffle
            self.last_card = {
                "card_name": "🔄 DECK SHUFFLING...",
                "card_id": "RESHUFFLE",
                "is_reshuffle": True,
            }
            self.card_display_time = event_time
            
        # Add to event log
        self.event_log.append(event)
        
        # Update pack status if affordable
        if event_type == "pack_affordable":
            pack_num = data.get("pack_number")
            if pack_num and pack_num not in [k for k, v in self.pack_status.items() if v is not None]:
                self.pack_status[pack_num] = event_time / 60  # Convert to minutes
                
    def set_playback_state(self, is_paused: bool, speed: int) -> None:
        """Update playback state.
        
        Args:
            is_paused: Whether playback is paused
            speed: Current speed multiplier
        """
        self.is_paused = is_paused
        self.speed = speed
        
    def render(self) -> RenderableType:
        """Render current display state.
        
        Returns:
            Rich renderable for display
        """
        # Create main layout with flexible sizing
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=5),
            Layout(name="main", ratio=1, minimum_size=8),
            Layout(name="packs", size=3),
            Layout(name="controls", size=5),
        )
        
        # Render each section
        layout["header"].update(self._render_header())
        layout["main"].update(self._render_main())
        layout["packs"].update(self._render_pack_status())
        layout["controls"].update(self._render_controls())
        
        # Return layout without outer Panel to avoid extra border lines
        return Panel(layout, title="[bold cyan]IDLE DECK BATTLER - LIVE SIMULATION[/bold cyan]", border_style="cyan", padding=(0, 0))
        
    def _render_header(self) -> RenderableType:
        """Render top status bar."""
        # Time and essence
        time_min = int(self.current_time // 60)
        time_sec = int(self.current_time % 60)
        duration_min = int(self.duration)
        
        left_text = Text()
        left_text.append(f"Time: {time_min:02d}:{time_sec:02d} / {duration_min:02d}:00", style="yellow")
        left_text.append("  ")
        left_text.append(f"Essence: {self.essence:,.0f}", style="cyan")
        left_text.append(f" (+{self.essence_rate:.0f}/sec)", style="dim cyan")
        
        # Player stats
        left_text.append("\n")
        # Player HP bar (matching enemy format)
        if self.player_max_hp > 0:
            hp_pct = self.player_hp / self.player_max_hp
            bar_width = 20
            filled = int(hp_pct * bar_width)
            bar = "█" * filled + "░" * (bar_width - filled)
            hp_color = "green" if hp_pct > 0.5 else "yellow" if hp_pct > 0.25 else "red"
            left_text.append(f"{bar} ", style=hp_color)
            left_text.append(f"{self.player_hp:.0f}/{self.player_max_hp:.0f} HP", style="white")
        else:
            left_text.append(f"HP: {self.player_hp:.0f}/{self.player_max_hp:.0f}", style="green" if self.player_hp > 50 else "yellow" if self.player_hp > 20 else "red")
        
        # UI Tweak (Task 2.1.2C): Move ATK/DEF to next line for better readability
        left_text.append("\n")
        left_text.append(f"ATK: {self.attack:,}", style="red")
        left_text.append("  ")
        left_text.append(f"DEF: {self.defense:,}", style="green")
        if self.player_deaths > 0:
            left_text.append("  ")
            left_text.append(f"Deaths: {self.player_deaths}", style="dim red")
        
        # Enemy info
        right_text = Text()
        if self.enemy_number > 0:
            right_text.append(f"Enemy #{self.enemy_number}\n", style="bold yellow")
            
            # HP bar (UI Tweak Task 2.1.2C: Keep red, don't change colors)
            if self.enemy_max_hp > 0:
                hp_pct = self.enemy_hp / self.enemy_max_hp
                bar_width = 20
                filled = int(hp_pct * bar_width)
                bar = "█" * filled + "░" * (bar_width - filled)
                # Keep enemy health bar red (user preference)
                right_text.append(f"{bar} ", style="red")
                right_text.append(f"{self.enemy_hp:,.0f} / {self.enemy_max_hp:,.0f} HP", style="white")
            
            # UI Tweak (Task 2.1.2C): Move ATK/DEF to next line for better readability
            right_text.append("\n")
            right_text.append(f"ATK: {self.enemy_attack}  ", style="red")
            right_text.append(f"DEF: {self.enemy_defense}", style="green")
        else:
            right_text.append("No enemy\n", style="dim")
            
        # Combine into table
        table = Table.grid(expand=True)
        table.add_column(ratio=1)
        table.add_column(ratio=1)
        table.add_row(left_text, right_text)
        
        return table
        
    def _render_main(self) -> RenderableType:
        """Render main content area (card highlight + event log)."""
        # Card highlight
        card_panel = self._render_card_highlight()
        
        # Event log
        log_panel = self._render_event_log()
        
        # Split layout
        main_layout = Layout()
        main_layout.split_column(
            Layout(card_panel, size=7),
            Layout(log_panel, ratio=1),
        )
        
        return main_layout
        
    def _render_card_highlight(self) -> RenderableType:
        """Render recently drawn card highlight."""
        if not self.last_card:
            return Panel("", title="[dim]No card drawn yet[/dim]", border_style="dim")
        
        # Check if this is a reshuffle indicator
        if self.last_card.get("is_reshuffle", False):
            content = Text("Deck exhausted - Reshuffling...", style="yellow bold", justify="center")
            return Panel(
                Align.center(content, vertical="middle"),
                title="[bold yellow]🔄 DECK SHUFFLE[/bold yellow]",
                border_style="yellow",
            )
            
        card_name = self.last_card.get("card_name", "Unknown Card")
        card_id = self.last_card.get("card_id", "")
        
        # Determine card type and color
        essence_rate = self.last_card.get("essence_rate", 0)
        essence_burst = self.last_card.get("essence_burst", 0)
        attack = self.last_card.get("attack", 0)
        defense = self.last_card.get("defense", 0)
        
        is_generator = essence_rate > 0 or essence_burst > 0
        is_combat = attack > 0 or defense > 0
        
        if is_generator and not is_combat:
            border_color = "cyan"
            card_type = "Generator"
        elif is_combat and not is_generator:
            border_color = "yellow"
            card_type = "Combat"
        else:
            border_color = "white"
            card_type = "Hybrid"
            
        # Build card display
        lines = []
        lines.append(Text(f"[{card_id}] {card_type}", style="dim"))
        
        if essence_rate > 0:
            lines.append(Text(f"+{essence_rate} Essence/sec", style="cyan bold"))
        if essence_burst > 0:
            lines.append(Text(f"+{essence_burst} Essence (burst)", style="cyan bold"))
        if attack > 0:
            lines.append(Text(f"+{attack} Attack", style="red bold"))
        if defense > 0:
            lines.append(Text(f"+{defense} Defense", style="green bold"))
            
        content = Group(*lines)
        
        return Panel(
            Align.center(content, vertical="middle"),
            title=f"[bold]{card_name}[/bold]",
            border_style=border_color,
        )
        
    def _render_event_log(self) -> RenderableType:
        """Render recent event log."""
        if not self.event_log:
            return Panel(Text("No events yet", style="dim"), title="Recent Activity", border_style="dim")
            
        lines = []
        for event in reversed(list(self.event_log)):
            event_time = event.get("time", 0)
            event_type = event.get("type", "unknown")
            data = event.get("data", {})
            
            time_str = f"{int(event_time // 60):02d}:{int(event_time % 60):02d}"
            
            if event_type == "draw":
                card_name = data.get("card_name", "Unknown")
                effects = []
                if data.get("essence_rate", 0) > 0:
                    effects.append(f"+{data['essence_rate']}/sec")
                if data.get("essence_burst", 0) > 0:
                    effects.append(f"+{data['essence_burst']} burst")
                if data.get("attack", 0) > 0:
                    effects.append(f"+{data['attack']} ATK")
                if data.get("defense", 0) > 0:
                    effects.append(f"+{data['defense']} DEF")
                    
                effect_str = ", ".join(effects) if effects else "no effect"
                lines.append(Text(f"{time_str} - ", style="dim") + Text(f"Card: {card_name}", style="cyan") + Text(f" ({effect_str})", style="dim"))
                
            elif event_type == "enemy_spawn":
                enemy_num = data.get("enemy_number", 0)
                hp = data.get("max_health", 0)  # Fixed: was "health", should be "max_health"
                lines.append(Text(f"{time_str} - ", style="dim") + Text(f"Enemy #{enemy_num} spawned", style="red bold") + Text(f" ({hp:,.0f} HP)", style="dim"))
                
            elif event_type == "victory":
                enemy_num = data.get("enemy_number", 0)
                # Show enemy HP from spawn event (need to track max_health)
                lines.append(Text(f"{time_str} - ", style="dim") + Text(f"✓ Defeated Enemy #{enemy_num}", style="green bold"))
                
            elif event_type == "reshuffle":
                deck_size = data.get("deck_size", 0)
                lines.append(Text(f"{time_str} - ", style="dim") + Text(f"🔄 Deck shuffled", style="yellow") + Text(f" ({deck_size} cards)", style="dim"))
                
            elif event_type == "pack_affordable":
                pack_num = data.get("pack_number", 0)
                lines.append(Text(f"{time_str} - ", style="dim") + Text(f"🎁 Pack {pack_num} affordable!", style="bright_green bold"))
                
        content = Group(*lines)  # Show all available events
        return Panel(content, title="Recent Activity", border_style="white")
        
    def _render_pack_status(self) -> RenderableType:
        """Render pack affordability status."""
        pack_costs = {1: 40_000, 2: 100_000, 3: 250_000, 4: 625_000}
        
        status_parts = []
        for pack_num in [1, 2, 3, 4]:
            affordable_time = self.pack_status.get(pack_num)
            cost = pack_costs[pack_num]
            
            if affordable_time is not None:
                status_parts.append(Text(f"Pack {pack_num} ", style="white") + Text(f"✓ ({affordable_time:.1f}m)", style="green"))
            elif self.essence >= cost:
                status_parts.append(Text(f"Pack {pack_num} ", style="white") + Text("✓", style="green"))
            else:
                needed = cost - self.essence
                status_parts.append(Text(f"Pack {pack_num} ", style="white") + Text(f"(needs {needed:,.0f})", style="dim"))
                
            if pack_num < 4:
                status_parts.append(Text("  ", style="dim"))
                
        content = Text.assemble(*status_parts)
        return Panel(Align.center(content), title="Packs", border_style="green")
        
    def _render_controls(self) -> RenderableType:
        """Render control hints."""
        # First line: Speed controls
        speed_indicators = []
        for s in [1, 2, 5, 10]:
            key = str([1, 2, 5, 10].index(s) + 1)
            if s == self.speed:
                speed_indicators.append(Text(f"[{key}]", style="bold yellow") + Text(f"{s}x", style="bold white"))
            else:
                speed_indicators.append(Text(f"[{key}]", style="dim") + Text(f"{s}x", style="dim"))
                
        speed_line = Text("Speed: ")
        for i, indicator in enumerate(speed_indicators):
            if i > 0:
                speed_line.append("  ")
            speed_line.append(indicator)
            
        # Second line: Pause/Step/Quit controls
        control_line = Text()
        if self.is_paused:
            control_line.append("[Space]", style="bold yellow")
            control_line.append("Resume", style="white")
            control_line.append("  [N]", style="bold yellow")
            control_line.append("Step", style="white")
        else:
            control_line.append("[Space]", style="yellow")
            control_line.append("Pause", style="white")
            
        control_line.append("  [Q]", style="yellow")
        control_line.append("Quit", style="white")
        
        # Combine lines
        lines = [speed_line, control_line]
        
        if self.is_paused:
            lines.append(Text("⏸ PAUSED", style="bold yellow"))
            
        content = Group(*lines)
        return Panel(Align.center(content, vertical="middle"), border_style="cyan")
        
    def render_summary(
        self,
        duration: float,
        final_essence: float,
        final_rate: float,
        enemies_defeated: int,
        enemies_encountered: int,
        cards_drawn: int,
        total_damage: float,
        pack_times: dict[int, float],
        death_enemy: int | None = None,
        player_hp: float = 100.0,
        player_max_hp: float = 100.0,
        player_deaths: int = 0,
        furthest_enemy: int = 0,
    ) -> RenderableType:
        """Render post-simulation summary screen.
        
        Args:
            duration: Simulation duration (minutes)
            final_essence: Final essence amount
            final_rate: Final essence rate
            enemies_defeated: Number of enemies defeated
            enemies_encountered: Total enemies encountered
            cards_drawn: Total cards drawn
            total_damage: Total damage dealt
            pack_times: Pack affordable times (minutes)
            death_enemy: Enemy number that caused death (if any)
            player_hp: Current player HP
            player_max_hp: Maximum player HP
            player_deaths: Number of deaths
            furthest_enemy: Furthest enemy reached
            
        Returns:
            Rich renderable for summary screen
        """
        # Build summary content
        lines = []
        
        # Duration and essence
        lines.append(Text(f"Duration: {duration:.1f} minutes", style="yellow"))
        lines.append(Text(f"Final Essence: {final_essence:,.0f} (+{final_rate:.0f}/sec)", style="cyan"))
        lines.append(Text(f"Enemies Defeated: {enemies_defeated} / {enemies_encountered}", style="white"))
        
        # New combat system stats
        if furthest_enemy > 0:
            lines.append(Text(f"Furthest Enemy: {furthest_enemy}", style="white"))
        lines.append(Text(f"Player HP: {player_hp:.0f} / {player_max_hp:.0f}", style="green" if player_hp > 0 else "red"))
        if player_deaths > 0:
            lines.append(Text(f"Deaths: {player_deaths}", style="red"))
        
        lines.append(Text(f"Cards Drawn: {cards_drawn:,}", style="white"))
        lines.append(Text(f"Total Damage: {total_damage:,.0f}", style="red"))
        lines.append(Text(""))
        
        # Pack timing
        lines.append(Text("Pack Timing:", style="bold cyan"))
        for pack_num in [1, 2, 3, 4]:
            if pack_num in pack_times:
                time_min = pack_times[pack_num]
                lines.append(Text(f"  Pack {pack_num}: ", style="white") + Text(f"{time_min:.2f}m ✓", style="green"))
            else:
                lines.append(Text(f"  Pack {pack_num}: ", style="white") + Text("Not reached", style="dim"))
        lines.append(Text(""))
        
        # Death status
        if death_enemy:
            lines.append(Text(f"Status: Died to Enemy #{death_enemy}", style="bold red"))
            if death_enemy == 150:
                lines.append(Text("        (First Boss - Tutorial Death)", style="dim red"))
        else:
            lines.append(Text("Status: Simulation completed successfully", style="bold green"))
            
        lines.append(Text(""))
        lines.append(Text("[C]harts  [R]eplay  [Q]uit", style="dim"))
        
        content = Group(*lines)
        
        return Panel(
            Align.center(content, vertical="middle"),
            title="[bold green]SIMULATION COMPLETE[/bold green]",
            border_style="green",
            padding=(1, 2),
        )

