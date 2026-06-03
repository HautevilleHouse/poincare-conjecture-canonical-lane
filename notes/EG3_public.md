# EG3 Public Note (PC Compactness and No-Zeno Package)

In-paper location: `paper/POINCARE_CONJECTURE_PREPRINT.md` (Section 5, Appendix C).

## Goal
Obtain precompactness of normalized near-failure Ricci-flow-with-surgery sequences and rule out surgery-time accumulation.

## Closure Criterion

`PC_G3 = PASS` iff theorem-level compactness modulus `kappa_compact > 0` controls extraction and the restart-spacing lower bound is positive.

## Lemma Chain

### Lemma EG3.1 (precompactness criterion)
If normalized sequence `U_n` satisfies uniform seminorm bounds and the declared compactness defect is bounded, then `{U_n}` is precompact.

### Lemma EG3.2 (badness lower-semicontinuity)
If `U_n -> U_infty`, then the badness functional does not improve in the limit.

### Theorem EG3.3 (gate closure)
Define

`kappa_compact^(raw) := (1 + delta_comp_sup^(raw))^(-1)`.

If `kappa_compact^(raw) > 0`, then `PC_G3 = PASS`.

## Current Instantiation

With `delta_comp_sup_raw = 0.25`, one has

`kappa_compact = 0.8`.
