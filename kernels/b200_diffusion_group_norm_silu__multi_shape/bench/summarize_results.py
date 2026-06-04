#!/usr/bin/env python3
"""Summarize a benchmark results JSONL: per-row table, bucket views, gates.

Usage:
    python3 bench/summarize_results.py bench/results_v1.jsonl [--markdown]

Reports:
  - headline equal-weight geomean over production rows (+ arithmetic mean);
  - promotion-gate checks: geomean > 1.0 and no production row < 0.97x;
  - per-(layout, size-bucket) geomeans for crossover analysis;
  - the slowest/fastest rows and every row below the no-regression floor;
  - optional full per-row markdown table (median/mean/std/min/p10/p90 both
    sides, speedup, layout, entry point) for docs/results.md.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

GATE_ROW_FLOOR = 0.97


def load(path: Path):
    prov, rows = None, []
    with path.open() as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            if rec.get("event") == "provenance":
                prov = rec
            elif rec.get("event") == "result":
                rows.append(rec)
    return prov, rows


def gsize(row) -> int:
    shp = row.get("workload", {}).get("shapes", {}).get("x")
    if not shp:
        return -1
    spatial = 1
    for s in shp[2:]:
        spatial *= s
    return (shp[1] // 32) * spatial


def buckets(rows):
    out = {}
    for r in rows:
        shapes = r.get("workload", {}).get("shapes", {})
        layout = "NC" if shapes.get("layout") == "channels_last_3d" else "C"
        n = gsize(r)
        size = "small(<64K)" if n < (1 << 16) else ("mid(64K-1M)" if n < (1 << 20) else "large(>=1M)")
        out.setdefault((layout, size), []).append(r)
    return out


def geomean(vals):
    vals = [v for v in vals if v and v > 0]
    if not vals:
        return float("nan")
    return math.exp(sum(math.log(v) for v in vals) / len(vals))


def gate_outcomes(prod):
    """Pure promotion-gate computation over production rows.

    Returns (gm, below, explained, unexplained):
      - gm: equal-weight geomean of speedups;
      - below: rows under GATE_ROW_FLOOR;
      - explained: below-floor rows on the baseline-equivalent path (identical
        implementation on both sides — regression impossible by construction;
        the reading is the characterized order-debt artifact, see
        docs/dispatch.md);
      - unexplained: every other below-floor row (hard FAIL).
    """
    gm = geomean([r["speedup"] for r in prod])
    below = [r for r in prod if r["speedup"] < GATE_ROW_FLOOR]
    explained = [r for r in below if r.get("matched_status") == "baseline_equivalent"]
    unexplained = [r for r in below if r.get("matched_status") != "baseline_equivalent"]
    return gm, below, explained, unexplained


def _self_test() -> int:
    """Verify the exit-code semantics of the promotion gates.

    Scenarios: strict pass; explained-residual pass (below-floor row on the
    baseline-equivalent path with geomean > 1.0); unexplained below-floor row
    (must fail); geomean <= 1.0 (must fail); failed benchmark row (must fail).
    Exits 0 only if every scenario produces the specified verdict.
    """
    def row(speed, matched="optimized"):
        return {
            "speedup": speed,
            "matched_status": matched,
            "production": True,
            "baseline": {"median_us": 100.0},
            "candidate": {"median_us": 100.0 / speed},
        }

    cases = [
        ("strict_pass", [row(2.0), row(1.1)], False, True),
        ("explained_residual_pass", [row(2.0), row(0.95, "baseline_equivalent")], False, True),
        ("unexplained_below_floor_fail", [row(2.0), row(0.95)], False, False),
        ("low_geomean_fail", [row(0.5)], False, False),
        ("failed_row_fail", [row(2.0)], True, False),
    ]
    mismatches = 0
    for name, prod, any_failed_rows, expect_ok in cases:
        gm, below, explained, unexplained = gate_outcomes(prod)
        ok = (not any_failed_rows) and gm > 1.0 and not unexplained
        status = "ok" if ok == expect_ok else "MISMATCH"
        if ok != expect_ok:
            mismatches += 1
        print(f"self-test {name}: ok={ok} expected={expect_ok} -> {status}")
    print("self-test:", "PASS" if mismatches == 0 else f"FAIL ({mismatches} mismatches)")
    return 0 if mismatches == 0 else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("results", type=Path, nargs="?")
    ap.add_argument("--markdown", action="store_true", help="emit full per-row table")
    ap.add_argument(
        "--self-test",
        action="store_true",
        help="verify the promotion-gate exit-code semantics on synthetic rows",
    )
    args = ap.parse_args()

    if args.self_test:
        return _self_test()
    if args.results is None:
        ap.error("results path is required unless --self-test is given")

    _prov, rows = load(args.results)
    passed = [r for r in rows if r.get("status") == "PASSED"]
    failed = [r for r in rows if r.get("status") != "PASSED"]
    prod = [r for r in passed if r.get("production", True)]

    print(f"rows: {len(rows)} passed: {len(passed)} failed: {len(failed)} production: {len(prod)}")
    for r in failed:
        print(f"  FAILED: {r.get('id')} -> {r.get('status')} {r.get('message','')[:120]}")

    sp = [r["speedup"] for r in prod]
    am = sum(sp) / len(sp) if sp else float("nan")
    # No-regression gate has two PASS outcomes (promotion ruling DEC-3 /
    # AC-5.2): strict (zero rows below the floor) or explained-residual
    # (every below-floor row runs the baseline-equivalent path — identical
    # implementation on both sides, so a real regression is impossible; the
    # reading is the characterized order-debt measurement artifact, see
    # docs/dispatch.md "Measured Residual on Routed Giant Rows"). A
    # below-floor row on an OPTIMIZED path is a hard FAIL.
    gm, below, explained, unexplained = gate_outcomes(prod)
    print(f"headline geomean (production, equal weight): {gm:.4f}")
    print(f"arithmetic mean (secondary): {am:.4f}")
    print(f"gate geomean>1.0: {'PASS' if gm > 1.0 else 'FAIL'}")
    if not below:
        print(f"gate no row <{GATE_ROW_FLOOR}: PASS (strict)")
    elif not unexplained:
        print(f"gate no row <{GATE_ROW_FLOOR}: PASS (explained residual: "
              f"{len(explained)} baseline-equivalent row(s) below floor)")
        for r in sorted(explained, key=lambda r: r["speedup"]):
            print(f"  explained-residual: {r['id']} speedup={r['speedup']:.4f} "
                  f"path={r.get('candidate_path')} regime={r.get('candidate_regime')} "
                  f"(identical code both sides; see docs/dispatch.md)")
    else:
        print(f"gate no row <{GATE_ROW_FLOOR}: FAIL ({len(unexplained)} unexplained rows)")
    for r in sorted(unexplained, key=lambda r: r["speedup"])[:20]:
        print(f"  below-floor (UNEXPLAINED): {r['id']} speedup={r['speedup']:.4f} "
              f"path={r.get('candidate_path')} regime={r.get('candidate_regime')} "
              f"base={r['baseline']['median_us']:.1f}us cand={r['candidate']['median_us']:.1f}us")

    print("\nper-bucket geomeans:")
    for (layout, size), rs in sorted(buckets(prod).items()):
        print(f"  {layout:>2} {size:<13} n={len(rs):3d} geomean={geomean([r['speedup'] for r in rs]):.4f} "
              f"min={min(r['speedup'] for r in rs):.4f} max={max(r['speedup'] for r in rs):.4f}")

    ranked = sorted(prod, key=lambda r: r["speedup"])
    print("\nworst 8:")
    for r in ranked[:8]:
        print(f"  {r['id']:<40} {r['speedup']:.4f} base={r['baseline']['median_us']:.1f}us")
    print("best 8:")
    for r in ranked[-8:]:
        print(f"  {r['id']:<40} {r['speedup']:.4f} base={r['baseline']['median_us']:.1f}us")

    if args.markdown:
        print("\n| id | layout | function | path | regime | matched | baseline med/mean/std/min/p10/p90 (us) | candidate med/mean/std/min/p10/p90 (us) | speedup |")
        print("|---|---|---|---|---|---|---|---|---|")
        for r in sorted(prod, key=lambda r: r["id"]):
            wl = r.get("workload", {})
            shapes = wl.get("shapes", {})
            layout = "NC" if shapes.get("layout") == "channels_last_3d" else "C"
            def fmt(side):
                s = r[side]
                return (f"{s['median_us']:.2f}/{s['mean_us']:.2f}/{s['std_us']:.2f}/"
                        f"{s['min_us']:.2f}/{s['p10_us']:.2f}/{s['p90_us']:.2f}")
            print(f"| {r['id']} | {layout} | {wl.get('function','')} "
                  f"| {r.get('candidate_path','-')} | {r.get('candidate_regime','-')} "
                  f"| {r.get('matched_status','-')} "
                  f"| {fmt('baseline')} | {fmt('candidate')} | {r['speedup']:.4f} |")

    # Machine-enforceable verdict: the exit code IS the promotion gate.
    status_ok = not failed
    geomean_ok = gm > 1.0
    row_gate_ok = not unexplained
    return 0 if (status_ok and geomean_ok and row_gate_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
