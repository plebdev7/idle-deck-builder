"""Deck management and operations."""

from collections.abc import Iterator

from pydantic import BaseModel, Field

from simulator.core.cards import Card


class Deck(BaseModel):
    """Deck model containing multiple cards.
    
    Manages card draw order, shuffling, and deck statistics.
    """

    name: str = Field(..., description="Deck name")
    cards: list[Card] = Field(..., description="Cards in deck")
    tier: str = Field("arcane", description="Primary tier")

    @property
    def size(self) -> int:
        """Total number of cards in deck."""
        return len(self.cards)

    @property
    def generator_count(self) -> int:
        """Number of generator cards."""
        return sum(1 for card in self.cards if card.is_generator)

    @property
    def combat_count(self) -> int:
        """Number of combat cards."""
        return sum(1 for card in self.cards if card.is_combat)

    @property
    def total_attack(self) -> int:
        """Sum of all attack values."""
        return sum(card.attack for card in self.cards)

    @property
    def total_defense(self) -> int:
        """Sum of all defense values."""
        return sum(card.defense for card in self.cards)

    @property
    def total_essence_rate(self) -> float:
        """Sum of all essence generation rates."""
        return sum(card.essence_rate for card in self.cards)

    @property
    def total_essence_burst(self) -> int:
        """Sum of all essence burst values."""
        return sum(card.essence_burst for card in self.cards)

    def __iter__(self) -> Iterator[Card]:
        """Iterate over cards."""
        return iter(self.cards)

    def __len__(self) -> int:
        """Deck size."""
        return self.size

    def __str__(self) -> str:
        """Human-readable deck representation."""
        return (
            f"{self.name} [{self.size} cards]\n"
            f"  Generators: {self.generator_count} | Combat: {self.combat_count}\n"
            f"  Total ATK: {self.total_attack} | DEF: {self.total_defense}\n"
            f"  Generation: {self.total_essence_rate:.1f}/sec + {self.total_essence_burst} burst"
        )

