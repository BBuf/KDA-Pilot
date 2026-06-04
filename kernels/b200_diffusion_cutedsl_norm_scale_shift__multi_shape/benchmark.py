#!/usr/bin/env python3
"""Benchmark entry point for ``b200_diffusion_cutedsl_norm_scale_shift__multi_shape``.

Thin delegator: the canonical harness lives in ``bench/benchmark.py`` (frozen
captured workloads, interleaved baseline/candidate A/B, end-to-end + device
timing modes, provenance columns, append-only ``benchmark.csv``). Run with the
same arguments, e.g.::

    CUDA_VISIBLE_DEVICES=0 python benchmark.py --impl both --gpu-id 0 --run-id r1
    python benchmark.py --report --run-id r1
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

KERNEL_DIR = Path(__file__).resolve().parent


def _load_bench():
    name = "kda_benchmark_lib"
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(
        name, KERNEL_DIR / "bench" / "benchmark.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


if __name__ == "__main__":
    _load_bench().main()
