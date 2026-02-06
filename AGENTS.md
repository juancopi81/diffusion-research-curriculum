# Repository Guidelines

## Project Structure & Module Organization
- `notes/`: Weekly theory summaries (`wNN_topic.md`) plus supporting images in `notes/figures/`.
- `notebooks/`: Hands-on work; paired unsolved/solved notebooks follow `wNN_topic.ipynb` and `wNN_topic_solved.ipynb`.
- `proofs/`: Written solutions that mirror the week numbers in `notes/`.
- `mini_projects/`: Placeholder for monthly milestone code and reports; keep each project in its own subfolder.
- `papers/`: Paper summaries and derivations; align filenames with the paper name.
- `pyproject.toml`/`uv.lock`: Python 3.11+ environment managed by `uv`.

## Setup, Build, and Run
- Install deps: `uv sync` (creates `.venv`, pins versions from `uv.lock`).
- Launch notebooks: `uv run jupyter lab`; add `--NotebookApp.token=''` for trusted local use.
- Quick script check: `uv run python main.py`.
- Add a new package: `uv add package_name` (updates lockfile); commit both `pyproject.toml` and `uv.lock`.

## Coding Style & Naming Conventions
- Python: PEP 8, 4-space indent, type hints for new functions, concise docstrings using imperative mood.
- Notebooks: Keep Markdown cells for narrative; reuse section headers already present in unsolved templates.
- Filenames: start with week number (`wNN_`), use lowercase with underscores; suffix solved variants with `_solved`.
- Data/figures: store small assets under the closest module (`notes/figures/`, `mini_projects/<name>/figures/`). Avoid committing files >10 MB.

## Markdown LaTeX Style (GitHub-safe)
- Use inline math as `$...$` for equations inside sentences and list items.
- Do not use inline `$$...$$` (GitHub frequently mis-renders this).
- Use display math as standalone blocks only:
  `$$` on its own line, equation lines, then closing `$$` on its own line.
- In list items, prefer inline math; if an equation is long/complex, move it outside the list as a standalone display block.
- Avoid complex inline constructs in bullets (for example `\underbrace`, `\begin{cases}`, `\begin{aligned}`); use standalone display math for those.

## Testing Guidelines
- No formal test suite yet; prefer `pytest` under `tests/` for any reusable code.
- For notebooks, include lightweight `assert` checks and seeded RNGs (`numpy.random.default_rng(seed)`) to keep outputs reproducible.
- If you add tests later, run them with `uv run pytest` and document any required data fixtures in `tests/README.md`.

## Commit & Pull Request Guidelines
- Commit messages: short, present-tense summaries with scope tags when useful (e.g., `week03 add normal score proof`, `notes: lecture 14`).
- Keep PRs focused; include a short overview, key file list, and before/after plots or screenshots when visuals change.
- Link the curriculum week or related issue in the PR description; note any new dependencies or data sources.

## Security & Data Hygiene
- Do not store secrets or private datasets in the repo or notebooks; load credentials via environment variables when needed.
- Prefer small, derived datasets checked into version control; keep raw or bulky data in external storage and document access steps.
- Add ignore rules for new tools that generate caches; keep the repo lightweight.

## Skills
A skill is a set of local instructions to follow that is stored in a `SKILL.md` file.

### Available repo skills
- `weekly-diffusion-notebook`: Create or refactor weekly unsolved/solved notebook pairs in `notebooks/` using this repo's `wNN_topic` conventions, reproducibility defaults, and experiment/tutorial templates; scaffold `wNN_topic.ipynb` first and create `wNN_topic_solved.ipynb` as an exact copy for solution work. (file: `.agents/skills/weekly-diffusion-notebook/SKILL.md`)
