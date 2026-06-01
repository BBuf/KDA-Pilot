"""NCU profiling entrypoint for the H200 fused QK-Norm+RoPE candidate.

Launches ONLY the candidate native CUDA kernel (built with -lineinfo via the
workspace wrapper) many times on a fixed captured shape, so Nsight Compute can
capture an isolated steady-state launch (filter by kernel name regex
`fused_qknorm_rope`, skip warmups with --launch-skip). The op is in place; for
profiling we reuse the same buffers across launches (kernel exec metrics are
value-independent — no data-dependent control flow), which keeps the captured
kernel free of interleaved clone launches.

Usage: python prof_entry.py <tokens> <num_heads>
"""

import os
import sys

import torch

_HERE = os.path.dirname(os.path.abspath(__file__))
_CAND = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))  # profile/<run>/harness -> cand root
sys.path.insert(0, os.path.join(_CAND, "src"))
import wrapper as W  # noqa: E402

T = int(sys.argv[1])
H = int(sys.argv[2])
D = 128
ROPE = 128
g = torch.Generator(device="cuda").manual_seed(0)
q = torch.randn(T, H, D, device="cuda", dtype=torch.bfloat16, generator=g)
k = torch.randn(T, H, D, device="cuda", dtype=torch.bfloat16, generator=g)
qw = torch.randn(D, device="cuda", dtype=torch.bfloat16, generator=g)
kw = torch.randn(D, device="cuda", dtype=torch.bfloat16, generator=g)
pos = torch.randint(0, T, (T,), device="cuda", dtype=torch.int64)
inv = 1.0 / (10000.0 ** (torch.arange(0, ROPE, 2, dtype=torch.float32, device="cuda") / ROPE))
t = torch.arange(T, dtype=torch.float32, device="cuda")
fr = torch.einsum("i,j->ij", t, inv)
cache = torch.cat((fr.cos(), fr.sin()), dim=-1)

W.build()
N = int(os.environ.get("PROF_ITERS", "90"))
for _ in range(N):
    W.fused_inplace_qknorm_rope(q, k, qw, kw, cache, pos, is_neox=False, rope_dim=ROPE)
torch.cuda.synchronize()
print("done T=%d H=%d path=%s" % (T, H, W.last_dispatch_path()))
