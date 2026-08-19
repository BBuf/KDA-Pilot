"""Correctness gate for a candidate kernel in `minimax_h3__sm103_block_sparse_attention`.

    python minimax_h3__sm103_block_sparse_attention/tests/test_solution.py        # or: pytest minimax_h3__sm103_block_sparse_attention/tests

Skips cleanly when `solution/entry.py` does not exist yet, so it is safe to run on a
fresh checkout. When a candidate is present it runs **every workload row** through the
gate this task declares in `config.json` (`tolerance`) and fails on the first row that
does not hold. No timing here - that is `tools/bench_harness.py`.
"""

import json
import os
import sys

TASK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(TASK)
sys.path.insert(0, os.path.join(ROOT, "tools"))

import gates          # noqa: E402
import workload       # noqa: E402

MODE = json.load(open(os.path.join(TASK, "config.json")))["correctness"].get("mode", "tolerance")


def _entry(kind):
    import importlib.util
    p = os.path.join(TASK, kind, "entry.py")
    if not os.path.exists(p):
        return None
    spec = importlib.util.spec_from_file_location("%s_entry_%s" % (os.path.basename(TASK), kind), p)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    return m


def _row_tokens(row):
    """The token count a shape-derived gate needs off the row (see gates.compare)."""
    for name in ("a", "input", "x"):
        spec = row["args"].get(name)
        if isinstance(spec, dict) and spec.get("shape"):
            shape = spec["shape"]
            return int(shape[-2]) if len(shape) >= 2 else int(shape[0])
    return 0


def _call(mod, op, kwargs):
    fix = getattr(mod, "RECONSTRUCT", {}) or {}
    if op in fix:
        kwargs = fix[op](dict(kwargs))
    return mod.OPS[op](**kwargs)


def test_candidate_matches_baseline():
    import torch

    sol = _entry("solution")
    if sol is None:
        print("no solution/entry.py yet - nothing to check")
        return
    base = _entry("baseline")
    failures, checked, skipped = [], 0, 0
    for op, row in workload.iter_rows(TASK):
        if op not in getattr(sol, "OPS", {}):
            skipped += 1
            continue
        built = workload.build_inputs(TASK, row)
        kw = built["kwargs"]
        trust, why = gates.reference_is_trustworthy(lambda **k: _call(base, op, k), kw, op,
                                                      tokens=_row_tokens(row))
        if not trust:
            skipped += 1
            print("skip %s: %s" % (row["row_id"], why))
            continue
        try:
            ref = _call(base, op, {k: (v.clone() if torch.is_tensor(v) else v) for k, v in kw.items()})
            got = _call(sol, op, {k: (v.clone() if torch.is_tensor(v) else v) for k, v in kw.items()})
        except Exception as exc:
            failures.append("%s: call failed: %r" % (row["row_id"], exc))
            if not workload.cuda_alive():
                failures.append("CUDA context lost at %s - run the remaining ops one at a "
                                "time; an integer index argument allocated to zeros can "
                                "address out of bounds" % row["row_id"])
                break
            continue
        ok, detail = gates.compare("tolerance" if MODE == "chained_state" else MODE,
                                   ref, got, op=op, tokens=_row_tokens(row))
        checked += 1
        if ok is False:
            failures.append("%s (%s): %s" % (row["row_id"], row["group"], detail))
    print("rows checked: %d, skipped (op not implemented): %d" % (checked, skipped))
    assert not failures, "\n".join(failures[:10])


def test_chained_state_gate():
    """The gate that per-row comparison cannot replace, where this task has a chain."""
    sol = _entry("solution")
    if sol is None:
        print("no solution/entry.py yet - nothing to check")
        return
    found = 0
    for chain_dir, steps, static in workload.chains(TASK):
        ops = [o for o in getattr(sol, "OPS", {})]
        if not ops:
            return
        op = ops[0]
        for cand in ops:
            if cand.split("__")[-1][:6] in os.path.basename(chain_dir):
                op = cand
        res = gates.replay_chain(chain_dir, steps, static,
                                 lambda **kw: _call(sol, op, kw))
        ok, detail = gates.chained_verdict(res, op=op)
        found += 1
        print("%s -> %s" % (os.path.basename(chain_dir), detail))
        assert ok, "%s: %s" % (chain_dir, detail)
    if not found:
        print("this task ships no state chain")


if __name__ == "__main__":
    for fn in (test_candidate_matches_baseline, test_chained_state_gate):
        fn()
        print("ok:", fn.__name__)
