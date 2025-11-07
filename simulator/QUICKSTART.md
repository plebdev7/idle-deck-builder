# Quick Start Guide

## Daily Usage Commands

### Run Commands
```bash
cd simulator

# Show simulator info
uv run sim info

# Run combat simulation (30 minutes)
uv run sim combat --duration 30

# Validate baseline numbers
uv run sim validate

# Analyze a deck
uv run sim analyze data/starter_deck.json
```

### Development
```bash
# Run tests
uv run pytest              # All tests
uv run pytest -v           # Verbose
uv run pytest --cov        # With coverage
uv run pytest -k combat    # Specific tests

# Code quality
uv run ruff check .        # Lint code
uv run ruff format .       # Format code
uv run mypy simulator/     # Type check
```

### Dependencies
```bash
# Add new package
uv add numpy

# Add dev package
uv add --dev ipython

# Update dependencies
uv sync

# Update all packages
uv sync --upgrade
```

## Project Structure

```
simulator/
├── simulator/          # Source code
│   ├── cli.py         # CLI commands
│   ├── core/          # Game logic
│   └── analysis/      # Analysis tools
├── tests/             # Test suite
├── data/              # JSON data files
└── output/            # Simulation results
```

## Key Files

- **cards.py** - Card models (includes starter deck from Session 1.3C)
- **deck.py** - Deck management
- **economy.py** - Pack costs, resource formulas
- **combat.py** - Combat simulator (implement in Task 2.0)

## Next Steps (Task 2.0)

1. Implement `CombatSimulator.simulate()` method
2. Add card draw mechanics
3. Add generator stacking logic
4. Add enemy spawning and scaling
5. Validate against Session 1.3 baseline numbers

## Tips

- Use `uv run` prefix for all commands (ensures correct venv)
- Tests run automatically on save in most IDEs
- Check `uv run sim --help` for all available commands
- All code is type-checked with mypy for safety

