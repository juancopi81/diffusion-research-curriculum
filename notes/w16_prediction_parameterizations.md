# Week 16 — Clean, Noise, and Score Prediction

**Status:** Day 2 completed on 2026-11-17, including Juan's read-through
and approval of this consolidated note. The
[daily plan](w16_study_plan.md) records the remaining sessions.

These are Juan's derivation attempts and our discussion, not an official
solution. The [original handwritten pages](#handwritten-pages) are preserved
unchanged, including the initial factorization and its correction.

## Setup and Prediction Conversions

Hold a noisy timestep fixed, with $0<\bar\alpha_t<1$:

$$
x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\epsilon,
\qquad \epsilon\sim\mathcal N(0,I).
$$

I first isolated $x_0$ using the known noise, then replaced the noise with
a prediction to obtain a clean-image estimate. Reversing the rearrangement
gave the corresponding noise estimate from a clean prediction:

$$
\hat x_{0,\theta}(x_t,t)
=\frac{x_t-\sqrt{1-\bar\alpha_t}\,\epsilon_\theta(x_t,t)}
{\sqrt{\bar\alpha_t}},
\qquad
\hat\epsilon_\theta(x_t,t)
=\frac{x_t-\sqrt{\bar\alpha_t}\,\hat x_{0,\theta}(x_t,t)}
{\sqrt{1-\bar\alpha_t}}.
$$

Both rearrangements were correct. Codex clarified the boundary in my first
page: allowing $\bar\alpha_t=0$ would make the clean conversion undefined.
The hats identify estimates; the original-noise rearrangement recovers the
actual $x_0$. These equations describe consistently converted outputs;
separately trained models need not make matching predictions.

## Deriving the Conditional Corruption Score

I chose the multivariate route, using the quadratic-form gradient from
the [Week 10 Gaussian proof](../proofs/w10_multivariate_gaussian_score.md#2-derivation).
With $x_0$ and $t$ fixed, define

$$
\mu=\sqrt{\bar\alpha_t}\,x_0,
\qquad \Sigma=(1-\bar\alpha_t)I.
$$

Then the terms depending on $x_t$ in the log density are

$$
\log q(x_t\mid x_0)
=-\frac12(x_t-\mu)^\top\Sigma^{-1}(x_t-\mu)+C.
$$

Using the symmetry of the precision matrix gives

$$
\nabla_{x_t}\log q(x_t\mid x_0)
=-\Sigma^{-1}(x_t-\mu).
$$

My general multivariate derivation was correct. Codex clarified two
notation points: retain $q$ inside the logarithm, and multiply by the
inverse covariance instead of writing division by a matrix. Since

$$
\Sigma^{-1}=\frac{1}{1-\bar\alpha_t}I,
$$

the conditional score is

$$
\nabla_{x_t}\log q(x_t\mid x_0)
=-\frac{x_t-\sqrt{\bar\alpha_t}\,x_0}{1-\bar\alpha_t}.
$$

Prompted to substitute the forward equation, I correctly used
$x_t-\sqrt{\bar\alpha_t}x_0=\sqrt{1-\bar\alpha_t}\,\epsilon$ and simplified:

$$
g:=\nabla_{x_t}\log q(x_t\mid x_0)
=-\frac{\epsilon}{\sqrt{1-\bar\alpha_t}}.
$$

This is an individual conditional-score target constructed from a known
clean source and noise draw.

## Ideal Predictors and the Marginal Score

Asked what minimizes noise MSE for a fixed noisy observation and timestep,
I correctly identified

$$
\epsilon^*(x_t,t)=\mathbb E[\epsilon\mid X_t=x_t,t],
$$

the average of compatible noise draws under their conditional distribution.
We used the MSE conditional-mean result already studied in
[Week 7](w07_conditional_expectation_in_diffusion.md#4-denoising-as-conditional-expectation);
no fresh proof was required or completed.

**Identity supplied by Codex:** The marginal noisy-data score is the
posterior average of the conditional scores:

$$
\nabla_{x_t}\log q_t(x_t)
=\mathbb E[g\mid X_t=x_t,t].
$$

Here $q_t$ averages over possible clean sources. Its posterior-average
identity is derived in the [Week 7 score discussion](w07_conditional_expectation_in_diffusion.md#checkpoint-52);
today I applied the supplied identity rather than rederiving it.

I correctly pulled the fixed-timestep coefficient outside the expectation:

$$
s_t(x_t):=\nabla_{x_t}\log q_t(x_t)
=-\frac{\mathbb E[\epsilon\mid X_t=x_t,t]}{\sqrt{1-\bar\alpha_t}}
=-\frac{\epsilon^*(x_t,t)}{\sqrt{1-\bar\alpha_t}}.
$$

Putting the ideal noise predictor into the clean conversion, I correctly
identified the result as the posterior mean clean image:

$$
m_t(x_t)
=\frac{x_t-\sqrt{1-\bar\alpha_t}\,\epsilon^*(x_t,t)}
{\sqrt{\bar\alpha_t}}
=\mathbb E[X_0\mid X_t=x_t,t].
$$

**Combined relation added by Codex:** These results also give

$$
s_t(x_t)
=\frac{\sqrt{\bar\alpha_t}\,m_t(x_t)-x_t}{1-\bar\alpha_t}.
$$

The clean posterior mean and marginal score are different quantities
connected by this transformation. The exact score equality uses the
population-optimal noise predictor; a trained network generally supplies
an approximation.

## Comparing Errors and Understanding Implicit Weighting

For predictions related by the clean/noise conversion, I subtracted the
true $x_0$ from the clean estimate. My setup with two fractions was
correct, but my initial final factorization incorrectly retained $x_t$ in
the purported scalar coefficient. Codex prompted me to combine the
numerators, cancel $x_t$, and distribute the subtraction carefully.

I then corrected the algebra to obtain

$$
\hat x_{0,\theta}-x_0
=\frac{\sqrt{1-\bar\alpha_t}}{\sqrt{\bar\alpha_t}}
(\epsilon-\epsilon_\theta)
=-\frac{\sqrt{1-\bar\alpha_t}}{\sqrt{\bar\alpha_t}}
(\epsilon_\theta-\epsilon).
$$

Asked to take squared Euclidean norms, I correctly squared the scalar
factor and removed the sign:

$$
\|\hat x_{0,\theta}-x_0\|_2^2
=\frac{1-\bar\alpha_t}{\bar\alpha_t}
\|\epsilon_\theta-\epsilon\|_2^2.
$$

Codex rearranged this into the form that weights clean-image error:

$$
\|\epsilon_\theta-\epsilon\|_2^2
=\frac{\bar\alpha_t}{1-\bar\alpha_t}
\|\hat x_{0,\theta}-x_0\|_2^2.
$$

Given $\bar\alpha_t=0.9$ and $0.1$, I correctly calculated weights $9$ and
$1/9$ and explained:

> So the same clean-image error contributes more at lower noise levels.
> Is that what they mean by implicit weighting?

**Interpretation confirmed by Codex:** Yes. Relative to unweighted
clean-image MSE, noise MSE weights the same clean-image squared error more
heavily at lower noise levels. The two example weights differ by a factor
of $81$. Even with uniformly sampled timesteps, this conversion introduces
different clean-error weights. That is the point in the
[HF training-objective discussion](https://huggingface.co/learn/diffusion-course/en/unit1/3#training-objective).

At one fixed timestep the positive scalar leaves the ideal minimizing
prediction unchanged. Across timesteps, the varying factors can change
training tradeoffs for a shared finite model. This comparison also holds
for per-image MSE when both errors average over the same coordinates.
It is separate from dropping the ELBO's own weights, discussed in
[Day 1](w16_hf_ddpm_training.md#my-questions-about-the-reading).

## Review Record and Next Step

- Juan supplied the clean/noise conversions and the multivariate Gaussian
  score derivation from given starting equations, invoking the Week 10
  quadratic-form result. Reference consultation during the handwritten work
  was not assessed; this is not labeled a notes-closed test.
- Codex corrected the boundary and matrix notation. Juan correctly
  substituted the forward noise into the conditional score.
- Juan identified the MSE-optimal noise predictor and posterior clean mean
  in response to prompts. The marginal-score averaging identity was
  supplied; Juan correctly applied linearity to derive its noise form.
- The error factorization required a cancellation/sign hint. Juan's
  corrected factorization, squared-error scaling, and numerical weighting
  interpretation were correct after that hint and the supplied rearrangement.

**Day 2 complete:** Juan read and approved this consolidation on 2026-11-17.
The derivations, discussion, and read-through meet Day 2's conceptual
stopping point. Active study time was not measured. Day 3 will trace
the sourced reverse sampler; the reverse-mean formula and full variational
bound have not been derived in this session.

## Handwritten Pages

| Page | Original work |
| --- | --- |
| 1 | [Clean estimate from noise prediction](figures/w16_day2_01_clean_from_noise_handwritten.png) |
| 2 | [Noise estimate from clean prediction](figures/w16_day2_02_noise_from_clean_handwritten.png) |
| 3 | [Multivariate Gaussian score derivation](figures/w16_day2_03_multivariate_score_handwritten.png) |
| 4 | [Precision substitution before notation clarification](figures/w16_day2_04_precision_substitution_attempt_handwritten.png) |
| 5 | [Conditional score expressed through noise](figures/w16_day2_05_conditional_score_noise_handwritten.png) |
| 6 | [Marginal score from the ideal noise predictor](figures/w16_day2_06_marginal_score_handwritten.png) |
| 7 | [Initial error-factorization attempt](figures/w16_day2_07_error_factorization_attempt_handwritten.png) |
| 8 | [Corrected error factorization](figures/w16_day2_08_error_factorization_correction_handwritten.png) |
| 9 | [Squared-error relationship](figures/w16_day2_09_squared_errors_handwritten.png) |
