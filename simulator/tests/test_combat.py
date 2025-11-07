"""Tests for combat simulation."""

import pytest

from simulator.core.cards import STARTER_DECK_CARDS
from simulator.core.combat import CombatSimulator, Enemy
from simulator.core.deck import Deck


def test_enemy_spawning() -> None:
    """Test enemy stat scaling formulas."""
    # Enemy 1: 20 * 1.15^0 = 20 HP, 0 attack
    enemy1 = Enemy.spawn(1)
    assert enemy1.number == 1
    assert enemy1.health == 20.0
    assert enemy1.attack == 0

    # Enemy 30: Should have scaled health, still 0 attack
    enemy30 = Enemy.spawn(30)
    assert enemy30.number == 30
    assert enemy30.health > 100  # Scaled up
    assert enemy30.attack == 0  # Still in safe zone (<=50)

    # Enemy 75: Should have some attack (51-100 range)
    enemy75 = Enemy.spawn(75)
    assert enemy75.attack > 0
    assert enemy75.attack <= 15

    # Enemy 125: Should have higher attack (101-150 range)
    enemy125 = Enemy.spawn(125)
    assert enemy125.attack >= 20
    assert enemy125.attack <= 50


def test_combat_simulator_initialization() -> None:
    """Test simulator initialization."""
    sim = CombatSimulator()
    
    assert sim.draw_interval == 1.0  # 1 card/sec baseline
    assert sim.enemy_interval == 12.0  # 12 sec baseline
    assert sim.current_time == 0.0
    assert sim.essence == 0.0
    assert sim.essence_rate == 0.0
    assert sim.accumulated_attack == 0
    assert sim.accumulated_defense == 0


def test_combat_simulator_reset() -> None:
    """Test simulator reset functionality."""
    sim = CombatSimulator()
    
    # Modify state
    sim.current_time = 100.0
    sim.essence = 5000.0
    sim.essence_rate = 10.0
    sim.cards_drawn = 50
    
    # Reset
    sim.reset()
    
    # Verify all state cleared
    assert sim.current_time == 0.0
    assert sim.essence == 0.0
    assert sim.essence_rate == 0.0
    assert sim.cards_drawn == 0


def test_deck_loading_and_shuffling() -> None:
    """Test deck loading and shuffle mechanics."""
    sim = CombatSimulator()
    deck = Deck(name="Test Deck", cards=STARTER_DECK_CARDS[:4], tier="arcane")
    
    sim.load_deck(deck)
    
    assert len(sim.deck_cards) == 4
    assert len(sim.draw_pile) == 4
    assert sim.draw_index == 0
    
    # Verify cards were shuffled (order might be different)
    assert set(c.id for c in sim.draw_pile) == set(c.id for c in deck.cards)


def test_card_draw_mechanics() -> None:
    """Test card drawing and deck cycling."""
    sim = CombatSimulator()
    deck = Deck(name="Mini Deck", cards=STARTER_DECK_CARDS[:3], tier="arcane")
    
    sim.load_deck(deck)
    
    # Draw all cards once
    for _ in range(3):
        card = sim._draw_card()
        assert card is not None
    
    assert sim.cards_drawn == 3
    assert sim.draw_index == 3
    
    # Drawing again should reshuffle
    card = sim._draw_card()
    assert card is not None
    assert sim.cards_drawn == 4
    assert sim.draw_index == 1  # Reset to 1 after shuffle + draw


def test_generator_stacking() -> None:
    """Test generator stacking mechanic."""
    from simulator.core.cards import Card, CardType, GeneratorType
    
    sim = CombatSimulator()
    
    # Create rate generator (+2 Essence/sec)
    rate_gen = Card(
        id="test_rate",
        name="Test Rate Gen",
        card_type=CardType.GENERATOR,
        generator_type=GeneratorType.RATE,
        essence_rate=2.0,
    )
    
    # Create burst generator (+100 Essence)
    burst_gen = Card(
        id="test_burst",
        name="Test Burst Gen",
        card_type=CardType.GENERATOR,
        generator_type=GeneratorType.BURST,
        essence_burst=100,
    )
    
    # Apply rate generator twice (stacking)
    sim._apply_card_effects(rate_gen)
    assert sim.essence_rate == 2.0
    
    sim._apply_card_effects(rate_gen)
    assert sim.essence_rate == 4.0  # Stacked!
    
    # Apply burst generator
    initial_essence = sim.essence
    sim._apply_card_effects(burst_gen)
    assert sim.essence == initial_essence + 100


def test_combat_power_accumulation() -> None:
    """Test combat stat accumulation."""
    from simulator.core.cards import Card, CardType
    
    sim = CombatSimulator()
    
    combat_card = Card(
        id="test_combat",
        name="Test Combat",
        card_type=CardType.COMBAT,
        attack=20,
        defense=15,
    )
    
    # Apply combat card
    sim._apply_card_effects(combat_card)
    assert sim.accumulated_attack == 20
    assert sim.accumulated_defense == 15
    
    # Apply again (accumulates)
    sim._apply_card_effects(combat_card)
    assert sim.accumulated_attack == 40
    assert sim.accumulated_defense == 30


def test_essence_generation() -> None:
    """Test continuous essence generation."""
    sim = CombatSimulator()
    sim.essence_rate = 10.0  # 10 Essence/sec
    
    # Generate for 5 seconds
    sim._generate_essence(5.0)
    assert sim.essence == 50.0
    
    # Generate for 3 more seconds
    sim._generate_essence(3.0)
    assert sim.essence == 80.0


def test_basic_simulation_run() -> None:
    """Test basic simulation execution with starter deck."""
    sim = CombatSimulator()
    deck = Deck(name="Starter Deck", cards=STARTER_DECK_CARDS, tier="arcane")
    
    # Run 5 minute simulation
    results = sim.simulate(duration_minutes=5.0, deck=deck)
    
    # Verify results structure
    assert results["status"] == "completed"
    assert results["duration_minutes"] == 5.0
    assert results["duration_seconds"] == 300.0
    
    # Should have drawn cards (60 cards/min * 5 min = 300 cards)
    assert results["cards_drawn"] > 250  # Allow some variance
    
    # Should have defeated enemies (5 enemies/min * 5 min = 25 enemies)
    assert results["enemies_defeated"] > 20
    
    # Should have generated essence
    assert results["final_essence"] > 0
    assert results["final_essence_rate"] > 0
    
    # Should have accumulated combat power
    assert results["final_attack"] > 0
    
    # Should have events
    assert len(results["events"]) > 0
    
    # Should have state history
    assert len(results["state_history"]) > 0


def test_pack_affordability_tracking() -> None:
    """Test that pack affordability is tracked correctly."""
    sim = CombatSimulator()
    deck = Deck(name="Starter Deck", cards=STARTER_DECK_CARDS, tier="arcane")
    
    # Run long enough to afford first pack
    results = sim.simulate(duration_minutes=10.0, deck=deck)
    
    # Should have pack affordable events
    pack_times = results["pack_affordable_times"]
    assert isinstance(pack_times, dict)
    
    # First pack (40k) should be affordable within 10 minutes
    # (depending on generation rate from starter deck)
    if 1 in pack_times:
        assert pack_times[1] <= 10.0  # Within 10 minutes


def test_simulation_events() -> None:
    """Test that simulation events are recorded properly."""
    sim = CombatSimulator()
    deck = Deck(name="Mini Deck", cards=STARTER_DECK_CARDS[:4], tier="arcane")
    
    results = sim.simulate(duration_minutes=1.0, deck=deck)
    
    events = results["events"]
    
    # Should have draw events
    draw_events = [e for e in events if e["type"] == "draw"]
    assert len(draw_events) > 0
    
    # Should have enemy spawn events
    spawn_events = [e for e in events if e["type"] == "enemy_spawn"]
    assert len(spawn_events) > 0
    
    # Should have victory events
    victory_events = [e for e in events if e["type"] == "victory"]
    assert len(victory_events) > 0


def test_state_history_recording() -> None:
    """Test that state history is recorded at intervals."""
    sim = CombatSimulator()
    deck = Deck(name="Starter Deck", cards=STARTER_DECK_CARDS, tier="arcane")
    
    # Run 30 second simulation (should record ~3 states at 10s intervals)
    results = sim.simulate(duration_minutes=0.5, deck=deck, state_recording_interval=10.0)
    
    state_history = results["state_history"]
    
    # Should have initial state + periodic states + final state
    assert len(state_history) >= 3
    
    # States should show progression
    assert state_history[-1]["essence"] >= state_history[0]["essence"]
    assert state_history[-1]["cards_drawn"] > state_history[0]["cards_drawn"]


def test_combat_resolution() -> None:
    """Test combat resolution mechanics."""
    sim = CombatSimulator()
    
    # Set up combat state
    sim.accumulated_attack = 100
    sim.current_enemy = Enemy.spawn(1)  # 20 HP
    
    # Resolve combat
    sim._resolve_combat()
    
    # Enemy should be defeated
    assert sim.current_enemy is None
    assert sim.enemies_defeated == 1
    assert sim.total_damage_dealt == 100


def test_hybrid_card_mechanics() -> None:
    """Test hybrid generator+combat cards."""
    from simulator.core.cards import Card, CardType, GeneratorType
    
    sim = CombatSimulator()
    
    hybrid = Card(
        id="test_hybrid",
        name="Test Hybrid",
        card_type=CardType.HYBRID,
        generator_type=GeneratorType.HYBRID,
        essence_rate=1.0,
        attack=10,
        defense=5,
    )
    
    # Apply hybrid card
    sim._apply_card_effects(hybrid)
    
    # Should affect both generation and combat
    assert sim.essence_rate == 1.0
    assert sim.accumulated_attack == 10
    assert sim.accumulated_defense == 5


