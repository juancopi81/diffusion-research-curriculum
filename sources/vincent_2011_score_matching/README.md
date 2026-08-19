# A Connection Between Score Matching and Denoising Autoencoders

Pascal Vincent's 2011 note connects a denoising objective with score matching
on a smoothed empirical data distribution. It is an active foundational source
for this repository's denoising-score targets and toy score-matching work.

- Author: Pascal Vincent
- Published as: *Neural Computation* 23(7), 1661-1674, July 2011
- Topics: `score_matching`, `denoising`, `denoising_autoencoders`,
  `energy_based_models`
- DOI and journal record:
  [10.1162/NECO_a_00142](https://doi.org/10.1162/NECO_a_00142)
- Author-hosted technical report:
  [Technical Report 1358](https://www.iro.umontreal.ca/~vincentp/Publications/smdae_techreport_1358_v1.pdf)
- Technical-report version: November 1, 2010; 15 PDF pages
- Local study copy:
  [`pdfs/vincent_2011_score_matching_technical_report.pdf`](./pdfs/vincent_2011_score_matching_technical_report.pdf)
- Local PDF metadata: 15 pages; 459,134 bytes; SHA-256
  `b586f6c73e9c4898f09e85c0e4dcbec6c743b3bec1044208c6b1533593dc7edc`
- Source status: verified against the journal metadata and the complete
  author-hosted technical report on August 19, 2026

## Storage and Redistribution Boundary

The journal article is published by MIT Press, and the author-hosted technical
report does not state an explicit redistribution license. This repository
therefore records provenance and official links while keeping the local study
copy gitignored. Do not commit the PDF unless permission or a compatible
license is documented here.

## What the Paper Establishes

Let $q_0$ be the empirical data distribution and let $q_\sigma$ be its
Gaussian Parzen smoothing. For $\sigma>0$, the paper develops this chain of
optimization-objective equivalences:

1. Explicit score matching on $q_\sigma$ is equivalent to implicit score
   matching under the stated regularity conditions.
2. Noise-gradient score matching against the conditional corruption score is
   equivalent to explicit score matching on the marginal $q_\sigma$.
3. For the particular tied-weight denoising autoencoder and energy function
   defined in the paper, this score-matching objective is also equivalent, up
   to a positive scale, to the squared reconstruction objective.

For Gaussian corruption $\tilde{x}=x_0+\sigma\epsilon$, the conditional target
in item 2 is

$$
\nabla_{\tilde{x}}\log q_\sigma(\tilde{x}\mid x_0)
=
\frac{x_0-\tilde{x}}{\sigma^2}
=
-\frac{\epsilon}{\sigma}.
$$

This is the practical bridge for the repository: clean/noisy pairs provide a
conditional score target even when the marginal score of $q_\sigma$ is not
available pointwise.

## Scope Boundaries

- The score being matched is that of the smoothed empirical density
  $q_\sigma$, not the unsmoothed empirical distribution.
- The explicit-score-matching regularity argument is stated for $\sigma>0$;
  the paper flags a boundary as $\sigma\to0$.
- The final denoising-autoencoder equivalence uses the paper's specific
  sigmoid encoder, tied weights, linear decoder, Gaussian corruption, squared
  reconstruction loss, and associated energy function.
- The paper does not establish equivalence of finite-time optimization for
  arbitrary modern network parameterizations.
- It does not explain why one objective outperformed another in this
  repository's short Checkpoint 02 experiment.
- It is not a source for a complete diffusion process, reverse sampler, or
  multi-noise-level training system.

## Selected Reading Map

- Section 3, equations (2)-(5): explicit and implicit score matching.
- Section 4, equations (6)-(10): the smoothed marginal objective, conditional
  noise-gradient target, and their equivalence.
- Section 4, equations (11)-(14): the architecture-specific energy function
  and denoising-autoencoder equivalence.
- Section 5, especially equation (15): consolidated result, interpretation,
  and limitations.
- Appendix A, equations (16)-(18): proof that conditional noise-gradient score
  matching and explicit score matching differ only by constants independent
  of the model parameters.

For the current curriculum, passes 1-2 over Sections 3-5 are sufficient:
identify the claim and evidence, then reproduce the load-bearing conditional
target and state the architecture boundary. Appendix A belongs to a later
derivation pass.

## Use in This Repository

- [`notes/w03_score_of_gaussian.md`](../../notes/w03_score_of_gaussian.md)
  previews the Gaussian conditional-score target.
- [`mini_projects/checkpoint_02_toy_score_matching/report.md`](../../mini_projects/checkpoint_02_toy_score_matching/report.md)
  uses that target to train a direct score predictor at one noise level.
- [`CURRICULUM.md`](../../CURRICULUM.md) assigns a bounded source check inside
  the existing Week 8 artifact rather than creating a separate paper-reading
  cadence.

## Use from Authored Files

Link to this catalog when using the Gaussian conditional-score target. Keep
three claims separate: the general score-matching equivalence, the
architecture-specific denoising-autoencoder equivalence, and any empirical
finding produced by this repository.
