# Task 2.0.2: Live Terminal Simulation View - Design Specification

**Session:** 2.0.2  
**Task:** Live Terminal Simulation View  
**Date:** 2025-11-07  
**Status:** Design Complete - Ready for Implementation

---

## Purpose

Create a live terminal visualization mode for the gameplay simulator to provide real-time understanding of game flow, pacing, and card interactions. This tool will be essential during card design work (Tasks 2.1-2.4) to immediately test and validate card behavior.

## User Requirements

From user conversation:
- **Display:** Terminal-based (not web)
- **Speed Controls:** Real-time (1x), 2x, 5x, 10x via keyboard 1-4
- **Interaction:** Pause (Space), Step-through (advance one event)
- **Purpose:** Understanding game flow during design, not production gameplay

## Design Specification

### 1. Display Layout

```
╔═══════════════════════════════════════════════════════════════╗
║           IDLE DECK BATTLER - LIVE SIMULATION                 ║
╠═══════════════════════════════════════════════════════════════╣
║  Time: 00:08:34 / 30:00        Enemy #43                      ║
║  Essence: 38,450 (+182/sec)    ████████░░ 2,845 / 3,000 HP   ║
║  Attack: 1,240  Defense: 680   Attack: 12  Defense: 0        ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  ┌────────────────────────────┐                              ║
║  │  JUST DREW                 │                              ║
║  │  [Arcane Conduit]          │                              ║
║  │  +2 Essence/sec            │                              ║
║  │  Rate: 180 → 182/sec       │                              ║
║  └────────────────────────────┘                              ║
║                                                                ║
║  Recent Activity:                                             ║
║  • 08:33 - Card: Arcane Bolt (+20 ATK)                       ║
║  • 08:32 - Card: Essence Burst (+150 Essence)                ║
║  • 08:30 - Enemy spawned: #43 (3,000 HP, 12 ATK)             ║
║  • 08:18 - Enemy defeated: #42                               ║
╠═══════════════════════════════════════════════════════════════╣
║  Packs: Pack 1 ✓ (8:34)  Pack 2 (needs 61,550)              ║
╠═══════════════════════════════════════════════════════════════╣
║  Speed: [1]1x  [2]2x  [3]5x  [4]10x  │ [Space]Pause  [Q]uit ║
╚═══════════════════════════════════════════════════════════════╝
```

### 2. Display Zones

#### Top Status Bar
**Content:**
- Current simulation time (MM:SS format) / total duration
- Current enemy number
- Enemy HP bar (visual progress indicator)
- Player essence (current + rate/sec)
- Player accumulated attack/defense
- Enemy attack/defense

**Update Frequency:** Every frame (~30-60 FPS)

#### Center Stage - Card Draw Area
**Content:**
- Large, highlighted box showing most recently drawn card
- Card name
- Card effects (essence rate, burst, attack, defense)
- Visual feedback of changes (e.g., "Rate: 180 → 182/sec")

**Visual Treatment:**
- Colored border based on card type:
  - Cyan: Generator cards
  - Yellow: Combat cards
  - White: Utility cards
- Larger text, emphasized box
- Stays visible for ~2-3 seconds at 1x speed (scales with speed multiplier)

**Update Trigger:** On every card draw event

#### Event Log - Recent Activity
**Content:**
- Scrolling list of last 5-8 events
- Timestamped entries (MM:SS format)
- Event type icons:
  - `🃏` or `[CARD]` - Card draw
  - `⚔` or `[ENEMY]` - Enemy spawn
  - `✓` or `[WIN]` - Victory
  - `📦` or `[PACK]` - Pack affordable
  - `☠` or `[BOSS]` - Boss encounter (future)
- Compact format: "08:33 - Card: Arcane Bolt (+20 ATK)"

**Color Coding:**
- Card draws: Cyan/Yellow/White (by type)
- Enemy spawns: Red
- Victories: Green
- Pack milestones: Bright green
- Boss encounters: Bright red

**Update Trigger:** On any simulation event

#### Bottom Status Bar - Pack Affordability
**Content:**
- Pack 1-4 status indicators
- Checkmark ✓ when affordable
- "needs X essence" when not affordable
- Time when pack became affordable

**Example:** `Pack 1 ✓ (8:34)  Pack 2 (needs 61,550)  Pack 3 (needs 211,550)`

#### Bottom Control Bar
**Content:**
- Speed indicator showing current speed (highlighted)
- Keyboard hints for controls
- Pause indicator when paused

### 3. Keyboard Controls

| Key | Action | Description |
|-----|--------|-------------|
| `1` | 1x speed | Real-time simulation (1 sim second = 1 real second) |
| `2` | 2x speed | 2× simulation speed |
| `3` | 5x speed | 5× simulation speed |
| `4` | 10x speed | 10× simulation speed |
| `Space` | Pause/Resume | Toggle pause state |
| `N` or `→` | Step forward | Advance to next event (when paused) |
| `Q` or `Esc` | Quit | Exit to summary screen |

**Speed Multiplier Implementation:**
- Controls how fast simulation time advances
- Visual updates maintain consistent ~30-60 FPS
- At 10x speed: 1 real second = 10 simulation seconds
- Display updates scale appropriately (card highlight duration, etc.)

### 4. Step-Through Mode

**Activation:** Press `Space` to pause

**Behavior:**
- Display shows "⏸ PAUSED" indicator
- Pressing `N` or `→` advances to next **event** (not time tick)
- Events are: card draw, enemy spawn, combat resolution, pack affordable
- Display updates immediately to show new event
- Simulation time jumps to event time

**Display Enhancements When Paused:**
- "Next event: Card draw in 0.3s" (or similar info)
- Clear visual indication of pause state
- Highlight "Step" control in bottom bar

**Use Cases:**
- Examine exact card sequencing
- Understand specific combat resolutions
- Debug unexpected behavior
- Validate specific card interactions

### 5. Auto-Pause Features

**Pack Affordable:**
- When pack becomes affordable, simulation auto-pauses
- Display highlights pack milestone in event log
- Visual/audio celebration (optional: terminal bell)
- Requires user to press Space or step to continue
- **Rationale:** Pack purchases are key milestones, worth examining

**Boss Encounters (future):**
- When boss enemy spawns (Enemy 50, 100, 150), auto-pause
- Display shows "BOSS ENCOUNTER" indicator
- Gives user time to observe boss stats
- **Rationale:** Bosses are dramatic moments, worth highlighting

**Manual Override:**
- User can disable auto-pause via command flag (future enhancement)
- `sim live --no-pause-milestones`

### 6. Post-Simulation Summary Screen

When simulation completes or user quits early:

```
╔═══════════════════════════════════════════════════════════════╗
║                   SIMULATION COMPLETE                          ║
╠═══════════════════════════════════════════════════════════════╣
║  Duration: 30:00                                               ║
║  Final Essence: 250,000 (+607/sec)                            ║
║  Enemies Defeated: 149 / 150                                  ║
║  Cards Drawn: 1,800                                           ║
║  Total Damage: 13,950                                         ║
║                                                                ║
║  Pack Timing:                                                  ║
║    Pack 1:  7:02 ✓                                            ║
║    Pack 2: 11:34 ✓                                            ║
║    Pack 3: 18:28 ✓                                            ║
║    Pack 4: Not reached                                        ║
║                                                                ║
║  Status: Died to Enemy #150 (First Boss)                     ║
║          Boss HP: 3,488 remaining                             ║
╠═══════════════════════════════════════════════════════════════╣
║  [C]harts  [R]eplay  [Q]uit                                   ║
╚═══════════════════════════════════════════════════════════════╝
```

**Summary Options:**
- `C` - Generate and open static charts (existing functionality)
- `R` - Replay simulation from start (restart live view)
- `Q` - Exit to shell

**Summary Content:**
- All key metrics from simulation
- Pack affordability times
- Final enemy reached
- Victory/defeat status
- Clear indication if died to boss

## Technical Architecture

### Component Structure

```
simulator/
├── cli.py
│   └── live() command - Entry point for live mode
├── visualization/
│   ├── live_viewer.py - Main live view controller
│   ├── display.py - Rich-based rendering
│   ├── event_player.py - Event stream playback
│   └── input_handler.py - Keyboard input processing
└── core/
    └── combat.py - CombatSimulator (already exists)
```

### Data Flow

```
User runs: sim live [--duration 30]
    ↓
CLI creates LiveViewer
    ↓
LiveViewer initializes Display
    ↓
LiveViewer runs CombatSimulator (returns event stream)
    ↓
EventPlayer consumes events at controlled rate (speed multiplier)
    ↓
Display renders at 30-60 FPS
    ↓
InputHandler processes keyboard commands
    ↓
On completion/quit: Show summary, offer options
```

### Key Technical Decisions

**1. Asynchronous Architecture**
- Simulation runs in background (non-blocking)
- Events queued for display consumption
- Allows pause/resume/speed changes without restarting
- Display rendering separate from simulation logic

**2. Event-Driven Display**
- Display reacts to events from simulation
- No polling or constant state checking
- Clean separation of concerns

**3. Frame-Rate Independent Rendering**
- Display updates at consistent FPS regardless of simulation speed
- Speed multiplier affects how fast events are consumed, not rendering
- Smooth visual experience at all speeds

**4. Rich Library Integration**
- Use `rich.live.Live` context manager for auto-refresh
- `rich.panel.Panel` for bordered sections
- `rich.progress.Progress` for HP bars
- `rich.table.Table` for structured layouts
- `rich.console.Console` for colored output

### Libraries

**Required:**
- `rich` - Already in project (pyproject.toml)
- `keyboard` or `pynput` - For non-blocking keyboard input
  - Alternative: Use Rich's `Live.process_renderables()` with input handling

**Optional:**
- `blessed` - Alternative terminal library (if Rich limitations found)

### Performance Considerations

**Event Queue Management:**
- Limit queue size to prevent memory bloat during fast simulation
- Drop old events if queue exceeds threshold
- Keep last 50-100 events for event log display

**Display Update Rate:**
- Target 30-60 FPS for smooth rendering
- Skip frames if falling behind (prioritize responsiveness)
- State snapshots every 0.1s sufficient for display updates

**Memory:**
- Full event history not needed for live view
- Keep only recent events (last 100)
- Summary statistics accumulated separately (lightweight)

### Edge Cases

**Simulation Faster Than Display:**
- At high speeds (10x), simulation may outpace display
- Event queue buffers this
- Display shows "catching up" indicator if lag exceeds threshold

**User Quits During Simulation:**
- Gracefully stop simulation
- Show summary with partial results
- No data loss

**Very Long Simulations:**
- Event log truncates to last 50-100 events
- Memory usage stays bounded
- Performance remains consistent

**Terminal Resize:**
- Detect resize events
- Redraw layout to fit new size
- Handle gracefully (no crash)

## CLI Integration

### Command Options

**Option 1: Flag on existing command**
```bash
sim combat --live --duration 30
sim combat --live --duration 30 --speed 10
```

**Option 2: New command**
```bash
sim live --duration 30
sim live --duration 30 --speed 10
```

**Recommended:** Option 2 (cleaner, more discoverable)

### Command Signature

```python
@app.command()
def live(
    duration: int = typer.Option(30, "--duration", "-t", help="Simulation duration (minutes)"),
    initial_speed: int = typer.Option(1, "--speed", "-s", help="Initial speed multiplier (1, 2, 5, 10)"),
    no_auto_pause: bool = typer.Option(False, "--no-pause", help="Disable auto-pause on milestones"),
) -> None:
    """Run live terminal simulation with real-time visualization."""
```

### Help Output

```bash
$ sim live --help

Usage: sim live [OPTIONS]

  Run live terminal simulation with real-time visualization.
  
  Watch the simulation unfold in real-time with card draws, enemy spawns,
  and combat resolution. Control playback speed and step through events.

Options:
  -t, --duration INTEGER   Simulation duration (minutes)  [default: 30]
  -s, --speed INTEGER      Initial speed multiplier (1, 2, 5, 10)  [default: 1]
  --no-pause              Disable auto-pause on milestones
  --help                  Show this message and exit.

Controls:
  1-4        Set speed (1x, 2x, 5x, 10x)
  Space      Pause/Resume
  N or →     Step forward (when paused)
  Q or Esc   Quit to summary
```

## Testing Strategy

### Validation Tests

**Functional:**
1. All keyboard controls work correctly
2. Speed multipliers accurately affect simulation rate
3. Pause/resume maintains correct state
4. Step-through advances by exactly one event
5. Auto-pause triggers on pack milestones
6. Quit shows accurate summary with partial results

**Display:**
1. All zones render correctly
2. No visual glitches or flicker
3. HP bars scale correctly
4. Event log scrolls properly
5. Colors/formatting consistent with theme

**Performance:**
1. Maintains 30-60 FPS at all speeds
2. Memory usage stays bounded
3. No lag accumulation over long simulations
4. Graceful handling of terminal resize

### User Experience Tests

**Game Feel:**
1. Can you "feel" the 1-second card draw rhythm at 1x?
2. Does 10x speed feel responsive (not too fast/slow)?
3. Are pack milestones noticeable and exciting?
4. Is Enemy 150 boss encounter dramatic?

**Usability:**
1. Are controls intuitive and discoverable?
2. Is display information clear and scannable?
3. Does step-through mode help understand sequencing?
4. Is summary screen informative and actionable?

### Test Cases

**Test 1: Starter Deck 30-Minute Run**
- Load starter deck
- Run 30-minute simulation at 1x
- Verify all 3 packs become affordable
- Verify ~149 enemies defeated
- Verify death to Enemy 150 boss

**Test 2: Speed Control**
- Start at 1x
- Switch to 10x after 5 minutes
- Verify display remains smooth
- Verify summary shows correct timing

**Test 3: Step-Through**
- Start simulation
- Pause at 5 minutes
- Step through 20 events
- Verify each event displays correctly
- Resume and complete

**Test 4: Early Quit**
- Start simulation
- Quit at 15 minutes
- Verify summary shows correct partial results
- Verify no data loss

## Future Enhancements (Post-Task 2.0.2)

### Task 2.1+ Integration
**Enhanced Card Display:**
- Show card rarity (Common/Rare/Epic colors)
- Display conditional effects when triggered
- Highlight synergies when activated
- Show combo chains as they resolve

### Session 2.2+ Integration
**Interaction Visualization:**
- Trigger chain display ("Card A → Card B → Card C")
- Combo requirements progress ("2/3 Fire cards")
- State effects duration ("Lasts 8 more seconds")

### Session 5+ Integration
**Boss Enhancements:**
- Boss health bars with phases
- Special boss mechanics display
- Victory celebration animations

### Polish
**Visual:**
- Smooth animations (card draws, HP bars)
- Particle effects (optional, terminal-based)
- Sound effects (optional, terminal bell + custom)

**Interaction:**
- Save/load replay states
- Export replay to file for sharing
- Compare two simulations side-by-side

## Success Criteria

Task 2.0.2 is complete when:

1. ✅ Live mode command exists and runs
2. ✅ All display zones render correctly
3. ✅ All keyboard controls work
4. ✅ Speed multipliers function correctly (1x, 2x, 5x, 10x)
5. ✅ Pause/resume works
6. ✅ Step-through advances one event at a time
7. ✅ Auto-pause triggers on pack milestones
8. ✅ Summary screen displays after completion/quit
9. ✅ 30-minute starter deck simulation runs smoothly
10. ✅ No crashes or visual glitches

## Implementation Estimate

**Complexity:** Medium

**Time Estimate:** 3-4 hours

**Breakdown:**
- Display layout & rendering (Rich integration): 1.5 hours
- Event player & speed control: 1 hour
- Input handling & keyboard controls: 0.5 hours
- Summary screen & post-simulation options: 0.5 hours
- Testing & polish: 0.5 hours

**Dependencies:**
- Task 2.0 (simulator) - ✅ Complete
- Rich library - ✅ Already in project

**Blockers:** None

---

## Design Decisions Log

### Decision: Terminal vs Web
**Chosen:** Terminal  
**Rationale:** Faster to implement, good enough for design work, works everywhere  
**User Input:** Explicit preference for terminal

### Decision: Speed Controls
**Chosen:** 1x, 2x, 5x, 10x via keyboard 1-4  
**Rationale:** Covers range from "feel the rhythm" to "fast validation"  
**User Input:** Explicit request for these speeds

### Decision: Step-Through Feature
**Chosen:** Implement pause + single-event advance  
**Rationale:** Debugging and understanding card sequences  
**User Input:** Explicit request for pause and step features

### Decision: Auto-Pause on Milestones
**Chosen:** Auto-pause on pack affordable (with opt-out flag)  
**Rationale:** Packs are key milestones worth examining  
**Trade-off:** Slightly interrupts flow, but provides important context

### Decision: Event Stream Playback
**Chosen:** Async simulation + event queue + display consumption  
**Rationale:** Clean separation, allows pause/speed changes, good performance  
**Alternative Considered:** Lockstep simulation (rejected: no pause/resume)

---

**Design Status:** Complete - Ready for Implementation  
**Next Step:** Implement Task 2.0.2 per this specification  
**Estimated Completion:** 3-4 hours of development work

