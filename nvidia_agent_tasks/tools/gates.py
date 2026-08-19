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


def compare(mode: str, ref, got, op: str = "", rtol: float = None, atol: float = None):
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
        return None, ("chained-state gate: use replay_chain(); a per-call comparison is not "
                      "the gate for this kernel")
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
    if isinstance(ref, (tuple, list)):
        parts = [one(r, g) for r, g in zip(ref, got) if torch.is_tensor(r) and torch.is_tensor(g)]
        ok = all(p[0] for p in parts) if parts else None
        return ok, "; ".join(p[1] for p in parts)
    if not (torch.is_tensor(ref) and torch.is_tensor(got)):
        return None, "output is not a tensor; write a task-specific comparison"
    return one(ref, got)


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
