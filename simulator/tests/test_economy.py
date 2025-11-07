"""Tests for economy calculations."""

import pytest

from simulator.core.economy import (
    cumulative_pack_cost,
    pack_cost,
    time_to_pack,
)


def test_pack_cost_formula() -> None:
    """Test pack cost exponential scaling."""
    # First pack: 40,000 × 2.5^0 = 40,000
    assert pack_cost(1) == 40_000

    # Second pack: 40,000 × 2.5^1 = 100,000
    assert pack_cost(2) == 100_000

    # Third pack: 40,000 × 2.5^2 = 250,000
    assert pack_cost(3) == 250_000

    # Fourth pack: 40,000 × 2.5^3 = 625,000
    assert pack_cost(4) == 625_000


def test_pack_cost_custom_params() -> None:
    """Test pack cost with custom parameters."""
    # Different base cost
    assert pack_cost(1, base_cost=10_000) == 10_000
    assert pack_cost(2, base_cost=10_000) == 25_000

    # Different multiplier
    assert pack_cost(1, multiplier=2.0) == 40_000
    assert pack_cost(2, multiplier=2.0) == 80_000


def test_pack_cost_validation() -> None:
    """Test pack cost input validation."""
    with pytest.raises(ValueError, match="pack_number must be >= 1"):
        pack_cost(0)

    with pytest.raises(ValueError, match="pack_number must be >= 1"):
        pack_cost(-1)


def test_cumulative_pack_cost() -> None:
    """Test total cost for multiple packs."""
    # First 3 packs: 40k + 100k + 250k = 390k
    assert cumulative_pack_cost(3) == 390_000

    # Just first pack
    assert cumulative_pack_cost(1) == 40_000

    # No packs
    assert cumulative_pack_cost(0) == 0


def test_time_to_pack() -> None:
    """Test time calculation for pack affordability."""
    # Pack 1 at 4 essence/sec: 40,000 / 4 = 10,000 seconds
    assert time_to_pack(1, essence_per_second=4.0) == 10_000.0

    # Pack 2 at 10 essence/sec: 100,000 / 10 = 10,000 seconds
    assert time_to_pack(2, essence_per_second=10.0) == 10_000.0

    # Zero generation rate
    assert time_to_pack(1, essence_per_second=0.0) == float("inf")

    # Very fast generation
    time = time_to_pack(1, essence_per_second=1000.0)
    assert time == 40.0  # 40,000 / 1000

