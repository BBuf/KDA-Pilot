"""Standalone NCU harness: launch one candidate CUDA kernel on a captured shape.

Imports only the compiled extension via ``wrapper._module()`` (no SGLang baseline
needed for profiling), warms it, then launches the target kernel once so NCU can
profile it. Usage: ``python prof.py {rms_huge|rms_small|ln}``.
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve()
WORK = HERE.parents[3]            # profile/ncu_round0/harness/prof.py -> work/
sys.path.insert(0, str(WORK / "src"))

import torch  # noqa: E402
import wrapper  # noqa: E402

wrapper.build()
mod = wrapper._module()
bucket = sys.argv[1] if len(sys.argv) > 1 else "rms_huge"
torch.manual_seed(0)
dev = "cuda"


def run_rms(M):
    x = torch.randn(M, 128, device=dev, dtype=torch.bfloat16)
    w = torch.randn(128, device=dev, dtype=torch.bfloat16)
    for _ in range(3):
        mod.rms_norm_bf16_n128(x, w, 1e-6)
    torch.cuda.synchronize()
    mod.rms_norm_bf16_n128(x, w, 1e-6)
    torch.cuda.synchronize()


def run_ln(M):
    x = torch.randn(M, 5120, device=dev, dtype=torch.float32)
    w = torch.randn(5120, device=dev, dtype=torch.float32)
    b = torch.randn(5120, device=dev, dtype=torch.float32)
    for _ in range(3):
        mod.layer_norm_fp32(x, w, b, 1e-6)
    torch.cuda.synchronize()
    mod.layer_norm_fp32(x, w, b, 1e-6)
    torch.cuda.synchronize()


if bucket == "rms_huge":
    run_rms(650040)
elif bucket == "rms_small":
    run_rms(1320)
elif bucket == "ln":
    run_ln(8640)
else:
    raise SystemExit(f"unknown bucket {bucket}")
print("PROF_DONE", bucket)
