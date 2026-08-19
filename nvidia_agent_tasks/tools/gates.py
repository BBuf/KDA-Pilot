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

import torch


def compare(mode: str, ref, got, tol: float = 2e-2):
    """-> (ok: bool|None, detail: str). None means 'this gate needs the chain runner'."""
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
    # tolerance
    def one(r, g):
        r, g = r.float(), g.float()
        if r.shape != g.shape:
            return None, "shape mismatch %s vs %s" % (list(r.shape), list(g.shape))
        rel = float((r - g).abs().max() / r.abs().max().clamp_min(1e-30))
        return rel < tol, "max rel err %.3g (tol %g)" % (rel, tol)
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
    denom = ref_final.float().abs().max().clamp_min(1e-30)
    final_err = float((running.float() - ref_final.float()).abs().max() / denom)
    return {"steps": len(steps), "state_arg": state_arg,
            "max_per_step_output_rel_err": out_err, "final_state_rel_err": final_err}


def chained_verdict(res: dict, tol: float = 2e-2) -> tuple:
    ok = res["final_state_rel_err"] < tol
    return ok, ("final state rel err %.3g over %d chained steps (per-step output max %.3g)"
                % (res["final_state_rel_err"], res["steps"], res["max_per_step_output_rel_err"]))
