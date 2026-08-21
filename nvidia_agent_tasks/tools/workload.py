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

from payload_match import payload_conflicts  # noqa: E402  shared with tools/coverage.py

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
    if 0 in shape:
        # A zero-element tensor allocated directly has `data_ptr() == 0`, and the
        # kernel is then handed a null pointer for an argument production always
        # hands a valid one: an empty `kv_indices` in production is an empty *slice*
        # of the live index buffer. Triton faults on the address arithmetic even
        # though every load is masked off, which is what killed the glm47 extend rows.
        return torch.zeros(1, device=device, dtype=dt).as_strided(
            shape, tuple(0 for _ in shape))
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
            # `t` is freshly drawn and contiguous here, so `reshape(-1)` is a view;
            # it is only ever read from. Do not copy this idiom to a tensor that has
            # to be written through: `reshape(-1)` on a strided tensor silently
            # returns a *copy*, and writing to the copy leaves the real tensor
            # untouched. Use `view(-1)` (which raises instead of copying) or index
            # along the last dimension.
            flat = t.reshape(-1)
            base[: min(numel, flat.numel())] = flat[: min(numel, flat.numel())]
            t = base.as_strided(shape, tuple(stride))
        except Exception:
            pass
    return t


def clone_kwargs(kwargs: dict) -> dict:
    """Clone a row's tensors, keeping the "this came from the capture" stamp.

    `Tensor.clone()` drops Python attributes, so cloning with a plain comprehension
    hands the copy to RECONSTRUCT as if every tensor had been drawn at random. The
    two benchmark arms then get *different inputs* - one keeps its recorded
    addresses, the other has them derived over the top - which is not a comparison.
    """
    out = {}
    for name, value in kwargs.items():
        if not torch.is_tensor(value):
            out[name] = value
            continue
        copy = value.clone()
        if getattr(value, "_kda_real", False):
            copy._kda_real = True
        out[name] = copy
    return out


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
        if payload_conflicts(c, row):
            continue
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
                # Stamped so RECONSTRUCT leaves it alone: a derived address is a
                # stand-in for data we do not have, and it must never displace data
                # we do. The clone drops the stamp, which is why it is set here on
                # the copy the kernel will actually see rather than on the payload.
                kwargs[name]._kda_real = True
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
    """A row that indexes out of bounds poisons the context for everything after it.

    The launch that did it may not be the call that reports it: an illegal access is
    asynchronous and sticky, so without an explicit synchronize here the error surfaces
    inside a *later* row's graph capture and the whole sweep dies with a raw
    AcceleratorError naming the wrong row. Synchronize first, then probe.
    """
    try:
        torch.cuda.synchronize()
        torch.zeros(1, device="cuda").add_(1)
        torch.cuda.synchronize()
        return True
    except Exception:
        return False
