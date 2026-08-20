#!/usr/bin/env python3
"""Standalone benchmark for GLM-4.7-Flash MLA grouped decode attention."""

from __future__ import annotations

import hashlib
from pathlib import Path

import torch
from bench_common import (
    CANDIDATE_ROOT,
    CONTEST_ROOT,
    choose_device,
    env_int,
    env_path,
    env_str,
    load_kernel,
    load_safetensor,
    load_solution_json,
    load_workloads,
    make_entries,
    run_benchmark,
)

DEVICE = env_str("BENCH_DEVICE", "auto")
WARMUP = env_int("BENCH_WARMUP", 3)
ITERS = env_int("BENCH_ITERS", 50)
TRIALS = env_int("BENCH_TRIALS", 5)
MAX_OFFICIAL_WORKLOADS = env_int("BENCH_MAX_OFFICIAL", 0)
FAST_MIX = env_int("BENCH_FAST_MIX", 0)
INCLUDE_OFFICIAL_WORKLOADS = env_int("BENCH_INCLUDE_OFFICIAL", 1)
INCLUDE_LARGE_WORKLOADS = env_int("BENCH_INCLUDE_LARGE", 1)

# SGLang's own test for this kernel:
# test/registered/attention/test_triton_attention_kernels.py:309.
ATOL = 1e-3
RTOL = 1e-2
REQUIRED_MATCHED_RATIO = None

DEFINITION = "glm47_mla_decode_grouped_h20_ckv512_kpe64"
WORKLOADS_PATH = CONTEST_ROOT / ("workloads/attention/%s.jsonl" % DEFINITION)
KERNEL_PATH = env_path("BENCH_GLM47_MLA_DECODE_KERNEL", CANDIDATE_ROOT / "mla_decode.py")
BASELINE_SOLUTION_JSON = None  # resolved in _sole_baseline() below

NUM_Q_HEADS = 20
QK_HEAD_DIM = 576
KV_LORA_RANK = 512


def _sole_baseline(group: str, definition: str) -> Path:
    """The one baseline package shipped for this definition.

    Resolved rather than hardcoded: the package name carries a digest of its own
    sources, so pinning the digest in this file means every edit to the baseline
    silently breaks the benchmark instead of being picked up.
    """
    folder = CONTEST_ROOT / "solutions/baseline" / group / definition
    found = sorted(folder.glob("*.json"))
    if len(found) != 1:
        raise RuntimeError(
            "expected exactly one baseline package in %s, found %d" % (folder, len(found))
        )
    return found[0]

_BASELINE_RUN = None
OFFICIAL_BENCHMARK_NAME = DEFINITION + "_official"


def make_workloads():
    return make_entries(
        load_workloads(WORKLOADS_PATH, 0),
        include_official=bool(INCLUDE_OFFICIAL_WORKLOADS),
        include_large=bool(INCLUDE_LARGE_WORKLOADS),
        max_official=MAX_OFFICIAL_WORKLOADS,
        fast_mix=FAST_MIX,
    )


def _entry_seed(entry):
    raw = f"{entry['suite']}:{entry['id']}:{entry['axes']}".encode()
    return int(hashlib.sha256(raw).hexdigest()[:8], 16)


def _balanced_page_table(num_seqs: int, total_pages: int, pool_rows: int, device):
    """Page tables for a generated row, when no capture is attached."""
    base, extra = divmod(total_pages, num_seqs)
    lengths = torch.full((num_seqs,), base, dtype=torch.int32, device=device)
    if extra:
        lengths[:extra] += 1
    indptr = torch.cat(
        [torch.zeros(1, dtype=torch.int32, device=device), lengths.cumsum(0).int()]
    )
    stride = max(pool_rows // max(total_pages, 1), 1)
    indices = (
        torch.arange(total_pages, dtype=torch.int64, device=device) * stride
    ) % pool_rows
    return indptr, indices


def make_inputs(entry, device):
    axes = entry["axes"]
    num_seqs = int(axes["num_seqs"])
    pool_rows = int(axes["kv_pool_rows"])
    max_kv_splits = int(axes["max_kv_splits"])
    torch.manual_seed(_entry_seed(entry))

    if entry["raw"] is not None:
        recorded = entry["raw"]["inputs"]
        query = load_safetensor(recorded["q"], device)
        kv_indptr = load_safetensor(recorded["kv_indptr"], device)
        kv_indices = load_safetensor(recorded["kv_indices"], device)
        num_kv_splits = load_safetensor(recorded["num_kv_splits"], device)
        sm_scale_withk = float(recorded["sm_scale_withk"]["value"])
        v_scale = float(recorded["v_scale"]["value"])
        logit_cap = float(recorded["logit_cap"]["value"])
        page_size = int(recorded["page_size"]["value"])
        has_mla = bool(recorded["has_mla"]["value"])
        use_pdl = bool(recorded["use_pdl"]["value"])
    else:
        kv_indptr, kv_indices = _balanced_page_table(
            num_seqs, int(axes["len_kv_indices"]), pool_rows, device
        )
        query = (
            torch.randn(
                (num_seqs, NUM_Q_HEADS, QK_HEAD_DIM), dtype=torch.float32, device=device
            )
            * 0.1
        ).to(torch.bfloat16)
        num_kv_splits = torch.full(
            (num_seqs,), max_kv_splits, dtype=torch.int32, device=device
        )
        sm_scale_withk, v_scale, logit_cap = QK_HEAD_DIM**-0.5, 1.0, 0.0
        page_size, has_mla, use_pdl = 1, True, True

    # The pool carries the recorded geometry so addressing and strides are the captured
    # ones, and only the pages this row reads are written. Zero-filled rather than
    # `empty`, so an untouched page can never introduce a NaN into a comparison that
    # both arms are supposed to agree on.
    k_buffer = torch.zeros((pool_rows, 1, QK_HEAD_DIM), dtype=torch.bfloat16, device=device)
    touched = kv_indices.long().unique()
    k_buffer[touched] = (
        torch.randn(
            (touched.numel(), 1, QK_HEAD_DIM), dtype=torch.float32, device=device
        )
        * 0.1
    ).to(torch.bfloat16)
    # Absorbed MLA reads the value out of the same row, truncated to the compressed-KV
    # width: a view, not a copy, exactly as the capture recorded it (stride 576 on a
    # 512-wide tensor). Materialising it separately would let the two disagree.
    v_buffer = k_buffer[:, :, :KV_LORA_RANK]

    output = torch.zeros(
        (num_seqs, NUM_Q_HEADS, KV_LORA_RANK), dtype=torch.bfloat16, device=device
    )
    attn_logits = torch.zeros(
        (num_seqs, NUM_Q_HEADS, max_kv_splits, KV_LORA_RANK),
        dtype=torch.float32,
        device=device,
    )
    attn_lse = torch.zeros(
        (num_seqs, NUM_Q_HEADS, max_kv_splits), dtype=torch.float32, device=device
    )
    return [
        query,
        k_buffer,
        v_buffer,
        output,
        kv_indptr,
        kv_indices,
        attn_logits,
        attn_lse,
        num_kv_splits,
        max_kv_splits,
        sm_scale_withk,
        v_scale,
        logit_cap,
        None,
        -1,
        has_mla,
        use_pdl,
        page_size,
    ]


def baseline_decode(*args):
    global _BASELINE_RUN
    if _BASELINE_RUN is None:
        _BASELINE_RUN = load_solution_json(
            env_path("BENCH_GLM47_MLA_DECODE_BASELINE_SOLUTION_JSON", _sole_baseline("attention", DEFINITION)), "embedded_glm47_mla_decode_baseline"
        )
    return _BASELINE_RUN(*args)


def run_official_benchmark(candidate, device, workloads):
    return run_benchmark(
        name=OFFICIAL_BENCHMARK_NAME,
        workloads=workloads,
        make_inputs=make_inputs,
        baseline_fn=None,
        candidate_fn=candidate,
        reference_fn=baseline_decode,
        timing_baseline_fn=baseline_decode,
        device=device,
        warmup=WARMUP,
        iters=ITERS,
        trials=TRIALS,
        atol=ATOL,
        rtol=RTOL,
        required_matched_ratio=REQUIRED_MATCHED_RATIO,
        group_axis="len_kv_indices",
    )


def main():
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is required")
    device = choose_device(DEVICE)
    workloads = make_workloads()
    official = [entry for entry in workloads if entry["suite"] == "official"]
    large = [entry for entry in workloads if entry["suite"] == "large"]
    candidate = load_kernel(KERNEL_PATH, "candidate_glm47_mla_decode")
    if official:
        run_official_benchmark(candidate, device, official)
    if large:
        run_benchmark(
            name=DEFINITION + "_large_embedded",
            workloads=large,
            make_inputs=make_inputs,
            baseline_fn=baseline_decode,
            candidate_fn=candidate,
            device=device,
            warmup=WARMUP,
            iters=ITERS,
            trials=TRIALS,
            atol=ATOL,
            rtol=RTOL,
            required_matched_ratio=REQUIRED_MATCHED_RATIO,
            group_axis="len_kv_indices",
        )


if __name__ == "__main__":
    main()
