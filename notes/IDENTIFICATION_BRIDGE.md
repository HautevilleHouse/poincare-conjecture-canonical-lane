# Identification Bridge (PC Limit -> Spherical Endpoint Class)

In-paper location: `paper/POINCARE_CONJECTURE_PREPRINT.md` (Section 6.3, Appendix E).

## Goal
Prevent endpoint ambiguity: the extracted geometrized limit must lie in the intended spherical determining class.

## Determining Class

Choose observable class `C_det` of spherical endpoint invariants and normalized geometric response quantities.

Lock conditions:

1. matching values on `C_det`,
2. continuity under admissible extraction,
3. strict coherence target `eps_coh = 0`.

## Lemma Chain

### Lemma ID.1 (lock persistence)
If `U_n -> U_infty` and each `Obs_O` is continuous for `O in C_det`, then

`Lock_O(U_n) -> Lock_O(U_infty)`.

### Lemma ID.2 (determining-class uniqueness)
If `Lock_O(U_infty) = 0` for all `O in C_det`, then `U_infty` is the intended spherical endpoint representative.

### Theorem ID.3 (coherence closure)
If lock persistence and determining-class uniqueness hold and `eps_coh = 0`, then the identification bridge closes and `PC_G6 = PASS`.

## Current Instantiation

Strict mode enforces:

`eps_coh = 0`.
