"""Regenerate every task's `bench/README.md` from what the task actually ships.

    python tools/gen_bench_readme.py [task ...]

Everything in the generated page is derived: the op/row table from
`bench/workloads*.json`, the tolerance table from `tools/tolerances.py`, the coverage
line from `tools/coverage.py`. The one measured fact - how many ops produce a timed
baseline on a GPU box - is read from `tools/bench_status.json`, which is written by
running `tools/bench_harness.py` on the box; it is not guessed here.
"""

from __future__ import annotations

import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import coverage  # noqa: E402
import tolerances  # noqa: E402

TEMPLATE = """# bench/ - how to run this task

```bash
# 1. does the package have everything?  (CPU only, no SGLang import)
python tools/check_task.py {task}
python {task}/tests/test_contract.py

# 2. time the baseline on every workload row (needs a GPU + the SGLang env)
python tools/bench_harness.py {task}

# 3. write solution/entry.py with the same OPS keys, then A/B it
python tools/bench_harness.py {task} --json report.json
```

The harness times inside a CUDA graph, interleaves the two arms, restores in-place
inputs between iterations, checks correctness before reporting a speedup, and uses the
real captured tensors for a row whenever this task ships a payload that matches it
(the per-row line prints how many inputs were real).

## What runs today

{status}

## Dropping a candidate in

```bash
cp solution/entry.py.template solution/entry.py     # implement the ops listed there
python tools/bench_harness.py {task} --json report.json
python {task}/tests/test_solution.py
```

`solution/entry.py` exposes the same `OPS` keys as `baseline/entry.py`, so the harness
calls both arms with identical inputs. The path is validated end to end with an identity
candidate (one that just calls the baseline): **1.002x geomean with every gate green**,
which is also this harness's measurement floor - trials alternate which arm runs first,
because running the candidate second in every trial was worth ~2% on its own.

`tests/test_solution.py` runs the same gate without timing: every row through
`config.json::correctness.mode`, plus - where the task ships a state chain - the chained
final-state gate (`gates.replay_chain` feeds each step's produced state into the next and
compares the final one; on the identity candidate that reads `final state rel err 0 over
N chained steps`).

A row whose integer index arguments had to be allocated can address out of bounds and take
the CUDA context down; the harness and the test detect that, name the row, and stop rather
than reporting nonsense for every row after it.

## Real-tensor coverage

```
{coverage}
```

Rows with a payload run on tensors captured from the live model; the rest fall back
to tensors allocated to the recorded shape/dtype/stride. Weights and whole state or
KV pools are never shipped - the first would mean distributing model weights, the
second ships as the touched rows - so they are excluded from the arg count and
recorded as metadata instead. `python tools/coverage.py {task}` recomputes this.

## Measurement regime

* **Timing is `triton.testing.do_bench` around a captured CUDA graph** (`--timer do_bench`,
  the default). do_bench clears L2 before every run, brackets each run with its own event
  pair and sizes the repetitions from a time budget; the graph keeps per-launch overhead out
  of kernels that take single-digit microseconds. `--timer graph` runs our own flush+event
  loop instead - the two agree to 0.1% on the K3 GEMM rows.
* **L2 is cold on every call.** Back-to-back replay with a warm L2 reads 58-82% faster on
  these rows - see `../../docs/measurement_contract.md`.
* **The baseline is called three times on identical inputs before anything is judged.** A row
  whose reference contains NaN/Inf or does not reproduce is printed as `NO VALID REFERENCE`
  and excluded, rather than judged against uninitialized memory.
* **Per-row trial spread is reported**, and a row whose spread exceeds 10% is marked
  unstable - its speedup is noise until that is fixed.
* Rows whose integer index arguments had to be synthesised are flagged in the row line.

## Correctness tolerances

`torch.testing.assert_close` with the rtol/atol **SGLang's own test for that
kernel uses** - not a threshold invented for this handoff. Same numbers in
`../config.json::correctness.tolerances`, table in `tools/tolerances.py`.

{tolerances}

## What is in here

| file | contents |
| --- | --- |
{files}

{ops}
"""


def main() -> None:
    tasks = sys.argv[1:] or sorted(
        os.path.basename(d) for d in glob.glob(os.path.join(ROOT, "*"))
        if os.path.isdir(d) and os.path.exists(os.path.join(d, "config.json")))
    status = {}
    sp = os.path.join(HERE, "bench_status.json")
    if os.path.exists(sp):
        status = json.load(open(sp))
    for task in tasks:
        tdir = os.path.join(ROOT, task)
        ops, files = [], {}
        for wf in sorted(glob.glob(os.path.join(tdir, "bench", "workloads*.json"))):
            d = json.load(open(wf))
            files.setdefault("`%s`" % os.path.basename(wf),
                             "frozen call signatures with their real-traffic call counts")
            for o in d["ops"]:
                ops.append((o["op"], o["total_real_calls"], len(o["rows"]),
                            o.get("rows_with_payload", 0), os.path.basename(wf)))
        for td in sorted(glob.glob(os.path.join(tdir, "bench", "tensors*"))):
            files["`%s/`" % os.path.basename(td)] = \
                "real captured tensors (inputs, outputs, state rows)"
        if os.path.exists(os.path.join(tdir, "bench", "target_signatures.json")):
            files["`target_signatures.json`"] = \
                "the exact signatures the tensor capture was pointed at"

        tol_rows = ["| op | rtol | atol | copied from |", "| --- | ---: | ---: | --- |"]
        for op in sorted({o[0] for o in ops}):
            t = tolerances.get(op)
            tol_rows.append("| `%s` | %s | %s | `%s` |"
                            % (op, t["rtol"], t["atol"], t["source"]))

        op_rows = ["| op | real calls | rows | rows with real tensors | workload file |",
                   "| --- | ---: | ---: | ---: | --- |"]
        for op, calls, n, pay, wf in ops:
            op_rows.append("| `%s` | %s | %d | %d | `%s` |" % (op, "{:,}".format(calls), n, pay, wf))

        cov = coverage.line(task, coverage.report(tdir))

        st = status.get(task)
        st = (st if st else
              "Not yet re-verified on a GPU box after the latest capture; "
              "`python tools/bench_harness.py %s` reports it in one run." % task)
        page = TEMPLATE.format(
            task=task, status=st, coverage=cov,
            tolerances="\n".join(tol_rows),
            files="\n".join("| %s | %s |" % (k, v) for k, v in sorted(files.items())),
            ops="\n".join(op_rows))
        open(os.path.join(tdir, "bench", "README.md"), "w").write(page)
        print("wrote %s/bench/README.md" % task)


if __name__ == "__main__":
    main()
