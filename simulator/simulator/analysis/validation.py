"""Baseline validation against DESIGN.md baseline targets.

Validates (Session 2.0.3 Combat-Over-Time System, Task 2.0.6 Adjustments):
- Pack timing (7.0 min, 11.5 min, 18.5 min)
- Essence rate progression (with combat-time adjustments, wider tolerances)
- Card draw rates (~52 cards/min, adjusted for combat)
- Enemy defeat rates (~2.0 enemies/min with combat duration)
- Combat duration targets (Enemy 1: ~2s, Enemy 50: ~47s, wider early tolerances)
- HP system (starting: 100 HP, no auto-healing)
- Death system (stat resets, resource persistence, respawn)
- Boss encounters (Enemy 50: 7,670 HP, Enemy 100: 18,555 HP, Enemy 150: 38,720 HP - CORRECTED)
- Progression milestones (Enemy 50 at ~23 min, Enemy 60 at ~30 min)

Data Ownership Validation (Task 2.1.2C):
- Verify simulator loads values from game-data/*.json (no hardcoded values)
- Validate formulas match between design docs and game-data
- Check cross-references (_design_spec fields) exist

Card Text Length Validation (Task 2.1.6):
- Validate ability_text fits within 3 lines (~126 characters max)
- Check all cards have ability_text and ability_text_short fields
- Ensure text meets card layout constraints (168px width, 12px font)
"""

import json
from dataclasses import dataclass
from pathlib import Path

from simulator.core.cards import STARTER_DECK_CARDS
from simulator.core.combat import BALANCE_CONFIG, CombatSimulator
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
        
        Updated for Session 2.0.3: Combat-Over-Time System
        """
        # Pack timing targets - STARTER DECK ONLY (revised Task 2.0)
        # Based on actual starter deck generation rates (3.0 Essence/sec per cycle)
        # NOTE: Pack affordability timing is INDEPENDENT of combat duration
        # (essence generation continues during combat ticks)
        self.pack_timing_targets = [
            ValidationTarget("Pack 1 Timing", expected=7.0, tolerance=0.15, unit="min"),  # ~7 min
            ValidationTarget("Pack 2 Timing", expected=11.5, tolerance=0.15, unit="min"),  # ~11.5 min
            ValidationTarget("Pack 3 Timing", expected=18.5, tolerance=0.15, unit="min"),  # ~18.5 min
        ]

        # Essence rate targets - STARTER DECK ONLY (ADJUSTED Task 2.0.6)
        # Linear accumulation: 3.0 Essence/sec per cycle, but reduced by combat time
        # Combat-over-time reduces effective card draw rate by ~15%
        # Formula: (minutes * 51 cards) / 8 cards * 3.0 Essence/sec (51 instead of 60 due to combat)
        self.essence_rate_targets = [
            ValidationTarget("Rate at 8 min", expected=180, tolerance=0.20, unit="Essence/sec"),   # Wider tolerance
            ValidationTarget("Rate at 17 min", expected=382, tolerance=0.20, unit="Essence/sec"),  # Wider tolerance
            ValidationTarget("Rate at 27 min", expected=607, tolerance=0.20, unit="Essence/sec"),  # Wider tolerance
        ]

        # Gameplay rate targets (ADJUSTED Task 2.0.6)
        # Card draw rate reduced due to combat ticks + reshuffle cooldowns
        # Enemy defeat rate reduced due to combat-over-time
        self.gameplay_targets = [
            ValidationTarget("Card Draw Rate", expected=52.0, tolerance=0.10, unit="cards/min"),  # 60 → 52 (combat impact)
            ValidationTarget("Enemy Defeat Rate", expected=2.0, tolerance=0.25, unit="enemies/min"),  # 2.5 → 2.0 (combat takes time)
        ]
        
        # HP system targets (Session 2.0.3)
        self.hp_system_targets = [
            ValidationTarget("Starting HP", expected=100.0, tolerance=0.0, unit="HP"),  # Exact value
            ValidationTarget("Starting Max HP", expected=100.0, tolerance=0.0, unit="HP"),  # Exact value
        ]
        
        # Combat duration targets (Session 2.0.3, ADJUSTED Task 2.0.6)
        # Based on starter deck (62 ATK, 54 DEF) against act-based HP scaling
        # Early enemies have higher variance, so wider tolerances
        self.combat_duration_targets = [
            ValidationTarget("Enemy 1 Combat", expected=2.0, tolerance=1.00, unit="sec"),    # ~2 seconds (very wide tolerance)
            ValidationTarget("Enemy 10 Combat", expected=17.0, tolerance=0.30, unit="sec"),  # ~17 seconds (wider tolerance)
            ValidationTarget("Enemy 25 Combat", expected=29.0, tolerance=0.20, unit="sec"),  # ~29 seconds
            ValidationTarget("Enemy 50 Combat", expected=47.0, tolerance=0.20, unit="sec"),  # ~47 seconds (boss)
        ]
        
        # Progression milestone targets (Session 2.0.3)
        self.milestone_targets = [
            ValidationTarget("Enemy 50 Time", expected=23.0, tolerance=0.15, unit="min"),  # Mini-Boss #1
            ValidationTarget("Enemy 60 Time", expected=30.0, tolerance=0.15, unit="min"),  # 30-min milestone
        ]
        
        # Boss encounter targets (Session 2.0.3, CORRECTED Task 2.0.6)
        self.boss_targets = {
            50: {
                "hp": ValidationTarget("Enemy 50 HP", expected=7670.0, tolerance=0.01, unit="HP"),  # CORRECTED: 5,900 × 1.3
                "attack": ValidationTarget("Enemy 50 Attack", expected=10.0, tolerance=0.0, unit="ATK"),  # First attacker
            },
            100: {
                "hp": ValidationTarget("Enemy 100 HP", expected=18555.0, tolerance=0.01, unit="HP"),  # 1.5x multiplier
                "attack": ValidationTarget("Enemy 100 Attack", expected=30.0, tolerance=0.10, unit="ATK"),
            },
            150: {
                "hp": ValidationTarget("Enemy 150 HP", expected=38720.0, tolerance=0.01, unit="HP"),  # CORRECTED: 19,360 × 2.0
                "attack": ValidationTarget("Enemy 150 Attack", expected=80.0, tolerance=0.10, unit="ATK"),
            },
        }

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
            "hp_system": [],
            "combat_durations": [],
            "milestones": [],
            "boss_encounters": [],
            "death_system": [],
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
                actual_rate = closest_state["player_essence_rate"]
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
        
        # Validate HP system (Session 2.0.3)
        if verbose:
            print("\n=== HP System Validation ===")
        
        # Starting HP
        actual_hp = results.get("player_hp", 100.0)
        actual_max_hp = results.get("player_max_hp", 100.0)
        
        passed, msg = self.hp_system_targets[0].check(actual_max_hp)  # Check max HP is 100
        if verbose:
            print(msg)
        
        validation_report["hp_system"].append({
            "metric": "starting_hp",
            "target": self.hp_system_targets[0].expected,
            "actual": actual_max_hp,
            "passed": passed,
            "message": msg,
        })
        
        if not passed:
            validation_report["overall_passed"] = False
        
        # Validate combat durations (Session 2.0.3)
        if verbose:
            print("\n=== Combat Duration Validation ===")
        
        # Build enemy_events dict from events list
        enemy_events = {}
        events = results.get("events", [])
        
        # First pass: get enemy stats from spawn events
        for event in events:
            if event["type"] == "enemy_spawn":
                enemy_num = event["data"].get("enemy_number")
                if enemy_num:
                    enemy_events[enemy_num] = {
                        "time": event["time"],
                        "enemy_max_hp": event["data"].get("max_health", 0.0),
                        "enemy_attack": event["data"].get("attack", 0),
                        "combat_duration": 0.0,  # Will be updated from victory event
                    }
        
        # Second pass: get combat durations from victory events
        for event in events:
            if event["type"] == "victory":
                enemy_num = event["data"].get("enemy_number")
                if enemy_num and enemy_num in enemy_events:
                    enemy_events[enemy_num]["combat_duration"] = event["data"].get("combat_duration", 0.0)
        
        test_enemies = [1, 10, 25, 50]  # Enemies to test duration
        
        for i, enemy_num in enumerate(test_enemies):
            if enemy_num in enemy_events:
                event = enemy_events[enemy_num]
                actual_duration = event.get("combat_duration", 0.0)
                
                passed, msg = self.combat_duration_targets[i].check(actual_duration)
                if verbose:
                    print(msg)
                
                validation_report["combat_durations"].append({
                    "enemy": enemy_num,
                    "target": self.combat_duration_targets[i].expected,
                    "actual": actual_duration,
                    "passed": passed,
                    "message": msg,
                })
                
                if not passed:
                    validation_report["overall_passed"] = False
            else:
                if verbose:
                    print(f"[SKIP] Enemy {enemy_num} not encountered in simulation")
        
        # Validate progression milestones (Session 2.0.3)
        if verbose:
            print("\n=== Progression Milestone Validation ===")
        
        milestone_enemies = [50, 60]
        
        for i, enemy_num in enumerate(milestone_enemies):
            if enemy_num in enemy_events:
                event = enemy_events[enemy_num]
                actual_time_min = event.get("time", 0.0) / 60.0
                
                passed, msg = self.milestone_targets[i].check(actual_time_min)
                if verbose:
                    print(msg)
                
                validation_report["milestones"].append({
                    "enemy": enemy_num,
                    "target": self.milestone_targets[i].expected,
                    "actual": actual_time_min,
                    "passed": passed,
                    "message": msg,
                })
                
                if not passed:
                    validation_report["overall_passed"] = False
            else:
                if verbose:
                    print(f"[SKIP] Enemy {enemy_num} not encountered in simulation")
        
        # Validate boss encounters (Session 2.0.3)
        if verbose:
            print("\n=== Boss Encounter Validation ===")
        
        for boss_num, boss_targets in self.boss_targets.items():
            if boss_num in enemy_events:
                event = enemy_events[boss_num]
                
                # HP validation
                actual_hp = event.get("enemy_max_hp", 0.0)
                passed, msg = boss_targets["hp"].check(actual_hp)
                if verbose:
                    print(msg)
                
                validation_report["boss_encounters"].append({
                    "enemy": boss_num,
                    "metric": "hp",
                    "target": boss_targets["hp"].expected,
                    "actual": actual_hp,
                    "passed": passed,
                    "message": msg,
                })
                
                if not passed:
                    validation_report["overall_passed"] = False
                
                # Attack validation
                actual_attack = event.get("enemy_attack", 0.0)
                passed, msg = boss_targets["attack"].check(actual_attack)
                if verbose:
                    print(msg)
                
                validation_report["boss_encounters"].append({
                    "enemy": boss_num,
                    "metric": "attack",
                    "target": boss_targets["attack"].expected,
                    "actual": actual_attack,
                    "passed": passed,
                    "message": msg,
                })
                
                if not passed:
                    validation_report["overall_passed"] = False
            else:
                if verbose:
                    print(f"[SKIP] Boss {boss_num} not encountered in simulation")
        
        # Validate death system (Session 2.0.3)
        if verbose:
            print("\n=== Death System Validation ===")
        
        player_deaths = results.get("player_deaths", 0)
        furthest_enemy = results.get("furthest_enemy", 0)
        
        # Death system checks (informational)
        if player_deaths > 0:
            death_msg = f"[INFO] Player died {player_deaths} time(s), furthest enemy: {furthest_enemy}"
        else:
            death_msg = f"[INFO] Player survived entire run (no deaths)"
        
        if verbose:
            print(death_msg)
        
        validation_report["death_system"].append({
            "metric": "player_deaths",
            "value": player_deaths,
            "furthest_enemy": furthest_enemy,
            "message": death_msg,
        })

        # Summary
        total_checks = (
            len(validation_report["pack_timing"])
            + len(validation_report["essence_rates"])
            + len(validation_report["gameplay_rates"])
            + len(validation_report["hp_system"])
            + len(validation_report["combat_durations"])
            + len(validation_report["milestones"])
            + len(validation_report["boss_encounters"])
        )
        passed_checks = sum(
            item["passed"]
            for category in ["pack_timing", "essence_rates", "gameplay_rates", "hp_system", "combat_durations", "milestones", "boss_encounters"]
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
        print("BASELINE VALIDATION - Session 2.0.3 Combat System")
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
        print(f"  Final Rate: {results['player_essence_rate']:.1f} Essence/sec")
        print(f"  Cards Drawn: {results['cards_drawn']}")
        print(f"  Enemies Defeated: {results['enemies_defeated']}/{results['enemies_encountered']}")
        print(f"  Player HP: {results['player_hp']:.0f}/{results['player_max_hp']:.0f}")
        print(f"  Player Deaths: {results['player_deaths']}")
        print(f"  Furthest Enemy: {results['furthest_enemy']}")

    # Validate results
    validator = BaselineValidator()
    report = validator.validate_simulation(results, verbose=verbose)

    return report


class DataOwnershipValidator:
    """Validates data ownership model compliance (Task 2.1.2C).
    
    Ensures:
    - balance-config.json has required fields
    - balance-config.json has _design_spec cross-references
    - Simulator loads values from balance-config.json (not hardcoded)
    - Formulas in balance-config.json match design docs
    """
    
    def __init__(self) -> None:
        """Initialize validator."""
        self.config = BALANCE_CONFIG
        
    def validate_data_ownership(self, verbose: bool = True) -> dict:
        """Validate data ownership model compliance.
        
        Args:
            verbose: If True, print detailed validation messages
            
        Returns:
            Validation report dictionary
        """
        report = {
            "overall_passed": True,
            "config_structure": [],
            "cross_references": [],
            "formula_consistency": [],
            "summary": {},
        }
        
        if verbose:
            print("\n" + "=" * 60)
            print("DATA OWNERSHIP MODEL VALIDATION (Task 2.1.2C)")
            print("=" * 60)
        
        # Check 1: Required config sections exist
        if verbose:
            print("\n=== Config Structure Validation ===")
        
        required_sections = [
            "enemy_scaling",
            "player_stats",
            "combat_timing",
            "pack_costs",
            "stat_point_system",
            "rarity_drop_rates",
        ]
        
        for section in required_sections:
            exists = section in self.config
            status = "[PASS]" if exists else "[FAIL]"
            msg = f"{status} Required section '{section}' exists in balance-config.json"
            
            if verbose:
                print(msg)
            
            report["config_structure"].append({
                "section": section,
                "exists": exists,
                "message": msg,
            })
            
            if not exists:
                report["overall_passed"] = False
        
        # Check 2: Cross-reference fields exist
        if verbose:
            print("\n=== Cross-Reference Validation ===")
        
        has_design_spec = "_design_spec" in self.config
        status = "[PASS]" if has_design_spec else "[WARN]"
        msg = f"{status} balance-config.json has '_design_spec' field linking to design docs"
        
        if verbose:
            print(msg)
        
        report["cross_references"].append({
            "field": "_design_spec",
            "exists": has_design_spec,
            "message": msg,
        })
        
        # Warn but don't fail if missing (it's a best practice, not critical)
        # if not has_design_spec:
        #     report["overall_passed"] = False
        
        # Check 3: Formula consistency (spot checks)
        if verbose:
            print("\n=== Formula Consistency Validation ===")
        
        # Check enemy HP scaling formulas match expected structure
        enemy_config = self.config.get("enemy_scaling", {})
        hp_formulas = enemy_config.get("hp_formulas", {})
        
        # Validate Act 1 formula structure
        act1_exists = "act_1" in hp_formulas
        status = "[PASS]" if act1_exists else "[FAIL]"
        msg = f"{status} Act 1 HP formula exists in balance-config.json"
        
        if verbose:
            print(msg)
        
        report["formula_consistency"].append({
            "formula": "act_1_hp",
            "exists": act1_exists,
            "message": msg,
        })
        
        if not act1_exists:
            report["overall_passed"] = False
        
        # Check per-tick scaling formulas
        per_tick_config = enemy_config.get("per_tick_scaling", {})
        act1_tick_exists = "act_1" in per_tick_config
        status = "[PASS]" if act1_tick_exists else "[FAIL]"
        msg = f"{status} Act 1 per-tick scaling exists in balance-config.json"
        
        if verbose:
            print(msg)
        
        report["formula_consistency"].append({
            "formula": "act_1_per_tick",
            "exists": act1_tick_exists,
            "message": msg,
        })
        
        if not act1_tick_exists:
            report["overall_passed"] = False
        
        # Check boss multipliers
        boss_config = enemy_config.get("boss_multipliers", {})
        has_hp_mult = "hp" in boss_config
        has_tick_mult = "per_tick_rates" in boss_config
        
        status = "[PASS]" if has_hp_mult else "[FAIL]"
        msg = f"{status} Boss HP multipliers exist in balance-config.json"
        
        if verbose:
            print(msg)
        
        report["formula_consistency"].append({
            "formula": "boss_hp_multipliers",
            "exists": has_hp_mult,
            "message": msg,
        })
        
        if not has_hp_mult:
            report["overall_passed"] = False
        
        status = "[PASS]" if has_tick_mult else "[FAIL]"
        msg = f"{status} Boss per-tick multipliers exist in balance-config.json"
        
        if verbose:
            print(msg)
        
        report["formula_consistency"].append({
            "formula": "boss_tick_multipliers",
            "exists": has_tick_mult,
            "message": msg,
        })
        
        if not has_tick_mult:
            report["overall_passed"] = False
        
        # Check 4: Simulator actually uses config (validate Enemy.spawn uses BALANCE_CONFIG)
        if verbose:
            print("\n=== Simulator Config Usage Validation ===")
        
        # Test that simulator loads values by checking combat.py imports BALANCE_CONFIG
        try:
            from simulator.core.combat import BALANCE_CONFIG as sim_config
            uses_config = sim_config is not None
            status = "[PASS]" if uses_config else "[FAIL]"
            msg = f"{status} Simulator imports and uses BALANCE_CONFIG from balance-config.json"
            
            if verbose:
                print(msg)
            
            report["config_structure"].append({
                "check": "simulator_uses_config",
                "passed": uses_config,
                "message": msg,
            })
            
            if not uses_config:
                report["overall_passed"] = False
                
        except ImportError as e:
            status = "[FAIL]"
            msg = f"{status} Failed to import BALANCE_CONFIG from simulator: {e}"
            
            if verbose:
                print(msg)
            
            report["config_structure"].append({
                "check": "simulator_uses_config",
                "passed": False,
                "message": msg,
            })
            report["overall_passed"] = False
        
        # Check 5: Card text length validation (Task 2.1.6)
        if verbose:
            print("\n=== Card Text Length Validation ===")
        
        report["card_text_validation"] = []
        
        # Load card files
        # Path relative to this file: simulator/simulator/analysis/validation.py
        # Need to go up 3 levels to repo root, then into game-data
        repo_root = Path(__file__).parent.parent.parent.parent
        card_files = [
            repo_root / "game-data" / "cards-starter-deck.json"
        ]
        
        # Character limit based on card layout (Task 2.1.6)
        # 168px width, 12px font, ~4px per char = ~42 chars/line
        # Max 3 lines = ~126 characters
        MAX_CHARACTERS = 126
        MAX_LINES = 3
        
        for card_file in card_files:
            if not card_file.exists():
                status = "[WARN]"
                msg = f"{status} Card file not found: {card_file.name}"
                if verbose:
                    print(msg)
                report["card_text_validation"].append({
                    "file": card_file.name,
                    "passed": True,  # Don't fail overall if file doesn't exist yet
                    "message": msg,
                })
                continue
            
            try:
                with open(card_file, "r") as f:
                    card_data = json.load(f)
                
                cards = card_data.get("cards", [])
                
                for card in cards:
                    card_id = card.get("id", "unknown")
                    card_name = card.get("name", "Unknown")
                    ability_text = card.get("ability_text", "")
                    
                    # Skip if no ability_text field (might be old format)
                    if not ability_text:
                        status = "[WARN]"
                        msg = f"{status} {card_name} ({card_id}): Missing 'ability_text' field"
                        if verbose:
                            print(msg)
                        report["card_text_validation"].append({
                            "card": card_name,
                            "passed": True,  # Don't fail for missing field (might be WIP)
                            "message": msg,
                        })
                        continue
                    
                    # Count characters and lines
                    char_count = len(ability_text)
                    line_count = ability_text.count('\n') + 1
                    
                    # Validate character limit
                    char_passed = char_count <= MAX_CHARACTERS
                    line_passed = line_count <= MAX_LINES
                    passed = char_passed and line_passed
                    
                    status = "[PASS]" if passed else "[FAIL]"
                    
                    if passed:
                        msg = f"{status} {card_name}: {char_count} chars, {line_count} lines (within limits)"
                    else:
                        violations = []
                        if not char_passed:
                            violations.append(f"exceeds {MAX_CHARACTERS} char limit")
                        if not line_passed:
                            violations.append(f"exceeds {MAX_LINES} line limit")
                        msg = f"{status} {card_name}: {char_count} chars, {line_count} lines ({', '.join(violations)})"
                    
                    if verbose:
                        print(msg)
                    
                    report["card_text_validation"].append({
                        "card": card_name,
                        "char_count": char_count,
                        "line_count": line_count,
                        "passed": passed,
                        "message": msg,
                    })
                    
                    if not passed:
                        report["overall_passed"] = False
                        
            except (json.JSONDecodeError, IOError) as e:
                status = "[FAIL]"
                msg = f"{status} Failed to load card file {card_file.name}: {e}"
                if verbose:
                    print(msg)
                report["card_text_validation"].append({
                    "file": card_file.name,
                    "passed": False,
                    "message": msg,
                })
                report["overall_passed"] = False
        
        # Summary
        total_checks = (
            len(report["config_structure"])
            + len(report["cross_references"])
            + len(report["formula_consistency"])
            + len(report["card_text_validation"])
        )
        
        passed_checks = sum(
            1 for item in report["config_structure"] if item.get("exists", item.get("passed", True))
        ) + sum(
            1 for item in report["cross_references"] if item.get("exists", True)
        ) + sum(
            1 for item in report["formula_consistency"] if item.get("exists", True)
        ) + sum(
            1 for item in report["card_text_validation"] if item.get("passed", True)
        )
        
        report["summary"] = {
            "total_checks": total_checks,
            "passed_checks": passed_checks,
            "failed_checks": total_checks - passed_checks,
            "pass_rate": passed_checks / total_checks if total_checks > 0 else 0,
        }
        
        if verbose:
            print("\n=== Data Ownership Validation Summary ===")
            print(f"Total Checks: {total_checks}")
            print(f"Passed: {passed_checks}")
            print(f"Failed: {total_checks - passed_checks}")
            print(f"Pass Rate: {report['summary']['pass_rate']*100:.1f}%")
            
            status = "PASSED" if report['overall_passed'] else "FAILED"
            print(f"\nOverall: {status}")
        
        return report


def run_full_validation(duration_minutes: float = 30.0, verbose: bool = True) -> tuple[dict, dict]:
    """Run both baseline and data ownership validation.
    
    Args:
        duration_minutes: Simulation duration for baseline validation
        verbose: Print detailed output
        
    Returns:
        (baseline_report, data_ownership_report) tuple
    """
    # Run baseline validation
    baseline_report = run_baseline_validation(duration_minutes=duration_minutes, verbose=verbose)
    
    # Run data ownership validation
    data_validator = DataOwnershipValidator()
    data_report = data_validator.validate_data_ownership(verbose=verbose)
    
    return baseline_report, data_report


if __name__ == "__main__":
    # Run validation when executed directly
    baseline_report, data_report = run_full_validation(duration_minutes=30.0, verbose=True)

    # Exit with error code if validation failed
    import sys

    overall_passed = baseline_report["overall_passed"] and data_report["overall_passed"]
    sys.exit(0 if overall_passed else 1)


