#!/usr/bin/env python3
"""Two-process behavioral parity: vendored snapshot vs real SGLang at the pinned commit.

Run once with ``--side real`` under ``PYTHONPATH=<sglang_checkout>/python`` (the
checkout must be at the commit recorded in docs/baseline_source.md), then with
``--side snapshot`` in a fresh process (no SGLang on the path). The snapshot run
loads the real run's outputs and requires bitwise equality (identical code,
identical device, fixed seeds).

One representative signature per dispatch bucket family keeps the check fast.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

import torch

BENCH_DIR = Path(__file__).resolve().parent
TASK_DIR = BENCH_DIR.parent

# (name, function, S, D, x_dtype, gate spec, wb dtype, scale/shift (layout, dtype))
BF16, FP32 = torch.bfloat16, torch.float32
CASES = [
    ("nss_row_bf16", "nss", 256, 3072, BF16, None, None, ("11D", BF16)),
    ("nss_row_fp32", "nss", 256, 5120, BF16, None, None, ("11D", FP32)),
    ("nss_token_bf16", "nss", 256, 5120, BF16, None, None, ("1SD", BF16)),
    ("nss_token_fp32", "nss", 256, 3072, BF16, None, None, ("1SD", FP32)),
    ("srnss_grow_bf16", "srnss", 256, 3072, BF16, ("11D", BF16), None, ("1D", BF16)),
    ("srnss_gnone_bf16", "srnss", 256, 5120, BF16, None, None, ("11D", BF16)),
    ("srnss_gnone_row_fp32", "srnss", 256, 5120, BF16, None, None, ("11D", FP32)),
    ("srnss_gnone_token_fp32", "srnss", 256, 3072, BF16, None, None, ("1SD", FP32)),
    ("srnss_grow_fp32_wb", "srnss", 256, 5120, BF16, ("11D", FP32), FP32, ("1", BF16)),
    ("srnss_gtoken_fp32_wb", "srnss", 256, 3072, BF16, ("1SD", FP32), FP32, ("1", BF16)),
]


def _shape(layout: str, S: int, D: int) -> tuple[int, ...]:
    return {"1": (1,), "1D": (1, D), "11D": (1, 1, D), "1SD": (1, S, D)}[layout]


def build_inputs(case, device):
    name, function, S, D, x_dt, gate_spec, wb_dt, (ss_layout, ss_dt) = case
    seed = int.from_bytes(name.encode()[-2:], "little") + 77
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    x = torch.randn(1, S, D, dtype=x_dt, device=device)
    scale = torch.randn(_shape(ss_layout, S, D), dtype=ss_dt, device=device)
    shift = torch.randn(_shape(ss_layout, S, D), dtype=ss_dt, device=device)
    weight = torch.randn(D, dtype=wb_dt, device=device) if wb_dt else None
    bias = torch.randn(D, dtype=wb_dt, device=device) if wb_dt else None
    out = {"x": x, "weight": weight, "bias": bias, "scale": scale, "shift": shift,
           "norm_type": "layer", "eps": 1e-6}
    if function == "srnss":
        out["residual"] = torch.randn_like(x)
        out["gate"] = (
            torch.randn(_shape(gate_spec[0], S, D), dtype=gate_spec[1], device=device)
            if gate_spec else None
        )
    return out


def get_entry_points(side: str):
    if side == "real":
        module = importlib.import_module(
            "sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift"
        )
        marker = getattr(sys.modules.get("sglang"), "_kda_snapshot_root", None)
        if marker is not None:
            raise SystemExit("real-side run resolved the snapshot alias, not an SGLang checkout")
        return module.fused_norm_scale_shift, module.fused_scale_residual_norm_scale_shift
    spec = importlib.util.spec_from_file_location(
        "kda_baseline_binding", TASK_DIR / "baseline" / "binding.py"
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["kda_baseline_binding"] = mod
    spec.loader.exec_module(mod)
    return mod.fused_norm_scale_shift, mod.fused_scale_residual_norm_scale_shift


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--side", choices=["real", "snapshot"], required=True)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--artifact", type=Path, required=True)
    args = parser.parse_args()

    device = torch.device(args.device)
    torch.cuda.set_device(device)
    torch.set_grad_enabled(False)
    nss, srnss = get_entry_points(args.side)

    outputs = {}
    for case in CASES:
        name, function = case[0], case[1]
        inputs = build_inputs(case, device)
        if function == "nss":
            y = nss(inputs["x"], inputs["weight"], inputs["bias"], inputs["scale"],
                    inputs["shift"], inputs["norm_type"], inputs["eps"])
            outputs[name] = {"y": y.cpu()}
        else:
            y, res = srnss(inputs["residual"], inputs["x"], inputs["gate"],
                           inputs["weight"], inputs["bias"], inputs["scale"],
                           inputs["shift"], inputs["norm_type"], inputs["eps"])
            outputs[name] = {"y": y.cpu(), "res_out": res.cpu()}
        torch.cuda.synchronize()

    if args.side == "real":
        torch.save(outputs, args.artifact)
        print(f"real-side outputs saved: {len(outputs)} cases -> {args.artifact}")
        return 0

    reference = torch.load(args.artifact, weights_only=True)
    mismatches = []
    for name, outs in outputs.items():
        for key, tensor in outs.items():
            if not torch.equal(tensor, reference[name][key]):
                mismatches.append(f"{name}.{key}")
    if mismatches:
        print("PARITY FAIL:", ", ".join(mismatches))
        return 1
    print(f"PARITY OK: {len(outputs)} cases bitwise-identical (snapshot vs real sglang)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
