# Source Library

This directory is the repository's immutable reference layer for third-party
material used by authored artifacts or retained for a specific, documented
future research trigger.

## Conventions

- Keep authored work in `notes/`, `proofs/`, `notebooks/`, or `papers/`.
- Do not modify third-party originals stored below `sources/`.
- Organize collection directories by source, not by broad topic. Use a stable,
  unambiguous source key for the directory name; a source series may contain
  source-specific subcollections.
- Represent topics as many-to-many metadata in each collection catalog using a
  `Topics:` field with normalized lowercase tags. A source may have several
  topics, and the same topic may appear in several source catalogs. Topic
  indexes or wiki pages may aggregate these tags later, but they do not own or
  duplicate the source files.
- Every source collection must include a `README.md` recording provenance,
  official URLs, descriptive metadata, and known redistribution status.
- A source without current authored use must state its unique role, scope
  exclusions, selected reading map, and revisit trigger; general interest alone
  is not enough for inclusion.
- A locally available source is not automatically safe to publish. Keep
  copyrighted binaries gitignored unless a compatible license or explicit
  permission is documented in the collection catalog.
- Prefer links to the collection catalog from authored work. The catalog can
  point to both a local study copy and the durable official source.

## Collections

- [Step-by-Step Diffusion: An Elementary Tutorial](./step_by_step_diffusion/)
- [Vincent (2011): Score Matching and Denoising Autoencoders](./vincent_2011_score_matching/)
- [Geometric Deep Learning](./geometric_deep_learning/)
- [Mathematics for Machine Learning](./mml/)
- [Stat 110 Strategic Practice and Homework](./stat110/strategic-practice/)
