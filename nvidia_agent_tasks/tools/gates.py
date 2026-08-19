"""The correctness gates, in one place, so timing and testing use the same judge.

Modes (a task picks one in `config.json::correctness.mode`):

* `tolerance`    - max relative error against the baseline output (default 2e-2).
* `bitexact`     - byte-identical output. Used where a drift compounds (diffusion).
* `index_set`    - the *set* of selected indices must match. An approximate top-k
                   changes model output even when the logits stay within tolerance.
* `chained_state`- for state-carrying kernels: replay N consecutive real steps, feeding
                   each step's produced state into the next, and compare the FINAL state.
                   Per-step tolerance cannot see a state that drifts underneath correct
                   looking outputs; this can.
"""

from __future__ import annotations

import json
import os
import sys

import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tolerances  # noqa: E402  per-op rtol/atol copied from SGLang's own tests


def tol_for(op: str, ref=None) -> dict:
    """The rtol/atol SGLang's own test uses for this op (see tools/tolerances.py)."""
    dt = "bfloat16"
    if torch.is_tensor(ref):
        dt = str(ref.dtype).replace("torch.", "")
    elif isinstance(ref, (tuple, list)) and ref and torch.is_tensor(ref[0]):
        dt = str(ref[0].dtype).replace("torch.", "")
    return tolerances.get(op, dt)


def written_scale_rows(scale, tokens: int):
    """Which rows of a swizzled NVFP4 scale block the kernel actually wrote.

    `flashinfer.silu_and_mul_scaled_nvfp4_experts_quantize` returns its scale
    factors in the 6-D swizzled layout `[32, 4, ceil(T/128), 4, K/32, 1]`, where
    token row `r` lives at `(r % 32, (r // 32) % 4, r // 128)`. The row count is
    padded up to a multiple of 128 and the padding rows are never written, so their
    bytes are whatever the allocator last left there: two calls with byte-identical
    inputs return scale blocks that differ outside the written rows, and a
    bit-exact gate over the whole tensor fails the *reference against itself* on
    every row where `T % 128 != 0` while passing where T is already a multiple of
    128.

    Comparing the written rows only is also the stricter gate: the padding is not
    part of the kernel's output, and a candidate that skips a row it should have
    written now fails instead of hiding in allocator noise.
    """
    lanes, groups, tiles = scale.shape[0], scale.shape[1], scale.shape[2]
    row = (torch.arange(tiles, device=scale.device).view(1, 1, tiles) * (lanes * groups)
           + torch.arange(groups, device=scale.device).view(1, groups, 1) * lanes
           + torch.arange(lanes, device=scale.device).view(lanes, 1, 1))
    return row < tokens


def _compare_swizzled_quantize(ref, got, tokens: int):
    """out0 (packed nibbles, exactly T rows) in full; out1 over the written rows."""
    if not (isinstance(ref, (tuple, list)) and isinstance(got, (tuple, list))):
        return None, "expected (packed, scale) from a quantizer"
    if len(ref) != len(got):
        return False, "candidate returned %d outputs, reference %d" % (len(got), len(ref))
    if not torch.equal(got[0].view(torch.uint8), ref[0].view(torch.uint8)):
        return False, "packed output is NOT bit-exact"
    r, g = ref[1], got[1]
    if r.shape != g.shape:
        return False, "scale shape %s != %s" % (list(g.shape), list(r.shape))
    if r.dim() != 6:
        ok = torch.equal(g.view(torch.uint8), r.view(torch.uint8))
        return ok, "scale block bit-exact" if ok else "scale block NOT bit-exact"
    keep = written_scale_rows(r, tokens)
    rb = r.view(torch.uint8)[keep]
    gb = g.view(torch.uint8)[keep]
    if torch.equal(rb, gb):
        return True, ("bit-exact: packed output in full, scale block over the %d written "
                      "rows of %d (the 128-row padding is never written - see "
                      "gates.written_scale_rows)" % (int(keep.sum()), keep.numel()))
    n = int((rb != gb).sum())
    return False, ("scale block differs in %d of %d bytes inside the written rows"
                   % (n, rb.numel()))


def compare(mode: str, ref, got, op: str = "", rtol: float = None, atol: float = None,
            tokens: int = 0):
    """-> (ok: bool|None, detail: str). None means 'this gate needs the chain runner'.

    Numeric comparisons use `torch.testing.assert_close` semantics with the rtol/atol
    SGLang's own test for that kernel uses; nothing here is a hand-picked threshold.
    """
    t = tol_for(op, ref)
    if rtol is None:
        rtol = t["rtol"]
    if atol is None:
        atol = t["atol"]
    src = t.get("source", "")
    if op == "qwen38_silu_fp4_quantize" and tokens:
        return _compare_swizzled_quantize(ref, got, tokens)
    if t.get("exact") and mode not in ("index_set",):
        mode = "bitexact"
    if mode == "index_set":
        def flat(x):
            return set(x.flatten().tolist()) if torch.is_tensor(x) else set(x)
        a, b = flat(ref), flat(got)
        same = a == b
        return same, ("selected index sets match (%d entries)" % len(a) if same else
                      "index sets differ: %d only in baseline, %d only in candidate"
                      % (len(a - b), len(b - a)))
    if mode in ("bitexact", "exact"):
        if isinstance(ref, (tuple, list)):
            ok = all(torch.equal(r, g) for r, g in zip(ref, got))
        else:
            ok = torch.is_tensor(ref) and torch.is_tensor(got) and \
                ref.shape == got.shape and torch.equal(ref, got)
        return ok, "bit-exact" if ok else "NOT bit-exact"
    if mode == "chained_state":
        # The authoritative gate for a state-carrying kernel is the chained final state
        # (replay_chain, run by tests/test_solution.py). Returning None here left the
        # per-row line reading `correct=None` next to a speedup, which is a hole: a
        # candidate could return anything and still be timed. Fall through to the
        # per-call comparison as a floor, and say which gate this is.
        mode = "tolerance"
        chained_floor = True
    else:
        chained_floor = False
    # numeric, with SGLang's tolerances
    def one(r, g):
        if r.shape != g.shape:
            return None, "shape mismatch %s vs %s" % (list(r.shape), list(g.shape))
        try:
            torch.testing.assert_close(g.float(), r.float(), rtol=rtol, atol=atol)
            ok, why = True, ""
        except AssertionError as exc:
            ok, why = False, str(exc).strip().splitlines()[0][:120]
        diff = (r.float() - g.float()).abs()
        worst = float((diff / (r.float().abs() + atol)).max())
        return ok, ("assert_close rtol=%g atol=%g [%s]%s  (worst elementwise %.3g)"
                    % (rtol, atol, src, "" if ok else " FAILED: " + why, worst))
    def label(result):
        ok, detail = result
        if chained_floor and detail:
            detail += ("  [per-call floor; the authoritative gate for this kernel is the "
                       "chained final state - tests/test_solution.py]")
        return ok, detail

    if isinstance(ref, (tuple, list)):
        parts = [one(r, g) for r, g in zip(ref, got) if torch.is_tensor(r) and torch.is_tensor(g)]
        ok = all(p[0] for p in parts) if parts else None
        return label((ok, "; ".join(p[1] for p in parts)))
    if not (torch.is_tensor(ref) and torch.is_tensor(got)):
        return None, ("output is not a tensor and the op declares no destination argument; "
                      "add OUTPUT_ARGS[op] in baseline/entry.py or a task-specific comparison")
    return label(one(ref, got))


def load_step(step_dir: str, static_dir: str | None) -> dict:
    """Everything one chain step needs: its tensors, the chain's static tensors, scalars."""
    meta = json.load(open(os.path.join(step_dir, "meta.json")))
    out = {"__meta__": meta, "scalars": dict(meta.get("scalars", {}))}
    for name, info in meta.get("tensors", {}).items():
        for base in (step_dir, static_dir or step_dir):
            p = os.path.join(base, info.get("file", ""))
            if os.path.exists(p):
                out[name] = torch.load(p, map_location="cuda")
                break
    return out


def replay_chain(chain_dir: str, steps: list, static_dir: str | None, call, state_arg: str = None):
    """Replay a captured chain through `call(**kwargs)` and judge the FINAL state.

    `call` receives the recorded kwargs with the state argument replaced by the running
    state, and is expected to update that state in place (which is what these kernels do).
    Returns a dict with the per-step output error and the final-state error.
    """
    first = load_step(steps[0], static_dir)
    if state_arg is None:
        cands = [k[len("state_before_"):] for k in first if k.startswith("state_before_")]
        if not cands:
            raise RuntimeError("no state_before_* in %s - not a state-carrying chain" % steps[0])
        state_arg = cands[0]
    running = first["state_before_" + state_arg].clone()
    # A pool-backed state ships as the touched rows plus the indices that selected them.
    # Replaying with the original indices would address a pool we do not have, so the
    # indices are remapped onto the compact rows (0..n-1).
    rows = first.get("state_rows_" + state_arg)
    remap = None
    if torch.is_tensor(rows):
        remap = torch.arange(rows.numel(), device=running.device, dtype=rows.dtype)
    out_err, ref_final = 0.0, None
    for sd in steps:
        rec = load_step(sd, static_dir)
        kwargs = {k[len("in_"):]: v for k, v in rec.items() if k.startswith("in_")}
        kwargs.update(rec["scalars"])
        kwargs[state_arg] = running
        if remap is not None:
            for k, v in list(kwargs.items()):
                if torch.is_tensor(v) and k.endswith("indices") and v.numel() == remap.numel():
                    kwargs[k] = remap
            for k in list(kwargs):
                if k.endswith("__rows"):          # sliced pools ship as <name>__rows
                    kwargs.setdefault(k[: -len("__rows")], kwargs[k])
        produced = call(**kwargs)
        ref_out = rec.get("out")
        if torch.is_tensor(ref_out) and torch.is_tensor(produced):
            denom = ref_out.float().abs().max().clamp_min(1e-30)
            out_err = max(out_err, float((produced.float() - ref_out.float()).abs().max() / denom))
        ref_final = rec.get("state_after_" + state_arg, ref_final)
    if ref_final is None:
        raise RuntimeError("chain has no state_after_%s to compare against" % state_arg)
    abs_err = float((running.float() - ref_final.float()).abs().max())
    denom = float(ref_final.float().abs().max())
    return {"steps": len(steps), "state_arg": state_arg,
            "state_dtype": str(ref_final.dtype).replace("torch.", ""),
            "max_per_step_output_rel_err": out_err,
            "final_state_abs_err": abs_err,
            "final_state_rel_err": abs_err / max(denom, 1e-30)}


def chained_verdict(res: dict, op: str = "", rtol: float = None, atol: float = None) -> tuple:
    """The chained gate uses the same per-op tolerance as the single-call gate."""
    # the tolerance branch follows the state's dtype, the way SGLang's tests do
    t = tolerances.get(op or "", res.get("state_dtype", "bfloat16"))
    rtol = t["rtol"] if rtol is None else rtol
    atol = t["atol"] if atol is None else atol
    ok = res["final_state_rel_err"] <= max(rtol, 1e-12) or res["final_state_abs_err"] <= atol
    return ok, ("final state: rel %.3g / abs %.3g vs rtol=%g atol=%g [%s] over %d chained "
                "steps (per-step output max rel %.3g)"
                % (res["final_state_rel_err"], res["final_state_abs_err"], rtol, atol,
                   t.get("source", ""), res["steps"], res["max_per_step_output_rel_err"]))


def _swizzle_written(t, op: str, tokens: int):
    """Restrict a padded NVFP4 scale block to the rows the kernel writes.

    Used by `reference_is_trustworthy` for the same reason `compare` uses it: the
    128-row padding is never written, so its bytes are allocator leftovers. They
    can be NaN, and they differ between two allocations - which made the trust
    check report "baseline output contains NaN/Inf" and "two identical baseline
    calls disagree" on a reference that is in fact perfectly reproducible where it
    writes.
    """
    if op != "qwen38_silu_fp4_quantize" or not tokens or not torch.is_tensor(t):
        return t
    if t.dim() != 6:
        return t
    return t.view(torch.uint8)[written_scale_rows(t, tokens)]


def reference_is_trustworthy(call, kwargs, op: str = "", tokens: int = 0) -> tuple:
    """Run the baseline twice on identical inputs before judging anything.

    A row whose inputs had to be allocated (because the task does not ship a payload for
    it) can drive a segment-based kernel with index arrays full of zeros: parts of the
    output are then never written, so the "reference" is uninitialized memory that differs
    between runs and can contain NaN. Judging a candidate against that is worse than not
    judging it. -> (ok, detail)
    """
    import copy

    def snap(x):
        return {k: (v.clone() if torch.is_tensor(v) else copy.copy(v)) for k, v in x.items()}

    # three calls, not two: with an index argument allocated to zeros several sequences can
    # map to the same state slot and race, which is intermittent - two calls sometimes agree
    kws = [snap(kwargs) for _ in range(3)]
    rets = [call(**k) for k in kws]
    first_kwargs, second_kwargs = kws[0], kws[1]
    r1, r2 = rets[0], rets[1]

    def tensors(ret, kw):
        out = [t for t in (ret if isinstance(ret, (tuple, list)) else [ret]) if torch.is_tensor(t)]
        out += [v for k, v in kw.items() if torch.is_tensor(v) and k in ("out", "output", "o")]
        return out

    a, b = tensors(r1, first_kwargs), tensors(r2, second_kwargs)
    c = tensors(rets[2], kws[2])
    a = [_swizzle_written(t, op, tokens) for t in a]
    b = [_swizzle_written(t, op, tokens) for t in b]
    c = [_swizzle_written(t, op, tokens) for t in c]
    if not a:
        return True, "no tensor output to check"
    for t in a:
        if torch.isnan(t.float()).any() or torch.isinf(t.float()).any():
            return False, ("baseline output contains NaN/Inf on these inputs - the row needs "
                           "real tensors (index/segment arguments allocated to zeros leave "
                           "part of the output unwritten)")
    t = tol_for(op, a[0])
    for x, y in list(zip(a, b)) + list(zip(a, c)):
        if x.shape != y.shape:
            return False, "baseline is not shape-stable across identical calls"
        try:
            torch.testing.assert_close(y.float(), x.float(), rtol=t["rtol"], atol=t["atol"])
        except AssertionError:
            return False, ("two identical baseline calls disagree beyond rtol=%g atol=%g - "
                           "the reference is not reproducible from these inputs"
                           % (t["rtol"], t["atol"]))
    return True, "baseline reproduces itself"
