# Quality Checklist

Before delivering notebook updates:

- Confirm names follow `wNN_topic.ipynb` and `wNN_topic_solved.ipynb`.
- Run top-to-bottom when possible, or state execution limits explicitly.
- Ensure setup cells define required state and do not depend on hidden state.
- Use seeded RNG: `numpy.random.default_rng(seed)`.
- Keep at least one lightweight assertion in each major section.
- Keep outputs concise; avoid noisy prints and oversized figures.
- Keep markdown skimmable with short headings and bullets.
- Verify `_solved` starts as an exact copy of unsolved, then only changes where solutions are added.
