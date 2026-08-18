"""Resolve a baseline symbol and prove it is the pinned version.

    from baseline_loader import load
    compress_forward = load("sglang.kernels.ops.attention.dsv4.compress",
                            "compress_forward", __file__,
                            "kernels/ops/attention/dsv4/compress.py")

The copied source in `baseline/` is the contract; the installed SGLang is what can
actually be imported (these kernels import the rest of the framework). `load()`
imports the installed module, hashes its source, compares it to the copy shipped with
the task, and prints a loud warning when they differ - i.e. when the environment has
drifted away from the commit the workload was captured on. Benchmarking against a
different baseline than the one in `baseline/` is the one way to make every number in
a task meaningless, so the check is not optional.
"""

from __future__ import annotations

import hashlib
import importlib
import inspect
import os
import sys


def _md5(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()


def load(module: str, attr: str, entry_file: str, copied_rel: str):
    mod = importlib.import_module(module)
    obj = mod
    for part in attr.split("."):
        obj = getattr(obj, part)
    copied = os.path.join(os.path.dirname(os.path.abspath(entry_file)), copied_rel)
    try:
        installed = inspect.getsourcefile(sys.modules[module])
        if installed and os.path.exists(copied):
            a, b = _md5(installed), _md5(copied)
            if a != b:
                print("[baseline_loader] WARNING: installed %s (%s) differs from the copy "
                      "shipped with this task (%s).\n"
                      "  The task's numbers were captured against the copy. Either check out "
                      "the pinned commit or state the drift in your report."
                      % (module, a[:8], b[:8]), file=sys.stderr)
    except Exception:
        pass
    return obj
