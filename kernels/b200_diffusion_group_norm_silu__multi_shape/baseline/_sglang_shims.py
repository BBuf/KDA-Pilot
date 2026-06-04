"""Local stand-ins for SGLang utilities referenced by the copied baseline.

The standalone benchmark contract forbids importing SGLang at correctness or
benchmark runtime. The copied Triton kernel only uses
``sglang.srt.utils.custom_op.register_custom_op`` as a torch custom-op
registration decorator; for standalone timing/correctness the decoration is a
no-op (the upstream decorator does not change eager-call behavior).
"""

from __future__ import annotations


def register_custom_op(*_args, **_kwargs):
    """No-op replacement for sglang.srt.utils.custom_op.register_custom_op."""

    def decorator(fn):
        return fn

    return decorator
