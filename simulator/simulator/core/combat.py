"""Combat simulation logic.

Handles:
- Card draw mechanics (1 card/sec)
- Power accumulation (generators stack)
- Enemy spawning and scaling (12s intervals)
- Victory/defeat conditions
- Resource rewards

Implements Session 1.3 baseline mechanics from DESIGN.md.
"""

import random
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from simulator.core.cards import Card
    from simulator.core.deck import Deck


@dataclass
class Enemy:
    """Enemy entity with scaling stats."""

    number: int  # Enemy sequence number (1-indexed)
    health: float
    attack: int
    defense: int = 0

    @classmethod
    def spawn(cls, enemy_number: int) -> "Enemy":
        """Spawn enemy with scaled stats.
        
        NEW SCALING SYSTEM (Task 2.0 revision):
        
        Enemies 1-149 (Regular): Linear progression
        - Formula: 20 + (n-1) * 65.8
        - Comfortable margins (~40%) throughout
        - Teaches mechanics and deck building
        
        Enemy 150 (First Boss): INTENTIONALLY IMPOSSIBLE on first run!
        - HP: 17,438 (125% of accumulated attack at 30min)
        - Purpose: Tutorial death, teaches prestige mechanic
        - Design: Forces first prestige, unlocks progression
        
        Enemy 151+ (Post-boss): TBD - Faster scaling or new tier
        
        Attack scaling:
        - 0-50: 0 attack (safe learning)
        - 51-100: 5-15 attack (gradual)
        - 101-149: 20-40 attack (moderate)
        - 150+ (bosses): Higher attack
        
        Args:
            enemy_number: Enemy sequence number (1-indexed)
            
        Returns:
            Enemy instance with scaled stats
        """
        # Health scaling
        if enemy_number < 150:
            # Linear progression for regular enemies (1-149)
            health = 20 + (enemy_number - 1) * 65.8
        elif enemy_number == 150:
            # First boss - TUTORIAL DEATH
            # Requires 125% of 30-minute accumulated attack (~13,950)
            health = 17_438
        else:
            # Post-boss enemies (151+)
            # For now, continue linear but steeper
            # TODO: Implement tier-based scaling in future sessions
            base_post_boss = 17_438
            health = base_post_boss + (enemy_number - 150) * 100

        # Attack scaling by range
        if enemy_number <= 50:
            attack = 0  # Safe learning phase
        elif enemy_number <= 100:
            # Linear scale from 5 to 15 over enemies 51-100
            attack = int(5 + (enemy_number - 51) * (10 / 49))
        elif enemy_number < 150:
            # Linear scale from 20 to 40 over enemies 101-149
            attack = int(20 + (enemy_number - 101) * (20 / 48))
        elif enemy_number == 150:
            # First boss - moderate attack
            attack = 50
        else:
            # Post-boss enemies
            attack = int(50 + (enemy_number - 150) * 1.0)

        return cls(number=enemy_number, health=health, attack=attack)


@dataclass
class SimulationEvent:
    """Timestamped simulation event."""

    time: float  # Time in seconds
    event_type: str  # 'draw', 'enemy_spawn', 'victory', 'defeat', 'pack_affordable'
    data: dict = field(default_factory=dict)


@dataclass
class SimulationState:
    """Current simulation state snapshot."""

    time: float
    essence: float
    essence_rate: float  # Current Essence/sec rate
    accumulated_attack: int
    accumulated_defense: int
    cards_drawn: int
    enemies_defeated: int
    enemies_encountered: int
    current_enemy: Enemy | None


class CombatSimulator:
    """Combat simulation engine.
    
    Simulates the continuous card draw system where:
    - Cards are drawn at 1/sec (60 cards/min) - DESIGN.md baseline
    - Generator cards stack (each draw adds to rate, including duplicates)
    - Combat power accumulates from cards drawn
    - Enemies spawn every 12 seconds with scaling stats
    - Combat resolves instantly when enemy spawns
    """

    def __init__(
        self,
        draw_interval: float = 1.0,  # 1 card/sec per DESIGN.md
        enemy_interval: float = 12.0,  # 12 sec per DESIGN.md
    ) -> None:
        """Initialize combat simulator.
        
        Args:
            draw_interval: Seconds between card draws (default: 1.0)
            enemy_interval: Seconds between enemy spawns (default: 12.0)
        """
        self.draw_interval = draw_interval
        self.enemy_interval = enemy_interval

        # Simulation state
        self.current_time: float = 0.0
        self.essence: float = 0.0
        self.essence_rate: float = 0.0  # Stacking generator rate (Essence/sec)
        self.accumulated_attack: int = 0
        self.accumulated_defense: int = 0

        # Deck state
        self.deck_cards: list["Card"] = []
        self.draw_pile: list["Card"] = []
        self.draw_index: int = 0

        # Combat state
        self.current_enemy: Enemy | None = None
        self.enemy_number: int = 0  # Next enemy to spawn

        # Statistics
        self.cards_drawn: int = 0
        self.enemies_defeated: int = 0
        self.enemies_encountered: int = 0
        self.total_damage_dealt: float = 0.0
        self.total_damage_taken: int = 0

        # Event tracking
        self.events: list[SimulationEvent] = []
        self.state_history: list[SimulationState] = []

    def reset(self) -> None:
        """Reset simulation state."""
        self.current_time = 0.0
        self.essence = 0.0
        self.essence_rate = 0.0
        self.accumulated_attack = 0
        self.accumulated_defense = 0
        self.deck_cards = []
        self.draw_pile = []
        self.draw_index = 0
        self.current_enemy = None
        self.enemy_number = 0
        self.cards_drawn = 0
        self.enemies_defeated = 0
        self.enemies_encountered = 0
        self.total_damage_dealt = 0.0
        self.total_damage_taken = 0
        self.events = []
        self.state_history = []

    def load_deck(self, deck: "Deck") -> None:
        """Load deck and prepare for simulation.
        
        Args:
            deck: Deck to simulate with
        """
        self.deck_cards = list(deck.cards)
        self._shuffle_deck()

    def _shuffle_deck(self) -> None:
        """Shuffle deck and reset draw pile."""
        self.draw_pile = self.deck_cards.copy()
        random.shuffle(self.draw_pile)
        self.draw_index = 0

    def _draw_card(self) -> "Card":
        """Draw next card from deck, reshuffling if needed.
        
        Returns:
            Drawn card
        """
        # Reshuffle if deck exhausted
        if self.draw_index >= len(self.draw_pile):
            self._shuffle_deck()

        card = self.draw_pile[self.draw_index]
        self.draw_index += 1
        self.cards_drawn += 1

        # Apply card effects
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
                },
            )
        )

        return card

    def _apply_card_effects(self, card: "Card") -> None:
        """Apply card effects when drawn.
        
        Generator stacking mechanic (DESIGN.md Session 1.3):
        - Rate generators: Add to essence_rate (stacks, persists until death)
        - Burst generators: Immediate essence
        - Combat cards: Add to accumulated attack/defense
        
        Args:
            card: Card being drawn
        """
        # Generator effects (stack on every draw, including duplicates)
        if card.essence_rate > 0:
            self.essence_rate += card.essence_rate

        if card.essence_burst > 0:
            self.essence += card.essence_burst

        # Combat effects (accumulate)
        self.accumulated_attack += card.attack
        self.accumulated_defense += card.defense

    def _generate_essence(self, time_delta: float) -> None:
        """Generate essence based on current rate.
        
        Args:
            time_delta: Time elapsed in seconds
        """
        if self.essence_rate > 0:
            self.essence += self.essence_rate * time_delta

    def _spawn_enemy(self) -> None:
        """Spawn next enemy with scaled stats."""
        self.enemy_number += 1
        self.current_enemy = Enemy.spawn(self.enemy_number)
        self.enemies_encountered += 1

        self.events.append(
            SimulationEvent(
                time=self.current_time,
                event_type="enemy_spawn",
                data={
                    "enemy_number": self.enemy_number,
                    "health": self.current_enemy.health,
                    "attack": self.current_enemy.attack,
                },
            )
        )

    def _resolve_combat(self) -> None:
        """Resolve combat with current enemy.
        
        Combat resolution (instant):
        - Player deals accumulated_attack damage
        - Enemy deals attack damage (blocked by accumulated_defense)
        - If enemy health <= 0: Victory
        - If player defense < enemy attack: Defeat (not implemented in baseline)
        """
        if not self.current_enemy:
            return

        # Deal damage to enemy
        damage_dealt = self.accumulated_attack
        self.current_enemy.health -= damage_dealt
        self.total_damage_dealt += damage_dealt

        # Take damage from enemy (if defense insufficient) - before checking victory
        if self.accumulated_defense < self.current_enemy.attack:
            damage_taken = self.current_enemy.attack - self.accumulated_defense
            self.total_damage_taken += damage_taken
            # Note: Defeat/death not fully implemented in baseline
            # (baseline assumes deck is strong enough to always win)

        # Check for victory (do this last, as it clears current_enemy)
        if self.current_enemy.health <= 0:
            self._handle_victory()

    def _handle_victory(self) -> None:
        """Handle enemy defeat - grant rewards and clear enemy."""
        if not self.current_enemy:
            return

        self.enemies_defeated += 1

        # Record victory event
        self.events.append(
            SimulationEvent(
                time=self.current_time,
                event_type="victory",
                data={
                    "enemy_number": self.current_enemy.number,
                    "overkill": abs(self.current_enemy.health),
                },
            )
        )

        # Clear enemy
        self.current_enemy = None

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
        state = SimulationState(
            time=self.current_time,
            essence=self.essence,
            essence_rate=self.essence_rate,
            accumulated_attack=self.accumulated_attack,
            accumulated_defense=self.accumulated_defense,
            cards_drawn=self.cards_drawn,
            enemies_defeated=self.enemies_defeated,
            enemies_encountered=self.enemies_encountered,
            current_enemy=self.current_enemy,
        )
        self.state_history.append(state)

    def simulate(
        self,
        duration_minutes: float,
        deck: "Deck",
        state_recording_interval: float = 10.0,  # Record state every 10s
    ) -> dict:
        """Run combat simulation for specified duration.
        
        Simulation loop:
        1. Draw card every draw_interval seconds
        2. Generate essence continuously based on rate
        3. Spawn enemy every enemy_interval seconds
        4. Resolve combat when enemy spawns
        5. Track all events and state changes
        
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
        last_draw_time = 0.0
        last_enemy_time = 0.0
        last_state_record = 0.0

        # Pack costs to track affordability (from economy.py baseline)
        pack_costs = {
            1: 40_000,
            2: 100_000,
            3: 250_000,
            4: 625_000,
        }

        # Record initial state
        self._record_state()

        # Simulation loop (advance time in small steps)
        time_step = 0.1  # 100ms resolution
        self.current_time = 0.0

        while self.current_time < duration_seconds:
            # Draw card if interval elapsed
            if self.current_time - last_draw_time >= self.draw_interval:
                self._draw_card()
                last_draw_time = self.current_time

            # Spawn enemy if interval elapsed (only if no enemy is currently fighting)
            if self.current_time - last_enemy_time >= self.enemy_interval:
                if self.current_enemy is None:
                    self._spawn_enemy()
                    self._resolve_combat()
                    last_enemy_time = self.current_time
                else:
                    # Enemy still alive - keep trying to defeat it
                    self._resolve_combat()
                    # Only advance enemy timer if we defeated the enemy
                    if self.current_enemy is None:
                        last_enemy_time = self.current_time

            # Generate essence continuously
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

        return {
            "duration_minutes": duration_minutes,
            "duration_seconds": duration_minutes * 60,
            "status": "completed",
            # Final stats
            "final_essence": self.essence,
            "final_essence_rate": self.essence_rate,
            "final_attack": self.accumulated_attack,
            "final_defense": self.accumulated_defense,
            "cards_drawn": self.cards_drawn,
            "enemies_defeated": self.enemies_defeated,
            "enemies_encountered": self.enemies_encountered,
            "total_damage_dealt": self.total_damage_dealt,
            "total_damage_taken": self.total_damage_taken,
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
                    "essence_rate": s.essence_rate,
                    "attack": s.accumulated_attack,
                    "defense": s.accumulated_defense,
                    "cards_drawn": s.cards_drawn,
                    "enemies_defeated": s.enemies_defeated,
                }
                for s in self.state_history
            ],
        }

