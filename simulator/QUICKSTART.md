# Idle Card Battler Simulator - Quick Start Guide

## Installation

The simulator uses `uv` for dependency management. If you haven't installed `uv` yet:

```bash
# Install uv (if not already installed)
pip install uv

# Install project dependencies
cd simulator
uv sync
```

## Commands

### Live Simulation View (NEW!)

Watch the simulation unfold in real-time with card draws, enemy spawns, and combat resolution.

**⚠️ IMPORTANT:** The live viewer requires an **interactive terminal**. Do NOT pipe input (like `echo q |`) as this will prevent the display from updating in real-time.

**Windows (PowerShell):**
```powershell
# Set UTF-8 encoding first (required for proper display)
$env:PYTHONIOENCODING='utf-8'

# Run 30-minute simulation at 1x speed (watch in real-time)
uv run sim live

# Run 5-minute simulation at 5x speed (good for testing, takes 1 real minute)
uv run sim live --duration 5 --speed 5
```

**Unix/Linux/Mac:**
```bash
# Run 30-minute simulation at 1x speed
uv run sim live

# Run 5-minute simulation at 5x speed (good for testing)
uv run sim live --duration 5 --speed 5
```

**Keyboard Controls:**
- `1-4`: Set speed (1x, 2x, 5x, 10x)
- `Space`: Pause/Resume
- `N`: Step forward one event (when paused)
- `Q`: Quit to summary

**Options:**
- `--duration` / `-t`: Simulation duration in minutes (default: 30)
- `--speed` / `-s`: Initial speed multiplier (1, 2, 5, 10, default: 1)
- `--no-pause`: Disable auto-pause on pack milestones

### Combat Simulation

Run a simulation and generate charts:

```bash
uv run sim combat --duration 30
```

Charts are saved to `output/` directory.

### Baseline Validation

Validate Session 1.3 baseline numbers:

```bash
uv run sim validate
```

### Info

Show simulator status and starter deck info:

```bash
uv run sim info
```

### Help

```bash
# Show all commands
uv run sim --help

# Show help for specific command
uv run sim live --help
uv run sim combat --help
```

## Example Workflows

### Quick Validation (Fast)
```bash
# 1-minute test at 10x speed, no pauses (takes ~6 real seconds)
uv run sim live -t 1 -s 10 --no-pause
```

### Card Design Testing (Interactive)
```bash
# 5-minute simulation at 2x speed (takes 2.5 real minutes)
# Good balance between speed and being able to see details
uv run sim live --duration 5 --speed 2
```

### Balance Testing (Moderate)
```bash
# 10-minute simulation at 5x speed (takes 2 real minutes)
uv run sim live -t 10 -s 5
```

### Full Session Testing (Slow)
```bash
# Full 30-minute simulation at normal speed
# This is REAL TIME - takes 30 actual minutes!
# Use higher speed for faster testing
uv run sim live --duration 30 --speed 1
```

## Output

- **Live Mode:** Real-time terminal display, optional charts at end
- **Combat Mode:** Charts saved to `output/` directory:
  - `progression.html`: Essence over time
  - `combat_stats.html`: Attack/Defense progression
  - `deck_composition.html`: Card draws breakdown
  - `event_timeline.html`: Event distribution

## Troubleshooting

### Windows: Box Characters Not Displaying

**Symptom:** Seeing `?` or garbled characters instead of boxes.

**Solution:** Set UTF-8 encoding:
```powershell
$env:PYTHONIOENCODING='utf-8'
```

Or add to your PowerShell profile (`$PROFILE`) permanently:
```powershell
$env:PYTHONIOENCODING='utf-8'
```

### "No module named 'typer'" Error

**Solution:** Install dependencies with `uv sync`:
```bash
cd simulator
uv sync
```

## Project Structure

```
simulator/
├── simulator/
│   ├── core/              # Core game mechanics
│   │   ├── cards.py       # Card definitions
│   │   ├── combat.py      # Combat simulation
│   │   ├── deck.py        # Deck management
│   │   └── economy.py     # Economy calculations
│   ├── analysis/          # Analysis and validation
│   │   ├── balance.py     # Balance metrics
│   │   ├── validation.py  # Baseline validation
│   │   └── visualization.py # Chart generation
│   ├── visualization/     # Live terminal view (NEW!)
│   │   ├── live_viewer.py   # Main orchestrator
│   │   ├── display.py       # Rich UI rendering
│   │   └── event_player.py  # Event playback
│   └── cli.py             # Command-line interface
├── tests/                 # Test suite
├── output/                # Generated charts
└── pyproject.toml         # Project configuration
```

## What's Implemented

- ✅ Core combat simulation
- ✅ Generator mechanics (rate, burst, hybrid, stacking)
- ✅ Enemy spawning and scaling
- ✅ Baseline validation
- ✅ Plotly visualizations
- ✅ **Live terminal view** (Task 2.0.2)
- ⏳ Card design testing (Task 2.1-2.4)
- ⏳ Multi-tier support (Task 8.1-8.3)

## Next Steps

- Use `sim live` during card design to test balance in real-time
- Run `sim validate` to ensure baseline numbers are correct
- Generate charts with `sim combat` for detailed analysis

## Support

For issues or questions, check:
- `DESIGN.md` - Game design specifications
- `ROADMAP.md` - Implementation roadmap
- `.cursor/log/sessions/` - Detailed task logs
