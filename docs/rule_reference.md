# Chandas-Compile Rule Reference

This document describes the core Chandassu and Telugu prosody rules implemented in Chandas-Compile.

## Syllable Weight Rules

### Laghu (0)
- Short vowels: అ, ఇ, ఉ, ఋ, ఎ, ఒ
- Short vowel signs: ి, ు, ృ, ె, ౒
- Default consonant-only syllables when no other weight rule applies

### Guru (1)
- Long vowels: ఆ, ఈ, ఊ, ౠ, ఏ, ఓ, ఐ, ఔ
- Long vowel signs: ా, ీ, ూ, ౄ, ె, ూ, ై, ౌ
- Anusvara (ం) and visarga (ః)
- Consonant clusters indicated by virama (్)
- Yati markers and weight-affecting punctuation: |, ॥, ।

## Advanced Handling

### Conjunct Clusters
- Any syllable followed by a virama-marked next unit is treated as Guru.

### Yati and Prasa
- Yati markers are treated as weight-affecting separators.
- The preceding syllable is annotated for yati influence.

### Trace Output
- Each syllable returns a trace with the rules used to derive the weight.
- Helps make the decision process explainable.

## Kirtana Structure Rules

### Section Labels
- PALLAVI
- ANUPALLAVI
- CHARANAM

### FSM Transitions
- `PALLAVI` -> `ANUPALLAVI`, `CHARANAM`, `END`
- `ANUPALLAVI` -> `CHARANAM`, `END`
- `CHARANAM` -> `CHARANAM`, `PALLAVI`, `END`

## Supported Chandassu Meter Patterns

- Utpalamala: `1,0,1,0` — Four-syllable pattern with alternating Guru-Laghu weights.
- Champakamala: `1,0,0,1` — Four-syllable pattern with a trailing Guru weight.
- Kanda Padyam: `1,0,1,0` + `1,0,0,1` — Two-line pattern combining Utpalamala and Champakamala.

## Future Rule Targets

- Mandaaram and other classical metre categories
- Sanskrit-derived vowel and consonant clusters
