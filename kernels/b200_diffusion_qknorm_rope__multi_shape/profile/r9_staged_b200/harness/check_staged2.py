#!/usr/bin/env python3
"""Correctness gate for the experimental two-token staged kernel (module-direct).

Runs QKNormRopeStaged2Kernel over all 10 captured production rows against the split
oracle (same seeded inputs, ATOL/RTOL, NaN/Inf checks as the task test suite). The
probe may not be benchmarked until this passes 10/10.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

import torch  # noqa: E402

from tests.test_correctness import ATOL, RTOL, _make_inputs, _run_oracle, make_cases  # noqa: E402


def main() -> int:
    spec = importlib.util.spec_from_file_location("kda_s2_wrapper", ROOT / "src" / "wrapper.py")
    wrapper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(wrapper)

    failures = 0
    for case in make_cases():
        mod = wrapper._candidate_module(
            case["head_dim"], case["rope_dim"], case["is_neox"], torch.bfloat16,
            "QKNormRopeStaged2Kernel",
        )
        inp = _make_inputs(case)
        q, k = inp["q"], inp["k"]
        mod.qknorm_rope(q, k, inp["q_weight"], inp["k_weight"],
                        inp["cos_sin_cache"], inp["positions"], case["eps"])
        eq, ek = _run_oracle(_make_inputs(case), case)
        ok = (
            torch.isfinite(q).all() and torch.isfinite(k).all()
            and torch.allclose(q.float(), eq.float(), atol=ATOL, rtol=RTOL)
            and torch.allclose(k.float(), ek.float(), atol=ATOL, rtol=RTOL)
        )
        failures += 0 if ok else 1
        print(f"{case['name']:>44s}  staged2 oracle_ok={bool(ok)}")
    print(f"STAGED2_CORRECTNESS {'PASS' if failures == 0 else f'FAIL({failures})'}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
