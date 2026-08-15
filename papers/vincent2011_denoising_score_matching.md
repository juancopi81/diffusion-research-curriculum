# Vincent (2011) - A Connection Between Score Matching and Denoising Autoencoders

> Status: Not started - stub prepared 2026-08-15
> Read on: <YYYY-MM-DD>
> Venue: *Neural Computation* 23(7):1661-1674 (14 pages)
> Link: https://www.iro.umontreal.ca/~vincentp/Pub/DenoisingScoreMatching_NeuralComp2011.pdf
> Canonical record: [MIT Press](https://direct.mit.edu/neco/article-abstract/23/7/1661/7677/A-Connection-Between-Score-Matching-and-Denoising)

Source status: **stub only.** Sections 1-5 below are prompts to fill while reading.
The framing in "Before reading" comes from the abstract and from prior repo work, not
from the body of the paper — replace it with what the paper actually says.

---

## 0. Source Map

- [`mini_projects/checkpoint_02_toy_score_matching/`](../mini_projects/checkpoint_02_toy_score_matching/) —
  trains one model on an $x_0$ target and one on a conditional-score target, then compares
  both to the analytic score. **Both objects in this paper were implemented here before
  the paper was read.**
- [`notes/w03_score_of_gaussian.md`](../notes/w03_score_of_gaussian.md) — the Gaussian
  score as a pull back toward the mean. This is the regression target the paper uses.
- [`notes/w07_conditional_expectation_in_diffusion.md`](../notes/w07_conditional_expectation_in_diffusion.md) —
  MSE-optimal denoising as conditional expectation.
- Blog post: *Two Ways to Learn the Same Score Field* (2026-07-30) — currently has **no
  references section**. This paper is the missing citation.

---

## Before reading: the minimum background

Two things appear in the introduction that are **motivation, not prerequisites**. The
result does not depend on knowing either in depth.

**Denoising autoencoders.** Take a clean $x$, corrupt it to $\tilde{x}$, train a network to
reconstruct $x$ from $\tilde{x}$. That is the whole idea. In 2011 this was a
representation-learning trick. The representation-learning literature is not needed here.

**Energy-based models / RBMs.** Exactly one fact is needed, and it is the fact that makes
the paper make sense. These models define $p(x) = \tilde{p}(x)/Z$ with an intractable
normalizing constant $Z$, so maximum likelihood is unavailable. The score sidesteps it:

$$
\nabla_x \log p(x) = \nabla_x \log \tilde{p}(x) - \nabla_x \log Z,
\qquad \nabla_x \log Z = 0 .
$$

$Z$ does not depend on $x$, so it vanishes. **That is why score matching was invented** —
as an escape hatch from the partition function, years before anyone used it to generate
images. With that one line, the RBM material is skippable.

### Reading route

1. Abstract and section headings (~10 min).
2. Skip the RBM / DAE background past the fact above.
3. Find where the **denoising score matching** objective is defined: corrupt with a
   Gaussian, regress the network onto the conditional score of the corruption. This is the
   payload, and it is algebra that can be verified line by line.
4. The **equivalence result** — that this objective matches the one you would want but
   cannot compute (which needs the unknown data score), up to a constant. Sit here.
5. The denoising-autoencoder connection section last. It supplies the title and is the
   least important part for diffusion purposes.

---

## 1. Pass 1 - What and Why

**Problem the paper solves:**

**Main claim (one sentence):**

**Evidence offered:**

---

## 2. Pass 2 - The Load-Bearing Result

**The denoising score matching objective**, in my own notation:

$$
% state it here
$$

**The equivalence, and what it is stated against.** Note carefully *which* density's score
is being matched. Per the abstract it is a **nonparametric Parzen density estimator** of
the data — that is, the data convolved with the corruption kernel at the chosen $\sigma$ —
not the raw data density. Record the exact statement.

**What it is silent about:**

**To verify this I would need:**

---

## 3. Pass 3 - Verification

---

## 4. What Changed for Me

### The question carried in from checkpoint 02

The 2026-07-30 experiment found the indirect $x_0$ objective produced the **lower validation
score MSE** after 20 optimizer updates, and the post called this "not completely obvious."

Read asking: **does the equivalence say anything about that?** Specifically, does it hold
*in expectation at the optimum*, or does it also constrain behaviour *during finite-step
optimization*? Two objectives can share a minimizer while differing sharply in gradient
variance and conditioning on the way there.

- If the theorem is silent on finite-step behaviour, the empirical result is not in tension
  with it — it is a statement about optimization efficiency, which is a separate question
  and a candidate follow-up experiment.
- Answer found: <fill in>

### The Parzen-smoothing consequence

If the objective matches the score of the data smoothed at scale $\sigma$, then a single
$\sigma$ is a bind: small $\sigma$ gives a faithful target but no signal away from the data
manifold; large $\sigma$ gives broad signal for the wrong distribution. Check whether the
paper says this explicitly, and record how it handles the choice of $\sigma$.

This is the tension Song & Ermon (2019) resolve by annealing across noise scales — the step
from a good objective to a working generative model. Confirm before asserting.

- What the paper actually says: <fill in>

---

## 5. Follow-ups

- [ ] Add a References section to the 2026-07-30 blog post, citing this paper
- [ ] Add a "Later I learned" note to that post recording what the equivalence does and
      does not claim
- [ ] Decide whether the finite-step efficiency question is worth a controlled experiment
      on top of `checkpoint_02` (longer training budget, gradient-variance measurement)
- [ ] Read Hyvärinen (2005) for contrast: the Hessian-trace form this result replaces
