"""Command-line interface for the simulator."""

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

app = typer.Typer(
    name="sim",
    help="Idle Card Battler Gameplay Simulator",
    add_completion=False,
)
console = Console()


@app.command()
def validate(
    starter_deck: Path = typer.Option(
        Path("data/starter_deck.json"),
        "--starter-deck",
        "-d",
        help="Path to starter deck JSON file",
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
) -> None:
    """Validate Session 1.3 baseline numbers.
    
    Tests the starter deck against the 30-minute progression timeline
    to ensure generator rates, pack timing, and enemy scaling are correct.
    """
    console.print(
        Panel.fit(
            "[bold cyan]Validating Session 1.3 Baseline Numbers[/bold cyan]",
            border_style="cyan",
        )
    )
    
    # Placeholder - will be implemented in Task 2.0
    console.print(f"[yellow]Loading starter deck from:[/yellow] {starter_deck}")
    console.print("[red]Not yet implemented - Task 2.0[/red]")


@app.command()
def combat(
    duration: int = typer.Option(30, "--duration", "-t", help="Simulation duration (minutes)"),
    deck: Path = typer.Option(
        Path("data/starter_deck.json"),
        "--deck",
        "-d",
        help="Path to deck JSON file",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output directory for results",
    ),
) -> None:
    """Run combat simulation.
    
    Simulates card draw, power accumulation, enemy intervals,
    and resource generation over the specified duration.
    """
    console.print(
        Panel.fit(
            f"[bold cyan]Combat Simulation ({duration} minutes)[/bold cyan]",
            border_style="cyan",
        )
    )
    
    console.print(f"[yellow]Deck:[/yellow] {deck}")
    console.print(f"[yellow]Duration:[/yellow] {duration} minutes")
    if output:
        console.print(f"[yellow]Output:[/yellow] {output}")
    
    # Placeholder - will be implemented in Task 2.0
    console.print("[red]Not yet implemented - Task 2.0[/red]")


@app.command()
def analyze(
    deck: Path = typer.Argument(..., help="Path to deck JSON file"),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output directory for charts",
    ),
) -> None:
    """Analyze deck composition and balance.
    
    Generates statistics and visualizations for a deck:
    - Generator vs combat card ratio
    - Power accumulation curves
    - Resource generation rates
    - Synergy analysis
    """
    console.print(
        Panel.fit(
            "[bold cyan]Deck Analysis[/bold cyan]",
            border_style="cyan",
        )
    )
    
    console.print(f"[yellow]Analyzing deck:[/yellow] {deck}")
    if output:
        console.print(f"[yellow]Charts will be saved to:[/yellow] {output}")
    
    # Placeholder - will be implemented in Task 2.0+
    console.print("[red]Not yet implemented - Task 2.0+[/red]")


@app.command()
def report(
    output_format: str = typer.Option(
        "html", "--format", "-f", help="Output format (html, json, csv)"
    ),
    output: Path = typer.Option(
        Path("output/reports/balance.html"),
        "--output",
        "-o",
        help="Output file path",
    ),
) -> None:
    """Generate balance report.
    
    Creates a comprehensive balance report including:
    - All simulation results
    - Balance metrics
    - Progression curves
    - Recommendations
    """
    console.print(
        Panel.fit(
            "[bold cyan]Balance Report Generator[/bold cyan]",
            border_style="cyan",
        )
    )
    
    console.print(f"[yellow]Format:[/yellow] {output_format}")
    console.print(f"[yellow]Output:[/yellow] {output}")
    
    # Placeholder - will be implemented in Task 2.0+
    console.print("[red]Not yet implemented - Task 2.0+[/red]")


@app.command()
def info() -> None:
    """Show simulator information and status."""
    console.print(
        Panel.fit(
            "[bold cyan]Idle Card Battler - Gameplay Simulator[/bold cyan]\n"
            "[dim]Version 0.1.0[/dim]",
            border_style="cyan",
        )
    )
    
    # Status table
    table = Table(title="Implementation Status", show_header=True, header_style="bold magenta")
    table.add_column("Feature", style="cyan", width=30)
    table.add_column("Status", width=20)
    table.add_column("Task", style="dim")
    
    table.add_row("Core Combat Simulation", "[red]Not Implemented[/red]", "Task 2.0")
    table.add_row("Generator Mechanics", "[red]Not Implemented[/red]", "Task 2.0")
    table.add_row("Baseline Validation", "[red]Not Implemented[/red]", "Task 2.0")
    table.add_row("Visualization", "[red]Not Implemented[/red]", "Task 2.0")
    table.add_row("Card Design Testing", "[red]Planned[/red]", "Task 2.1-2.4")
    table.add_row("Multi-Tier Support", "[red]Planned[/red]", "Task 8.1-8.3")
    
    console.print(table)
    console.print("\n[dim]Run [cyan]sim --help[/cyan] to see available commands[/dim]")


if __name__ == "__main__":
    app()

