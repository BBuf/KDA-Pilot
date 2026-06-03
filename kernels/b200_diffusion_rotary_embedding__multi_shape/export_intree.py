#!/usr/bin/env python3
"""In-tree SGLang csrc export + drop-in test (AC-9).

Run with PYTHONPATH pointing at a TASK-OWNED SGLang worktree where
`python/sglang/jit_kernel/csrc/diffusion/rotary_embedding.cuh` has been placed,
so `import sglang` resolves there and the `cache_once` loaders build via the
RELATIVE csrc path (`cuda_files=["diffusion/rotary_embedding.cuh"]`) — the
official packaged form. Then the two public symbols are swapped to candidate
callables, and the in-SGLang oracle (11 sigs) + smoke benchmark + non-captured
fallback are exercised. No shared production checkout is mutated.
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
    import sglang
    from sglang.jit_kernel.utils import KERNEL_PATH, cache_once, load_jit, make_cpp_args
    import sglang.jit_kernel.diffusion.triton.rotary as rmod
    import sglang.jit_kernel.diffusion.triton.ltx2_rotary as lmod

    corr = _load("corr", "tests/test_correctness.py")
    wrap = _load("wrap", os.path.join("src", "wrapper.py"))  # tight gate functions

    USE_PDL = False

    # cache_once loaders that build via the RELATIVE csrc path (official in-tree form).
    @cache_once
    def _std_module(head_dim, dtype):
        a = make_cpp_args(head_dim, USE_PDL, dtype)
        return load_jit(
            "kda_intree_std", *a,
            cuda_files=["diffusion/rotary_embedding.cuh"],
            cuda_wrappers=[("apply_rotary", f"kda_diffusion_rotary::StandardRotaryKernel<{a}>::run")],
        )

    @cache_once
    def _ltx2_module(half, dtype):
        a = make_cpp_args(half, USE_PDL, dtype)
        return load_jit(
            "kda_intree_ltx2", *a,
            cuda_files=["diffusion/rotary_embedding.cuh"],
            cuda_wrappers=[("apply_ltx2", f"kda_diffusion_rotary::Ltx2SplitRotaryKernel<{a}>::run")],
        )

    orig_rotary = rmod.apply_rotary_embedding
    orig_ltx2 = lmod.apply_ltx2_split_rotary_emb

    def cand_rotary(x, cos, sin, interleaved=False):
        if wrap._is_standard_fast(x, cos, sin, interleaved):
            h, d = x.shape[-2], x.shape[-1]
            out = torch.empty_like(x)
            _std_module(d, x.dtype).apply_rotary(out.reshape(-1, h, d), x.reshape(-1, h, d), cos, sin)
            return out
        return orig_rotary(x, cos, sin, interleaved)

    def cand_ltx2(x, cos, sin):
        if wrap._is_ltx2_fast(x, cos, sin):
            out = torch.empty_like(x)
            _ltx2_module(cos.shape[-1], x.dtype).apply_ltx2(out, x, cos, sin)
            return out
        return orig_ltx2(x, cos, sin)

    csrc_path = os.path.join(str(KERNEL_PATH), "csrc", "diffusion", "rotary_embedding.cuh")
    res = {
        "sglang_from": sglang.__file__,
        "kernel_path": str(KERNEL_PATH),
        "csrc_file_present": os.path.exists(csrc_path),
        "loader": "cache_once + load_jit(cuda_files=['diffusion/rotary_embedding.cuh'])",
    }

    cases = corr.make_cases()
    oracle_ref = {
        c["name"]: (orig_rotary(*c["args"]) if c["kind"] == "standard" else orig_ltx2(*c["args"]))
        for c in cases
    }

    # ---- install: swap the public symbols in the (worktree) sglang ----
    rmod.apply_rotary_embedding = cand_rotary
    lmod.apply_ltx2_split_rotary_emb = cand_ltx2
    try:
        md = 0.0
        for c in cases:
            fn = rmod.apply_rotary_embedding if c["kind"] == "standard" else lmod.apply_ltx2_split_rotary_emb
            got = fn(*c["args"])
            md = max(md, (got.float() - oracle_ref[c["name"]].float()).abs().max().item())
        res["in_sglang_oracle"] = {"shapes": len(cases), "max_abs_diff": md, "bit_exact": md == 0.0}

        smoke = []
        for nm in [
            "hunyuanvideo__standard__1x27030x24x128",
            "ltx23_two__1x24576x4096__half64",
            "ltx23_two__1x24576x2048__half32",
        ]:
            c = next(x for x in cases if x["name"] == nm)
            base = orig_rotary if c["kind"] == "standard" else orig_ltx2
            cand = rmod.apply_rotary_embedding if c["kind"] == "standard" else lmod.apply_ltx2_split_rotary_emb
            bt = _median_us(base, c["args"])
            ct = _median_us(cand, c["args"])
            smoke.append({"shape": nm, "baseline_us": round(bt, 2), "candidate_us": round(ct, 2), "speedup": round(bt / ct, 3)})
        res["in_sglang_smoke"] = smoke

        g = torch.Generator(device="cuda").manual_seed(7)
        xf = torch.randn(1, 64, 8, 128, generator=g, device="cuda", dtype=torch.float32).half()
        cf = torch.randn(64, 64, generator=g, device="cuda", dtype=torch.float32)
        sf = torch.randn(64, 64, generator=g, device="cuda", dtype=torch.float32)
        exp = orig_rotary(xf, cf, sf, False)
        got = rmod.apply_rotary_embedding(xf, cf, sf, False)
        res["in_sglang_fallback"] = {"max_abs_diff": (got.float() - exp.float()).abs().max().item()}
    finally:
        rmod.apply_rotary_embedding = orig_rotary
        lmod.apply_ltx2_split_rotary_emb = orig_ltx2

    res["restored"] = (
        rmod.apply_rotary_embedding is orig_rotary and lmod.apply_ltx2_split_rotary_emb is orig_ltx2
    )
    print(json.dumps(res, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
