#!/usr/bin/env python3
"""Send small Kimi-K3 requests and mark shape-capture scenarios.

Mirrors ``run_glm52_shape_capture_requests.py``: the sitecustomize hook records
the Python kernel API call contracts while this driver walks the cookbook
scenario shapes and appends ``scenario_markers.jsonl`` so
``aggregate_sglang_shape_capture.py`` can attribute every record to a scenario.

Kimi-K3 is a hybrid model (69 KDA linear-attention layers + 24 MLA layers, 92
latent-MoE layers), so the driver covers both a long prefill (exercises the
prefill GEMM / MoE / attention shapes) and single-stream plus concurrent decode
(the KDA fused decode, tiny GEMV chains, and M=1 MoE front shapes).
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import time
import urllib.request
from pathlib import Path
from typing import Any


def post_json(base_url: str, payload: dict[str, Any], timeout: int) -> str:
    req = urllib.request.Request(
        base_url.rstrip("/") + "/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def append_marker(
    marker_path: Path,
    scenario: str,
    start_time: float,
    end_time: float,
    payload: dict[str, Any],
) -> None:
    row = {
        "scenario": scenario,
        "start_time": start_time,
        "end_time": end_time,
        "payload": payload,
    }
    marker_path.parent.mkdir(parents=True, exist_ok=True)
    with marker_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, sort_keys=True) + "\n")


def run_one(
    base_url: str,
    marker_path: Path,
    scenario: str,
    text: str,
    max_new_tokens: int,
    timeout: int,
) -> None:
    payload = {
        "text": text,
        "sampling_params": {
            "temperature": 0,
            "max_new_tokens": max_new_tokens,
            "ignore_eos": True,
        },
    }
    start_time = time.time()
    output = post_json(base_url, payload, timeout)
    end_time = time.time()
    append_marker(
        marker_path,
        scenario,
        start_time,
        end_time,
        {"text_chars": len(text), "max_new_tokens": max_new_tokens},
    )
    print(
        scenario,
        "seconds",
        round(end_time - start_time, 2),
        "response_prefix",
        output[:180].replace("\n", " "),
        flush=True,
    )


def run_batch(
    base_url: str,
    marker_path: Path,
    scenario: str,
    text: str,
    concurrency: int,
    max_new_tokens: int,
    timeout: int,
) -> None:
    payloads = [
        {
            "text": f"{text}\nConcurrent request {idx}.",
            "sampling_params": {
                "temperature": 0,
                "max_new_tokens": max_new_tokens,
                "ignore_eos": True,
            },
        }
        for idx in range(concurrency)
    ]
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        outputs = list(
            executor.map(lambda payload: post_json(base_url, payload, timeout), payloads)
        )
    end_time = time.time()
    append_marker(
        marker_path,
        scenario,
        start_time,
        end_time,
        {
            "concurrency": concurrency,
            "text_chars": len(text),
            "max_new_tokens": max_new_tokens,
        },
    )
    print(
        scenario,
        "seconds",
        round(end_time - start_time, 2),
        "responses",
        len(outputs),
        "first_prefix",
        outputs[0][:180].replace("\n", " ") if outputs else "",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:30001")
    parser.add_argument(
        "--marker-path",
        type=Path,
        default=Path("/tmp/kda_kernel_shape_capture/scenario_markers.jsonl"),
    )
    parser.add_argument("--timeout", type=int, default=3600)
    parser.add_argument("--batch-concurrency", type=int, default=16)
    args = parser.parse_args()

    long_text = (
        "Kimi-K3 shape capture request. The kernel workload should reflect real "
        "prefill and decode tensors for the hybrid KDA/MLA stack. "
        * 150
    )
    short_text = "Kimi-K3 short decode shape capture. " * 16

    run_one(
        args.base_url,
        args.marker_path,
        "sharegpt_low_long_prompt",
        long_text,
        max_new_tokens=8,
        timeout=args.timeout,
    )
    run_one(
        args.base_url,
        args.marker_path,
        "random_low_short_prompt",
        short_text,
        max_new_tokens=16,
        timeout=args.timeout,
    )
    run_batch(
        args.base_url,
        args.marker_path,
        "sharegpt_mid_concurrency16_long_prompt",
        long_text,
        concurrency=args.batch_concurrency,
        max_new_tokens=4,
        timeout=args.timeout,
    )


if __name__ == "__main__":
    main()
