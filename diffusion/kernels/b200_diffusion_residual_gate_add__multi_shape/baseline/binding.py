"""Local baseline adapters reproducing the profiled PyTorch-eager elementwise
patterns, exposed through the same destination-passing ABI as the candidate.

Faithful baseline: the production callsites run
``out = residual + update * gate`` in eager mode, which the torch profiler shows
as a separate ``aten::mul`` then ``aten::add`` (two launches plus an
intermediate tensor). We reproduce exactly that two-op path, but write the
intermediate into a cached, preallocated scratch buffer (keyed by
shape/dtype/device) so the timed steady state contains only the two real kernel
launches and their memory traffic -- never a caching-allocator call. The 4D
broadcast add is a single eager ``torch.add`` (one launch).

No sglang import: these are pure torch ops reproducing the recovered semantics
(see docs/baseline_source.md). Output tensors are passed last and written
in-place; nothing is allocated in the timed path.
"""

from __future__ import annotations

import torch

# Cache of scratch buffers for the two-op residual-gate path, keyed by the
# (shape, dtype, device) of the `update * gate` intermediate (== update's shape).
_SCRATCH: dict[tuple, torch.Tensor] = {}


def _scratch_like(t: torch.Tensor) -> torch.Tensor:
    key = (tuple(t.shape), t.dtype, t.device)
    buf = _SCRATCH.get(key)
    if buf is None:
        buf = torch.empty(t.shape, dtype=t.dtype, device=t.device)
        _SCRATCH[key] = buf
    return buf


def residual_gate_add(residual: torch.Tensor, update: torch.Tensor,
                      gate: torch.Tensor, out: torch.Tensor) -> None:
    """out = residual + update * gate (faithful two-launch eager path)."""
    scratch = _scratch_like(update)
    torch.mul(update, gate, out=scratch)   # aten::mul  (broadcasts a [.,1,D] gate)
    torch.add(residual, scratch, out=out)  # aten::add


def broadcast_add_4d(a: torch.Tensor, b: torch.Tensor, out: torch.Tensor) -> None:
    """out = a + b, with a [B,1,P,D] broadcasting over b's sequence dim."""
    torch.add(a, b, out=out)
