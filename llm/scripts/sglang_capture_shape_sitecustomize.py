"""Record selected SGLang kernel API call contracts as JSONL.

Use as a temporary ``sitecustomize.py`` by placing this file in a directory on
``PYTHONPATH`` before launching SGLang. It records tensor metadata only: no
tensor values are copied or saved.
"""

from __future__ import annotations

import functools
import importlib.abc
import importlib.machinery
import json
import os
import sys
import threading
import time
import dataclasses
from collections.abc import Mapping
from pathlib import Path
from typing import Any


OUT_TEMPLATE = os.environ.get("KDA_CAPTURE_SHAPES_JSONL")
MAX_CALLS_PER_FUNC = int(os.environ.get("KDA_CAPTURE_MAX_CALLS_PER_FUNC", "256"))

TARGETS: dict[str, tuple[str, ...]] = {
    "sglang.srt.layers.quantization.fp8_kernel": (
        "deep_gemm_fp8_fp8_bf16_nt",
        "w8a8_block_fp8_matmul_deepgemm",
        "w8a8_block_fp8_matmul_triton",
        "triton_scaled_mm",
        "scaled_fp8_quant",
        "static_quant_fp8",
        "sglang_per_token_quant_fp8",
        "sgl_per_token_quant_fp8",
        "sglang_per_token_group_quant_fp8",
        "sglang_per_token_group_quant_fp8_row_padded",
        "per_token_group_quant_fp8",
        "sglang_per_token_group_quant_8bit",
        "per_token_group_quant_8bit",
    ),
    "sglang.srt.layers.quantization.fp8_utils": (
        "flashinfer_bmm_fp8",
        "apply_fp8_linear",
        "apply_fp8_linear_bmm_flashinfer",
        "flashinfer_gemm_w8a8_block_fp8_linear_with_fallback",
        "flashinfer_deepgemm_w8a8_block_fp8_linear_with_fallback",
        "cutlass_w8a8_block_fp8_linear_with_fallback",
        "deepgemm_w8a8_block_fp8_linear_with_fallback",
        "triton_w8a8_block_fp8_linear",
        "triton_scaled_mm",
        "fp8_scaled_mm",
        "fp8_blockwise_scaled_mm",
        "_apply_fallback_scaled_mm",
    ),
    "sglang.jit_kernel.nvfp4": (
        "cutlass_scaled_fp4_mm",
        "cutlass_fp4_group_mm",
        "scaled_fp4_quant",
        "scaled_fp4_experts_quant",
        "silu_and_mul_scaled_fp4_experts_quant_packed",
        "scaled_fp4_grouped_quant",
        "silu_and_mul_scaled_fp4_grouped_quant",
    ),
    "sglang.jit_kernel.hadamard": (
        "hadamard_transform",
        "hadamard_transform_12n",
        "hadamard_transform_20n",
        "hadamard_transform_28n",
        "hadamard_transform_40n",
    ),
    "sglang.jit_kernel.dsv4.elementwise": (
        "fused_q_indexer_rope_hadamard_fp4_quant",
        "fused_q_indexer_rope_hadamard_quant",
    ),
    "sglang.jit_kernel.activation": (
        "_run_activation_inplace",
        "_run_activation_filtered_inplace",
        "run_activation",
        "silu_and_mul",
        "gelu_and_mul",
        "gelu_tanh_and_mul",
    ),
    "sglang.jit_kernel.moe_align": (
        "moe_align_block_size",
    ),
    "sgl_kernel.elementwise": (
        "dsv4_fused_q_indexer_rope_hadamard_quant",
    ),
    "sglang.srt.layers.quantization.fp4_utils": (
        "fp4_quantize",
    ),
    "sglang.srt.layers.quantization.fp8": (
        "Fp8LinearMethod.apply",
    ),
    "sglang.multimodal_gen.runtime.layers.quantization.weight_only_fp8": (
        "_apply_srt_w8a8_fp8_linear",
        "_apply_weight_only_fp8_linear",
        "dequantize_rowwise_fp8_weight",
    ),
    "sglang.srt.layers.layernorm": (
        "rmsnorm",
        "gemma_rmsnorm",
        "_jit_rmsnorm_hf",
        "fused_add_rmsnorm",
        "gemma_fused_add_rmsnorm",
        "_jit_fused_add_rmsnorm",
    ),
    "sglang.srt.layers.moe.moe_runner.triton_utils.fused_moe": (
        "fused_experts",
        "inplace_fused_experts",
        "outplace_fused_experts",
        "fused_experts_impl",
        "_fused_moe_kernel_sequence",
        "moe_sum_reduce",
        "moe_sum_reduce_torch_compile",
        "moe_sum_reduce_triton",
    ),
    "sglang.srt.layers.moe.moe_runner.triton_utils.moe_align_block_size": (
        "moe_align_block_size",
    ),
    "sglang.srt.layers.moe.moe_runner.triton_utils.fused_moe_triton_kernels": (
        "invoke_fused_moe_kernel",
        "moe_sum_reduce_triton",
    ),
    "sglang.srt.layers.moe.topk": (
        "select_experts",
        "fused_topk",
        "fused_topk_torch_native",
        "fused_topk_softmax_torch_raw_logits",
        "grouped_topk_gpu",
        "grouped_topk_cpu",
        "biased_grouped_topk_impl",
        "biased_grouped_topk_gpu",
        "biased_grouped_topk_cpu",
    ),
    "sglang.srt.layers.attention.trtllm_mha_backend": (
        "TRTLLMHAAttnBackend.forward_decode",
        "TRTLLMHAAttnBackend.forward_extend",
    ),
    "sglang.srt.layers.attention.triton_backend": (
        "TritonAttnBackend.forward_decode",
        "TritonAttnBackend.forward_extend",
    ),
    "sglang.srt.layers.attention.flashattention_backend": (
        "FlashAttentionBackend.forward_decode",
        "FlashAttentionBackend.forward_extend",
        "flash_attn_varlen_func",
        "flash_attn_with_kvcache",
    ),
    "sglang.srt.layers.radix_attention": (
        "unified_attention_with_output",
        "breakable_unified_attention_with_output",
    ),
    "sglang.srt.models.deepseek_common.attention_forward_methods.forward_mla": (
        "bmm_fp8",
        "_bmm_fp8_op",
        "mla_bmm_then_unified_attention",
        "bcg_mla_bmm_then_unified_attention",
    ),
    "sglang.srt.layers.attention.deepseek_v4_backend": (
        "DeepseekV4AttnBackend.forward",
        "DeepseekV4AttnBackend._forward_prefill_sparse",
    ),
    "sglang.srt.layers.attention.deepseek_v4_backend_hip_radix": (
        "DeepseekV4HipRadixBackend.forward",
    ),
    "sglang.srt.layers.attention.dsv4.indexer": (
        "fp8_paged_mqa_logits_torch",
        "fp8_paged_mqa_logits_torch_sm120",
        "_aiter_fp8_paged_mqa_logits",
    ),
    "sglang.srt.layers.attention.dsa_backend": (
        "DeepseekSparseAttnBackend.forward_extend",
        "DeepseekSparseAttnBackend.forward_decode",
        "DeepseekSparseAttnBackend._forward_fa3",
        "DeepseekSparseAttnBackend._forward_flashmla_sparse",
        "DeepseekSparseAttnBackend._forward_flashmla_kv",
        "DeepseekSparseAttnBackend._forward_standard_mha",
        "DeepseekSparseAttnBackend._forward_trtllm",
    ),
    "sglang.srt.models.nemotron_h": (
        "NemotronHAttention.forward",
        "NemotronHMambaDecoderLayer._forward_mamba",
        "nemotron_mamba2_with_output",
        "breakable_nemotron_mamba2_with_output",
    ),
    "sglang.srt.layers.attention.mamba.causal_conv1d": (
        "causal_conv1d_fn",
        "causal_conv1d_update",
    ),
    "sglang.srt.layers.attention.mamba.causal_conv1d_triton": (
        "causal_conv1d_fn",
        "causal_conv1d_update",
    ),
    "sglang.srt.layers.attention.mamba.ops.ssd_combined": (
        "mamba_chunk_scan_combined",
        "_mamba_chunk_scan_combined_fwd",
    ),
    "sglang.srt.layers.attention.mamba.ops.ssd_chunk_scan": (
        "_chunk_scan_fwd",
    ),
    "sglang.srt.layers.attention.mamba.ops.ssd_chunk_state": (
        "_chunk_state_fwd",
        "chunk_state_varlen",
    ),
    "sglang.srt.layers.attention.mamba.ops.ssd_state_passing": (
        "_state_passing_fwd",
    ),
    "sgl_kernel.flash_mla": (
        "flash_mla_with_kvcache",
        "flash_mla_sparse_fwd",
    ),
    "sgl_kernel": (
        "bmm_fp8",
        "fp8_scaled_mm",
        "fp8_blockwise_scaled_mm",
        "moe_align_block_size",
        "sgl_per_token_quant_fp8",
        "sglang_per_token_quant_fp8",
        "sgl_per_token_group_quant_fp8",
        "sglang_per_token_group_quant_fp8",
        "sglang_per_token_group_quant_fp8_row_padded",
    ),
    "sgl_kernel.gemm": (
        "bmm_fp8",
        "fp8_scaled_mm",
        "fp8_blockwise_scaled_mm",
        "sgl_per_token_quant_fp8",
        "sglang_per_token_quant_fp8",
        "sgl_per_token_group_quant_fp8",
        "sglang_per_token_group_quant_fp8",
        "sglang_per_token_group_quant_fp8_row_padded",
    ),
    "sglang.srt.layers.attention.flash_mla_sm120": (
        "flash_mla_with_kvcache_sm120",
    ),
    "flashinfer.prefill": (
        "trtllm_ragged_attention_deepseek",
        "trtllm_batch_context_with_kv_cache",
    ),
    "flashinfer.decode": (
        "trtllm_batch_decode_with_kv_cache_mla",
        "trtllm_batch_decode_with_kv_cache",
    ),
    "flashinfer": (
        "bmm_bf16",
        "bmm_fp8",
        "bmm_mxfp8",
        "mm_fp4",
        "mm_fp8",
        "mm_mxfp8",
        "grouped_mm_fp4",
        "grouped_mm_fp8",
        "grouped_mm_mxfp8",
        "group_gemm_nvfp4_nt_groupwise",
        "group_gemm_mxfp4_nt_groupwise",
        "trtllm_fp4_block_scale_moe",
        "trtllm_fp4_block_scale_routed_moe",
        "nvfp4_quantize",
        "nvfp4_block_scale_interleave",
    ),
    "flashinfer.gemm": (
        "bmm_bf16",
        "bmm_fp8",
        "bmm_mxfp8",
        "mm_fp4",
        "mm_fp8",
        "mm_mxfp8",
        "group_gemm_nvfp4_nt_groupwise",
        "group_gemm_mxfp4_nt_groupwise",
        "grouped_gemm_nt_masked",
    ),
}

TORCH_OP_TARGETS: dict[str, tuple[str, ...]] = {
    "sglang": (
        "flashinfer_fp4_quantize",
        "hadamard_transform",
        "inplace_fused_experts",
        "unified_attention_with_output",
    ),
}

TORCH_OP_OVERLOAD_TARGETS: dict[str, tuple[str, ...]] = {
    "sgl_kernel": (
        "bmm_fp8",
        "fp8_scaled_mm",
        "fp8_blockwise_scaled_mm",
        "sgl_per_token_quant_fp8",
        "sglang_per_token_quant_fp8",
        "sgl_per_token_group_quant_fp8",
        "sglang_per_token_group_quant_fp8",
        "sglang_per_token_group_quant_fp8_row_padded",
    ),
    # Kimi-K3 hot Python interfaces (hybrid KDA + MLA, latent MoE, SiTU).
    "sglang.kernels.ops.gemm.cutedsl_bf16_gemm": (
        "cutedsl_bf16_gemm",
        "cutedsl_bf16_gemm_out",
    ),
    "sglang.kernels.ops.gemm.tiny_gemm": (
        "tiny_n_gemm_bf16",
        "tiny_k_gemm_bf16",
    ),
    "sglang.kernels.ops.attention.kda_fused_decode": (
        "kda_fused_decode",
    ),
    "sglang.kernels.ops.quantization.per_token_group_quant": (
        "per_token_group_quant",
    ),
    "sglang.kernels.ops.moe.moe_route_radix": (
        "route_radix",
    ),
    "sglang.kernels.ops.moe.moe_fused_gate": (
        "moe_fused_gate",
    ),
    "sglang.kernels.ops.kimi_k3.activation": (
        "situ_and_mul",
    ),
    # The production attention-residual path is AttnResidual.forward ->
    # _aggregate -> _aggregate_fast/_aggregate_fused (aggregate_stream is only
    # the dspark aux-capture entry), so record the dispatcher and both fast
    # paths. Intra-module calls resolve through module globals at call time, so
    # patching the module attribute reaches them.
    "sglang.srt.layers.attn_residual": (
        "_aggregate",
        "_aggregate_fast",
        "_aggregate_fused",
        "_aggregate_fused_add",
        "aggregate_stream",
    ),
}

_lock = threading.Lock()
_counts: dict[str, int] = {}
_wrapped: set[str] = set()


def _disable_transformers_torchao_probe() -> None:
    """Avoid optional torchao imports in capture-only environments."""
    try:
        import transformers.utils as transformers_utils
        import transformers.utils.import_utils as import_utils

        def is_torchao_available(*args: Any, **kwargs: Any) -> bool:
            return False

        import_utils.is_torchao_available = is_torchao_available
        transformers_utils.is_torchao_available = is_torchao_available
    except Exception:
        pass


def _patch_torch_core_decompositions() -> None:
    """Normalize PyTorch nightly CustomDecompTable for older inductor callers."""
    try:
        import torch._decomp as torch_decomp

        original = torch_decomp.core_aten_decompositions
        if getattr(original, "_kda_capture_wrapped", False):
            return

        @functools.wraps(original)
        def core_aten_decompositions(*args: Any, **kwargs: Any) -> Mapping[Any, Any]:
            table = original(*args, **kwargs)
            if type(table) is dict:
                return table
            try:
                return dict(table.items())
            except Exception:
                return dict(table)

        setattr(core_aten_decompositions, "_kda_capture_wrapped", True)
        try:
            import torch.export.decomp_utils as decomp_utils

            if hasattr(decomp_utils, "core_aten_decompositions"):
                decomp_utils.core_aten_decompositions = core_aten_decompositions
        except Exception:
            pass
        torch_decomp.core_aten_decompositions = core_aten_decompositions
    except Exception:
        pass


def _out_path() -> Path | None:
    if not OUT_TEMPLATE:
        return None
    return Path(OUT_TEMPLATE.replace("%p", str(os.getpid())))


def _rank_env() -> dict[str, str | None]:
    keys = (
        "RANK",
        "LOCAL_RANK",
        "WORLD_SIZE",
        "TP_RANK",
        "CUDA_VISIBLE_DEVICES",
        "SGLANG_CAPTURE_SCENARIO",
    )
    return {key: os.environ.get(key) for key in keys}


def _tensor_meta(value: Any) -> dict[str, Any] | None:
    try:
        import torch
    except Exception:
        return None
    if not torch.is_tensor(value):
        return None
    device = value.device
    return {
        "kind": "tensor",
        "shape": list(value.shape),
        "dtype": str(value.dtype),
        "device": str(device),
        "device_type": device.type,
        "device_index": device.index,
        "stride": list(value.stride()),
        "storage_offset": int(value.storage_offset()),
        "is_contiguous": bool(value.is_contiguous()),
        "requires_grad": bool(value.requires_grad),
        "numel": int(value.numel()),
    }


def _summarize(value: Any, depth: int = 0) -> Any:
    tensor = _tensor_meta(value)
    if tensor is not None:
        return tensor
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if depth >= 3:
        return _object_meta(value)
    if isinstance(value, (tuple, list)):
        return {
            "kind": type(value).__name__,
            "items": [_summarize(item, depth + 1) for item in value],
        }
    if isinstance(value, dict):
        return {
            "kind": "dict",
            "items": {
                str(key): _summarize(item, depth + 1)
                for key, item in list(value.items())[:64]
            },
        }
    if dataclasses.is_dataclass(value) and not isinstance(value, type):
        items: dict[str, Any] = {}
        for field in dataclasses.fields(value)[:64]:
            try:
                items[field.name] = _summarize(getattr(value, field.name), depth + 1)
            except Exception as exc:
                items[field.name] = {
                    "kind": "unavailable",
                    "error": type(exc).__name__,
                }
        meta = _object_meta(value)
        meta["fields"] = items
        return meta
    if isinstance(value, tuple) and hasattr(value, "_fields"):
        items = {
            str(name): _summarize(getattr(value, name), depth + 1)
            for name in list(value._fields)[:64]
        }
        meta = _object_meta(value)
        meta["fields"] = items
        return meta
    return _object_meta(value)


def _object_meta(value: Any) -> dict[str, str]:
    cls = type(value)
    return {"kind": cls.__name__, "module": getattr(cls, "__module__", "")}


def _append_record(record: dict[str, Any]) -> None:
    path = _out_path()
    if path is None:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(record, sort_keys=True, separators=(",", ":"))
    with _lock:
        with path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")


def _is_torch_compiling() -> bool:
    try:
        import torch

        compiler = getattr(torch, "compiler", None)
        is_compiling = getattr(compiler, "is_compiling", None)
        if callable(is_compiling) and is_compiling():
            return True
    except Exception:
        pass
    try:
        import torch._dynamo

        return bool(torch._dynamo.is_compiling())
    except Exception:
        return False


def _resolve_target(module: Any, target_name: str) -> tuple[Any, str] | None:
    parts = target_name.split(".")
    parent = module
    for part in parts[:-1]:
        if not hasattr(parent, part):
            return None
        parent = getattr(parent, part)
    return parent, parts[-1]


def _wrap_function(module: Any, module_name: str, target_name: str) -> None:
    resolved = _resolve_target(module, target_name)
    if resolved is None:
        return
    parent, attr_name = resolved
    if not hasattr(parent, attr_name):
        return
    func = getattr(parent, attr_name)
    if not callable(func) or getattr(func, "_kda_shape_capture_wrapped", False):
        return
    full_name = f"{module_name}.{target_name}"
    if full_name in _wrapped:
        return

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if _is_torch_compiling():
            return func(*args, **kwargs)
        count = _counts.get(full_name, 0)
        should_record = count < MAX_CALLS_PER_FUNC
        if should_record:
            _counts[full_name] = count + 1
            record: dict[str, Any] = {
                "event": "call",
                "time": time.time(),
                "pid": os.getpid(),
                "call_index": count + 1,
                "function": full_name,
                "rank_env": _rank_env(),
                "args": [_summarize(arg) for arg in args],
                "kwargs": {key: _summarize(val) for key, val in kwargs.items()},
            }
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                record["exception"] = {
                    "type": type(exc).__name__,
                    "message": str(exc),
                }
                _append_record(record)
                raise
            record["result"] = _summarize(result)
            _append_record(record)
            return result
        return func(*args, **kwargs)

    setattr(wrapper, "_kda_shape_capture_wrapped", True)
    setattr(parent, attr_name, wrapper)
    _wrapped.add(full_name)


def _wrap_module(module: Any, module_name: str) -> None:
    for attr_name in TARGETS.get(module_name, ()):
        _wrap_function(module, module_name, attr_name)


def _wrap_torch_function(torch_module: Any, attr_name: str, full_name: str) -> None:
    if not hasattr(torch_module, attr_name):
        return
    func = getattr(torch_module, attr_name)
    if not callable(func) or getattr(func, "_kda_shape_capture_wrapped", False):
        return

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if _is_torch_compiling():
            return func(*args, **kwargs)
        count = _counts.get(full_name, 0)
        should_record = count < MAX_CALLS_PER_FUNC
        if should_record:
            _counts[full_name] = count + 1
            record: dict[str, Any] = {
                "event": "call",
                "time": time.time(),
                "pid": os.getpid(),
                "call_index": count + 1,
                "function": full_name,
                "rank_env": _rank_env(),
                "args": [_summarize(arg) for arg in args],
                "kwargs": {key: _summarize(val) for key, val in kwargs.items()},
            }
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                record["exception"] = {
                    "type": type(exc).__name__,
                    "message": str(exc),
                }
                _append_record(record)
                raise
            record["result"] = _summarize(result)
            _append_record(record)
            return result
        return func(*args, **kwargs)

    setattr(wrapper, "_kda_shape_capture_wrapped", True)
    setattr(torch_module, attr_name, wrapper)
    _wrapped.add(full_name)


def _wrap_torch_op_overload(
    op_packet: Any,
    overload_name: str,
    full_name: str,
) -> None:
    if full_name in _wrapped:
        return
    if not hasattr(op_packet, overload_name):
        return
    func = getattr(op_packet, overload_name)
    if not callable(func) or getattr(func, "_kda_shape_capture_wrapped", False):
        return

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if _is_torch_compiling():
            return func(*args, **kwargs)
        count = _counts.get(full_name, 0)
        should_record = count < MAX_CALLS_PER_FUNC
        if should_record:
            _counts[full_name] = count + 1
            record: dict[str, Any] = {
                "event": "call",
                "time": time.time(),
                "pid": os.getpid(),
                "call_index": count + 1,
                "function": full_name,
                "rank_env": _rank_env(),
                "args": [_summarize(arg) for arg in args],
                "kwargs": {key: _summarize(val) for key, val in kwargs.items()},
            }
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                record["exception"] = {
                    "type": type(exc).__name__,
                    "message": str(exc),
                }
                _append_record(record)
                raise
            record["result"] = _summarize(result)
            _append_record(record)
            return result
        return func(*args, **kwargs)

    setattr(wrapper, "_kda_shape_capture_wrapped", True)
    setattr(op_packet, overload_name, wrapper)
    _wrapped.add(full_name)


def _wrap_torch_ops_once() -> bool:
    try:
        import torch
    except Exception:
        return False

    all_wrapped = True
    for namespace, names in TORCH_OP_TARGETS.items():
        try:
            op_namespace = getattr(torch.ops, namespace)
        except Exception:
            all_wrapped = False
            continue
        for name in names:
            full_name = f"torch.ops.{namespace}.{name}"
            if full_name in _wrapped:
                continue
            if not hasattr(op_namespace, name):
                all_wrapped = False
                continue
            try:
                _wrap_torch_function(op_namespace, name, full_name)
            except Exception:
                all_wrapped = False
    for namespace, names in TORCH_OP_OVERLOAD_TARGETS.items():
        try:
            op_namespace = getattr(torch.ops, namespace)
        except Exception:
            all_wrapped = False
            continue
        for name in names:
            packet_name = f"torch.ops.{namespace}.{name}"
            full_name = f"{packet_name}.default"
            if full_name in _wrapped:
                continue
            if not hasattr(op_namespace, name):
                all_wrapped = False
                continue
            try:
                _wrap_torch_op_overload(
                    getattr(op_namespace, name), "default", full_name
                )
            except Exception:
                all_wrapped = False
    return all_wrapped


def _wrap_torch_ops_periodically() -> None:
    poll_steps = int(os.environ.get("KDA_CAPTURE_TORCH_OP_POLL_STEPS", "2400"))
    poll_interval = float(os.environ.get("KDA_CAPTURE_TORCH_OP_POLL_INTERVAL", "0.25"))
    initial_delay = float(os.environ.get("KDA_CAPTURE_TORCH_OP_INITIAL_DELAY", "0"))
    if initial_delay > 0:
        time.sleep(initial_delay)
    for _ in range(poll_steps):
        if _wrap_torch_ops_once():
            return
        time.sleep(poll_interval)


class _CaptureLoader(importlib.abc.Loader):
    def __init__(self, wrapped: importlib.abc.Loader, module_name: str):
        self._wrapped = wrapped
        self._module_name = module_name

    def create_module(self, spec: importlib.machinery.ModuleSpec) -> Any:
        create = getattr(self._wrapped, "create_module", None)
        if create is None:
            return None
        return create(spec)

    def exec_module(self, module: Any) -> None:
        self._wrapped.exec_module(module)
        _wrap_module(module, self._module_name)


class _CaptureFinder(importlib.abc.MetaPathFinder):
    def find_spec(
        self,
        fullname: str,
        path: object | None,
        target: object | None = None,
    ) -> importlib.machinery.ModuleSpec | None:
        if fullname not in TARGETS:
            return None
        for finder in sys.meta_path:
            if finder is self:
                continue
            find_spec = getattr(finder, "find_spec", None)
            if find_spec is None:
                continue
            spec = find_spec(fullname, path, target)
            if spec is None or spec.loader is None:
                continue
            spec.loader = _CaptureLoader(spec.loader, fullname)
            return spec
        return None


if OUT_TEMPLATE:
    if os.environ.get("KDA_CAPTURE_DISABLE_TORCHAO") == "1":
        _disable_transformers_torchao_probe()
    if os.environ.get("KDA_CAPTURE_PATCH_TORCH_DECOMPOSITIONS") == "1":
        _patch_torch_core_decompositions()

    sys.meta_path.insert(0, _CaptureFinder())
    for _module_name, _module in list(sys.modules.items()):
        if _module_name in TARGETS:
            _wrap_module(_module, _module_name)

    if os.environ.get("KDA_CAPTURE_TORCH_BMM") == "1":
        try:
            import torch

            _wrap_torch_function(torch, "bmm", "torch.bmm")
        except Exception:
            pass

    if os.environ.get("KDA_CAPTURE_TORCH_SCALED_MM") == "1":
        try:
            import torch

            _wrap_torch_function(torch, "_scaled_mm", "torch._scaled_mm")
        except Exception:
            pass

    if os.environ.get("KDA_CAPTURE_TORCH_LINEAR") == "1":
        try:
            import torch.nn.functional as F

            _wrap_torch_function(F, "linear", "torch.nn.functional.linear")
        except Exception:
            pass

    if os.environ.get("KDA_CAPTURE_TORCH_OPS") == "1":
        threading.Thread(target=_wrap_torch_ops_periodically, daemon=True).start()
