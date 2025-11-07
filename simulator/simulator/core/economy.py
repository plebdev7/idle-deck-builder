"""Economy and resource generation logic.

Handles:
- Pack cost scaling (40,000 * 2.5^n)
- Resource accumulation
- Idle generation calculations
- Economy balance modeling

Will be fully implemented in Task 2.0+.
"""


def pack_cost(pack_number: int, base_cost: int = 40_000, multiplier: float = 2.5) -> int:
    """Calculate pack cost using exponential scaling.
    
    Formula: base_cost * multiplier^(pack_number - 1)
    
    Args:
        pack_number: Pack number (1-indexed)
        base_cost: Base cost for first pack (default: 40,000)
        multiplier: Cost multiplier per pack (default: 2.5)
        
    Returns:
        Cost for the specified pack
        
    Examples:
        >>> pack_cost(1)
        40000
        >>> pack_cost(2)
        100000
        >>> pack_cost(3)
        250000
    """
    if pack_number < 1:
        raise ValueError("pack_number must be >= 1")

    return int(base_cost * (multiplier ** (pack_number - 1)))


def cumulative_pack_cost(num_packs: int, base_cost: int = 40_000, multiplier: float = 2.5) -> int:
    """Calculate total cost for purchasing multiple packs.
    
    Args:
        num_packs: Number of packs to purchase
        base_cost: Base cost for first pack
        multiplier: Cost multiplier per pack
        
    Returns:
        Total cost for all packs
    """
    return sum(pack_cost(i, base_cost, multiplier) for i in range(1, num_packs + 1))


def time_to_pack(
    pack_number: int,
    essence_per_second: float,
    base_cost: int = 40_000,
    multiplier: float = 2.5,
) -> float:
    """Calculate time required to afford a pack.
    
    Args:
        pack_number: Pack number (1-indexed)
        essence_per_second: Current essence generation rate
        base_cost: Base pack cost
        multiplier: Cost multiplier
        
    Returns:
        Time in seconds to afford the pack
    """
    cost = pack_cost(pack_number, base_cost, multiplier)
    return cost / essence_per_second if essence_per_second > 0 else float("inf")

