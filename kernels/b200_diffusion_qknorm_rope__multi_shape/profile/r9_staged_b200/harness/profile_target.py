#!/usr/bin/env python3
"""NCU harness: one device kernel per launch on an exact captured production row.

Usage (inside sglang_bbuf, idle GPU pinned, KDA_LINEINFO=1 for SASS->source mapping):
  python profile_target.py staged   [shape_name]   # candidate CTA-per-token staged kernel
  python profile_target.py baseline [shape_name]   # hermetic baseline/ copy (warp kernel)

Defaults to qwen-edit__large__B8424_H24_D128_R128 (the heaviest captured row). The script
does 10 un-profiled warmup launches, then 3 launches for NCU to capture — pair with
``ncu --launch-skip 10 --launch-count 3``. Inputs come from the task correctness module so
the profiled shape is byte-identical to the benchmark/correctness workload.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # harness/ -> r9_staged_b200/ -> profile/ -> kernel folder
sys.path.insert(0, str(ROOT))

import torch  # noqa: E402

from tests.test_correctness import _make_inputs, make_cases  # noqa: E402


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    which = sys.argv[1] if len(sys.argv) > 1 else "staged"
    shape = sys.argv[2] if len(sys.argv) > 2 else "qwen-edit__large__B8424_H24_D128_R128"
    case = {c["name"]: c for c in make_cases()}[shape]
    inp = _make_inputs(case)

    if which == "staged":
        wrapper = _load(ROOT / "src" / "wrapper.py", "kda_profile_wrapper")
        mod = wrapper._candidate_module(
            case["head_dim"], case["rope_dim"], case["is_neox"], torch.bfloat16,
            "QKNormRopeStagedKernel",
        )
    elif which == "baseline":
        loader = _load(ROOT / "baseline" / "loader.py", "kda_profile_baseline")
        mod = loader.baseline_module(
            case["head_dim"], case["rope_dim"], case["is_neox"], torch.bfloat16,
        )
    else:
        raise SystemExit(f"unknown target {which!r}; use staged|baseline")

    def call() -> None:
        mod.qknorm_rope(inp["q"], inp["k"], inp["q_weight"], inp["k_weight"],
                        inp["cos_sin_cache"], inp["positions"], case["eps"])

    for _ in range(10):  # warmup; excluded via ncu --launch-skip 10
        call()
    torch.cuda.synchronize()
    for _ in range(3):  # profiled launches (ncu --launch-count 3)
        call()
    torch.cuda.synchronize()
    print(f"done {which} {shape}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
