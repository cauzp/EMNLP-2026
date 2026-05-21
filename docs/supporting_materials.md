# EMNLP-2026 Submission Support Package

This repository provides compact, review-friendly materials for the EMNLP 2026 submission workflow.

## Included Materials

### 1. Few-Shot Python Core Code

File: `src/few_shot_core.py`

The core module includes:
- loading JSONL validation data,
- selecting in-context examples,
- rendering a few-shot prompt,
- parsing predicted labels from model text, and
- a mock predictor entry point for deterministic validation.

### 2. 500 Anonymized Validation Records

File: `data/validation_500_anonymized.jsonl`

The validation file provides 500 anonymized records in JSON Lines format (`.jsonl`).
Each row includes:
- `id`: unique record identifier,
- `text`: anonymized sample text,
- `label`: reference label (`positive` or `negative`).

## Data Privacy Note

The validation records use synthetic placeholders (for example, `[PERSON_001]` and `[ORG_002]`) to avoid exposing private or identifying information.
