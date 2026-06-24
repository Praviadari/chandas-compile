# Chandas-Compile Future Work

This document captures the next wave of future work beyond the current MVP and implementation plan. It is intended for roadmap planning, contributor orientation, and research preparation.

## Purpose

- Define long-term technical goals clearly.
- Track research gaps and advanced feature opportunities.
- Provide a structured handoff from current implementation to future expansion.
- Ensure the project remains focused on Telugu prosody, Kirtana structure, benchmark evaluation, and AI research.

## Core Future Themes

### 1. Advanced Chandassu Rule Engine

Objective: support the full classical spectrum of Telugu metrical rules.

Tasks:
- Add explicit yati/prasa handling to the rule engine.
- Detect and validate Utpalamala, Champakamala, and Kanda Padyam patterns.
- Implement rule exceptions for Sanskrit loan words and tradition-specific scansion.
- Add traceable justification for each weighted syllable.

Success criteria:
- The engine supports named meter validation for at least 5 classical patterns.
- A canonical test corpus exists for advanced Chandassu examples.
- Rule decisions are explainable and auditable.

### 2. Complete Kirtana Structure Support

Objective: validate full Kirtana texts, including all classical section schemes.

Tasks:
- Add support for `ANUPALLAVI`, repeated `CHARANAM`, and nested section flows.
- Create templates for `PALLAVI-ANUPALLAVI-CHARANAM` and other classical formats.
- Add diagnostics for missing or extra sections and invalid transitions.
- Support labeled stanza metadata in dataset ingestion.

Success criteria:
- The validator handles at least 3 distinct historical Kirtana layouts.
- Structural reports clearly indicate the failure reason.
- CLI supports validating full multi-section kirtanas from text files.

### 3. Benchmark and AI Evaluation Framework

Objective: build a reliable evaluation platform for Telugu poetry generation.

Tasks:
- Define benchmark schema with metadata, patterns, and source attribution.
- Add score metrics for metre, structure, and overall compliance.
- Create a dataset of annotated verses for evaluation.
- Add support for comparing model outputs and summarized reports.

Success criteria:
- Benchmark suite can run end-to-end from JSON dataset input.
- Reports include pass ratios, invalid entries, and structured diagnostics.
- The framework is extendable to external model output workflows.

### 4. Large-Scale Corpus and Dataset Engineering

Objective: make Chandas-Compile ready for production-scale Telugu verse data.

Tasks:
- Support large JSON/CSV corpus ingestion with provenance metadata.
- Add normalization for punctuation, labels, and section markers.
- Create versioned dataset exports and sample corpus collections.
- Design annotation workflows for metre and section labels.

Success criteria:
- The project can ingest and normalize multiple corpus formats.
- Versioned dataset payloads include metadata and source provenance.
- Sample datasets are available in `datasets/` for contributors.

### 5. Research and ML Readiness

Objective: prepare the platform for research, ML experiments, and academic collaboration.

Tasks:
- Document rule-based limitations and ML opportunity areas.
- Design explainability outputs for metre and structure classification.
- Prototype a model evaluation pipeline for generated Telugu poetry.
- Create research-oriented issue templates and annotation guidelines.

Success criteria:
- A documented research agenda exists in `docs/`.
- The project clearly separates deterministic rule logic from future ML experiments.
- The codebase is structured to allow future model-based validators.

## Recommended Documentation Additions

- `docs/future_work.md`: this document.
- `docs/benchmark_design.md`: benchmark dataset schema and report definitions.
- `docs/rule_reference.md`: detailed Chandassu rule descriptions and examples.
- `docs/research_notes.md`: experiments, limitations, and model integration ideas.

## How to Use This Document

- Review during sprint planning and feature prioritization.
- Use as the source of truth for future roadmap discussions.
- Attach relevant GitHub issues or PRs to future work themes.
- Keep this document updated as new research or requirements emerge.
