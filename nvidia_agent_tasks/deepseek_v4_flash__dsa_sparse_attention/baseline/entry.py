"""Baseline wrapper for `deepseek_v4_flash__dsa_sparse_attention`.

The harness (`tools/bench_harness.py`) calls `OPS[<op>](**row_args)`. Each entry loads
the symbol from the installed SGLang and checks its source hash against the copy in this
directory, so a drifted environment is reported instead of silently benchmarked - see
`tools/baseline_loader.py`.

Write `solution/entry.py` with the same `OPS` keys to have the harness A/B it.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
from baseline_loader import load  # noqa: E402

COPIED = {'sglang.kernels.ops.attention.dsv4.compress': 'kernels/ops/attention/dsv4/compress.py', 'sglang.kernels.ops.attention.dsv4.elementwise': 'kernels/ops/attention/dsv4/elementwise.py', 'deep_gemm': '', 'sglang.kernels.ops.attention.dsv4.topk': 'kernels/ops/attention/dsv4/topk.py', 'sgl_kernel.flash_mla': '', 'sglang.kernels.ops.attention.dsv4.attn': '', 'sglang.kernels.ops.layernorm.mhc': ''}


def _sym(module, attr):
    rel = COPIED.get(module, "")
    return load(module, attr, __file__, rel)


def _call(module, attr, kwargs):
    fn = _sym(module, attr)
    try:
        return fn(**kwargs)
    except TypeError as exc:
        raise RuntimeError(
            "%s.%s could not be called with the recorded arguments: %s\n"
            "The workload row carries only what the capture could serialize. Arguments that "
            "are large tensors (expert weights, KV pools) or non-tensor plan objects are "
            "recorded as metadata in bench/tensors/*/meta.json under 'metadata_only', with "
            "their shape/dtype/quantization flags - reconstruct them here, once, and the "
            "whole row set becomes runnable." % (module, attr, exc)) from exc


OPS = {
    "dsa_compress_forward":
        lambda **kw: _call("sglang.kernels.ops.attention.dsv4.compress", "compress_forward", kw),
    "dsa_compress_norm_rope_store":
        lambda **kw: _call("sglang.kernels.ops.attention.dsv4.compress", "compress_norm_rope_store", kw),
    "dsa_fused_q_indexer_rope_hadamard_quant":
        lambda **kw: _call("sglang.kernels.ops.attention.dsv4.elementwise", "fused_q_indexer_rope_hadamard_quant", kw),
    "dsa_indexer_logits_deepgemm_DEFAULT":
        lambda **kw: _call("deep_gemm", "fp8_paged_mqa_logits", kw),
    "dsa_topk_transform_v2":
        lambda **kw: _call("sglang.kernels.ops.attention.dsv4.topk", "topk_transform_512_v2", kw),
    "dsa_sparse_attention_flash_mla_alt":
        lambda **kw: _call("sgl_kernel.flash_mla", "flash_mla_sparse_fwd", kw),
    "dsa_paged_mqa_logits_metadata":
        lambda **kw: _call("sglang.kernels.ops.attention.dsv4.attn", "get_paged_mqa_logits_metadata", kw),
    "dsa_topk_transform":
        lambda **kw: _call("sglang.kernels.ops.attention.dsv4.topk", "topk_transform_512", kw),
    "mhc_pre_big_fuse_with_norm_tilelang":
        lambda **kw: _call("sglang.kernels.ops.layernorm.mhc", "mhc_pre_big_fuse_with_norm_tilelang", kw),
    "mhc_pre":
        lambda **kw: _call("sglang.kernels.ops.layernorm.mhc", "mhc_pre", kw),
    "mhc_post_tilelang":
        lambda **kw: _call("sglang.kernels.ops.layernorm.mhc", "mhc_post_tilelang", kw),
    "mhc_post":
        lambda **kw: _call("sglang.kernels.ops.layernorm.mhc", "mhc_post", kw),
}
