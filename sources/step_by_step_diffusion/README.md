# Step-by-Step Diffusion: An Elementary Tutorial

*Step-by-Step Diffusion: An Elementary Tutorial* by Preetum Nakkiran,
Arwen Bradley, Hattie Zhou, and Madhu Advani presents an introductory route
from Gaussian diffusion through DDPM, DDIM, flow matching, and practical
diffusion design.

- arXiv identifier: `2406.08929`
- Version: v2, revised June 23, 2024
- Topics: `diffusion`, `denoising`, `score_estimation`, `flow_matching`,
  `sampling`
- Official abstract: [arXiv:2406.08929v2](https://arxiv.org/abs/2406.08929v2)
- Official PDF: [arXiv PDF](https://arxiv.org/pdf/2406.08929v2)
- DOI: [10.48550/arXiv.2406.08929](https://doi.org/10.48550/arXiv.2406.08929)
- Local source copy: [`pdfs/step_by_step_diffusion_v2.pdf`](./pdfs/step_by_step_diffusion_v2.pdf)
- Local PDF metadata: 51 pages; SHA-256
  `dbe691ba686abc29612f2c737c7472eded285b373f56005690fedc1669d953c8`
- License: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- Redistribution status: the license permits sharing the unmodified paper with
  attribution for noncommercial purposes. This repository stores the official
  v2 PDF unchanged and retains the license and source links here.

## Curriculum Reading Map

- Pages 3-6, Sections 1.1-1.2: Gaussian forward diffusion, ideal reverse
  sampling, and the abstract reverse-sampler definition.
- Pages 6-7, Section 1.3: discretization and the per-step variance
  $\sigma_q^2\Delta t$.
- Pages 9-10, Section 2.1: the Bayes-rule and Taylor-expansion derivation of
  the approximately Gaussian reverse conditional.
- Appendix B.1: the more careful one-dimensional KL-error argument behind the
  informal derivation.

The first two readings are accessible after the probability, conditioning,
Gaussian-score, multivariate-Gaussian, and introductory Taylor-expansion work
in Weeks 1-8. Section 2.1 is a useful bridge into the forward and reverse
diffusion work planned for Weeks 15-16.

## Notation Caveat in Figure 2

Equation (1) defines

$$
x_t=x_{t-1}+\eta_{t-1},
\qquad
\eta_{t-1}\sim\mathcal{N}(0,\sigma^2 I).
$$

Therefore the forward transition is

$$
p(x_t\mid x_{t-1})
=
\mathcal{N}(x_t;x_{t-1},\sigma^2 I),
$$

or, equivalently, the increment $x_t-x_{t-1}$ is
$\mathcal{N}(0,\sigma^2 I)$. The Figure 2 caption writes
$p(x_t\mid x_{t-1})=\mathcal{N}(0,\sigma^2)$; read this as shorthand for the
zero-mean increment distribution. The centered-difference likelihood used in
Section 2.1 confirms the shifted transition above.

## Use from Authored Files

Link to this catalog when recording provenance. When referring to the reverse
Gaussian approximation, distinguish the heuristic statement in Section 2.1
from the exact conditional-mean identity attributed there to Tweedie's
formula.
