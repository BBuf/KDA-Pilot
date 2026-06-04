#!/usr/bin/env python3
"""Entry point kept for the scaffold contract; delegates to bench/benchmark.py.

The authoritative benchmark runner (interleaved A/B, three timing views,
benchmark.csv schema, GPU idleness checks) lives in bench/benchmark.py.
"""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

_TARGET = Path(__file__).resolve().parent / "bench" / "benchmark.py"

if __name__ == "__main__":
    sys.argv[0] = str(_TARGET)
    runpy.run_path(str(_TARGET), run_name="__main__")
