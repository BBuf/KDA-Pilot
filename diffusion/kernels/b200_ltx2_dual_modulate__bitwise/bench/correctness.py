#!/usr/bin/env python3
"""Production bitwise correctness gate for LTX2 dual modulation.

The oracle is `bench.adapter.call_baseline`, which runs the SGLang LTX2.3
production expression under CUDA bf16 autocast and writes visible fp32 outputs.
Candidate outputs must match those tensors bit-for-bit.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import torch

_TASK_ROOT = Path(__file__).resolve().parents[1]
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))

import bench.adapter as adapter  # noqa: E402

_WORKLOADS = _TASK_ROOT / "bench" / "workloads.json"
_EXPECTED_DTYPE = torch.float32


def _poison(outputs: list[torch.Tensor]) -> None:
    for out in outputs:
        out.fill_(float("nan"))


def _row_status(row: dict, device: torch.device, index: int) -> tuple[bool, str]:
    case = adapter.make_case(row, device=device, seed=91000 + index)
    adapter.call_baseline(row, case["inputs"], case["baseline_outputs"])
    _poison(case["candidate_outputs"])
    adapter.call_candidate(row, case["inputs"], case["candidate_outputs"])
    torch.cuda.synchronize()

    for name, outputs in (
        ("baseline", case["baseline_outputs"]),
        ("candidate", case["candidate_outputs"]),
    ):
        for i, out in enumerate(outputs):
            if out.dtype != _EXPECTED_DTYPE:
                return False, f"{name}[{i}] dtype {out.dtype} != {_EXPECTED_DTYPE}"
            if torch.isnan(out).any() or torch.isinf(out).any():
                return False, f"{name}[{i}] contains NaN/Inf"

    verdict = adapter.compare_outputs(
        row,
        case["baseline_outputs"],
        case["candidate_outputs"],
        case["tolerance"],
    )
    return bool(verdict.get("ok")), str(verdict.get("message", ""))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true", help="run only the first workload")
    args = parser.parse_args()

    if not torch.cuda.is_available():
        print("FAIL: CUDA is required for the production autocast gate")
        return 1

    rows = json.loads(_WORKLOADS.read_text())
    if args.quick:
        rows = rows[:1]

    failures: list[str] = []
    device = torch.device("cuda")
    for i, row in enumerate(rows):
        try:
            ok, msg = _row_status(row, device, i)
        except Exception as exc:  # noqa: BLE001
            ok, msg = False, f"{type(exc).__name__}: {exc}"
        label = row.get("id", f"row_{i}")
        print(("PASS" if ok else "FAIL"), label, msg)
        if not ok:
            failures.append(f"{label}: {msg}")

    if failures:
        print("\n".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
