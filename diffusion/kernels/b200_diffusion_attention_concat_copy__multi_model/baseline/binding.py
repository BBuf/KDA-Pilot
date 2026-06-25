"""Local destination-passing baseline ABI for the attention concat/copy/slice task.

Reproduces the upstream SGLang ``USPAttention`` PyTorch memory movement
(``tensor[:, :, h_start:h_end, :].contiguous()`` + ``torch.cat(..., dim=1)`` +
contiguous copy) WITHOUT importing SGLang. See ``docs/baseline_source.md`` for
provenance and ``docs/benchmark_method.md`` for the ABI and the ``config.toml``
baseline-entry override.

This is the headline-speedup baseline: it calls ATen ops directly (the same
``copy_`` / ``CatArrayBatchedCopy`` kernels PyTorch dispatches in production),
with preallocated ``output`` and prefix ``scratch`` so no allocation happens in
the timed path. The candidate in ``solution/`` is driven through the identical
ABI signature (see ``OP_*`` / ``ORDER_*`` below).
"""

from __future__ import annotations

from typing import Optional

import torch

# --- op_type selector (shared verbatim with solution/kernel.cu and bench/adapter.py) ---
OP_COPY_CONTIGUOUS = 0
OP_CONCAT_SEQUENCE = 1
OP_SLICE_HEADS_THEN_CONCAT = 2

# --- source order selector (sequence-dim concat order) ---
ORDER_AB = 0  # [source_a, source_b]  (prefix-first / a-first; prefix models, e.g. FLUX.2)
ORDER_BA = 1  # [source_b, source_a]  (shard-first; suffix models, e.g. JoyAI)


def attention_concat_copy_baseline(
    op_type: int,
    order: int,
    h_start: int,
    h_local: int,
    source_a: torch.Tensor,
    source_b: Optional[torch.Tensor],
    scratch: Optional[torch.Tensor],
    output: torch.Tensor,
) -> torch.Tensor:
    """Faithful PyTorch/ATen reproduction of the USPAttention memory movement.

    Args mirror the candidate ABI exactly (destination passing, ``output`` last):
      - ``op_type``  : one of ``OP_*``.
      - ``order``    : one of ``ORDER_*`` (concat order on the sequence dim).
      - ``h_start``  : head-slice start (``sp_rank * h_local``); ignored unless slice op.
      - ``h_local``  : local head count to keep from the full-head prefix; ignored unless slice op.
      - ``source_a`` : primary source. copy: the (non-contiguous) source; concat: tensor A;
                       slice: the full-head prefix ``[B, P, h_full, D]``.
      - ``source_b`` : secondary source. concat: tensor B; slice: the shard ``[B, S, h_local, D]``.
                       Unused (may be ``None``) for copy.
      - ``scratch``  : preallocated buffer for the intermediate prefix-slice ``.contiguous()``
                       materialization. Used only by the slice op; ``None`` otherwise.
      - ``output``   : preallocated destination, written in place.
    """
    op_type = int(op_type)
    order = int(order)
    h_start = int(h_start)
    h_local = int(h_local)

    if op_type == OP_COPY_CONTIGUOUS:
        # upstream: x.contiguous() on a non-contiguous (head-sliced) view.
        # copy_ materializes the strided source into the preallocated contiguous output.
        output.copy_(source_a)
        return output

    if op_type == OP_CONCAT_SEQUENCE:
        # upstream: torch.cat([a, b], dim=1) of equal-head tensors on the sequence dim.
        if source_b is None:
            raise ValueError("concat_sequence requires source_b")
        if order == ORDER_AB:
            torch.cat([source_a, source_b], dim=1, out=output)
        elif order == ORDER_BA:
            torch.cat([source_b, source_a], dim=1, out=output)
        else:
            raise ValueError(f"unknown order={order}")
        return output

    if op_type == OP_SLICE_HEADS_THEN_CONCAT:
        # upstream: torch.cat([prefix[:, :, h_start:h_end, :].contiguous(), shard], dim=1)
        # Two-stage, matching the real source: (1) materialize the head-sliced prefix into
        # preallocated scratch; (2) concat scratch + shard into the preallocated output.
        if source_b is None:
            raise ValueError("slice_heads_then_concat requires source_b (the shard)")
        if scratch is None:
            raise ValueError("slice_heads_then_concat requires preallocated scratch")
        prefix = source_a
        shard = source_b
        h_end = h_start + h_local
        sliced = prefix[:, :, h_start:h_end, :]  # non-contiguous view over the heads dim
        scratch.copy_(sliced)  # contiguous materialization into preallocated scratch
        if order == ORDER_AB:
            torch.cat([scratch, shard], dim=1, out=output)
        elif order == ORDER_BA:
            torch.cat([shard, scratch], dim=1, out=output)
        else:
            raise ValueError(f"unknown order={order}")
        return output

    raise ValueError(f"unknown op_type={op_type}")
