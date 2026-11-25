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
| Radar | Kumbong et al., [*Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation*](https://arxiv.org/abs/2610.14162v1) | Connects learned discrete representations, hierarchical generation, and sampling efficiency; a useful comparison with diffusion language models. | After the Weeks 19–20 DDPM/DDIM comparison, with a short VQ-VAE and discrete text-diffusion primer. |
| Radar | Jia et al., [*LLaCO: Continuous Diffusion for Large Language Models with Competition-Aware Semantic Scheduling*](https://arxiv.org/abs/2610.32604v1) | Connects embedding geometry, token identity loss, and noise scheduling; a direct diffusion-language-model companion. | After the Weeks 23–24 schedule ablations, with a short primer on normalized token embeddings and continuous text diffusion. |
| Radar | Hoover et al., [*Classical Energies Learn to Reason 1,000x Faster than Looped Models*](https://arxiv.org/abs/2611.17309v1) | Energy-based inference, local constraint learning, and a useful warning about what reasoning benchmarks establish. | After the Weeks 33–34 score-SDE work, with a short primer on Hopfield networks and pairwise energy models. |
| Radar | Patel, [*Tessera-small*](https://huggingface.co/thejagstudio/tessera-small) (model and demo) | Makes discrete diffusion visible through confidence-guided unmasking of palette tokens on a 16×16 sprite. | After the Weeks 19–20 DDPM/DDIM comparison, trace one sprite through its sampling rounds. |
| Radar | Chng et al., [*Looped Diffusion Transformer*](https://arxiv.org/abs/2609.40305v1) | Tests whether compute is better spent repeating shared blocks inside the denoiser or taking more sampling steps. | Revisit alongside the Weeks 25–26 DiT reading once the MNIST baseline is reproducible. |
| Radar | Zhou et al., [*Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model*](https://arxiv.org/abs/2408.11039) | Shows how next-token text prediction and image diffusion can share a transformer; connects the curriculum to multimodal systems. | After the Weeks 25–26 architecture bridge, if a question about combining objectives warrants optional follow-up. |
| Radar | Chefer et al., [*Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis*](https://bfl.ai/techblog/self-flow/index.html) (Self-Flow) | Connects representation learning with flow-based generation across images, video, and audio. | After the Weeks 39–40 bridge report, if representation learning is relevant to the later project choice. |
| Radar | Black et al., [*π₀: A Vision-Language-Action Flow Model for General Robot Control*](https://arxiv.org/abs/2410.24164) | Connects a pretrained vision-language model to flow-based action generation; helps distinguish a policy from a predictive world model. | After the Weeks 39–40 bridge report, if action generation or robotics remains an interest. |

### World models and multimodal generation

Orientation added on 2026-11-17 from primary abstracts and project overviews
for Transfusion, Self-Flow, and π₀; full paper reviews and replications remain
pending. **[DiT]** and **[V-JEPA2]** have short, scheduled roles in the
[curriculum](../CURRICULUM.md#architecture-and-world-model-bridges); the three
radar entries above are optional follow-up, not additional assigned reading.

The useful comparison is between generating observations, predicting learned
representations or future states, and generating actions. π₀ supplies an
action policy; this alone does not make it a next-state dynamics model.
For any later experiment, ask what the model predicts, what evidence supports
its usefulness, and which failures the evaluation can detect. Visual quality
alone does not establish physical accuracy or planning ability.

Revisit these directions when selecting the Weeks 45–48 project and a target
role. Larger expansions into 3D geometry, robotics, or planning stay beyond
the core curriculum unless a bounded project fits the existing scope and
budget. Keep observations and decisions in the existing notes and project
reports.

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

### Next-Concept Modeling

- Authors: Hermann Kumbong et al.
- arXiv: `2610.14162v1` (`cs.CL`), submitted October 9, 2026
- Source status: initial triage against the official arXiv metadata and
  [v1 HTML](https://arxiv.org/html/2610.14162v1), especially Section 3,
  Section 4.6, and Appendices C and I, on October 19, 2026

#### Why it may matter for this repository

NCM first learns a text tokenizer using multiscale residual vector
quantization, then trains a transformer to generate code levels in order,
predicting positions within each level in parallel (Section 3). This is
hierarchical latent generation; its connection to diffusion is a comparison
of generation strategies.

Our curriculum connection is the [Week 11 latent-representation
bridge](../notes/w11_why_latent_diffusion.md): how does the representation
change the work left for the generator? It also gives us a future comparison
for the [Weeks 19–20 sampling work](../CURRICULUM.md), separating fewer
sequential steps from cheaper steps.

#### Evidence to revisit

The authors report 10–31× faster generation than selected diffusion baselines.
These are task-specific results; Section 4.6 benchmarks sampling on one H100
at batch size 16. Main generators have roughly 100M parameters, with additional
parameters and training costs for the tokenizer (Appendices C and I).
Evaluate quality, diversity, tokenizer overhead, and latency together when
revisiting these claims.

#### First useful return point

Revisit after the Weeks 19–20 DDPM/DDIM comparison, adding a short primer on
VQ-VAE and discrete diffusion for text. First reading question: how much of the
advantage comes from the representation, the generation order, and the cost
per step? Keep this as optional enrichment until a concrete experiment emerges.

### LLaCO

- Authors: Zijian Jia et al.
- arXiv: `2610.32604v1` (`cs.AI`), submitted October 23, 2026
- Source status: initial triage against the official arXiv metadata and
  [v1 HTML](https://arxiv.org/html/2610.32604v1), especially Sections 3–5
  and Appendices 9.2 and 10, on October 27, 2026

#### Why it may matter for this repository

The authors study how token identity disappears as continuous embeddings are
corrupted. They use directional competition to motivate spherical noising and
Semantic Retention Scheduling, allocating time according to identity loss
(Sections 3–4).

For our curriculum, the useful question is whether evenly spaced noise levels
produce evenly spaced changes in what the denoiser must recover. This connects
directly to the [Weeks 23–24 schedule and loss-weighting
ablations](../CURRICULUM.md). Our possible application is a small experiment
measuring identity retention under different schedules; transfer to our image
or Gaussian-mixture models would need separate evidence.

#### Evidence to revisit

Reported gains use an adapted 8B pretrained model; the main comparison excludes
its original hybrid backbone (Appendix 10.2). Default decoding uses four model
evaluations per four-token block (Section 5.1). A future review should separate
scheduling effects from initialization and assess total generation cost.

#### First useful return point

Revisit after the Weeks 23–24 controlled ablations, with a short primer on
normalized token embeddings and continuous diffusion for text. Start with the
geometry and scheduling argument, then inspect the ablations and their controls.
The detailed theory can remain optional until we have a concrete question to
test. This stays on the radar as complementary reading.

### Classical Energies Learn to Reason 1,000x Faster than Looped Models

- Authors: Benjamin Hoover, Hugh Blayney, and James C. R. Whittington
- arXiv: `2611.17309v1` (`cs.AI`), submitted November 12, 2026
- Source status: initial triage against the official arXiv metadata and
  [v1 HTML](https://arxiv.org/html/2611.17309v1), especially Sections 3–5
  and Appendices B, C.2, and C.4, on November 16, 2026; results not replicated

#### Why it may matter for this repository

CRAM learns a Hopfield-style pairwise energy from solved puzzles, primarily
using pseudolikelihood without backpropagating through the inference search.
At inference, it searches the energy with puzzle clues fixed and uses explicit
stopping tests (Section 3).

Our connection is conceptual: compare learning an energy and searching it with
learning a noise-conditioned score and sampling from it. The paper studies
discrete constraint puzzles; transfer to diffusion would need separate evidence.
It could be useful companion reading after the [Weeks 33–34 score-SDE
work](../CURRICULUM.md).

#### Evidence to revisit

The authors report near-perfect Sudoku-Extreme and Maze-Unique accuracy with
millisecond-scale training on one H200 (Table 2). Read the headline with three
qualifications:

- The benchmarks admit simple pairwise constraints; performance does not
  establish general reasoning ability (Section 5).
- CRAM fit times use warm runs; long baseline fits include startup costs
  (Appendix C.2).
- Maze-Unique depends on initialization: the empty board has lower energy
  than the solution, so inference is not simply global energy minimization
  (Appendix C.4).

#### First useful return point

Revisit after the Weeks 33–34 score-SDE work, with a short Hopfield/pairwise-energy
primer. First question: which benefits come from the learned energy, the search
procedure, and the task structure? Keep this as optional enrichment on the radar.

### Tessera-small

Initial review on 2026-11-19 of Jagrat Patel's model card and sampler, following
[Sayak Paul's post](https://x.com/RisingSayak/status/2123427418367266990).
Each pixel is a token from a learned 512-entry palette, including transparency.
The text-conditioned model starts with all 256 pixels masked. In each round,
it proposes colors in parallel and commits a subset based on confidence. A
cosine schedule controls how many positions stay masked over roughly 16 rounds.
[Model card](https://huggingface.co/thejagstudio/tessera-small) ·
[Sampler source](https://huggingface.co/spaces/thejagstudio/tessera-pixel-studio/blob/main/tessera/sampler.py)

After the Weeks 19–20 DDPM/DDIM comparison, use the browser demo to trace one
sprite and compare it with the [Week 16 reverse loop](../notes/w16_hf_ddpm_training.md#day-3--sampling-from-a-trained-ddpm).
In DDPM the state is a noisy real-valued image at each step. In Tessera it is a
partially filled grid of color tokens. Ask which decisions the schedule makes
(how many pixels to reveal) and which the model's predictions guide (where and
what to reveal). The model card reports 47.6M parameters and about 5.5 hours of
training on an RTX PRO 6000 Blackwell using 1.4M sprites. Start with the demo and
sampler walkthrough. [Slack Moji demo](https://huggingface.co/spaces/cfahlgren1/slack-moji)

### Looped Diffusion Transformer

Inkling 2 Mini reuses its middle layers three times per token. Chng et al.
study the corresponding idea in image diffusion. At a fixed noise level, a
shared block gets several passes to refine the image features before the
sampler advances. In Figure 6, four passes outperformed spending the same
inference compute on additional sampling steps in the settings tested.
Table 4 shows a modest gain from looping alone, with larger gains when the
authors also supervised intermediate predictions and modulated attention.
[Inkling 2 Mini release](https://thinkingmachines.ai/news/inkling-2-mini/) ·
[Looped-DiT, Sections 3.2–3.3](https://arxiv.org/html/2609.40305v1)

Juan’s Week 16 question was whether seeing more of a digit would help the
denoiser connect fragmented strokes. An optional MNIST test would compare the
current single middle convolution with three passes through that convolution
and with three separately learned convolutions. Both deeper variants see a
nominal 17×17 region per output pixel, up from 9×9. Comparing them at the
same depth tests what weight sharing contributes. Use the same starting noise
to compare stroke continuity and record sampling time.
[Week 16 discussion](../notes/w16_hf_ddpm_training.md#what-i-would-test-next)

**Can the first pass guide the last?** Liu et al.’s LoopCD amplifies the change
in a language model’s next-token prediction between an early and a late pass.
The analogy to classifier-free guidance is the extrapolation. CFG varies the
conditioning, while LoopCD holds the input fixed and varies the depth.
[LoopCD, Section 3](https://arxiv.org/html/2610.02185v1) ·
[Inkling follow-up discussed by Peter Baylies](https://x.com/pbaylies/status/2125449107820974571)

Wang and An tested this directly in image generation. Their distilled
four-step SD3-medium student used an early prediction from the same forward
pass to guide the final one. GenEval rose from 0.592 to 0.643 as compute
increased from 7.21 to 7.79 TFLOPs per image. If the MNIST experiment produces
usable noise estimates at both depths, compare ordinary final-pass sampling
with amplifying the final-minus-early difference on the same checkpoint and
seeds. Check both stroke continuity and whether the samples still cover a
variety of digits. [*Distill to Loop*, Table 4 and Appendix C.1](https://arxiv.org/html/2611.31977v1)
