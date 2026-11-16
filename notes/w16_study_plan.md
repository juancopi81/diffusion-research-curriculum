# Week 16 — Train and Sample a Tiny DDPM: Study Plan

**Status:** Prepared on 2026-11-13; Week 16 started on 2026-11-16.
Day 1 is complete, including Juan's read-through and approval of the
[consolidated note](w16_hf_ddpm_training.md). Days 2–6 have not started. The dates below are
a suggested calendar for **November 16–22, 2026**. Move unfinished
sessions forward in order if needed.

**Pacing:** Six sessions totaling **six hours of active study**, plus Sunday
for rest or up to 45 minutes of catch-up. This is one hour more than Week
15's planned budget because this week adds both training and generation.
Reading, discussion, and reviewing cleaned notes are included. Computer run
time is separate and should be measured; the proposed training settings
have not yet been timed. Stop at the budget and carry a specific unfinished
item forward.

## Where We Are

- **Weeks 1–8:** probability foundations, conditioning, and the first 2D
  score-learning experiment are complete.
- **Weeks 9–14:** linear algebra, Gaussian scores, VAEs, flows, optimization,
  and the generative-toolkit checkpoint are complete.
- **Week 15:** completed on 2026-11-05. You derived the Gaussian forward
  process, implemented sequential and direct noising on MNIST, compared
  linear and cosine schedules, and checked conditional moments numerically.
  The [final discussion](w15_forward_process_discrete.md#day-6--consolidating-the-forward-process-and-closing-week-15)
  records what you recalled, what used saved evidence, and what was explained.
- **Week 16:** the final week of Phase 2. We now add a model that learns at
  multiple noise levels and a loop that generates images from noise.

The Week 15 discussion correctly distinguished a posterior clean estimate
from a score with the score formula supplied. Deriving their relationship
independently was not assessed. That connection returns naturally on Day 2;
it does not require a separate remedial session.

## What This Week Produces

One small MNIST experiment that connects **training examples → noise
prediction → reverse sampling → generated images**. We will use one
schedule and one small model, inspect the loss and generated samples, and
explain the results. The [Week 16 curriculum](../CURRICULUM.md#week-16--first-full-toy-diffusion-training-small)
sets the scope.

Build the following as the sessions progress. The training note now
contains Day 1's discussion; the derivation note and notebook pair remain
planned outputs:

- `notes/w16_hf_ddpm_training.md`: your explanation of the objective,
  timestep conditioning, sampler, and experimental observations.
- `notes/w16_prediction_parameterizations.md`: your derivation attempts,
  reviewed relationships among clean prediction, noise prediction, and
  score prediction, with assistance identified.
- `notebooks/w16_train_tiny_ddpm_mnist.ipynb` and its `_solved.ipynb`
  counterpart: an exercise baseline and the working experiment, including
  configuration, training loss, sample grids, runtime, and conclusions.

## Working Rhythm

Follow the Week 15 sequence: read the selected material, explain your
understanding, discuss one question at a time, restate corrections, then
briefly review the consolidated note. For derivations, keep your first
attempt. For experiments, predict what you expect before running them.

Use the existing weekly notes and notebook observations for brief review
records. Record reference use and hints when they occur. Codex handles
notebook scaffolding, routine setup, and note formatting within these
sessions; your work concentrates on the equations, code exercises, and
interpretation.

> Let's work on Day __ of the Week 16 plan. Here is my understanding or
> attempt: __. Start from it and discuss one question at a time. Let me try
> before giving a solution, unless I ask for a direct explanation. Keep us
> within today's budget, preserve useful attempts and corrections in the
> existing weekly files, and finish by identifying the next stopping point.

## Reading Map

Selected sections checked on 2026-11-13. These two external readings and
your existing notes are enough for the week.

| Source | Use and boundary |
| --- | --- |
| [HF Unit 1: Diffusion Models from Scratch](https://huggingface.co/learn/diffusion-course/en/unit1/3#comparison-to-ddpm) | Day 1: within **Comparison To DDPM**, read **Training Objective** and **Timestep Conditioning**. Day 3: read the final **Sampling** subsection for the questions a sampler must answer. |
| [The Annotated Diffusion Model](https://huggingface.co/blog/annotated-diffusion) | Day 1: scan **Defining an objective function (by reparametrizing the mean)** through the noise-prediction objective. Day 3: read **Sampling**, focusing on `p_sample` and `p_sample_loop`. Days 4–5: consult `p_losses` and **Train the model** as code references. |
| [Week 15 forward-process note](w15_forward_process_discrete.md) and [completed notebook](../notebooks/w15_forward_diffusion_mnist_solved.ipynb) | Reuse the notation, normalization, schedule, and direct-noising construction. A brief lookup is enough. |
| [Week 7: MSE-optimal denoising and the score connection](w07_conditional_expectation_in_diffusion.md) | Day 2: consult after your own attempt, especially **Denoising as Conditional Expectation** and **Score Connection**. Its generic signal coefficient uses a different alpha convention. |

**Adaptation notes:** HF's earlier toy uses a uniform-noise blend and clean
prediction; an intermediate example also holds the timestep at zero. Our
experiment uses Gaussian noise and each example's actual timestep. Keep
Week 15's verified forward formulas. In Annotated Diffusion, select the
L2/MSE loss rather than its demonstrated Huber option. Its sampler code
uses zero-based noisy-step indices; map those explicitly to our clean
$t=0$ convention. These choices follow our curriculum's experiment.

## Day-by-Day Schedule

| Day | Date | Budget | Focus | Concrete stopping point |
| --- | --- | --- | --- | --- |
| 1 | Mon Nov 16 | 45 min | What the denoiser learns | Explain one training example, the noise target, the loss, and why the model receives $t$. |
| 2 | Tue Nov 17 | 60 min | Connect the three prediction forms | Review the clean/noise/score relationships, their conditioning, and the loss-weighting distinction. |
| 3 | Wed Nov 18 | 60 min | Understand a reverse step | Trace one sourced update and write the full sampling loop in pseudocode, including the final-step rule. |
| 4 | Thu Nov 19 | 75 min | Build and check training | Complete the training-step exercises; run a short learning check with correct shapes, indices, and targets. |
| 5 | Fri Nov 20 | 75 min | Train and generate | Complete the sampler, run the small experiment, and save loss plus genuinely generated sample grids. |
| 6 | Sat Nov 21 | 45 min | Explain the complete system | Review the math, implementation checks, and observed images; consolidate the notes and Week 17 handoff. |
| 7 | Sun Nov 22 | 0–45 min | Rest or catch up | Finish one named unresolved item. Leave the day free if the week is complete. |

### Day 1 — What Does the Model Learn?

**Use:** HF's two assigned subsections, then the objective section of
Annotated Diffusion. Budget about 25 minutes to read, 15 to discuss, and
five to check the note. Recognize the connection to the VAE/ELBO work;
the full DDPM variational-bound derivation can wait for Weeks 17–18.

Start from the forward construction you already implemented:

$$
x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\epsilon,
\qquad \epsilon\sim\mathcal N(0,I).
$$

Explain how we create a training example by drawing a clean image, a
timestep, and Gaussian noise. Identify what the model receives, what it
predicts, and what we know because we constructed the example. Translate
the simplified objective into words:

$$
\mathcal L_{\mathrm{simple}}
=\mathbb E_{x_0,t,\epsilon}
\left[\left\|\epsilon-\epsilon_\theta(x_t,t)\right\|^2\right],
\qquad t\sim\mathrm{Uniform}\{1,\ldots,T\}.
$$

**Stop when:** you can explain why the target is the original unit-Gaussian
draw, how $t$ tells the model which corruption level it faces, and why a
training pair is available without an analytic MNIST score. Keep the
distinction between this simplified objective and the full variational
bound visible.

**Day 1 completed on 2026-11-16, including learner read-through.** The
[Day 1 consolidation](w16_hf_ddpm_training.md) preserves Juan's correct
reading-based training explanation, questions about the VAE/ELBO and loss
weights, and the guided corrections on sampling noise, fresh draws, and
timestep conditioning. Follow-up answers and the final restatement were
correct after explanation. No independent reverse-mean derivation or
loss-weighting derivation is claimed. Juan read and approved the
consolidated note; the next session is Day 2.

### Day 2 — One Noisy Observation, Three Prediction Forms

**Use:** yesterday's equation and your Week 7 note as a reference after
attempting the algebra. Budget 35 minutes for your attempt, 20 for
discussion, and five for checking the consolidated derivation.

At a fixed noisy timestep, attempt these connected steps:

1. Rearrange the forward equation to express a clean estimate in terms of
   a noise estimate, and reverse that conversion.
2. Differentiate the Gaussian conditional log density to obtain the
   conditional corruption-score target. Relate it to the noise draw.
3. Use conditional expectation to explain what the population MSE-optimal
   noise predictor returns and how it relates to the marginal noisy-data
   score. Distinguish an individual target from its conditional average.
4. Substitute the clean/noise conversion into squared error. Identify the
   timestep-dependent factor that relates the two losses: convertible
   predictions do not make unweighted training across timesteps identical.

Keep $t$ fixed with $0<\bar\alpha_t<1$ for these conversions. Use one small
numerical example to check signs and scaling. These are our derivations,
not an attributed official solution.

**Stop when:** the relationships are correct and you can distinguish the
clean posterior mean from the score. Record whether the explanation used
notes or hints. Consolidate into `notes/w16_prediction_parameterizations.md`.

### Day 3 — How Does a Reverse Step Work?

**Use:** the final HF sampling subsection for intuition, then Annotated
Diffusion's **Sampling** code. Budget 20 minutes to read, 25 to trace the
update and write pseudocode, and 15 for discussion and consolidation.

Treat the sourced reverse-mean formula and fixed posterior-variance choice
as references to understand and implement. A full Bayes derivation of the
Gaussian posterior is not required in this session.

Trace what takes $x_t$ to $x_{t-1}$: predict noise, construct the reverse
mean, and add the prescribed fresh Gaussian noise except on the final
step. Then write the outer loop starting from $x_T\sim\mathcal N(0,I)$.
Explain why the same trained weights are used throughout sampling.

Distinguish the tractable forward posterior $q(x_{t-1}\mid x_t,x_0)$ from
the reverse conditional without the clean image, $q(x_{t-1}\mid x_t)$,
which our learned Gaussian transition approximates. Generation does not
have the original $x_0$ available.

**Stop when:** your pseudocode runs from mathematical $t=T$ down to $1$,
uses the matching schedule values, adds no fresh noise in the final
transition to $x_0$, and never performs an optimizer update. Check one
step numerically with supplied values before polishing the explanation.

### Day 4 — Build the Training Step

**Starting point:** Codex prepares the notebook pair following the repo's
weekly-notebook conventions, adapting the Week 15 data loader and forward
helpers. The data/plotting setup and tiny convolutional model are provided;
trace how the timestep enters the model. Keep architecture study bounded.

Budget 15 minutes to inspect setup, 40 for the core exercises, and 20 for
checks and discussion. Implement batched timestep/noise sampling, direct
noising, and the noise-MSE optimizer step. Verify that the predicted noise
has the image's shape and that schedule coefficients broadcast per image.

Run a brief fixed-batch learning check. Check finite outputs, loss, and
gradients, confirm that optimization changes model parameters, and inspect
whether the fixed-batch loss improves. This diagnoses the training path;
it does not establish generation quality.

**Stop when:** the training step works and the notebook can construct a
noisy batch, predict its noise, compute MSE, and update parameters. Retain
the completed exercises and actual observations in the working notebook.

### Day 5 — Train, Then Generate from Noise

Budget 25 minutes to implement the reverse step and loop from Day 3,
20 for numerical checks and launching the run, and 30 to inspect the
results and discuss them. Keep run time separate from active study.

Before the main run, check the reverse step against the sourced formula
on fixed inputs/noise, check the final transition, and confirm that
sampling leaves the weights unchanged. An untrained-model run can check
shapes and finite values; it is not evidence of learned image generation.

Use this bounded starting configuration, subject to the setup timing check:

- MNIST at $28\times28$, normalized as in Week 15, with a fixed subset of
  5,000 training images and a recorded seed (start with 16).
- One tiny timestep-conditioned convolutional denoiser, noise-MSE training,
  Adam, and batch size 64. Record the chosen learning rate and model size.
- The existing linear schedule: $T=1000$, betas from $10^{-4}$ to $0.02$.
  Reuse the clean $t=0$ boundary; training samples $t=1,\ldots,T$.
- Start with two epochs and a 16-image generated grid after each epoch,
  using fixed sampling seeds for comparison. Record actual epochs, updates,
  device, training time, and sampling time.

If runtime is excessive, reduce the image-grid size or training subset and
record the change. Changing the number of diffusion steps also changes the
endpoint distribution unless the schedule is adjusted; preserve the
verified schedule for this first experiment. Carry unfinished work into
the buffer rather than silently dropping sampling.

**Stop when:** one complete training-and-sampling run has a loss curve,
generated grids, and a short interpretation. The grids must begin from
Gaussian noise; reconstructions of supplied clean digits are a different
diagnostic. Inspect recognizability, diversity, and failure cases without
assuming that lower training loss guarantees better samples.

### Day 6 — Explain the Whole Path and Close the Week

Use five minutes for an explanation with notes initially closed, 20 to
discuss saved evidence, and 20 to review and consolidate the weekly files.
Explain how we manufacture targets, why $t$ matters, how predictions
convert, and how fixed trained weights produce new images through the
reverse loop. Then use your notes and outputs to check uncertain details.

Choose one training result and one generated grid. State what they support
and what remains uncertain. Keep crude images as honest evidence if the
implementation checks pass; unresolved correctness bugs keep the affected
work open. Record one useful next experiment in the existing note.

**Stop when:** the completion checks below have been reviewed and your
explanation, corrections, and remaining questions are accurately recorded.
Identify the forward helpers, model, training step, and sampler that can
become shared code in Weeks 17–18. No extraction or new framework is
required this week.

## Completion Checks

- [x] Explain the noise target, timestep input, and training objective.
- [ ] Review the clean/noise/score conversions and loss-weighting distinction.
- [ ] Explain the reverse update and the final-step rule.
- [ ] Complete and check the training and sampling implementations.
- [ ] Save the run configuration, loss, per-epoch generated grids, and runtime.
- [ ] Review the evidence and consolidated notes, recording any assistance
  and unresolved items before deciding whether Week 16 is complete.

Update progress from work actually completed. Preparing this plan does
not mark any reading, derivation, implementation, or experiment as done.

## What Comes After

**Weeks 17–18** begin Phase 3: read the DDPM algorithm/objective more
closely and turn this prototype into a reproducible
`mini_projects/nano_diffusion/` baseline, with shared code, configuration,
EMA, and experiment records. **Weeks 19–20** compare DDPM and DDIM sampling
using the same trained model where possible.

The cosine-schedule exploration and generative-toolkit blog remain optional
or separate work. They add no sessions or prerequisites to this plan.
