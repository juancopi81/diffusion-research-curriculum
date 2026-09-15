# MIT 6.S184: Introduction to Flow Matching and Diffusion Models

This course supplies the curriculum's ODE/SDE and flow-matching backbone,
with selected lectures supporting guidance and architecture work earlier in
the plan. Use it within existing weekly sessions and Nano-Diffusion/Nano-Flow
artifacts rather than as a separate syllabus.

- Edition: MIT IAP 2026
- Lecture instructor: Peter Holderrieth
- Course-note authors: Peter Holderrieth and Ezra Erives
- Topics: `diffusion`, `flow_matching`, `score_matching`, `sde`, `ode`,
  `guidance`, `neural_architectures`
- Official course: [2026 course page](https://diffusion.csail.mit.edu/2026/index.html)
- Official notes: [2026 lecture notes PDF](https://diffusion.csail.mit.edu/2026/docs/lecture_notes.pdf)
- Provenance checked: September 7, 2026, against the course page's lecture
  titles, recording links, lab links, and notes citation.
- Redistribution status: the course page states CC BY-NC-SA. This catalog
  retains links only; no third-party PDFs, videos, or notebooks are copied.
  Check asset-specific terms before redistributing individual materials.

## Selected Curriculum Map

These placements are our study plan, not the MIT course's prescribed order.

| Existing weeks | Recording | Use |
| --- | --- | --- |
| 21–22 | [Lecture 3-B: Classifier-free Guidance](https://www.youtube.com/watch?v=8oWZ1bHwyRI) | Support the MNIST guidance experiment |
| 25–26 | [Lecture 4: Latent Spaces and Neural Network Architectures](https://www.youtube.com/watch?v=g0MB1CCBmsI) | Connect U-Nets, transformers, and VAEs |
| 29–30 | [Lecture 1: Flow and Diffusion Models](https://www.youtube.com/watch?v=9eJQQVrUUoI) | Introduce ODE/SDE sampling before the Euler–Maruyama artifact |
| 33–34 | [Lecture 3-A: Score Functions and Score Matching](https://www.youtube.com/watch?v=ngC3QnYSVNM) | Connect score training with SDE sampling |
| 35–36 | [Lecture 2: Flow Matching](https://www.youtube.com/watch?v=PNkMKWW8Khw) | Support the existing 2D Nano-Flow experiment |

## Selected Labs

- Weeks 29–30: [Lab 1: Working with ODEs and SDEs](https://drive.google.com/file/d/1hddGSpAn1rfTQI2zacx2ueOrpAq_Boqd/view?usp=sharing).
  Select exercises that support the Euler–Maruyama notebook.
- Weeks 35–36: [Lab 2: Flow Matching and Score Matching](https://drive.google.com/file/d/1L2ntkxl04jiiz-t40sKscXhEC_XD5FQp/view?usp=sharing).
  Select flow-matching exercises that support the existing 2D implementation.

Lab titles and destinations are verified from the course page; individual
exercise contents have not been reviewed. Choose exercises when reaching
the corresponding weeks. Full lab completion and separate lab artifacts are
not required. No additional enrichment sessions are scheduled.

See [the curriculum](../../CURRICULUM.md) for the surrounding readings,
experiments, and implementation conventions.
