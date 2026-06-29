"""Benchmark adapter for b200_ltx2_rms_adaln__bitwise.

Supplies tensor construction and the two ABI calls for bench/benchmark.py.
``call_baseline`` and ``call_candidate`` route through one shared dispatch over
pre-resolved function tables so both sides pay near-identical adapter overhead;
neither allocates output tensors (outputs are preallocated in ``make_case`` and
poisoned/timed by the benchmark template).

- Baseline: baseline/kernel.cu -> ATen eager (bit-identical to Python eager).
- Candidate: solution/kernel.cu -> at::rms_norm + fused modulation kernel.

The candidate is gate-routed in Python: in-gate inputs (the production rows)
ALWAYS exercise the optimized kernel (no silent masking of kernel bugs);
out-of-gate inputs take an explicit eager fallback (bit-exact). The raw kernel
itself fails closed (throws) on out-of-gate inputs -- see bench/correctness.py.

Bitwise comparison is supplied via the optional ``compare_outputs`` hook (raw
uint16/int storage equality + torch.equal); this overrides the benchmark
template's tolerance comparator because this task forbids tolerance.

No sglang import anywhere in this process (asserted below).
"""

from __future__ import annotations

import sys
from pathlib import Path

_TASK_ROOT = Path(__file__).resolve().parents[1]
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))

import torch

from baseline.build import load_baseline_module
from solution.build import load_candidate_module

assert not any(
    name == "sglang" or name.startswith("sglang.") for name in sys.modules
), "standalone contract violation: sglang imported at benchmark runtime"

_DTYPES = {
    "bfloat16": torch.bfloat16,
    "float16": torch.float16,
    "float32": torch.float32,
}

# Integer reinterpretation for raw-storage (byte-level) comparison.
_INT_VIEW = {
    torch.bfloat16: torch.uint16,
    torch.float16: torch.uint16,
    torch.float32: torch.int32,
}

_EP = "rms_adaln"

_baseline_module = load_baseline_module()
_candidate_module = load_candidate_module()

_BASELINE_FNS = {_EP: _baseline_module.ltx2_rms_adaln_baseline}
_CANDIDATE_FNS = {_EP: _candidate_module.ltx2_rms_adaln_candidate}


def _randn(shape, dtype, device):
    return torch.randn(shape, device=device, dtype=dtype)


def _validate_against_spec(name: str, tensor: torch.Tensor, spec: dict) -> None:
    if list(tensor.shape) != list(spec["shape"]):
        raise ValueError(
            f"{name}: constructed shape {tuple(tensor.shape)} != frozen spec {spec['shape']}"
        )
    want_stride = spec.get("stride")
    if want_stride is not None and list(tensor.stride()) != list(want_stride):
        raise ValueError(
            f"{name}: constructed stride {tuple(tensor.stride())} != frozen spec {want_stride}"
        )


def make_case(workload: dict, *, device: torch.device, seed: int) -> dict:
    del seed  # benchmark.py / correctness.py already seeded the generators
    shapes = workload["shapes"]
    x = _randn(shapes["x"]["shape"], _DTYPES[shapes["x"]["dtype"]], device)
    scale = _randn(shapes["scale"]["shape"], _DTYPES[shapes["scale"]["dtype"]], device)
    shift = _randn(shapes["shift"]["shape"], _DTYPES[shapes["shift"]["dtype"]], device)
    _validate_against_spec("x", x, shapes["x"])
    _validate_against_spec("scale", scale, shapes["scale"])
    _validate_against_spec("shift", shift, shapes["shift"])
    inputs = {
        "x": x,
        "scale": scale,
        "shift": shift,
        "eps": float(workload.get("eps", 1e-6)),
    }
    return {
        "inputs": inputs,
        "baseline_outputs": [torch.empty_like(x)],
        "candidate_outputs": [torch.empty_like(x)],
        "tolerance": {
            "atol": float(workload.get("atol", 0.0)),
            "rtol": float(workload.get("rtol", 0.0)),
        },
    }


# ---------------------------------------------------------------------------
# eager fallback + support gate (mirror solution/kernel.cu's gate exactly)
# ---------------------------------------------------------------------------


def eager_rms_adaln(x, scale, shift, eps):
    """The exact eager oracle, also used as the out-of-gate fallback.

    A 2D [B, D] scale/shift is per-(batch, channel) modulation broadcast over the
    sequence, i.e. semantically [B, 1, D] (matches the kernel's PERBATCH mode);
    PyTorch will not broadcast a bare [B, D] against [B, S, D], so unsqueeze it.
    [D], [B, 1, D], and [B, S, D] already broadcast directly.
    """
    normed = torch.nn.functional.rms_norm(x, (x.shape[-1],), eps=eps)
    s = scale.unsqueeze(-2) if scale.dim() == 2 else scale
    h = shift.unsqueeze(-2) if shift.dim() == 2 else shift
    return normed * (1 + s) + h


def layout_mode(mod: torch.Tensor, B: int, S: int, D: int):
    """Shape-based classifier mirroring solution/kernel.cu::classify_mode EXACTLY.

    Returns 'perchan' | 'perbatch' | 'full', or None if unsupported (so the
    public candidate routes the row to the eager fallback). Shape-based (not
    numel-based) to avoid misclassifying colliding shapes such as [S, D] when
    S == B. scale and shift are classified independently; the kernel reads each
    with its own broadcast base, so mixed supported layouts are accepted.
    """
    if not mod.is_cuda or mod.dtype != torch.bfloat16 or not mod.is_contiguous():
        return None
    shp = tuple(mod.shape)
    if shp == (D,):
        return "perchan"
    if shp == (B, D) or shp == (B, 1, D):
        return "perbatch"
    if shp == (B, S, D):
        return "full"
    return None


def in_gate(x, scale, shift) -> bool:
    """True iff the optimized kernel accepts x/scale/shift (mirrors the raw
    solution/kernel.cu gate for those inputs). The FULL optimized-path gate,
    including the output tensor and its aliasing policy, is optimized_in_gate()
    below; the public candidate uses that. Otherwise -> eager fallback.

    Requires all tensors on the same CUDA device; a CUDA x with a CPU or
    cross-device scale/shift must NOT enter the raw kernel (would hand host /
    wrong-device pointers to a CUDA launch).
    """
    if not x.is_cuda or x.dtype != torch.bfloat16:
        return False
    if x.dim() != 3 or not x.is_contiguous():
        return False
    if scale.device != x.device or shift.device != x.device:
        return False
    B, S, D = x.shape
    if D % 256 != 0 or D > 8192:
        return False
    # The optimized kernel issues 16-byte vector loads/stores; it requires every
    # vectorized base pointer (x / scale / shift; the output is checked in
    # optimized_in_gate) to be 16-byte aligned. A contiguous view with a nonzero
    # storage offset can be only bf16-aligned -> route such rows to the eager
    # fallback. This mirrors the raw kernel's alignment gate exactly.
    if x.data_ptr() % 16 != 0 or scale.data_ptr() % 16 != 0 or shift.data_ptr() % 16 != 0:
        return False
    return (layout_mode(scale, B, S, D) is not None
            and layout_mode(shift, B, S, D) is not None)


def _overlaps(a: torch.Tensor, b: torch.Tensor) -> bool:
    """True iff the storage byte ranges of a and b intersect on the same device
    (numel-based extent, matching the raw kernel's overlap check)."""
    if a.device != b.device:
        return False
    a0 = a.data_ptr()
    a1 = a0 + a.numel() * a.element_size()
    b0 = b.data_ptr()
    b1 = b0 + b.numel() * b.element_size()
    return a0 < b1 and b0 < a1


def optimized_in_gate(x, scale, shift, output) -> bool:
    """True iff the raw optimized kernel accepts (x, scale, shift, output) -- the
    EXACT mirror of solution/kernel.cu's fail-closed gate, INCLUDING the output
    checks and the aliasing policy. Otherwise the public candidate routes the row
    to the eager fallback.

    Output must be a same-device bf16 [B,S,D] contiguous, 16-byte-aligned buffer
    that does NOT overlap scale or shift (those overlaps would corrupt the kernel's
    vectorized reads, so the raw kernel rejects them). Output overlapping x IS
    allowed: x is fully consumed by at::rms_norm into a fresh `normed` buffer before
    the modulation kernel writes any output element.
    """
    if not in_gate(x, scale, shift):
        return False
    if not output.is_cuda or output.device != x.device:
        return False
    if output.dtype != torch.bfloat16:
        return False
    if list(output.shape) != list(x.shape) or not output.is_contiguous():
        return False
    if output.data_ptr() % 16 != 0:
        return False
    if _overlaps(output, scale) or _overlaps(output, shift):
        return False
    return True


def call_baseline(workload: dict, inputs, outputs) -> None:
    fn = _BASELINE_FNS[workload["function"]]
    fn(inputs["x"], inputs["scale"], inputs["shift"], inputs["eps"], outputs[0])


def call_candidate(workload: dict, inputs, outputs) -> None:
    x, scale, shift, eps = inputs["x"], inputs["scale"], inputs["shift"], inputs["eps"]
    # The optimized path runs only when the full raw-kernel gate accepts every
    # tensor (x/scale/shift AND output, incl. alignment and the scale/shift alias
    # rejection). Any other row takes the bit-exact eager fallback, which builds the
    # result in a fresh tensor before copying into output (safe even when output
    # aliases scale/shift); rows eager itself cannot compute raise a controlled error.
    if optimized_in_gate(x, scale, shift, outputs[0]):
        _CANDIDATE_FNS[workload["function"]](x, scale, shift, eps, outputs[0])
    else:
        outputs[0].copy_(eager_rms_adaln(x, scale, shift, eps))


# ---------------------------------------------------------------------------
# bitwise comparison hook (overrides the template's tolerance default)
# ---------------------------------------------------------------------------


def bitwise_equal(a: torch.Tensor, b: torch.Tensor) -> bool:
    if a.shape != b.shape or a.dtype != b.dtype:
        return False
    iv = _INT_VIEW.get(a.dtype)
    if iv is None:
        return bool(torch.equal(a, b))
    return bool(torch.equal(a.contiguous().view(iv), b.contiguous().view(iv)))


def compare_outputs(workload, baseline_outputs, candidate_outputs, tolerance):
    del tolerance  # this task forbids tolerance; bitwise only
    if len(baseline_outputs) != len(candidate_outputs):
        return {"ok": False, "max_abs": float("inf"), "max_rel": float("inf"),
                "message": "output count mismatch"}
    for i, (b, c) in enumerate(zip(baseline_outputs, candidate_outputs)):
        cf = c.float()
        if torch.isnan(cf).any() or torch.isinf(cf).any():
            return {"ok": False, "max_abs": float("inf"), "max_rel": float("inf"),
                    "message": f"output[{i}]: NaN/Inf in candidate"}
        if not bitwise_equal(b, c):
            diff = (cf - b.float()).abs()
            n = int((cf != b.float()).sum().item())
            return {"ok": False, "max_abs": float(diff.max().item()), "max_rel": 0.0,
                    "message": f"output[{i}]: not bitwise equal "
                               f"({n} elems differ, max_abs={diff.max().item():.3e})"}
    return {"ok": True, "max_abs": 0.0, "max_rel": 0.0, "message": "bitwise equal"}
