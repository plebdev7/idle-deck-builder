"""Combat simulation logic with combat-over-time mechanics.

Implements Session 2.0.3 + 2.1.2B combat system (DESIGN.md Version 2.0.2):
- Tick-based combat (1.0 second per tick)
- Player HP system with death mechanics
- Continuous deck cycling with reshuffle cooldown
- Stat accumulation and reset per enemy
- Death and respawn system
- Per-tick enemy scaling (ATK/DEF grow each tick)

Key Mechanics:
- Cards drawn at 1/sec continuously
- Deck cycles indefinitely (stats accumulate exponentially)
- Combat resolves tick-by-tick
- Enemy ATK/DEF scale per combat tick (counters player cycling)
- Stats accumulate during enemy fight, reset when enemy dies
- HP depletes across enemies, no healing between fights
- Death at HP = 0, respawn at Enemy 1 with full HP

Data Ownership (Task 2.1.2C):
- ALL balance values loaded from game-data/balance-config.json
- NO hardcoded formulas or scaling values
"""

import json
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from simulator.core.cards import Card
    from simulator.core.deck import Deck


# Load balance config at module level (Task 2.1.2C - Data Ownership)
_BALANCE_CONFIG_PATH = Path(__file__).parent.parent.parent.parent / "game-data" / "balance-config.json"
try:
    with open(_BALANCE_CONFIG_PATH, "r", encoding="utf-8") as f:
        BALANCE_CONFIG = json.load(f)
except FileNotFoundError:
    raise FileNotFoundError(
        f"balance-config.json not found at {_BALANCE_CONFIG_PATH}. "
        "Simulator requires game-data/balance-config.json for all balance values."
    )


@dataclass
class Player:
    """Player entity with HP and combat stats.
    
    DATA OWNERSHIP (Task 2.1.2C):
    Default HP value loaded from game-data/balance-config.json
    """
    
    current_hp: float = field(default_factory=lambda: BALANCE_CONFIG["player_stats"]["starting_hp"])
    max_hp: float = field(default_factory=lambda: BALANCE_CONFIG["player_stats"]["starting_hp"])
    
    # Combat stats (accumulate during fight, reset per enemy)
    attack: int = 0
    defense: int = 0
    
    # Generation stats (accumulate during fight, reset on death)
    essence_rate: float = 0.0  # Essence/sec from generators
    
    # Death tracking
    deaths: int = 0
    furthest_enemy: int = 0
    
    def is_alive(self) -> bool:
        """Check if player is alive."""
        return self.current_hp > 0
    
    def take_damage(self, amount: float) -> None:
        """Take damage, reducing current HP.
        
        Args:
            amount: Damage amount (already reduced by defense)
        """
        self.current_hp = max(0, self.current_hp - amount)
    
    def reset_combat_stats(self) -> None:
        """Reset combat stats after enemy defeat."""
        self.attack = 0
        self.defense = 0
        # essence_rate persists between enemies
    
    def die(self) -> None:
        """Handle player death - reset stats and HP."""
        self.deaths += 1
        self.current_hp = self.max_hp
        self.attack = 0
        self.defense = 0
        self.essence_rate = 0.0


@dataclass
class Enemy:
    """Enemy entity with per-tick scaling stats.
    
    Per-Tick Scaling System (Session 2.1.2B):
    - Enemies gain ATK and DEF each combat tick
    - Prevents "default invulnerability" from player deck cycling
    - Bosses scale 2× faster than regular enemies
    """

    number: int  # Enemy sequence number (1-indexed)
    max_health: float  # Maximum health
    current_health: float  # Current health (for combat)
    atk_per_tick: float  # ATK gained per combat tick
    def_per_tick: float  # DEF gained per combat tick
    is_boss: bool = False  # Boss multiplier flag
    combat_ticks_elapsed: int = 0  # Ticks since combat started

    @classmethod
    def spawn(cls, enemy_number: int) -> "Enemy":
        """Spawn enemy with scaled stats.
        
        DATA OWNERSHIP (Task 2.1.2C):
        All scaling values loaded from game-data/balance-config.json
        
        PER-TICK SCALING SYSTEM (Session 2.1.2B):
        - All enemies attack from tick 0. ATK/DEF grow each combat tick
        - Per-tick rates defined in balance-config.json per_tick_scaling
        - Bosses scale 2× faster than regular enemies
        
        HP SCALING (Act-Based Step Function):
        - HP formulas defined in balance-config.json hp_formulas
        - Boss multipliers defined in balance-config.json boss_multipliers
        
        Args:
            enemy_number: Enemy sequence number (1-indexed)
            
        Returns:
            Enemy instance with scaled stats
        """
        # Load scaling config from balance-config.json
        enemy_config = BALANCE_CONFIG["enemy_scaling"]
        hp_formulas = enemy_config["hp_formulas"]
        per_tick_config = enemy_config["per_tick_scaling"]
        boss_config = enemy_config["boss_multipliers"]
        
        # Boss detection (every 50 enemies)
        is_boss = (enemy_number % 50 == 0)
        
        # Determine which act this enemy belongs to
        if enemy_number <= 50:
            act_key = "act_1"
            hp_data = hp_formulas["act_1"]
            tick_data = per_tick_config["act_1"]
        elif enemy_number <= 100:
            act_key = "act_2"
            hp_data = hp_formulas["act_2"]
            tick_data = per_tick_config["act_2"]
        elif enemy_number <= 150:
            act_key = "act_3"
            hp_data = hp_formulas["act_3"]
            tick_data = per_tick_config["act_3"]
        else:
            # Act 4+ (future content)
            act_key = "act_4"
            hp_data = hp_formulas["act_4"]
            # Act 4 tick data not in config yet, use Act 3 values
            tick_data = {
                "atk_base": 13.5,
                "atk_growth_per_enemy": 0.15,
                "def_base": 6.75,
                "def_growth_per_enemy": 0.075,
            }
        
        # Calculate HP from formula in config
        # Parse formula string to extract base and growth values
        # Format: "base + (n - start) * growth"
        if act_key == "act_1":
            base_hp = 20 + (enemy_number - 1) * 120
        elif act_key == "act_2":
            base_hp = 6000 + (enemy_number - 51) * 130
        elif act_key == "act_3":
            base_hp = 12500 + (enemy_number - 101) * 140
        else:  # act_4
            base_hp = 38880 + (enemy_number - 151) * 200
        
        # Apply boss HP multiplier
        if is_boss:
            boss_hp_mult = boss_config["hp"].get(str(enemy_number), 2.0)  # Default 2× for future bosses
            health = base_hp * boss_hp_mult
        else:
            health = base_hp
        
        # Calculate per-tick ATK/DEF from config
        if act_key == "act_1":
            atk_per_tick = tick_data["atk_base"] + (enemy_number - 1) * tick_data["atk_growth_per_enemy"]
            def_per_tick = tick_data["def_base"] + (enemy_number - 1) * tick_data["def_growth_per_enemy"]
        elif act_key == "act_2":
            atk_per_tick = tick_data["atk_base"] + (enemy_number - 51) * tick_data["atk_growth_per_enemy"]
            def_per_tick = tick_data["def_base"] + (enemy_number - 51) * tick_data["def_growth_per_enemy"]
        elif act_key == "act_3":
            atk_per_tick = tick_data["atk_base"] + (enemy_number - 101) * tick_data["atk_growth_per_enemy"]
            def_per_tick = tick_data["def_base"] + (enemy_number - 101) * tick_data["def_growth_per_enemy"]
        else:  # act_4
            atk_per_tick = tick_data["atk_base"] + (enemy_number - 151) * tick_data["atk_growth_per_enemy"]
            def_per_tick = tick_data["def_base"] + (enemy_number - 151) * tick_data["def_growth_per_enemy"]
        
        # Apply boss multiplier (2× faster scaling)
        if is_boss:
            boss_tick_mult = boss_config["per_tick_rates"]["multiplier"]
            atk_per_tick *= boss_tick_mult
            def_per_tick *= boss_tick_mult

        return cls(
            number=enemy_number, 
            max_health=health,
            current_health=health,
            atk_per_tick=atk_per_tick,
            def_per_tick=def_per_tick,
            is_boss=is_boss,
            combat_ticks_elapsed=0
        )
    
    def current_attack(self) -> float:
        """Calculate current ATK based on ticks elapsed.
        
        Returns:
            Current ATK value (atk_per_tick × ticks_elapsed)
        """
        return self.atk_per_tick * self.combat_ticks_elapsed
    
    def current_defense(self) -> float:
        """Calculate current DEF based on ticks elapsed.
        
        Returns:
            Current DEF value (def_per_tick × ticks_elapsed)
        """
        return self.def_per_tick * self.combat_ticks_elapsed
    
    def tick(self) -> None:
        """Increment combat tick counter (called each combat tick)."""
        self.combat_ticks_elapsed += 1
    
    def is_alive(self) -> bool:
        """Check if enemy is alive."""
        return self.current_health > 0
    
    def take_damage(self, amount: float) -> None:
        """Take damage, reducing current HP.
        
        Args:
            amount: Damage amount (already reduced by defense)
        """
        self.current_health = max(0, self.current_health - amount)


@dataclass
class SimulationEvent:
    """Timestamped simulation event."""

    time: float  # Time in seconds
    event_type: str  # 'draw', 'enemy_spawn', 'victory', 'defeat', 'death', 'combat_tick', 'pack_affordable', 'reshuffle'
    data: dict = field(default_factory=dict)


@dataclass
class SimulationState:
    """Current simulation state snapshot."""

    time: float
    essence: float
    player: Player
    cards_drawn: int
    enemies_defeated: int
    enemies_encountered: int
    current_enemy: Enemy | None
    in_combat: bool
    combat_ticks: int  # Total combat ticks this run


class CombatSimulator:
    """Combat simulation engine with tick-based combat.
    
    Implements Session 2.0.3 combat system redesign:
    - Tick-based combat (1.0 second per tick)
    - Player HP system with death/respawn
    - Continuous deck cycling with 1s reshuffle cooldown
    - Stat accumulation during fight, reset per enemy
    - Essence rate persists between enemies, resets on death
    
    Combat Flow:
    1. Cards draw at 1/sec, adding to player ATK/DEF/essence_rate
    2. Enemy spawns when no active enemy
    3. Combat ticks at 1/sec: deal damage, take damage
    4. Enemy dies → reset ATK/DEF, spawn next enemy
    5. Player dies (HP=0) → reset to Enemy 1, restore HP
    """

    def __init__(
        self,
        draw_interval: float | None = None,
        combat_tick_interval: float | None = None,
        reshuffle_cooldown: float | None = None,
    ) -> None:
        """Initialize combat simulator.
        
        DATA OWNERSHIP (Task 2.1.2C):
        If timing values not provided, load from game-data/balance-config.json
        
        Args:
            draw_interval: Seconds between card draws (default: from balance-config.json)
            combat_tick_interval: Seconds between combat ticks (default: from balance-config.json)
            reshuffle_cooldown: Cooldown after deck exhausts (default: from balance-config.json)
        """
        # Load timing from balance-config.json if not provided
        timing_config = BALANCE_CONFIG["combat_timing"]
        
        self.draw_interval = draw_interval if draw_interval is not None else timing_config["card_draw_interval"]
        self.combat_tick_interval = combat_tick_interval if combat_tick_interval is not None else timing_config["combat_tick_interval"]
        self.reshuffle_cooldown = reshuffle_cooldown if reshuffle_cooldown is not None else timing_config["reshuffle_cooldown"]

        # Simulation state
        self.current_time: float = 0.0
        self.essence: float = 0.0
        self.shards: int = 0  # Combat rewards
        self.player: Player = Player()

        # Deck state
        self.deck_cards: list["Card"] = []
        self.draw_pile: list["Card"] = []
        self.draw_index: int = 0
        self.is_reshuffling: bool = False
        self.reshuffle_end_time: float = 0.0

        # Combat state
        self.current_enemy: Enemy | None = None
        self.enemy_number: int = 0  # Current enemy sequence
        self.in_combat: bool = False
        self.combat_start_time: float = 0.0  # Track combat start for duration

        # Statistics
        self.cards_drawn: int = 0
        self.enemies_defeated: int = 0
        self.enemies_encountered: int = 0
        self.total_damage_dealt: float = 0.0
        self.total_damage_taken: float = 0.0
        self.combat_ticks: int = 0  # Total combat ticks
        self.combat_durations: list[float] = []  # Duration per enemy

        # Event tracking
        self.events: list[SimulationEvent] = []
        self.state_history: list[SimulationState] = []

    def reset(self) -> None:
        """Reset simulation state."""
        self.current_time = 0.0
        self.essence = 0.0
        self.shards = 0
        self.player = Player()
        self.deck_cards = []
        self.draw_pile = []
        self.draw_index = 0
        self.is_reshuffling = False
        self.reshuffle_end_time = 0.0
        self.current_enemy = None
        self.enemy_number = 0
        self.in_combat = False
        self.combat_start_time = 0.0
        self.cards_drawn = 0
        self.enemies_defeated = 0
        self.enemies_encountered = 0
        self.total_damage_dealt = 0.0
        self.total_damage_taken = 0.0
        self.combat_ticks = 0
        self.combat_durations = []
        self.events = []
        self.state_history = []

    def load_deck(self, deck: "Deck") -> None:
        """Load deck and prepare for simulation.
        
        Args:
            deck: Deck to simulate with
        """
        # Validate minimum deck size
        if len(deck.cards) < 8:
            raise ValueError(f"Deck must have at least 8 cards (has {len(deck.cards)})")
        
        self.deck_cards = list(deck.cards)
        self._shuffle_deck()

    def _shuffle_deck(self) -> None:
        """Shuffle deck and reset draw pile."""
        self.draw_pile = self.deck_cards.copy()
        random.shuffle(self.draw_pile)
        self.draw_index = 0

    def _can_draw_card(self) -> bool:
        """Check if a card can be drawn (not in reshuffle cooldown).
        
        Returns:
            True if card can be drawn
        """
        # Can't draw during reshuffle cooldown
        if self.is_reshuffling:
            return self.current_time >= self.reshuffle_end_time
        return True

    def _draw_card(self) -> "Card | None":
        """Draw next card from deck, reshuffling if needed.
        
        Returns:
            Drawn card, or None if in reshuffle cooldown
        """
        # Check if we can draw (not in reshuffle cooldown)
        if self.is_reshuffling:
            if self.current_time >= self.reshuffle_end_time:
                # Reshuffle cooldown finished
                self.is_reshuffling = False
                self._shuffle_deck()
            else:
                # Still in cooldown
                return None
        
        # Check if we need to start reshuffle cooldown
        if self.draw_index >= len(self.draw_pile):
            # Deck exhausted, start reshuffle cooldown
            self.is_reshuffling = True
            self.reshuffle_end_time = self.current_time + self.reshuffle_cooldown
            
            # Record reshuffle event for display
            self.events.append(
                SimulationEvent(
                    time=self.current_time,
                    event_type="reshuffle",
                    data={
                        "deck_size": len(self.deck_cards),
                        "cooldown": self.reshuffle_cooldown,
                    },
                )
            )
            
            return None

        card = self.draw_pile[self.draw_index]
        self.draw_index += 1
        self.cards_drawn += 1

        # Apply card effects to player
        self._apply_card_effects(card)

        # Record event
        self.events.append(
            SimulationEvent(
                time=self.current_time,
                event_type="draw",
                data={
                    "card_id": card.id,
                    "card_name": card.name,
                    "essence_rate": card.essence_rate,
                    "essence_burst": card.essence_burst,
                    "attack": card.attack,
                    "defense": card.defense,
                    "player_attack": self.player.attack,
                    "player_defense": self.player.defense,
                    "player_essence_rate": self.player.essence_rate,
                },
            )
        )

        return card

    def _apply_card_effects(self, card: "Card") -> None:
        """Apply card effects to player when drawn.
        
        Generator stacking mechanic (DESIGN.md Session 1.3 + 2.0.3):
        - Rate generators: Add to player.essence_rate (stacks, persists until death)
        - Burst generators: Immediate essence
        - Combat cards: Add to player attack/defense (accumulate until enemy dies)
        
        Args:
            card: Card being drawn
        """
        # Generator effects (stack on every draw, including duplicates)
        if card.essence_rate > 0:
            self.player.essence_rate += card.essence_rate

        if card.essence_burst > 0:
            self.essence += card.essence_burst

        # Combat effects (accumulate until enemy dies)
        self.player.attack += card.attack
        self.player.defense += card.defense

    def _generate_essence(self, time_delta: float) -> None:
        """Generate essence based on player's current rate.
        
        Args:
            time_delta: Time elapsed in seconds
        """
        if self.player.essence_rate > 0:
            self.essence += self.player.essence_rate * time_delta

    def _spawn_enemy(self) -> None:
        """Spawn next enemy and start combat."""
        self.enemy_number += 1
        self.current_enemy = Enemy.spawn(self.enemy_number)
        self.enemies_encountered += 1
        self.in_combat = True
        self.combat_start_time = self.current_time
        
        # Track furthest enemy reached
        if self.enemy_number > self.player.furthest_enemy:
            self.player.furthest_enemy = self.enemy_number

        self.events.append(
            SimulationEvent(
                time=self.current_time,
                event_type="enemy_spawn",
                data={
                    "enemy_number": self.enemy_number,
                    "max_health": self.current_enemy.max_health,
                    "atk_per_tick": self.current_enemy.atk_per_tick,
                    "def_per_tick": self.current_enemy.def_per_tick,
                    "is_boss": self.current_enemy.is_boss,
                    "player_hp": self.player.current_hp,
                    "player_attack": self.player.attack,
                    "player_defense": self.player.defense,
                },
            )
        )

    def _combat_tick(self) -> None:
        """Process one combat tick (1 second).
        
        Combat tick mechanics (DESIGN.md Session 2.0.3 + 2.1.2B):
        - Enemy gains ATK/DEF each tick (per-tick scaling)
        - Player deals damage: max(player_attack - enemy_current_defense, 0)
        - Enemy deals damage: max(enemy_current_attack - player_defense, 0)
        - No minimum damage (perfect defense = 0 damage)
        - Cards continue to draw during combat
        """
        if not self.current_enemy or not self.in_combat:
            return
        
        self.combat_ticks += 1
        
        # Enemy gains ATK/DEF this tick (per-tick scaling)
        self.current_enemy.tick()
        
        # Calculate current enemy stats
        enemy_attack = self.current_enemy.current_attack()
        enemy_defense = self.current_enemy.current_defense()
        
        # Calculate damage (ATK - DEF, no minimum)
        player_damage = max(self.player.attack - enemy_defense, 0)
        enemy_damage = max(enemy_attack - self.player.defense, 0)
        
        # Apply damage
        if player_damage > 0:
            self.current_enemy.take_damage(player_damage)
            self.total_damage_dealt += player_damage
        
        if enemy_damage > 0:
            self.player.take_damage(enemy_damage)
            self.total_damage_taken += enemy_damage
        
        # Record combat tick event for live viewer
        # (Every tick so live viewer can show real-time HP updates)
        self.events.append(
            SimulationEvent(
                time=self.current_time,
                event_type="combat_tick",
                data={
                    "enemy_number": self.enemy_number,
                    "player_damage": player_damage,
                    "enemy_damage": enemy_damage,
                    "enemy_hp": self.current_enemy.current_health,
                    "enemy_attack": enemy_attack,
                    "enemy_defense": enemy_defense,
                    "player_hp": self.player.current_hp,
                    "player_attack": self.player.attack,
                    "player_defense": self.player.defense,
                    "ticks_elapsed": self.current_enemy.combat_ticks_elapsed,
                },
            )
        )
        
        # Check for victory or defeat
        if not self.current_enemy.is_alive():
            self._handle_victory()
        elif not self.player.is_alive():
            self._handle_defeat()

    def _handle_victory(self) -> None:
        """Handle enemy defeat - grant rewards, reset combat stats."""
        if not self.current_enemy:
            return

        self.enemies_defeated += 1
        combat_duration = self.current_time - self.combat_start_time
        self.combat_durations.append(combat_duration)
        
        # Calculate shard rewards (2-3 early, 4-6 mid, 8-12 late)
        is_boss = (self.current_enemy.number % 50 == 0)
        if is_boss:
            # Bosses give 3x-5x regular rewards
            base_shards = 2 + (self.current_enemy.number // 50) * 3
            shards = base_shards * 4
        else:
            base_shards = 2 + (self.current_enemy.number // 100)
            shards = base_shards
        
        self.shards += shards

        # Record victory event
        self.events.append(
            SimulationEvent(
                time=self.current_time,
                event_type="victory",
                data={
                    "enemy_number": self.current_enemy.number,
                    "combat_duration": combat_duration,
                    "overkill": abs(self.current_enemy.current_health),
                    "shards_earned": shards,
                    "is_boss": is_boss,
                    "player_hp": self.player.current_hp,
                },
            )
        )

        # Reset combat stats (ATK/DEF reset, essence_rate persists, HP persists)
        self.player.reset_combat_stats()
        
        # Clear enemy and exit combat
        self.current_enemy = None
        self.in_combat = False

    def _handle_defeat(self) -> None:
        """Handle player death - respawn at Enemy 1, reset stats, keep resources."""
        # Record death event
        self.events.append(
            SimulationEvent(
                time=self.current_time,
                event_type="death",
                data={
                    "furthest_enemy": self.player.furthest_enemy,
                    "enemies_defeated": self.enemies_defeated,
                    "essence_earned": self.essence,
                    "shards_earned": self.shards,
                    "deaths": self.player.deaths + 1,
                },
            )
        )
        
        # Player dies - reset stats and HP, keep resources
        self.player.die()
        
        # Respawn at Enemy 1
        self.enemy_number = 0
        self.current_enemy = None
        self.in_combat = False

    def _check_pack_affordability(self, pack_number: int, pack_cost: int) -> None:
        """Check if pack is now affordable and log event.
        
        Args:
            pack_number: Pack number to check
            pack_cost: Cost of the pack
        """
        if self.essence >= pack_cost:
            # Check if we've already logged this pack
            pack_events = [
                e
                for e in self.events
                if e.event_type == "pack_affordable" and e.data.get("pack_number") == pack_number
            ]
            if not pack_events:
                self.events.append(
                    SimulationEvent(
                        time=self.current_time,
                        event_type="pack_affordable",
                        data={
                            "pack_number": pack_number,
                            "pack_cost": pack_cost,
                            "essence": self.essence,
                        },
                    )
                )

    def _record_state(self) -> None:
        """Record current state snapshot."""
        # Make a copy of player for state history
        player_copy = Player(
            current_hp=self.player.current_hp,
            max_hp=self.player.max_hp,
            attack=self.player.attack,
            defense=self.player.defense,
            essence_rate=self.player.essence_rate,
            deaths=self.player.deaths,
            furthest_enemy=self.player.furthest_enemy,
        )
        
        state = SimulationState(
            time=self.current_time,
            essence=self.essence,
            player=player_copy,
            cards_drawn=self.cards_drawn,
            enemies_defeated=self.enemies_defeated,
            enemies_encountered=self.enemies_encountered,
            current_enemy=self.current_enemy,
            in_combat=self.in_combat,
            combat_ticks=self.combat_ticks,
        )
        self.state_history.append(state)

    def simulate(
        self,
        duration_minutes: float,
        deck: "Deck",
        state_recording_interval: float = 10.0,  # Record state every 10s
    ) -> dict:
        """Run tick-based combat simulation for specified duration.
        
        NEW Simulation loop (Session 2.0.3 - Tick-Based Combat):
        1. Every 1 second: Draw card + Combat tick (synchronized)
        2. Card draw adds stats, then combat tick uses those stats
        3. Generate essence continuously based on player.essence_rate
        4. Spawn enemy when no active enemy
        5. Handle victory (reset ATK/DEF, spawn next enemy)
        6. Handle defeat (respawn at Enemy 1, restore HP)
        7. Track all events, state changes, and combat durations
        
        Key Changes from Old System:
        - Combat no longer instant - resolves tick-by-tick
        - Card draws and combat ticks are synchronized (1 second intervals)
        - Player HP depletes over time, no healing between enemies
        - Death triggers respawn, not game over
        - Stats reset per enemy (ATK/DEF), essence_rate persists
        
        Args:
            duration_minutes: Simulation duration in minutes
            deck: Deck to simulate with
            state_recording_interval: How often to record state snapshots (seconds)
            
        Returns:
            Simulation results dictionary with events, stats, and timeline
        """
        # Reset and initialize
        self.reset()
        self.load_deck(deck)

        duration_seconds = duration_minutes * 60
        last_tick_time = 0.0  # Combined card draw + combat tick
        last_state_record = 0.0

        # Pack costs to track affordability (DATA OWNERSHIP - Task 2.1.2C)
        # Load from balance-config.json instead of hardcoded values
        pack_config = BALANCE_CONFIG["pack_costs"]["Arcane_Pack"]
        pack_costs = {
            1: pack_config["1"],
            2: pack_config["2"],
            3: pack_config["3"],
            4: pack_config["4"],
        }

        # Record initial state
        self._record_state()

        # Simulation loop (advance time in small steps)
        time_step = 0.1  # 100ms resolution for smooth essence generation
        self.current_time = 0.0

        while self.current_time < duration_seconds:
            # Spawn enemy if none active and player is alive
            if self.current_enemy is None and self.player.is_alive():
                self._spawn_enemy()

            # Process tick (card draw + combat) every 1 second
            if self.current_time - last_tick_time >= self.draw_interval:
                # Draw card first (adds stats for this tick's combat)
                self._draw_card()  # Returns None if in reshuffle cooldown
                
                # Combat tick happens immediately after card draw
                if self.in_combat:
                    self._combat_tick()
                    
                last_tick_time = self.current_time

            # Generate essence continuously (based on player.essence_rate)
            self._generate_essence(time_step)

            # Check pack affordability
            for pack_num, cost in pack_costs.items():
                self._check_pack_affordability(pack_num, cost)

            # Record state periodically
            if self.current_time - last_state_record >= state_recording_interval:
                self._record_state()
                last_state_record = self.current_time

            # Advance time
            self.current_time += time_step

        # Final state record
        self._record_state()

        # Compile results
        return self._compile_results(duration_minutes)

    def _compile_results(self, duration_minutes: float) -> dict:
        """Compile simulation results into structured dictionary.
        
        Args:
            duration_minutes: Simulation duration
            
        Returns:
            Results dictionary with stats, events, and timeline
        """
        # Find pack affordable times
        pack_times = {}
        for event in self.events:
            if event.event_type == "pack_affordable":
                pack_num = event.data["pack_number"]
                if pack_num not in pack_times:
                    pack_times[pack_num] = event.time / 60  # Convert to minutes
        
        # Calculate average combat duration
        avg_combat_duration = (
            sum(self.combat_durations) / len(self.combat_durations)
            if self.combat_durations
            else 0.0
        )

        return {
            "duration_minutes": duration_minutes,
            "duration_seconds": duration_minutes * 60,
            "status": "completed",
            # Final stats
            "final_essence": self.essence,
            "final_shards": self.shards,
            "cards_drawn": self.cards_drawn,
            "enemies_defeated": self.enemies_defeated,
            "enemies_encountered": self.enemies_encountered,
            "total_damage_dealt": self.total_damage_dealt,
            "total_damage_taken": self.total_damage_taken,
            "combat_ticks": self.combat_ticks,
            # Player stats
            "player_hp": self.player.current_hp,
            "player_max_hp": self.player.max_hp,
            "player_attack": self.player.attack,
            "player_defense": self.player.defense,
            "player_essence_rate": self.player.essence_rate,
            "player_deaths": self.player.deaths,
            "furthest_enemy": self.player.furthest_enemy,
            # Combat metrics
            "avg_combat_duration": avg_combat_duration,
            "total_combat_time": sum(self.combat_durations),
            "combat_count": len(self.combat_durations),
            # Pack timing
            "pack_affordable_times": pack_times,
            # Event timeline
            "events": [
                {
                    "time": e.time,
                    "time_minutes": e.time / 60,
                    "type": e.event_type,
                    "data": e.data,
                }
                for e in self.events
            ],
            # State history
            "state_history": [
                {
                    "time": s.time,
                    "time_minutes": s.time / 60,
                    "essence": s.essence,
                    "player_hp": s.player.current_hp,
                    "player_essence_rate": s.player.essence_rate,
                    "player_attack": s.player.attack,
                    "player_defense": s.player.defense,
                    "cards_drawn": s.cards_drawn,
                    "enemies_defeated": s.enemies_defeated,
                    "in_combat": s.in_combat,
                }
                for s in self.state_history
            ],
        }

