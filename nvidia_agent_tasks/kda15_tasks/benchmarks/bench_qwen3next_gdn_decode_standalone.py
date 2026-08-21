#!/usr/bin/env python3
"""Standalone benchmark for Qwen3-Next packed GDN decode."""

from __future__ import annotations

import hashlib
from pathlib import Path
import math

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

# SGLang's own test for this kernel family:
# test/registered/kernels/ops/attention/test_kda_fused_decode.py:207-208.
ATOL = 2e-2
RTOL = 2e-2
REQUIRED_MATCHED_RATIO = None

DEFINITION = "qwen3next_gdn_packed_decode_hv4_d128"
WORKLOADS_PATH = CONTEST_ROOT / ("workloads/gdn/%s.jsonl" % DEFINITION)
KERNEL_PATH = env_path("BENCH_QWEN3NEXT_GDN_DECODE_KERNEL", CANDIDATE_ROOT / "gdn_decode.py")
BASELINE_SOLUTION_JSON = None  # resolved in _sole_baseline() below

NUM_V_HEADS = 4
HEAD_V_DIM = 128
HEAD_K_DIM = 128
QKV_DIM = 1024


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


def make_inputs(entry, device):
    axes = entry["axes"]
    num_seqs = int(axes["num_seqs"])
    num_slots = int(axes["num_slots"])
    torch.manual_seed(_entry_seed(entry))
    recorded = entry["raw"]["inputs"] if entry["raw"] is not None else {}

    def blob_or_draw(name, shape, dtype, spread=1.0):
        spec = recorded.get(name)
        if isinstance(spec, dict) and spec.get("type") == "safetensors":
            return load_safetensor(spec, device)
        drawn = torch.randn(shape, dtype=torch.float32, device=device) * spread
        return drawn.to(dtype)

    mixed_qkv = blob_or_draw("mixed_qkv", (num_seqs, QKV_DIM), torch.bfloat16, 0.5)
    a = blob_or_draw("a", (num_seqs, NUM_V_HEADS), torch.bfloat16, 1.5)
    b = blob_or_draw("b", (num_seqs, NUM_V_HEADS), torch.bfloat16, 1.0)
    A_log = blob_or_draw("A_log", (NUM_V_HEADS,), torch.float32, 0.5)
    dt_bias = blob_or_draw("dt_bias", (NUM_V_HEADS,), torch.bfloat16, 1.0)

    slots_spec = recorded.get("cache_indices")
    if isinstance(slots_spec, dict) and slots_spec.get("type") == "safetensors":
        cache_indices = load_safetensor(slots_spec, device)
    else:
        # Distinct slots by construction: two sequences sharing a slot is a
        # read-modify-write race, not a slower kernel, and the pool is fresh per row
        # so which distinct slots they are cannot matter.
        cache_indices = torch.arange(num_seqs, dtype=torch.int32, device=device)

    # Recorded geometry, so the state stride and the slot addressing are the captured
    # ones; only the slots this batch owns are written. Zero-filled rather than `empty`
    # so an untouched slot can never introduce a NaN into a comparison both arms have
    # to agree on - the state pool is part of this kernel's output.
    ssm_states = torch.zeros(
        (num_slots, NUM_V_HEADS, HEAD_V_DIM, HEAD_K_DIM), dtype=torch.float32, device=device
    )
    slots = cache_indices.long()
    state_spec = recorded.get("ssm_state_values")
    if isinstance(state_spec, dict) and state_spec.get("type") == "safetensors":
        ssm_states[slots] = load_safetensor(state_spec, device).to(ssm_states.dtype)
    else:
        ssm_states[slots] = (
            torch.randn(
                (slots.numel(), NUM_V_HEADS, HEAD_V_DIM, HEAD_K_DIM),
                dtype=torch.float32,
                device=device,
            )
            * 0.05
        )

    scale = (
        float(recorded["scale"]["value"])
        if "scale" in recorded
        else 1.0 / math.sqrt(HEAD_K_DIM)
    )
    return [
        mixed_qkv,
        a,
        b,
        A_log,
        dt_bias,
        scale,
        ssm_states,
        cache_indices,
        NUM_V_HEADS,
        HEAD_V_DIM,
    ]


def baseline_decode(*args):
    global _BASELINE_RUN
    if _BASELINE_RUN is None:
        _BASELINE_RUN = load_solution_json(
            env_path("BENCH_QWEN3NEXT_GDN_DECODE_BASELINE_SOLUTION_JSON", _sole_baseline("gdn", DEFINITION)), "embedded_qwen3next_gdn_decode_baseline"
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
        group_axis="num_seqs",
    )


def main():
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is required")
    device = choose_device(DEVICE)
    workloads = make_workloads()
    official = [entry for entry in workloads if entry["suite"] == "official"]
    large = [entry for entry in workloads if entry["suite"] == "large"]
    candidate = load_kernel(KERNEL_PATH, "candidate_qwen3next_gdn_decode")
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
            group_axis="num_seqs",
        )


if __name__ == "__main__":
    main()
