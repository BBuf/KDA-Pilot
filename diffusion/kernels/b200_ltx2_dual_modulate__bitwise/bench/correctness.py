"""Bitwise correctness gate for b200_ltx2_dual_modulate__bitwise.

The candidate must be BIT-FOR-BIT equal (`torch.equal`, atol=rtol=0) to the
PyTorch eager baseline for both operations across the production rows, the
canonical regression grid (diffusion_correctness_contract.md, Scale-Shift), the
fp32 `scale_shift_table` path, `temb_seq in {1, S}`, and all explicit param
layouts. Output buffers are NaN-poisoned before each run so a skipped/zero kernel
is caught. Unsupported inputs must be rejected (raise) on both sides.

Run on a B200:  python bench/correctness.py
Exit code 0 iff every check passes.
"""

from __future__ import annotations

import sys
from pathlib import Path

_TASK_ROOT = Path(__file__).resolve().parents[1]
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))

import torch
import torch.nn.functional as F

import baseline.binding as B
from solution.build import load_candidate_module

_cand = load_candidate_module()
_DEV = "cuda"
_EPS = 1e-6

_n_pass = 0
_n_fail = 0
_failures: list[str] = []


def _poison(outs):
    for t in outs:
        t.fill_(float("nan"))


def _rms(x, eps=_EPS):
    return F.rms_norm(x, normalized_shape=(x.shape[-1],), eps=eps)


def _check(tag: str, cond: bool, detail: str = "") -> None:
    global _n_pass, _n_fail
    if cond:
        _n_pass += 1
    else:
        _n_fail += 1
        _failures.append(f"{tag}: {detail}")
        print(f"  FAIL {tag}: {detail}")


def _explicit_params(B_, S, D, layout, device):
    """Build (scale0, shift0, scale1, shift1) for the requested broadcast layout."""
    if layout == "BD":
        shape = (B_, D)
    elif layout == "B1D":
        shape = (B_, 1, D)
    elif layout == "BSD":
        shape = (B_, S, D)
    else:
        raise ValueError(layout)
    return [torch.randn(shape, device=device, dtype=torch.bfloat16) for _ in range(4)]


def case_explicit(B_, S, D, layout, tag):
    x = torch.randn(B_, S, D, device=_DEV, dtype=torch.bfloat16)
    scale0, shift0, scale1, shift1 = _explicit_params(B_, S, D, layout, _DEV)
    y0_b, y1_b = torch.empty_like(x), torch.empty_like(x)
    y0_c, y1_c = torch.empty_like(x), torch.empty_like(x)
    B.ltx2_dual_modulate_baseline(x, scale0, shift0, scale1, shift1, _EPS, y0_b, y1_b)
    _poison([y0_c, y1_c])
    normed = _rms(x)
    _cand.ltx2_dual_modulate_candidate(normed, scale0, shift0, scale1, shift1, y0_c, y1_c)
    _check(f"explicit/{tag}/y0", torch.equal(y0_b, y0_c), "not bitwise equal")
    _check(f"explicit/{tag}/y1", torch.equal(y1_b, y1_c), "not bitwise equal")


def case_ca(B_, S, D, table_dtype, temb_seq, tag):
    x = torch.randn(B_, S, D, device=_DEV, dtype=torch.bfloat16)
    temb = torch.randn(B_, temb_seq, 4 * D, device=_DEV, dtype=torch.bfloat16)
    table = torch.randn(4, D, device=_DEV, dtype=table_dtype)
    y0_b, y1_b = torch.empty_like(x), torch.empty_like(x)
    y0_c, y1_c = torch.empty_like(x), torch.empty_like(x)
    B.ltx2_ca_dual_modulate_from_temb_baseline(x, temb, table, _EPS, y0_b, y1_b)
    _poison([y0_c, y1_c])
    normed = _rms(x)
    _cand.ltx2_ca_dual_modulate_from_temb_candidate(normed, temb, table, y0_c, y1_c)
    _check(f"ca/{tag}/y0", torch.equal(y0_b, y0_c), "not bitwise equal")
    _check(f"ca/{tag}/y1", torch.equal(y1_b, y1_c), "not bitwise equal")


def expect_raises(tag, thunk):
    try:
        thunk()
    except Exception:
        _check(f"reject/{tag}", True)
        return
    _check(f"reject/{tag}", False, "expected an exception, none raised")


def main():
    torch.manual_seed(0)
    torch.backends.cuda.matmul.allow_tf32 = False
    if not torch.cuda.is_available():
        print("CUDA not available; this gate must run on a B200.")
        return 2

    # Production rows (D in {2048, 4096}; B in {1,2}; S in {126,1536,6144}).
    print("[production rows]")
    for B_, S, D in [(2, 1536, 4096), (2, 126, 2048), (1, 6144, 4096), (1, 126, 2048)]:
        case_explicit(B_, S, D, "B1D", f"prod_{B_}x{S}x{D}")
        case_ca(B_, S, D, torch.bfloat16, 1, f"prod_{B_}x{S}x{D}")

    # Canonical regression grid (Scale-Shift section), bf16.
    print("[regression grid]")
    for B_ in (1, 2, 4):
        for S in (6, 33, 128, 257):
            for D in (512, 1024, 1536, 3072):
                case_explicit(B_, S, D, "B1D", f"grid_{B_}x{S}x{D}")
                case_ca(B_, S, D, torch.bfloat16, 1, f"grid_{B_}x{S}x{D}")

    # Explicit param layouts.
    print("[param layouts]")
    for layout in ("BD", "B1D", "BSD"):
        case_explicit(2, 128, 1024, layout, f"layout_{layout}")

    # fp32 scale_shift_table + temb_seq == S.
    print("[ca variants]")
    case_ca(2, 128, 1024, torch.float32, 1, "table_fp32")
    case_ca(2, 128, 1024, torch.bfloat16, 128, "temb_seq_S")
    case_ca(2, 128, 1024, torch.float32, 128, "table_fp32_temb_seq_S")

    # Poison self-test: skipping the candidate must be detected.
    print("[poison self-test]")
    x = torch.randn(2, 64, 512, device=_DEV, dtype=torch.bfloat16)
    s0, h0, s1, h1 = _explicit_params(2, 64, 512, "B1D", _DEV)
    yb0, yb1 = torch.empty_like(x), torch.empty_like(x)
    yc0, yc1 = torch.empty_like(x), torch.empty_like(x)
    B.ltx2_dual_modulate_baseline(x, s0, h0, s1, h1, _EPS, yb0, yb1)
    _poison([yc0, yc1])  # deliberately do NOT run the candidate
    _check("poison_selftest", not torch.equal(yb0, yc0), "poison not detected")

    # Rejection of unsupported rows (both baseline and candidate).
    print("[rejection]")
    good = lambda B_, S, D: torch.randn(B_, S, D, device=_DEV, dtype=torch.bfloat16)
    p = lambda B_, D: torch.randn(B_, 1, D, device=_DEV, dtype=torch.bfloat16)
    expect_raises("baseline/non_bf16_x", lambda: B.ltx2_dual_modulate_baseline(
        torch.randn(2, 8, 512, device=_DEV, dtype=torch.float16),
        p(2, 512), p(2, 512), p(2, 512), p(2, 512), _EPS,
        torch.empty(2, 8, 512, device=_DEV, dtype=torch.float16),
        torch.empty(2, 8, 512, device=_DEV, dtype=torch.float16)))
    expect_raises("baseline/D_not_mult_256", lambda: B.ltx2_dual_modulate_baseline(
        good(2, 8, 300), p(2, 300), p(2, 300), p(2, 300), p(2, 300), _EPS,
        good(2, 8, 300), good(2, 8, 300)))
    expect_raises("baseline/D_gt_8192", lambda: B.ltx2_dual_modulate_baseline(
        good(2, 8, 8448), p(2, 8448), p(2, 8448), p(2, 8448), p(2, 8448), _EPS,
        good(2, 8, 8448), good(2, 8, 8448)))
    expect_raises("baseline/param_hidden_mismatch", lambda: B.ltx2_dual_modulate_baseline(
        good(2, 8, 512), p(2, 256), p(2, 512), p(2, 512), p(2, 512), _EPS,
        good(2, 8, 512), good(2, 8, 512)))
    x_good = good(2, 8, 512)
    nm = _rms(x_good)
    expect_raises("candidate/D_not_mult_256", lambda: _cand.ltx2_dual_modulate_candidate(
        _rms(good(2, 8, 300)), p(2, 300), p(2, 300), p(2, 300), p(2, 300),
        good(2, 8, 300), good(2, 8, 300)))
    expect_raises("candidate/param_hidden_mismatch", lambda: _cand.ltx2_dual_modulate_candidate(
        nm, p(2, 256), p(2, 512), p(2, 512), p(2, 512), x_good, x_good))

    print(f"\n=== correctness: {_n_pass} passed, {_n_fail} failed ===")
    if _n_fail:
        for f in _failures:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
