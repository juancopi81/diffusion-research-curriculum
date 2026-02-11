"""Week 4 S3 checkpoint: Monte Carlo for biased Monty Hall switching.

This script estimates three probabilities for the "always switch" strategy:
1) P(W)
2) P(W | D2)
3) P(W | D3)

Where:
- W: switching wins
- D2: Monty opens Door 2
- D3: Monty opens Door 3

Run examples:
    uv run python mini_projects/checkpoint_01_conditioning_in_code/simulate.py
    uv run python mini_projects/checkpoint_01_conditioning_in_code/simulate.py --p 0.9 --trials 300000
    uv run python mini_projects/checkpoint_01_conditioning_in_code/simulate.py --grid 0.5,0.7,0.9,1.0
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass
class SimulationRow:
    p: float
    trials: int
    opened_door2_count: int
    opened_door3_count: int
    est_p_switch_win: float
    est_p_switch_win_given_d2: float
    est_p_switch_win_given_d3: float
    th_p_switch_win: float
    th_p_switch_win_given_d2: float
    th_p_switch_win_given_d3: float
    abs_err_switch_win: float
    abs_err_switch_win_given_d2: float
    abs_err_switch_win_given_d3: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Monte Carlo for biased Monty Hall.")
    parser.add_argument(
        "--p",
        type=float,
        default=0.75,
        help="Monty's preference to open Door 2 when he has a choice (default: 0.75).",
    )
    parser.add_argument(
        "--trials",
        type=int,
        default=200_000,
        help="Number of Monte Carlo games (default: 200000).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=4,
        help="RNG seed for reproducibility (default: 4).",
    )
    parser.add_argument(
        "--grid",
        type=str,
        default="",
        help="Optional comma-separated p values, e.g. 0.5,0.7,0.9,1.0",
    )
    parser.add_argument(
        "--csv",
        type=str,
        default="",
        help="Optional output CSV path.",
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Use a fast sanity run (trials=30000, grid=0.5,0.75,0.9,1.0).",
    )
    return parser.parse_args()


def validate_p(p: float) -> None:
    if not (0.5 <= p <= 1.0):
        raise ValueError(f"Expected p in [0.5, 1.0], got {p}.")


def theoretical_probabilities(p: float) -> tuple[float, float, float]:
    """Return theoretical values for (P(W), P(W|D2), P(W|D3))."""
    validate_p(p)
    p_switch_win = 2.0 / 3.0
    p_switch_win_given_d2 = 1.0 / (1.0 + p)
    p_switch_win_given_d3 = 1.0 / (2.0 - p)
    return p_switch_win, p_switch_win_given_d2, p_switch_win_given_d3


def simulate_once(p: float, trials: int, seed: int) -> SimulationRow:
    """Run one Monte Carlo experiment for a fixed p."""
    validate_p(p)
    if trials <= 0:
        raise ValueError(f"Expected trials > 0, got {trials}.")

    rng = np.random.default_rng(seed)

    # Car locations: 1, 2, 3 with equal probability.
    car = rng.integers(1, 4, size=trials)

    # Contestant always picks Door 1.
    # Monty opens:
    # - If car is behind Door 1: opens Door 2 with prob p, Door 3 with prob (1-p).
    # - If car is behind Door 2: must open Door 3.
    # - If car is behind Door 3: must open Door 2.
    opened = np.empty(trials, dtype=np.int8)
    mask_c1 = car == 1
    mask_c2 = car == 2
    mask_c3 = car == 3

    choices_c1 = rng.random(np.sum(mask_c1))
    opened[mask_c1] = np.where(choices_c1 < p, 2, 3)
    opened[mask_c2] = 3
    opened[mask_c3] = 2

    # If contestant switches from Door 1:
    # - if Monty opened Door 2, switch to Door 3
    # - if Monty opened Door 3, switch to Door 2
    switched_to = np.where(opened == 2, 3, 2)
    switch_win = switched_to == car

    mask_d2 = opened == 2
    mask_d3 = opened == 3
    count_d2 = int(np.sum(mask_d2))
    count_d3 = int(np.sum(mask_d3))

    est_switch_win = float(np.mean(switch_win))
    est_switch_win_given_d2 = float(np.mean(switch_win[mask_d2])) if count_d2 else float("nan")
    est_switch_win_given_d3 = float(np.mean(switch_win[mask_d3])) if count_d3 else float("nan")

    th_switch_win, th_switch_win_given_d2, th_switch_win_given_d3 = theoretical_probabilities(p)

    return SimulationRow(
        p=p,
        trials=trials,
        opened_door2_count=count_d2,
        opened_door3_count=count_d3,
        est_p_switch_win=est_switch_win,
        est_p_switch_win_given_d2=est_switch_win_given_d2,
        est_p_switch_win_given_d3=est_switch_win_given_d3,
        th_p_switch_win=th_switch_win,
        th_p_switch_win_given_d2=th_switch_win_given_d2,
        th_p_switch_win_given_d3=th_switch_win_given_d3,
        abs_err_switch_win=abs(est_switch_win - th_switch_win),
        abs_err_switch_win_given_d2=abs(est_switch_win_given_d2 - th_switch_win_given_d2),
        abs_err_switch_win_given_d3=abs(est_switch_win_given_d3 - th_switch_win_given_d3),
    )


def parse_grid(grid_arg: str) -> list[float]:
    values = [x.strip() for x in grid_arg.split(",") if x.strip()]
    if not values:
        return []
    parsed = [float(v) for v in values]
    for p in parsed:
        validate_p(p)
    return parsed


def run_grid(p_values: list[float], trials: int, seed: int) -> list[SimulationRow]:
    rows: list[SimulationRow] = []
    for i, p in enumerate(p_values):
        rows.append(simulate_once(p=p, trials=trials, seed=seed + i))
    return rows


def print_row(row: SimulationRow) -> None:
    print(f"p = {row.p:.3f} | trials = {row.trials:,}")
    print(
        "  P(W):"
        f" est={row.est_p_switch_win:.6f}"
        f" theory={row.th_p_switch_win:.6f}"
        f" abs_err={row.abs_err_switch_win:.6f}"
    )
    print(
        "  P(W|D2):"
        f" est={row.est_p_switch_win_given_d2:.6f}"
        f" theory={row.th_p_switch_win_given_d2:.6f}"
        f" abs_err={row.abs_err_switch_win_given_d2:.6f}"
        f" (count D2={row.opened_door2_count:,})"
    )
    print(
        "  P(W|D3):"
        f" est={row.est_p_switch_win_given_d3:.6f}"
        f" theory={row.th_p_switch_win_given_d3:.6f}"
        f" abs_err={row.abs_err_switch_win_given_d3:.6f}"
        f" (count D3={row.opened_door3_count:,})"
    )
    print()


def write_csv(rows: list[SimulationRow], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "p",
                "trials",
                "opened_door2_count",
                "opened_door3_count",
                "est_p_switch_win",
                "est_p_switch_win_given_d2",
                "est_p_switch_win_given_d3",
                "th_p_switch_win",
                "th_p_switch_win_given_d2",
                "th_p_switch_win_given_d3",
                "abs_err_switch_win",
                "abs_err_switch_win_given_d2",
                "abs_err_switch_win_given_d3",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(row.__dict__)


def main() -> None:
    args = parse_args()

    if args.quick:
        trials = 30_000
        p_values = [0.5, 0.75, 0.9, 1.0]
    else:
        trials = args.trials
        p_values = parse_grid(args.grid) if args.grid else [args.p]

    rows = run_grid(p_values=p_values, trials=trials, seed=args.seed)
    for row in rows:
        print_row(row)

    if args.csv:
        out_path = Path(args.csv)
        write_csv(rows, out_path)
        print(f"Wrote CSV to: {out_path}")

    # TODO (learning extension 1):
    # Add the "always stay" strategy and compare it against "always switch."
    #
    # TODO (learning extension 2):
    # Add 95% confidence intervals for each estimated probability.
    #
    # TODO (learning extension 3):
    # Run repeated experiments (same p, same trials, different seeds) and
    # summarize the distribution of Monte Carlo error.


if __name__ == "__main__":
    main()
