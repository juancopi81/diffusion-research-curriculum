# Week 15 — The Forward Diffusion Process: Study Plan

**Status:** Started on 2026-10-30. Days 1–5 are complete, including the learner's
read-through and approval of the [cleaned note](w15_forward_process_discrete.md).
The Day 1 section was approved on 2026-10-30; the Day 2 and Day 3 sections
were approved on 2026-11-02. Day 4's implementation, discussion, and learner
approval of the note and notebook observations completed on 2026-11-03.
Day 5's code, discussion, and learner approval of the cleaned note and
notebook observations completed on 2026-11-04. Day 6 remains planned.

**Pacing:** Six sessions totaling about five hours, plus a seventh day for
rest or up to 45 minutes of catch-up. These are flexible study days, not
calendar deadlines. Stop at the budget, record the precise unresolved point,
and use the buffer if needed.

The [Week 15 curriculum](../CURRICULUM.md#week-15--bridge-to-diffusion-math-forward-process)
has a narrower focus than Week 14: understand Gaussian forward noising,
derive its distributions, and check them on MNIST. The main thinking is in
the cumulative variance and the numerical verification. Training and reverse
sampling start in Week 16; this week needs no additional lecture series.

## Working Rhythm

Use the sequence that has worked for you:

1. Read the selected material first. Keep rough notes, questions, and your own
   derivation attempts; presentation can wait.
2. Explain the main idea to Codex in three to five sentences and bring one or
   two questions. For code sessions, predict the result before running it.
3. Discuss the gaps. Codex asks one question at a time, starts from your
   explanation, and offers a hint before a worked answer. Aim for three or
   four focused questions within the session's budget.
4. Restate the corrected idea yourself. Codex then consolidates that discussion
   into the weekly note, preserving useful corrections and marking open
   questions. Briefly read the result for meaning and voice.

A reusable prompt:

> I have read the material for Day __ of the Week 15 plan. Here is my
> understanding and what I am unsure about: __. Discuss my questions, then
> ask me one question at a time to check the central ideas. Let me attempt
> the reasoning before giving a solution. After I restate the corrections,
> consolidate what we covered into the weekly note and keep unresolved points
> visible. Keep the discussion within today's budget.

On reading days, allow roughly 25–30 minutes for the source, 10–15 for
discussion, and five for checking the cleaned note. The budgets include the
discussion and review; polishing should not become a second study session.

## Reading Map

The two assigned sources are enough for the core week. Source sections were
checked on 2026-10-29.

| Source | Selected use |
| --- | --- |
| [The Annotated Diffusion Model](https://huggingface.co/blog/annotated-diffusion) | Day 1: introduction and forward-transition equation. Day 2: direct conditional noising formula in the objective discussion. Day 4: schedule and `q_sample` code under [Defining the forward diffusion process](https://huggingface.co/blog/annotated-diffusion#defining-the-forward-diffusion-process). |
| [HF Unit 1: Diffusion Models from Scratch](https://huggingface.co/learn/diffusion-course/en/unit1/3#comparison-to-ddpm) | Day 2: within the DDPM comparison, jump past the network material to the later corruption subsection; stop before the training objective. The earlier uniform-noise blend is an intuition example. |
| [Gaussian identities](gaussian_identities.md#diffusion-forward-noising-kernel) and [Week 7 conditioning discussion](w07_conditional_expectation_in_diffusion.md) | Open only to resolve a specific Gaussian or conditioning question. |

**Reading caution:** The HF course's later corruption subsection currently
has notation slips. For independent standard Gaussian noise, the one-step
noise multiplier is $\sqrt{\beta_t}$; the closed-form covariance is
$(1-\bar\alpha_t)I$; and $\bar\alpha_t$ is the product of the $\alpha_s$ through
the current $t$. Use Annotated Diffusion and the local Gaussian sheet to
check these. In Week 7's generic notation, $\alpha_t$ names the signal
multiplier; in this week's DDPM notation, $\alpha_t=1-\beta_t$.

## Day-by-Day Schedule

| Day | Budget | Your work first | Discussion and concrete stopping point |
| --- | --- | --- | --- |
| 1 | 45 min | Read the forward-process introduction and one-step equation. Write a short explanation of what is fixed and what is random. | Explain one noising step and distinguish the noise's variance from its standard deviation. Codex records the reviewed intuition and notation. |
| 2 | 45 min | Read the direct noising formula and the HF DDPM corruption comparison. Sketch what happens to signal and noise over time. | Distinguish one-step and cumulative quantities, and the conditional distribution from the data marginal. Stop with a clear account of what the closed form lets us sample. |
| 3 | 60 min | Attempt the one-step distribution, expand two steps, then generalize to the closed form. | Review the mean and covariance calculation. Codex cleans your attempted derivation, corrections, and any reference use into the note. |
| 4 | 60 min | Read the selected forward-process code, then implement the noising equations in the weekly notebook. Predict the image progression. | Check indexing, shapes, and coefficients. Stop with one working schedule, an MNIST noising grid, and signal/noise curves. |
| 5 | 60 min | Compare linear and cosine schedules; run small Monte Carlo checks of the derived moments. | Explain the plots and any numerical discrepancies. Stop with a paired schedule comparison and evidence that both sequential and direct noising match the predicted moments. |
| 6 | 30 min | Give a short explanation of the whole process with notes initially closed; interpret your saved results. | Resolve the central gaps, briefly revisit the Week 14 conditioning distinction, and read the consolidated note. Record readiness for Week 16 based on the work actually done. |
| 7 | 0–45 min | Rest, or finish one specific unresolved derivation or notebook check. | Close that item and update its status. If the week is complete, leave the day free. |

### Day 1 — Understand One Step

**Reading boundary:** Read the whole introductory section, then the beginning
of the mathematical section through the forward trajectory from $x_0$ to
$x_T$. Stop before the paragraph introducing the reverse conditional.

Start with the source, then explain the role of $x_0$, $x_{t-1}$, $x_t$,
and $\beta_t$. Discuss why the step both rescales the previous image and
adds noise, and which part of the process is chosen in advance.

Useful check: given $x_{t-1}$, what is still random? What would change if
you multiplied unit Gaussian noise by its intended variance instead of its
intended standard deviation?

**Discussion completed on 2026-10-30.** The
[weekly note](w15_forward_process_discrete.md) records the one-step kernel,
the scalar sampling check, the conditional-versus-mixture distinction, and
the approximately Gaussian endpoint. The discussion included hints and
corrections, recorded in the note. The learner read and approved the cleaned
note on 2026-10-30, completing Day 1.

### Day 2 — Understand the Shortcut

**Reading boundaries, checked on 2026-10-30:**

- In Annotated Diffusion, jump to the objective-function section. Skip its
  first two ELBO paragraphs and read the short passage introducing direct
  noising from $x_0$: the conditional Gaussian formula, the definitions of
  $\alpha_t$ and $\bar\alpha_t$, and the paragraph explaining precomputation.
  Stop before the discussion turns to selecting training-loss terms.
- In HF Unit 1, go to the DDPM comparison and find the later corruption
  subsection after the U-Net material. Read through its coefficient plots,
  image visualization, and final normalization explanation. Stop at the
  training-objective heading. Skim code to understand the plots; execution
  belongs to the later notebook sessions. Apply the notation corrections
  in the [reading map](#reading-map).

Read for meaning before trying to reproduce the algebra. Distinguish
$\beta_t$, $\alpha_t$, and $\bar\alpha_t$; label the signal multiplier, noise
multiplier, and conditional variance in the direct formula.

Useful checks: why can we jump straight from a clean image to a selected
noise level? Does Gaussian noise make the distribution over all noisy
images Gaussian at every step? What must be small before the final
distribution is approximately standard Gaussian?

Keep the answer about the conditional distribution $q(x_t\mid x_0)$
separate from the marginal $q(x_t)$ over different clean images.

**Reading and discussion completed on 2026-10-30.** The
[Day 2 note](w15_forward_process_discrete.md#day-2--direct-sampling-from-the-clean-image)
records the direct formula, cumulative schedule quantities, the learner's
handwritten coefficient-crossing calculation, distributional agreement of
the two methods, and the normalization explanation. The three discussion
checks were answered correctly; Codex's clarifications are recorded. The
learner read and approved the section on 2026-11-02, completing Day 2.

### Day 3 — Derive Before Cleaning

Spend about 30 minutes on your own attempt, 20 discussing it, and 10
reviewing the consolidated derivation. Work through two steps explicitly,
using independent noise at each step, then use a recurrence or induction.
Check $t=1$ against the original transition and $t=0$ against the clean
input. Keep the Gaussian reference sheet available when needed.

Useful checks: where is independence used? Why do the old noise terms get
rescaled? Does a fresh direct sample have to equal a particular sequential
sample, or do the two constructions agree in distribution at the chosen time?

**Derivation and guided review completed on 2026-11-02.** The
[Day 3 section](w15_forward_process_discrete.md#day-3--deriving-the-forward-distributions)
contains the one-step law, two-step expansion, conditional moments,
Gaussianity argument, induction, and both boundary checks. It preserves
all five handwritten pages. The starting attempt exceeded its 15–20-minute
budget; exact time was not recorded. Notation correction, algebra prompts,
the induction scaffold, and Codex's covariance recurrence are recorded.
The learner read and approved the cleaned section on 2026-11-02,
completing Day 3.

### Day 4 — Make the Equations Visible

**Material prepared on 2026-11-02:** Open the
[working copy](../notebooks/w15_forward_diffusion_mnist_solved.ipynb) and
keep the [unsolved baseline](../notebooks/w15_forward_diffusion_mnist.ipynb)
as a reference. The files start as exact copies, each with three exercises:
cumulative schedule coefficients, one-step corruption, and direct sampling.
Data loading, shape/boundary checks, coefficient plots, and both image grids
are provided. Start at Setup and continue to the Day 4 stopping point under
Wrap-up, then bring the three observation answers for discussion.

The tutorial uses NumPy on CPU, seed 15, and the checksum-verified cached
MNIST test files from Week 11. Generated figures and any missing raw data
stay in the ignored scratch directory. The prepared code was executed with
temporary reference implementations to validate the complete flow and
plots; both delivered notebooks retain their exercises and empty outputs.
Preparation does not mark the learner's implementation or review complete.

Use the repository's unsolved/solved notebook convention when scaffolding
the experiment. Codex can prepare data loading and plotting scaffolding;
leave the core noising calculation and interpretation for your attempt.
Reuse the earlier MNIST setup where practical.

Implement a single step and direct noising, seed the random generators,
and make the mapping from mathematical timesteps to array indices explicit.
Start with a linear schedule. Plot the same few digits at selected
timesteps, alongside signal decay and conditional variance growth.

Check the clean-input boundary and tensor shapes. Record normalization and
schedule settings. Keep raw samples for calculations; any display clipping
belongs only to the image presentation.

**Implementation and discussion reviewed on 2026-11-03.** Juan completed
the three exercises correctly. A fresh execution of all 16 code cells
passed the supplied assertions. The
[Day 4 note](w15_forward_process_discrete.md#day-4--implementing-and-interpreting-forward-noising)
preserves the three observations, figures, and corrections: amplitudes
versus image percentages, the clean input in direct sampling, and the
proposed fixed-input Monte Carlo comparison. The empirical moment check
and second schedule remain for Day 5. The learner read and approved the
note and the notebook's consolidated observation cells on 2026-11-03,
completing Day 4.

### Day 5 — Check What the Pictures Suggest

**Material prepared on 2026-11-03:** Continue in the
[working notebook](../notebooks/w15_forward_diffusion_mnist_solved.ipynb)
at **Day 5 — Compare Schedules and Check Conditional Moments**, below the
completed Day 4 Wrap-up. After a kernel restart, first run the completed
Day 4 code cells to restore the functions and data. The new sections also
appear in the unsolved baseline; Day 4's completed code and outputs are
preserved in the working copy.

Fill two new exercises: **TODO 4** returns the conditional reference mean
and variance, and **TODO 5** estimates them across repetitions. The cosine
schedule, matched-noise image comparison, repeated sampling, tolerance
checks, plots, and CSV export are provided. The default uses 4,000 draws
of two fixed clean coordinates at times 1, 100, 500, and 1000, under each
schedule and each sampling method. Finish with the three Day 5 observations
and stop at Day 5 Wrap-up for discussion.

At preparation, all 16 schedule/method/time Monte Carlo cases passed the
mean, variance, and cross-covariance diagnostics using temporary reference
answers. The delivered cells retained their learner
exercises and empty outputs; that preparation was separate from the
learner's subsequent execution and discussion.

Allow roughly 20 minutes for the second schedule and plots, 25 for moment
checks, and 15 for interpretation with Codex.

- Compare linear and cosine schedules at the same number of steps. Use the
  same clean images and matched noise draws for the visual comparison.
- For moment checks, fix a clean scalar or a few pixel coordinates and
  generate many independent repetitions. Compare empirical means and
  variances with the derivation at early, middle, and late timesteps.
- Run a small sequential simulation as well as direct sampling. Use a tiny
  vector for this check so that repeatedly noising full images is unnecessary.
- Include seeded, lightweight assertions with tolerances appropriate to
  Monte Carlo error. Averaging different pixels or different digits does
  not estimate the conditional variance for a fixed clean input.

Useful checks: can you explain the schedule differences from the curves?
Why needn't two random images match pixel by pixel? Shared-noise direct
snapshots help compare schedules, but do not constitute a sampled Markov
trajectory. These forward-only results support claims about corruption;
generation quality requires later training and sampling evidence.

**Implementation and discussion reviewed on 2026-11-04.** Juan completed
both exercises correctly; a fresh execution of all 27 notebook code cells
passed the supplied checks, including all 16 Monte Carlo cases. The
[Day 5 note](w15_forward_process_discrete.md#day-5--comparing-schedules-and-checking-conditional-moments)
and notebook observations preserve his schedule comparison and chosen
coordinate's estimates. After a standard-error prompt, he correctly
interpreted both mean discrepancies as expected sampling variation; Codex's
variance explanation and wording corrections are identified separately.
Juan read and approved the cleaned note and notebook observations on
2026-11-04, completing Day 5.

### Day 6 — Consolidate and Hand Off to Week 16

**Bring:** The [weekly note](w15_forward_process_discrete.md) and
[completed notebook](../notebooks/w15_forward_diffusion_mnist_solved.ipynb).
Briefly skim your equations and Days 4–5 observations. Choose one saved
plot and one Monte Carlo example to explain; your cosine, coordinate-1,
$t=100$ example is a ready option.

Use about five minutes for your explanation, 15 for questions, and 10 to
review the note. Explain the path from a clean image and a schedule to a
noisy training input, then interpret one plot and one numerical check.
Start the explanation with notes closed, then use them to check gaps.
Connect the one-step and direct formulas, cumulative coefficients,
conditional moments, and the agreement between the two constructions.

Within the discussion, spend at most five minutes on the
[Week 14 carryover](w14_study_plan.md#day-7-completion-decision): distinguish
the mean noisy point given a clean input, the estimated clean point given a
noisy observation, and the score at that noisy observation. Identify what
each quantity conditions on and what it returns. Use the Week 7 reference
if needed, especially [The Direction Flip](w07_conditional_expectation_in_diffusion.md#1-the-direction-flip)
and [Score Connection](w07_conditional_expectation_in_diffusion.md#5-score-connection);
its generic signal coefficient uses a different alpha convention, as noted
in the reading map. Record any guidance accurately.

Codex now organizes the accumulated note, including source links,
derivations, selected notebook evidence, your interpretation, and any open
questions. Read it for accuracy before recording completion.
Stop once the whole-process explanation, selected evidence, and conditioning
distinction have been reviewed and the cleaned final note has been read.
Week 16's training and reverse sampling remain the next week's work.

## Expected Outputs and Completion

Create these as the study progresses:

- `notes/w15_forward_process_discrete.md`: one compact note built from the
  discussions, containing notation, both derivations, the schedule comparison,
  and the connection to earlier fixed-noise experiments and Week 16.
- `notebooks/w15_forward_diffusion_mnist.ipynb` and its `_solved.ipynb`
  counterpart: the exercise scaffold and completed, reproducible experiment.

The notebook's noising functions and settings are candidates for reuse in
Week 16's Nano-Diffusion work. Keep them small and readable.

- [x] Explain the one-step and direct constructions, including their conditioning.
- [x] Derive their means and covariances, with reference use or hints recorded.
- [x] Compare two schedules using images and coefficient/variance curves.
- [x] Verify the predicted moments numerically and check both constructions.
- [ ] Read the cleaned note and explain the central results in your own words.

Update progress after these checks are actually completed. This plan itself
does not mark the readings, derivations, or experiment as done.
