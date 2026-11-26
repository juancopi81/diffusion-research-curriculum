# Week 17 — From the DDPM Paper to Nano-Diffusion

**Week of November 23–29, 2026.** Days 1–3 are complete. The
[concept note](w17_ddpm_posterior_and_objective.md) connects the notebook,
posterior, reverse mean, and loss. The [worked derivation](../proofs/w17_ddpm_worked_derivation.md)
preserves the handwritten steps and tutoring discussion.
Day 4 opens with a [short read-through of the reverse step](#day-4--move-the-working-pieces-into-nano-diffusion).

**Concept-note read-through.** Juan read Days 1–2 and was happy with them.
On 2026-11-26 he read and approved the revised
[Day 3 explanation of the tower property and linearity](w17_ddpm_posterior_and_objective.md#day-3--averaging-over-possible-clean-images).
After each new concept section is drafted, share it
for a read-through and record Juan’s feedback or approval here.

Week 16 and Phase 2 are complete. You already have a working DDPM that
trains on MNIST and generates images from Gaussian noise. The
[Week 16 review](w16_hf_ddpm_training.md#day-6--reviewing-the-ddpm-workflow)
leaves two theory questions open: how the clean-conditioned Gaussian
posterior supplies its mean and variance, and how averaging over possible
clean images relates to the reverse mean. This week connects those
questions to the code you wrote.

**Pacing:** Six sessions totaling **5 hours 50 minutes of active study**,
plus an optional Sunday buffer. Days 1 and 6 are short. Days 4 and 5 have
more space for implementation and a run from a fresh process. Track run
time separately. The first block of each day is a place to pause if you
only have a short window.

## What This Week Produces

- A [concept reference](w17_ddpm_posterior_and_objective.md) on the
  posterior, sampling update, and noise loss, with a [worked companion](../proofs/w17_ddpm_worked_derivation.md)
  for your attempts, hints, and corrections.
- A first version of `mini_projects/nano_diffusion/` that runs with one
  explicit config and one documented command from a fresh process. Reuse
  the Week 16 MNIST data setup, TinyDenoiser, training step, and sampler.
- A quick reference run with saved config, loss, sample grids, and
  timing. [Weeks 17–18 curriculum](../CURRICULUM.md#weeks-1718--ddpm-from-scratch-clean-baseline)

**Working rhythm.** Try the derivation or implementation first, then bring
your reasoning and the point where you got stuck. We'll review one question
at a time. Use the Week 16 notebook as a reference once you have a route
in mind. Keep assistance and unresolved questions with the relevant
worked step. Count the correct run and its evidence as the engineering result,
even if the digits still look rough.

## Reading Map

| Reference | When to use it |
| --- | --- |
| [Ho, Jain, and Abbeel, DDPM, Algorithms 1 and 2](https://arxiv.org/pdf/2006.11239#page=4) | Day 1. Read both algorithms and match them to your Week 16 functions. |
| [DDPM, Section 2, Equations 4–7](https://arxiv.org/pdf/2006.11239#page=2) | Day 2. Use Equation 4 for the forward Gaussian. Compare your posterior attempt with Equations 6–7 on the next page. |
| [DDPM, Section 3.2](https://arxiv.org/pdf/2006.11239#page=3) and [Section 3.4](https://arxiv.org/pdf/2006.11239#page=4) | Day 3. Focus on the fixed-variance Gaussian comparison in Equation 8, the mean in Equation 11, the weighted error in Equation 12, and the simplified loss in Equation 14. |
| [Week 4 completing the square](w04_conditioning_in_diffusion.md#checkpoint-22-complete-the-square-step-by-step), [Week 7 tower property](w07_conditional_expectation_in_diffusion.md#3-tower-property-averaging-after-conditioning), and [Week 15 forward conditional](w15_forward_process_discrete.md#the-direct-conditional-distribution) | Days 2–3. Open the specific prerequisite when needed. |
| [Week 16 working notebook](../notebooks/w16_train_tiny_ddpm_mnist_solved.ipynb) and [Annotated Diffusion, Sampling](https://huggingface.co/blog/annotated-diffusion#sampling) | Days 1 and 4. The notebook is our behavior reference. The blog is a lookup for implementation details. Its code starts noisy indices at zero, while our mathematical convention reserves zero for the clean state. |

## Day-by-Day Schedule

| Day | Date | Budget | Focus | Stop when |
| --- | --- | --- | --- | --- |
| 1 | Mon Nov 23 | 45 min | Read DDPM through your own code | You can point to the notebook function behind each major step in Algorithms 1 and 2. |
| 2 | Tue Nov 24 | 60 min | Derive the clean-conditioned posterior | You have the mean and variance for $t>1$ and can explain the clean boundary at $t=1$. |
| 3 | Wed Nov 25 | 55 min | Connect the posterior to the model and loss | You can explain how predicted noise gives the reverse mean and where the simplified noise loss drops weights. |
| 4 | Thu Nov 26 | 70 min | Extract the Week 16 baseline | The core functions run outside the notebook and agree with fixed-input reference checks. |
| 5 | Fri Nov 27 | 75 min | Run the baseline from a fresh process | The documented command produces an identifiable config, loss, grids, and timings. A repeat checks reproducibility. |
| 6 | Sat Nov 28 | 45 min | Review what changed and what the run supports | The derivation and run notes are reviewed, with a clear handoff to Week 18. |
| 7 | Sun Nov 29 | 0–45 min | Rest or buffer | Use this only for one named unfinished item. |

### Day 1 — Read the Algorithms Through the Notebook

**15 min.** Open Algorithms 1 and 2 in the paper. With the notebook
closed, pick one line in each algorithm and write where you think it
lives in your implementation.

**20 min.** Open the notebook and check that mapping. Follow
`prepare_batch` and `train_step` for training, then `single_step_reverse`
and `sample_loop` for generation. Locate what comes from the schedule,
what the network predicts, and when the random generator is used.

**10 min.** Summarize the two procedures in your own words. Identify
where the clean image is known and where the generation loop starts.
Mark Equation 7 as the reference for tomorrow's derivation.

### Day 2 — Derive One Gaussian Posterior

**25 min.** Fix $x_0$, $x_t$, and $t>1$. In one dimension, use Bayes
to express $q(x_{t-1}\mid x_t,x_0)$ up to a constant. Write its two
Gaussian factors using the Week 15 schedule. Try collecting the terms in
$x_{t-1}$ before checking the paper.

**20 min.** Complete the square or read the precision and linear
coefficient directly. Compare your mean and variance with Equations 6–7.
Explain why the same calculation extends coordinatewise for isotropic
noise. Use Week 4's example if you need to recover the algebra.

**15 min.** Check what changes at $t=1$, when conditioning on $x_0$
already fixes the previous state. Relate the result to why the code
uses a standard deviation in the sample update. Save the first attempt
and any correction that helped.

### Day 3 — From the Posterior to Predicted Noise

**20 min.** Revisit the Day 6 handoff question. When $x_0$ is unavailable,
explain which possible clean images contribute to the mean of
$X_{t-1}\mid X_t=x_t$. Use the tower property from Week 7 and the
clean-conditioned mean you derived.

**20 min.** Use the Week 16 clean-image estimate to express that mean
through predicted noise. Check the resulting expression against
Equation 11 and your sampler. Distinguish the mean connection from
the fixed variance the sampler uses.

**15 min.** Trace one intermediate term of the paper's objective.
With fixed variance, Equation 8 is a weighted mean error. Follow
Equation 12 to see how it becomes a weighted noise error, then identify
the change made in the simplified noise MSE. A full derivation of the
variational bound can carry into Week 18.

### Day 4 — Move the Working Pieces into Nano-Diffusion

**15 min.** Start with `single_step_reverse`, where the reverse mean from
Day 3 appears in code. Read its signature and body. Which schedule tensors
does it read from earlier cells, and how would you give it those values in
a fresh Python process? A proposed signature and one sentence about the
inputs are enough for the first sitting. Use the same approach for
`prepare_batch` and `sample_loop` when you return. [Week 16 solved notebook](../notebooks/w16_train_tiny_ddpm_mnist_solved.ipynb)

**40 min.** Move the dataset loading and normalization, schedule and
coefficient lookup, TinyDenoiser, training step, and reverse sampling
into a small importable project. Connect them through one training
entry point. The first extraction uses the same architecture, objective,
and schedule as Week 16 so we can compare behavior.

**15 min.** Check direct noising on fixed inputs and repeat the
[Week 16 scalar reverse step](w16_hf_ddpm_training.md#tracing-one-reverse-step).
The reference mean is $0.894427$ and the sample with $z=-0.6$ is
$0.694427$ (both rounded). Check the no-noise branch at $t=1$ separately.
Run a single optimizer update and a small generation check. Record
any behavior difference before moving on to a longer run.

### Day 5 — Run and Repeat a Short Baseline

**15 min.** Prepare one CPU config and record the exact command
that runs it. Start with the Week 16 settings: 5,000 MNIST images,
batch size 64, Adam at $10^{-3}$, seed 16, the $T=1000$ linear
schedule, two epochs, and 16 generated images after each epoch.
Keep initialization, shuffling, corruption, and generation seeded.

**40 min.** Run the same command twice, each time from a fresh process.
Compare the two runs’ losses and grids to check repeatability. To check
that the extraction preserved the notebook’s behavior, compare each run
with the first two epochs of the saved Week 16 CPU run. On the same setup
with 5,000 images and seed 16, the mean batch noise MSE printed as
**0.4860 at epoch 1** and **0.2044 at epoch 2**. Compare the corresponding
16-image grids as well, resetting the sampling generator to seed 16 each
epoch as the notebook does. [Week 16 notebook, “Train and compare grids”](../notebooks/w16_train_tiny_ddpm_mnist_solved.ipynb)

If time runs short, carry the repeat into the buffer. If you use a smaller
training subset, record its size and compare the two runs at that size.
The Week 16 reference values apply to the original 5,000-image setup.

**20 min.** Save the resolved config, losses, per-epoch sample grids,
and separate training and sampling times under
`mini_projects/nano_diffusion/experiments/ddpm_baseline_mnist/` or link
to those outputs from a small run record there. Write down the actual
device and update count. Keep large disposable outputs in the existing
ignored scratch area.

### Day 6 — Close the Loop

**10 min.** With notes initially closed, explain how the posterior you
derived connects to one step of the sampler. Then check the formulas in
the paper or your derivation note.

**20 min.** Review the fixed-input checks, one loss result, and one
generated grid. Explain what the repeat tells you about reproducibility
and what the grid tells you about image quality. If Friday’s comparisons
diverge, an agent can optionally trace the first differing input or output.
On Saturday, verify that finding against the two runs or the notebook.

**15 min.** Review the consolidated note and run record. Write one
sentence on what to carry into Week 18. Preserve any unresolved theory
or implementation issue with the point at which you stopped.

## Completion Checks

- [x] Map DDPM Algorithms 1 and 2 to the working implementation.
- [x] Derive the clean-conditioned mean and variance and identify the sampler’s noise scale and final no-noise step.
- [x] Connect the clean-conditioned mean to the sampler’s predicted-noise mean when the clean image is unknown.
- [x] Explain the weighted versus simplified objective for one intermediate step.
- [ ] Run the extracted baseline from a documented command and check a repeat.
- [ ] Save and review the config, losses, samples, and timings.

**Week 18:** Add EMA and finish the logging, snapshots, and longer
reference run once the plain baseline is reproducible. The wider-context
denoiser is a follow-up comparison. Hold the data, schedule, training
budget, and sampling seeds fixed when testing it.
