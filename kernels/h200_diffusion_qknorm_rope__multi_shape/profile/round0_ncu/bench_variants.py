"""Dispatcher A/B: 2-heads-per-warp vs 1-head-per-warp on H200, with a
1-head-vs-2-head correctness cross-check (both are already validated vs the
oracle through the 2-head path). Pristine inputs per timed sample, CUDA events."""

import os
import sys

import torch

_HERE = os.path.dirname(os.path.abspath(__file__))
_CAND = os.path.abspath(os.path.join(_HERE, "..", ".."))  # profile/round0_ncu -> cand
sys.path.insert(0, os.path.join(_CAND, "src"))
import wrapper as W  # noqa: E402

mod = W._module()


def make_cos_sin(rope, maxpos):
    inv = 1.0 / (10000.0 ** (torch.arange(0, rope, 2, dtype=torch.float32, device="cuda") / rope))
    t = torch.arange(maxpos, dtype=torch.float32, device="cuda")
    fr = torch.einsum("i,j->ij", t, inv)
    return torch.cat((fr.cos(), fr.sin()), dim=-1)


def bench(fn, q0, k0, qw, kw, cache, pos, warmup=30, iters=200):
    q, k = q0.clone(), k0.clone()
    def restore():
        q.copy_(q0); k.copy_(k0)
    for _ in range(warmup):
        restore(); fn(q, k, qw, kw, cache, pos)
    torch.cuda.synchronize()
    s = torch.cuda.Event(enable_timing=True); e = torch.cuda.Event(enable_timing=True); ts = []
    for _ in range(iters):
        restore(); torch.cuda.synchronize(); s.record(); fn(q, k, qw, kw, cache, pos); e.record(); torch.cuda.synchronize()
        ts.append(s.elapsed_time(e) * 1000.0)
    ts.sort(); return ts[len(ts) // 2]


SHAPES = [("large_h24", 8424, 24), ("large_h30", 4128, 30), ("qwen_4096", 4096, 24),
          ("tiny_47", 47, 24), ("tiny_19", 19, 24)]
print(f"{'shape':14s} {'2head_us':>9s} {'1head_us':>9s} {'2head/1head':>11s}  maxdiff")
for name, T, H in SHAPES:
    g = torch.Generator(device="cuda").manual_seed(0)
    q0 = torch.randn(T, H, 128, device="cuda", dtype=torch.bfloat16, generator=g)
    k0 = torch.randn(T, H, 128, device="cuda", dtype=torch.bfloat16, generator=g)
    qw = torch.randn(128, device="cuda", dtype=torch.bfloat16, generator=g)
    kw = torch.randn(128, device="cuda", dtype=torch.bfloat16, generator=g)
    pos = torch.randint(0, T, (T,), device="cuda", dtype=torch.int64)
    cache = make_cos_sin(128, T)
    f2 = lambda q, k, qw, kw, c, p: mod.fused_qknorm_rope(q, k, qw, kw, c, p, 1e-6, False)
    f1 = lambda q, k, qw, kw, c, p: mod.fused_qknorm_rope_1head(q, k, qw, kw, c, p, 1e-6, False)
    qa, ka = q0.clone(), k0.clone(); f2(qa, ka, qw, kw, cache, pos)
    qb, kb = q0.clone(), k0.clone(); f1(qb, kb, qw, kw, cache, pos)
    md = max((qa.float() - qb.float()).abs().max().item(), (ka.float() - kb.float()).abs().max().item())
    t2 = bench(f2, q0, k0, qw, kw, cache, pos)
    t1 = bench(f1, q0, k0, qw, kw, cache, pos)
    print(f"{name:14s} {t2:9.3f} {t1:9.3f} {t2 / t1:11.3f}  {md:.5f}")
