# Chandas-Compile World-Class Implementation Plan

This document expands the existing roadmap with a professional, execution-ready implementation plan for the higher phases of Chandas-Compile.

## Purpose

Provide a structured, measurable plan to move from the current MVP to a production-grade Telugu prosody analysis and AI evaluation platform. This plan is designed for engineering teams, open-source contributors, and research collaborators.

## Vision

Chandas-Compile should become a trusted Telugu prosody compiler that:

- transforms Telugu poetic rules into executable algorithms,
- validates Kirtana structure and meter with deterministic logic,
- supports large corpora of annotated Telugu verses,
- evaluates AI-generated poetry with benchmark-grade metrics,
- evolves into a research platform for Indian prosody-aware language models.

## Key Focus Areas

1. Linguistic Accuracy
2. Poetic Structure Validation
3. AI Evaluation & Benchmarking
4. Data Engineering & Corpus Management
5. Deployment, Community, and Documentation
6. Research & Model Evolution

## Phase 1: Linguistic Accuracy and Orthographic Depth

### Goal
Produce a robust Telugu text processor that understands true akshara segmentation, conjuncts, and advanced Chandassu weight rules.

### Deliverables
- Full Telugu orthographic parser for akshara/vatthulu.
- Explicit handling for yati/prasa, anusvara, visarga, and halant rules.
- Enhanced Laghu/Guru rule engine with rule metadata and trace output.
- Unit test suite covering classical Telugu metrics.

### Milestones
1. Implement a character cluster tokenizer covering all Telugu Unicode ranges.
2. Add rule metadata for why each syllable is classified as Laghu or Guru.
3. Support secondary weight rules for yati and prasa.
4. Add a validation corpus of canonical Telugu lines.

### Success Metrics
- 95% agreement with annotated Telugu metre examples.
- 100% test coverage for core linguistic rules.
- Traceable decision output for each analysed unit.

## Phase 2: Poetic Structure and Kirtana Validation

### Goal
Build a deterministic Kirtana validator that verifies sections, repeat structure, and stanza flow.

### Deliverables
- Extended FSM for Pallavi/Charanam/Anupallavi and repeated structures.
- Section templates with expected stanza counts and transition rules.
- Validation reports with line-level pass/fail and diagnostics.
- Example wrappers for different Kirtana styles.

### Milestones
1. Extend FSM to support Anupallavi and encoded stanza numbering.
2. Define section label schema for real Telugu Kirtana text.
3. Add a structure diagnostics engine for invalid transitions.
4. Create sample templates and validation rule sets.

### Success Metrics
- Clear validation status for each section.
- Support for at least 3 classical Kirtana formats.
- Reproducible validation reports consumable by CI.

## Phase 3: AI Evaluation and Benchmarking

### Goal
Turn Chandas-Compile into an evaluation framework for generated Telugu poetry.

### Deliverables
- Benchmark dataset format for annotated poems.
- Evaluation scripts for metre, structure, and model output quality.
- Summary reports and JSON results for comparison.
- A CLI and programmatic API for benchmark execution.

### Milestones
1. Define benchmark schema for text, expected patterns, and metadata.
2. Add evaluation metrics including structural, metre, and token-level checks.
3. Implement result aggregation and comparison reports.
4. Publish sample benchmark dataset and usage examples.

### Success Metrics
- Platform supports at least one benchmark run end-to-end.
- Benchmark reports include pass ratio, invalid entries, and diagnostics.
- AI integration plan documented for future model evaluation.

## Phase 4: Data Engineering and Corpus Management

### Goal
Ensure the project can consume, normalize, and version large Telugu verse datasets.

### Deliverables
- Corpus ingesters for JSON, CSV, and labeled text formats.
- Normalization pipeline for Telugu text and metadata.
- Provenance metadata for source, author, metre, and section labels.
- Dataset versioning support and sample corpus exports.

### Milestones
1. Implement ingestion utilities for common data sources.
2. Add normalization rules for punctuation and section labels.
3. Create sample normalized corpus files and dataset docs.
4. Add save/load pipelines for reproducible dataset creation.

### Success Metrics
- Data ingestion handles at least 3 corpus formats.
- Normalized dataset files are machine-readable and versionable.
- Proof-of-concept corpus exists in `datasets/` with metadata.

## Phase 5: Deployment, Community, and UX

### Goal
Deliver an accessible project structure, packaging, docs, and incentives for contributors.

### Deliverables
- Package metadata, CLI, and example usage.
- README, contributing guide, issue templates, and roadmap docs.
- CI pipeline for test automation.
- Public examples and quick-start material.

### Milestones
1. Ship `pyproject.toml` and installable package metadata.
2. Add command-line usage examples and an `examples/` folder.
3. Create contribution guidelines and CI workflow.
4. Publish docs in `docs/` for roadmap and implementation.

### Success Metrics
- Package installs cleanly in a local virtual environment.
- CLI commands execute without errors.
- Contributor docs exist and test suite passes automatically.

## Phase 6: Research, ML, and Future Evolution

### Goal
Position Chandas-Compile as a research platform for Telugu prosody-aware language models.

### Deliverables
- Research notes for rule-based vs ML hybrid approaches.
- Explainability layer for meter decisions.
- Roadmap for model fine-tuning or zero-shot validation.
- Planning docs for cross-lingual prosody research.

### Milestones
1. Document rule-based limitations and ML opportunity areas.
2. Add explainable output for why meter decisions were made.
3. Define experimental pipelines for model evaluation.
4. Create research-oriented issue templates and dataset annotation plans.

### Success Metrics
- A documented research agenda exists.
- Exploratory notes for ML integration are available.
- The project is ready for future academic or AI collaboration.

## Execution Guidelines

### Team Organization
- `Core Engineering`: tokenizer, rule engine, validator.
- `Data Engineering`: dataset ingestion, normalization, corpus management.
- `Benchmarking`: benchmark definition, reporting, metric design.
- `Docs & QA`: documentation, examples, automations.

### Prioritization
- Priority 1: linguistic correctness and deterministic validation.
- Priority 2: benchmark and dataset support.
- Priority 3: packaging, docs, community readiness.
- Priority 4: research/ML evolution.

### Risk Management
- Use small, measurable milestones.
- Keep rule engine traceable for debugging.
- Avoid over-engineering early by validating with real Telugu examples.

## Next Immediate Steps

1. Finalize advanced vowel/conjunct rules and create a test corpus for them.
2. Implement a broader Kirtana section schema and add diagnostic output.
3. Build the first benchmark dataset and publish CLI benchmark commands.
4. Add large-corpus ingestion support with provenance metadata.
5. Document the implementation plan and make it discoverable from the roadmap.

## Notes

This document is intended to complement `docs/ai-agent-roadmap.md` and act as the operational next-stage plan for turning Chandas-Compile into a world-class Telugu prosody platform.
