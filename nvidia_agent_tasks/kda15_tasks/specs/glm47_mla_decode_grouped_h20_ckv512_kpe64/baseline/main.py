"""Baseline: the SGLang kernel this task is asking a candidate to beat.

Not a PyTorch reference - `decode_attention_fwd_grouped` is the kernel GLM-4.7-Flash
actually serves decode with, so the number to clear is a real one.
"""

from sglang.kernels.ops.attention.decode_attention import decode_attention_fwd_grouped


def run(
    q,
    k_buffer,
    v_buffer,
    o,
    kv_indptr,
    kv_indices,
    attn_logits,
    attn_lse,
    num_kv_splits,
    max_kv_splits,
    sm_scale_withk,
    v_scale,
    logit_cap=0.0,
    sinks=None,
    xai_temperature_len=-1,
    has_mla=False,
    use_pdl=False,
    page_size=1,
    score_mod=None,
    aux_tensors=None,
):
    decode_attention_fwd_grouped(
        q,
        k_buffer,
        v_buffer,
        o,
        kv_indptr,
        kv_indices,
        attn_logits,
        attn_lse,
        num_kv_splits,
        max_kv_splits,
        sm_scale_withk,
        v_scale,
        logit_cap=logit_cap,
        sinks=sinks,
        xai_temperature_len=xai_temperature_len,
        has_mla=has_mla,
        use_pdl=use_pdl,
        page_size=page_size,
        score_mod=score_mod,
        aux_tensors=aux_tensors,
    )
    return o
