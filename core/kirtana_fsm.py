"""Finite-state model for kirtana section flow."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class KirtanaFSM:
    """Minimal FSM: Pallavi as home state with Charanam loop support."""

    state: str = "PALLAVI"
    history: list[str] = field(default_factory=lambda: ["PALLAVI"])

    valid_transitions: dict[str, set[str]] = field(
        default_factory=lambda: {
            "PALLAVI": {"CHARANAM", "END"},
            "CHARANAM": {"PALLAVI", "CHARANAM", "END"},
            "END": set(),
        }
    )

    def transition(self, to_state: str) -> bool:
        """Move to next state if valid; return True on success."""
        if to_state in self.valid_transitions[self.state]:
            self.state = to_state
            self.history.append(to_state)
            return True
        return False

    def validate_sequence(self, states: list[str]) -> bool:
        """Validate a full state sequence without modifying the original FSM."""
        current = self.state
        if not states or states[0] != current:
            return False

        for next_state in states[1:]:
            if next_state not in self.valid_transitions[current]:
                return False
            current = next_state
        return True
