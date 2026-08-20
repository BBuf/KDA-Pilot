"""Bring up the pieces of SGLang's runtime that a kernel expects to already exist.

Several captured kernels are not pure functions of their arguments: they read the
published server config, or they call into the tensor-parallel group. Outside a server
those are absent and the kernel raises before it computes anything:

    ValueError: config namespace 'exec' not published
    AssertionError: tensor model parallel group is not initialized
    ParallelContext has no 'enable_dsa_prefill_context_parallel' (config not published)

None of that is a property of the workload - it is scaffolding the server would have
built. This module builds the smallest version of it: a default `ServerArgs` published
so every namespace exists with the value the server uses when nothing is set, and a
single-rank parallel group so `get_tensor_model_parallel_*` answers. Both are
idempotent, and neither sets a knob that changes which branch a kernel takes.

`ServerArgs()` is *not* constructed normally: its `__post_init__` resolves the model on
the Hugging Face hub, which a kernel benchmark has no business doing. The dataclass is
filled at its declared defaults instead.
"""

from __future__ import annotations

_published = False
_parallel_ready = False


def publish_config() -> None:
    """Make every config namespace exist, at the server's own defaults."""
    global _published
    if _published:
        return
    import dataclasses

    from sglang.srt import runtime_context
    from sglang.srt.server_args import ServerArgs

    if not runtime_context._CONTEXT.is_config_namespace_published("exec"):
        args = ServerArgs.__new__(ServerArgs)
        for field in dataclasses.fields(ServerArgs):
            if field.default is not dataclasses.MISSING:
                value = field.default
            elif field.default_factory is not dataclasses.MISSING:
                value = field.default_factory()
            else:
                value = None
            setattr(args, field.name, value)
        args.model_path = "unused-for-kernel-benchmarks"
        runtime_context.publish(args, role="engine")
    _published = True


def init_single_rank_parallel() -> None:
    """A one-rank tensor-parallel group, so the collectives resolve to no-ops."""
    global _parallel_ready
    if _parallel_ready:
        return
    import os

    import torch
    from sglang.srt.distributed import parallel_state

    if not torch.distributed.is_initialized():
        os.environ.setdefault("MASTER_ADDR", "127.0.0.1")
        os.environ.setdefault("MASTER_PORT", "29591")
        os.environ.setdefault("RANK", "0")
        os.environ.setdefault("WORLD_SIZE", "1")
        os.environ.setdefault("LOCAL_RANK", "0")
        parallel_state.init_distributed_environment(
            world_size=1,
            rank=0,
            distributed_init_method="tcp://127.0.0.1:%s" % os.environ["MASTER_PORT"],
            local_rank=0,
            backend="nccl",
        )
    try:
        parallel_state.initialize_model_parallel(
            tensor_model_parallel_size=1, pipeline_model_parallel_size=1
        )
    except Exception:
        # Already initialized by an earlier row; that is the state we wanted.
        pass
    _parallel_ready = True


def ensure(*, parallel: bool = False) -> None:
    """Call from a task's RECONSTRUCT before the kernel runs."""
    publish_config()
    if parallel:
        init_single_rank_parallel()
