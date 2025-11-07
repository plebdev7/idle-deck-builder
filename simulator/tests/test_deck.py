"""Tests for deck models."""

from simulator.core.cards import STARTER_DECK_CARDS, Card, CardType
from simulator.core.deck import Deck


def test_deck_creation() -> None:
    """Test basic deck creation."""
    deck = Deck(
        name="Test Deck",
        cards=STARTER_DECK_CARDS,
        tier="arcane",
    )
    assert deck.name == "Test Deck"
    assert deck.size == 8
    assert deck.tier == "arcane"


def test_deck_statistics() -> None:
    """Test deck statistical properties."""
    deck = Deck(
        name="Starter Deck",
        cards=STARTER_DECK_CARDS,
        tier="arcane",
    )

    # Count checks
    assert deck.generator_count == 3  # 2 pure generators + 1 hybrid
    assert deck.combat_count == 6  # 5 pure combat + 1 hybrid

    # Total stats
    assert deck.total_attack > 0
    assert deck.total_defense > 0
    assert deck.total_essence_rate > 0
    assert deck.total_essence_burst > 0


def test_deck_iteration() -> None:
    """Test deck iteration."""
    cards = [
        Card(id=f"card_{i}", name=f"Card {i}", card_type=CardType.COMBAT)
        for i in range(5)
    ]
    deck = Deck(name="Test", cards=cards)

    # Test iteration
    count = 0
    for card in deck:
        assert isinstance(card, Card)
        count += 1
    assert count == 5

    # Test len
    assert len(deck) == 5


def test_empty_deck() -> None:
    """Test deck with no cards."""
    deck = Deck(name="Empty", cards=[])

    assert deck.size == 0
    assert deck.generator_count == 0
    assert deck.combat_count == 0
    assert deck.total_attack == 0
    assert deck.total_defense == 0
    assert deck.total_essence_rate == 0.0
    assert deck.total_essence_burst == 0


def test_deck_string_representation() -> None:
    """Test deck __str__ method."""
    deck = Deck(
        name="Test Deck",
        cards=STARTER_DECK_CARDS,
        tier="arcane",
    )

    deck_str = str(deck)
    assert "Test Deck" in deck_str
    assert "8 cards" in deck_str
    assert "Generators:" in deck_str
    assert "Combat:" in deck_str

