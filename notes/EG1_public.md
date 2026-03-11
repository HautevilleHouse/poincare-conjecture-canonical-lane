# EG1 Public Note (PC Coercive Monotonicity Package)

In-paper location: `paper/POINCARE_CONJECTURE_PREPRINT.md` (Section 4, Appendix A).

## Goal
Establish a uniform projected coercive floor on the Ricci-flow response sector:

`<xi, E_tau xi> >= kappa_coercive ||xi||^2`, with `kappa_coercive > 0`.

## Closure Criterion

`PC_G1 = PASS` iff:

1. `kappa_coercive` exists and is theorem-level,
2. `kappa_coercive > 0`,
3. the lower bound is uniform on the declared canonical tube.

## Lemma Chain

### Lemma EG1.1 (comparison reduction)
If `<xi, K_tau xi> >= A_ker,* ||xi||^2` and
`<xi, E_tau xi> >= c_* <xi, K_tau xi> - e_* ||xi||^2`, then

`<xi, E_tau xi> >= (c_* A_ker,* - e_*) ||xi||^2`.

### Lemma EG1.2 (tube perturbation transfer)
If `||E_tau - E_tau*|| <= L_E,* |tau-tau*|` on radius `r_*`, then

`lambda_min(E_tau|H_resp) >= lambda_min(E_tau*|H_resp) - L_E,* r_*`.

### Theorem EG1.3 (gate closure)
Define

`kappa_coercive^(raw) := c_* A_ker,* - e_*`.

If `kappa_coercive^(raw) > 0`, then `PC_G1 = PASS` with
`kappa_coercive := kappa_coercive^(raw)/kappa_coercive,ref > 0`.

## Current Instantiation

Using the tracked extraction components:

- `c_star_raw = 1.4625`,
- `A_ker_raw = 0.918`,
- `e_star_raw = 0.24225`.

Hence:

`kappa_coercive = 1.100325`.
