"""Benchmark adapter for b200_diffusion_residual_gate_add__multi_shape.

Supplies tensor construction and the two ABI calls for bench/benchmark.py.
``call_baseline`` and ``call_candidate`` route through one shared dispatch
helper over pre-resolved function tables, so both sides pay byte-identical
adapter overhead. Neither call allocates output tensors: outputs are
preallocated in ``make_case`` and poisoned/timed by the benchmark template.

The baseline side calls the faithful PyTorch-eager launchers in
baseline/binding.py; the candidate side calls the CUDA module built from
solution/kernel.cu via tvm-ffi. No sglang import anywhere in this process
(asserted below).
"""

from __future__ import annotations

import functools
import sys
from pathlib import Path

_TASK_ROOT = Path(__file__).resolve().parents[1]
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))

import torch

import baseline.binding as _baseline
from solution.build import load_candidate_module

assert not any(
    name == "sglang" or name.startswith("sglang.") for name in sys.modules
), "standalone contract violation: sglang imported at benchmark runtime"

_DTYPES = {
    "bfloat16": torch.bfloat16,
    "float16": torch.float16,
    "float32": torch.float32,
}

_EP_RGA = "residual_gate_add"
_EP_BCAST = "broadcast_add_4d"

_BASELINE_FNS = {
    _EP_RGA: _baseline.residual_gate_add,
    _EP_BCAST: _baseline.broadcast_add_4d,
}


@functools.lru_cache(maxsize=1)
def _candidate_fns() -> dict:
    # Build the candidate lazily (NOT at import): tvm-ffi's build queries the
    # current CUDA device for gencode/provenance, so it must run AFTER the caller
    # selects its target device (correctness.py / benchmark.py call
    # torch.cuda.set_device first). Importing this module therefore stays cheap
    # and device-independent.
    m = load_candidate_module()
    return {_EP_RGA: m.residual_gate_add, _EP_BCAST: m.broadcast_add_4d}


def _randn(shape, dtype, device):
    return torch.randn(shape, device=device, dtype=dtype)


def _validate_against_spec(name: str, tensor: torch.Tensor, spec: dict) -> None:
    """Fail before benchmarking if a constructed tensor diverges from the frozen
    workload metadata (shape/stride self-description)."""
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
    del seed  # benchmark.py already seeded the global generators
    assert_pinned_gpu(device)
    fn = workload["function"]
    shapes = workload["shapes"]

    if fn == _EP_RGA:
        residual = _randn(shapes["residual"]["shape"], _DTYPES[shapes["residual"]["dtype"]], device)
        update = _randn(shapes["update"]["shape"], _DTYPES[shapes["update"]["dtype"]], device)
        gate = _randn(shapes["gate"]["shape"], _DTYPES[shapes["gate"]["dtype"]], device)
        _validate_against_spec("residual", residual, shapes["residual"])
        _validate_against_spec("update", update, shapes["update"])
        _validate_against_spec("gate", gate, shapes["gate"])
        inputs = {"residual": residual, "update": update, "gate": gate}
        baseline_outputs = [torch.empty_like(residual)]
        candidate_outputs = [torch.empty_like(residual)]
    elif fn == _EP_BCAST:
        a = _randn(shapes["a"]["shape"], _DTYPES[shapes["a"]["dtype"]], device)
        b = _randn(shapes["b"]["shape"], _DTYPES[shapes["b"]["dtype"]], device)
        _validate_against_spec("a", a, shapes["a"])
        _validate_against_spec("b", b, shapes["b"])
        inputs = {"a": a, "b": b}
        baseline_outputs = [torch.empty_like(b)]
        candidate_outputs = [torch.empty_like(b)]
    else:
        raise ValueError(f"unknown function {fn!r}")

    return {
        "inputs": inputs,
        "baseline_outputs": baseline_outputs,
        "candidate_outputs": candidate_outputs,
        "tolerance": {"atol": float(workload["atol"]), "rtol": float(workload["rtol"])},
    }


_FLOAT_DTYPES = {torch.bfloat16, torch.float16, torch.float32}


def _validate(fn: str, inputs: dict, outputs) -> None:
    """Shared ABI contract enforced before either implementation runs, so the
    baseline (eager) and candidate (CUDA host checks) reject the same malformed
    inputs with identical adapter overhead. Mirrors solution/kernel.cu's host
    checks: CUDA device, shared float dtype, contiguous, out distinct from
    inputs, full [.,L,D] or same-rank row-broadcast [.,1,D] gate, B=1 4D add."""
    out = outputs[0]
    if fn == _EP_RGA:
        residual, update, gate = inputs["residual"], inputs["update"], inputs["gate"]
        tensors = (residual, update, gate, out)
        if not all(t.is_cuda for t in tensors):
            raise ValueError("residual/update/gate/out must be CUDA tensors")
        if residual.dim() < 2:
            raise ValueError("residual must be at least 2D ([.., D])")
        if update.shape != residual.shape or out.shape != residual.shape:
            raise ValueError("update/out shape must match residual")
        dt = residual.dtype
        if dt not in _FLOAT_DTYPES or any(t.dtype != dt for t in tensors):
            raise ValueError("residual/update/gate/out must share a float dtype (bf16/fp16/fp32)")
        if any(out.data_ptr() == t.data_ptr() for t in (residual, update, gate)):
            raise ValueError("out must not alias residual/update/gate")
        if not (residual.is_contiguous() and update.is_contiguous() and out.is_contiguous()):
            raise ValueError("residual/update/out must be contiguous")
        D = residual.shape[-1]
        if gate.shape[-1] != D:
            raise ValueError("gate last dim must equal residual last dim")
        if gate.shape == residual.shape:
            if not gate.is_contiguous():
                raise ValueError("full-shape gate must be contiguous")
            return  # full gate
        # row-broadcast: same rank, size-1 row dim, all leading dims == 1
        if gate.dim() != residual.dim() or gate.shape[-2] != 1 or any(
            s != 1 for s in gate.shape[:-1]
        ):
            raise ValueError("gate must be full [.., D] or same-rank row-broadcast [.., 1, D]")
        if not gate.is_contiguous():
            raise ValueError("broadcast gate must be contiguous")
    else:  # broadcast_add_4d
        a, b = inputs["a"], inputs["b"]
        tensors = (a, b, out)
        if not all(t.is_cuda for t in tensors):
            raise ValueError("a/b/out must be CUDA tensors")
        if a.dim() != 4 or b.dim() != 4:
            raise ValueError("broadcast_add_4d expects 4D a and b")
        if b.shape[0] != 1:
            raise ValueError("broadcast_add_4d supports batch size 1 only")
        if a.shape[0] != b.shape[0] or a.shape[1] != 1 or a.shape[2] != b.shape[2] or a.shape[3] != b.shape[3]:
            raise ValueError("a must be [1,1,P,D] broadcasting over dim1 of b")
        if out.shape != b.shape:
            raise ValueError("out shape must match b")
        dt = b.dtype
        if dt not in _FLOAT_DTYPES or any(t.dtype != dt for t in tensors):
            raise ValueError("a/b/out must share a float dtype (bf16/fp16/fp32)")
        if any(out.data_ptr() == t.data_ptr() for t in (a, b)):
            raise ValueError("out must not alias a/b")
        if not (a.is_contiguous() and b.is_contiguous() and out.is_contiguous()):
            raise ValueError("a/b/out must be contiguous")


def _dispatch(fns: dict, workload: dict, inputs: dict, outputs) -> None:
    fn = workload["function"]
    _validate(fn, inputs, outputs)
    impl = fns[fn]
    if fn == _EP_RGA:
        impl(inputs["residual"], inputs["update"], inputs["gate"], outputs[0])
    else:
        impl(inputs["a"], inputs["b"], outputs[0])


def call_baseline(workload: dict, inputs, outputs) -> None:
    _dispatch(_BASELINE_FNS, workload, inputs, outputs)


def call_candidate(workload: dict, inputs, outputs) -> None:
    _dispatch(_candidate_fns(), workload, inputs, outputs)


def assert_pinned_gpu(device: torch.device) -> None:
    """Fail-closed GPU-pinning guard for benchmark/profile runs. Enabled when
    KDA_REQUIRE_PINNED_GPU is set (remote benchmark mode): REMOTE_GPU_ID must be
    set and must be the sole visible CUDA device, so every measured number is
    attributable to one pinned GPU. No-op for local/dev correctness runs."""
    import os
    if not os.environ.get("KDA_REQUIRE_PINNED_GPU"):
        return
    pinned = (os.environ.get("REMOTE_GPU_ID") or "").strip()
    if not pinned:
        raise RuntimeError("REMOTE_GPU_ID must be set when KDA_REQUIRE_PINNED_GPU=1")
    visible = (os.environ.get("CUDA_VISIBLE_DEVICES") or "").strip()
    if visible != pinned:
        raise RuntimeError(
            f"pinned-GPU contract violated: CUDA_VISIBLE_DEVICES={visible!r} != REMOTE_GPU_ID={pinned!r}"
        )
    idx = device.index if getattr(device, "index", None) is not None else 0
    if idx != 0:
        raise RuntimeError(f"pinned GPU must be the sole visible device (cuda:0); got {device}")


def extra_provenance() -> dict:
    """Optional hook consumed by bench/benchmark.py to record the task-specific
    provenance the standalone contract requires beyond the template defaults:
    baseline commit, candidate source hash, TVM-FFI / NVCC versions, compile
    flags, and the pinned REMOTE_GPU_ID."""
    import hashlib
    import os
    import re
    import subprocess

    info: dict = {
        "task_slug": "b200_diffusion_residual_gate_add__multi_shape",
        "target_gpu": "NVIDIA B200",
        "remote_gpu_id": os.environ.get("REMOTE_GPU_ID"),
    }
    kernel = _TASK_ROOT / "solution" / "kernel.cu"
    if kernel.exists():
        info["candidate_kernel_sha256"] = hashlib.sha256(kernel.read_bytes()).hexdigest()
    doc = _TASK_ROOT / "docs" / "baseline_source.md"
    if doc.exists():
        m = re.search(r"Resolved commit SHA: `([0-9a-f]{7,40})`", doc.read_text())
        info["baseline_commit"] = m.group(1) if m else "unknown"
    try:
        import tvm_ffi
        info["tvm_ffi"] = getattr(tvm_ffi, "__version__", "unknown")
    except Exception:
        info["tvm_ffi"] = "unavailable"
    try:
        from solution.build import candidate_compile_flags
        info["candidate_compile_flags"] = candidate_compile_flags()
    except Exception:
        pass
    try:
        nv = subprocess.check_output(["nvcc", "--version"], text=True,
                                     stderr=subprocess.STDOUT, timeout=5)
        info["nvcc"] = nv.strip().splitlines()[-1]
    except Exception:
        info["nvcc"] = "unavailable"
    return info
