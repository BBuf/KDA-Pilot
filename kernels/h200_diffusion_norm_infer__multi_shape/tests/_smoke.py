"""Fast remote smoke: build the CUDA extension, then check both kernels on a
representative captured shape (correctness vs SGLang baseline + dispatch path).
Run inside the container with PYTHONPATH=<sglang>/python and CUDA_VISIBLE_DEVICES set.
"""

import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))               # tests/ (for _baseline_env)
sys.path.insert(0, str(HERE.parent / "src"))  # src/ (for wrapper)

from _baseline_env import get_baselines, install_platform_shim

install_platform_shim()
import torch

reg_path = HERE.parent / "src" / "register.py"
spec = importlib.util.spec_from_file_location("reg", reg_path)
reg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reg)

reg.build()
print("BUILD_OK")

bni, brms = get_baselines()
torch.manual_seed(0)
dev = "cuda"

# RMS bf16 [4096,128]
x = torch.randn(4096, 128, device=dev, dtype=torch.bfloat16)
w = torch.randn(128, device=dev, dtype=torch.bfloat16)
yb = brms(x, w, 1e-6)
yc = reg.triton_one_pass_rms_norm(x, w, 1e-6)
ref = x.double() * torch.rsqrt((x.double() ** 2).mean(-1, keepdim=True) + 1e-6) * w.double()
print("rms[4096,128] path=%s dtype=%s errBase=%.3e errCand=%.3e maxAbsDiff(cand,base)=%.3e" % (
    reg.last_dispatch("rms"), yc.dtype,
    (yb.double() - ref).abs().max().item(),
    (yc.double() - ref).abs().max().item(),
    (yc.double() - yb.double()).abs().max().item()))

# LN fp32 [8640,5120]
x = torch.randn(8640, 5120, device=dev, dtype=torch.float32)
wl = torch.randn(5120, device=dev, dtype=torch.float32)
bl = torch.randn(5120, device=dev, dtype=torch.float32)
yb = bni(x, wl, bl, 1e-6, False)
yc = reg.norm_infer(x, wl, bl, 1e-6, False)
m = x.double().mean(-1, keepdim=True)
v = ((x.double() - m) ** 2).mean(-1, keepdim=True)
ref = (x.double() - m) * torch.rsqrt(v + 1e-6) * wl.double() + bl.double()
print("ln[8640,5120] path=%s dtype=%s errBase=%.3e errCand=%.3e maxAbsDiff(cand,base)=%.3e" % (
    reg.last_dispatch("norm_infer"), yc.dtype,
    (yb.double() - ref).abs().max().item(),
    (yc.double() - ref).abs().max().item(),
    (yc.double() - yb.double()).abs().max().item()))

# fallback check: a non-captured shape must NOT take the cuda path
xf = torch.randn(100, 128, device=dev, dtype=torch.bfloat16)
_ = reg.triton_one_pass_rms_norm(xf, w, 1e-6)
print("fallback[100,128] path=%s (expect fallback)" % reg.last_dispatch("rms"))
print("SMOKE_OK")
