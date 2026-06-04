"""NCU harness: run one qknorm_rope candidate build at the qwen_t4096 captured shape.

Env:
  RKD          - session dir (contains src/ and src_incumbent/)
  KDA_SRC_DIR  - which build to profile: "src" (variant) or "src_incumbent" (incumbent)
  KDA_LAUNCHES - total kernel launches (ncu selects via --launch-skip/--launch-count)

The qwen_t4096 shape: q/k [4096, 24, 128] bf16, rope_dim=128, GPT-J, eps=1e-6, int64 positions.
Tensors are built once; q/k are NOT reset between launches (norm+rope of already-rotated data is
numerically irrelevant for profiling and keeps the loop free of extra copy kernels).
"""

import importlib.util
import os
import sys

import torch

RKD = os.environ["RKD"]
SRC_DIR = os.environ.get("KDA_SRC_DIR", "src")
LAUNCHES = int(os.environ.get("KDA_LAUNCHES", "60"))

spec = importlib.util.spec_from_file_location("wrapper_profiled", os.path.join(RKD, SRC_DIR, "wrapper.py"))
wrapper = importlib.util.module_from_spec(spec)
sys.modules["wrapper_profiled"] = wrapper
spec.loader.exec_module(wrapper)

dev = "cuda"
tokens, heads, dim, rope = 4096, 24, 128, 128
gen = torch.Generator(device="cpu").manual_seed(tokens * 131 + heads)
q = torch.randn(tokens, heads, dim, generator=gen, dtype=torch.bfloat16).to(dev)
k = torch.randn(tokens, heads, dim, generator=gen, dtype=torch.bfloat16).to(dev)
qw = torch.randn(dim, generator=gen, dtype=torch.bfloat16).to(dev)
kw = torch.randn(dim, generator=gen, dtype=torch.bfloat16).to(dev)
inv = 1.0 / (10000.0 ** (torch.arange(0, rope, 2, device=dev, dtype=torch.float32) / rope))
tt = torch.arange(tokens, device=dev, dtype=torch.float32)
csc = torch.cat([torch.outer(tt, inv).cos(), torch.outer(tt, inv).sin()], dim=-1)
pos = torch.arange(tokens, device=dev, dtype=torch.int64)

mod = wrapper._candidate_module(dim, rope, False, torch.bfloat16)
torch.cuda.synchronize()

for _ in range(LAUNCHES):
    mod.qknorm_rope(q, k, qw, kw, csc, pos, 1e-6)
torch.cuda.synchronize()
print(f"profiled {SRC_DIR} for {LAUNCHES} launches", flush=True)
