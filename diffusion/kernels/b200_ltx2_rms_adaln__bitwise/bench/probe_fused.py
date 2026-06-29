#!/usr/bin/env python3
"""Bounded fully-fused-attempt feasibility probe.

Decides whether a fully-fused single kernel (RMS reduction + modulation in one
pass) can be bit-wise exact. The gate is: does a custom single-kernel fp32 RMS
reduction reproduce at::rms_norm's bf16 `normed` bit-for-bit?

Builds solution/fused_probe.cu (`ltx2_rms_normed_probe`) and compares its raw
uint16 output against torch.nn.functional.rms_norm on the production rows plus the
canonical adapted shapes. If any row differs, a fully-fused kernel cannot
guarantee bit-exactness -> the staged path (reuse at::rms_norm) is the production
choice (see docs/results.md). No sglang import.
"""

from __future__ import annotations

import pathlib
import sys

import torch

_SOL = pathlib.Path(__file__).resolve().parents[1] / "solution"
_CU = _SOL / "fused_probe.cu"


def _load():
    from torch.utils import cpp_extension as c
    from tvm_ffi.cpp import load

    inc = list(c.include_paths(device_type="cuda"))
    lib = list(c.library_paths(device_type="cuda"))
    ld = [f"-L{p}" for p in lib] + [f"-Wl,-rpath,{p}" for p in lib]
    ld += ["-lc10", "-lc10_cuda", "-ltorch_cpu", "-ltorch_cuda"]
    major, minor = torch.cuda.get_device_capability()
    return load(
        "ltx2_rms_normed_probe",
        cuda_files=[str(_CU)],
        extra_cflags=["-std=c++17", "-O3"],
        extra_cuda_cflags=["-std=c++17", "-O3",
                           f"-gencode=arch=compute_{major}{minor},code=sm_{major}{minor}"],
        extra_ldflags=ld,
        extra_include_paths=inc,
        build_directory=str(_SOL / ".build" / "probe"),
    )


def main() -> int:
    dev = torch.device("cuda:0")
    torch.cuda.set_device(dev)
    torch.set_grad_enabled(False)
    mod = _load()

    print(f"[probe] env: torch {torch.__version__} cuda {torch.version.cuda} "
          f"gpu {torch.cuda.get_device_name(dev)}")

    # All SIX production rows (4 CI two-stage + 2 HQ video) plus the canonical
    # adapted grid shapes, so the gate is not limited to the original 4 rows.
    rows = [
        ("stage1_video", (2, 1536, 4096)),
        ("stage1_audio", (2, 126, 2048)),
        ("stage2_video", (1, 6144, 4096)),
        ("stage2_audio", (1, 126, 2048)),
        ("hq_stage1_video", (1, 8160, 4096)),
        ("hq_stage2_video", (1, 32640, 4096)),
        ("canon_1_8192_3072", (1, 8192, 3072)),
        ("canon_4_8192_3072", (4, 8192, 3072)),
    ]
    # Multiple seeds + an adversarial wide-magnitude mode: a single-kernel fp32
    # reduction whose summation order differs from ATen will diverge most visibly
    # on wide-magnitude inputs (more catastrophic cancellation / reordering).
    seeds = [1234, 20260629, 777]
    iv = torch.uint16
    any_mismatch = False
    total_cases = 0
    print("[probe] candidate single-kernel RMS reduction vs at::rms_norm (bf16, eps=1e-6)")
    print("[probe] modes: randn (~unit) and wide (adversarial wide-magnitude)")
    for name, (B, S, D) in rows:
        for seed in seeds:
            for mode in ("randn", "wide"):
                g = torch.Generator(device=dev).manual_seed(seed)
                if mode == "randn":
                    x = torch.randn(B, S, D, generator=g, device=dev, dtype=torch.bfloat16)
                else:
                    x = ((torch.rand(B, S, D, generator=g, device=dev) * 16.0 - 8.0)
                         .to(torch.bfloat16))
                ref = torch.nn.functional.rms_norm(x, (D,), eps=1e-6)
                got = torch.empty_like(x)
                mod.ltx2_rms_normed_probe(x, 1e-6, got)
                torch.cuda.synchronize()
                eq = torch.equal(got.view(iv), ref.view(iv))
                n = int((got.view(iv) != ref.view(iv)).sum().item())
                tot = got.numel()
                maxabs = (got.float() - ref.float()).abs().max().item()
                any_mismatch = any_mismatch or not eq
                total_cases += 1
                print(f"  {name:18s} [{B},{S},{D}] seed={seed:<9d} {mode:5s}: "
                      f"{'EQUAL ' if eq else 'DIFFER'} mismatch={n}/{tot} "
                      f"({100.0 * n / tot:.4f}%) max_abs={maxabs:.3e}")
    print(f"[probe] cases={total_cases}")
    if any_mismatch:
        print("[probe] RESULT: normed NOT bit-exact on >=1 row/seed/mode -> fully-fused single "
              "kernel NO-GO; staged path (reuse at::rms_norm) is the production choice.")
    else:
        print("[probe] RESULT: normed bit-exact on every row/seed/mode -> fully-fused single "
              "kernel is feasible (would still need to pass the full bitwise + no-regression gates).")
    return 1 if any_mismatch else 0


if __name__ == "__main__":
    sys.exit(main())
