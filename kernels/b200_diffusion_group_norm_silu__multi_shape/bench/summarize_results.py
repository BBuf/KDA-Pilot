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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("results", type=Path)
    ap.add_argument("--markdown", action="store_true", help="emit full per-row table")
    args = ap.parse_args()

    prov, rows = load(args.results)
    passed = [r for r in rows if r.get("status") == "PASSED"]
    failed = [r for r in rows if r.get("status") != "PASSED"]
    prod = [r for r in passed if r.get("production", True)]

    print(f"rows: {len(rows)} passed: {len(passed)} failed: {len(failed)} production: {len(prod)}")
    for r in failed:
        print(f"  FAILED: {r.get('id')} -> {r.get('status')} {r.get('message','')[:120]}")

    sp = [r["speedup"] for r in prod]
    gm = geomean(sp)
    am = sum(sp) / len(sp) if sp else float("nan")
    below = [r for r in prod if r["speedup"] < GATE_ROW_FLOOR]
    print(f"headline geomean (production, equal weight): {gm:.4f}")
    print(f"arithmetic mean (secondary): {am:.4f}")
    print(f"gate geomean>1.0: {'PASS' if gm > 1.0 else 'FAIL'}")
    print(f"gate no row <{GATE_ROW_FLOOR}: {'PASS' if not below else f'FAIL ({len(below)} rows)'}")
    for r in sorted(below, key=lambda r: r["speedup"])[:20]:
        print(f"  below-floor: {r['id']} speedup={r['speedup']:.4f} "
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
        print("\n| id | layout | function | baseline med/mean/std/min/p10/p90 (us) | candidate med/mean/std/min/p10/p90 (us) | speedup |")
        print("|---|---|---|---|---|---|")
        for r in sorted(prod, key=lambda r: r["id"]):
            wl = r.get("workload", {})
            shapes = wl.get("shapes", {})
            layout = "NC" if shapes.get("layout") == "channels_last_3d" else "C"
            def fmt(side):
                s = r[side]
                return (f"{s['median_us']:.2f}/{s['mean_us']:.2f}/{s['std_us']:.2f}/"
                        f"{s['min_us']:.2f}/{s['p10_us']:.2f}/{s['p90_us']:.2f}")
            print(f"| {r['id']} | {layout} | {wl.get('function','')} | {fmt('baseline')} | {fmt('candidate')} | {r['speedup']:.4f} |")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
