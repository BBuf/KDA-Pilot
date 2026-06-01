"""NCU profiling entrypoint: launch a single target kernel (candidate or
baseline) on a given shape, after warmup, for Nsight Compute to profile.

Usage: profile_entry.py <kind> <M> <N>
  kind in {rms, rms_base, ln, ln_base}
Run under ncu with `-k regex:"rms_norm_warp|layer_norm_block|rms_norm|norm_infer"`
and `--launch-skip 4 --launch-count 1` to profile the post-warmup launch.
"""
import importlib.util
import pathlib
import sys

import torch

KD = pathlib.Path(__file__).resolve().parents[3]  # workspace root
sys.path.insert(0, str(KD / "src"))
import norm_dispatch as nd  # noqa: E402

kind = sys.argv[1]
M, N = int(sys.argv[2]), int(sys.argv[3])
is_ln = kind in ("ln", "ln_base")
dt = torch.float32 if is_ln else torch.bfloat16

x = torch.randn(M, N, device="cuda", dtype=dt)
w = torch.randn(N, device="cuda", dtype=dt)
b = torch.randn(N, device="cuda", dtype=dt) if is_ln else None


def call():
    if kind == "rms":
        return nd.triton_one_pass_rms_norm(x, w, 1e-6)
    if kind == "rms_base":
        return nd._baseline_rms_norm(x, w, 1e-6)
    if kind == "ln":
        return nd.norm_infer(x, w, b, 1e-6, is_rms_norm=False)
    if kind == "ln_base":
        return nd._baseline_norm_infer(x, w, b, 1e-6, is_rms_norm=False)
    raise SystemExit(f"bad kind {kind}")


for _ in range(5):  # warmup (compile + cache + launch a few times)
    call()
torch.cuda.synchronize()
call()  # the launch NCU profiles (after --launch-skip)
torch.cuda.synchronize()
