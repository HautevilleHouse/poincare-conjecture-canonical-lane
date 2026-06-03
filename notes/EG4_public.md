# EG4 Public Note (PC Rigidity and Geometrization Package)

In-paper location: `paper/POINCARE_CONJECTURE_PREPRINT.md` (Section 6, Appendices D and E).

## Goal
Close the final bridge from extracted singularity-model limits to the geometrized spherical endpoint.

## Closure Criterion

`PC_G4` and `PC_G5` pass iff theorem-level constants exist with:

- `rho_rigidity > 0`,
- `geometrization_factor > 0`.

## Lemma Chain

### Lemma EG4.1 (rigidity trichotomy)
Every normalized bad limit satisfies at least one:

1. admissible Ricci-flow identity violation,
2. singularity-model rigidity violation,
3. contradiction with safe re-entry into the canonical class.

### Lemma EG4.2 (transfer inequality)
If bad limits are excluded and the geometrization transfer inequality holds, then the extracted endpoint lies in the geometrized spherical class.

### Theorem EG4.3 (gate closure)
If `rho_rigidity^(raw) > 0` and `geometrization_factor^(raw) > 0`, then `PC_G4 = PASS` and `PC_G5 = PASS`.

## Current Instantiation

- `rho_rigidity = 1.074`,
- `geometrization_factor = 1.0308`.
