"""Candidate package: optimized CUDA kernels for the SGLang USPAttention
prefix head-slice / contiguous-copy / sequence-concat memory movement on B200,
exposed through the shared destination-passing ABI."""

from .binding import attention_concat_copy_candidate

__all__ = ["attention_concat_copy_candidate"]
