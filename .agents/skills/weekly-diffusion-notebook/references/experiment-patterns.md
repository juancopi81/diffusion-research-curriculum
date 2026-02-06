# Experiment Patterns

Use this structure for exploratory weekly notebooks:

- State a clear question and success criteria in the opening cells.
- Keep setup deterministic: imports, `numpy.random.default_rng(seed)`, and one config cell.
- Build one smallest runnable baseline before adding complexity.
- Keep TODO cells granular: one task per cell.
- Add at least one checkpoint assertion per major section.
- Record results near the relevant code with short markdown interpretation.
- Close with explicit findings and follow-up questions.
