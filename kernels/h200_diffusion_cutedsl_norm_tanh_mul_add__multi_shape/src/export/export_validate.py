"""In-SGLang drop-in arbiter: correctness + smoke benchmark of the patched
public ops inside an isolated sglang worktree.

Run with PYTHONPATH pointing at <worktree>/python so ``import sglang`` resolves
to the patched tree. The vendored PINNED baseline (kda_baseline:: namespace)
provides the baseline side in the same process — both sides are registered
custom ops, so the comparison goes through IDENTICAL wrapper/dispatch/
registration machinery with only the device path differing.

Usage:
  PYTHONPATH=<worktree>/python python export_validate.py <kernel_task_dir>
"""

import statistics
import sys
import time
from pathlib import Path

import torch

KERNEL_DIR = Path(sys.argv[1]).resolve()
if str(KERNEL_DIR) not in sys.path:
    sys.path.insert(0, str(KERNEL_DIR))

import sglang  # noqa: E402  (must resolve to the patched worktree)
from sglang.jit_kernel.diffusion.cutedsl import (  # noqa: E402
    norm_tanh_mul_add_norm_scale as sgl_ops,
)

import baseline as vendored  # noqa: E402  (pinned baseline, kda_baseline:: ops)

SEQ_LENS = (4096, 4128)
D, EPS = 3840, 1e-5


def _norm32(t32, w, eps):
    return torch.rms_norm(t32, t32.shape[-1:], weight=w.float() if w is not None else None, eps=eps)


def _check_close(a, ref32, scale_terms, atol=5e-2, rtol=5e-2):
    diff = (a.float() - ref32).abs()
    tol = atol + rtol * torch.maximum(ref32.abs(), scale_terms)
    bad = diff > tol
    assert not bad.any(), f"{int(bad.sum())} elements out of tolerance (max {diff.max():.4e})"


def _check_device_fallback_parity() -> None:
    """Unsupported-device probes: production-shaped bf16 calls on CPU (and a
    mixed-device variant) must NOT enter the native CUDA module — they continue
    through the original CuTe-DSL path and behave exactly like the pinned
    baseline (same error class, since that path requires CUDA tensors)."""

    dt = torch.bfloat16
    S = 64
    x_cpu = torch.randn(1, S, D, dtype=dt)
    w_cpu = torch.randn(D, dtype=dt)
    sc_cpu = torch.randn(1, 1, D, dtype=dt)
    sh_cpu = torch.randn(1, S, D, dtype=dt)

    def probe(fn_sgl, fn_base, args, tag):
        err_sgl = err_base = None
        try:
            fn_sgl(*args)
        except Exception as e:  # noqa: BLE001 - parity check needs the class
            err_sgl = e
        try:
            fn_base(*args)
        except Exception as e:  # noqa: BLE001
            err_base = e
        assert (err_sgl is None) == (err_base is None), (
            f"{tag}: patched op and pinned baseline disagree on raising "
            f"({type(err_sgl)} vs {type(err_base)})"
        )
        if err_sgl is not None:
            assert type(err_sgl) is type(err_base), (
                f"{tag}: error-class mismatch {type(err_sgl)} vs {type(err_base)}"
            )
        print(f"{tag}: fallback parity OK "
              f"({'no error' if err_sgl is None else type(err_sgl).__name__})")

    # All-CPU production-shaped call.
    probe(sgl_ops.fused_norm_tanh_mul_add, vendored.fused_norm_tanh_mul_add,
          (x_cpu, w_cpu, None, sc_cpu, sh_cpu, "rms", EPS), "cpu-all single")
    # Mixed-device: CUDA x, CPU scale (gate must reject before any native launch).
    x_gpu = x_cpu.cuda()
    sh_gpu = sh_cpu.cuda()
    w_gpu = w_cpu.cuda()
    probe(sgl_ops.fused_norm_tanh_mul_add, vendored.fused_norm_tanh_mul_add,
          (x_gpu, w_gpu, None, sc_cpu, sh_gpu, "rms", EPS), "mixed-device single")
    # Dual: all-CPU.
    w2_cpu = torch.randn(D, dtype=dt)
    sc2_cpu = torch.randn(1, 1, D, dtype=dt)
    probe(sgl_ops.fused_norm_tanh_mul_add_norm_scale,
          vendored.fused_norm_tanh_mul_add_norm_scale,
          (x_cpu, w_cpu, None, sc_cpu, sh_cpu, w2_cpu, None, sc2_cpu, "rms", EPS),
          "cpu-all dual")


def main() -> int:
    print(f"sglang resolves to: {sglang.__file__}")
    sglang_root = Path(sglang.__file__).resolve()
    assert "sglang_export" in str(sglang_root), (
        f"sglang must resolve to the isolated patched worktree, got {sglang_root}"
    )
    torch.manual_seed(20260604)
    dt = torch.bfloat16

    _check_device_fallback_parity()

    for S in SEQ_LENS:
        x = torch.randn(1, S, D, device="cuda", dtype=dt)
        w = torch.randn(D, device="cuda", dtype=dt)
        sc = torch.randn(1, 1, D, device="cuda", dtype=dt)
        sh = torch.randn(1, S, D, device="cuda", dtype=dt)
        w2 = torch.randn(D, device="cuda", dtype=dt)
        sc2 = torch.randn(1, 1, D, device="cuda", dtype=dt)

        # --- correctness: patched public op vs fp32 oracle + pinned baseline
        y_sgl = sgl_ops.fused_norm_tanh_mul_add(x, w, None, sc, sh, "rms", EPS)
        y_base = vendored.fused_norm_tanh_mul_add(x, w, None, sc, sh, "rms", EPS)
        n_q = _norm32(x.float(), w, EPS).to(dt).float()
        t = n_q * torch.tanh(sc.float())
        y_ref = t + sh.float()
        _check_close(y_sgl, y_ref, t.abs() + sh.float().abs())
        err_sgl = (y_sgl.float() - y_ref).abs().max().item()
        err_base = (y_base.float() - y_ref).abs().max().item()
        assert err_sgl <= 2.0 * err_base + 1e-6, (err_sgl, err_base)
        print(f"S={S} single: oracle OK (sgl-err {err_sgl:.3e} <= 2x base-err {err_base:.3e})")

        yd, y2d = sgl_ops.fused_norm_tanh_mul_add_norm_scale(
            x, w, None, sc, sh, w2, None, sc2, "rms", EPS)
        bd, b2d = vendored.fused_norm_tanh_mul_add_norm_scale(
            x, w, None, sc, sh, w2, None, sc2, "rms", EPS)
        _check_close(yd, y_ref, t.abs() + sh.float().abs())
        n2_q = _norm32(yd.float(), w2, EPS).to(dt).float()
        y2_ref = n2_q * (1 + sc2.float())
        _check_close(y2d, y2_ref, y2_ref.abs())
        print(f"S={S} dual: oracle OK")

        # --- fallback fidelity inside the patched tree (fp32 must take CuTe path
        # and match the pinned baseline bitwise)
        xf, wf = x.float(), w.float()
        scf, shf = sc.float(), sh.float()
        y_fb = sgl_ops.fused_norm_tanh_mul_add(xf, wf, None, scf, shf, "rms", EPS)
        y_fb_base = vendored.fused_norm_tanh_mul_add(xf, wf, None, scf, shf, "rms", EPS)
        assert torch.equal(y_fb, y_fb_base), "fp32 fallback diverged from pinned baseline"
        print(f"S={S} fallback (fp32 -> CuTe path): bitwise OK")

        # --- smoke benchmark: identical custom-op layers, alternating order
        def run_sgl():
            return sgl_ops.fused_norm_tanh_mul_add_norm_scale(
                x, w, None, sc, sh, w2, None, sc2, "rms", EPS)

        def run_base():
            return vendored.fused_norm_tanh_mul_add_norm_scale(
                x, w, None, sc, sh, w2, None, sc2, "rms", EPS)

        for _ in range(25):
            run_sgl()
            run_base()
        torch.cuda.synchronize()
        wall = {"sgl": [], "base": []}
        for i in range(100):
            order = (("sgl", run_sgl), ("base", run_base)) if i % 2 == 0 else (
                ("base", run_base), ("sgl", run_sgl))
            for tag, fn in order:
                t0 = time.perf_counter()
                fn()
                torch.cuda.synchronize()
                wall[tag].append((time.perf_counter() - t0) * 1e6)
        med_s = statistics.median(wall["sgl"])
        med_b = statistics.median(wall["base"])
        print(f"S={S} dual smoke (interleaved): sglang-native {med_s:.2f}us vs "
              f"pinned-baseline {med_b:.2f}us -> {med_b / med_s:.4f}x")
        assert med_s <= med_b * 1.02, "in-SGLang native path failed parity-or-speedup"

        # single-entry smoke
        def run_sgl_s():
            return sgl_ops.fused_norm_tanh_mul_add(x, w, None, sc, sh, "rms", EPS)

        def run_base_s():
            return vendored.fused_norm_tanh_mul_add(x, w, None, sc, sh, "rms", EPS)

        for _ in range(25):
            run_sgl_s()
            run_base_s()
        torch.cuda.synchronize()
        wall = {"sgl": [], "base": []}
        for i in range(100):
            order = (("sgl", run_sgl_s), ("base", run_base_s)) if i % 2 == 0 else (
                ("base", run_base_s), ("sgl", run_sgl_s))
            for tag, fn in order:
                t0 = time.perf_counter()
                fn()
                torch.cuda.synchronize()
                wall[tag].append((time.perf_counter() - t0) * 1e6)
        med_s = statistics.median(wall["sgl"])
        med_b = statistics.median(wall["base"])
        print(f"S={S} single smoke (interleaved): sglang-native {med_s:.2f}us vs "
              f"pinned-baseline {med_b:.2f}us -> {med_b / med_s:.4f}x")
        assert med_s <= med_b * 1.02, "in-SGLang native path failed parity-or-speedup"

    print("EXPORT ARBITER PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
