"""Golden baseline for TileRT receive_selected_token_ids.

COMM/P2P kernel (not 1-GPU-isolatable). Workers GPU1-7 wait on the flag and copy the
top-2048 indices that GPU0 broadcast into their local buffer. No compute — the golden
is the identity copy from the (peer) low-latency buffer to the destination. Baseline
returns the source indices unchanged (correctness = bit-identical receive).
"""
import torch


def receive_selected_token_ids_baseline(ll_buf):
    """ll_buf [1,seq,2048] int32 (peer-written) -> dst (a copy)."""
    return ll_buf.clone()


def make_inputs(shapes, dev, topk=2048, cache_len=4096):
    seq = shapes["seq"]
    g = torch.Generator(device=dev).manual_seed(0)
    ll_buf = torch.randint(0, cache_len, (1, seq, topk), device=dev, dtype=torch.int32, generator=g)
    return {"ll_buf": ll_buf}
