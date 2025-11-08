# Final Enemy HP Scaling Formula - APPROVED

**Date:** 2025-11-07 22:00:00  
**Status:** APPROVED by user

---

## Act-Based Step Function System

### **Act 1 (Enemies 1-50): Tutorial Tier**
```python
def enemy_hp_act1(n: int) -> float:
    """Enemies 1-50: Learning phase"""
    base = 20 + (n - 1) * 120
    
    if n == 50:
        return base * 1.3  # Mini-Boss #1: 9,768 HP
    return base

# Key values:
# Enemy 1:  20 HP
# Enemy 49: 5,780 HP
# Enemy 50: 9,768 HP (boss)
```

### **Act 2 (Enemies 51-100): Challenge Tier**
```python
def enemy_hp_act2(n: int) -> float:
    """Enemies 51-100: Increased difficulty"""
    base = 6_000 + (n - 51) * 130
    
    if n == 100:
        return base * 1.5  # Mini-Boss #2: 18,555 HP
    return base

# Key values:
# Enemy 51:  6,000 HP (step up from Act 1, but < boss)
# Enemy 99:  12,240 HP
# Enemy 100: 18,555 HP (boss)
```

### **Act 3 (Enemies 101-150): Master Tier**
```python
def enemy_hp_act3(n: int) -> float:
    """Enemies 101-150: End game content"""
    base = 12_500 + (n - 101) * 140
    
    if n == 150:
        return base * 2.0  # Major Boss: 38,680 HP
    return base

# Key values:
# Enemy 101: 12,500 HP (step up from Act 2, but < boss)
# Enemy 149: 19,220 HP
# Enemy 150: 38,680 HP (boss)
```

---

## Complete Formula

```python
def calculate_enemy_hp(enemy_number: int) -> float:
    """Calculate enemy HP with act-based step function."""
    
    # Act 1: Enemies 1-50
    if enemy_number <= 50:
        base = 20 + (enemy_number - 1) * 120
        return base * 1.3 if enemy_number == 50 else base
    
    # Act 2: Enemies 51-100
    elif enemy_number <= 100:
        base = 6_000 + (enemy_number - 51) * 130
        return base * 1.5 if enemy_number == 100 else base
    
    # Act 3: Enemies 101-150
    elif enemy_number <= 150:
        base = 12_500 + (enemy_number - 101) * 140
        return base * 2.0 if enemy_number == 150 else base
    
    # Act 4+: Future content
    else:
        # To be designed in future sessions
        base = 38_680 + (enemy_number - 150) * 200
        return base
```

---

## Key Milestones

```
Enemy 1:   20 HP      (Start)
Enemy 10:  1,100 HP
Enemy 25:  2,900 HP
Enemy 49:  5,780 HP   (Act 1 final regular enemy)
Enemy 50:  9,768 HP   (Mini-Boss #1 - First Attacker) ← ~23 minutes

[ACT 2 BEGINS]
Enemy 51:  6,000 HP   (Step up, but easier than boss)
Enemy 75:  9,120 HP
Enemy 99:  12,240 HP  (Act 2 final regular enemy)
Enemy 100: 18,555 HP  (Mini-Boss #2) ← ~60-70 minutes

[ACT 3 BEGINS]
Enemy 101: 12,500 HP  (Step up, but easier than boss)
Enemy 125: 15,860 HP
Enemy 149: 19,220 HP  (Act 3 final regular enemy)
Enemy 150: 38,680 HP  (Major Boss - End of "Act 1" content) ← ~120-180 minutes

[ACT 4 BEGINS - Future content]
Enemy 151: 38,880 HP
Enemy 200: 48,680 HP
...
```

---

## Design Philosophy

### Why Step Functions?
1. **Boss Victories Feel Rewarding:** Beating a boss unlocks easier content initially
2. **Clear Progression Tiers:** Each act has distinct feel and pacing
3. **No Regression:** Enemy 51 > Enemy 49 (progress continues)
4. **Escalating Challenge:** HP per enemy increases (120 → 130 → 140)
5. **Natural Breathing Room:** Post-boss enemies give players a moment to stabilize

### Why These Specific Numbers?
- **6,000 HP start (Act 2):** ~3.7% above Enemy 49 (5,780), ~39% below Boss 50 (9,768)
- **12,500 HP start (Act 3):** ~2.1% above Enemy 99 (12,240), ~33% below Boss 100 (18,555)
- **Gentle increases (120→130→140):** Progressive difficulty without sudden walls

---

## Attack Scaling (Unchanged from Parts A & B)

```python
def calculate_enemy_attack(enemy_number: int) -> int:
    """Enemy attack scaling."""
    
    if enemy_number <= 49:
        return 0  # Safe learning phase
    elif enemy_number == 50:
        return 10  # First attacker!
    elif enemy_number <= 99:
        return int(10 + (enemy_number - 51) * 0.3)
    elif enemy_number == 100:
        return 30  # Mini-Boss #2
    elif enemy_number <= 149:
        return int(25 + (enemy_number - 101) * 0.6)
    elif enemy_number == 150:
        return 80  # Major Boss
    else:
        return int(80 + (enemy_number - 150) * 1.0)
```

---

## Status: APPROVED ✅

Ready to implement in:
1. DESIGN.md (Part D documentation)
2. combat.py (Task 2.0.4 implementation)
3. validation.py (Task 2.0.5 validation)

**Approved by:** User  
**Date:** 2025-11-07 22:00:00

