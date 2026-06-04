#!/usr/bin/env python3
"""Fold LTX upsampler capture rows into bench/workloads.json as diagnostics.

Per the preset-audit decision (DEC-5): the fresh reduced-step LTX two-stage
captures contribute `production=false` diagnostic workloads (wrapper entry, so
bench/correctness.py's wrapper suite covers them automatically) while the
production headline stays the 48 retained HunyuanVideo signatures. Idempotent:
existing diagnostic ids are updated in place, never duplicated; production
rows are never touched.

Usage:
    python3 bench/add_ltx_diagnostics.py --captures cap_a.jsonl cap_b.jsonl \
        --workloads bench/workloads.json
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

BF16_TOL = {"atol": 7e-2, "rtol": 2e-2}
FP16_TOL = {"atol": 3e-3, "rtol": 3e-3}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--captures", nargs="+", required=True)
    parser.add_argument("--workloads", required=True)
    args = parser.parse_args()

    sigs: dict[tuple, dict] = {}
    for path in args.captures:
        for line in open(path, encoding="utf-8"):
            row = json.loads(line)
            x = row["args"][0]
            if not isinstance(x, dict):
                continue
            kwargs = row.get("kwargs") or {}
            eps = float(kwargs.get("eps", 1e-5))
            num_groups = int(kwargs.get("num_groups", 32))
            key = (tuple(x["shape"]), x["dtype"], num_groups, eps)
            entry = sigs.setdefault(
                key,
                {
                    "presets": set(),
                    "rows": 0,
                    "contiguous": bool(x["contiguous"]),
                    "entries": set(),
                },
            )
            entry["presets"].add(row.get("model", "unknown"))
            entry["rows"] += 1
            entry["entries"].add(row["kernel"].split(".")[-1])

    workloads = json.load(open(args.workloads, encoding="utf-8"))
    by_id = {w["id"]: w for w in workloads}
    added, updated = 0, 0
    for (shape, dtype_str, num_groups, eps), info in sorted(sigs.items()):
        dtype = dtype_str.replace("torch.", "")
        tag = "x".join(str(d) for d in shape)
        wid = f"diag__apply__ltx__{tag}__{'bf16' if dtype == 'bfloat16' else dtype}__g{num_groups}"
        tol = BF16_TOL if dtype == "bfloat16" else FP16_TOL
        row = {
            "id": wid,
            "function": "apply_group_norm_silu",
            "production": False,
            "shapes": {"x": list(shape)},
            "dtype": dtype,
            "num_groups": num_groups,
            "eps": eps,
            "contiguous": info["contiguous"],
            "atol": tol["atol"],
            "rtol": tol["rtol"],
            "capture": {
                "source": "fresh reduced-step LTX two-stage captures (preset audit)",
                "presets": sorted(info["presets"]),
                "capture_rows": info["rows"],
                "entries_observed": sorted(info["entries"]),
            },
        }
        if wid in by_id:
            by_id[wid].update(row)
            updated += 1
        else:
            workloads.append(row)
            added += 1

    with open(args.workloads, "w", encoding="utf-8") as fh:
        json.dump(workloads, fh, indent=1)
        fh.write("\n")
    prod = sum(1 for w in workloads if w.get("production"))
    print(
        f"workloads: {len(workloads)} total ({prod} production); "
        f"ltx diagnostics added={added} updated={updated}"
    )
    for key, info in sorted(sigs.items()):
        print(f"  {key} presets={sorted(info['presets'])} rows={info['rows']}")


if __name__ == "__main__":
    main()
