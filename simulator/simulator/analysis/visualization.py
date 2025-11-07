"""Visualization using Plotly.

Generates interactive charts for:
- Progression curves (essence, rate over time)
- Resource generation over time
- Combat power accumulation
- Deck composition analysis
- Event timeline
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots


def create_progression_chart(results: dict, title: str = "Simulation Progression") -> go.Figure:
    """Create interactive progression curve chart showing essence and rate over time.
    
    Args:
        results: Simulation results from CombatSimulator
        title: Chart title
        
    Returns:
        Plotly figure with dual-axis progression chart
    """
    state_history = results.get("state_history", [])

    if not state_history:
        fig = go.Figure()
        fig.add_annotation(
            text="No state history data available",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
        )
        return fig

    # Extract time series data
    times = [s["time_minutes"] for s in state_history]
    essence = [s["essence"] for s in state_history]
    essence_rate = [s["essence_rate"] for s in state_history]

    # Create figure with dual y-axes
    fig = make_subplots(
        rows=2,
        cols=1,
        subplot_titles=("Essence Accumulated", "Essence Generation Rate"),
        vertical_spacing=0.12,
        row_heights=[0.5, 0.5],
    )

    # Essence accumulation
    fig.add_trace(
        go.Scatter(
            x=times,
            y=essence,
            mode="lines",
            name="Essence",
            line=dict(color="#7C3AED", width=2),
            hovertemplate="<b>%{y:,.0f} Essence</b><br>Time: %{x:.1f} min<extra></extra>",
        ),
        row=1,
        col=1,
    )

    # Essence rate
    fig.add_trace(
        go.Scatter(
            x=times,
            y=essence_rate,
            mode="lines",
            name="Essence/sec",
            line=dict(color="#10B981", width=2),
            hovertemplate="<b>%{y:.1f} Essence/sec</b><br>Time: %{x:.1f} min<extra></extra>",
        ),
        row=2,
        col=1,
    )

    # Add pack affordable markers
    pack_times = results.get("pack_affordable_times", {})
    pack_costs = {1: 40_000, 2: 100_000, 3: 250_000, 4: 625_000}

    for pack_num, pack_time in pack_times.items():
        cost = pack_costs.get(pack_num, 0)

        # Add vertical line on essence chart
        fig.add_vline(
            x=pack_time,
            line_dash="dash",
            line_color="rgba(255, 100, 100, 0.5)",
            annotation_text=f"Pack {pack_num}",
            annotation_position="top",
            row=1,
            col=1,
        )

    # Update axes
    fig.update_xaxes(title_text="Time (minutes)", row=2, col=1)
    fig.update_yaxes(title_text="Essence", row=1, col=1)
    fig.update_yaxes(title_text="Essence/sec", row=2, col=1)

    # Update layout
    fig.update_layout(
        title_text=title,
        height=700,
        showlegend=False,
        hovermode="x unified",
    )

    return fig


def create_combat_stats_chart(results: dict) -> go.Figure:
    """Create chart showing combat power accumulation over time.
    
    Args:
        results: Simulation results from CombatSimulator
        
    Returns:
        Plotly figure with combat stats over time
    """
    state_history = results.get("state_history", [])

    if not state_history:
        fig = go.Figure()
        fig.add_annotation(
            text="No state history data available",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
        )
        return fig

    times = [s["time_minutes"] for s in state_history]
    attack = [s["attack"] for s in state_history]
    defense = [s["defense"] for s in state_history]
    enemies = [s["enemies_defeated"] for s in state_history]

    fig = make_subplots(
        rows=2,
        cols=1,
        subplot_titles=("Combat Power Accumulation", "Enemies Defeated"),
        vertical_spacing=0.12,
    )

    # Attack
    fig.add_trace(
        go.Scatter(
            x=times,
            y=attack,
            mode="lines",
            name="Attack",
            line=dict(color="#EF4444", width=2),
            hovertemplate="<b>%{y:,.0f} Attack</b><extra></extra>",
        ),
        row=1,
        col=1,
    )

    # Defense
    fig.add_trace(
        go.Scatter(
            x=times,
            y=defense,
            mode="lines",
            name="Defense",
            line=dict(color="#3B82F6", width=2),
            hovertemplate="<b>%{y:,.0f} Defense</b><extra></extra>",
        ),
        row=1,
        col=1,
    )

    # Enemies defeated
    fig.add_trace(
        go.Scatter(
            x=times,
            y=enemies,
            mode="lines",
            name="Enemies",
            line=dict(color="#F59E0B", width=2),
            fill="tozeroy",
            hovertemplate="<b>%{y} Enemies</b><extra></extra>",
        ),
        row=2,
        col=1,
    )

    fig.update_xaxes(title_text="Time (minutes)", row=2, col=1)
    fig.update_yaxes(title_text="Power", row=1, col=1)
    fig.update_yaxes(title_text="Count", row=2, col=1)

    fig.update_layout(
        title_text="Combat Statistics",
        height=700,
        hovermode="x unified",
    )

    return fig


def create_deck_composition_chart(deck: object) -> go.Figure:
    """Create deck composition breakdown chart.
    
    Args:
        deck: Deck object with cards
        
    Returns:
        Plotly figure with deck composition visualization
    """
    from simulator.core.cards import CardType

    # Count card types
    type_counts = {}
    for card in deck.cards:
        card_type = card.card_type.value
        type_counts[card_type] = type_counts.get(card_type, 0) + 1

    # Create pie chart
    fig = go.Figure(
        data=[
            go.Pie(
                labels=list(type_counts.keys()),
                values=list(type_counts.values()),
                marker=dict(
                    colors=["#10B981", "#EF4444", "#7C3AED", "#F59E0B"]
                ),
                textinfo="label+percent+value",
                hovertemplate="<b>%{label}</b><br>%{value} cards (%{percent})<extra></extra>",
            )
        ]
    )

    fig.update_layout(
        title_text=f"Deck Composition: {deck.name}",
        height=500,
    )

    return fig


def create_event_timeline(results: dict, max_events: int = 100) -> go.Figure:
    """Create event timeline visualization.
    
    Args:
        results: Simulation results
        max_events: Maximum number of events to display
        
    Returns:
        Plotly figure with event timeline
    """
    events = results.get("events", [])

    if not events:
        fig = go.Figure()
        fig.add_annotation(
            text="No events recorded",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
        )
        return fig

    # Filter to important events only
    important_types = ["enemy_spawn", "victory", "pack_affordable"]
    filtered_events = [e for e in events if e["type"] in important_types]

    # Limit to max_events
    if len(filtered_events) > max_events:
        # Sample evenly
        step = len(filtered_events) // max_events
        filtered_events = filtered_events[::step]

    # Color mapping
    colors = {
        "enemy_spawn": "#F59E0B",
        "victory": "#10B981",
        "pack_affordable": "#7C3AED",
        "draw": "#94A3B8",
    }

    # Create scatter plot
    times = [e["time_minutes"] for e in filtered_events]
    types = [e["type"] for e in filtered_events]
    event_colors = [colors.get(t, "#94A3B8") for t in types]

    fig = go.Figure()

    for event_type in important_types:
        type_events = [e for e in filtered_events if e["type"] == event_type]
        if not type_events:
            continue

        fig.add_trace(
            go.Scatter(
                x=[e["time_minutes"] for e in type_events],
                y=[event_type] * len(type_events),
                mode="markers",
                name=event_type.replace("_", " ").title(),
                marker=dict(size=8, color=colors[event_type]),
                hovertemplate="<b>%{text}</b><br>Time: %{x:.2f} min<extra></extra>",
                text=[
                    f"{e['type']}: {e['data']}" for e in type_events
                ],
            )
        )

    fig.update_layout(
        title_text="Event Timeline",
        xaxis_title="Time (minutes)",
        yaxis_title="Event Type",
        height=400,
        hovermode="closest",
    )

    return fig


def save_all_charts(results: dict, deck: object, output_dir: str = "output") -> list[str]:
    """Generate and save all visualization charts.
    
    Args:
        results: Simulation results
        deck: Deck object
        output_dir: Output directory for HTML files
        
    Returns:
        List of created file paths
    """
    import os

    os.makedirs(output_dir, exist_ok=True)

    saved_files = []

    # Progression chart
    fig = create_progression_chart(results)
    filepath = os.path.join(output_dir, "progression.html")
    fig.write_html(filepath)
    saved_files.append(filepath)

    # Combat stats chart
    fig = create_combat_stats_chart(results)
    filepath = os.path.join(output_dir, "combat_stats.html")
    fig.write_html(filepath)
    saved_files.append(filepath)

    # Deck composition
    fig = create_deck_composition_chart(deck)
    filepath = os.path.join(output_dir, "deck_composition.html")
    fig.write_html(filepath)
    saved_files.append(filepath)

    # Event timeline
    fig = create_event_timeline(results)
    filepath = os.path.join(output_dir, "event_timeline.html")
    fig.write_html(filepath)
    saved_files.append(filepath)

    return saved_files

