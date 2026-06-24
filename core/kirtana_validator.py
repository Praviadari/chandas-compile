"""Kirtana stanza validation combining FSM flow and meter patterns."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from core.kirtana_fsm import KirtanaFSM
from core.meter_validator import validate_pattern


@dataclass
class SectionResult:
    name: str
    lines: list[str]
    expected_patterns: list[list[int]]
    line_results: list[dict[str, object]] = field(default_factory=list)
    valid: bool = False


def parse_kirtana_text(text: str) -> list[SectionResult]:
    """Parse labeled Kirtana text into sections."""
    sections: list[SectionResult] = []
    current_section: SectionResult | None = None
    section_labels = ["PALLAVI", "ANUPALLAVI", "CHARANAM"]

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        upper_line = line.upper()
        matched_label = next(
            (label for label in section_labels if upper_line.startswith(f"{label}:")),
            None,
        )

        if matched_label:
            current_section = SectionResult(matched_label, [line[len(matched_label) + 1 :].strip()], [])
            sections.append(current_section)
            continue

        if current_section is None:
            raise ValueError("Kirtana text must begin with a section label like PALLAVI:, ANUPALLAVI:, or CHARANAM:." )

        current_section.lines.append(line)

    return sections


def validate_kirtana_sections(
    sections: Iterable[SectionResult], expected_patterns: dict[str, list[list[int]]]
) -> dict[str, object]:
    """Validate each section and the overall kirtana structure."""
    sequence = KirtanaFSM()
    section_results: list[SectionResult] = []
    structure_valid = True
    section_order: list[str] = []
    invalid_transitions: list[str] = []

    for index, section in enumerate(sections):
        if section.name not in expected_patterns:
            raise ValueError(f"Missing expected patterns for section {section.name}.")

        expected_for_section = expected_patterns[section.name]
        if len(expected_for_section) != len(section.lines):
            raise ValueError(
                f"Expected pattern count for {section.name} does not match line count."
            )

        section.line_results = []
        section.valid = True

        for line, expected in zip(section.lines, expected_for_section):
            result = validate_pattern(line, expected)
            section.line_results.append(result)
            if not result["valid"]:
                section.valid = False
                structure_valid = False

        section_results.append(section)
        section_order.append(section.name)

        if index == 0:
            if section.name != sequence.state:
                invalid_transitions.append(
                    f"Expected initial section {sequence.state}, but found {section.name}."
                )
                structure_valid = False
                sequence.transition(section.name)
            continue

        if not sequence.transition(section.name):
            invalid_transitions.append(
                f"Invalid transition from {sequence.history[-1]} to {section.name}."
            )
            structure_valid = False

    if structure_valid and sequence.state != "END":
        if not sequence.transition("END"):
            structure_valid = False

    return {
        "sections": section_results,
        "section_order": section_order,
        "structure_valid": structure_valid,
        "invalid_transitions": invalid_transitions,
        "fsm_state": sequence.state,
    }


def validate_kirtana_text(text: str, expected_patterns: dict[str, list[list[int]]]) -> dict[str, object]:
    """Parse and validate a labeled Kirtana text against expected patterns."""
    sections = parse_kirtana_text(text)
    return validate_kirtana_sections(sections, expected_patterns)
