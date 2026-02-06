---
name: weekly-diffusion-notebook
description: Create or refactor weekly Jupyter notebooks in this repo using the `wNN_topic.ipynb` and `wNN_topic_solved.ipynb` convention. Use when requests involve notebook scaffolding, experiment or tutorial structure, TODO/checkpoint formatting, reproducibility cleanup, or converting rough weekly notes into runnable notebook pairs under `notebooks/`. Generate the unsolved notebook first, then create `_solved` as an exact copy.
---

# Weekly Diffusion Notebook

Create weekly notebook pairs quickly and consistently with this repo's conventions.

## Decision Tree
- Choose `experiment` for exploratory, analytical, or hypothesis-driven work.
- Choose `tutorial` for instructional, step-by-step walkthroughs.
- If editing existing notebooks, preserve intent and improve structure and reproducibility.

## Quick Start
Run the helper script from the repository root:

```bash
uv run python .agents/skills/weekly-diffusion-notebook/scripts/new_weekly_notebook.py \
  --week 4 \
  --topic normal_loc_scale \
  --title "Normal Location-Scale Family" \
  --mode tutorial
```

This creates:
- `notebooks/w04_normal_loc_scale.ipynb`
- `notebooks/w04_normal_loc_scale_solved.ipynb`

The `_solved` notebook is a direct file copy of the unsolved notebook at scaffold time.

## Workflow
1. Lock intent and metadata.
Define `week`, `topic`, notebook `mode`, and learning goal.

2. Scaffold the pair from templates.
Use `scripts/new_weekly_notebook.py` instead of hand-authoring notebook JSON.
Create `wNN_topic.ipynb` with TODO scaffolding, then copy it to `wNN_topic_solved.ipynb`.

3. Fill cells in small runnable steps.
Use short markdown explanations and focused code cells.
Keep TODO/checkpoint markers clear.

4. Apply mode-specific patterns.
For experiment flow, read `references/experiment-patterns.md`.
For tutorial flow, read `references/tutorial-patterns.md`.

5. Validate reproducibility.
Use seeded RNG (`numpy.random.default_rng(seed)`), add lightweight `assert` checks, and keep outputs concise.
Use `references/quality-checklist.md` before delivery.

## Editing Existing Notebooks
- Preserve top-to-bottom story; avoid unnecessary cell reordering.
- Keep section headers stable so unsolved and solved versions are easy to compare.
- Preserve the unsolved notebook as baseline; do solution work in the `_solved` copy.
- Prefer targeted edits over full rewrites.
- If raw JSON edits are required, follow `references/notebook-structure.md`.

## References
- `references/experiment-patterns.md`
- `references/tutorial-patterns.md`
- `references/notebook-structure.md`
- `references/quality-checklist.md`
