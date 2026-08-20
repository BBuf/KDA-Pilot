"""Derive the arguments a shape-only replay cannot draw at random.

A captured row records each argument's shape and dtype. For a float activation a
random draw is a fair stand-in. For the arguments below it is not: they are
*addresses and extents*, and a random draw sends the kernel outside its buffers.
What comes back is not a wrong number, it is an illegal memory access - and because
that is asynchronous and sticky, it surfaces in whichever row runs next. One
un-derived `kv_indices` took out 41 of the 72 rows in the GLM-4.7 attention task.

Every rule here reconstructs the argument from the row itself, so the routing or the
segmentation is arbitrary but *valid*, and identical for both arms of an A/B. Nothing
is invented: an indptr is a prefix sum, an index array addresses the pool it is passed
alongside, and a split count is bounded by the buffer that holds the splits.

Used by each task's `baseline/entry.py::RECONSTRUCT`, and lifted verbatim into KDA-1.5
so both sides judge a candidate on the same inputs.
"""

from __future__ import annotations

# Index arguments that address a pool the kernel only *reads*. Aliasing is harmless
# here, so the index wraps and every row is replayable.
_READ_POOL_FOR = {
    "kv_indices": ("k_buffer", "v_buffer"),
    "req_pool_indices": ("req_to_token",),
}
# Index arguments that select a slot the kernel *updates in place*. These must be
# distinct: two rows pointing at one slot is a read-modify-write race, so the kernel
# returns a different answer every run and the reference fails its own gate. That is
# strictly worse than not replaying the row, so when the recorded pool cannot give every
# row its own slot the derivation refuses instead of aliasing.
_STATE_POOL_FOR = {
    "conv_state_indices": ("conv_state",),
    "initial_state_indices": ("initial_state_source", "initial_state"),
    "cache_indices": ("ssm_states", "conv_state"),
    "intermediate_state_indices": ("intermediate_conv_window",),
}


class NotReconstructible(RuntimeError):
    """The row cannot be replayed from its shapes without inventing a race."""
# Token-count arguments an indptr segments, in preference order.
_TOKENS_FOR = (
    "q_extend", "q", "x", "a", "mixed_qkvz", "hidden_states", "A", "input",
)


def _extent_for_indptr(name: str, kwargs: dict) -> int | None:
    """How many items the indptr named `name` segments.

    The distinction matters and cost 41 rows to learn: `kv_indptr` segments the *index
    array*, `qo_indptr` and `cu_seqlens` segment the *query tokens*. An extend row with
    no cached prefix records `kv_indices=[0]` and `kv_indptr=[0, 0]`; deriving that
    indptr from the 103 query tokens instead tells the kernel there are 103 cached keys
    to read out of an empty index array, which is an illegal access, not a wrong answer.
    So an empty index array yields extent 0 - it is an answer, not a missing value.
    """
    import torch

    if name.startswith("kv"):
        index = kwargs.get("kv_indices")
        if torch.is_tensor(index):
            return int(index.numel())
    for candidate in _TOKENS_FOR:
        value = kwargs.get(candidate)
        if torch.is_tensor(value) and value.numel():
            if value.dim() >= 3:
                return int(value.shape[-2] if value.shape[0] == 1 else value.shape[0])
            return int(value.shape[0])
    return None


def _fill_prefix_sum(tensor, total: int) -> None:
    """`tensor` becomes 0..total split evenly across its segments."""
    import torch

    segments = tensor.numel() - 1
    if segments < 1:
        tensor.zero_()
        return
    bounds = [(total * i) // segments for i in range(segments + 1)]
    tensor.copy_(torch.tensor(bounds, dtype=tensor.dtype, device=tensor.device))


def _rebuild_compressed_list(name: str, spec: dict, kwargs: dict) -> list:
    """Rebuild a Python list the capture stored as a summary.

    A long host-side list is recorded as `{"seq_len": n, "head": [...]}` - its length
    plus a prefix. The kernel does arithmetic on it (`can only concatenate str (not
    "int") to str` is what passing the summary through produces), so it has to be a list
    again. Per-sequence lengths additionally have to sum to the token count the
    activation carries, or the kernel walks off the end of it, so the known prefix is
    kept and the remainder is distributed over what is left.
    """
    import torch

    length = int(spec.get("seq_len") or 0)
    head = [int(v) for v in (spec.get("head") or [])]
    if length <= 0:
        return head
    if "len" not in name:
        return (head * length)[:length] if head else [0] * length
    total = None
    for candidate in ("x", "q", "q_extend", "hidden_states"):
        value = kwargs.get(candidate)
        if torch.is_tensor(value) and value.numel():
            total = int(value.shape[0] if value.dim() <= 2 else value.shape[-2])
            break
    head = head[:length]
    if total is None:
        return head + [head[-1] if head else 1] * (length - len(head))
    remaining = max(total - sum(head), 0)
    rest = length - len(head)
    if rest <= 0:
        # The prefix alone already covers the sequences; rescale it onto the tokens.
        scaled = [max(1, total // length)] * length
        scaled[-1] += total - sum(scaled)
        return scaled
    each = remaining // rest
    tail = [max(1, each)] * rest
    tail[-1] += max(total - sum(head) - sum(tail), 0)
    return head + tail


def derive(kwargs: dict) -> dict:
    """Repair every address-like argument in place. Safe to call on any row."""
    import torch

    # 0. lists the capture compressed to a summary
    for name, value in list(kwargs.items()):
        if isinstance(value, dict) and "seq_len" in value and "head" in value:
            kwargs[name] = _rebuild_compressed_list(name, value, kwargs)

    def _bound(pools):
        for pool_name in pools:
            pool = kwargs.get(pool_name)
            if torch.is_tensor(pool) and pool.dim() >= 1:
                return int(pool.shape[0])
        return None

    # 1a. read-only pools: wrap, so the index is always in bounds
    for name, pools in _READ_POOL_FOR.items():
        index = kwargs.get(name)
        if not torch.is_tensor(index) or not index.numel():
            continue
        bound = _bound(pools)
        if not bound:
            index.zero_()
            continue
        arange = torch.arange(index.numel(), device=index.device, dtype=index.dtype)
        index.copy_(arange % bound)

    # 1b. in-place state pools: distinct slots, or refuse
    for name, pools in _STATE_POOL_FOR.items():
        index = kwargs.get(name)
        if not torch.is_tensor(index) or not index.numel():
            continue
        bound = _bound(pools)
        if not bound:
            index.zero_()
            continue
        if index.numel() > bound:
            raise NotReconstructible(
                "%s selects %d slots from a %d-slot %s: replaying it would alias two rows "
                "onto one state and race. The row needs its captured indices."
                % (name, index.numel(), bound, pools[0]))
        index.copy_(torch.arange(index.numel(), device=index.device, dtype=index.dtype))

    # 2. indptr arrays: a prefix sum over the tokens they segment
    for name, value in kwargs.items():
        if not torch.is_tensor(value) or value.numel() < 2:
            continue
        if not (name.endswith("_indptr") or "cu_seqlens" in name
                or name in ("query_start_loc", "seq_start_loc")):
            continue
        lengths = next((v for k, v in kwargs.items()
                        if isinstance(v, list) and "len" in k and len(v) == value.numel() - 1),
                       None)
        if lengths is not None:
            # Exact: the indptr is the prefix sum of the list the kernel also reads.
            bounds, running = [0], 0
            for length in lengths:
                running += int(length)
                bounds.append(running)
            value.copy_(torch.tensor(bounds, dtype=value.dtype, device=value.device))
            continue
        total = _extent_for_indptr(name, kwargs)
        if total is not None:
            _fill_prefix_sum(value, total)

    # 2b. chunk maps: FLA's chunked kernels take a program-id -> (sequence, chunk) map
    #     built by `prepare_chunk_indices(cu_seqlens, chunk_size)`. Random values let two
    #     programs claim one output chunk, which is a write race: the kernel returns a
    #     different answer every run and the reference fails its own gate by ~3 (measured
    #     on gdn_recompute_w_u). The chunk size is not recorded, so it is recovered by
    #     asking the producer which size reproduces the recorded length - self-checking,
    #     and it fails loudly if none does.
    chunk_map = kwargs.get("chunk_indices")
    cu_seqlens = kwargs.get("cu_seqlens")
    if torch.is_tensor(chunk_map) and torch.is_tensor(cu_seqlens) and chunk_map.numel():
        from sglang.kernels.ops.attention.fla.index import prepare_chunk_indices

        want = int(chunk_map.shape[0])
        built = None
        for chunk_size in (64, 32, 128, 16, 256):
            candidate = prepare_chunk_indices(cu_seqlens, chunk_size)
            if int(candidate.shape[0]) == want:
                built = candidate
                break
        if built is None:
            raise NotReconstructible(
                "no chunk size in (16, 32, 64, 128, 256) reproduces the recorded "
                "chunk_indices length %d for these cu_seqlens" % want)
        chunk_map.copy_(built.to(chunk_map.dtype))

    # 3. split counts: bounded by the buffer that holds the splits
    splits = kwargs.get("num_kv_splits")
    if torch.is_tensor(splits) and splits.numel():
        cap = kwargs.get("max_kv_splits")
        logits = kwargs.get("attn_logits")
        if not isinstance(cap, int) and torch.is_tensor(logits) and logits.dim() >= 2:
            cap = int(logits.shape[-2])
        splits.fill_(max(1, int(cap) if isinstance(cap, int) else 1))

    # 4. per-sequence state predicates: the recorded call had state for the sequences it
    #    was given, and a random draw would benchmark the cheap branch on half the rows
    for name in ("has_initial_state", "has_initial_states"):
        value = kwargs.get(name)
        if torch.is_tensor(value) and value.dtype == torch.bool:
            value.fill_(True)

    # 4b. `*_cpu` arguments live on the host by contract - the kernel reads them with
    #     Python indexing to build its launch grid. The capture records a tensor spec and
    #     the allocator puts it on the device, which fails inside the kernel wrapper
    #     ("can only ..." from list arithmetic) rather than at the call.
    for name, value in list(kwargs.items()):
        if name.endswith("_cpu") and torch.is_tensor(value) and value.is_cuda:
            kwargs[name] = value.detach().cpu()

    # 5. scales are positive factors; a negative draw makes the reference meaningless
    for name in ("alpha", "global_scale", "a_global_sf", "weight_scale", "input_scale",
                 "k_scale", "v_scale", "dt_bias"):
        value = kwargs.get(name)
        if torch.is_tensor(value) and value.is_floating_point():
            value.abs_().clamp_(min=1e-4)
    return kwargs
