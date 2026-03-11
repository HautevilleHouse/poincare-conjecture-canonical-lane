# Scripts

- `pc_closure_guard.py`: canonical-lane closure gate evaluator for the Poincare conjecture workspace.
- `extract_constants.py`: deterministic constant extraction from `artifacts/constants_extraction_inputs.json`.
- `promote_constants.py`: promotion step for registry and stitch constants.
- `update_manifest.py`: SHA-256 manifest refresh for tracked public files.
- `release_gate.py`: release-surface validator for normalized or fully extracted mode.

Guard inputs:

- `artifacts/constants_registry.json`
- `artifacts/stitch_constants.json`

Guard output:

- `repro/certificate_runtime.json`

Output schema includes:

- native gate keys (`PC_G*`),
- normalized gate layer (`G1..G6,GCoh,GM`) under `normalized`,
- strict pass flags: `all_pass`, `all_pass_normalized`.
