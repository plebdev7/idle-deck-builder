"""Card models and definitions using Pydantic."""

from enum import Enum

from pydantic import BaseModel, Field


class CardType(str, Enum):
    """Card type classification."""

    GENERATOR = "generator"
    COMBAT = "combat"
    HYBRID = "hybrid"
    UTILITY = "utility"


class GeneratorType(str, Enum):
    """Generator card subtypes."""

    RATE = "rate"  # +X Essence/sec
    BURST = "burst"  # +X flat Essence
    HYBRID = "hybrid"  # +X Essence/sec + combat stats
    MULTIPLIER = "multiplier"  # +(Current rate × Y seconds)
    CONDITIONAL = "conditional"  # +X if condition met


class Card(BaseModel):
    """Card model with validation.
    
    Represents a single card with all its properties.
    Immutable after creation (frozen=True).
    """

    # Identity
    id: str = Field(..., description="Unique card identifier")
    name: str = Field(..., min_length=1, description="Card name")
    description: str = Field("", description="Card description text")

    # Classification
    card_type: CardType = Field(..., description="Card type (generator, combat, etc.)")
    generator_type: GeneratorType | None = Field(
        None, description="Generator subtype (if applicable)"
    )

    # Combat Stats
    attack: int = Field(0, ge=0, description="Attack power")
    defense: int = Field(0, ge=0, description="Defense power")

    # Generator Stats
    essence_rate: float = Field(0.0, ge=0, description="Essence generation per second")
    essence_burst: int = Field(0, ge=0, description="Flat essence on draw")

    # Meta
    tier: str = Field("arcane", description="Tier (arcane, fire, water, earth, air)")
    rarity: str = Field("common", description="Rarity (common, rare, epic, legendary)")
    level: int = Field(1, ge=1, description="Card level")
    cost: int = Field(0, ge=0, description="Acquisition cost (if relevant)")

    model_config = {"frozen": True}  # Immutable

    @property
    def is_generator(self) -> bool:
        """Check if card has generation capability."""
        return self.essence_rate > 0 or self.essence_burst > 0

    @property
    def is_combat(self) -> bool:
        """Check if card has combat capability."""
        return self.attack > 0 or self.defense > 0

    @property
    def total_combat_power(self) -> int:
        """Total combat power (attack + defense)."""
        return self.attack + self.defense

    def __str__(self) -> str:
        """Human-readable card representation."""
        parts = [f"{self.name} [{self.tier.upper()}]"]

        if self.is_combat:
            parts.append(f"ATK:{self.attack} DEF:{self.defense}")

        if self.is_generator:
            if self.essence_rate > 0:
                parts.append(f"+{self.essence_rate}/sec")
            if self.essence_burst > 0:
                parts.append(f"+{self.essence_burst}")

        return " | ".join(parts)


# Starter deck cards from Session 1.3C
STARTER_DECK_CARDS = [
    Card(
        id="gen_rate_basic",
        name="Arcane Flow",
        description="Steady essence generation",
        card_type=CardType.GENERATOR,
        generator_type=GeneratorType.RATE,
        essence_rate=2.0,
        tier="arcane",
    ),
    Card(
        id="gen_burst_basic",
        name="Essence Burst",
        description="Large instant essence gain",
        card_type=CardType.GENERATOR,
        generator_type=GeneratorType.BURST,
        essence_burst=150,
        tier="arcane",
    ),
    Card(
        id="gen_hybrid_basic",
        name="Battle Mage",
        description="Generates essence while providing combat support",
        card_type=CardType.HYBRID,
        generator_type=GeneratorType.HYBRID,
        essence_rate=1.0,
        attack=12,
        defense=6,
        tier="arcane",
    ),
    Card(
        id="combat_specialist_attack",
        name="Arcane Blast",
        description="Pure offensive power",
        card_type=CardType.COMBAT,
        attack=50,
        defense=0,
        tier="arcane",
    ),
    Card(
        id="combat_specialist_defense",
        name="Mystic Shield",
        description="Pure defensive power",
        card_type=CardType.COMBAT,
        attack=0,
        defense=50,
        tier="arcane",
    ),
    Card(
        id="combat_balanced_high",
        name="Arcane Guardian",
        description="Balanced combat card",
        card_type=CardType.COMBAT,
        attack=25,
        defense=25,
        tier="arcane",
    ),
    Card(
        id="combat_balanced_mid",
        name="Spellsword",
        description="Balanced combat card",
        card_type=CardType.COMBAT,
        attack=20,
        defense=20,
        tier="arcane",
    ),
    Card(
        id="combat_attack_focused",
        name="Fire Bolt",
        description="Attack-focused combat",
        card_type=CardType.COMBAT,
        attack=35,
        defense=10,
        tier="arcane",
    ),
]

