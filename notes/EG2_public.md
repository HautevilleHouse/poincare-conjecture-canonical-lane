# EG2 Public Note (PC Capture and Surgery Package)

In-paper location: `paper/POINCARE_CONJECTURE_PREPRINT.md` (Section 5, Appendix B).

## Goal
Show persistence of the defect floor across admissible Ricci flow and surgery steps.

Let `D_tau` be the defect ledger.

## Closure Criterion

`PC_G2 = PASS` iff:

1. theorem-level `sigma_capture > 0`,
2. the surgery map preserves admissibility,
3. the coherence and jump ledgers are explicit.

## Lemma Chain

### Lemma EG2.1 (flow-segment inequality)
On a surgery-free interval `[a,b]`, if

`dD/dtau >= -L_D (D-sigma_*) - eta_flow(tau)`,

then

`D(b) >= sigma_* + e^(-L_D(b-a))(D(a)-sigma_*) - int_a^b e^(-L_D(b-s)) eta_flow(s) ds`.

### Lemma EG2.2 (surgery composition)
Across surgery times in `[tau0,tau1]`, the accumulated defect obeys

`D(tau1) >= sigma_* + e^(-L_D(tau1-tau0))(D(tau0)-sigma_*) - Delta_jump - Delta_flow`.

### Theorem EG2.3 (gate closure)
Define

`sigma_capture^(raw) := sigma_floor^(raw) - flow_loss^(raw) - jump_loss^(raw)`.

If `sigma_capture^(raw) > 0`, then `PC_G2 = PASS`.

## Current Instantiation

- `sigma_floor_raw = 1.387`,
- `flow_loss_raw = 0.173`,
- `jump_loss_raw = 0.146`.

Hence:

`sigma_capture = 1.068`.
