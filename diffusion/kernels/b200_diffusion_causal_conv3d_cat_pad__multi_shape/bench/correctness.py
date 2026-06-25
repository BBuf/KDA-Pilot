"""Correctness harness for b200_diffusion_causal_conv3d_cat_pad__multi_shape.

Checks the candidate against (a) an independent torch oracle and (b) the copied
SGLang Triton baseline, bitwise-exactly (atol=0, rtol=0; NaN/Inf preserved via an
integer-view comparison), across the production grid plus targeted regression,
edge, and rejection rows. Output buffers are poisoned before each run so an
unwritten cell (skipped launch / missed border) is caught. No sglang import at
runtime.

Run on a CUDA device:  python bench/correctness.py
"""

from __future__ import annotations

import sys
from pathlib import Path

_TASK_ROOT = Path(__file__).resolve().parents[1]
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))

import torch
import torch.nn.functional as F

import baseline.binding as _baseline
from solution.build import load_candidate_module

assert not any(
    n == "sglang" or n.startswith("sglang.") for n in sys.modules
), "standalone contract violation: sglang imported at correctness runtime"

_CAND = load_candidate_module().causal_conv3d_cat_pad_candidate
_BASE = _baseline.fused_causal_conv3d_cat_pad


def oracle(x: torch.Tensor, cache: torch.Tensor, padding) -> torch.Tensor:
    """Independent reference: cat on depth, then constant-zero F.pad with the
    cache-consumed left-depth padding (eff_d_l = depth_left - cache_t)."""
    w_l, w_r, h_t, h_b, d_l, d_r = padding
    cache_t = cache.shape[2]
    eff_d_l = d_l - cache_t
    assert eff_d_l >= 0, "depth_left must be >= cache_t"
    cat = torch.cat([cache, x], dim=2) if cache_t > 0 else x
    # F.pad pads trailing dims first: (W_l, W_r, H_t, H_b, D_l_eff, D_r) for 5D.
    return F.pad(cat, [w_l, w_r, h_t, h_b, eff_d_l, d_r], mode="constant", value=0)


def _int_view(t: torch.Tensor) -> torch.Tensor:
    assert t.is_contiguous()
    return t.view(torch.int16 if t.element_size() == 2 else torch.int32)


def _exact_equal(a: torch.Tensor, b: torch.Tensor) -> bool:
    if tuple(a.shape) != tuple(b.shape) or a.dtype != b.dtype:
        return False
    return bool(torch.equal(_int_view(a), _int_view(b)))


def _poison(t: torch.Tensor) -> None:
    t.view(torch.int16 if t.element_size() == 2 else torch.int32).fill_(0x4242)


def _out_shape(x_shape, cache_t, padding):
    w_l, w_r, h_t, h_b, d_l, d_r = padding
    n, c, t, h, w = x_shape
    return (n, c, t + (d_l - cache_t) + cache_t + d_r, h + h_t + h_b, w + w_l + w_r)


def _make_inputs(x_shape, cache_shape, device, *, inject_naninf=False, seed=0):
    g = torch.Generator(device="cpu").manual_seed(seed)
    x = torch.randn(x_shape, generator=g, dtype=torch.float32).to(device=device, dtype=torch.bfloat16)
    if cache_shape[2] > 0:
        cache = torch.randn(cache_shape, generator=g, dtype=torch.float32).to(device=device, dtype=torch.bfloat16)
    else:
        cache = torch.empty(cache_shape, device=device, dtype=torch.bfloat16)
    if inject_naninf:
        x.view(-1)[0] = float("nan")
        x.view(-1)[1] = float("inf")
        if cache.numel() > 0:
            cache.view(-1)[0] = float("-inf")
    return x, cache


def run_case(cid, x_shape, cache_shape, padding, device, *, inject_naninf=False, seed=0):
    errs = []
    x, cache = _make_inputs(x_shape, cache_shape, device, inject_naninf=inject_naninf, seed=seed)
    out_shape = _out_shape(x_shape, cache_shape[2], padding)

    out_base = torch.empty(out_shape, device=device, dtype=torch.bfloat16)
    out_cand = torch.empty(out_shape, device=device, dtype=torch.bfloat16)
    _poison(out_base)
    _poison(out_cand)

    _BASE(x, cache, list(padding), out_base)
    _CAND(x, cache, padding[0], padding[1], padding[2], padding[3], padding[4], padding[5], out_cand)
    out_oracle = oracle(x, cache, padding)

    if tuple(out_cand.shape) != tuple(out_shape):
        errs.append(f"{cid}: candidate shape {tuple(out_cand.shape)} != {out_shape}")
    if not _exact_equal(out_cand, out_oracle):
        errs.append(f"{cid}: candidate != torch oracle (bitwise)")
    if not _exact_equal(out_base, out_oracle):
        errs.append(f"{cid}: baseline != torch oracle (bitwise)")
    if not _exact_equal(out_cand, out_base):
        errs.append(f"{cid}: candidate != baseline (bitwise)")
    if not inject_naninf and (torch.isnan(out_cand.float()).any() or torch.isinf(out_cand.float()).any()):
        errs.append(f"{cid}: candidate introduced NaN/Inf on clean inputs")
    return errs


def run_poison_selftest(device):
    """A deliberately skipped launch must be detected (proves poison works)."""
    x_shape, cache_shape, padding = (1, 4, 1, 3, 5), (1, 4, 1, 3, 5), (1, 1, 1, 1, 2, 0)
    x, cache = _make_inputs(x_shape, cache_shape, device, seed=99)
    out_shape = _out_shape(x_shape, cache_shape[2], padding)
    out = torch.empty(out_shape, device=device, dtype=torch.bfloat16)
    _poison(out)  # do NOT run the candidate
    oracle_out = oracle(x, cache, padding)
    if _exact_equal(out, oracle_out):
        return ["poison self-test FAILED: skipped launch was not detected"]
    return []


def run_rejection_tests(device):
    errs = []
    dummy = torch.empty((1, 1, 1, 1, 1), device=device, dtype=torch.bfloat16)

    def expect_raise(tag, fn):
        try:
            fn()
        except Exception:
            return
        errs.append(f"rejection[{tag}]: expected an exception but none was raised")

    x = torch.randn((1, 4, 1, 3, 5), device=device, dtype=torch.bfloat16)
    cache2 = torch.randn((1, 4, 2, 3, 5), device=device, dtype=torch.bfloat16)
    cache1 = torch.randn((1, 4, 1, 3, 5), device=device, dtype=torch.bfloat16)

    # depth_left < cache_t  (d_l=1 < cache_t=2)
    expect_raise("d_l<cache_t", lambda: _CAND(x, cache2, 1, 1, 1, 1, 1, 0, dummy))
    # depth_right != 0
    expect_raise("d_r!=0", lambda: _CAND(x, cache1, 1, 1, 1, 1, 2, 1, dummy))
    # asymmetric width
    expect_raise("asym_w", lambda: _CAND(x, cache1, 1, 2, 1, 1, 2, 0, dummy))
    # asymmetric height
    expect_raise("asym_h", lambda: _CAND(x, cache1, 1, 1, 1, 2, 2, 0, dummy))
    # dtype mismatch (output fp32)
    out_f32 = torch.empty((1, 4, 3, 5, 7), device=device, dtype=torch.float32)
    expect_raise("dtype", lambda: _CAND(x, cache1, 1, 1, 1, 1, 2, 0, out_f32))
    # cache N/C/H/W mismatch (wrong H)
    bad_cache = torch.randn((1, 4, 1, 4, 5), device=device, dtype=torch.bfloat16)
    expect_raise("cache_hw", lambda: _CAND(x, bad_cache, 1, 1, 1, 1, 2, 0, dummy))
    # non-contiguous x (transpose H/W) must be rejected
    x_nc = torch.randn((1, 4, 1, 5, 3), device=device, dtype=torch.bfloat16).transpose(3, 4)
    out_ok = torch.empty(_out_shape((1, 4, 1, 3, 5), 1, (1, 1, 1, 1, 2, 0)), device=device, dtype=torch.bfloat16)
    expect_raise("noncontig_x", lambda: _CAND(x_nc, cache1, 1, 1, 1, 1, 2, 0, out_ok))
    return errs


def main():
    if not torch.cuda.is_available():
        print("FAIL: CUDA device required for correctness checks")
        return 1
    device = torch.device("cuda")

    # production grid (mirrors bench/workloads.json) + regression/edge rows
    pad = (1, 1, 1, 1, 2, 0)
    cases = [
        ("prod_c1024_t1_h30_w52__cache1", (1, 1024, 1, 30, 52), (1, 1024, 1, 30, 52), pad),
        ("prod_c1024_t1_h30_w52__cache2", (1, 1024, 1, 30, 52), (1, 1024, 2, 30, 52), pad),
        ("prod_c1024_t2_h60_w104__cache1", (1, 1024, 2, 60, 104), (1, 1024, 1, 60, 104), pad),
        ("prod_c1024_t2_h60_w104__cache2", (1, 1024, 2, 60, 104), (1, 1024, 2, 60, 104), pad),
        ("prod_c512_t4_h120_w208__cache1", (1, 512, 4, 120, 208), (1, 512, 1, 120, 208), pad),
        ("prod_c512_t4_h120_w208__cache2", (1, 512, 4, 120, 208), (1, 512, 2, 120, 208), pad),
        ("prod_c256_t4_h240_w416__cache1", (1, 256, 4, 240, 416), (1, 256, 1, 240, 416), pad),
        ("prod_c256_t4_h240_w416__cache2", (1, 256, 4, 240, 416), (1, 256, 2, 240, 416), pad),
        # regression / edge rows
        ("reg_cache_null", (1, 8, 2, 7, 9), (1, 8, 0, 7, 9), (1, 1, 1, 1, 2, 0)),
        ("reg_no_pad_cat_only", (1, 8, 2, 7, 9), (1, 8, 1, 7, 9), (0, 0, 0, 0, 1, 0)),
        ("edge_distinct_axis_pad", (1, 4, 1, 5, 7), (1, 4, 1, 5, 7), (2, 2, 1, 1, 2, 0)),
        ("edge_small_cache2", (1, 3, 1, 2, 3), (1, 3, 2, 2, 3), (1, 1, 1, 1, 2, 0)),
    ]

    all_errs = []
    for i, (cid, xs, cs, pd) in enumerate(cases):
        all_errs += run_case(cid, xs, cs, pd, device, seed=1000 + i)
    # NaN/Inf preservation on a small shape
    all_errs += run_case("naninf_preserve", (1, 4, 1, 3, 5), (1, 4, 1, 3, 5), pad,
                         device, inject_naninf=True, seed=7)
    all_errs += run_poison_selftest(device)
    all_errs += run_rejection_tests(device)

    if all_errs:
        print(f"CORRECTNESS FAIL ({len(all_errs)} error(s)):")
        for e in all_errs:
            print("  -", e)
        return 1
    print(f"CORRECTNESS PASS: {len(cases) + 1} value cases + poison self-test + rejection tests")
    return 0


if __name__ == "__main__":
    sys.exit(main())
