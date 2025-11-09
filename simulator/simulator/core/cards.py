"""Card models and definitions using Pydantic."""

import json
from enum import Enum
from pathlib import Path
from typing import Any

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
        essence_burst=250,  # Buffed from 150 in Session 2.1.2A
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
        defense=20,  # Buffed from 18 in Session 2.1.2A
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


def load_cards_from_json(json_path: str | Path) -> list[Card]:
    """Load cards from JSON file.
    
    Args:
        json_path: Path to JSON file containing card definitions
        
    Returns:
        List of Card instances
        
    Raises:
        FileNotFoundError: If JSON file doesn't exist
        ValueError: If JSON is malformed or cards don't validate
        
    Example:
        >>> cards = load_cards_from_json("game-data/cards-starter-deck.json")
        >>> len(cards)
        8
    """
    path = Path(json_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Card JSON file not found: {path}")
    
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Handle both single object and array of objects
    if isinstance(data, dict):
        if "cards" in data:
            cards_data = data["cards"]
        else:
            raise ValueError(f"Expected 'cards' key in JSON, got: {list(data.keys())}")
    elif isinstance(data, list):
        cards_data = data
    else:
        raise ValueError(f"Expected dict or list in JSON, got: {type(data)}")
    
    # Parse each card
    cards = []
    for card_data in cards_data:
        try:
            # Convert JSON format to Card model format
            card_dict = _convert_json_to_card_format(card_data)
            card = Card(**card_dict)
            cards.append(card)
        except Exception as e:
            raise ValueError(f"Failed to parse card {card_data.get('id', 'unknown')}: {e}") from e
    
    return cards


def _convert_json_to_card_format(json_card: dict[str, Any]) -> dict[str, Any]:
    """Convert JSON card format to Card model format.
    
    JSON format uses "type" and "effects" arrays.
    Card model uses flat fields like attack, defense, essence_rate, etc.
    
    Args:
        json_card: Card data from JSON file
        
    Returns:
        Dictionary suitable for Card(**dict)
    """
    card_dict = {
        "id": json_card["id"],
        "name": json_card["name"],
        "description": json_card.get("flavor_text", ""),
        "tier": json_card["tier"].lower(),
        "rarity": json_card["rarity"].lower(),
        "level": json_card.get("level", 1),
        "cost": json_card.get("cost", 0),
    }
    
    # Convert "type" field to card_type and generator_type
    card_type_str = json_card.get("type", "Combat").lower()
    if card_type_str == "generator":
        card_dict["card_type"] = CardType.GENERATOR
        # Determine generator type based on effects
        card_dict["generator_type"] = _determine_generator_type(json_card.get("effects", []))
    elif card_type_str == "hybrid":
        card_dict["card_type"] = CardType.HYBRID
        card_dict["generator_type"] = GeneratorType.HYBRID
    elif card_type_str == "utility":
        card_dict["card_type"] = CardType.UTILITY
        card_dict["generator_type"] = None
    else:  # Combat
        card_dict["card_type"] = CardType.COMBAT
        card_dict["generator_type"] = None
    
    # Parse effects into flat stats
    attack = 0
    defense = 0
    essence_rate = 0.0
    essence_burst = 0
    
    for effect in json_card.get("effects", []):
        effect_type = effect.get("effect_type", "")
        value = effect.get("value", 0)
        
        if effect_type == "add_attack":
            attack += value
        elif effect_type == "add_defense":
            defense += value
        elif effect_type == "essence_per_sec":
            essence_rate += value
        elif effect_type == "essence_flat":
            essence_burst += value
    
    card_dict["attack"] = attack
    card_dict["defense"] = defense
    card_dict["essence_rate"] = essence_rate
    card_dict["essence_burst"] = essence_burst
    
    return card_dict


def _determine_generator_type(effects: list[dict[str, Any]]) -> GeneratorType:
    """Determine generator subtype based on effects.
    
    Args:
        effects: List of effect dictionaries
        
    Returns:
        GeneratorType enum value
    """
    has_rate = any(e.get("effect_type") == "essence_per_sec" for e in effects)
    has_burst = any(e.get("effect_type") == "essence_flat" for e in effects)
    has_combat = any(e.get("effect_type") in ["add_attack", "add_defense"] for e in effects)
    
    if has_rate and has_combat:
        return GeneratorType.HYBRID
    elif has_rate:
        return GeneratorType.RATE
    elif has_burst:
        return GeneratorType.BURST
    else:
        return GeneratorType.RATE  # Default



def get_game_data_path() -> Path:
    """Get path to game-data directory.
    
    Returns:
        Path to game-data directory (relative to project root)
    """
    # Assuming simulator is at project_root/simulator/simulator/
    # Game data is at project_root/game-data/
    current_file = Path(__file__)  # .../simulator/simulator/core/cards.py
    project_root = current_file.parent.parent.parent.parent  # Go up 4 levels
    return project_root / "game-data"


def load_starter_deck_from_json() -> list[Card]:
    """Load starter deck from game-data/cards-starter-deck.json.
    
    Falls back to STARTER_DECK_CARDS constant if JSON not found.
    
    Returns:
        List of starter deck Card instances
    """
    try:
        game_data_path = get_game_data_path()
        json_path = game_data_path / "cards-starter-deck.json"
        return load_cards_from_json(json_path)
    except FileNotFoundError:
        # Fall back to hardcoded cards
        return list(STARTER_DECK_CARDS)


def load_balance_config() -> dict[str, Any]:
    """Load balance configuration from game-data/balance-config.json.
    
    Returns:
        Balance configuration dictionary
        
    Raises:
        FileNotFoundError: If balance config file doesn't exist
    """
    game_data_path = get_game_data_path()
    config_path = game_data_path / "balance-config.json"
    
    if not config_path.exists():
        raise FileNotFoundError(f"Balance config not found: {config_path}")
    
    with config_path.open("r", encoding="utf-8") as f:
        return json.load(f)


