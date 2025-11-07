"""Tests for card models."""

import pytest
from pydantic import ValidationError

from simulator.core.cards import STARTER_DECK_CARDS, Card, CardType


def test_card_creation() -> None:
    """Test basic card creation."""
    card = Card(
        id="test_1",
        name="Test Card",
        card_type=CardType.GENERATOR,
        essence_rate=2.0,
    )
    assert card.id == "test_1"
    assert card.name == "Test Card"
    assert card.essence_rate == 2.0


def test_card_validation() -> None:
    """Test card validation rules."""
    # Attack must be >= 0
    with pytest.raises(ValidationError):
        Card(
            id="bad",
            name="Bad Card",
            card_type=CardType.COMBAT,
            attack=-10,
        )

    # Name cannot be empty
    with pytest.raises(ValidationError):
        Card(
            id="bad2",
            name="",
            card_type=CardType.COMBAT,
        )


def test_card_properties() -> None:
    """Test card computed properties."""
    # Generator card
    gen = Card(
        id="gen",
        name="Generator",
        card_type=CardType.GENERATOR,
        essence_rate=2.0,
    )
    assert gen.is_generator
    assert not gen.is_combat
    assert gen.total_combat_power == 0

    # Combat card
    combat = Card(
        id="combat",
        name="Attacker",
        card_type=CardType.COMBAT,
        attack=50,
        defense=25,
    )
    assert not combat.is_generator
    assert combat.is_combat
    assert combat.total_combat_power == 75

    # Hybrid card
    hybrid = Card(
        id="hybrid",
        name="Battle Mage",
        card_type=CardType.HYBRID,
        essence_rate=1.0,
        attack=20,
        defense=20,
    )
    assert hybrid.is_generator
    assert hybrid.is_combat
    assert hybrid.total_combat_power == 40


def test_card_immutability() -> None:
    """Test that cards are immutable."""
    card = Card(
        id="test",
        name="Test",
        card_type=CardType.GENERATOR,
    )

    with pytest.raises(ValidationError):
        card.name = "Modified"  # type: ignore


def test_starter_deck_cards() -> None:
    """Test starter deck card definitions."""
    assert len(STARTER_DECK_CARDS) == 8

    # Check we have the right mix
    generators = [c for c in STARTER_DECK_CARDS if c.card_type == CardType.GENERATOR]
    combat = [c for c in STARTER_DECK_CARDS if c.card_type == CardType.COMBAT]
    hybrids = [c for c in STARTER_DECK_CARDS if c.card_type == CardType.HYBRID]

    assert len(generators) == 2  # Rate and Burst
    assert len(hybrids) == 1  # Battle Mage
    assert len(combat) == 5  # 5 combat cards

    # Verify all cards are valid
    for card in STARTER_DECK_CARDS:
        assert card.tier == "arcane"
        assert len(card.name) > 0
        assert len(card.id) > 0


def test_card_string_representation() -> None:
    """Test card __str__ method."""
    card = Card(
        id="test",
        name="Test Card",
        card_type=CardType.HYBRID,
        tier="fire",
        attack=20,
        defense=15,
        essence_rate=1.5,
    )

    card_str = str(card)
    assert "Test Card" in card_str
    assert "FIRE" in card_str
    assert "ATK:20" in card_str
    assert "DEF:15" in card_str
    assert "1.5/sec" in card_str

