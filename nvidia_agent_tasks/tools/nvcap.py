"""Real-workload kernel capture hook for SGLang (shapes + tensor payloads).

Drop this file on ``PYTHONPATH`` as ``sitecustomize.py`` (or import it before the
model is built) and point ``NVCAP_CONFIG`` at a JSON target list.  Every wrapped
call is recorded twice:

1. **shape manifest** (always, cheap, metadata only) - every call's tensor
   shapes / dtypes / strides / contiguity / scalar args, aggregated by signature
   with an occurrence count, split into ``real_workload_shapes`` and
   ``warmup_only_shapes``.
2. **tensor payload** (budgeted) - one folder per distinct shape signature with
   the real inputs, the real outputs, and (for state-carrying ops) the state
   rows before and after the call, so a candidate kernel can be verified against
   ground truth produced by the real model instead of synthetic gaussians.

The active workload label is read from ``<NVCAP_DIR>/GROUP`` on every call, so a
single server process can walk a whole capture matrix (sequence-length x
concurrency x dataset).  Calls seen while that file is absent are tagged
``warmup`` - startup, CUDA-graph capture and autotuning must not be mistaken for
production traffic.

Environment:
  NVCAP_DIR                  output directory (required)
  NVCAP_CONFIG               JSON target list (required)
  NVCAP_GROUP_MB             tensor byte budget per group        (default 80)
  NVCAP_MAX_SHAPES_PER_OP    tensor folders per (group, op)      (default 6)
  NVCAP_RANK                 which local rank saves tensors      (default 0)
  NVCAP_OPS                  comma-separated op allowlist        (default all)
  NVCAP_NO_TENSORS=1         manifest only, skip tensor payloads
  NVCAP_MAX_TENSOR_MB        per-tensor payload cap              (default 96)
  NVCAP_TARGET_SIGS          JSON {op: [signature, ...]} - capture tensors for exactly
                             these call signatures (the rows a task actually ships) and
                             ignore the per-op/byte budgets for them

Config format (list of targets):
  [
    {"module": "sglang.srt.layers.attention.mamba.ops.ssd_combined",
     "attr":   "_mamba_chunk_scan_combined_fwd",
     "op":     "mamba2_chunk_scan_combined",
     "state_args": ["initial_states"],       # snapshot before + after the call
     "index_arg":  "cache_indices",          # keep only these state rows
     "shape_from": ["x", "dt"],              # tensors that name the folder
     "gather_args": {"k_buffer": "kv_indices"},  # save only the rows a call reads
     "skip_args": ["w1", "w2"],              # metadata only (expert weights etc.)
     "tensors": true}
  ]

Only ``module`` and ``attr`` are required.
"""

from __future__ import annotations

import importlib
import importlib.abc
import importlib.machinery
import inspect
import json
import os
import sys
import threading
import traceback

_DIR = os.environ.get("NVCAP_DIR")
_CONFIG = os.environ.get("NVCAP_CONFIG")
_BUDGET = int(float(os.environ.get("NVCAP_GROUP_MB", "80")) * 1024 * 1024)
_MAX_PER_OP = int(os.environ.get("NVCAP_MAX_SHAPES_PER_OP", "6"))
_CAPTURE_RANK = int(os.environ.get("NVCAP_RANK", "0"))
_OPS = [x for x in os.environ.get("NVCAP_OPS", "").split(",") if x]
_NO_TENSORS = os.environ.get("NVCAP_NO_TENSORS", "0") == "1"
_MAX_TENSOR = int(float(os.environ.get("NVCAP_MAX_TENSOR_MB", "96")) * 1024 * 1024)
_TARGETS_PATH = os.environ.get("NVCAP_TARGET_SIGS")
_TARGET_SIGS: dict = {}
if _TARGETS_PATH:
    try:
        with open(_TARGETS_PATH) as _fh:
            _TARGET_SIGS = {k: set(v) for k, v in json.load(_fh).items()}
    except Exception as _exc:  # pragma: no cover
        print("[nvcap] cannot read NVCAP_TARGET_SIGS=%s: %r" % (_TARGETS_PATH, _exc),
              file=sys.stderr)

_lock = threading.RLock()
_manifest: dict = {}          # sig_key -> record
_bytes: dict = {}             # group -> bytes written
_shapes_per_op: dict = {}     # (group, op) -> folders written
_saved: set = set()           # (group, shape_id) already saved
_steps: dict = {}             # (group, shape_id) -> consecutive steps saved
_chain_id: dict = {}          # (group, shape_id) -> identity of the chained instance
_targets: list = []
_installed = False
_log_once: set = set()
_pending: list = []           # specs whose module was not patchable yet
_calls_seen = [0]


def _warn(msg: str) -> None:
    if msg in _log_once:
        return
    _log_once.add(msg)
    print("[nvcap] " + msg, file=sys.stderr, flush=True)


# --------------------------------------------------------------------------- #
# metadata helpers
# --------------------------------------------------------------------------- #
def _torch():
    return sys.modules.get("torch")


def _is_tensor(x) -> bool:
    t = _torch()
    return t is not None and t.is_tensor(x)


def _tinfo(t) -> dict:
    return {
        "shape": list(t.shape),
        "dtype": str(t.dtype).replace("torch.", ""),
        "stride": list(t.stride()),
        "contiguous": bool(t.is_contiguous()),
        "device": str(t.device).split(":")[0],
        "numel": int(t.numel()),
        "bytes": int(t.numel() * t.element_size()),
    }


def _describe(x, depth: int = 0):
    """JSON-able description of an argument: tensors -> metadata, scalars -> value."""
    if _is_tensor(x):
        return _tinfo(x)
    if isinstance(x, (int, float, bool)) or x is None:
        return x
    if isinstance(x, str):
        return x[:120]
    if isinstance(x, (list, tuple)) and depth < 2:
        if len(x) > 16:
            return {"seq_len": len(x), "head": [_describe(v, depth + 1) for v in x[:4]]}
        return [_describe(v, depth + 1) for v in x]
    if isinstance(x, dict) and depth < 2:
        return {str(k): _describe(v, depth + 1) for k, v in list(x.items())[:16]}
    return {"repr": type(x).__name__}


def _rank() -> int:
    t = _torch()
    try:
        if t is not None and t.cuda.is_initialized():
            return int(t.cuda.current_device())
    except Exception:
        pass
    return int(os.environ.get("LOCAL_RANK", os.environ.get("RANK", "0")))


def _group():
    try:
        with open(os.path.join(_DIR, "GROUP")) as fh:
            g = fh.read().strip()
        return g or "warmup"
    except Exception:
        return "warmup"


# --------------------------------------------------------------------------- #
# manifest
# --------------------------------------------------------------------------- #
def _sig_of(bound: dict) -> str:
    parts = []
    for k, v in bound.items():
        if _is_tensor(v):
            parts.append("%s=%s:%s%s" % (
                k, "x".join(str(s) for s in v.shape),
                str(v.dtype).replace("torch.", ""),
                "" if v.is_contiguous() else "!c"))
        elif isinstance(v, (int, float, bool)) and not isinstance(v, bool):
            parts.append("%s=%s" % (k, v))
    return "|".join(parts)


def _record_manifest(op: str, group: str, bound: dict, out) -> bool:
    """Aggregate one call into the manifest; True when the signature is new."""
    sig = _sig_of(bound)
    key = (op, group, sig)
    is_new = False
    with _lock:
        rec = _manifest.get(key)
        if rec is None:
            is_new = True
            rec = {
                "op": op,
                "group": group,
                "signature": sig,
                "count": 0,
                "args": {k: _describe(v) for k, v in bound.items()},
                "output": _describe(out) if not isinstance(out, (tuple, list))
                else [_describe(o) for o in out[:6]],
            }
            _manifest[key] = rec
        rec["count"] += 1
    return is_new


def dump_manifest() -> None:
    if not _DIR:
        return
    real, warm = [], []
    with _lock:
        recs = list(_manifest.values())
    for r in recs:
        (warm if r["group"] == "warmup" else real).append(r)
    real.sort(key=lambda r: -r["count"])
    warm.sort(key=lambda r: -r["count"])
    out = {
        "capture_tool": "nvcap.py",
        "pid": os.getpid(),
        "note": ("real_workload_shapes excludes every call seen while no GROUP "
                 "file was present (startup, CUDA-graph capture, autotune). "
                 "count is per capture group."),
        "real_workload_shapes": real,
        "warmup_only_shapes": warm,
    }
    # one file per process: SGLang runs TP workers / diffusion workers in
    # separate processes, and a process that never called a wrapped op would
    # otherwise clobber a busy process's manifest. merge_manifests.py combines them.
    path = os.path.join(_DIR, "shape_manifest_pid%d.json" % os.getpid())
    tmp = path + ".tmp"
    try:
        os.makedirs(_DIR, exist_ok=True)
        with open(tmp, "w") as fh:
            json.dump(out, fh, indent=2)
        os.replace(tmp, path)
    except Exception as exc:
        _warn("manifest dump failed: %r" % (exc,))


# --------------------------------------------------------------------------- #
# tensor payloads
# --------------------------------------------------------------------------- #
def _cpu(t):
    return t.detach().contiguous().to("cpu", copy=True)


def _rows(state, idx):
    """Slice the rows a call actually touched out of a big state pool.

    Returns (cpu_slice, gpu_index). The index is returned on its ORIGINAL device:
    slicing the post-call state with a CPU index would raise, which silently cost
    us the state_after half of a capture once.
    """
    if not _is_tensor(state):
        return None, None
    if not _is_tensor(idx):
        return _cpu(state), None
    try:
        good = idx[idx >= 0]
        if good.numel() == 0:
            return None, None
        return state.index_select(0, good).detach().to("cpu", copy=True), good
    except Exception:
        return None, None


def _shape_id(op: str, bound: dict, spec: dict) -> str:
    names = spec.get("shape_from") or []
    bits = []
    for n in names:
        v = bound.get(n)
        if _is_tensor(v):
            bits.append("%s%s" % (n, "x".join(str(s) for s in v.shape)))
    if not bits:
        for k, v in bound.items():
            if _is_tensor(v):
                bits.append("%s%s" % (k, "x".join(str(s) for s in v.shape)))
            if len(bits) >= 2:
                break
    return (op + "__" + "_".join(bits))[:150] or op


def _save_payload(op, group, bound, out, spec, state_before, state_rows, step=0):
    d = os.path.join(_DIR, "tensors", group, _shape_id(op, bound, spec))
    if int(spec.get("chain", 1)) > 1:
        d = os.path.join(d, "step%03d" % step)
    os.makedirs(d, exist_ok=True)
    t = _torch()
    meta = {"op": op, "group": group, "scalars": {}, "tensors": {},
            "metadata_only": {}, "gathered": {}}
    written = 0
    skip = set(spec.get("skip_args") or [])
    gather = dict(spec.get("gather_args") or {})
    if spec.get("index_arg"):
        # the sliced state rows are stored separately; the full pool is a
        # multi-slot allocation that says nothing about this call
        skip |= set(spec.get("state_args") or [])

    def put(name, v):
        nonlocal written
        if not _is_tensor(v):
            return
        nbytes = int(v.numel() * v.element_size())
        if nbytes > _MAX_TENSOR:
            info = _tinfo(v)
            info["not_saved"] = "exceeds NVCAP_MAX_TENSOR_MB"
            meta["metadata_only"][name] = info
            return
        p = os.path.join(d, name + ".pt")
        t.save(_cpu(v), p)
        info = _tinfo(v)
        info["file"] = name + ".pt"
        meta["tensors"][name] = info
        written += os.path.getsize(p)

    for k, v in bound.items():
        if _is_tensor(v):
            if k in skip:
                meta["metadata_only"]["in_" + k] = dict(_tinfo(v), not_saved="skip_args")
                continue
            if k in gather:
                idx = bound.get(gather[k])
                rows, kept = _rows(v, idx)
                if rows is not None:
                    put("in_%s__gathered" % k, rows)
                    put("in_%s__rows" % k, kept)
                    meta["gathered"][k] = {"index_arg": gather[k], "full": _tinfo(v)}
                    continue
            put("in_" + k, v)
        elif isinstance(v, (int, float, bool, str)) or v is None:
            meta["scalars"][k] = v if not isinstance(v, str) else v[:120]
    for name, sb in (state_before or {}).items():
        put("state_before_" + name, sb)
        after = bound.get(name)
        rows = (state_rows or {}).get(name)
        if rows is not None:
            sa, _ = _rows(after, rows)
        else:
            sa = _cpu(after) if _is_tensor(after) else None
        put("state_after_" + name, sa)
        if rows is not None:
            put("state_rows_" + name, rows.detach().to("cpu", copy=True))
    if isinstance(out, (tuple, list)):
        for i, o in enumerate(out[:8]):
            put("out_%d" % i, o)
    else:
        put("out", out)
    meta["bytes_on_disk"] = written
    with open(os.path.join(d, "meta.json"), "w") as fh:
        json.dump(meta, fh, indent=2)
    print("[nvcap] payload %s / %s -> %.1f MB" % (group, os.path.basename(d), written / 1e6),
          flush=True)
    return written


# --------------------------------------------------------------------------- #
# wrapping
# --------------------------------------------------------------------------- #
def _bind(fn, args, kwargs) -> dict:
    try:
        sig = inspect.signature(fn)
        bound = sig.bind_partial(*args, **kwargs)
        return dict(bound.arguments)
    except Exception:
        d = {"arg%d" % i: v for i, v in enumerate(args)}
        d.update(kwargs)
        return d


def _wrap(fn, spec):
    op = spec.get("op") or spec["attr"]
    want_tensors = bool(spec.get("tensors", True)) and not _NO_TENSORS
    state_args = spec.get("state_args") or []
    index_arg = spec.get("index_arg")

    def wrapper(*args, **kwargs):
        _calls_seen[0] += 1
        if _pending and _calls_seen[0] % 256 == 1:
            _retry_pending()
        if _OPS and op not in _OPS:
            return fn(*args, **kwargs)
        try:
            bound = _bind(fn, args, kwargs)
            group = _group()
        except Exception:
            return fn(*args, **kwargs)

        do_payload = False
        step = 0
        chain = int(spec.get("chain", 1))
        wanted_sig = None
        if _TARGET_SIGS and want_tensors and _rank() == _CAPTURE_RANK:
            sig = _sig_of(bound)
            if sig in _TARGET_SIGS.get(op, ()):        # a signature this task ships
                wanted_sig = sig
        if wanted_sig is not None:
            with _lock:
                key = ("__target__", op, wanted_sig)
                n = _steps.get(key, 0)
                if n < chain:
                    _steps[key] = n + 1
                    do_payload, step = True, n
            if do_payload:
                try:
                    idx = bound.get(index_arg) if index_arg else None
                    state_before, state_rows = {}, {}
                    for name in state_args:
                        sb, rws = _rows(bound.get(name), idx)
                        if sb is not None:
                            state_before[name] = sb
                            state_rows[name] = rws
                except Exception:
                    state_before, state_rows = {}, {}
                out = fn(*args, **kwargs)
                try:
                    _record_manifest(op, group if group != "warmup" else "targeted", bound, out)
                    written = _save_payload(op, "targeted", bound, out, spec,
                                            state_before, state_rows, step)
                    with _lock:
                        _bytes["targeted"] = _bytes.get("targeted", 0) + written
                    dump_manifest()
                except Exception as exc:
                    _warn("targeted record failed for %s: %r" % (op, exc))
                return out
        if want_tensors and group != "warmup" and _rank() == _CAPTURE_RANK:
            try:
                sid = _shape_id(op, bound, spec)
                with _lock:
                    n = _shapes_per_op.get((group, op), 0)
                    used = _bytes.get(group, 0)
                    seen = (group, sid) in _saved
                    same_instance = True
                    if chain > 1 and spec.get("chain_key"):
                        # consecutive calls of one shape usually come from
                        # DIFFERENT layers, not from consecutive time steps of one
                        # layer. Pin the chain to one instance by the identity of a
                        # per-layer tensor (its weight), so the saved steps really
                        # do chain through the same state rows.
                        kt = bound.get(spec["chain_key"])
                        ident = int(kt.data_ptr()) if _is_tensor(kt) else None
                        prev = _chain_id.get((group, sid))
                        if prev is None:
                            _chain_id[(group, sid)] = ident
                        else:
                            same_instance = (ident == prev)
                    if same_instance and used < _BUDGET and (not seen or _steps.get((group, sid), 1) < chain):
                        if not seen and n >= _MAX_PER_OP:
                            pass  # this op already has enough distinct shapes
                        else:
                            if not seen:
                                _saved.add((group, sid))
                                _shapes_per_op[(group, op)] = n + 1
                            step = _steps.get((group, sid), 0)
                            _steps[(group, sid)] = step + 1
                            do_payload = True
            except Exception:
                do_payload = False

        state_before, state_rows = {}, {}
        if do_payload:
            try:
                idx = bound.get(index_arg) if index_arg else None
                for name in state_args:
                    sb, rows = _rows(bound.get(name), idx)
                    if sb is not None:
                        state_before[name] = sb
                        state_rows[name] = rows
            except Exception:
                state_before, state_rows = {}, {}

        out = fn(*args, **kwargs)

        try:
            is_new = _record_manifest(op, group, bound, out)
            if do_payload:
                written = _save_payload(op, group, bound, out, spec, state_before,
                                        state_rows, step)
                with _lock:
                    _bytes[group] = _bytes.get(group, 0) + written
            if is_new:
                # the server is usually torn down with a signal, so the manifest
                # cannot rely on atexit alone
                dump_manifest()
        except Exception as exc:
            _warn("record failed for %s: %r\n%s" % (op, exc, traceback.format_exc(limit=3)))
        return out

    wrapper.__name__ = getattr(fn, "__name__", op)
    wrapper.__doc__ = getattr(fn, "__doc__", None)
    wrapper._nvcap_wrapped = True
    return wrapper


def _retry_pending() -> None:
    if not _pending:
        return
    still = []
    for mod_name, spec in _pending:
        try:
            mod = sys.modules.get(spec["module"]) or importlib.import_module(spec["module"])
            obj = mod
            parts = spec["attr"].split(".")
            for p in parts[:-1]:
                obj = getattr(obj, p)
            fn = getattr(obj, parts[-1])
            if getattr(fn, "_nvcap_wrapped", False):
                continue
            setattr(obj, parts[-1], _wrap(fn, spec))
            print("[nvcap] wrapped (retry) %s.%s as op=%s"
                  % (spec["module"], spec["attr"], spec.get("op") or spec["attr"]), flush=True)
        except Exception:
            still.append((mod_name, spec))
    _pending[:] = still


def _patch_module(mod, specs) -> None:
    for spec in specs:
        attr = spec["attr"]
        try:
            obj = mod
            parts = attr.split(".")
            for p in parts[:-1]:
                obj = getattr(obj, p)
            fn = getattr(obj, parts[-1])
            if getattr(fn, "_nvcap_wrapped", False):
                continue
            setattr(obj, parts[-1], _wrap(fn, spec))
            print("[nvcap] wrapped %s.%s as op=%s" % (mod.__name__, attr, spec.get("op") or attr),
                  flush=True)
        except Exception as exc:
            # a module that is still executing (circular import) cannot be patched
            # yet; retry later from the call path rather than losing the target
            _pending.append((mod.__name__ if hasattr(mod, "__name__") else spec["module"], spec))
            _warn("cannot wrap %s.%s yet (%r) - queued for retry"
                  % (spec.get("module"), attr, exc))


class _Finder(importlib.abc.MetaPathFinder):
    """Patch each target module right after it is first imported."""

    def find_module(self, fullname, path=None):  # py2 shim, unused
        return None

    def find_spec(self, fullname, path=None, target=None):
        if fullname not in _by_module:
            return None
        real = None
        for finder in sys.meta_path:
            if finder is self:
                continue
            try:
                real = finder.find_spec(fullname, path, target)
            except Exception:
                real = None
            if real is not None:
                break
        if real is None or real.loader is None:
            return None
        real.loader = _Loader(real.loader, fullname)
        return real


class _Loader(importlib.abc.Loader):
    def __init__(self, inner, fullname):
        self.inner = inner
        self.fullname = fullname

    def create_module(self, spec):
        return self.inner.create_module(spec)

    def exec_module(self, module):
        self.inner.exec_module(module)
        try:
            _patch_module(module, _by_module.get(self.fullname, []))
        except Exception as exc:
            _warn("post-import patch failed for %s: %r" % (self.fullname, exc))

    def __getattr__(self, item):
        return getattr(self.inner, item)


_by_module: dict = {}


def install() -> None:
    global _installed, _targets
    if _installed or not _DIR or not _CONFIG:
        return
    _installed = True
    try:
        with open(_CONFIG) as fh:
            _targets = json.load(fh)
        if isinstance(_targets, dict):
            _targets = _targets.get("targets", [])
    except Exception as exc:
        _warn("cannot read NVCAP_CONFIG=%s: %r" % (_CONFIG, exc))
        return
    os.makedirs(_DIR, exist_ok=True)
    for spec in _targets:
        _by_module.setdefault(spec["module"], []).append(spec)
    sys.meta_path.insert(0, _Finder())
    # anything already imported gets patched right away
    for name, specs in _by_module.items():
        mod = sys.modules.get(name)
        if mod is not None:
            _patch_module(mod, specs)
    import atexit
    atexit.register(dump_manifest)
    print("[nvcap] armed: %d targets in %d modules -> %s"
          % (len(_targets), len(_by_module), _DIR), flush=True)


install()
