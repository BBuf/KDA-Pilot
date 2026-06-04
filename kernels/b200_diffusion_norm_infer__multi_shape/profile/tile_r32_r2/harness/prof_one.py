"""NCU harness for the tiled multi-row RMSNorm winner (R=32, persistent) and
the pinned Triton baseline, at the captured production shape S=650040, D=128,
bf16 (docs/captured_shapes_b200.jsonl verbatim).

Builds the tiled module from the workspace .cuh through the same jit_kernel /
tvm-ffi stack as production, plus ``-lineinfo`` so SASS maps back to source
(debug info only; codegen flags unchanged — still no fast-math).

Usage under ncu (profile the 4th launch: 3 warmups, then 1 profiled):
    ncu --set full --target-processes all -s 3 -c 1 \
        -k regex:rmsnorm_tiled -o reports/full python harness/prof_one.py tiled
    ncu --set source --section SourceCounters -s 3 -c 1 \
        -k regex:rmsnorm_tiled -o reports/source python harness/prof_one.py tiled
    ncu --set full --target-processes all -s 3 -c 1 \
        -k regex:_rms_norm_tiled_onepass -o reports/baseline_full \
        python harness/prof_one.py baseline
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import torch

KERNEL_DIR = Path(__file__).resolve().parents[3]
S, D = 650040, 128
ROWS_PER_CTA = 32
SCHEDULING = 1
LAUNCHES = 8


def _load_by_path(fq_name: str, path: Path):
    if fq_name in sys.modules:
        return sys.modules[fq_name]
    spec = importlib.util.spec_from_file_location(fq_name, path)
    assert spec is not None and spec.loader is not None, path
    module = importlib.util.module_from_spec(spec)
    sys.modules[fq_name] = module
    spec.loader.exec_module(module)
    return module


def _tiled_module_lineinfo():
    from sglang.jit_kernel.utils import load_jit, make_cpp_args

    args = make_cpp_args(D, ROWS_PER_CTA, torch.bfloat16)
    return load_jit(
        "b200_diffnorm_rms_tiled_prof",
        "v3-lineinfo",
        *args,
        cuda_files=[str(KERNEL_DIR / "src" / "norm_cuda" / "diffusion_norm_infer.cuh")],
        cuda_wrappers=[("rms_tiled", f"RmsNormTiledKernel<{args}>::run")],
        extra_include_paths=[str(KERNEL_DIR / "src" / "norm_cuda")],
        extra_cuda_cflags=["-lineinfo"],
    )


def main() -> int:
    which = sys.argv[1] if len(sys.argv) > 1 else "tiled"
    torch.manual_seed(1004)
    x = torch.randn(S, D, device="cuda", dtype=torch.bfloat16)
    w = torch.randn(D, device="cuda", dtype=torch.bfloat16)

    if which == "tiled":
        mod = _tiled_module_lineinfo()
        out = torch.empty_like(x)
        for _ in range(LAUNCHES):
            mod.rms_tiled(x, w, out, 1e-6, SCHEDULING)
    elif which == "baseline":
        pinned = _load_by_path("kda_pinned_baseline", KERNEL_DIR / "baseline" / "__init__.py")
        for _ in range(LAUNCHES):
            pinned.triton_one_pass_rms_norm(x, w, 1e-6)
    else:
        raise SystemExit(f"unknown target {which!r} (use tiled|baseline)")

    torch.cuda.synchronize()
    print(f"done: {which} x{LAUNCHES} at S={S} D={D}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
