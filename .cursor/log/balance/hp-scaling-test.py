"""Quick test to find optimal HP scaling for 30-minute target."""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from combat_duration_calculator import calculate_cumulative_time, DeckStats

deck = DeckStats(total_attack=62, total_defense=54, deck_size=8)

print("="*80)
print("HP SCALING COMPARISON - Finding optimal value for Enemy 50 at 30 minutes")
print("="*80)

for hp_per_enemy in [110, 120, 130, 135, 140, 145, 150]:
    results = calculate_cumulative_time(deck, 60, hp_per_enemy=hp_per_enemy)
    
    enemy_50 = results[49]
    enemy_60 = results[59]
    
    time_50 = enemy_50["cumulative_time_minutes"]
    time_60 = enemy_60["cumulative_time_minutes"]
    hp_50 = enemy_50.get("remaining_hp", 0)
    
    diff_from_30 = abs(30.0 - time_50)
    
    print(f"\nHP per enemy: {hp_per_enemy}")
    print(f"  Enemy 50: {time_50:.2f} min (diff from 30: {diff_from_30:.2f} min) | HP: {hp_50:.0f}")
    print(f"  Enemy 60: {time_60:.2f} min | HP: {enemy_60.get('remaining_hp', 0):.0f}")
    
    if 29.5 <= time_50 <= 30.5:
        print(f"  >>> OPTIMAL <<<")

print("\n" + "="*80)

