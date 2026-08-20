#!/usr/bin/env python3
"""Check each definition's shipped reference against the SGLang kernel it describes.

The reference is what an agent reads to learn what the kernel is *supposed* to compute,
so a reference that disagrees with the kernel is worse than no reference at all. This
runs both on every workload row, with the tolerance the task declares, and prints the
worst relative error per row.

    BENCH_REPO_ROOT=<run tree> PYTHONPATH=<run tree>/benchmarks \
        python verify_reference.py [definition ...]
"""

from __future__ import annotations

import importlib
import json
import os
import sys
import types
from pathlib import Path

import torch

TRACE = Path(os.environ.get("BENCH_TRACE_ROOT",
                            Path(os.environ["BENCH_REPO_ROOT"]) / "flashinfer_trace"))

TASKS = {
    "glm47_mla_decode_grouped_h20_ckv512_kpe64": {
        "group": "attention",
        "bench": "bench_glm47_mla_decode_standalone",
        "rtol": 1e-2,
        "atol": 1e-3,
    },
    "qwen3next_gdn_packed_decode_hv4_d128": {
        "group": "gdn",
        "bench": "bench_qwen3next_gdn_decode_standalone",
        "rtol": 2e-2,
        "atol": 2e-2,
    },
}


def load_reference(definition: str, group: str):
    source = json.loads(
        (TRACE / "definitions" / group / (definition + ".json")).read_text()
    )["reference"]
    module = types.ModuleType("reference_" + definition)
    exec(compile(source, definition + "/reference.py", "exec"), module.__dict__)
    return module.run


def load_baseline(definition: str, group: str):
    from bench_common import load_solution_json

    found = sorted((TRACE / "solutions/baseline" / group / definition).glob("*.json"))
    assert len(found) == 1, found
    return load_solution_json(found[0], "baseline_" + definition)


def main() -> int:
    wanted = sys.argv[1:] or list(TASKS)
    failures = 0
    for definition in wanted:
        meta = TASKS[definition]
        bench = importlib.import_module(meta["bench"])
        reference = load_reference(definition, meta["group"])
        baseline = load_baseline(definition, meta["group"])
        rows = bench.make_workloads()
        print("##### %s (%d rows, rtol=%g atol=%g)"
              % (definition, len(rows), meta["rtol"], meta["atol"]))
        for entry in rows:
            device = torch.device("cuda")
            got = baseline(*bench.make_inputs(entry, device))
            want = reference(*bench.make_inputs(entry, device))
            got = got if isinstance(got, tuple) else (got,)
            want = want if isinstance(want, tuple) else (want,)
            worst, verdict = 0.0, "PASS"
            for index, (left, right) in enumerate(zip(got, want, strict=True)):
                left, right = left.float(), right.float()
                if left.shape != right.shape:
                    verdict = "SHAPE %s vs %s" % (list(left.shape), list(right.shape))
                    break
                worst = max(worst, float(
                    ((left - right).abs() / (right.abs() + meta["atol"])).max()))
                try:
                    torch.testing.assert_close(
                        left, right, rtol=meta["rtol"], atol=meta["atol"])
                except AssertionError as exc:
                    verdict = "output %d: %s" % (index, str(exc).splitlines()[1][:66])
            if verdict != "PASS":
                failures += 1
            print("   %-9s %-40s worst-rel=%.3g  %s"
                  % (entry["suite"], entry["id"], worst, verdict))
    print("\n%s" % ("the reference matches the kernel on every row"
                    if not failures else "%d rows disagree" % failures))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
