"""Candidate entry point for the bench harness.

The candidate has two parts:
  - RMSNorm: reuse the torch.nn.RMSNorm modules passed in `inputs`, so the norm
            output is bit-identical to the oracle by construction.
  - split RoPE: a single fused bit-exact CUDA kernel (solution/kernel.cu) replaces
            the eager `split_x*cos` + two `addcmul_` ops, preserving the exact rounding.

`run_candidate(inputs, outputs)` validates the inputs on EVERY call (so in-place
mutation of an already-seen dict/list can never bypass the gate), raising
ValueError BEFORE RMSNorm or any kernel launch when anything is unsupported —
including wrong dtype/shape/stride/contiguity, a non-`torch.nn.RMSNorm` norm, or
any tensor that is not a CUDA tensor on q's device. This guarantees a malformed
input can never reach `solution/kernel.cu` (which would otherwise risk an illegal
or wrong-device memory access). Imports nothing from sglang.
"""

import sys
from pathlib import Path

import torch

_TASK_ROOT = Path(__file__).resolve().parents[1]
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))


# `msg` is a zero-arg callable so the (only-needed-on-failure) error string is NOT
# built on the success path. validate_candidate_inputs runs on every candidate
# call, so eagerly formatting ~25 f-strings each call was adding tens of µs of
# pure-CPU overhead to the benchmark's timed loop; deferring it keeps validation
# to cheap metadata checks.
def _require(cond, msg):
    if not cond:
        raise ValueError(f"unsupported candidate input: {msg()}")


def _require_cuda_on(name, t, dev):
    _require(torch.is_tensor(t), lambda: f"{name}: must be a tensor")
    _require(t.is_cuda and t.device == dev, lambda: f"{name}: must be a CUDA tensor on {dev}, got {t.device}")


def validate_candidate_inputs(inputs, outputs):
    """Reject any configuration the candidate does not support, BEFORE launching
    the kernel. O(1) metadata-only checks (dtype/shape/stride/contiguity/device/
    module attributes) — no GPU sync and no data reads. Validates both Q and K
    sides plus both output buffers; raises ValueError on the first unsupported
    property (per the source-prompt reject list). The expected device is q's
    device; every tensor (q, k, q/k cos, q/k sin, both norm weights, both outputs)
    must be a CUDA tensor on it.
    """
    _require(int(inputs.get("tp_world_size", 1)) == 1, lambda: "tensor-parallel world size must be 1")
    eps = float(inputs["eps"])
    num_heads = int(inputs["num_heads"])
    head_dim = int(inputs["head_dim"])
    _require(head_dim % 2 == 0, lambda: f"head_dim {head_dim} must be even")
    _require(len(outputs) == 2, lambda: f"expected 2 output tensors, got {len(outputs)}")
    half = head_dim // 2

    q = inputs["q"]
    _require(torch.is_tensor(q) and q.is_cuda, lambda: "q must be a CUDA tensor")
    dev = q.device  # the one expected CUDA device for this invocation

    sides = (
        ("q", q, inputs["q_cos"], inputs["q_sin"], inputs["q_norm"], outputs[0]),
        ("k", inputs["k"], inputs["k_cos"], inputs["k_sin"], inputs["k_norm"], outputs[1]),
    )
    for name, x, cos, sin, norm, out in sides:
        _require(torch.is_tensor(x) and x.dim() == 3, lambda: f"{name}: must be a 3-D tensor")
        b, s, hidden = x.shape
        _require(x.dtype == torch.bfloat16, lambda: f"{name}: dtype {x.dtype} != torch.bfloat16")
        _require_cuda_on(name, x, dev)
        _require(x.is_contiguous(), lambda: f"{name}: must be contiguous")
        _require(hidden == num_heads * head_dim,
                 lambda: f"{name}: hidden {hidden} != num_heads*head_dim {num_heads * head_dim}")

        # Exactly torch.nn.RMSNorm (a subclass overriding forward could produce a
        # post-norm tensor shape/dtype the kernel never re-validates).
        _require(type(norm) is torch.nn.RMSNorm,
                 lambda: f"{name}_norm: must be exactly torch.nn.RMSNorm, got {type(norm).__name__}")
        _require(tuple(norm.normalized_shape) == (hidden,),
                 lambda: f"{name}_norm: normalized_shape {tuple(norm.normalized_shape)} != ({hidden},)")
        _require(norm.eps is not None and float(norm.eps) == eps,
                 lambda: f"{name}_norm: eps {norm.eps} != {eps}")
        w = norm.weight
        _require(w is not None and w.dtype == torch.bfloat16,
                 lambda: f"{name}_norm: weight dtype {getattr(w, 'dtype', None)} != torch.bfloat16")
        _require_cuda_on(f"{name}_norm.weight", w, dev)

        for tname, t in ((f"{name}_cos", cos), (f"{name}_sin", sin)):
            _require(torch.is_tensor(t) and t.dim() == 4, lambda: f"{tname}: must be 4-D (split layout)")
            _require(t.dtype == torch.bfloat16, lambda: f"{tname}: dtype {t.dtype} != torch.bfloat16")
            _require_cuda_on(tname, t, dev)
            _require(t.stride(-1) == 1, lambda: f"{tname}: last-dim stride {t.stride(-1)} != 1")
            _require(tuple(t.shape) == (b, num_heads, s, half),
                     lambda: f"{tname}: shape {tuple(t.shape)} != {(b, num_heads, s, half)}")

        _require(torch.is_tensor(out) and out.dtype == torch.bfloat16,
                 lambda: f"{name}_out: dtype {getattr(out, 'dtype', None)} != torch.bfloat16")
        _require_cuda_on(f"{name}_out", out, dev)
        _require(out.is_contiguous(), lambda: f"{name}_out: must be contiguous")
        _require(tuple(out.shape) == (b, s, hidden), lambda: f"{name}_out: shape {tuple(out.shape)} != {(b, s, hidden)}")


def _module():
    from solution.build import load_candidate_module

    return load_candidate_module()


def run_candidate(inputs, outputs):
    # Validate on EVERY call: rejection must be guaranteed before any kernel launch
    # even if a caller mutates an already-used inputs dict / outputs list in place.
    # The checks are O(1) metadata-only; for a fair benchmark the validation is a
    # per-call safety gate (a production integration would hoist it to setup — the
    # pure-compute speedup measured without it is reported in docs/results.md).
    validate_candidate_inputs(inputs, outputs)
    # RMSNorm reused from the same torch modules the oracle uses (bit-exact).
    q_normed = inputs["q_norm"](inputs["q"])
    k_normed = inputs["k_norm"](inputs["k"])
    # Fused bit-exact split RoPE (custom CUDA kernel), destination-passing.
    mod = _module()
    mod.ltx2_split_rope_candidate(q_normed, inputs["q_cos"], inputs["q_sin"], outputs[0])
    mod.ltx2_split_rope_candidate(k_normed, inputs["k_cos"], inputs["k_sin"], outputs[1])
