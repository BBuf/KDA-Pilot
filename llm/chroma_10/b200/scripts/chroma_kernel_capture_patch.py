"""Runtime-only SGLang kernel interface logging for the Chroma cookbook server."""

from __future__ import annotations

import functools
import inspect
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Callable

import torch

_LOG_LEVEL = int(os.environ.get("SGLANG_KERNEL_API_LOGLEVEL", "0") or "0")
_LOG_DEST = os.environ.get("SGLANG_KERNEL_API_LOGDEST", "stdout")
_LOGGER = logging.getLogger("chroma.sglang.kernel_api")


def _setup_logger() -> None:
    for handler in list(_LOGGER.handlers):
        _LOGGER.removeHandler(handler)
        handler.close()
    if _LOG_LEVEL == 0:
        _LOGGER.addHandler(logging.NullHandler())
        _LOGGER.setLevel(logging.CRITICAL + 1)
        return
    _LOGGER.setLevel(logging.DEBUG)
    if _LOG_DEST == "stdout":
        handler = logging.StreamHandler(sys.stdout)
    elif _LOG_DEST == "stderr":
        handler = logging.StreamHandler(sys.stderr)
    else:
        path = Path(_LOG_DEST.replace("%i", str(os.getpid())))
        path.parent.mkdir(parents=True, exist_ok=True)
        handler = logging.FileHandler(path, mode="a")
    handler.setFormatter(logging.Formatter("%(message)s"))
    _LOGGER.addHandler(handler)
    _LOGGER.propagate = False


def _timestamp() -> str:
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")


def _is_compiling() -> bool:
    try:
        return bool(torch.compiler.is_compiling())
    except Exception:
        return False


def _append_line(lines: list[str], indent: int, text: str) -> None:
    lines.append(" " * indent + text)


def _serialize_tensor(tensor: torch.Tensor) -> list[str]:
    lines = ["Tensor("]
    _append_line(lines, 2, f"shape={tuple(tensor.shape)}")
    _append_line(lines, 2, f"dtype={tensor.dtype}")
    _append_line(lines, 2, f"device={tensor.device}")
    _append_line(lines, 2, f"requires_grad={tensor.requires_grad}")
    _append_line(lines, 2, f"is_contiguous={tensor.is_contiguous()}")
    lines.append(")")
    return lines


def _serialize_value(value: Any, depth: int = 0) -> list[str]:
    if depth >= 2:
        return [f"{type(value).__name__}(...)"]
    if isinstance(value, torch.Tensor):
        return _serialize_tensor(value)
    if isinstance(value, (str, int, float, bool, type(None))):
        return [repr(value)]
    if isinstance(value, (list, tuple)):
        opener = "[" if isinstance(value, list) else "("
        closer = "]" if isinstance(value, list) else ")"
        lines = [opener]
        for idx, item in enumerate(value[:4]):
            item_lines = _serialize_value(item, depth + 1)
            lines.append(f"  [{idx}] {item_lines[0]}")
            for extra in item_lines[1:]:
                lines.append(f"      {extra}")
        if len(value) > 4:
            lines.append(f"  ... ({len(value) - 4} more items)")
        lines.append(closer)
        return lines
    if isinstance(value, dict):
        lines = ["{"]
        for key, item in list(value.items())[:8]:
            item_lines = _serialize_value(item, depth + 1)
            lines.append(f"  {key!r}: {item_lines[0]}")
            for extra in item_lines[1:]:
                lines.append(f"      {extra}")
        if len(value) > 8:
            lines.append(f"  ... ({len(value) - 8} more items)")
        lines.append("}")
        return lines
    summary = [f"{type(value).__name__}("]
    for attr in ("shape", "dtype", "device"):
        if hasattr(value, attr):
            try:
                _append_line(summary, 2, f"{attr}={getattr(value, attr)}")
            except Exception:
                pass
    if len(summary) == 1:
        _append_line(summary, 2, f"repr={repr(value)[:200]}")
    summary.append(")")
    return summary


def _log_section(title: str, data: dict[str, Any]) -> None:
    _LOGGER.debug(title)
    for key, value in data.items():
        lines = _serialize_value(value)
        _LOGGER.debug("  %s=%s", key, lines[0])
        for line in lines[1:]:
            _LOGGER.debug("    %s", line)


def debug_kernel_api(func: Callable, *, op_name: str) -> Callable:
    if _LOG_LEVEL == 0 or getattr(func, "_chroma_kernel_wrapped", False):
        return func

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if _is_compiling():
            return func(*args, **kwargs)
        positional_args = args
        try:
            params = tuple(inspect.signature(func).parameters.values())
        except (TypeError, ValueError):
            params = ()
        if args and params and params[0].name in {"self", "cls"}:
            positional_args = args[1:]

        _LOGGER.debug("=" * 80)
        _LOGGER.debug("%s SGLang Kernel API Call: %s", _timestamp(), op_name)
        if _LOG_LEVEL >= 3:
            if positional_args:
                _log_section(
                    "Positional input arguments:",
                    {f"arg[{idx}]": arg for idx, arg in enumerate(positional_args)},
                )
            if kwargs:
                _log_section("Keyword input arguments:", kwargs)
        result = func(*args, **kwargs)
        if _LOG_LEVEL >= 3:
            _log_section("Output:", {"return": result})
        return result

    setattr(wrapper, "_chroma_kernel_wrapped", True)
    return wrapper


def _wrap_module_func(module_name: str, attr: str, op_name: str | None = None) -> None:
    try:
        module = __import__(module_name, fromlist=[attr])
        func = getattr(module, attr)
    except Exception:
        return
    setattr(module, attr, debug_kernel_api(func, op_name=op_name or f"{module_name}.{attr}"))


def _wrap_method(module_name: str, class_name: str, method: str, op_name: str | None = None) -> None:
    try:
        module = __import__(module_name, fromlist=[class_name])
        cls = getattr(module, class_name)
        func = getattr(cls, method)
    except Exception:
        return
    setattr(
        cls,
        method,
        debug_kernel_api(func, op_name=op_name or f"{module_name}.{class_name}.{method}"),
    )


def install() -> None:
    _setup_logger()
    if _LOG_LEVEL == 0:
        return

    for module_name in ("sgl_kernel", "sglang.srt.layers.layernorm"):
        for attr in (
            "rmsnorm",
            "fused_add_rmsnorm",
            "gemma_rmsnorm",
            "gemma_fused_add_rmsnorm",
            "apply_rope_with_cos_sin_cache_inplace",
            "fast_topk",
            "fast_topk_transform_fused",
            "top_k_top_p_sampling_from_logits",
            "top_k_renorm_prob",
            "top_p_renorm_prob",
        ):
            _wrap_module_func(module_name, attr, f"{module_name}.{attr}")

    for attr in ("silu_and_mul", "gelu_and_mul", "gelu_tanh_and_mul"):
        _wrap_module_func("sglang.srt.layers.activation", attr, f"sglang.srt.layers.activation.{attr}")

    for class_name in ("ColumnParallelLinear", "RowParallelLinear", "ReplicatedLinear"):
        _wrap_method("sglang.srt.layers.linear", class_name, "forward")

    _wrap_method("sglang.srt.layers.quantization.unquant", "UnquantizedLinearMethod", "apply")
    _wrap_method("sglang.srt.layers.quantization.unquant", "UnquantizedEmbeddingMethod", "apply")

    _wrap_method("sglang.srt.layers.attention.base_attn_backend", "AttentionBackend", "forward")
    _wrap_method("sglang.srt.layers.radix_attention", "RadixAttention", "forward")
    for class_name in (
        "VisionAttention",
        "VisionSdpaAttention",
        "VisionTritonAttention",
        "VisionFlash3Attention",
    ):
        _wrap_method("sglang.srt.layers.attention.vision", class_name, "forward")

    _wrap_method("sglang.srt.layers.vocab_parallel_embedding", "VocabParallelEmbedding", "forward")
    _wrap_method("sglang.srt.layers.vocab_parallel_embedding", "ParallelLMHead", "forward")
    _wrap_method("sglang.srt.layers.logits_processor", "LogitsProcessor", "forward")
