"""Validate a task package without a GPU: is everything an agent needs actually here?

    python tools/check_task.py <task_dir> ...     # or no args = every task

Checks, per task:

1. `prompt.md`, `config.json`, `baseline/SOURCES.txt` present, and every file listed in
   SOURCES.txt actually copied into `baseline/`.
2. `bench/workloads*.json` parse, every op has rows, every row records its
   `real_calls`, `group` and `kept_because`.
3. Every tensor payload folder has a `meta.json` whose referenced `.pt` files exist.
4. Any payload folder with `step*` subfolders is a real chain: step[n+1] state-before
   equals step[n] state-after byte for byte (this is the correctness oracle, so a
   broken chain is a packaging bug, not a detail).
5. Relative links in the task's markdown resolve.
6. No absolute paths from the capture box leaked into the shipped JSON/markdown.

Exit code is non-zero if any check fails, so this doubles as CI.
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys

FAIL: list = []
WARN: list = []


def fail(task: str, msg: str) -> None:
    FAIL.append("%s: %s" % (task, msg))


def warn(task: str, msg: str) -> None:
    WARN.append("%s: %s" % (task, msg))


def check_baseline(task: str) -> None:
    src = os.path.join(task, "baseline", "SOURCES.txt")
    if not os.path.exists(src):
        return fail(task, "baseline/SOURCES.txt missing")
    listed = [l.strip() for l in open(src) if l.strip() and not l.startswith("#")]
    if not listed:
        return fail(task, "baseline/SOURCES.txt lists no files")
    for rel in listed:
        want = os.path.join(task, "baseline", os.path.relpath(rel, "python/sglang"))
        if not os.path.exists(want):
            fail(task, "SOURCES.txt lists %s but %s is not in the package"
                 % (rel, os.path.relpath(want, task)))
    if not os.path.exists(os.path.join(task, "baseline", "entry.py")):
        warn(task, "no baseline/entry.py - tools/bench_harness.py cannot run this task yet")


def check_workloads(task: str) -> None:
    files = sorted(glob.glob(os.path.join(task, "bench", "workloads*.json")))
    if not files:
        return fail(task, "no bench/workloads*.json")
    for f in files:
        try:
            d = json.load(open(f))
        except Exception as exc:
            fail(task, "%s does not parse: %r" % (os.path.basename(f), exc))
            continue
        if not d.get("ops"):
            fail(task, "%s has no ops" % os.path.basename(f))
        for o in d.get("ops", []):
            if not o.get("rows"):
                fail(task, "%s op %s has no rows" % (os.path.basename(f), o.get("op")))
            for r in o.get("rows", []):
                for key in ("row_id", "group", "real_calls", "kept_because", "args"):
                    if key not in r:
                        fail(task, "%s row %s misses %s"
                             % (os.path.basename(f), r.get("row_id", "?"), key))
                if r.get("group") == "warmup":
                    fail(task, "%s row %s is a warmup-only signature and must not be a "
                               "workload row" % (os.path.basename(f), r.get("row_id")))


def check_payloads(task: str) -> None:
    root = os.path.join(task, "bench", "tensors")
    if not os.path.isdir(root):
        return
    metas = sorted(glob.glob(os.path.join(root, "**", "meta.json"), recursive=True))
    if not metas:
        return fail(task, "bench/tensors exists but contains no meta.json")
    for m in metas:
        meta = json.load(open(m))
        base = os.path.dirname(m)
        for name, info in meta.get("tensors", {}).items():
            if not os.path.exists(os.path.join(base, info.get("file", ""))):
                fail(task, "payload %s references missing %s"
                     % (os.path.relpath(base, task), info.get("file")))
    for d in sorted(glob.glob(os.path.join(root, "*"))):
        steps = sorted(glob.glob(os.path.join(d, "step*")))
        if len(steps) < 2:
            continue
        try:
            import torch
        except Exception:
            warn(task, "torch unavailable; chain in %s not verified" % os.path.basename(d))
            continue
        names = {os.path.basename(f)[len("state_after_"):-3]
                 for f in glob.glob(os.path.join(steps[0], "state_after_*.pt"))}
        if not names:
            fail(task, "chain %s has step folders but no state_after_*.pt - the chained "
                       "gate cannot be run" % os.path.basename(d))
            continue
        for n in sorted(names):
            for i in range(len(steps) - 1):
                a = torch.load(os.path.join(steps[i], "state_after_%s.pt" % n), map_location="cpu")
                bp = os.path.join(steps[i + 1], "state_before_%s.pt" % n)
                if not os.path.exists(bp):
                    fail(task, "chain %s step%03d has no state_before_%s"
                         % (os.path.basename(d), i + 1, n)); break
                b = torch.load(bp, map_location="cpu")
                if a.shape != b.shape or not torch.equal(a, b):
                    fail(task, "chain %s breaks between step%03d and step%03d (%s)"
                         % (os.path.basename(d), i, i + 1, n)); break


def check_text(task: str) -> None:
    for f in glob.glob(os.path.join(task, "**", "*.md"), recursive=True):
        s = open(f).read()
        for m in re.finditer(r"\]\(([^)#][^)]*)\)", s):
            t = m.group(1)
            if t.startswith("http"):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), t))):
                fail(task, "%s has a broken link -> %s" % (os.path.relpath(f, task), t))
    for f in glob.glob(os.path.join(task, "**", "*.json"), recursive=True) + \
             glob.glob(os.path.join(task, "**", "*.md"), recursive=True):
        s = open(f).read()
        for leak in ("/scratch/", "/cluster-storage/", "/home/bbuf", "/Users/"):
            if leak in s and "capture" not in os.path.basename(f):
                warn(task, "%s mentions the capture box path %s"
                     % (os.path.relpath(f, task), leak))
                break


def main() -> None:
    tasks = sys.argv[1:] or sorted(
        d for d in os.listdir(".")
        if os.path.isdir(d) and d not in ("docs", "tools", ".git")
        and os.path.exists(os.path.join(d, "prompt.md")))
    for t in tasks:
        t = t.rstrip("/")
        for f in ("prompt.md", "config.json"):
            if not os.path.exists(os.path.join(t, f)):
                fail(t, "%s missing" % f)
        check_baseline(t)
        check_workloads(t)
        check_payloads(t)
        check_text(t)
        print("checked %s" % t)
    print()
    for w in WARN:
        print("WARN  " + w)
    for f in FAIL:
        print("FAIL  " + f)
    print("\n%d tasks, %d failures, %d warnings" % (len(tasks), len(FAIL), len(WARN)))
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
