#!/usr/bin/env python3
"""Canonical-lane closure guard for the Poincare conjecture workspace."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

DEFAULT_REGISTRY = 'artifacts/constants_registry.json'
DEFAULT_STITCH = 'artifacts/stitch_constants.json'
DEFAULT_OUT = 'repro/certificate_runtime.json'
DEFAULT_HISTORY = 'repro/drift_guard_runs.jsonl'

REQUIRED_KEYS = (
    'kappa_coercive',
    'sigma_capture',
    'kappa_compact',
    'rho_rigidity',
    'geometrization_factor',
    'eps_coh',
)


def _finite(v: Any) -> bool:
    return isinstance(v, (int, float)) and math.isfinite(float(v))


def _resolve(path_str: str) -> Path:
    p = Path(path_str).expanduser()
    if p.is_absolute():
        return p
    return PROJECT_ROOT / p


def _bootstrap_registry(path: Path) -> None:
    payload = {
        'constants': {
            k: {
                'value': None,
                'theorem_level': False,
                'source': '',
                'notes': 'pending theorem extraction',
            }
            for k in REQUIRED_KEYS
        }
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n')


def _load_registry(path: Path) -> dict[str, Any]:
    if not path.exists():
        _bootstrap_registry(path)
    data = json.loads(path.read_text())
    if not isinstance(data, dict):
        raise ValueError('registry must be JSON object')
    consts = data.get('constants')
    if not isinstance(consts, dict):
        raise ValueError('registry missing constants object')
    return data


def _load_sigma_from_stitch(path: Path) -> float | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text())
    except Exception:  # noqa: BLE001
        return None
    consts = data.get('constants')
    if not isinstance(consts, dict):
        return None
    sigma = consts.get('sigma_star_can')
    if isinstance(sigma, dict):
        v = sigma.get('value')
        return float(v) if _finite(v) else None
    return float(sigma) if _finite(sigma) else None


def _entry(constants: dict[str, Any], key: str) -> tuple[float | None, bool]:
    obj = constants.get(key)
    if isinstance(obj, dict):
        v = obj.get('value')
        theorem = bool(obj.get('theorem_level', False))
        return (float(v) if _finite(v) else None, theorem)
    if _finite(obj):
        return float(obj), False
    return None, False


def compute_report(data: dict[str, Any], sigma_star: float | None, strict_coh_zero: bool) -> dict[str, Any]:
    consts = data['constants']

    kappa_coercive, t1 = _entry(consts, 'kappa_coercive')
    sigma_capture, t2 = _entry(consts, 'sigma_capture')
    kappa_compact, t3 = _entry(consts, 'kappa_compact')
    rho_rigidity, t4 = _entry(consts, 'rho_rigidity')
    geometrization_factor, t5 = _entry(consts, 'geometrization_factor')
    eps_coh, t6 = _entry(consts, 'eps_coh')

    pc_g1 = t1 and _finite(kappa_coercive) and float(kappa_coercive) > 0.0
    pc_g2 = t2 and _finite(sigma_capture) and float(sigma_capture) > 0.0
    pc_g3 = t3 and _finite(kappa_compact) and float(kappa_compact) > 0.0
    pc_g4 = t4 and _finite(rho_rigidity) and float(rho_rigidity) > 0.0
    pc_g5 = t5 and _finite(geometrization_factor) and float(geometrization_factor) > 0.0
    pc_g6_base = t6 and _finite(eps_coh) and float(eps_coh) >= 0.0
    pc_g6 = pc_g6_base and ((abs(float(eps_coh)) < 1e-15) if strict_coh_zero else True)

    margin = None
    if all(
        _finite(x)
        for x in (
            kappa_coercive,
            sigma_capture,
            kappa_compact,
            rho_rigidity,
            geometrization_factor,
            eps_coh,
        )
    ):
        margin = min(
            float(kappa_coercive),
            float(sigma_capture),
            float(kappa_compact),
            float(rho_rigidity),
            float(geometrization_factor),
        ) - float(eps_coh)

    pc_gm = pc_g1 and pc_g2 and pc_g3 and pc_g4 and pc_g5 and pc_g6 and _finite(margin) and float(margin) > 0.0

    gates = {
        'PC_G1': 'PASS' if pc_g1 else 'FAIL',
        'PC_G2': 'PASS' if pc_g2 else 'FAIL',
        'PC_G3': 'PASS' if pc_g3 else 'FAIL',
        'PC_G4': 'PASS' if pc_g4 else 'FAIL',
        'PC_G5': 'PASS' if pc_g5 else 'FAIL',
        'PC_G6': 'PASS' if pc_g6 else 'FAIL',
        'PC_GM': 'PASS' if pc_gm else 'FAIL',
    }
    blockers = {
        'PC_G1': [] if pc_g1 else ['kappa_coercive missing/nonpositive or not theorem-level'],
        'PC_G2': [] if pc_g2 else ['sigma_capture missing/nonpositive or not theorem-level'],
        'PC_G3': [] if pc_g3 else ['kappa_compact missing/nonpositive or not theorem-level'],
        'PC_G4': [] if pc_g4 else ['rho_rigidity missing/nonpositive or not theorem-level'],
        'PC_G5': [] if pc_g5 else ['geometrization_factor missing/nonpositive or not theorem-level'],
        'PC_G6': [] if pc_g6 else ['eps_coh missing/invalid or strict-zero target failed'],
        'PC_GM': [] if pc_gm else ['strict margin <= 0 or upstream gates failed'],
    }
    normalized_gates = {
        'G1': gates['PC_G1'],
        'G2': gates['PC_G2'],
        'G3': gates['PC_G3'],
        'G4': gates['PC_G4'],
        'G5': gates['PC_G5'],
        'G6': 'NA',
        'GCoh': gates['PC_G6'],
        'GM': gates['PC_GM'],
    }
    normalized_blockers = {
        'G1': blockers['PC_G1'],
        'G2': blockers['PC_G2'],
        'G3': blockers['PC_G3'],
        'G4': blockers['PC_G4'],
        'G5': blockers['PC_G5'],
        'G6': [],
        'GCoh': blockers['PC_G6'],
        'GM': blockers['PC_GM'],
    }

    report = {
        'meta': {
            'computed_at_utc': dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
            'framework': 'poincare_conjecture',
        },
        'schema': {
            'normalized_gate_keys': ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'GCoh', 'GM'],
            'g6_policy': 'NA means this framework has no standalone pre-coherence G6 gate',
        },
        'lane': {
            'canonical_theorem_lane': 'manifold_constrained',
            'active_lane': 'manifold_constrained',
        },
        'inputs': {
            'kappa_coercive': kappa_coercive,
            'sigma_capture': sigma_capture,
            'kappa_compact': kappa_compact,
            'rho_rigidity': rho_rigidity,
            'geometrization_factor': geometrization_factor,
            'eps_coh': eps_coh,
            'sigma_star_can': sigma_star,
        },
        'derived': {
            'strict_margin': margin,
            'strict_coh_zero': bool(strict_coh_zero),
        },
        'gates': gates,
        'blockers': blockers,
        'normalized': {
            'gates': normalized_gates,
            'blockers': normalized_blockers,
        },
    }
    report['all_pass'] = all(v == 'PASS' for v in gates.values())
    report['all_pass_normalized'] = all(v in {'PASS', 'NA'} for v in normalized_gates.values()) and all(
        v == 'PASS' for v in normalized_gates.values() if v != 'NA'
    )
    return report


def append_history(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {
        'timestamp_utc': report['meta']['computed_at_utc'],
        'all_pass': report['all_pass'],
        'gates': report['gates'],
        'strict_margin': report['derived']['strict_margin'],
    }
    with path.open('a', encoding='utf-8') as f:
        f.write(json.dumps(row, sort_keys=True) + '\n')


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--registry', default=DEFAULT_REGISTRY)
    ap.add_argument('--stitch', default=DEFAULT_STITCH)
    ap.add_argument('--out', default=DEFAULT_OUT)
    ap.add_argument('--history', default=DEFAULT_HISTORY)
    ap.add_argument('--strict-coh-zero', action='store_true')
    ap.add_argument('--pretty', action='store_true')
    ns = ap.parse_args()

    registry_path = _resolve(ns.registry)
    stitch_path = _resolve(ns.stitch)
    out_path = _resolve(ns.out)
    history_path = _resolve(ns.history)

    data = _load_registry(registry_path)
    sigma_star = _load_sigma_from_stitch(stitch_path)
    report = compute_report(data, sigma_star=sigma_star, strict_coh_zero=bool(ns.strict_coh_zero))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2 if ns.pretty else None, sort_keys=True) + '\n')
    append_history(history_path, report)

    if ns.pretty:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(json.dumps(report, sort_keys=True))


if __name__ == '__main__':
    main()
