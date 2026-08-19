"""Turn a task's recorded workload rows into callable inputs.

Shared by `bench_harness.py` (timing) and each task's `tests/test_solution.py`
(correctness), so a candidate is fed exactly the same tensors in both.

Rules, in order:

1. If the task ships a tensor payload whose shapes match the row, use those **real**
   tensors - this is the point of the capture, and it is what keeps a verifier from
   being satisfiable by a shortcut that only works on Gaussians.
2. Otherwise allocate to the recorded shape/dtype, reproducing a non-contiguous view
   when the capture recorded one (several of these kernels really are fed slices of a
   fused buffer).
3. Arguments the capture could not serialize - a plan namedtuple, the instance behind a
   bound method, a Triton dtype - are reported as `needs RECONSTRUCT` and rebuilt by the
   task's `baseline/entry.py::RECONSTRUCT` hook.
"""

from __future__ import annotations

import glob
import json
import os

import torch

DTYPES = {
    "bfloat16": torch.bfloat16, "float16": torch.float16, "float32": torch.float32,
    "float64": torch.float64, "int64": torch.int64, "int32": torch.int32,
    "int16": torch.int16, "int8": torch.int8, "uint8": torch.uint8, "bool": torch.bool,
    "float8_e4m3fn": getattr(torch, "float8_e4m3fn", torch.uint8),
    "complex64": torch.complex64,
}


def alloc(info: dict, device: str = "cuda") -> torch.Tensor:
    dt = DTYPES.get(info["dtype"], torch.float32)
    shape = tuple(info["shape"])
    if dt.is_floating_point:
        t = torch.randn(shape, device=device, dtype=torch.float32).to(dt)
    elif dt.is_complex:
        t = torch.randn(shape, device=device, dtype=torch.float32).to(torch.complex64)
    else:
        t = torch.zeros(shape, device=device, dtype=dt)
    stride = info.get("stride")
    if stride and not info.get("contiguous", True):
        try:
            numel = 1
            for s, st in zip(shape, stride):
                numel = max(numel, (s - 1) * st + 1)
            base = torch.zeros(numel, device=device, dtype=dt)
            flat = t.reshape(-1)
            base[: min(numel, flat.numel())] = flat[: min(numel, flat.numel())]
            t = base.as_strided(shape, tuple(stride))
        except Exception:
            pass
    return t


def holds_tensor_meta(x) -> bool:
    if isinstance(x, dict):
        return "shape" in x and "dtype" in x or any(holds_tensor_meta(v) for v in x.values())
    if isinstance(x, list):
        return any(holds_tensor_meta(v) for v in x)
    return False


def _row_shapes(row: dict) -> dict:
    return {k: tuple(v["shape"]) for k, v in row["args"].items()
            if isinstance(v, dict) and "shape" in v}


def load_payload(task_dir: str, row: dict) -> dict:
    """The shipped payload folder whose tensor shapes best match this row."""
    roots = [d for d in glob.glob(os.path.join(task_dir, "bench", "tensors*")) if os.path.isdir(d)]
    cands = []
    for root in roots:
        for dirpath, _, files in os.walk(root):
            if "meta.json" in files:
                cands.append(dirpath)
    want = _row_shapes(row)
    best, best_score = {}, 0
    for c in cands:
        meta = json.load(open(os.path.join(c, "meta.json")))
        got = {}
        static = os.path.join(os.path.dirname(c), "static")
        for name, info in meta.get("tensors", {}).items():
            for base in (c, static):
                p = os.path.join(base, info.get("file", ""))
                if os.path.exists(p):
                    got[name] = torch.load(p, map_location="cuda")
                    break
        score = sum(1 for k, sh in want.items()
                    if torch.is_tensor(got.get("in_" + k)) and tuple(got["in_" + k].shape) == sh)
        if score > best_score:
            best, best_score = dict(got, __meta__=meta, __dir__=c), score
    return best


def build_inputs(task_dir: str, row: dict) -> dict:
    """-> {"kwargs": ..., "source": {arg: real|allocated|scalar|config|needs ...}, "payload": ...}"""
    payload = load_payload(task_dir, row)
    kwargs, source = {}, {}
    for name, info in row["args"].items():
        if isinstance(info, dict) and "shape" in info:
            real = payload.get("in_" + name)
            if real is not None and list(real.shape) == list(info["shape"]):
                kwargs[name] = real.clone()
                source[name] = "real"
            else:
                kwargs[name] = alloc(info)
                source[name] = "allocated"
        elif isinstance(info, dict) and "repr" in info:
            source[name] = "needs RECONSTRUCT (%s)" % info["repr"]
        elif isinstance(info, (dict, list)) and holds_tensor_meta(info):
            source[name] = "needs RECONSTRUCT (structured arg with tensors)"
        else:
            kwargs[name] = info
            source[name] = "config" if isinstance(info, (dict, list)) else "scalar"
    risky = [n for n, v in kwargs.items()
             if torch.is_tensor(v) and not v.is_floating_point() and source.get(n) == "allocated"
             and v.numel() > 1]
    return {"kwargs": kwargs, "source": source, "payload": payload,
            "allocated_index_args": risky}


def iter_rows(task_dir: str, op: str = "", limit: int = 0):
    """Yield (op, row) for every workload row in the task."""
    for wf in sorted(glob.glob(os.path.join(task_dir, "bench", "workloads*.json"))):
        for o in json.load(open(wf))["ops"]:
            if op and o["op"] != op:
                continue
            for r in (o["rows"][:limit] if limit else o["rows"]):
                yield o["op"], r


def chains(task_dir: str):
    """Yield every shipped state chain as (dir, steps, static_dir_or_None)."""
    for root in glob.glob(os.path.join(task_dir, "bench", "tensors*")):
        for dirpath, dirnames, _ in os.walk(root):
            steps = sorted(d for d in dirnames if d.startswith("step"))
            if len(steps) >= 2:
                static = os.path.join(dirpath, "static")
                yield dirpath, [os.path.join(dirpath, s) for s in steps], (
                    static if os.path.isdir(static) else None)


def cuda_alive() -> bool:
    """A row that indexes out of bounds poisons the context for everything after it."""
    try:
        torch.zeros(1, device="cuda").add_(1)
        torch.cuda.synchronize()
        return True
    except Exception:
        return False
