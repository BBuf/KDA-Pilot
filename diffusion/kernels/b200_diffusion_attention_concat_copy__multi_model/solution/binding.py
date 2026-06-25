"""Python wrapper exposing the candidate CUDA kernel through the shared
destination-passing ABI (identical positional signature to
baseline/binding.py::attention_concat_copy_baseline).

The tvm-ffi module is built/loaded lazily on first call (lru_cached in
solution/build.py) so importing this module off-GPU does not trigger a build.
"""

from __future__ import annotations

import functools
from typing import Optional

import torch

from .build import load_candidate_module


@functools.lru_cache(maxsize=None)
def _candidate_fn():
    return load_candidate_module().attention_concat_copy_candidate


def attention_concat_copy_candidate(
    op_type: int,
    order: int,
    h_start: int,
    h_local: int,
    source_a: torch.Tensor,
    source_b: Optional[torch.Tensor],
    scratch: Optional[torch.Tensor],
    output: torch.Tensor,
) -> torch.Tensor:
    # source_b / scratch may be None (Optional<TensorView>); the candidate ignores scratch.
    _candidate_fn()(int(op_type), int(order), int(h_start), int(h_local),
                    source_a, source_b, scratch, output)
    return output
