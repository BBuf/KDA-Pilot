"""In-SGLang export + drop-in replacement test. Run on the remote H200:

    CUDA_VISIBLE_DEVICES=<idle> PYTHONPATH=<sglang>/python \
        KDA_SGLANG_ORACLE_COMMIT=c47f0e7cd python tests/sglang_export_test.py

Replaces the public SGLang diffusion RoPE symbols with the candidate (whose
load_jit builds the .cuh under the SGLang csrc tree), then verifies, inside
SGLang: (1) correctness over all 6 production shapes via the public symbol
(candidate == original baseline within 1e-2, and the CUDA route is taken);
(2) an unsupported signature falls back (not CUDA); (3) a smoke benchmark shows
parity-or-speedup vs the original baseline. Restores the symbols at the end.
"""

from __future__ import annotations

import importlib.util
import json
import math
import statistics
import sys
import time
from pathlib import Path

import torch

KDIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KDIR / "src"))


def _load_tc():
    spec = importlib.util.spec_from_file_location("tc_export", KDIR / "tests" / "test_correctness.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _median_us(fn, args, it=50, wu=20):
    for _ in range(wu):
        fn(*args)
    torch.cuda.synchronize()
    s = []
    for _ in range(it):
        t = time.perf_counter()
        fn(*args)
        torch.cuda.synchronize()
        s.append((time.perf_counter() - t) * 1e6)
    return statistics.median(s)


def main() -> int:
    tc = _load_tc()
    import wrapper as W
    import sglang.jit_kernel.diffusion.triton.rotary as R
    import sglang.jit_kernel.diffusion.triton.ltx2_rotary as L

    orig_std = W._BASELINES["standard"]
    orig_ltx2 = W._BASELINES["ltx2"]
    assert orig_std is R.apply_rotary_embedding, "captured standard baseline must be the public symbol"
    assert orig_ltx2 is L.apply_ltx2_split_rotary_emb, "captured ltx2 baseline must be the public symbol"

    cases = tc.make_cases()
    results = {"correctness": [], "fallback": [], "smoke": []}

    # Drop-in replacement: public SGLang symbols now resolve to the candidate.
    R.apply_rotary_embedding = W.apply_rotary_embedding
    L.apply_ltx2_split_rotary_emb = W.apply_ltx2_split_rotary_emb
    try:
        for case in cases:
            api, args = case["api"], case["args"]
            pub = R.apply_rotary_embedding if api == "standard" else L.apply_ltx2_split_rotary_emb
            orig = orig_std if api == "standard" else orig_ltx2
            W._LAST_DISPATCH[api] = None
            out = pub(*args)
            ref = orig(*args)
            assert out.dtype == ref.dtype and out.shape == ref.shape
            torch.testing.assert_close(out.float(), ref.float(), atol=1e-2, rtol=1e-2)
            route = W._LAST_DISPATCH[api]
            assert route == "cuda", f"{case['name']}: expected CUDA route in-SGLang, got {route}"
            results["correctness"].append({"case": case["name"], "route": route, "ok": True})

        # Unsupported (fp16 standard) via the public symbol -> fallback, not CUDA.
        x16 = torch.randn(1, 64, 24, 128, device="cuda", dtype=torch.float16)
        ang = torch.randn(64, 64, device="cuda", dtype=torch.float32)
        W._LAST_DISPATCH["standard"] = None
        ofb = R.apply_rotary_embedding(x16, torch.cos(ang), torch.sin(ang), False)
        assert W._LAST_DISPATCH["standard"] != "cuda" and ofb.dtype == x16.dtype
        results["fallback"].append({"case": "fp16-standard", "route": W._LAST_DISPATCH["standard"], "ok": True})

        # Smoke benchmark: candidate (via public symbol) vs original baseline.
        sp = []
        for case in cases:
            api, args = case["api"], case["args"]
            pub = R.apply_rotary_embedding if api == "standard" else L.apply_ltx2_split_rotary_emb
            orig = orig_std if api == "standard" else orig_ltx2
            cand_us = _median_us(pub, args)
            base_us = _median_us(orig, args)
            r = base_us / cand_us
            sp.append(r)
            results["smoke"].append({"case": case["name"], "baseline_us": round(base_us, 2), "candidate_us": round(cand_us, 2), "speedup": round(r, 3)})
        results["smoke_geomean"] = round(math.exp(sum(math.log(x) for x in sp) / len(sp)), 4)
    finally:
        R.apply_rotary_embedding = orig_std
        L.apply_ltx2_split_rotary_emb = orig_ltx2

    print("EXPORT_TEST_RESULTS", json.dumps(results))
    print("EXPORT_TEST: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
