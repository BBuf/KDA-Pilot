"""NCU profile harness for the anchor candidate kernels.

Builds the task-local candidate ``.cuh`` through SGLang's load_jit with
``-lineinfo`` added (separate module name so the production build cache is
untouched) and drives ONE entry at the captured production shape so Nsight
Compute can attach with ``--launch-skip/--launch-count``.

Usage (inside the sglang_bbuf container, CUDA_VISIBLE_DEVICES pinned):
    python profile_harness.py single|dual [iters]
"""

import sys
from pathlib import Path

import torch

_HARNESS_DIR = Path(__file__).resolve().parent
_KERNEL_DIR = _HARNESS_DIR.parents[2]
_CANDIDATE_CUH = _KERNEL_DIR / "src" / "norm_tanh_mul_add_candidate.cuh"

# Captured production shape (S=4096 bucket; S=4128 is near-identical).
SEQ_LEN = 4096
DIM = 3840
EPS = 1e-5


def _jit_module_lineinfo():
    from sglang.jit_kernel.utils import load_jit

    return load_jit(
        "kda_h200_norm_tanh_mul_add_profile",
        cuda_files=[str(_CANDIDATE_CUH)],
        cuda_wrappers=[
            ("single_fast", "NormTanhMulAddSingleKernel<bf16_t>::run"),
            ("dual_fast", "NormTanhMulAddDualKernel<bf16_t>::run"),
        ],
        extra_cuda_cflags=["-lineinfo"],
    )


def main() -> int:
    entry = sys.argv[1] if len(sys.argv) > 1 else "single"
    iters = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    assert entry in ("single", "dual"), entry
    torch.manual_seed(20260604)
    dt = torch.bfloat16

    x = torch.randn(SEQ_LEN, DIM, device="cuda", dtype=dt)
    w = torch.randn(DIM, device="cuda", dtype=dt)
    sc = torch.randn(DIM, device="cuda", dtype=dt)
    sh = torch.randn(SEQ_LEN, DIM, device="cuda", dtype=dt)
    y = torch.empty_like(x)
    mod = _jit_module_lineinfo()

    if entry == "single":
        fn = mod.single_fast
        args = (x, w, sc, sh, y, EPS)
    else:
        w2 = torch.randn(DIM, device="cuda", dtype=dt)
        sc2 = torch.randn(DIM, device="cuda", dtype=dt)
        y2 = torch.empty_like(x)
        fn = mod.dual_fast
        args = (x, w, sc, sh, w2, sc2, y, y2, EPS)

    # JIT/compile + cache warmup outside the profiled launches.
    for _ in range(5):
        fn(*args)
    torch.cuda.synchronize()
    for _ in range(iters):
        fn(*args)
    torch.cuda.synchronize()
    print(f"profiled entry={entry} shape=[1,{SEQ_LEN},{DIM}] bf16 iters={iters}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
