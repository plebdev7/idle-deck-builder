"""Deck management and operations."""

from collections.abc import Iterator
from typing import Any

from pydantic import BaseModel, Field, model_validator

from simulator.core.cards import Card


class Deck(BaseModel):
    """Deck model containing multiple cards.
    
    Manages card draw order, shuffling, and deck statistics.
    
    Updated in Session 2.1.2A:
    - Default deck size limit: 12 cards (Arcane Student)
    - Validates minimum deck size (8 cards)
    - Can be configured via max_size parameter
    """

    name: str = Field(..., description="Deck name")
    cards: list[Card] = Field(..., description="Cards in deck")
    tier: str = Field("arcane", description="Primary tier")
    max_size: int = Field(12, description="Maximum deck size (default: 12 for Arcane Student)")

    @model_validator(mode="after")
    def validate_deck_size(self) -> "Deck":
        """Validate deck size constraints.
        
        - Minimum: 8 cards (required for basic gameplay)
        - Maximum: Configurable (default 12 for Arcane Student)
        """
        if len(self.cards) < 8:
            raise ValueError(f"Deck must have at least 8 cards (has {len(self.cards)})")
        
        if len(self.cards) > self.max_size:
            raise ValueError(
                f"Deck exceeds maximum size ({len(self.cards)} > {self.max_size})"
            )
        
        return self

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

