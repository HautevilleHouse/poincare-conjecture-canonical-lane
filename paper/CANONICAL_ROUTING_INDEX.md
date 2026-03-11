# Canonical Routing Index (Poincare)

This file is the single routing map for where each proof package lives in:

- main preprint sections/appendices,
- mirror note files,
- certificate/artifact keys.

## Gate Routing

| Gate | Main preprint location | Mirror note | Registry/artifact key(s) |
|---|---|---|---|
| `PC_G1` (coercivity) | `Section 4`, `Appendix A` | `notes/EG1_public.md` | `kappa_coercive` |
| `PC_G2` (capture) | `Section 5`, `Appendix B` | `notes/EG2_public.md` | `sigma_capture` |
| `PC_G3` (compactness/no-Zeno) | `Section 5`, `Appendix C` | `notes/EG3_public.md` | `kappa_compact` |
| `PC_G4` (rigidity) | `Section 6.1`, `Appendix D` | `notes/EG4_public.md` | `rho_rigidity` |
| `PC_G5` (geometrization transfer) | `Section 6.2`, `Appendix E.4` | `notes/EG4_public.md` | `geometrization_factor` |
| `PC_G6` (strict coherence) | `Section 6.3`, `Appendix E.6` | `notes/IDENTIFICATION_BRIDGE.md` | `eps_coh` |
| `PC_GM` (final strict margin) | `Section 8`, `Appendix E.5` | derived | all above keys |

## Repro Routing

| Artifact | Path |
|---|---|
| Runner | `repro/run_repro.sh` |
| Guard | `scripts/pc_closure_guard.py` |
| Runtime certificate | `repro/certificate_runtime.json` |
| Baseline certificate | `repro/certificate_baseline.json` |
| Registry | `artifacts/constants_registry.json` |
| Stitch constants | `artifacts/stitch_constants.json` |
| Third-party rerun protocol | `repro/THIRD_PARTY_RERUN_PROTOCOL.md` |
