"""Task adapter for the standalone diffusion benchmark/correctness harness.

Required API (see bench/benchmark.py header):
    make_case(workload, *, device, seed) -> dict with keys
        inputs, baseline_outputs, candidate_outputs, tolerance
    call_baseline(workload, inputs, outputs) -> None
    call_candidate(workload, inputs, outputs) -> None
    compare_outputs(workload, baseline_outputs, candidate_outputs, tolerance) -> dict

Baseline = task-local SGLang production oracle (baseline/reference.py), including
the bf16 split-RoPE Triton fast path for live rows. Candidate = optimized kernel exposed by solution/
(built separately under solution/). Comparison is BIT-EXACT (torch.equal on an int16
bitcast); tolerances are forbidden. Imports nothing from sglang.
"""

import sys
from pathlib import Path

import torch

_TASK_ROOT = Path(__file__).resolve().parents[1]
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))

from baseline.reference import build_rms_norm, qknorm_split_rope_reference  # noqa: E402

_DTYPE = {
    "bfloat16": torch.bfloat16,
    "float16": torch.float16,
    "float32": torch.float32,
}

_TWO_PI = 6.283185307179586


def _production_autocast(device: torch.device):
    return torch.autocast(
        device_type=device.type,
        dtype=torch.bfloat16,
        enabled=device.type == "cuda",
    )


def _build_contiguous(shape, dtype, device, gen):
    return (
        torch.randn(tuple(shape), dtype=torch.float32, device=device, generator=gen)
        .to(dtype)
        .contiguous()
    )


def _build_cos_sin(b, num_heads, seq, half, dtype, device, gen):
    """Reproduce the production cos/sin layout: physically [B, S, H, half]
    contiguous, viewed [B, H, S, half] via transpose(1, 2) -> last-dim stride 1,
    head/seq strides swapped (non-contiguous), matching workloads.json strides.
    """
    angles = (
        torch.rand((b, seq, num_heads, half), dtype=torch.float32, device=device, generator=gen)
        * _TWO_PI
    )
    cos = torch.cos(angles).to(dtype).transpose(1, 2)
    sin = torch.sin(angles).to(dtype).transpose(1, 2)
    return cos, sin


def make_case(workload, *, device, seed):
    shapes = workload["shapes"]
    num_heads = int(workload["num_heads"])
    head_dim = int(workload["head_dim"])
    eps = float(workload.get("eps", 1e-6))
    half = head_dim // 2
    qd = _DTYPE[shapes["q"]["dtype"]]
    gen = torch.Generator(device=device).manual_seed(int(seed))

    q = _build_contiguous(shapes["q"]["shape"], qd, device, gen)
    k = _build_contiguous(shapes["k"]["shape"], qd, device, gen)
    b, s_q, hidden = q.shape
    _, s_k, _ = k.shape

    q_cos, q_sin = _build_cos_sin(b, num_heads, s_q, half, qd, device, gen)
    k_cos, k_sin = _build_cos_sin(b, num_heads, s_k, half, qd, device, gen)

    q_norm_weight = _build_contiguous((hidden,), qd, device, gen)
    k_norm_weight = _build_contiguous((hidden,), qd, device, gen)
    q_norm = build_rms_norm(q_norm_weight, eps)
    k_norm = build_rms_norm(k_norm_weight, eps)

    inputs = {
        "q": q, "k": k,
        "q_cos": q_cos, "q_sin": q_sin, "k_cos": k_cos, "k_sin": k_sin,
        "q_norm": q_norm, "k_norm": k_norm,
        "q_norm_weight": q_norm_weight, "k_norm_weight": k_norm_weight,
        "eps": eps, "num_heads": num_heads, "head_dim": head_dim,
    }
    return {
        "inputs": inputs,
        "baseline_outputs": [torch.empty_like(q), torch.empty_like(k)],
        "candidate_outputs": [torch.empty_like(q), torch.empty_like(k)],
        "tolerance": {"atol": 0.0, "rtol": 0.0},
    }


def call_baseline(workload, inputs, outputs):
    with _production_autocast(inputs["q"].device):
        q_out, k_out = qknorm_split_rope_reference(
            inputs["q"], inputs["k"], inputs["q_norm"], inputs["k_norm"],
            (inputs["q_cos"], inputs["q_sin"]), (inputs["k_cos"], inputs["k_sin"]),
        )
    outputs[0].copy_(q_out)
    outputs[1].copy_(k_out)


_CANDIDATE_FN = None


def _load_candidate():
    global _CANDIDATE_FN
    if _CANDIDATE_FN is not None:
        return _CANDIDATE_FN
    try:
        from solution.candidate import run_candidate  # type: ignore
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(
            "solution candidate not available yet. Build the "
            "candidate kernel under solution/ and expose run_candidate(inputs, outputs) "
            f"writing q_out/k_out into outputs[0]/outputs[1]. Import error: {exc}"
        ) from exc
    _CANDIDATE_FN = run_candidate
    return _CANDIDATE_FN


def call_candidate(workload, inputs, outputs):
    with _production_autocast(inputs["q"].device):
        _load_candidate()(inputs, outputs)


def compare_outputs(workload, baseline_outputs, candidate_outputs, tolerance):
    base = baseline_outputs if isinstance(baseline_outputs, (list, tuple)) else [baseline_outputs]
    cand = candidate_outputs if isinstance(candidate_outputs, (list, tuple)) else [candidate_outputs]
    if len(base) != len(cand):
        return {"ok": False, "message": f"output count mismatch {len(base)} vs {len(cand)}"}
    for i, (a, b) in enumerate(zip(base, cand)):
        if a.shape != b.shape:
            return {"ok": False, "message": f"output {i} shape {tuple(a.shape)} vs {tuple(b.shape)}"}
        if a.dtype != b.dtype:
            return {"ok": False, "message": f"output {i} dtype {a.dtype} vs {b.dtype}"}
        # Strict bit-equality: bitcast to a same-width integer (bf16/fp16 -> int16)
        # so -0.0 vs 0.0 and NaN bit patterns are compared exactly. No tolerance.
        a_i = a.contiguous().view(torch.int16)
        b_i = b.contiguous().view(torch.int16)
        if not torch.equal(a_i, b_i):
            mism = int((a_i != b_i).sum().item())
            return {
                "ok": False, "max_abs": float("inf"), "max_rel": float("inf"),
                "message": f"output {i} not bit-equal: {mism} mismatched bf16 elements",
            }
    return {"ok": True, "max_abs": 0.0, "max_rel": 0.0, "message": "bit-equal (torch.equal int16 bitcast)"}
