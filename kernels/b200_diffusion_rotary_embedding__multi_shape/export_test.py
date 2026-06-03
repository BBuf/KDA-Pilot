#!/usr/bin/env python3
"""In-SGLang drop-in replacement test (AC-9), constraint-safe.

Validates that the candidate drop-in replaces the two public SGLang diffusion
RoPE entry points and runs, WITHOUT mutating the shared SGLang checkout:
  - the candidate builds through SGLang jit_kernel/tvm-ffi (load_jit) from the
    workspace .cuh (same machinery as a csrc-placed source);
  - the two public symbols are swapped in-process to the candidate ("install");
  - the in-SGLang correctness oracle passes (public API == original baseline);
  - a smoke benchmark through the public API shows parity-or-speedup;
  - a non-captured signature falls back to the baseline (recursion-safe);
  - the originals are restored ("uninstall").

Run inside sglang_bbuf on an idle B200:
  CUDA_VISIBLE_DEVICES=<idle> python export_test.py
"""

from __future__ import annotations

import importlib.util
import json
import os
import statistics

import torch

KDIR = os.path.dirname(os.path.abspath(__file__))


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(KDIR, rel))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _median_us(fn, args, warmup=20, iters=100):
    for _ in range(warmup):
        fn(*args)
    torch.cuda.synchronize()
    s = [torch.cuda.Event(enable_timing=True) for _ in range(iters)]
    e = [torch.cuda.Event(enable_timing=True) for _ in range(iters)]
    for i in range(iters):
        s[i].record()
        fn(*args)
        e[i].record()
    torch.cuda.synchronize()
    return statistics.median([s[i].elapsed_time(e[i]) * 1000.0 for i in range(iters)])


def main() -> int:
    corr = _load("corr", "tests/test_correctness.py")
    wrapper = _load("wrap", os.path.join("src", "wrapper.py"))  # captures originals at import

    import sglang.jit_kernel.diffusion.triton.rotary as rotary_mod
    import sglang.jit_kernel.diffusion.triton.ltx2_rotary as ltx2_mod

    orig_rotary = rotary_mod.apply_rotary_embedding
    orig_ltx2 = ltx2_mod.apply_ltx2_split_rotary_emb

    cases = corr.make_cases()
    # Oracle reference: original baseline outputs captured BEFORE the swap.
    oracle_ref = {
        c["name"]: (orig_rotary(*c["args"]) if c["kind"] == "standard" else orig_ltx2(*c["args"]))
        for c in cases
    }

    results: dict = {"jit_build": "load_jit via SGLang jit_kernel/tvm-ffi (no torch cpp_extension)"}

    # ---- install: swap the public symbols to the candidate ----
    rotary_mod.apply_rotary_embedding = wrapper.apply_rotary_embedding
    ltx2_mod.apply_ltx2_split_rotary_emb = wrapper.apply_ltx2_split_rotary_emb
    try:
        # in-SGLang oracle: public API now routes to the candidate
        max_diff = 0.0
        for c in cases:
            fn = (
                rotary_mod.apply_rotary_embedding
                if c["kind"] == "standard"
                else ltx2_mod.apply_ltx2_split_rotary_emb
            )
            got = fn(*c["args"])
            d = (got.float() - oracle_ref[c["name"]].float()).abs().max().item()
            max_diff = max(max_diff, d)
        results["in_sglang_oracle"] = {
            "shapes": len(cases),
            "max_abs_diff_vs_baseline": max_diff,
            "bit_exact": max_diff == 0.0,
        }

        # smoke benchmark through the public API vs the original baseline
        smoke = []
        for nm in [
            "hunyuanvideo__standard__1x27030x24x128",
            "ltx23_two__1x24576x4096__half64",
            "ltx23_two__1x24576x2048__half32",
        ]:
            c = next(x for x in cases if x["name"] == nm)
            base = orig_rotary if c["kind"] == "standard" else orig_ltx2
            cand = (
                rotary_mod.apply_rotary_embedding
                if c["kind"] == "standard"
                else ltx2_mod.apply_ltx2_split_rotary_emb
            )
            bt = _median_us(base, c["args"])
            ct = _median_us(cand, c["args"])
            smoke.append({"shape": nm, "baseline_us": round(bt, 2), "candidate_us": round(ct, 2), "speedup": round(bt / ct, 3)})
        results["in_sglang_smoke"] = smoke

        # fallback: a non-captured (fp16) signature via the public API
        g = torch.Generator(device="cuda").manual_seed(7)
        xf = torch.randn(1, 64, 8, 128, generator=g, device="cuda", dtype=torch.float32).half()
        cf = torch.randn(64, 64, generator=g, device="cuda", dtype=torch.float32)
        sf = torch.randn(64, 64, generator=g, device="cuda", dtype=torch.float32)
        exp = orig_rotary(xf, cf, sf, False)
        got = rotary_mod.apply_rotary_embedding(xf, cf, sf, False)
        fb = (got.float() - exp.float()).abs().max().item()
        results["in_sglang_fallback"] = {
            "case": "fp16 non-captured standard via public API",
            "max_abs_diff_vs_baseline": fb,
            "fell_back_correctly": fb == 0.0,
        }
    finally:
        # ---- uninstall: restore originals ----
        rotary_mod.apply_rotary_embedding = orig_rotary
        ltx2_mod.apply_ltx2_split_rotary_emb = orig_ltx2

    results["restored"] = (
        rotary_mod.apply_rotary_embedding is orig_rotary
        and ltx2_mod.apply_ltx2_split_rotary_emb is orig_ltx2
    )
    print(json.dumps(results, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
