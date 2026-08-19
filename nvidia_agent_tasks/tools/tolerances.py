"""Per-op tolerances, taken from SGLang's own tests - not invented here.

Every entry cites the test file and line it came from, at the commit these tasks were
captured against (`main @ 43226af`). If a kernel's tolerance is wrong, the fix is to
change SGLang's test and re-copy the number here, not to loosen it in a task.

`get(op, dtype)` -> {"rtol", "atol", "source", "note"}.  Ops whose gate is not a
numeric comparison at all (bit-exact, index-set) are marked `exact: True`.
"""

from __future__ import annotations

# --------------------------------------------------------------------------- #
# family -> tolerance, with the SGLang test it is copied from
# --------------------------------------------------------------------------- #
TOLERANCES = {
    # ---- Mamba-2 / conv1d --------------------------------------------------
    "causal_conv1d": {
        "bfloat16": (1e-2, 5e-2), "float16": (3e-3, 5e-3), "float32": (3e-4, 1e-3),
        "source": "test/registered/layers/mamba/test_causal_conv1d.py:163-165",
        "note": "bf16 branch is the one these rows hit (silu activation)."},
    "mamba2_ssd": {
        "bfloat16": (5e-2, 5e-2), "float32": (5e-3, 8e-3),
        "source": "test/registered/layers/mamba/test_mamba_ssm_ssd.py:244-248",
        "note": ("SGLang's own comment: 'the bfloat16 case requires higher thresholds, "
                 "to be investigated'. Long sequences use 5e-3/1e-2 at line 340-343.")},
    "sconv_cache": {
        "bfloat16": (2e-2, 2e-2),
        "source": "test/registered/kernels/ops/mamba/test_sconv_cache.py:164"},

    # ---- linear attention (GDN / KDA) --------------------------------------
    "gdn_chunk": {
        "bfloat16": (1e-2, 2e-2),
        "source": "test/registered/attention/test_chunk_gated_delta_rule.py:28-29"},
    "kda_decode": {
        "bfloat16": (2e-2, 2e-2),
        "source": "test/registered/kernels/ops/attention/test_kda_fused_decode.py:207-208",
        "note": ("the same test asserts the conv state with rtol=0, atol=0 (line 209) - "
                 "the conv half is exact, only the SSM half carries tolerance.")},
    "kda_mtp_ring": {
        "bfloat16": (2e-2, 3e-2),
        "source": "test/registered/kernels/test_kda_mtp_cutedsl_replayssm_ring.py:177"},

    # ---- attention ---------------------------------------------------------
    "triton_attention": {
        "bfloat16": (1e-2, 1e-3),
        "source": "test/registered/attention/test_triton_attention_kernels.py:309",
        "note": ("the same file uses 1e-2/2e-2 for the split-kv comparison at line 401; "
                 "we take the tighter extend/decode number.")},
    "attention_splitkv": {
        "bfloat16": (1e-2, 2e-2), "float8_e4m3fn": (2e-2, 8e-2),
        "source": "test/registered/attention/test_verify_splitkv.py:40-41 and "
                  "test_verify_shared_kv.py:19-22"},

    # ---- MoE ---------------------------------------------------------------
    "triton_fused_moe": {
        "bfloat16": (1e-5, 1e-5), "float16": (1e-5, 1e-5), "float32": (1e-5, 1e-5),
        "source": "test/registered/moe/test_triton_fused_moe.py:45-49",
        "note": ("SGLang compares the fused MoE against a torch-naive MoE at 1e-5; the "
                 "LoRA MoE kernel test uses 1e-2/1e-2 (test_fused_moe_lora_kernel.py:378) "
                 "for a fused-vs-fused comparison.")},

    # ---- GEMM --------------------------------------------------------------
    "cutedsl_bf16_gemm": {
        "bfloat16": (2e-2, 2.5),
        "source": "test/registered/kernels/ops/gemm/test_cutedsl_bf16_gemm.py:53",
        "note": ("atol is large because the reference is an fp32 matmul cast to bf16; "
                 "the accumulation order differs, so absolute error scales with K.")},
    "tiny_gemm": {
        "bfloat16": (1e-3, 1e-3),
        "source": "test/registered/kernels/ops/test_kimi_k3_prerequisite_ops.py:385-386",
        "note": "compared in double precision against x @ w.T."},

    # ---- NVFP4 / FP8 on sm_120 (Qwen3.8-27B) --------------------------------
    "nvfp4_gemm": {
        "bfloat16": (1e-2, 2e-2),
        "source": "test/registered/attention/test_chunk_gated_delta_rule.py:28-29",
        "note": ("SGLang ships no dedicated mm_fp4 test; this is the same fallback "
                 "tolerance its linear-attention tests use for a bf16 output built "
                 "from a low-precision accumulation.")},
    "fp8_linear": {
        "bfloat16": (2e-2, 1.0),
        "source": "test/registered/kernels/ops/gemm/test_fp8_blockwise_gemm.py:73-75",
        "note": ("atol is 1.0 because the reference is an fp32 matmul cast to bf16: "
                 "absolute error scales with K, which is 5120-16384 on these rows.")},

    # ---- exact gates -------------------------------------------------------
    "dsa_index_transform": {
        "exact": True,
        "source": "test/registered/kernels/ops/attention/test_dsa_transform_index.py:120",
        "note": "rtol=0, atol=0 - an index transform is exact or it is wrong."},
    "packed_bytes": {
        "exact": True,
        "source": "test/registered/moe/test_triton_fused_moe.py:45-49",
        "note": ("A quantizer's outputs are packed nibbles and e4m3 scale blocks, and a "
                 "split/reshape/cat only moves bytes: any difference is a different "
                 "encoding, not rounding. Bit-exact or wrong.")},
    "diffusion_conv3d_cat_pad": {
        "exact": True,
        "source": "test/registered/kernels/ops/diffusion/test_causal_conv3d_cat_pad.py:73"},
}

# --------------------------------------------------------------------------- #
# op -> family
# --------------------------------------------------------------------------- #
OP_FAMILY = {
    # nemotron3_nano__mamba2_ssm
    "causal_conv1d_prefill": "causal_conv1d",
    "causal_conv1d_decode": "causal_conv1d",
    "gdn_decode_causal_conv1d_update": "causal_conv1d",
    "mamba2_chunk_scan_combined_fwd": "mamba2_ssd",
    "mamba2_chunk_scan_combined": "mamba2_ssd",
    "mamba2_chunk_scan": "mamba2_ssd",
    "mamba2_chunk_state": "mamba2_ssd",
    "mamba2_chunk_state_varlen": "mamba2_ssd",
    "mamba2_chunk_cumsum": "mamba2_ssd",
    "mamba2_state_passing": "mamba2_ssd",
    # qwen3_next__gdn_chunk_prefill
    "gdn_chunk_prefill": "gdn_chunk",
    "gdn_chunk_delta_h": "gdn_chunk",
    "gdn_chunk_o": "gdn_chunk",
    "gdn_recompute_w_u": "gdn_chunk",
    "gdn_gating": "gdn_chunk",
    "gdn_decode_packed_triton": "kda_decode",
    # kimi_k3__kda_linear_attention
    "k3_kda_fused_decode": "kda_decode",
    "k3_kda_packed_decode": "kda_decode",
    "k3_kda_chunk_prefill": "gdn_chunk",
    # glm47_flash__triton_attention
    "triton_decode_attention": "triton_attention",
    "triton_decode_attention_grouped": "triton_attention",
    "triton_extend_attention": "triton_attention",
    # lfm25__triton_fused_moe
    "triton_fused_moe_gemm": "triton_fused_moe",
    # glm45__fp8_fused_moe - the FP8 arm of the same kernel plus its dispatch level
    "moe_fused_experts_fp8": "triton_fused_moe",
    "triton_moe_act_and_mul": "triton_fused_moe",
    "triton_moe_sum_reduce": "triton_fused_moe",
    "moe_align_block_size": "dsa_index_transform",     # a permutation: exact
    # kimi_k3__tgv_bf16_tiny_gemm
    "k3_cutedsl_tgv_bf16_gemm": "cutedsl_bf16_gemm",
    "k3_cutedsl_tgv_bf16_gemm_out": "cutedsl_bf16_gemm",
    "k3_tiny_gemm": "tiny_gemm",
    "k3_tiny_n_gemm_bf16": "tiny_gemm",
    "k3_tiny_k_gemm_bf16": "tiny_gemm",
    # deepseek_v4_flash__dsa_sparse_attention
    "dsa_topk_transform": "dsa_index_transform",
    "dsa_topk_transform_v2": "dsa_index_transform",
    "dsa_sparse_attention_flash_mla_alt": "attention_splitkv",
    "dsa_indexer_logits_deepgemm_DEFAULT": "attention_splitkv",
    "dsa_compress_forward": "attention_splitkv",
    "dsa_compress_norm_rope_store": "attention_splitkv",
    "dsa_fused_q_indexer_rope_hadamard_quant": "attention_splitkv",
    "dsa_paged_mqa_logits_metadata": "dsa_index_transform",
    "mhc_pre": "triton_attention",
    "mhc_post": "triton_attention",
    "mhc_pre_big_fuse_with_norm_tilelang": "triton_attention",
    "mhc_post_tilelang": "triton_attention",
    # minimax_h3__sm103_block_sparse_attention (dense reference arm)
    "diffusion_attention_cudnn_sdpa": "attention_splitkv",
    "diffusion_attention_fa4": "attention_splitkv",
    "diffusion_attention_sdpa": "attention_splitkv",
    "diffusion_causal_conv3d_cat_pad": "diffusion_conv3d_cat_pad",
    # qwen38_nvfp4__* (sm_120 verify tier)
    "qwen38_fp4_gemm": "nvfp4_gemm",
    "qwen38_fp4_quantize": "packed_bytes",
    "qwen38_silu_fp4_quantize": "packed_bytes",
    "qwen38_fp8_gemv": "fp8_linear",
    "qwen38_fp8_linear": "fp8_linear",
    "qwen38_gdn_gating_update": "kda_decode",
    "qwen38_qkvzba_split": "packed_bytes",
    "qwen38_conv1d_update": "causal_conv1d",
}

DEFAULT = {"rtol": 1e-2, "atol": 2e-2,
           "source": "test/registered/attention/test_chunk_gated_delta_rule.py:28-29",
           "note": "fallback for an op with no family mapping - add one rather than rely on this"}


def get(op: str, dtype: str = "bfloat16") -> dict:
    fam = OP_FAMILY.get(op)
    if fam is None:
        return dict(DEFAULT, family=None, op=op)
    entry = TOLERANCES[fam]
    out = {"family": fam, "op": op, "source": entry["source"]}
    if entry.get("note"):
        out["note"] = entry["note"]
    if entry.get("exact"):
        out["exact"] = True
        out["rtol"], out["atol"] = 0.0, 0.0
        return out
    rtol, atol = entry.get(dtype, entry.get("bfloat16", (1e-2, 2e-2)))
    out["rtol"], out["atol"], out["dtype"] = rtol, atol, dtype
    return out


def table() -> str:
    lines = ["| op | family | rtol | atol | from SGLang test |",
             "| --- | --- | ---: | ---: | --- |"]
    for op in sorted(OP_FAMILY):
        t = get(op)
        lines.append("| `%s` | %s | %s | %s | `%s` |"
                     % (op, t["family"], t["rtol"], t["atol"], t["source"]))
    return "\n".join(lines)


if __name__ == "__main__":
    print(table())
