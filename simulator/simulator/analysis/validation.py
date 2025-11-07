"""Baseline validation against DESIGN.md Session 1.3 targets.

Validates:
- Pack timing (8-9 min, 16-17 min, 26-27 min)
- Essence rate progression (0 -> 180 -> 652 -> 1,252 Essence/sec)
- Card draw rates (60 cards/min)
- Enemy defeat rates (5 enemies/min)
"""

from dataclasses import dataclass

from simulator.core.cards import STARTER_DECK_CARDS
from simulator.core.combat import CombatSimulator
from simulator.core.deck import Deck


@dataclass
class ValidationTarget:
    """Expected value with tolerance."""

    name: str
    expected: float
    tolerance: float  # Percentage tolerance (e.g., 0.1 = 10%)
    unit: str = ""

    def check(self, actual: float) -> tuple[bool, str]:
        """Check if actual value is within tolerance.
        
        Returns:
            (passed, message) tuple
        """
        lower = self.expected * (1 - self.tolerance)
        upper = self.expected * (1 + self.tolerance)
        passed = lower <= actual <= upper

        if self.unit:
            unit_str = f" {self.unit}"
        else:
            unit_str = ""

        # Use ASCII-safe symbols for Windows compatibility
        check_symbol = "[PASS]" if passed else "[FAIL]"
        
        if passed:
            msg = f"{check_symbol} {self.name}: {actual:.2f}{unit_str} (expected {self.expected:.2f}{unit_str}, +/-{self.tolerance*100:.0f}%)"
        else:
            msg = f"{check_symbol} {self.name}: {actual:.2f}{unit_str} (expected {self.expected:.2f}{unit_str}, +/-{self.tolerance*100:.0f}%)"

        return passed, msg


class BaselineValidator:
    """Validates simulation results against DESIGN.md baseline targets."""

    def __init__(self) -> None:
        """Initialize validator with baseline targets.
        
        NOTE: These targets are for STARTER DECK ONLY progression.
        This establishes the "bad player" baseline (no pack purchases).
        "Good player" progression with Pack 1-3 cards will be designed in Task 2.1+.
        """
        # Pack timing targets - STARTER DECK ONLY (revised Task 2.0)
        # Based on actual starter deck generation rates (3.0 Essence/sec per cycle)
        self.pack_timing_targets = [
            ValidationTarget("Pack 1 Timing", expected=7.0, tolerance=0.15, unit="min"),  # ~7 min
            ValidationTarget("Pack 2 Timing", expected=11.5, tolerance=0.15, unit="min"),  # ~11.5 min
            ValidationTarget("Pack 3 Timing", expected=18.5, tolerance=0.15, unit="min"),  # ~18.5 min
        ]

        # Essence rate targets - STARTER DECK ONLY (revised Task 2.0)
        # Linear accumulation: 3.0 Essence/sec per cycle, 7.5 cycles/min
        # Formula: (minutes * 60 cards) / 8 cards * 3.0 Essence/sec
        self.essence_rate_targets = [
            ValidationTarget("Rate at 8 min", expected=180, tolerance=0.10, unit="Essence/sec"),   # 60 cycles
            ValidationTarget("Rate at 17 min", expected=382, tolerance=0.10, unit="Essence/sec"),  # 127.5 cycles
            ValidationTarget("Rate at 27 min", expected=607, tolerance=0.10, unit="Essence/sec"),  # 202.5 cycles
        ]

        # Gameplay rate targets (DESIGN.md lines 934-936)
        self.gameplay_targets = [
            ValidationTarget("Card Draw Rate", expected=60.0, tolerance=0.05, unit="cards/min"),
            ValidationTarget("Enemy Defeat Rate", expected=5.0, tolerance=0.10, unit="enemies/min"),
        ]

    def validate_simulation(self, results: dict, verbose: bool = True) -> dict:
        """Validate simulation results against all targets.
        
        Args:
            results: Simulation results from CombatSimulator.simulate()
            verbose: If True, print detailed validation messages
            
        Returns:
            Validation report dictionary
        """
        validation_report = {
            "overall_passed": True,
            "pack_timing": [],
            "essence_rates": [],
            "gameplay_rates": [],
            "summary": {},
        }

        # Validate pack timing
        if verbose:
            print("\n=== Pack Timing Validation ===")

        pack_times = results.get("pack_affordable_times", {})
        for i, target in enumerate(self.pack_timing_targets, 1):
            actual = pack_times.get(i, float("inf"))
            passed, msg = target.check(actual)

            if verbose:
                print(msg)

            validation_report["pack_timing"].append({
                "pack_number": i,
                "target": target.expected,
                "actual": actual,
                "passed": passed,
                "message": msg,
            })

            if not passed:
                validation_report["overall_passed"] = False

        # Validate essence rates at key times
        if verbose:
            print("\n=== Essence Rate Validation ===")

        # Find states closest to target times
        state_history = results.get("state_history", [])
        target_times = [8, 17, 27]  # minutes

        for i, target_min in enumerate(target_times):
            target_sec = target_min * 60

            # Find closest state
            closest_state = min(
                state_history,
                key=lambda s: abs(s["time"] - target_sec),
                default=None,
            )

            if closest_state:
                actual_rate = closest_state["essence_rate"]
                passed, msg = self.essence_rate_targets[i].check(actual_rate)

                if verbose:
                    print(msg)

                validation_report["essence_rates"].append({
                    "time_minutes": target_min,
                    "target": self.essence_rate_targets[i].expected,
                    "actual": actual_rate,
                    "passed": passed,
                    "message": msg,
                })

                if not passed:
                    validation_report["overall_passed"] = False

        # Validate gameplay rates
        if verbose:
            print("\n=== Gameplay Rate Validation ===")

        duration_min = results.get("duration_minutes", 1.0)

        # Card draw rate
        actual_draw_rate = results["cards_drawn"] / duration_min
        passed, msg = self.gameplay_targets[0].check(actual_draw_rate)

        if verbose:
            print(msg)

        validation_report["gameplay_rates"].append({
            "metric": "card_draw_rate",
            "target": self.gameplay_targets[0].expected,
            "actual": actual_draw_rate,
            "passed": passed,
            "message": msg,
        })

        if not passed:
            validation_report["overall_passed"] = False

        # Enemy defeat rate
        actual_defeat_rate = results["enemies_defeated"] / duration_min
        passed, msg = self.gameplay_targets[1].check(actual_defeat_rate)

        if verbose:
            print(msg)

        validation_report["gameplay_rates"].append({
            "metric": "enemy_defeat_rate",
            "target": self.gameplay_targets[1].expected,
            "actual": actual_defeat_rate,
            "passed": passed,
            "message": msg,
        })

        if not passed:
            validation_report["overall_passed"] = False

        # Summary
        total_checks = (
            len(validation_report["pack_timing"])
            + len(validation_report["essence_rates"])
            + len(validation_report["gameplay_rates"])
        )
        passed_checks = sum(
            item["passed"]
            for category in ["pack_timing", "essence_rates", "gameplay_rates"]
            for item in validation_report[category]
        )

        validation_report["summary"] = {
            "total_checks": total_checks,
            "passed_checks": passed_checks,
            "failed_checks": total_checks - passed_checks,
            "pass_rate": passed_checks / total_checks if total_checks > 0 else 0,
        }

        if verbose:
            print("\n=== Validation Summary ===")
            print(f"Total Checks: {total_checks}")
            print(f"Passed: {passed_checks}")
            print(f"Failed: {total_checks - passed_checks}")
            print(f"Pass Rate: {validation_report['summary']['pass_rate']*100:.1f}%")
            
            # ASCII-safe status
            status = "PASSED" if validation_report['overall_passed'] else "FAILED"
            print(f"\nOverall: {status}")

        return validation_report


def run_baseline_validation(duration_minutes: float = 30.0, verbose: bool = True) -> dict:
    """Run full baseline validation with starter deck.
    
    Args:
        duration_minutes: Simulation duration (default 30 min to test all 3 packs)
        verbose: Print detailed output
        
    Returns:
        Validation report dictionary
    """
    if verbose:
        print("=" * 60)
        print("BASELINE VALIDATION - DESIGN.md Session 1.3")
        print("=" * 60)
        print(f"\nRunning {duration_minutes} minute simulation with starter deck...")

    # Create starter deck
    deck = Deck(name="Starter Deck", cards=STARTER_DECK_CARDS, tier="arcane")

    if verbose:
        print(f"\nDeck: {deck.name}")
        print(f"  Cards: {deck.size}")
        print(f"  Generators: {deck.generator_count}")
        print(f"  Combat: {deck.combat_count}")
        print(f"  Total Rate: {deck.total_essence_rate}/sec")
        print(f"  Total Burst: {deck.total_essence_burst}")

    # Run simulation
    sim = CombatSimulator()
    results = sim.simulate(duration_minutes=duration_minutes, deck=deck)

    if verbose:
        print(f"\nSimulation Complete!")
        print(f"  Duration: {results['duration_minutes']:.1f} minutes")
        print(f"  Final Essence: {results['final_essence']:,.0f}")
        print(f"  Final Rate: {results['final_essence_rate']:.1f} Essence/sec")
        print(f"  Cards Drawn: {results['cards_drawn']}")
        print(f"  Enemies Defeated: {results['enemies_defeated']}/{results['enemies_encountered']}")

    # Validate results
    validator = BaselineValidator()
    report = validator.validate_simulation(results, verbose=verbose)

    return report


if __name__ == "__main__":
    # Run validation when executed directly
    report = run_baseline_validation(duration_minutes=30.0, verbose=True)

    # Exit with error code if validation failed
    import sys

    sys.exit(0 if report["overall_passed"] else 1)


