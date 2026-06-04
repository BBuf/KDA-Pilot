"""Minimal local stand-ins for the sglang-internal symbols imported by the
pinned baseline copies, so the copies run without importing the installed
sglang checkout at benchmark/correctness runtime.

The local A/B lane intentionally strips the custom-op registration layer from
BOTH sides symmetrically (the candidate's local entry is likewise a plain
callable); the shipping-integration comparison with full registration on both
sides happens separately inside an SGLang worktree. ``register_custom_op`` and
``debug_kernel_api`` therefore become passthrough decorators here, and
``current_platform`` reports plain CUDA (not MPS, not CPU), which matches the
B200 container these copies are benchmarked in.
"""

from __future__ import annotations

from typing import Any, Callable


def register_custom_op(fn: Callable | None = None, **_kwargs: Any):
    """Passthrough for ``sglang.srt.utils.custom_op.register_custom_op``.

    Supports both ``@register_custom_op`` and ``@register_custom_op(...)``
    decorator forms; returns the wrapped function unchanged.
    """

    if fn is not None and callable(fn):
        return fn

    def _decorator(inner: Callable) -> Callable:
        return inner

    return _decorator


def debug_kernel_api(fn: Callable) -> Callable:
    """Passthrough for ``sglang.kernel_api_logging.debug_kernel_api``."""

    return fn


class _CudaPlatform:
    """Stand-in for ``sglang.multimodal_gen.runtime.platforms.current_platform``
    restricted to the predicates the pinned files actually call."""

    @staticmethod
    def is_mps() -> bool:
        return False

    @staticmethod
    def is_cpu() -> bool:
        return False


current_platform = _CudaPlatform()
