# EMNLP-2026: AI Romance Discourse Classification

## Overview

This repository contains materials for an EMNLP 2026 submission focusing on Human-AI Romance discourse analysis on social media.

## Files

- **`AI_Love_Test.csv`**: Test dataset containing social media comments for classification evaluation.
- **`fewshot.py`**: Few-shot classification pipeline with detailed category definitions and reference examples.

## Categories

The classification framework identifies five main themes in Human-AI Romance discourse:

1. **碳硅同权与哲学认同** (Carbon-Silicon Equivalence & Philosophical Consensus): Comments comparing AI code to human cells, suggesting metaphysical equivalence.
2. **现实避难与情绪价值依赖** (Reality Refuge & Emotional Value Dependency): Comments viewing AI as an escape from real-world relationship pressures.
3. **交互体验与身体性玩梗** (Interactive Experience & Embodiment Jokes): Comments about AI performance, voice naturalness, and physical embodiment desires.
4. **虚假性警惕与存在论恐惧** (Authenticity Vigilance & Existential Fears): Comments questioning AI authenticity, privacy concerns, and psychological impacts.
5. **其他/无法分类** (Other/Unclassifiable): Factual statements, advertisements, or unclear comments.

## Usage

Run the few-shot classifier:

```bash
python fewshot.py
```

Ensure `fewshot.py` has access to your APIClassifier implementation configured with the provided few-shot examples.

## Language

All content is in Chinese and American English.
