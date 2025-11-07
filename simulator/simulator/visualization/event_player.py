"""Event playback system for live simulation view.

Consumes simulation events at a controlled rate with speed multipliers.
"""

import threading
import time
from collections import deque
from enum import Enum
from typing import Callable


class PlaybackState(Enum):
    """Playback state."""

    PLAYING = "playing"
    PAUSED = "paused"
    STOPPED = "stopped"
    COMPLETED = "completed"


class EventPlayer:
    """Manages event playback with speed control and pause/resume.
    
    Events are consumed from the simulation and played back at a controlled
    rate based on the speed multiplier. Supports pause, resume, and step-through.
    """

    def __init__(
        self,
        events: list[dict],
        on_event: Callable[[dict], None],
        on_complete: Callable[[], None],
        initial_speed: int = 1,
    ):
        """Initialize event player.
        
        Args:
            events: List of simulation events to play
            on_event: Callback when event should be displayed
            on_complete: Callback when playback completes
            initial_speed: Initial speed multiplier (1, 2, 5, 10)
        """
        self.events = events
        self.on_event = on_event
        self.on_complete = on_complete
        
        self.event_index = 0
        self.state = PlaybackState.PLAYING
        self.speed = initial_speed
        
        # Simulation time tracking
        self.current_sim_time = 0.0
        self.last_update_time = time.time()
        
        # Thread control
        self.thread: threading.Thread | None = None
        self.stop_flag = threading.Event()
        self.step_flag = threading.Event()
        
    def start(self) -> None:
        """Start event playback in background thread."""
        if self.thread is not None and self.thread.is_alive():
            return
            
        self.stop_flag.clear()
        self.thread = threading.Thread(target=self._playback_loop, daemon=True)
        self.thread.start()
        
    def stop(self) -> None:
        """Stop event playback."""
        self.state = PlaybackState.STOPPED
        self.stop_flag.set()
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            
    def pause(self) -> None:
        """Pause event playback."""
        if self.state == PlaybackState.PLAYING:
            self.state = PlaybackState.PAUSED
            
    def resume(self) -> None:
        """Resume event playback."""
        if self.state == PlaybackState.PAUSED:
            self.state = PlaybackState.PLAYING
            self.last_update_time = time.time()
            
    def toggle_pause(self) -> bool:
        """Toggle pause state.
        
        Returns:
            True if now paused, False if now playing
        """
        if self.state == PlaybackState.PLAYING:
            self.pause()
            return True
        elif self.state == PlaybackState.PAUSED:
            self.resume()
            return False
        return self.state == PlaybackState.PAUSED
        
    def step_forward(self) -> None:
        """Advance to next event (when paused)."""
        if self.state == PlaybackState.PAUSED:
            self.step_flag.set()
            
    def set_speed(self, speed: int) -> None:
        """Set playback speed multiplier.
        
        Args:
            speed: Speed multiplier (1, 2, 5, 10)
        """
        if speed in [1, 2, 5, 10]:
            self.speed = speed
            
    def get_next_event(self) -> dict | None:
        """Get next event without consuming it.
        
        Returns:
            Next event or None if no more events
        """
        if self.event_index < len(self.events):
            return self.events[self.event_index]
        return None
        
    def _playback_loop(self) -> None:
        """Main playback loop running in background thread."""
        while not self.stop_flag.is_set() and self.event_index < len(self.events):
            # Handle pause
            if self.state == PlaybackState.PAUSED:
                # Wait for resume or step
                if self.step_flag.wait(timeout=0.1):
                    self.step_flag.clear()
                    self._process_next_event()
                continue
                
            # Playing - advance simulation time based on speed
            current_time = time.time()
            elapsed_real = current_time - self.last_update_time
            self.last_update_time = current_time
            
            # Advance simulation time (real time × speed multiplier)
            self.current_sim_time += elapsed_real * self.speed
            
            # Process all events up to current sim time
            while self.event_index < len(self.events):
                event = self.events[self.event_index]
                event_time = event.get("time", 0)
                
                if event_time <= self.current_sim_time:
                    self._process_event(event)
                    self.event_index += 1
                else:
                    break
                    
            # Small sleep to prevent CPU spinning
            time.sleep(0.016)  # ~60 FPS
            
        # Playback complete
        self.state = PlaybackState.COMPLETED
        self.on_complete()
        
    def _process_next_event(self) -> None:
        """Process the next event (for step-through)."""
        if self.event_index < len(self.events):
            event = self.events[self.event_index]
            self.current_sim_time = event.get("time", 0)
            self._process_event(event)
            self.event_index += 1
            
    def _process_event(self, event: dict) -> None:
        """Process an event and call callback.
        
        Args:
            event: Event to process
        """
        self.on_event(event)

