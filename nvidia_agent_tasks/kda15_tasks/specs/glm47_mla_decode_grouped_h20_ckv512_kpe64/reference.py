"""Reference for GLM-4.7-Flash MLA grouped decode attention.

Independent of the kernel under test: one sequence at a time, gather the pages this
sequence owns, and run the textbook attention on them in float32. The absorbed-MLA
layout is what makes this short - the same pool row holds the compressed KV and the
rope key, so `k_buffer[i]` is the full 576-wide key and `v_buffer[i]` is its first 512
columns.
"""

import torch


@torch.no_grad()
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
    num_seqs = q.shape[0]
    for seq in range(num_seqs):
        start = int(kv_indptr[seq].item())
        end = int(kv_indptr[seq + 1].item())
        if end <= start:
            # A sequence with no cached history attends to nothing. Softmax over an
            # empty axis is NaN, so the answer is a zero row, not a division.
            o[seq].zero_()
            continue
        pages = kv_indices[start:end].long()
        keys = k_buffer[pages].squeeze(1).float()
        values = v_buffer[pages].squeeze(1).float()
        logits = (q[seq].float() @ keys.transpose(0, 1)) * float(sm_scale_withk)
        if logit_cap and logit_cap > 0:
            logits = logit_cap * torch.tanh(logits / logit_cap)
        weights = torch.softmax(logits, dim=-1)
        o[seq] = ((weights @ values) * float(v_scale)).to(o.dtype)
    return o
