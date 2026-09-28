# Week 12 — Flows and Score-Based Diffusion

**Status:** Reviewed and approved by the learner on 2026-09-28. Consolidated
from the Week 12 RealNVP notebook and our Session 8 discussion.

## What each model learns

In our RealNVP notebook, the forward map takes data to a Gaussian latent:

$$
z=f_\theta(x),
\qquad
\log p_\theta(x)
=\log p_Z(f_\theta(x))
+\log\left|\det J_{f_\theta}(x)\right|.
$$

Invertibility lets us evaluate this density exactly **under the learned model**.
It does not mean that $p_\theta$ exactly equals the unknown data density.
The Jacobian correction accounts for how the map expands or contracts volume;
we trained the flow by minimizing negative log likelihood (NLL). To generate,
we draw $z$ from the Gaussian base distribution and apply $f_\theta^{-1}$.
Our six-layer model lowered held-out NLL to about 2.44 and generated four
visible concentrations, but also placed some samples in the sparse regions
between the target blobs. The plots and NLL assess different aspects of fit.

Our Week 8 toy learned a different quantity: either a clean-sample prediction
$\hat x_0(x_t)$ converted to a score, or a score predicted directly. At its
single Gaussian noise level, the score is the vector field
$\nabla_{x_t}\log p_\sigma(x_t)$: the local direction in which the **noisy**
data log density rises. It is not a value of $\log p(x)$ at each point. Week 8
compared score errors; it did not train across a noise schedule or implement
reverse-process sampling.

## How generation differs

The score gives useful directions, but repeatedly moving uphill without a
sampling mechanism tends to concentrate points near density peaks. With
several blobs, points may head toward different nearby peaks, not necessarily
the overall mean. For one fixed noise level, a stochastic method such as
Langevin sampling can combine score-guided motion with fresh random noise;
its target is the **smoothed density at that noise level**, assuming a suitable
score and sampling procedure. A full score-based diffusion model instead
learns denoising information across noise levels and generates through a
sequence of reverse updates from noise. Some reverse samplers inject noise at
each step; deterministic variants can still generate varied samples because
their initial noise is random. Our Week 8 exercise did not test any of these
samplers.

RealNVP generation uses a Gaussian draw followed by one inverse traversal of
the flow's layers. This gives direct sampling and a tractable model density.
Diffusion generation uses many reverse updates and does not obtain the same
direct change-of-variables likelihood from a denoising or score predictor.
Neither property alone guarantees better-looking samples or a better fit to
the data.

**Learning chain:** change of variables $\rightarrow$ exact model NLL and
inverse sampling $\rightarrow$ score or denoising prediction $\rightarrow$
iterative generation.

**Local evidence:** [Week 12 RealNVP solved notebook](../notebooks/w12_realnvp_2d_blobs_solved.ipynb), [Week 8 score-matching report](../mini_projects/checkpoint_02_toy_score_matching/report.md), and [Week 12 flow foundations](w12_cs236_normalizing_flows.md).
