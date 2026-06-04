"""In-tree misaligned-cache check for the arbiter (runs against whichever SGLang is on PYTHONPATH).

Builds a contiguous [rows, 128] float32 cos/sin cache whose data_ptr() % 16 != 0 and calls
SGLang's OWN public fused_inplace_qknorm_rope with it. With the candidate .cuh placed in-tree,
the launcher's alignment guard must route this base to the scalar-load one-head kernel and the
result must still match the split oracle from the same checkout.
"""

import os

import torch

from flashinfer.rope import apply_rope_with_cos_sin_cache_inplace
from sglang.jit_kernel.diffusion.qknorm_rope import fused_inplace_qknorm_rope as public_fn
from sglang.jit_kernel.norm import fused_inplace_qknorm

dev = "cuda"
ATOL, RTOL = 8e-2, 1e-2
tokens, heads, D, R, eps = 4096, 24, 128, 128, 1e-6

gen = torch.Generator(device="cpu").manual_seed(tokens * 131 + heads)
q = torch.randn(tokens, heads, D, generator=gen, dtype=torch.bfloat16).to(dev)
k = torch.randn(tokens, heads, D, generator=gen, dtype=torch.bfloat16).to(dev)
qw = torch.randn(D, generator=gen, dtype=torch.bfloat16).to(dev)
kw = torch.randn(D, generator=gen, dtype=torch.bfloat16).to(dev)
inv = 1.0 / (10000.0 ** (torch.arange(0, R, 2, device=dev, dtype=torch.float32) / R))
tt = torch.arange(tokens, device=dev, dtype=torch.float32)
csc = torch.cat([torch.outer(tt, inv).cos(), torch.outer(tt, inv).sin()], dim=-1)
pos = torch.randperm(tokens, device=dev).to(torch.int64)

backing = torch.empty(tokens * R + 4, device=dev, dtype=torch.float32)
mis = backing[1 : 1 + tokens * R].view(tokens, R)
mis.copy_(csc)
assert mis.is_contiguous()
assert mis.data_ptr() % 16 != 0, "setup must produce a misaligned base"

q_o, k_o = q.clone(), k.clone()
fused_inplace_qknorm(q_o, k_o, qw, kw, eps)
apply_rope_with_cos_sin_cache_inplace(
    positions=pos, query=q_o.view(tokens, -1), key=k_o.view(tokens, -1),
    head_size=D, cos_sin_cache=csc, is_neox=False)

q_c, k_c = q.clone(), k.clone()
public_fn(q_c, k_c, qw, kw, mis, pos, is_neox=False, eps=eps, rope_dim=R)

assert not torch.isnan(q_c.float()).any() and not torch.isinf(q_c.float()).any()
assert not torch.isnan(k_c.float()).any() and not torch.isinf(k_c.float()).any()
torch.testing.assert_close(q_c.float(), q_o.float(), atol=ATOL, rtol=RTOL)
torch.testing.assert_close(k_c.float(), k_o.float(), atol=ATOL, rtol=RTOL)
print(f"MISALIGNED_CACHE PASS (sglang={os.path.dirname(__import__('sglang').__file__)}, "
      f"base_mod16={mis.data_ptr() % 16})")
