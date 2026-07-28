#!/usr/bin/env python3
"""Aggregate KDA SGLang kernel shape-capture JSONL into task workload files."""

from __future__ import annotations

import argparse
import glob
import json
import re
from collections import OrderedDict
from pathlib import Path
from typing import Any


TASK_SUFFIX_RULES = {
    "__sglang_deep_gemm_fp8_fp8_bf16_nt": (
        "deep_gemm_fp8_fp8_bf16_nt",
    ),
    "__fp8_bmm": (
        ".bmm_fp8",
        ".bmm_mxfp8",
        ".bmm_bf16",
        ".mm_fp4",
        ".mm_fp8",
        ".mm_mxfp8",
        "._bmm_fp8_op",
        ".flashinfer_bmm_fp8",
        "torch.bmm",
        "fp8_paged_mqa_logits_torch",
        "_aiter_fp8_paged_mqa_logits",
    ),
    "__sglang_unified_attention_with_output": (
        "unified_attention_with_output",
        "mla_bmm_then_unified_attention",
        "DeepseekV4AttnBackend.forward",
        "DeepseekV4HipRadixBackend.forward",
        "DeepseekSparseAttnBackend.forward_extend",
        "DeepseekSparseAttnBackend.forward_decode",
        "DeepseekSparseAttnBackend._forward_fa3",
        "DeepseekSparseAttnBackend._forward_flashmla_sparse",
        "DeepseekSparseAttnBackend._forward_flashmla_kv",
        "DeepseekSparseAttnBackend._forward_standard_mha",
        "DeepseekSparseAttnBackend._forward_trtllm",
        "TRTLLMHAAttnBackend.forward_decode",
        "TRTLLMHAAttnBackend.forward_extend",
        "TritonAttnBackend.forward_decode",
        "TritonAttnBackend.forward_extend",
        "flash_mla_with_kvcache",
        "flash_mla_sparse_fwd",
        "trtllm_ragged_attention_deepseek",
        "trtllm_batch_context_with_kv_cache",
        "trtllm_batch_decode_with_kv_cache",
        "trtllm_batch_decode_with_kv_cache_mla",
        "torch.ops.sglang.unified_attention_with_output",
        "_forward_prefill_sparse",
    ),
    "__attention": (
        "unified_attention_with_output",
        "FlashAttentionBackend.forward_decode",
        "FlashAttentionBackend.forward_extend",
        "DeepseekSparseAttnBackend.forward_extend",
        "DeepseekSparseAttnBackend.forward_decode",
        "DeepseekSparseAttnBackend._forward_standard_mha",
        "DeepseekSparseAttnBackend._forward_trtllm",
        "flash_attn_varlen_func",
        "flash_attn_with_kvcache",
        "TRTLLMHAAttnBackend.forward_decode",
        "TRTLLMHAAttnBackend.forward_extend",
        "trtllm_batch_context_with_kv_cache",
        "trtllm_batch_decode_with_kv_cache",
        "trtllm_ragged_attention_deepseek",
        "trtllm_batch_decode_with_kv_cache_mla",
    ),
    "__per_token_group_quant": (
        "sglang_per_token_group_quant_fp8",
        "sglang_per_token_group_quant_fp8_row_padded",
        "per_token_group_quant_fp8",
        "sglang_per_token_group_quant_8bit",
        "per_token_group_quant_8bit",
    ),
    "__fused_add_rmsnorm": (
        ".fused_add_rmsnorm",
        ".gemma_fused_add_rmsnorm",
        "._jit_fused_add_rmsnorm",
    ),
    "__rmsnorm": (
        ".rmsnorm",
        ".gemma_rmsnorm",
        "._jit_rmsnorm_hf",
    ),
    "__fused_moe_triton": (
        "triton_utils.fused_moe.fused_experts",
        "triton_utils.fused_moe.inplace_fused_experts",
        "triton_utils.fused_moe.outplace_fused_experts",
        "triton_utils.fused_moe.fused_experts_impl",
        "triton_utils.fused_moe._fused_moe_kernel_sequence",
        "triton_utils.fused_moe_triton_kernels.invoke_fused_moe_kernel",
    ),
    "__sglang_inplace_fused_experts": (
        "triton_utils.fused_moe.inplace_fused_experts",
        "triton_utils.fused_moe.fused_experts_impl",
        "triton_utils.fused_moe._fused_moe_kernel_sequence",
        "triton_utils.fused_moe_triton_kernels.invoke_fused_moe_kernel",
        "torch.ops.sglang.inplace_fused_experts",
    ),
    "__sglang_run_activation_inplace": (
        "jit_kernel.activation._run_activation_inplace",
        "jit_kernel.activation._run_activation_filtered_inplace",
        "jit_kernel.activation.run_activation",
        "jit_kernel.activation.silu_and_mul",
        "jit_kernel.activation.gelu_and_mul",
        "jit_kernel.activation.gelu_tanh_and_mul",
    ),
    "__sglang_flashinfer_fp4_quantize": (
        "quantization.fp4_utils.fp4_quantize",
        "torch.ops.sglang.flashinfer_fp4_quantize",
        "nvfp4_quantize",
        "nvfp4_block_scale_interleave",
        "scaled_fp4_quant",
    ),
    "__void_anonymous_namespace_fast_ha": (
        "DeepseekSparseAttnBackend.forward_extend",
        "DeepseekSparseAttnBackend.forward_decode",
        "DeepseekSparseAttnBackend._forward_standard_mha",
        "DeepseekSparseAttnBackend._forward_trtllm",
        "fused_q_indexer_rope_hadamard_fp4_quant",
        "fused_q_indexer_rope_hadamard_quant",
        "dsv4_fused_q_indexer_rope_hadamard_quant",
        "jit_kernel.hadamard.hadamard_transform",
        "torch.ops.sglang.hadamard_transform",
    ),
    "__linear_gemm": (
        ".apply_fp8_linear",
        ".apply_fp8_linear_bmm_flashinfer",
        ".flashinfer_gemm_w8a8_block_fp8_linear_with_fallback",
        ".cutlass_w8a8_block_fp8_linear_with_fallback",
        ".deepgemm_w8a8_block_fp8_linear_with_fallback",
        ".triton_w8a8_block_fp8_linear",
        ".triton_scaled_mm",
        ".fp8_scaled_mm",
        ".fp8_blockwise_scaled_mm",
        ".cutlass_scaled_fp4_mm",
        ".cutlass_fp4_group_mm",
        ".mm_fp4",
        ".mm_fp8",
        ".mm_mxfp8",
        ".group_gemm_nvfp4_nt_groupwise",
        ".group_gemm_mxfp4_nt_groupwise",
        ".grouped_gemm_nt_masked",
        "._apply_fallback_scaled_mm",
        "torch._scaled_mm",
        "torch.nn.functional.linear",
    ),
    "__quant_fp8": (
        "scaled_fp8_quant",
        "static_quant_fp8",
        "sglang_per_token_quant_fp8",
        "sgl_per_token_quant_fp8",
        "sglang_per_token_group_quant_fp8",
        "sglang_per_token_group_quant_fp8_row_padded",
        "sgl_per_token_group_quant_fp8",
        "torch.ops.sgl_kernel.sglang_per_token_quant_fp8.default",
        "torch.ops.sgl_kernel.sgl_per_token_quant_fp8.default",
        "torch.ops.sgl_kernel.sglang_per_token_group_quant_fp8.default",
        "torch.ops.sgl_kernel.sgl_per_token_group_quant_fp8.default",
        "torch.ops.sgl_kernel.sglang_per_token_group_quant_fp8_row_padded.default",
        "per_token_group_quant_fp8",
        "scaled_fp4_quant",
        "scaled_fp4_experts_quant",
        "silu_and_mul_scaled_fp4_experts_quant",
        "scaled_fp4_grouped_quant",
        "nvfp4_quantize",
        "nvfp4_block_scale_interleave",
    ),
    "__moe_align_block_size": (
        "moe_align_block_size",
    ),
    "__sgl_kernel_moe_align_block_size": (
        "sgl_kernel.moe_align_block_size",
        "jit_kernel.moe_align.moe_align_block_size",
        "triton_utils.moe_align_block_size.moe_align_block_size",
    ),
    "__sgl_kernel_fp8_scaled_mm": (
        "sgl_kernel.fp8_scaled_mm",
        "sgl_kernel.fp8_blockwise_scaled_mm",
        "torch.ops.sgl_kernel.fp8_scaled_mm",
        "torch.ops.sgl_kernel.fp8_scaled_mm.default",
        "torch.ops.sgl_kernel.fp8_blockwise_scaled_mm",
        "torch.ops.sgl_kernel.fp8_blockwise_scaled_mm.default",
        "quantization.fp8.Fp8LinearMethod.apply",
        "quantization.fp8_utils.apply_fp8_linear",
        "quantization.fp8_utils.flashinfer_gemm_w8a8_block_fp8_linear_with_fallback",
        "quantization.fp8_utils.flashinfer_deepgemm_w8a8_block_fp8_linear_with_fallback",
        "quantization.fp8_utils.cutlass_w8a8_block_fp8_linear_with_fallback",
        "quantization.fp8_utils.deepgemm_w8a8_block_fp8_linear_with_fallback",
        "quantization.fp8_utils.triton_w8a8_block_fp8_linear",
        "quantization.fp8_kernel.w8a8_block_fp8_matmul_deepgemm",
        "quantization.fp8_kernel.w8a8_block_fp8_matmul_triton",
        "multimodal_gen.runtime.layers.quantization.weight_only_fp8._apply_srt_w8a8_fp8_linear",
        "multimodal_gen.runtime.layers.quantization.weight_only_fp8._apply_weight_only_fp8_linear",
    ),
    "__void_at_native_sbtopk_gather_top": (
        ".select_experts",
        ".fused_topk",
        ".fused_topk_torch_native",
        ".fused_topk_softmax_torch_raw_logits",
        ".grouped_topk",
        ".biased_grouped_topk",
    ),
    "__void_moe_sum_reduce_warp_per_tok": (
        "moe_sum_reduce",
    ),
    "__void_moe_sum_reduce_kernel_warp": (
        "moe_sum_reduce",
    ),
}

TASK_EXACT_RULES = {
    "qwen36__fp8_bmm": (
        "TRTLLMHAAttnBackend.forward_decode",
        "TRTLLMHAAttnBackend.forward_extend",
        "trtllm_batch_context_with_kv_cache",
        "trtllm_batch_decode_with_kv_cache",
    ),
    "qwen3_coder_next__fp8_bmm": (
        "TritonAttnBackend.forward_decode",
        "TritonAttnBackend.forward_extend",
    ),
    "qwen3_coder__fp8_bmm": (
        "flashinfer.decode.trtllm_batch_decode_with_kv_cache",
        "flashinfer.prefill.trtllm_batch_context_with_kv_cache",
    ),
    "qwen3_next__fp8_bmm": (
        "TritonAttnBackend.forward_decode",
        "TritonAttnBackend.forward_extend",
    ),
    "qwen35__fp8_bmm": (
        "TritonAttnBackend.forward_decode",
        "TritonAttnBackend.forward_extend",
    ),
    "qwen3__fp8_bmm": (
        "flashinfer.decode.trtllm_batch_decode_with_kv_cache",
        "flashinfer.prefill.trtllm_batch_context_with_kv_cache",
    ),
    "gpt_oss_120b__fp8_bmm": (
        "flashinfer.decode.trtllm_batch_decode_with_kv_cache",
        "flashinfer.prefill.trtllm_batch_context_with_kv_cache",
    ),
    "intern_s2_preview__fp8_bmm": (
        "TritonAttnBackend.forward_decode",
        "TritonAttnBackend.forward_extend",
    ),
    "mimo_v25__fp8_bmm": (
        "FlashAttentionBackend.forward_decode",
        "FlashAttentionBackend.forward_extend",
        "flash_attn_with_kvcache",
    ),
    "nemotron3_nano__sglang_flashinfer_bmm_fp8": (
        "flashinfer_bmm_fp8",
        "flashinfer.gemm.bmm_fp8",
    ),
    "nemotron3_nano__sglang_nemotron_mamba2_with_output": (
        "NemotronHMambaDecoderLayer._forward_mamba",
        "nemotron_mamba2_with_output",
        "breakable_nemotron_mamba2_with_output",
        "mamba_chunk_scan_combined",
        "_mamba_chunk_scan_combined_fwd",
        "_chunk_scan_fwd",
        "_chunk_state_fwd",
        "chunk_state_varlen",
        "_state_passing_fwd",
        "causal_conv1d_fn",
        "causal_conv1d_update",
    ),
    "nemotron3_nano__sglang_unified_attention_with_output": (
        "NemotronHAttention.forward",
        "unified_attention_with_output",
    ),
    "nemotron3_nano__static_quant_fp8": (
        "static_quant_fp8",
    ),
    "step35_flash__sgl_kernel_gemma_rmsnorm": (
        "gemma_rmsnorm",
    ),
    "step35_flash__void_moe_top_k_256_float_const_b": (
        ".select_experts",
        ".fused_topk",
        ".fused_topk_torch_native",
        ".fused_topk_softmax_torch_raw_logits",
        ".grouped_topk",
        ".biased_grouped_topk",
    ),
    # Kimi-K3: the dense bf16 GEMM task owns the TGV dispatch entries and the
    # skinny KDA projection GEMVs; attention-residual records the production
    # dispatcher (aggregate_stream is only the dspark aux entry).
    "kimi_k3__sglang_cutedsl_tgv_bf16_gemm": (
        "cutedsl_bf16_gemm",
        "cutedsl_bf16_gemm_out",
        "tiny_n_gemm_bf16",
        "tiny_k_gemm_bf16",
    ),
    "kimi_k3__sglang_attn_res_aggregate": (
        "attn_residual._aggregate",
        "attn_residual.aggregate_stream",
    ),
    "kimi_k3__sglang_kda_fused_decode": (
        "kda_fused_decode",
    ),
}

TASK_DUPLICATE_RULES = {
    "qwen3__void_cublas_lt_split_kreduce_ker": (
        "torch.nn.functional.linear",
    ),
}

DEFAULT_TASK_PREFIX = "glm_52"

DROP_TENSOR_KEYS = {"device", "device_index", "device_type", "requires_grad", "numel"}


def load_jsonl(patterns: list[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for pattern in patterns:
        for path in sorted(glob.glob(pattern)):
            with open(path, encoding="utf-8") as f:
                for line_no, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError as exc:
                        raise ValueError(f"{path}:{line_no}: {exc}") from exc
                    row["_source_file"] = path
                    row["_source_line"] = line_no
                    rows.append(row)
    rows.sort(key=lambda row: (row.get("time", 0), row.get("pid", 0), row.get("call_index", 0)))
    return rows


def load_markers(path: Path | None) -> list[dict[str, Any]]:
    if path is None or not path.exists():
        return []
    markers: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                markers.append(json.loads(line))
    return markers


def scenario_for_time(markers: list[dict[str, Any]], timestamp: float | None) -> str | None:
    if timestamp is None:
        return None
    for marker in markers:
        start = marker.get("start_time")
        end = marker.get("end_time")
        if start is not None and end is not None and start <= timestamp <= end:
            return marker.get("scenario")
    return None


def tensor_paths(value: Any, prefix: str = "") -> list[tuple[str, dict[str, Any]]]:
    out: list[tuple[str, dict[str, Any]]] = []
    if isinstance(value, dict) and value.get("kind") == "tensor":
        out.append((prefix, value))
    elif isinstance(value, dict) and value.get("kind") in {"list", "tuple"}:
        for idx, item in enumerate(value.get("items", [])):
            out.extend(tensor_paths(item, f"{prefix}.{idx}" if prefix else str(idx)))
    elif isinstance(value, dict) and value.get("kind") == "dict":
        for key, item in value.get("items", {}).items():
            out.extend(tensor_paths(item, f"{prefix}.{key}" if prefix else key))
    elif isinstance(value, dict):
        for key, item in value.items():
            out.extend(tensor_paths(item, f"{prefix}.{key}" if prefix else key))
    elif isinstance(value, list):
        for idx, item in enumerate(value):
            out.extend(tensor_paths(item, f"{prefix}.{idx}" if prefix else str(idx)))
    return out


def scalarize(value: Any) -> Any:
    if isinstance(value, dict):
        if value.get("kind") == "tensor":
            return {
                key: val
                for key, val in value.items()
                if key not in DROP_TENSOR_KEYS
            }
        if value.get("kind") in {"list", "tuple"}:
            return [scalarize(item) for item in value.get("items", [])]
        if value.get("kind") == "dict":
            return {key: scalarize(item) for key, item in value.get("items", {}).items()}
        if "repr" in value:
            return {"kind": value.get("kind")}
        return {key: scalarize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [scalarize(item) for item in value]
    return value


def record_signature(row: dict[str, Any]) -> str:
    material = {
        "function": row.get("function"),
        "args": scalarize(row.get("args")),
        "kwargs": scalarize(row.get("kwargs")),
    }
    return json.dumps(material, sort_keys=True, separators=(",", ":"))


def build_task_rules(task_prefix: str, repo_root: Path) -> dict[str, tuple[str, ...]]:
    rules = {
        f"{task_prefix}{suffix}": needles
        for suffix, needles in TASK_SUFFIX_RULES.items()
    }
    rules.update(
        {
            task: needles
            for task, needles in TASK_EXACT_RULES.items()
            if task.startswith(f"{task_prefix}__")
        }
    )
    return {
        task: needles
        for task, needles in rules.items()
        if (repo_root / "llm" / task).exists()
    }


def build_duplicate_task_rules(
    task_prefix: str, repo_root: Path
) -> dict[str, tuple[str, ...]]:
    return {
        task: needles
        for task, needles in TASK_DUPLICATE_RULES.items()
        if task.startswith(f"{task_prefix}__") and (repo_root / "llm" / task).exists()
    }


def task_for_function(function: str, task_rules: dict[str, tuple[str, ...]]) -> str | None:
    for task, needles in task_rules.items():
        if any(needle in function for needle in needles):
            return task
    return None


def duplicate_tasks_for_function(
    function: str, task_rules: dict[str, tuple[str, ...]]
) -> list[str]:
    return [
        task
        for task, needles in task_rules.items()
        if any(needle in function for needle in needles)
    ]


def compact_workload(row: dict[str, Any], scenario: str | None, ordinal: int) -> dict[str, Any]:
    function = row["function"]
    arg_tensors = OrderedDict(tensor_paths(row.get("args", []), "arg"))
    kwarg_tensors = OrderedDict(tensor_paths(row.get("kwargs", {}), "kwarg"))
    tensors = OrderedDict()
    tensors.update((key, scalarize(meta)) for key, meta in arg_tensors.items())
    tensors.update((key, scalarize(meta)) for key, meta in kwarg_tensors.items())
    shape_tag = "_".join(
        "x".join(str(dim) for dim in meta.get("shape", []))
        for meta in list(tensors.values())[:3]
        if meta.get("shape") is not None
    )
    shape_tag = re.sub(r"[^0-9x]+", "_", shape_tag).strip("_")[:80] or "scalar"
    return {
        "id": f"{function.rsplit('.', 1)[-1]}__{scenario or 'unmarked'}__{ordinal:04d}__{shape_tag}",
        "production": True,
        "source": "fresh_sglang_kernel_api_capture",
        "scenario": scenario,
        "function": function,
        "tensors": tensors,
        "args": scalarize(row.get("args", [])),
        "kwargs": scalarize(row.get("kwargs", {})),
        "result": scalarize(row.get("result")),
    }


SHAPE_SECTION = "## Fresh captured kernel API shapes"


def refresh_evidence_doc(
    path: Path, workload_count: int, capture_note: str, functions: list[str]
) -> None:
    """Replace the shape section of profile_evidence.md with the populated one.

    Keeps the generated doc honest after a capture: workload count, capture note
    and covered interfaces instead of the "populate before RLCR" stub.
    """
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    start = text.find(SHAPE_SECTION)
    if start < 0:
        return
    end = text.find("\n## ", start + len(SHAPE_SECTION))
    tail = text[end:] if end >= 0 else ""
    covered = "\n".join(f"- `{fn}`" for fn in functions)
    section = f"""{SHAPE_SECTION}

- Shape source: `docs/captured_kernel_api_shapes.json`
- Standalone workloads: `bench/workloads.json`
- Workload count: {workload_count}
- Capture note: {capture_note}

Functions covered:
{covered}

The old profiler `input_shapes` strings were noisy and are no longer an acceptance source.
Use the task-local workload file above for standalone single-GPU correctness and benchmark work.
"""
    path.write_text(section + tail, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--records", nargs="+", required=True)
    parser.add_argument("--markers", type=Path)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--model", default="zai-org/GLM-5.2-FP8")
    parser.add_argument("--task-prefix", default=DEFAULT_TASK_PREFIX)
    parser.add_argument("--capture-note", default="")
    args = parser.parse_args()

    rows = load_jsonl(args.records)
    markers = load_markers(args.markers)
    task_rules = build_task_rules(args.task_prefix, args.repo_root)
    duplicate_task_rules = build_duplicate_task_rules(args.task_prefix, args.repo_root)
    if not task_rules and not duplicate_task_rules:
        raise SystemExit(f"no task dirs found for task prefix: {args.task_prefix}")
    task_names = list(task_rules)
    task_names.extend(task for task in duplicate_task_rules if task not in task_rules)
    by_task: dict[str, OrderedDict[str, dict[str, Any]]] = {
        task: OrderedDict() for task in task_names
    }
    unmatched = 0

    for row in rows:
        function = row.get("function")
        if not function:
            unmatched += 1
            continue
        task = task_for_function(function, task_rules)
        tasks = []
        if task is not None:
            tasks.append(task)
        for duplicate_task in duplicate_tasks_for_function(function, duplicate_task_rules):
            if duplicate_task not in tasks:
                tasks.append(duplicate_task)
        if not tasks:
            unmatched += 1
            continue
        scenario = scenario_for_time(markers, row.get("time"))
        signature = record_signature(row)
        for target_task in tasks:
            if signature not in by_task[target_task]:
                by_task[target_task][signature] = compact_workload(
                    row, scenario, len(by_task[target_task]) + 1
                )

    summary: dict[str, Any] = {
        "model": args.model,
        "record_count": len(rows),
        "unmatched_record_count": unmatched,
        "marker_count": len(markers),
        "capture_note": args.capture_note,
        "tasks": {},
    }

    for task, workloads_by_sig in by_task.items():
        workloads = list(workloads_by_sig.values())
        task_dir = args.repo_root / "llm" / task
        docs_dir = task_dir / "docs"
        bench_dir = task_dir / "bench"
        docs_dir.mkdir(parents=True, exist_ok=True)
        bench_dir.mkdir(parents=True, exist_ok=True)
        payload = {
            "model": args.model,
            "task": task,
            "source": "fresh_sglang_kernel_api_capture",
            "capture_note": args.capture_note,
            "markers": markers,
            "workload_count": len(workloads),
            "workloads": workloads,
        }
        (docs_dir / "captured_kernel_api_shapes.json").write_text(
            json.dumps(payload, indent=2) + "\n",
            encoding="utf-8",
        )
        (bench_dir / "workloads.json").write_text(
            json.dumps(workloads, indent=2) + "\n",
            encoding="utf-8",
        )
        functions = sorted({w["function"] for w in workloads})
        refresh_evidence_doc(
            docs_dir / "profile_evidence.md", len(workloads), args.capture_note, functions
        )
        summary["tasks"][task] = {
            "workload_count": len(workloads),
            "functions": functions,
        }

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
