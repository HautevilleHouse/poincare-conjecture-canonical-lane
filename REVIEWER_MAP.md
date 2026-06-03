# Reviewer Map

## Claim Scope

- Canonical-lane claim: inside the `manifold_constrained` lane, if the theorem chain in this repository holds and the guard certificate passes, the repository-level Poincare closure claim is satisfied.
- Classical mapping claim: carried by the in-repo bridge theorems tying the Ricci-flow lane to the geometrization target statement.

## Theorem Dependency Chain

1. `EG1`: coercive monotonicity and singularity-control floor.
2. `EG2`: capture and surgery-compatible continuation.
3. `EG3`: compactness and no-Zeno surgery spacing.
4. `EG4`: rigidity and geometrization transfer.
5. Identification bridge: strict coherence on the determining class.
6. Scalar closure: `PC_G1, PC_G2, PC_G3, PC_G4, PC_G5, PC_G6, PC_GM` all `PASS`.

Primary files:

- `paper/POINCARE_CONJECTURE_PREPRINT.md`
- `notes/EG1_public.md`
- `notes/EG2_public.md`
- `notes/EG3_public.md`
- `notes/EG4_public.md`
- `notes/IDENTIFICATION_BRIDGE.md`

## Closure Gates

| Gate | Constant | Description |
|------|----------|-------------|
| `PC_G1` | `kappa_coercive` | coercive Ricci-flow floor on the admissible tube |
| `PC_G2` | `sigma_capture` | defect capture under flow and surgery |
| `PC_G3` | `kappa_compact` | compactness and restart-spacing control |
| `PC_G4` | `rho_rigidity` | rigidity exclusion of bad singularity limits |
| `PC_G5` | `geometrization_factor` | transfer from rigid limit to geometrization closure |
| `PC_G6` | `eps_coh` | strict coherence / identification closure |
| `PC_GM` | derived | final strict margin |

## Falsification Conditions

- `repro/certificate_runtime.json` has any non-`PASS` gate.
- `lane.active_lane != "manifold_constrained"`.
- `all_pass != true`.
- Any manifest hash mismatch under `repro/repro_manifest.json`.
- A verified counterexample to any EG theorem statement used in the paper.

## Reproducibility Check

Run:

```bash
bash repro/run_repro.sh
```

Then verify:

```bash
python3 - <<'PY'
import json
from pathlib import Path
d=json.loads(Path('repro/certificate_runtime.json').read_text())
assert d.get('all_pass') is True
assert d.get('lane',{}).get('active_lane') == 'manifold_constrained'
for g in ['PC_G1','PC_G2','PC_G3','PC_G4','PC_G5','PC_G6','PC_GM']:
    assert d['gates'].get(g) == 'PASS', g
print('OK')
PY
```
