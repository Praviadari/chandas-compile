# Chandas-Compile AI Agent Roadmap

This roadmap defines a phased implementation plan for the Chandas-Compile project, organized by autonomous AI agent roles and practical engineering milestones.

## Phase 0: Foundation and MVP

Objective: establish a working Telugu prosody engine and project scaffold.

Tasks:
- Create the base repository structure: `core/`, `tests/`, `datasets/`, `examples/`, `docs/`.
- Implement a simple Telugu tokenizer to split akshara-like units.
- Build a Laghu/Guru rule engine for Telugu vowels, matras, anusvara/visarga, and halant.
- Add a minimal `main.py` demo and initial `pytest` coverage.
- Document MVP assumptions and next-step priorities.

Agent Role: `Setup Agent`
- Responsibilities: environment bootstrap, baseline code, documentation.
- Deliverables: working CLI demo, README, unit tests.

## Phase 1: Linguistic Analysis Agent

Objective: make Telugu syllable analysis robust and linguistically accurate.

Tasks:
- Expand tokenizer support for complex conjuncts (vatthulu), double consonants, and combined glyphs.
- Add true akshara segmentation for Telugu orthography instead of heuristic clusters.
- Enhance the Laghu/Guru rule engine with rules for:
  - consonant clusters when attached to halant,
  - yati and prasa effect on syllable weight,
  - special cases such as anusvara with long vowels.
- Create data-driven validation for Telugu word examples and known prosody cases.

Agent Role: `Linguistics Agent`
- Responsibilities: Telugu orthographic modeling, rule refinement, data collection.
- Deliverables: parser module, rule engine extension, test corpus.

## Phase 2: Kirtana FSM and Structural Agent

Objective: encode poetic structure and section flow as finite-state logic.

Tasks:
- Define a Kirtana state machine for `Pallavi`, `Charanam`, and return transitions.
- Add support for section markers and repeated stanza logic.
- Build a validation layer that can verify if a poem follows expected Kirtana structure.
- Create example kirtana templates and metadata formats.

Agent Role: `Structure Agent`
- Responsibilities: formalize poem structure, validate section transitions, provide templates.
- Deliverables: FSM module, structure validator, example data files.

## Phase 3: AI Evaluation and Benchmarking Agent

Objective: evaluate Telugu poem generation and classification using AI benchmarks.

Tasks:
- Design benchmark tasks for:
  - Laghu/Guru classification accuracy,
  - meter validation of generated lines,
  - structural compliance for kirtanas.
- Add a dataset pipeline for annotated Telugu verses and kirtana examples.
- Integrate with existing AI tools or local models for generation/evaluation experiments.
- Build a results dashboard or structured output format for model comparisons.

Agent Role: `Benchmark Agent`
- Responsibilities: design evaluation metrics, collect dataset, measure AI output quality.
- Deliverables: benchmark scripts, sample datasets, evaluation reports.

## Phase 4: Data Automation and Knowledge Agent

Objective: automate ingestion of Telugu verse sources and expand the knowledge base.

Tasks:
- Create data import tools for text files, CSV, or scraped Telugu poetry.
- Normalize input to the project’s internal representation.
- Build metadata tagging for verse source, author, metre type, section labels.
- Add provenance logging and dataset versioning.

Agent Role: `Data Agent`
- Responsibilities: dataset engineering, normalization, metadata extraction.
- Deliverables: ingestion utilities, normalized corpus, dataset docs.

## Phase 5: Deployment, UX, and Community Agent

Objective: make the project accessible, reproducible, and open for contributors.

Tasks:
- Add installation docs, example usage, and quick-start guides.
- Create automated tests, CI configuration, and linting rules.
- Publish sample notebooks or demo scripts illustrating the pipeline.
- Add clear contribution guidelines, issue templates, and roadmap visibility.

Agent Role: `Release Agent`
- Responsibilities: packaging, docs, community readiness.
- Deliverables: `README.md`, `CONTRIBUTING.md`, CI config, demos.

## Phase 6: Evolution Agent

Objective: refine the system into a sustainable research and AI evaluation platform.

Tasks:
- Move from heuristic rules to probabilistic or ML-enhanced prosody models.
- Add explainability for why a line is classified as Laghu or Guru.
- Explore cross-lingual comparisons between Telugu meter and other prosody systems.
- Plan future integration with AI model fine-tuning or evaluation suites.

Agent Role: `Research Agent`
- Responsibilities: long-term system growth, research experiments, new feature proposals.
- Deliverables: research notes, improved algorithms, extension proposals.

## Suggested Implementation Sequence

1. Finish Phase 0 and Phase 1 before adding benchmark logic.
2. Enable Phase 2 only after the tokenizer and rule engine are stable.
3. Begin Phase 3 with simple in-house evaluation, then add external model comparisons.
4. Keep Phase 4 and Phase 5 parallel where possible, because data and docs improve together.
5. Use Phase 6 to convert practical lessons into next-generation features.

## How to Use This Roadmap

- Treat each phase as a discrete development sprint.
- Assign one agent role to each major feature area.
- Use the roadmap as a checklist for implementation, testing, and documentation.
- Update the roadmap as new Telugu prosody requirements appear.
- Refer to `docs/implementation_plan.md` for an execution-ready world-class implementation plan.
