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
    MULTIPLIER = "multiplier"  # +(Current rate * Y seconds)
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


# Starter deck cards from DESIGN.md Session 1.3C (lines 1067-1125)
STARTER_DECK_CARDS = [
    # Generator Cards (3 cards)
    Card(
        id="starter_gen_rate",
        name="Arcane Conduit",
        description="A stable channel of pure arcane energy. Draw upon it to fuel your magic.",
        card_type=CardType.GENERATOR,
        generator_type=GeneratorType.RATE,
        essence_rate=2.0,
        tier="arcane",
    ),
    Card(
        id="starter_gen_burst",
        name="Essence Burst",
        description="A concentrated surge of magical energy, released all at once.",
        card_type=CardType.GENERATOR,
        generator_type=GeneratorType.BURST,
        essence_burst=150,
        tier="arcane",
    ),
    Card(
        id="starter_gen_hybrid",
        name="Combat Siphon",
        description="Draw power from combat itself, channeling the clash into usable essence.",
        card_type=CardType.HYBRID,
        generator_type=GeneratorType.HYBRID,
        essence_rate=1.0,
        attack=12,
        defense=6,
        tier="arcane",
    ),
    # Combat Cards (5 cards)
    Card(
        id="starter_combat_pure_attack",
        name="Arcane Bolt",
        description="A focused blast of raw magical force.",
        card_type=CardType.COMBAT,
        attack=20,
        defense=0,
        tier="arcane",
    ),
    Card(
        id="starter_combat_pure_defense",
        name="Mystic Shield",
        description="A shimmering barrier of protective magic.",
        card_type=CardType.COMBAT,
        attack=0,
        defense=18,
        tier="arcane",
    ),
    Card(
        id="starter_combat_balanced",
        name="Balanced Strike",
        description="Harmonious magic balancing offense and defense.",
        card_type=CardType.COMBAT,
        attack=10,
        defense=10,
        tier="arcane",
    ),
    Card(
        id="starter_combat_offense_leaning",
        name="Power Strike",
        description="Aggressive magic that prioritizes overwhelming force.",
        card_type=CardType.COMBAT,
        attack=15,
        defense=5,
        tier="arcane",
    ),
    Card(
        id="starter_combat_defense_leaning",
        name="Stalwart Guard",
        description="Patient, enduring magic that outlasts threats.",
        card_type=CardType.COMBAT,
        attack=5,
        defense=15,
        tier="arcane",
    ),
]

