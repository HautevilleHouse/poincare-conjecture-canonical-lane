# Public Reproducibility Pack (Poincare Canonical Lane)

## Objective
Provide a local, hash-locked rerun path for the Poincare closure gate certificate.

Authoritative routing index:

- `paper/CANONICAL_ROUTING_INDEX.md`

## Included Artifacts

1. `repro_manifest.json`,
2. `run_repro.sh`,
3. baseline output `certificate_baseline.json`,
4. `THIRD_PARTY_RERUN_PROTOCOL.md`.

## Runner

From repository root:

```bash
bash repro/run_repro.sh
```

This executes:

```bash
python3 scripts/extract_constants.py --inputs artifacts/constants_extraction_inputs.json --out artifacts/constants_extracted.json
python3 scripts/promote_constants.py --extracted artifacts/constants_extracted.json --registry artifacts/constants_registry.json --stitch artifacts/stitch_constants.json --report artifacts/promotion_report.json
python3 scripts/pc_closure_guard.py --strict-coh-zero --registry artifacts/constants_registry.json --stitch artifacts/stitch_constants.json --out repro/certificate_runtime.json --history repro/drift_guard_runs.jsonl --pretty
python3 scripts/update_manifest.py --manifest repro/repro_manifest.json
python3 scripts/release_gate.py --mode fully_extracted --manifest repro/repro_manifest.json --registry artifacts/constants_registry.json --inputs artifacts/constants_extraction_inputs.json --pretty
```

## Pass Criteria

1. `repro/certificate_runtime.json` exists,
2. `lane.active_lane = manifold_constrained`,
3. `all_pass` is `true`,
4. all gates `PC_G1,PC_G2,PC_G3,PC_G4,PC_G5,PC_G6,PC_GM` are `PASS`,
5. manifest check reports `ok = true`,
6. release gate in `fully_extracted` mode reports `ok = true`.

## Current Runtime Snapshot

At current registry state:

- `PC_G1..PC_G6,PC_GM = PASS`,
- strict margin = `0.8`,
- lane remains `manifold_constrained`.
