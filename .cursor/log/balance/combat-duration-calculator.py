"""Combat Duration Calculator for Combat-Over-Time System.

Calculates combat durations based on Session 2.0.3 new combat mechanics:
- Combat ticks at 1.0 second intervals
- Damage = ATK - DEF per tick (no minimum)
- Continuous deck cycling with 1-second reshuffle cooldown
- Stats accumulate during fight, reset per enemy

Used for Part C: Balance & Scaling calculations.
"""

from dataclasses import dataclass
import math


@dataclass
class DeckStats:
    """Deck statistics."""
    total_attack: int
    total_defense: int
    deck_size: int
    
    @property
    def cycle_time(self) -> float:
        """Time to cycle through full deck (draw + reshuffle)."""
        return self.deck_size + 1  # +1 for reshuffle cooldown
    
    @property
    def attack_per_cycle(self) -> int:
        """Attack gained per full cycle."""
        return self.total_attack
    
    @property
    def defense_per_cycle(self) -> int:
        """Defense gained per full cycle."""
        return self.total_defense


@dataclass
class EnemyStats:
    """Enemy statistics."""
    number: int
    health: float
    attack: int
    defense: int = 0


def calculate_enemy_stats(enemy_number: int, hp_per_enemy: float = 120.0) -> EnemyStats:
    """Calculate enemy stats based on scaling formulas.
    
    HP Formula: 20 + (n-1) × hp_per_enemy
    - OLD (Task 2.0.1): hp_per_enemy = 65.8
    - NEW (Session 2.0.3 Part C): hp_per_enemy = 120.0 (1.82× increase for 30-min target)
    
    Attack Formula: Based on Session 2.0.3 Part B:
    - Enemies 1-49: 0 attack
    - Enemy 50: 10 attack (Mini-Boss #1, 1.3× HP multiplier)
    - Enemies 51-99: 10 + (n-51) × 0.3
    - Enemy 100: 30 attack (Mini-Boss #2, 1.5× HP multiplier)
    - Enemies 101-149: 25 + (n-101) × 0.6
    - Enemy 150: 80 attack (Major Boss, 2× HP multiplier)
    
    Args:
        enemy_number: Enemy sequence number
        hp_per_enemy: HP gain per enemy level (default: 120.0)
    """
    # Health scaling
    if enemy_number < 150:
        base_hp = 20 + (enemy_number - 1) * hp_per_enemy
    elif enemy_number == 150:
        base_hp = 20 + (149) * hp_per_enemy  # Base before multiplier
    else:
        base_hp = 20 + (enemy_number - 1) * hp_per_enemy
    
    # Boss HP multipliers
    if enemy_number == 50:
        hp = base_hp * 1.3  # Mini-Boss #1
    elif enemy_number == 100:
        hp = base_hp * 1.5  # Mini-Boss #2
    elif enemy_number == 150:
        hp = base_hp * 2.0  # Major Boss
    else:
        hp = base_hp
    
    # Attack scaling
    if enemy_number <= 49:
        attack = 0
    elif enemy_number == 50:
        attack = 10  # First attacker!
    elif enemy_number <= 99:
        attack = int(10 + (enemy_number - 51) * 0.3)
    elif enemy_number == 100:
        attack = 30  # Mini-Boss #2
    elif enemy_number <= 149:
        attack = int(25 + (enemy_number - 101) * 0.6)
    elif enemy_number == 150:
        attack = 80  # Major Boss
    else:
        attack = int(80 + (enemy_number - 150) * 1.0)
    
    return EnemyStats(number=enemy_number, health=hp, attack=attack)


def calculate_combat_duration(deck: DeckStats, enemy: EnemyStats, player_hp: float = 100.0) -> dict:
    """Calculate combat duration with tick-by-tick simulation.
    
    Simulates combat with continuous cycling:
    - Each tick: Deal (ATK - Enemy_DEF) damage, take (Enemy_ATK - DEF) damage
    - Cards draw over cycle time, stats accumulate
    - Combat ends when enemy HP = 0 or player HP = 0
    
    Args:
        deck: Deck statistics
        enemy: Enemy statistics  
        player_hp: Starting player HP
        
    Returns:
        Dict with combat stats (duration, cycles, final_hp, etc.)
    """
    # Track state
    current_tick = 0
    player_current_hp = player_hp
    enemy_current_hp = enemy.health
    
    player_atk = 0
    player_def = 0
    
    cards_drawn_in_cycle = 0
    cycles_completed = 0
    in_reshuffle = False
    
    # For calculating average stats during ramp-up
    total_damage_dealt = 0.0
    total_damage_taken = 0.0
    
    while enemy_current_hp > 0 and player_current_hp > 0:
        # Draw card (1 per tick unless in reshuffle)
        if not in_reshuffle:
            cards_drawn_in_cycle += 1
            
            # Stats increase linearly during cycle
            # Simplified: assume even distribution of stats across cards
            player_atk += deck.total_attack / deck.deck_size
            player_def += deck.total_defense / deck.deck_size
            
            # Check if cycle complete
            if cards_drawn_in_cycle >= deck.deck_size:
                in_reshuffle = True
                cards_drawn_in_cycle = 0
        else:
            # Reshuffle cooldown (1 tick)
            in_reshuffle = False
            cycles_completed += 1
        
        # Combat tick
        damage_dealt = max(int(player_atk) - enemy.defense, 0)
        damage_taken = max(enemy.attack - int(player_def), 0)
        
        enemy_current_hp -= damage_dealt
        player_current_hp -= damage_taken
        
        total_damage_dealt += damage_dealt
        total_damage_taken += damage_taken
        
        current_tick += 1
        
        # Safety: break if combat too long (stalemate or error)
        if current_tick > 10000:
            return {
                "duration_seconds": current_tick,
                "duration_minutes": current_tick / 60,
                "cycles_completed": cycles_completed,
                "victory": False,
                "death": False,
                "stalemate": True,
                "final_player_hp": player_current_hp,
                "final_enemy_hp": enemy_current_hp,
                "damage_dealt": total_damage_dealt,
                "damage_taken": total_damage_taken,
            }
    
    # Combat resolved
    return {
        "duration_seconds": current_tick,
        "duration_minutes": current_tick / 60,
        "cycles_completed": cycles_completed,
        "victory": enemy_current_hp <= 0,
        "death": player_current_hp <= 0,
        "stalemate": False,
        "final_player_hp": player_current_hp,
        "final_enemy_hp": enemy_current_hp,
        "final_player_atk": int(player_atk),
        "final_player_def": int(player_def),
        "damage_dealt": total_damage_dealt,
        "damage_taken": total_damage_taken,
    }


def calculate_cumulative_time(deck: DeckStats, enemy_count: int, hp_per_enemy: float = 120.0) -> list[dict]:
    """Calculate combat duration for enemies 1-N and cumulative time.
    
    Args:
        deck: Deck statistics
        enemy_count: Number of enemies to calculate
        hp_per_enemy: HP gain per enemy level (default: 120.0)
        
    Returns:
        List of dicts with per-enemy and cumulative stats
    """
    results = []
    cumulative_time = 0.0
    cumulative_damage_taken = 0.0
    
    for n in range(1, enemy_count + 1):
        enemy = calculate_enemy_stats(n, hp_per_enemy=hp_per_enemy)
        
        # Player HP: Start fight with remaining HP from previous fights
        # (no healing between enemies)
        remaining_hp = 100.0 - cumulative_damage_taken
        if remaining_hp <= 0:
            # Player died before this enemy
            results.append({
                "enemy_number": n,
                "enemy_hp": enemy.health,
                "enemy_atk": enemy.attack,
                "combat_duration": 0,
                "cumulative_time": cumulative_time,
                "cumulative_time_minutes": cumulative_time / 60,
                "player_death": True,
                "remaining_hp": 0,
                "cumulative_damage_taken": cumulative_damage_taken,
            })
            continue
        
        combat = calculate_combat_duration(deck, enemy, player_hp=remaining_hp)
        
        cumulative_time += combat["duration_seconds"]
        cumulative_damage_taken += combat["damage_taken"]
        
        results.append({
            "enemy_number": n,
            "enemy_hp": enemy.health,
            "enemy_atk": enemy.attack,
            "combat_duration": combat["duration_seconds"],
            "cumulative_time": cumulative_time,
            "cumulative_time_minutes": cumulative_time / 60,
            "victory": combat["victory"],
            "death": combat["death"],
            "final_player_hp": combat["final_player_hp"],
            "final_player_atk": combat.get("final_player_atk", 0),
            "final_player_def": combat.get("final_player_def", 0),
            "damage_taken": combat["damage_taken"],
            "cumulative_damage_taken": cumulative_damage_taken,
            "remaining_hp": remaining_hp - combat["damage_taken"],
        })
    
    return results


def print_combat_table(results: list[dict], max_enemies: int = 60) -> None:
    """Print formatted combat duration table.
    
    Args:
        results: Combat results from calculate_cumulative_time
        max_enemies: Max enemies to print (default: 60)
    """
    print("\n" + "="*120)
    print(f"{'Enemy':<8} {'HP':<10} {'ATK':<6} {'Duration':<12} {'Cumulative':<15} {'Cum. Min':<10} {'Damage':<10} {'HP Left':<10} {'Status':<12}")
    print("="*120)
    
    for i, result in enumerate(results[:max_enemies]):
        enemy_num = result["enemy_number"]
        enemy_hp = f"{result['enemy_hp']:.0f}"
        enemy_atk = result["enemy_atk"]
        duration = f"{result['combat_duration']:.1f}s"
        cumulative = f"{result['cumulative_time']:.1f}s"
        cumulative_min = f"{result['cumulative_time_minutes']:.2f}"
        damage = f"{result.get('damage_taken', 0):.0f}"
        hp_left = f"{result.get('remaining_hp', 0):.0f}"
        
        # Status
        if result.get("death"):
            status = "DEATH"
        elif result.get("victory"):
            status = "Victory"
        elif result.get("player_death"):
            status = "DEAD (prev)"
        else:
            status = "Unknown"
        
        # Highlight bosses
        boss_marker = ""
        if enemy_num == 50:
            boss_marker = " [*] MINI-BOSS #1"
        elif enemy_num == 100:
            boss_marker = " [*] MINI-BOSS #2"
        elif enemy_num == 150:
            boss_marker = " [**] MAJOR BOSS"
        
        print(f"{enemy_num:<8} {enemy_hp:<10} {enemy_atk:<6} {duration:<12} {cumulative:<15} {cumulative_min:<10} {damage:<10} {hp_left:<10} {status:<12}{boss_marker}")
    
    print("="*120)


if __name__ == "__main__":
    # Starter deck stats (from DESIGN.md Session 1.3C)
    starter_deck = DeckStats(
        total_attack=62,  # 20+12+10+15+5 = 62
        total_defense=54,  # 18+6+10+5+15 = 54
        deck_size=8,
    )
    
    print("="*120)
    print("COMBAT DURATION CALCULATIONS - Session 2.0.3 Part C")
    print("="*120)
    print(f"\nStarter Deck Stats:")
    print(f"  Total Attack: {starter_deck.total_attack}")
    print(f"  Total Defense: {starter_deck.total_defense}")
    print(f"  Deck Size: {starter_deck.deck_size} cards")
    print(f"  Cycle Time: {starter_deck.cycle_time}s ({starter_deck.deck_size} draw + 1 reshuffle)")
    
    print("\n" + "="*120)
    print("CALCULATING COMBAT DURATIONS - NEW HP SCALING (120 per enemy)")
    print("="*120)
    
    # Calculate with NEW HP scaling (120 per enemy)
    print("\n[Using ADJUSTED HP formula: 20 + (n-1) × 120]")
    print("[Target: Enemy 50 at 30 minutes]\n")
    
    results_new = calculate_cumulative_time(starter_deck, 100, hp_per_enemy=120.0)
    
    # Print table
    print_combat_table(results_new, max_enemies=100)
    results = results_new  # Use for milestone analysis
    
    # Key milestones
    print("\n" + "="*120)
    print("KEY MILESTONES")
    print("="*120)
    
    milestones = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for milestone in milestones:
        if milestone <= len(results):
            result = results[milestone - 1]
            print(f"\nEnemy {milestone}:")
            print(f"  Time to reach: {result['cumulative_time_minutes']:.2f} minutes")
            print(f"  Combat duration: {result['combat_duration']:.1f} seconds")
            print(f"  Player HP remaining: {result.get('remaining_hp', 0):.0f} / 100")
            print(f"  Cumulative damage taken: {result.get('cumulative_damage_taken', 0):.0f}")
            if result.get("death"):
                print(f"  [!] PLAYER DEATH")
    
    # Check if player survives to Enemy 50
    if len(results) >= 50:
        enemy_50 = results[49]
        print("\n" + "="*120)
        print("ENEMY 50 ANALYSIS (Mini-Boss #1 - First Attacker)")
        print("="*120)
        print(f"Time to reach: {enemy_50['cumulative_time_minutes']:.2f} minutes")
        print(f"Player HP: {enemy_50.get('remaining_hp', 0):.0f} / 100")
        
        if enemy_50.get('death'):
            print("[!] PLAYER DIES BEFORE REACHING ENEMY 50")
        elif enemy_50.get('remaining_hp', 0) > 0:
            print("[OK] PLAYER SURVIVES TO ENEMY 50")
        else:
            print("[!] PLAYER DIES AT ENEMY 50")
    
    # Determine actual 30-minute target
    print("\n" + "="*120)
    print("30-MINUTE TARGET VALIDATION")
    print("="*120)
    
    target_time = 30.0  # minutes
    closest_enemy = None
    closest_diff = float('inf')
    
    for result in results:
        if result.get('player_death'):
            continue
        time_diff = abs(result['cumulative_time_minutes'] - target_time)
        if time_diff < closest_diff:
            closest_diff = time_diff
            closest_enemy = result['enemy_number']
    
    if closest_enemy:
        result = results[closest_enemy - 1]
        print(f"\nClosest to 30 minutes: Enemy {closest_enemy}")
        print(f"  Actual time: {result['cumulative_time_minutes']:.2f} minutes")
        print(f"  Difference: {closest_diff:.2f} minutes")
        print(f"  Player HP: {result.get('remaining_hp', 0):.0f} / 100")
        
        if closest_enemy == 50:
            print("\n[OK] Enemy 50 IS the 30-minute target (as designed)")
        elif closest_enemy < 50:
            print(f"\n[!] 30-minute target is EARLIER than Enemy 50 (actually Enemy {closest_enemy})")
            print("   Consider: Adjust enemy HP scaling or move Mini-Boss #1")
        else:
            print(f"\n[!] 30-minute target is LATER than Enemy 50 (actually Enemy {closest_enemy})")
            print("   Consider: Increase enemy HP scaling or move Mini-Boss #1")

