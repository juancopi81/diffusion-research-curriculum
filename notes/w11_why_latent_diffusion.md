# Week 11 — Why Diffusion in a Learned Latent Space?

**Status:** Reviewed and approved by the learner on 2026-09-15; Week 11 complete.
Consolidated from our discussion and
the completed [MNIST VAE notebook](../notebooks/w11_minimal_vae_mnist_solved.ipynb).

## What our compression preserved and lost

Our VAE preserved some broad digit structure, like the zero's closed loop and
the one's stroke, but lost distinctive details. The two and five became harder
to recognize. These results reflect the two-dimensional bottleneck together
with the small network, brief training, and reconstruction–KL tradeoff; they
do not isolate the effect of compression alone. The images are blurry, but
no diffusion process was used in this notebook.

## From PCA to learned compression

PCA compresses through a linear projection. In our 2D-to-1D example, we could
measure the discarded variance, but the retained coordinate did not tell us
each point's original displacement in the discarded direction.

Probabilistic PCA describes a linear Gaussian latent-variable model with
Gaussian observation noise. It can propose a plausible displacement around
the linear subspace, but cannot identify the original point's lost displacement.
**Modeling missing variation is not the same as recovering discarded information.**
[Tipping and Bishop, §2](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bishop-ppca-jrss.pdf)

A VAE uses nonlinear networks to encode a distribution and decode sampled
latents, giving more flexibility than a linear mapping. Compression still
involves a tradeoff. Separately, the ELBO makes generally intractable
likelihood-based training workable; we do not need it merely because
reconstruction is imperfect. This is a conceptual connection between methods,
not a sequence of models that must all be trained.

## What latent diffusion learns

In the two-stage setup, we first train an autoencoder to provide useful
compressed representations and reconstruct images. We then keep it fixed
while training diffusion on encoded images. These latents can be spatial
feature maps, not just two-number vectors like ours.

During diffusion training, a prescribed forward process adds noise to clean
latents. The learned denoising model supports reversing that process. It learns
the distribution of encoded images, not the image-compression mapping itself.
At generation time:

**Latent noise → learned denoising process → generated clean latent → decoder → image.**

Unlike our notebook, which samples directly from a standard-normal prior and
decodes, latent diffusion first transforms noise into a latent through the
learned generation process. The encoder is not needed to generate an
unconditional image. [Rombach et al., §§3.1–3.2](https://arxiv.org/html/2112.10752v2#S3)

## Why do this, and what do we give up?

Smaller representations can reduce computation and memory across the repeated
denoising steps. The aim is to retain perceptually important information while
making generation cheaper—not to compress as aggressively as possible.
[Rombach et al., §4.1](https://arxiv.org/html/2112.10752v2#S4.SS1)

If compression discards information that distinguishes original details, the
decoder cannot reliably recover those exact details from the latent alone.
It may produce plausible details instead. Excessive compression can damage
global structure as well as fine detail, so a good compression stage matters
even with a strong diffusion model.

**Learning chain:** latent-variable model and ELBO → trainable reconstruction/KL
loss → encoding and decoding → learned compression → diffusion in latent space.
