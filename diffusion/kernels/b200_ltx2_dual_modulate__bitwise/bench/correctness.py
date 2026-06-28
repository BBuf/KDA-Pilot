"""Bitwise correctness gate for b200_ltx2_dual_modulate__bitwise.

The candidate must be BIT-FOR-BIT equal (`torch.equal`, atol=rtol=0) to an
INDEPENDENT pure-PyTorch oracle (defined here, not imported from baseline/) for both
operations across: production rows; the canonical regression grid crossed with the
[B,D]/[B,1,D]/[B,S,D] param layouts (uniform AND every independent mix); the CA grid
crossed with table dtype {bf16,fp32} and temb_seq in {1,S}; padded (non-compact,
last-dim-contiguous) tables; the D=8192 boundary; fixed-seed reproducibility. The
baseline module is checked against the same oracle. Output buffers are NaN-poisoned
before each run so a skipped kernel is caught. Unsupported inputs (including
non-contiguous temb) must raise on BOTH the baseline and the candidate.

Run on a B200:  python bench/correctness.py    (exit 0 iff all checks pass)
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

_TASK_ROOT = Path(__file__).resolve().parents[1]
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))

import torch
import torch.nn.functional as F

from baseline.build import load_baseline_module
from solution.build import load_candidate_module

_baseline = load_baseline_module()
_candidate = load_candidate_module()
_DEV = "cuda"
_EPS = 1e-6

_n_pass = 0
_n_fail = 0
_failures: list[str] = []


def _check(tag: str, cond: bool, detail: str = "") -> None:
    global _n_pass, _n_fail
    if cond:
        _n_pass += 1
    else:
        _n_fail += 1
        _failures.append(f"{tag}: {detail}")
        print(f"  FAIL {tag}: {detail}")


def _poison(*outs):
    for t in outs:
        t.fill_(float("nan"))


# ---- Independent pure-PyTorch oracle (the authoritative reference) ----
def _bc(p):
    return p.unsqueeze(1) if p.dim() == 2 else p


def oracle_explicit(x, s0, h0, s1, h1, eps=_EPS):
    normed = F.rms_norm(x, (x.shape[-1],), eps=eps)
    return (normed * (1 + _bc(s0)) + _bc(h0), normed * (1 + _bc(s1)) + _bc(h1))


def oracle_ca(x, temb, table, eps=_EPS):
    b, s, d = x.shape
    temb_seq = temb.shape[1]
    # reshape (not view) so a non-compact, last-dim-contiguous table is handled.
    s0, h0, s1, h1 = (
        table.to(dtype=x.dtype).reshape(1, 1, 4, d) + temb.reshape(b, temb_seq, 4, d)
    ).unbind(dim=2)
    normed = F.rms_norm(x, (d,), eps=eps)
    return (normed * (1 + s0) + h0, normed * (1 + s1) + h1)


def _one_param(B_, S, D, layout, device):
    shape = {"BD": (B_, D), "B1D": (B_, 1, D), "BSD": (B_, S, D)}[layout]
    return torch.randn(shape, device=device, dtype=torch.bfloat16)


def case_explicit(B_, S, D, layouts, tag):
    """layouts: 4-tuple of {BD,B1D,BSD}, one per scale0/shift0/scale1/shift1."""
    x = torch.randn(B_, S, D, device=_DEV, dtype=torch.bfloat16)
    s0, h0, s1, h1 = (_one_param(B_, S, D, l, _DEV) for l in layouts)
    r0, r1 = oracle_explicit(x, s0, h0, s1, h1)
    yb0, yb1 = torch.empty_like(x), torch.empty_like(x)
    yc0, yc1 = torch.empty_like(x), torch.empty_like(x)
    _poison(yc0, yc1)
    _candidate.ltx2_dual_modulate_candidate(x, s0, h0, s1, h1, _EPS, yc0, yc1)
    _baseline.ltx2_dual_modulate_baseline(x, s0, h0, s1, h1, _EPS, yb0, yb1)
    _check(f"explicit/{tag}/cand_y0", torch.equal(r0, yc0), "candidate != oracle")
    _check(f"explicit/{tag}/cand_y1", torch.equal(r1, yc1), "candidate != oracle")
    _check(f"explicit/{tag}/base_y0", torch.equal(r0, yb0), "baseline != oracle")
    _check(f"explicit/{tag}/base_y1", torch.equal(r1, yb1), "baseline != oracle")


def _make_table(D, table_dtype, pad, device):
    if pad:
        parent = torch.randn(4, D + pad, device=device, dtype=table_dtype)
        t = parent[:, :D]  # [4,D], last-dim contiguous, row stride D+pad > D
        assert t.stride(0) == D + pad and t.stride(1) == 1
        return t
    return torch.randn(4, D, device=device, dtype=table_dtype)


def case_ca(B_, S, D, table_dtype, temb_seq, tag, table_pad=0):
    x = torch.randn(B_, S, D, device=_DEV, dtype=torch.bfloat16)
    temb = torch.randn(B_, temb_seq, 4 * D, device=_DEV, dtype=torch.bfloat16)
    table = _make_table(D, table_dtype, table_pad, _DEV)
    r0, r1 = oracle_ca(x, temb, table)
    yb0, yb1 = torch.empty_like(x), torch.empty_like(x)
    yc0, yc1 = torch.empty_like(x), torch.empty_like(x)
    _poison(yc0, yc1)
    _candidate.ltx2_ca_dual_modulate_from_temb_candidate(x, temb, table, _EPS, yc0, yc1)
    _baseline.ltx2_ca_dual_modulate_from_temb_baseline(x, temb, table, _EPS, yb0, yb1)
    _check(f"ca/{tag}/cand_y0", torch.equal(r0, yc0), "candidate != oracle")
    _check(f"ca/{tag}/cand_y1", torch.equal(r1, yc1), "candidate != oracle")
    _check(f"ca/{tag}/base_y0", torch.equal(r0, yb0), "baseline != oracle")
    _check(f"ca/{tag}/base_y1", torch.equal(r1, yb1), "baseline != oracle")


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

    print("[production rows]")
    for B_, S, D in [(2, 1536, 4096), (2, 126, 2048), (1, 6144, 4096), (1, 126, 2048)]:
        case_explicit(B_, S, D, ("B1D",) * 4, f"prod_{B_}x{S}x{D}")
        case_ca(B_, S, D, torch.bfloat16, 1, f"prod_{B_}x{S}x{D}")

    print("[regression grid x uniform explicit param layouts]")
    for B_ in (1, 2, 4):
        for S in (6, 33, 128, 257):
            for D in (512, 1024, 1536, 3072):
                for layout in ("BD", "B1D", "BSD"):
                    case_explicit(B_, S, D, (layout,) * 4, f"grid_{B_}x{S}x{D}_{layout}")

    print("[independent mixed explicit param layouts: 81 combinations]")
    short = {"BD": "d", "B1D": "1", "BSD": "s"}
    for combo in itertools.product(("BD", "B1D", "BSD"), repeat=4):
        tag = "mix_" + "".join(short[c] for c in combo)
        case_explicit(2, 128, 1024, combo, tag)
    # A production-sized mixed row.
    case_explicit(2, 1536, 4096, ("BD", "B1D", "BSD", "B1D"), "mix_prod_2x1536x4096")

    print("[regression grid x CA table dtype x temb_seq]")
    for B_ in (1, 2, 4):
        for S in (6, 33, 128, 257):
            for D in (512, 1024, 1536, 3072):
                for td in (torch.bfloat16, torch.float32):
                    for tseq in (1, S):
                        case_ca(B_, S, D, td, tseq, f"grid_{B_}x{S}x{D}_{td}_ts{tseq}")

    print("[padded (non-compact, last-dim-contiguous) tables]")
    for td in (torch.bfloat16, torch.float32):
        for tseq in (1, 128):
            case_ca(2, 128, 1024, td, tseq, f"padtab_{td}_ts{tseq}", table_pad=64)

    print("[D=8192 boundary]")
    case_explicit(1, 8, 8192, ("B1D",) * 4, "D8192")
    case_ca(1, 8, 8192, torch.float32, 8, "D8192")

    print("[reproducibility: same seed -> identical bits]")
    torch.manual_seed(123)
    x = torch.randn(2, 64, 1024, device=_DEV, dtype=torch.bfloat16)
    s0, h0, s1, h1 = (_one_param(2, 64, 1024, "B1D", _DEV) for _ in range(4))
    a0, a1 = torch.empty_like(x), torch.empty_like(x)
    b0, b1 = torch.empty_like(x), torch.empty_like(x)
    _candidate.ltx2_dual_modulate_candidate(x, s0, h0, s1, h1, _EPS, a0, a1)
    _candidate.ltx2_dual_modulate_candidate(x, s0, h0, s1, h1, _EPS, b0, b1)
    _check("repro", torch.equal(a0, b0) and torch.equal(a1, b1), "non-deterministic")

    print("[poison self-test: skipped kernel detected]")
    yc0, yc1 = torch.empty_like(x), torch.empty_like(x)
    _poison(yc0, yc1)
    r0, _ = oracle_explicit(x, s0, h0, s1, h1)
    _check("poison_selftest", not torch.equal(r0, yc0), "poison not detected")

    print("[rejection: both sides must raise]")
    g = lambda B_, S, D: torch.randn(B_, S, D, device=_DEV, dtype=torch.bfloat16)
    p = lambda B_, D: torch.randn(B_, 1, D, device=_DEV, dtype=torch.bfloat16)
    o = lambda B_, S, D: torch.empty(B_, S, D, device=_DEV, dtype=torch.bfloat16)
    # non-compact output view: stride(1) = 2D != D
    nc = lambda B_, S, D: torch.empty(B_, S, 2 * D, device=_DEV, dtype=torch.bfloat16)[:, :, :D]
    explicit_cases = {
        "non_cuda_x": lambda f: f(torch.randn(2, 8, 512, dtype=torch.bfloat16),
                                  p(2, 512), p(2, 512), p(2, 512), p(2, 512), _EPS,
                                  o(2, 8, 512), o(2, 8, 512)),
        "non_bf16_x": lambda f: f(torch.randn(2, 8, 512, device=_DEV, dtype=torch.float16),
                                  p(2, 512), p(2, 512), p(2, 512), p(2, 512), _EPS,
                                  torch.empty(2, 8, 512, device=_DEV, dtype=torch.float16),
                                  torch.empty(2, 8, 512, device=_DEV, dtype=torch.float16)),
        "noncontig_last_x": lambda f: f(g(2, 8, 1024)[:, :, ::2], p(2, 512), p(2, 512),
                                        p(2, 512), p(2, 512), _EPS, o(2, 8, 512), o(2, 8, 512)),
        "D_not_mult_256": lambda f: f(g(2, 8, 300), p(2, 300), p(2, 300), p(2, 300),
                                      p(2, 300), _EPS, g(2, 8, 300), g(2, 8, 300)),
        "D_gt_8192": lambda f: f(g(2, 8, 8448), p(2, 8448), p(2, 8448), p(2, 8448),
                                 p(2, 8448), _EPS, g(2, 8, 8448), g(2, 8, 8448)),
        "param_hidden_mismatch": lambda f: f(g(2, 8, 512), p(2, 256), p(2, 512),
                                             p(2, 512), p(2, 512), _EPS, o(2, 8, 512), o(2, 8, 512)),
        "param_rank1": lambda f: f(g(2, 8, 512),
                                   torch.randn(512, device=_DEV, dtype=torch.bfloat16),
                                   p(2, 512), p(2, 512), p(2, 512), _EPS, o(2, 8, 512), o(2, 8, 512)),
        "param_wrong_batch": lambda f: f(g(2, 8, 512), p(1, 512), p(2, 512), p(2, 512),
                                         p(2, 512), _EPS, o(2, 8, 512), o(2, 8, 512)),
        "param_wrong_seq": lambda f: f(g(2, 8, 512),
                                       torch.randn(2, 2, 512, device=_DEV, dtype=torch.bfloat16),
                                       p(2, 512), p(2, 512), p(2, 512), _EPS, o(2, 8, 512), o(2, 8, 512)),
        "noncompact_y0": lambda f: f(g(2, 8, 512), p(2, 512), p(2, 512), p(2, 512),
                                     p(2, 512), _EPS, nc(2, 8, 512), o(2, 8, 512)),
        "noncompact_y1": lambda f: f(g(2, 8, 512), p(2, 512), p(2, 512), p(2, 512),
                                     p(2, 512), _EPS, o(2, 8, 512), nc(2, 8, 512)),
    }
    for name, build in explicit_cases.items():
        expect_raises(f"baseline/{name}", lambda b=build: b(_baseline.ltx2_dual_modulate_baseline))
        expect_raises(f"candidate/{name}", lambda b=build: b(_candidate.ltx2_dual_modulate_candidate))

    # Non-compact temb (sliced last dim) and bad table/temb shapes.
    def noncompact_temb(D):
        parent = torch.randn(2, 1, 4 * D + 64, device=_DEV, dtype=torch.bfloat16)
        t = parent[:, :, : 4 * D]  # stride(1) = 4D+64 != 4D -> non-compact
        assert t.stride(2) == 1 and t.stride(1) != 4 * D
        return t
    ca_cases = {
        "table_wrong_rows": lambda f: f(g(2, 8, 512),
                                        torch.randn(2, 1, 4 * 512, device=_DEV, dtype=torch.bfloat16),
                                        torch.randn(5, 512, device=_DEV, dtype=torch.bfloat16),
                                        _EPS, o(2, 8, 512), o(2, 8, 512)),
        "temb_wrong_last": lambda f: f(g(2, 8, 512),
                                       torch.randn(2, 1, 3 * 512, device=_DEV, dtype=torch.bfloat16),
                                       torch.randn(4, 512, device=_DEV, dtype=torch.bfloat16),
                                       _EPS, o(2, 8, 512), o(2, 8, 512)),
        "temb_noncompact": lambda f: f(g(2, 8, 512), noncompact_temb(512),
                                       torch.randn(4, 512, device=_DEV, dtype=torch.bfloat16),
                                       _EPS, o(2, 8, 512), o(2, 8, 512)),
        "noncompact_y0": lambda f: f(g(2, 8, 512),
                                     torch.randn(2, 1, 4 * 512, device=_DEV, dtype=torch.bfloat16),
                                     torch.randn(4, 512, device=_DEV, dtype=torch.bfloat16),
                                     _EPS, nc(2, 8, 512), o(2, 8, 512)),
        "noncompact_y1": lambda f: f(g(2, 8, 512),
                                     torch.randn(2, 1, 4 * 512, device=_DEV, dtype=torch.bfloat16),
                                     torch.randn(4, 512, device=_DEV, dtype=torch.bfloat16),
                                     _EPS, o(2, 8, 512), nc(2, 8, 512)),
    }
    for name, build in ca_cases.items():
        expect_raises(f"baseline/{name}", lambda b=build: b(_baseline.ltx2_ca_dual_modulate_from_temb_baseline))
        expect_raises(f"candidate/{name}", lambda b=build: b(_candidate.ltx2_ca_dual_modulate_from_temb_candidate))

    if torch.cuda.device_count() >= 2:
        print("[multi-GPU: candidate honors x.device via CUDAGuard]")
        torch.cuda.set_device(0)  # current device 0; the tensors live on device 1
        d1 = "cuda:1"
        xm = torch.randn(2, 64, 1024, device=d1, dtype=torch.bfloat16)
        pm = [torch.randn(2, 1, 1024, device=d1, dtype=torch.bfloat16) for _ in range(4)]
        rm0, rm1 = oracle_explicit(xm, *pm)
        ym0, ym1 = torch.empty_like(xm), torch.empty_like(xm)
        _candidate.ltx2_dual_modulate_candidate(xm, *pm, _EPS, ym0, ym1)
        torch.cuda.synchronize(d1)
        _check("multigpu/explicit_y0", torch.equal(rm0, ym0), "wrong on non-current device")
        _check("multigpu/explicit_y1", torch.equal(rm1, ym1), "wrong on non-current device")
        tm = torch.randn(2, 1, 4 * 1024, device=d1, dtype=torch.bfloat16)
        tbl = torch.randn(4, 1024, device=d1, dtype=torch.bfloat16)
        cm0, cm1 = oracle_ca(xm, tm, tbl)
        yc0, yc1 = torch.empty_like(xm), torch.empty_like(xm)
        _candidate.ltx2_ca_dual_modulate_from_temb_candidate(xm, tm, tbl, _EPS, yc0, yc1)
        torch.cuda.synchronize(d1)
        _check("multigpu/ca_y0", torch.equal(cm0, yc0), "wrong on non-current device")
        _check("multigpu/ca_y1", torch.equal(cm1, yc1), "wrong on non-current device")
        ybad = torch.empty(2, 64, 1024, device="cuda:0", dtype=torch.bfloat16)
        expect_raises("multigpu/cross_device_output",
                      lambda: _candidate.ltx2_dual_modulate_candidate(xm, *pm, _EPS, ybad, ym1))
        torch.cuda.set_device(0)
    else:
        print("[multi-GPU: skipped — fewer than 2 visible CUDA devices]")

    print(f"\n=== correctness: {_n_pass} passed, {_n_fail} failed ===")
    if _n_fail:
        for f in _failures[:50]:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
