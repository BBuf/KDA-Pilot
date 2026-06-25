"""Local baseline package: faithful PyTorch/ATen reproduction of the SGLang
USPAttention prefix head-slice / contiguous-copy / sequence-concat memory
movement, exposed through the shared destination-passing ABI.

See ``docs/baseline_source.md`` for upstream provenance.
"""

from .binding import (
    OP_COPY_CONTIGUOUS,
    OP_CONCAT_SEQUENCE,
    OP_SLICE_HEADS_THEN_CONCAT,
    ORDER_AB,
    ORDER_BA,
    attention_concat_copy_baseline,
)

__all__ = [
    "OP_COPY_CONTIGUOUS",
    "OP_CONCAT_SEQUENCE",
    "OP_SLICE_HEADS_THEN_CONCAT",
    "ORDER_AB",
    "ORDER_BA",
    "attention_concat_copy_baseline",
]
