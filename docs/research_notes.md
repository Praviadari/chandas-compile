# Chandas-Compile Research Notes

This document captures research ideas, limitations, and future model integration concepts for Chandas-Compile.

## Current Limitations

- Rule-based Chandassu validation is heuristic and may not capture all classical exceptions.
- Complex conjunct clusters and retroflex/sandhi forms are not fully covered.
- Current meter patterns are simplified and only cover a small set of classical examples.

## Research Opportunities

### ML-Enhanced Prosody
- Use a sequence model to classify Telugu syllable weight given orthographic input.
- Train on annotated meter corpora to learn exceptions and context-sensitive patterns.
- Compare rule-based output against model predictions.

### Explainability
- Provide reasoning traces for each syllable and section decision.
- Use the rule engine as a gating layer for ML predictions.
- Highlight differences between deterministic rules and learned outputs.

### Cross-Lingual Prosody Research
- Compare Telugu Chandassu rules against Sanskrit, Tamil, and other Indian metre systems.
- Explore whether meter patterns align with cross-lingual rhythm representations.

## Experimental Pipeline Ideas

1. Collect annotated Telugu metre corpus.
2. Preprocess text into akshara-level units.
3. Extract Laghu/Guru sequences and section labels.
4. Train a classifier to predict weight and section validity.
5. Evaluate generated poems against Chandas-Compile rule-based validation.

## Notes for Future Collaboration

- Add an `experiments/` folder once prototype notebooks are ready.
- Keep dataset annotation guidelines in `docs/`.
- Use issue labels like `research`, `experiment`, and `benchmark` for future work.
