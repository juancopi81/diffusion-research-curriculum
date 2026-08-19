# Paper Radar

This file is the lightweight queue for papers that may shape future work but do
not yet belong in the core curriculum.

- Keep a paper here while it is a promising direction rather than an active
  reading or replication task.
- Promote it to `papers/<paper_slug>.md` only after a deep read, derivation, or
  experiment gives us an authored artifact worth preserving.
- Change `CURRICULUM.md` only when a paper has earned a concrete role in a
  scheduled session or milestone.

## Radar

| Status | Paper | Why it is on the radar | Revisit trigger |
| --- | --- | --- | --- |
| Radar | Lourie et al., [*Small-Scale Experiments: Are We There Yet?*](https://arxiv.org/abs/2608.11859v1) | A methodology for learning about larger models from well-tuned small-scale experiments, with useful warnings about hyperparameter sensitivity and extrapolation. | Nano-Diffusion has one stable baseline, repeatable training runs, configuration logging, and enough compute budget for a real sweep across several model sizes. |

### Small-Scale Experiments: Are We There Yet?

- Authors: Nicholas Lourie, Kyunghyun Cho, Karen Ullrich, and Sanae Lotfi
- arXiv: `2608.11859v1` (`cs.LG`), submitted August 12, 2026
- DOI: [10.48550/arXiv.2608.11859](https://doi.org/10.48550/arXiv.2608.11859)
- Source status: verified against the official v1 arXiv metadata and 29-page PDF
  on August 14, 2026
- License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

#### What the paper establishes

The paper studies transformer language-model pretraining from 4M to 268M
effective parameters. Its main result is not merely that small experiments can
scale: the scaling law appears only near the fully tuned frontier. In the
authors' sweep, 4 or 16 configurations per scale hide the law, 64 make it
visible but imprecise, and 256 produce an accurate estimate (Section 3.2).

The authors also find that models become less sensitive to hyperparameters as
parameter count and data grow together. They interpret this through a decline
in the intrinsic dimension of the hyperparameter loss surface (Section 4).
Their proposed workflow is therefore to explore and tune thoroughly at small
scale, check that the expected diagnostics actually emerge, and only then
carry the better model upward (Section 5.1).

The limit matters: far extrapolation magnifies statistical error, and the
paper's pretraining-loss argument assumes fixed data. The evidence is for
model-centric transformer research, not for changing datasets or for diffusion
models directly (Sections 5.2 and 7).

#### Why it may matter for this repository

Our working hypothesis is that the methodology could strengthen the
Nano-Diffusion experiment spine. Instead of treating a single tiny run as
evidence about a larger model, we could eventually:

1. hold the dataset, objective, and evaluation protocol fixed;
2. define a small ladder of model and training-compute scales;
3. search the same hyperparameter space at every scale and retain the full run
   distribution, not only the winner;
4. reserve the largest affordable scale as a held-out transfer check; and
5. compare trends near observed scales rather than trusting a long-range point
   extrapolation.

That is an application hypothesis, not a result established by the paper. A
future pilot should first test whether diffusion loss, sample quality, and the
relevant hyperparameter surface behave regularly enough for this framework to
be useful.

#### First useful return point

Revisit this paper after the first image-level Nano-Diffusion baseline is
stable and repeated runs produce comparable metrics. At that point, use it to
design a bounded scaling pilot before spending effort on larger architectures
or broad ablations. Until then, it stays on the radar and does not expand the
current study sequence.
