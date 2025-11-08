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
    duration: int = typer.Option(30, "--duration", "-t", help="Simulation duration (minutes)"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
) -> None:
    """Validate Session 1.3 baseline numbers.
    
    Tests the starter deck against the 30-minute progression timeline
    to ensure generator rates, pack timing, and enemy scaling are correct.
    """
    from simulator.analysis.validation import run_baseline_validation
    
    console.print(
        Panel.fit(
            "[bold cyan]Validating Session 1.3 Baseline Numbers[/bold cyan]",
            border_style="cyan",
        )
    )
    
    console.print(f"[yellow]Duration:[/yellow] {duration} minutes")
    console.print("[yellow]Running simulation...[/yellow]\n")
    
    try:
        report = run_baseline_validation(duration_minutes=duration, verbose=verbose)
        
        if report["overall_passed"]:
            console.print("\n[bold green]VALIDATION PASSED[/bold green]")
            console.print(f"All checks passed ({report['summary']['passed_checks']}/{report['summary']['total_checks']})")
        else:
            console.print("\n[bold red]VALIDATION FAILED[/bold red]")
            console.print(f"Passed: {report['summary']['passed_checks']}/{report['summary']['total_checks']}")
            console.print(f"Pass rate: {report['summary']['pass_rate']*100:.1f}%")
            
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)


@app.command()
def combat(
    duration: int = typer.Option(30, "--duration", "-t", help="Simulation duration (minutes)"),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output directory for results and charts",
    ),
    save_charts: bool = typer.Option(True, "--charts/--no-charts", help="Generate visualization charts"),
) -> None:
    """Run combat simulation with starter deck.
    
    Simulates card draw, power accumulation, enemy intervals,
    and resource generation over the specified duration.
    """
    from simulator.core.cards import STARTER_DECK_CARDS
    from simulator.core.combat import CombatSimulator
    from simulator.core.deck import Deck
    from simulator.analysis.visualization import save_all_charts
    
    console.print(
        Panel.fit(
            f"[bold cyan]Combat Simulation ({duration} minutes)[/bold cyan]",
            border_style="cyan",
        )
    )
    
    console.print(f"[yellow]Duration:[/yellow] {duration} minutes")
    console.print("[yellow]Running simulation...[/yellow]\n")
    
    try:
        # Create starter deck
        deck = Deck(name="Starter Deck", cards=STARTER_DECK_CARDS, tier="arcane")
        
        # Run simulation
        sim = CombatSimulator()
        results = sim.simulate(duration_minutes=duration, deck=deck)
        
        # Display results
        console.print("[bold green]Simulation Complete![/bold green]\n")
        
        table = Table(show_header=False, box=None)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="white")
        
        table.add_row("Final Essence", f"{results['final_essence']:,.0f}")
        table.add_row("Essence Rate", f"{results['player_essence_rate']:.1f}/sec")
        table.add_row("Cards Drawn", f"{results['cards_drawn']:,}")
        table.add_row("Enemies Defeated", f"{results['enemies_defeated']}/{results['enemies_encountered']}")
        table.add_row("Total Damage", f"{results['total_damage_dealt']:,.0f}")
        table.add_row("Player HP", f"{results['player_hp']:.0f}/{results['player_max_hp']:.0f}")
        table.add_row("Player Deaths", f"{results['player_deaths']}")
        table.add_row("Furthest Enemy", f"{results['furthest_enemy']}")
        
        console.print(table)
        
        # Pack affordable times
        if results['pack_affordable_times']:
            console.print("\n[bold cyan]Pack Affordable Times:[/bold cyan]")
            for pack_num, time in sorted(results['pack_affordable_times'].items()):
                console.print(f"  Pack {pack_num}: [green]{time:.1f}[/green] minutes")
        
        # Save charts
        if save_charts:
            output_dir = output or Path("output")
            console.print(f"\n[yellow]Generating charts...[/yellow]")
            saved_files = save_all_charts(results, deck, str(output_dir))
            console.print(f"[green]Saved {len(saved_files)} chart files to {output_dir}/[/green]")
            
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)


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
def live(
    duration: int = typer.Option(30, "--duration", "-t", help="Simulation duration (minutes)"),
    speed: int = typer.Option(1, "--speed", "-s", help="Initial speed multiplier (1, 2, 5, 10)"),
    no_pause: bool = typer.Option(False, "--no-pause", help="Disable auto-pause on milestones"),
) -> None:
    """Run live terminal simulation with real-time visualization.
    
    Watch the simulation unfold in real-time with card draws, enemy spawns,
    and combat resolution. Control playback speed and step through events.
    
    Controls:
        1-4        Set speed (1x, 2x, 5x, 10x)
        Space      Pause/Resume
        N          Step forward (when paused)
        Q or Esc   Quit to summary
    """
    from simulator.core.cards import STARTER_DECK_CARDS
    from simulator.core.deck import Deck
    from simulator.visualization import LiveViewer
    
    # Validate speed
    if speed not in [1, 2, 5, 10]:
        console.print(f"[red]Invalid speed: {speed}. Must be 1, 2, 5, or 10[/red]")
        raise typer.Exit(code=1)
    
    try:
        # Create starter deck
        deck = Deck(name="Starter Deck", cards=STARTER_DECK_CARDS, tier="arcane")
        
        # Create and run live viewer
        viewer = LiveViewer(
            duration_minutes=duration,
            initial_speed=speed,
            auto_pause_milestones=not no_pause,
        )
        
        viewer.run(deck)
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Simulation interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)


@app.command()
def info() -> None:
    """Show simulator information and status."""
    console.print(
        Panel.fit(
            "[bold cyan]Idle Card Battler - Gameplay Simulator[/bold cyan]\n"
            "[dim]Version 0.3.0 - Task 2.0.5 Complete[/dim]",
            border_style="cyan",
        )
    )
    
    # Status table
    table = Table(title="Implementation Status", show_header=True, header_style="bold magenta")
    table.add_column("Feature", style="cyan", width=30)
    table.add_column("Status", width=20)
    table.add_column("Task", style="dim")
    
    table.add_row("Core Combat Simulation", "[green]Complete[/green]", "Task 2.0")
    table.add_row("Generator Mechanics", "[green]Complete[/green]", "Task 2.0")
    table.add_row("Enemy Spawning & Scaling", "[green]Complete[/green]", "Task 2.0")
    table.add_row("Combat-Over-Time System", "[green]Complete[/green]", "Task 2.0.3-2.0.4")
    table.add_row("HP & Death System", "[green]Complete[/green]", "Task 2.0.3-2.0.4")
    table.add_row("Baseline Validation", "[green]Complete[/green]", "Task 2.0.5")
    table.add_row("Visualization (Plotly)", "[green]Complete[/green]", "Task 2.0")
    table.add_row("Live Terminal View", "[green]Complete[/green]", "Task 2.0.2")
    table.add_row("Card Design Testing", "[yellow]Planned[/yellow]", "Task 2.1-2.4")
    table.add_row("Multi-Tier Support", "[yellow]Planned[/yellow]", "Task 8.1-8.3")
    
    console.print(table)
    
    # Quick stats
    from simulator.core.cards import STARTER_DECK_CARDS
    from simulator.core.deck import Deck
    
    deck = Deck(name="Starter Deck", cards=STARTER_DECK_CARDS, tier="arcane")
    
    console.print("\n[bold cyan]Starter Deck Info:[/bold cyan]")
    console.print(f"  Cards: {deck.size}")
    console.print(f"  Generators: {deck.generator_count}")
    console.print(f"  Combat: {deck.combat_count}")
    console.print(f"  Total Attack: {deck.total_attack}")
    console.print(f"  Total Defense: {deck.total_defense}")
    console.print(f"  Generation Rate: {deck.total_essence_rate}/sec")
    console.print(f"  Burst Essence: {deck.total_essence_burst}")
    
    console.print("\n[bold cyan]Available Commands:[/bold cyan]")
    console.print("[dim]Run [cyan]sim live[/cyan] for real-time simulation view[/dim]")
    console.print("[dim]Run [cyan]sim validate[/cyan] to test baseline numbers[/dim]")
    console.print("[dim]Run [cyan]sim combat[/cyan] to run a simulation[/dim]")
    console.print("[dim]Run [cyan]sim --help[/cyan] to see all commands[/dim]")


if __name__ == "__main__":
    app()

