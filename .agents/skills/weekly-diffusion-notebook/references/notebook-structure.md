# Notebook Structure

Jupyter notebooks are JSON with:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells`

When editing `.ipynb` programmatically:

- Preserve cell ordering unless reordering clearly improves narrative.
- Keep code cell `execution_count` as `null` for scaffolds.
- Keep code cell `outputs` as an empty list for scaffolds.
- Keep markdown and code `metadata` dictionaries present.
- Prefer template-based generation through `scripts/new_weekly_notebook.py`.
