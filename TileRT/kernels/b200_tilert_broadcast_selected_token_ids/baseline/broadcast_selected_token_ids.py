"""Golden baseline for TileRT broadcast_selected_token_ids.

COMM/P2P kernel (not 1-GPU-isolatable). GPU0 writes the top-2048 selected-KV indices
into each peer's NVLink low-latency buffer (peer_bufs + flag). There is no compute —
the golden is the identity: the broadcast must deliver the same index tensor. Baseline
returns the indices unchanged (the candidate's correctness = bit-identical delivery).
"""
import torch


def broadcast_selected_token_ids_baseline(idx):
    """idx [1,seq,2048] int32 -> same tensor (broadcast is a copy)."""
    return idx.clone()


def make_inputs(shapes, dev, topk=2048, cache_len=4096):
    seq = shapes["seq"]
    g = torch.Generator(device=dev).manual_seed(0)
    idx = torch.randint(0, cache_len, (1, seq, topk), device=dev, dtype=torch.int32, generator=g)
    return {"idx": idx}
