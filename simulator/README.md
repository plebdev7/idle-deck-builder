# Idle Card Battler - Gameplay Simulator

Python-based simulator for testing game balance, validating mechanics, and analyzing progression curves.

## Purpose

This simulator is used during the design phase (Sessions 1-8) to:
- Validate baseline numbers and progression curves
- Test card balance and deck compositions
- Simulate combat outcomes and resource generation
- Analyze economy flow and pacing
- Generate data for balance spreadsheets and visualizations

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for fast dependency management.

### Install uv (if not already installed)

```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install Dependencies

```bash
cd simulator
uv sync              # Install all dependencies
uv sync --dev        # Include dev dependencies (pytest, ruff, etc.)
```

### Run the Simulator

```bash
uv run sim --help    # Show available commands
uv run sim validate  # Validate Session 1.3 baseline numbers
uv run sim combat    # Run combat simulation
uv run sim analyze   # Analyze deck composition
```

## Development

### Project Structure

```
simulator/
├── pyproject.toml        # Project config, dependencies
├── simulator/            # Main package
│   ├── __init__.py
│   ├── cli.py           # CLI entry point (typer)
│   ├── core/            # Core game logic
│   │   ├── __init__.py
│   │   ├── cards.py     # Card models (Pydantic)
│   │   ├── deck.py      # Deck logic
│   │   ├── combat.py    # Combat simulation
│   │   └── economy.py   # Resource generation
│   └── analysis/        # Analysis & visualization
│       ├── __init__.py
│       ├── balance.py   # Balance calculations
│       └── visualization.py  # Plotly charts
├── tests/               # pytest tests
│   ├── test_cards.py
│   ├── test_combat.py
│   └── test_economy.py
└── data/                # Game data (JSON)
    ├── starter_deck.json
    └── baseline_numbers.json
```

### Running Tests

```bash
uv run pytest              # Run all tests
uv run pytest -v           # Verbose output
uv run pytest --cov        # With coverage report
uv run pytest -k combat    # Run specific tests
```

### Code Quality

```bash
uv run ruff check .        # Lint code
uv run ruff format .       # Format code
uv run mypy simulator/     # Type checking
```

### Adding Dependencies

```bash
uv add numpy               # Add runtime dependency
uv add --dev ipython       # Add dev dependency
uv remove some-package     # Remove dependency
```

## Usage Examples

### Validate Session 1.3 Baseline Numbers

```bash
uv run sim validate --starter-deck data/starter_deck.json
```

### Run 30-Minute Combat Simulation

```bash
uv run sim combat --duration 30 --deck data/starter_deck.json
```

### Analyze Deck Composition

```bash
uv run sim analyze --deck data/starter_deck.json --output charts/
```

### Generate Balance Report

```bash
uv run sim report --format html --output reports/balance.html
```

## Output

Simulation results are saved to:
- `output/simulations/` - Raw simulation data (JSON, CSV)
- `output/charts/` - Interactive Plotly charts (HTML)
- `output/reports/` - Balance analysis reports

## Design Phase Usage

This simulator supports the following CHECKLIST tasks:
- **Task 2.0**: Gameplay simulator foundation
- **Task 2.1-2.4**: Card design validation
- **Task 4.1-4.2**: Economy balance modeling
- **Task 5.1-5.3**: Combat system testing
- **Task 6.1-6.3**: Deck composition analysis
- **Task 7.3**: Progression curve validation
- **Task 8.1-8.3**: Multi-tier integration testing

## Notes

- This is a design/testing tool, NOT the actual game
- Game logic will be ported to TypeScript (SvelteKit) for production
- Python is used here for rapid iteration and analysis
- Output JSON data can be imported into the TypeScript game

