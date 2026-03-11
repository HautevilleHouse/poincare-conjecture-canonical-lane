# Constant Extraction Spec (PC)

This file defines the theorem-constant extraction contract for this repository.

## Objective
Move constants from manual placeholder assignment to deterministic promotion:

1. extract raw constants from explicit component inputs + formulas,
2. normalize by declared references,
3. promote into `artifacts/constants_registry.json` and `artifacts/stitch_constants.json`.

## Inputs
- `artifacts/constants_extraction_inputs.json`

## Extracted Output
- `artifacts/constants_extracted.json`

## Promotion Output
- `artifacts/constants_registry.json`
- `artifacts/stitch_constants.json`
- `artifacts/promotion_report.json`

## Formula Set
- `kappa_coercive_raw = c_star_raw * A_ker_raw - e_star_raw`
- `sigma_capture_raw = sigma_floor_raw - flow_loss_raw - jump_loss_raw`
- `kappa_compact_raw = 1 / (1 + delta_comp_sup_raw)`
- `rho_rigidity_raw = rho_rigidity_raw`
- `geometrization_factor_raw = geometrization_factor_raw`
- `eps_coh_raw = eps_coh_raw`
- `sigma_star_can_raw = sigma_star_can_raw`

## Validations
- positivity required for: `kappa_coercive`, `sigma_capture`, `kappa_compact`, `rho_rigidity`, `geometrization_factor`, `sigma_star_can`
- nonnegative required for: `eps_coh`
- strict-zero required for: `eps_coh` in strict mode

## Execution
`repro/run_repro.sh` runs:
1. `scripts/extract_constants.py`
2. `scripts/promote_constants.py`
3. `scripts/pc_closure_guard.py`
