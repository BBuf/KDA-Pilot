#!/usr/bin/env python3
"""One-time equivalence check: vendored baseline/ vs the LIVE SGLang Triton module.

This is the single sanctioned live-SGLang import in the harness suite: it
certifies that the copy in baseline/ behaves identically to
sglang.jit_kernel.diffusion.triton.scale_shift, then the copy is frozen and
all later runs use baseline/ only.

Expectation: bit-identical outputs (same Triton source compiled in the same
process). The elementwise kernels are reduction-free, and the LN kernels use a
fixed BLOCK_N, so even autotune cannot change numerics.

Usage (inside the remote container):
  python bench/equivalence_check.py --sglang-python /home/sglang-omni/bbuf/repos/sglang/python \
      --json /path/to/report.json
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import subprocess
import sys
from pathlib import Path

KERNEL_DIR = Path(__file__).resolve().parents[1]
if str(KERNEL_DIR) not in sys.path:
    sys.path.insert(0, str(KERNEL_DIR))

import torch  # noqa: E402

from baseline import scale_shift as vendored  # noqa: E402
from bench import cases as cases_mod  # noqa: E402


def _as_tuple(out):
    return out if isinstance(out, tuple) else (out,)


def _pick_cases():
    cases = list(cases_mod.production_cases())
    grid = {c.case_id: c for c in cases_mod.grid_cases()}
    extra_ids = [
        # layout/dtype coverage beyond production: fp16/fp32, 4D, scalar,
        # broadcastable-3D, bool/int64 index select01, affine weights.
        "grid_ss_fp16_B2L128C512_frame4d_c1",
        "grid_ss_fp32_B1L33C1024_scalar_c0",
        "grid_ss_fp32_B4L257C3072_rowwise_bc_c1",
        "grid_ss_bf16_B2L128C512_b1c_c0",
        "grid_select01_fp32_B2L33C512_aff",
        "grid_residual_select01_fp16_B1L128C1536_aff",
    ]
    for cid in extra_ids:
        if cid in grid:
            cases.append(grid[cid])
    return cases


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sglang-python", required=True,
                    help="path to <sglang checkout>/python")
    ap.add_argument("--json", default="")
    args = ap.parse_args()

    if not torch.cuda.is_available():
        print("ERROR: CUDA required", file=sys.stderr)
        return 2

    sys.path.insert(0, args.sglang_python)
    live_mod = importlib.import_module("sglang.jit_kernel.diffusion.triton.scale_shift")
    live_file = Path(live_mod.__file__)
    live_md5 = hashlib.md5(live_file.read_bytes()).hexdigest()
    try:
        commit = subprocess.run(
            ["git", "-C", str(live_file.parent), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:  # noqa: BLE001
        commit = "unknown"

    pairs = {
        cases_mod.OP_SCALE_SHIFT: (
            vendored.fuse_scale_shift_kernel, live_mod.fuse_scale_shift_kernel),
        cases_mod.OP_SELECT01: (
            vendored.fuse_layernorm_scale_shift_gate_select01_kernel,
            live_mod.fuse_layernorm_scale_shift_gate_select01_kernel),
        cases_mod.OP_RESIDUAL: (
            vendored.fuse_residual_layernorm_scale_shift_gate_select01_kernel,
            live_mod.fuse_residual_layernorm_scale_shift_gate_select01_kernel),
    }

    device = torch.device("cuda")
    results, n_bitexact, n_fail = [], 0, 0
    for case in _pick_cases():
        v_fn, l_fn = pairs[case.op]
        args_t, kwargs_t = case.build(device)
        v_out = _as_tuple(v_fn(*args_t, **kwargs_t))
        l_out = _as_tuple(l_fn(*args_t, **kwargs_t))
        bit = all(torch.equal(a, b) for a, b in zip(v_out, l_out))
        rec = {"case_id": case.case_id, "bit_identical": bit}
        if bit:
            n_bitexact += 1
        else:
            maxdiff = max(
                (a.float() - b.float()).abs().max().item()
                for a, b in zip(v_out, l_out)
            )
            rec["max_abs_diff"] = maxdiff
            if maxdiff > 0.0:
                n_fail += 1
                rec["status"] = "MISMATCH"
        results.append(rec)
        print(f"  {'OK ' if bit else 'DIFF'} {case.case_id}")

    summary = {
        "vendored_file": str(KERNEL_DIR / "baseline" / "scale_shift.py"),
        "live_file": str(live_file),
        "live_md5": live_md5,
        "live_sglang_commit": commit,
        "device": torch.cuda.get_device_name(device),
        "torch": torch.__version__,
        "cases": len(results),
        "bit_identical": n_bitexact,
        "mismatches": n_fail,
        "verdict": "EQUIVALENT" if n_fail == 0 else "MISMATCH",
    }
    print(json.dumps(summary, indent=2))
    if args.json:
        Path(args.json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.json).write_text(json.dumps({"summary": summary, "results": results}, indent=1))
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
