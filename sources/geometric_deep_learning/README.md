# Geometric Deep Learning

*Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges* by
Michael M. Bronstein, Joan Bruna, Taco Cohen, and Petar Veličković is a
proto-book that develops a common geometric view of neural-network
architectures through symmetry, invariance, equivariance, locality, and scale
separation.

- Resource type: survey and proto-book
- Repository status: reference source; not part of the active curriculum
- Topics: `geometric_deep_learning`, `symmetry`, `invariance`, `equivariance`,
  `architectures`
- arXiv identifier: `2104.13478`
- Version: v2, revised May 2, 2021
- Official abstract: [arXiv:2104.13478v2](https://arxiv.org/abs/2104.13478v2)
- Official PDF: [arXiv PDF](https://arxiv.org/pdf/2104.13478v2)
- DOI: [10.48550/arXiv.2104.13478](https://doi.org/10.48550/arXiv.2104.13478)
- Living book site: [Geometric Deep Learning](https://geometricdeeplearning.com/book/)
- Local study copy:
  [`pdfs/geometric_deep_learning_arxiv_2104.13478v2.pdf`](./pdfs/geometric_deep_learning_arxiv_2104.13478v2.pdf)
- Local PDF metadata: 160 pages; 45,092,403 bytes; SHA-256
  `dcf8212ed37db9ac154ac975b8f9c7d36831cf56b75261679b04ab9814985fc2`
- Source status: verified against the official v2 arXiv metadata and PDF, and
  the authors' living book site, on August 19, 2026

## Storage and Version Boundary

The arXiv PDF is approximately 45 MB, above this repository's preferred 10 MB
limit. Its arXiv record uses the arXiv non-exclusive distribution license,
which should not be treated as a general redistribution grant. The living book
site separately states a CC BY-NC-ND license for its evolving book chapters.
This repository therefore tracks links and metadata while keeping the large
local study copy gitignored. Do not commit the PDF unless its redistribution
boundary and the repository size policy are deliberately revisited.

Use the versioned arXiv text for stable citations. Consult the living book site
for newer exposition, and record the chapter version or access date when an
authored artifact depends on material that differs from the 2021 proto-book.

## Why This Source Is Here

This source has one bounded role: explain how assumptions about a data domain
and its symmetries constrain useful neural-network building blocks. It is a
conceptual reference for questions about:

- invariance and equivariance;
- locality, receptive fields, pooling, and scale separation;
- CNNs on grids and group-equivariant CNNs; and
- extensions to sets, graphs, manifolds, and geometric graphs.

The proto-book explicitly treats representation-learning architectures as its
focus. It is not a primary source for score matching, diffusion objectives,
SDEs, reverse processes, or sampling algorithms.

## Selected Reading Map

- Section 3.1, pages 12-17: symmetry groups, group actions,
  representations, invariance, and equivariance.
- Sections 3.3-3.5, pages 19-30: deformation stability, scale separation,
  and the Geometric Deep Learning blueprint.
- Section 4.2, pages 35-40: grids and Euclidean spaces.
- Section 5.1, pages 69-74: CNNs, including multiscale architectures and
  U-Net in the broader CNN family.
- Optional Section 5.2, pages 74-77: group-equivariant CNNs.
- Optional Section 5.4, pages 80-83: Deep Sets, Transformers, and latent
  graph inference.

This map is a reference path, not an additional reading assignment.

## Revisit Triggers

Return to this source when at least one of these is true:

1. Weeks 25-26 reach the architecture-literacy module.
2. A Nano-Diffusion experiment asks whether an architectural symmetry should
   be built in rather than learned through augmentation.
3. A research question moves from image grids to rotations, sets, graphs,
   manifolds, molecules, or other structured domains.

At that point, promote only the sections needed for a concrete note,
derivation, or experiment. Do not add the entire proto-book to the curriculum.

## Potential Diffusion Research Bridge

A future project may use this source to ask which invariances of a target data
distribution should induce equivariances in a denoiser or score network, and
whether enforcing them improves data efficiency or generalization. That is a
repository research question, not a result established by this proto-book.

## Use from Authored Files

Link to this catalog when recording provenance. State whether a claim comes
from the stable 2021 proto-book, a later living-book chapter, or a repository
inference connecting geometric priors to diffusion research.
