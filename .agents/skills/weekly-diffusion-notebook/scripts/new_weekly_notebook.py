from __future__ import annotations

import argparse
import copy
import json
import re
import shutil
from pathlib import Path
from typing import Any


def find_repo_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / ".git").exists():
            return candidate
    return start


def normalize_topic(topic: str) -> str:
    text = topic.strip().lower()
    text = re.sub(r"^w\d{2}_", "", text)
    text = re.sub(r"[^a-z0-9]+", "_", text).strip("_")
    return text or "topic"


def title_from_topic(topic_slug: str) -> str:
    return " ".join(word.capitalize() for word in topic_slug.split("_"))


def load_template(skill_dir: Path, mode: str) -> dict[str, Any]:
    template_name = "experiment-template.ipynb" if mode == "experiment" else "tutorial-template.ipynb"
    template_path = skill_dir / "assets" / template_name
    if not template_path.exists():
        raise SystemExit(f"Missing template: {template_path}")
    with template_path.open("r", encoding="utf-8") as handle:
        notebook = json.load(handle)
    if not isinstance(notebook, dict):
        raise SystemExit(f"Unexpected template format: {template_path}")
    return notebook


def replace_tokens(text: str, tokens: dict[str, str]) -> str:
    out = text
    for key, value in tokens.items():
        out = out.replace(f"{{{{{key}}}}}", value)
    return out


def apply_tokens(notebook: dict[str, Any], tokens: dict[str, str]) -> dict[str, Any]:
    data = copy.deepcopy(notebook)
    cells = data.get("cells")
    if not isinstance(cells, list):
        raise SystemExit("Template notebook has invalid or missing cells.")

    for cell in cells:
        source = cell.get("source", [])
        if isinstance(source, str):
            lines = [source]
        elif isinstance(source, list):
            lines = [str(line) for line in source]
        else:
            lines = []
        cell["source"] = [replace_tokens(line, tokens) for line in lines]
        cell.setdefault("metadata", {})
        if cell.get("cell_type") == "code":
            cell.setdefault("execution_count", None)
            cell.setdefault("outputs", [])

    metadata = data.setdefault("metadata", {})
    if isinstance(metadata, dict):
        kernelspec = metadata.setdefault("kernelspec", {})
        if isinstance(kernelspec, dict):
            kernelspec.setdefault("display_name", "Python 3")
            kernelspec.setdefault("language", "python")
            kernelspec.setdefault("name", "python3")
        language_info = metadata.setdefault("language_info", {})
        if isinstance(language_info, dict):
            language_info.setdefault("name", "python")
            language_info.setdefault("version", "3.11")

    data.setdefault("nbformat", 4)
    data.setdefault("nbformat_minor", 5)
    return data


def output_paths(repo_root: Path, week_pad: str, topic_slug: str, out_dir: Path | None) -> tuple[Path, Path]:
    base_dir = (out_dir.resolve() if out_dir else (repo_root / "notebooks").resolve())
    base_name = f"w{week_pad}_{topic_slug}"
    return base_dir / f"{base_name}.ipynb", base_dir / f"{base_name}_solved.ipynb"


def write_notebook(path: Path, notebook: dict[str, Any], force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing notebook without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(notebook, handle, indent=2)
        handle.write("\n")


def copy_notebook(src: Path, dst: Path, force: bool) -> None:
    if dst.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing notebook without --force: {dst}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scaffold weekly unsolved/solved notebook pairs for this repo.")
    parser.add_argument("--week", type=int, required=True, help="Week number, for example 4.")
    parser.add_argument("--topic", required=True, help="Topic slug or text; will normalize to lowercase underscore style.")
    parser.add_argument(
        "--title",
        default=None,
        help="Notebook title shown in the first markdown cell. Defaults to a title made from --topic.",
    )
    parser.add_argument(
        "--mode",
        choices=["experiment", "tutorial"],
        default="experiment",
        help="Notebook mode to scaffold (default: experiment).",
    )
    parser.add_argument("--seed", type=int, default=None, help="Seed for template setup cells (default: week number).")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Output directory (default: <repo>/notebooks).",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite outputs if they already exist.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.week < 1 or args.week > 99:
        raise SystemExit("Week must be between 1 and 99.")

    week_pad = f"{args.week:02d}"
    topic_slug = normalize_topic(args.topic)
    title = args.title.strip() if args.title else title_from_topic(topic_slug)
    seed = args.seed if args.seed is not None else args.week

    script_path = Path(__file__).resolve()
    skill_dir = script_path.parents[1]
    repo_root = find_repo_root(skill_dir)

    template = load_template(skill_dir, args.mode)
    unsolved_path, solved_path = output_paths(repo_root, week_pad, topic_slug, args.out_dir)

    common_tokens = {
        "WEEK": str(args.week),
        "WEEK_PAD": week_pad,
        "TOPIC_SLUG": topic_slug,
        "TITLE": title,
        "SEED": str(seed),
    }

    tokens = {
        **common_tokens,
        "PAIR_ROLE": "**Workflow**: this file is the TODO scaffold. The `_solved` notebook is an exact copy you will solve.",
        "WORK_PREFIX": "TODO",
        "DONE_NOTE": "Copy is created as `_solved`; solve that notebook and keep this one as the TODO baseline.",
    }

    write_notebook(unsolved_path, apply_tokens(template, tokens), args.force)
    copy_notebook(unsolved_path, solved_path, args.force)

    print(f"Wrote {unsolved_path}")
    print(f"Wrote {solved_path}")


if __name__ == "__main__":
    main()
