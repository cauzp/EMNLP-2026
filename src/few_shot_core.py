"""Core utilities for a simple Few-Shot classification workflow."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable, Iterable

Record = dict[str, str]


def load_jsonl(path: str | Path) -> list[Record]:
    """Load JSONL records from disk."""
    path = Path(path)
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def select_examples(records: Iterable[Record], k: int = 3) -> list[Record]:
    """Select the first k records as in-context examples."""
    return list(records)[: max(k, 0)]


def format_few_shot_prompt(examples: Iterable[Record], query_text: str) -> str:
    """Render a minimal few-shot prompt for binary classification."""
    lines = ["Task: Classify each text as positive or negative.", ""]
    for idx, record in enumerate(examples, start=1):
        lines.append(f"Example {idx}:")
        lines.append(f"Text: {record['text']}")
        lines.append(f"Label: {record['label']}")
        lines.append("")

    lines.append("Now classify the next item.")
    lines.append(f"Text: {query_text}")
    lines.append("Label:")
    return "\n".join(lines)


def parse_label(model_output: str) -> str:
    """Parse a binary label from model output text."""
    normalized = model_output.strip().lower()
    if "positive" in normalized:
        return "positive"
    if "negative" in normalized:
        return "negative"
    return "unknown"


def predict_with_prompt(
    examples: Iterable[Record], query_text: str, predictor: Callable[[str], str]
) -> str:
    """Build prompt and return parsed predictor output."""
    prompt = format_few_shot_prompt(examples, query_text)
    return parse_label(predictor(prompt))


def mock_predictor(prompt: str) -> str:
    """Deterministic fallback predictor for quick validation checks."""
    return "positive" if "great" in prompt.lower() else "negative"
