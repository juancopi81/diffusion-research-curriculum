# Week 14 Checkpoint — Report, Blog Draft, and Evidence

| File | Purpose |
| --- | --- |
| [report.md](report.md) | Completed Week 14 study deliverable, preserved as committed at checkpoint closeout. |
| [blog_draft.md](blog_draft.md) | Active post manuscript, including the new score-field section; continue blog edits here. |
| [draft.md](draft.md) | Working notes, reviewed answers, and editorial history; this is not the post manuscript. |

The two manuscripts were separated on 2026-10-29 after the author pointed
out that blog edits had been applied to the study deliverable. The current
blog text was preserved before `report.md` was restored byte for byte to
its committed checkpoint version. Figure provenance below covers both files.

During blog editing on 2026-10-26, the author's "Models and Experiments"
roadmap was added before the table, with light language corrections and
links to the existing notes and experiments. Its reviewed wording is also
recorded in the working draft. The author added the closing diffusion
connections and open questions on 2026-10-29; these received a focused
grammar and technical-accuracy review in `blog_draft.md`.

On 2026-10-29, the blog's score section was replaced with the author's
reviewed vector-field interpretation and two saved Week 8 plots. The Week 14
report retains its original clipping passage and figure. The blog's diffusion
connection now focuses on the ingredients still needed for diffusion; the
separate Week 13 training aside was removed in the approved editorial pass.

The author reviewed the draft on 2026-10-26 and said the wording sounds good
so far. The expanded blog now includes transitions, a personal takeaway, and
closing questions. The Week 14 study checkpoint closed on 2026-10-27 after
[Day 7's review and corrections](../../notes/w14_study_plan.md#day-7-completion-decision).
That record distinguishes reference use and guided corrections from unaided
recall. The blog manuscript is retained in `blog_draft.md`.

The local HTML post was created on 2026-10-29 in the sibling blog repository:
`juancopi81.github.io/posts/2026-10-29-vae-realnvp-and-a-score-toy.html`.
It includes the requested AI-use disclosure, the four experiment figures,
Writing and series entries, RSS/sitemap registration, and a generated social
preview. The author accepted the title for now. Desktop/mobile and manuscript
fidelity checks passed. On 2026-10-29, the author approved committing and
pushing the final post and its supporting manuscript files. The site files
were pushed in
[`449fb84`](https://github.com/juancopi81/juancopi81.github.io/commit/449fb840931c5484be47493871b00a0d828adcd5).
The post's public URL is
[VAE, RealNVP, and a Score Toy](https://juancopi81.github.io/posts/2026-10-29-vae-realnvp-and-a-score-toy.html).

The author approved seven focused editorial changes on 2026-10-29. The HTML
and Markdown now share the References section, related-post links, experiment
context, and revised RealNVP interpretation. Figures link to their full-size
images. The title and top AI disclosure remain as approved.

The author then supplied and approved "What I Think I Learned." It appears
before Open Questions in the HTML post and blog draft, ending with the
requested italic "Chapeau!" for RealNVP. The final formatting pass adds sparse
bold emphasis to the model distinctions and preserves the author's emphasis
on "you." Manuscript fidelity and desktop/mobile checks passed after this
addition; the completed study report remains unchanged.

## Figure Provenance

All cell and output indices below are zero-based. PNGs were extracted from
saved output bytes or copied from the existing figure; notebooks were not
executed or modified, and the images were not edited.

| Figure | Saved source | Cell index and ID | Output identity |
| --- | --- | --- | --- |
| [VAE reconstructions](figures/w11_vae_reconstructions.png) | [Week 11 solved notebook](../../notebooks/w11_minimal_vae_mnist_solved.ipynb) | 23, `reconstructions` | Output 0, `display_data`, `image/png`; execution count 16 |
| [RealNVP first-coordinate comparison](figures/w12_realnvp_first_coordinate_comparison.png) | [Week 12 solved notebook](../../notebooks/w12_realnvp_2d_blobs_solved.ipynb) | 20, `9c459c26` | Output 0, `display_data`, `image/png`; execution count 11 |
| [Analytical score field](figures/w08_score_analytical_field.png) | [Existing Week 8 figure](../checkpoint_02_toy_score_matching/figures/true_analytical_vector_field.png) | Not a notebook output | Exact noisy-mixture score; existing PNG from `evaluate.py` |
| [Learned score field](figures/w08_score_learned_field.png) | [Existing Week 8 figure](../checkpoint_02_toy_score_matching/figures/toy_score_matching_exp_20260724_222934_1784932174.2667751_vector_field.png) | Not a notebook output | Saved direct-score run after 20 updates; existing PNG from `evaluate.py` |
| [Score clipping comparison](figures/w13_score_clipping_comparison.png) | [Existing Week 13 figure](../../notes/figures/w13_score_clipping_comparison.png), identical to the [Week 13 solved notebook](../../notebooks/w13_optimizers_sanity_solved.ipynb) output | 29, `s7-results` | Output 1, `display_data`, `image/png`; execution count 16 |

The study report displays the clipping figure; the blog draft displays the
two Week 8 fields. Both use the same VAE and RealNVP figures.

## Verified Run Context

### VAE

Configuration is recorded in Week 11 cell 2 (`setup`), with training in cell
20 (`training`). The run uses MNIST, 10,000 training and 1,000 held-out images,
seed 11, 784 input coordinates, two latent coordinates, hidden width 128,
batch size 128, Adam learning rate 0.001, and five epochs on CPU. The Gaussian
decoder has fixed observation variance 0.1.

The selected panel uses one held-out example of each digit. Its four rows
show inputs, initial reconstructions using encoder means, trained
reconstructions using encoder means, and trained reconstructions using
sampled encoder latents. The decoder displays mean images in every
reconstruction row. Latent sampling in this panel uses seed 18.

### RealNVP

Configuration and data are recorded in Week 12 cell 2 (`b3fad07f`), training
in cell 14 (`bd55c4a5`), and the one-layer comparison in cell 19 (`a2d29281`).
The data use seed 12, 2,000 training and 400 held-out points, four centers at
the combinations of −1.8 and 1.8, and component standard deviation 0.35.
The models use a standard normal base, hidden width 32, batch size 256,
and Adam learning rate 0.002 on CPU.

The six-layer model uses 450 updates and initialization seed 22; the
one-layer model uses 200 updates and initialization seed 32. Their minibatch
generators use seeds 23 and 33, respectively. The plotted model samples use
the same 1,000 base draws, seeded with 17, and are compared with the 400
held-out data points.

Training budgets and training seeds differ between the two models. This
figure is not a controlled depth-only comparison. The unchanged first
coordinate in the one-layer model is an architectural constraint.

### Score Toy — Week 8 Field Comparison

The [Week 8 report](../checkpoint_02_toy_score_matching/report.md) records
the selected direct-score run,
`toy_score_matching_exp_20260724_222934_1784932174.2667751`.
It uses 1,500 points from three equally weighted Gaussian components,
an 80/20 training/validation split, seed 42, a 2–32–32–2 ReLU MLP, and
full-batch SGD with learning rate 0.1 for 20 updates. The clean component
standard deviation and corruption standard deviation are both 0.5.
The reported final held-out marginal-score MSE is 1.407152.

The [evaluation code](../checkpoint_02_toy_score_matching/evaluate.py)
forms the analytical noisy-mixture score using the sum of the clean and
corruption variances. The grid spans −4 to 4 on each axis with 30 points
per axis; both plots use quiver scale 50. The blue background dots are
clean data. The learned arrows are direct score predictions, and the
plots do not show generated samples or a reverse sampler.

Both PNGs were copied unchanged from the saved figures on 2026-10-29.
No training or evaluation was rerun for this revision.

### Score Toy — Retained Week 13 Clipping Evidence

The [Week 13 stability note](../../notes/w13_training_stability_for_diffusion.md)
is the reference for the study report's selected result. Notebook cells 21 (`s7-setup`),
23 (`s7-matching`), 28 (`s7-runner`), and 29 (`s7-results`) record the paired
configuration and saved comparison.

Both conditions use 1,200 training and 300 held-out points from the same
Gaussian-blob construction, corruption standard deviation 0.5, plain SGD
learning rate 0.1, and 20 updates on CPU. Data, split, and initialization
seeds are 42; the shared fresh training-noise sequence uses seed 43, and the
fixed held-out noisy set uses seed 44. The intervention is global L2
parameter-gradient clipping off versus a threshold of 0.5.

Training MSE uses conditional Gaussian corruption scores; held-out MSE uses
the analytical marginal score of the noisy mixture. Both metrics average
over examples and coordinates. The final held-out score MSE is 1.240304
without clipping and 1.345339 with clipping, from a shared initial value of
1.869517. These are Week 13 measurements, not the earlier Week 8 run's
results. No reverse sampler is implemented in this comparison.

### Comparison Scope

The three experiments use different datasets and training objectives; their
raw loss values do not form a matched benchmark or rank the model families.
The report and blog draft compare what each approach learns and the saved
evidence from its own experiment.

## SHA256 Audit

Hashes record the saved sources used for this assembly.

| Repository source | SHA256 |
| --- | --- |
| `notebooks/w11_minimal_vae_mnist_solved.ipynb` | `80290078d2943b1bfc9878aa7b81de80f3763c36f81186ee512230b8414ed8f2` |
| `notebooks/w12_realnvp_2d_blobs_solved.ipynb` | `da0a4d0bd3beceabb8328585637a99decc3c6b702a704c3db938beb8b72e898f` |
| `notebooks/w13_optimizers_sanity_solved.ipynb` | `f8a996e8d04433693cef13c7a87da5bb3db1e54c4b27dea5b48f75a76ce944b8` |
| `notes/figures/w13_score_clipping_comparison.png` | `f2ee20b68e061594bf8ad159211af9792be41898e0c33e0b47a990ad32143646` |
| `notes/w13_training_stability_for_diffusion.md` | `a0cce7a360b3e7ef005d87e64ed575bab5e230e087b384a10ecb85e297c5c667` |
| `notes/w06_stat110_transformations_convolutions.md` | `8cf0ab0e7ae8e66c3cfdc330b9f4fed890dc28a0d0b7c3b19b70c97ae1a1a908` |
| `mini_projects/checkpoint_02_toy_score_matching/report.md` | `32fb00976f1693862304ee75344f7d0ff55c36c213fa2ac54f6ec0a986b690f5` |
| `mini_projects/checkpoint_02_toy_score_matching/evaluate.py` | `6f75c57e79cbf920d2b24fbba7fc08fd1b354b292a6a6dfc13cf672bf414df17` |

The Week 11, Week 12, and retained Week 13 PNGs match their saved notebook
outputs byte for byte. The two Week 8 PNGs and the Week 13 clipping PNG
also match their existing source figures byte for byte.

| Local figure | Dimensions (pixels) | Bytes | SHA256 |
| --- | --- | --- | --- |
| `w11_vae_reconstructions.png` | 1308 × 575 | 67,052 | `ea2c2f704c3904e7f97e4c0094ccd570eddab74104709bfe4b4e2b0b09877cae` |
| `w12_realnvp_first_coordinate_comparison.png` | 990 × 390 | 64,142 | `864e5a4f5203f74acdb492fc00abbe8c24183f1bbba0b9ca41584efc0dc18b5e` |
| `w08_score_analytical_field.png` | 2370 × 2369 | 1,721,283 | `82964c3f518a25976bef6ffe92707419b496c85f920639473876596e15082ffc` |
| `w08_score_learned_field.png` | 2370 × 2369 | 866,780 | `77dc5bcbdc71df29dde31b3de6626b7bf79ff8d498a53435dd28d603c895ec0d` |
| `w13_score_clipping_comparison.png` | 1552 × 430 | 109,116 | `f2ee20b68e061594bf8ad159211af9792be41898e0c33e0b47a990ad32143646` |
