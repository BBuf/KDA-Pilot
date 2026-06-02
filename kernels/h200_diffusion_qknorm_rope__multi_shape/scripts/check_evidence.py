#!/usr/bin/env python3
"""Verify every evidence path declared in solutions.jsonl resolves from the workspace (AC-10).

Exits non-zero if any `evidence_files` / `profile_paths` entry does not exist locally.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOL = os.path.join(ROOT, "solutions.jsonl")
missing = []
checked = 0
with open(SOL) as f:
    for ln, line in enumerate(f, 1):
        line = line.strip()
        if not line:
            continue
        e = json.loads(line)
        files = list(e.get("evidence_files", [])) + list(e.get("profile_paths", []))
        if not files:
            print(f"WARNING: candidate {e.get('id')!r} (line {ln}) has no evidence_files")
        for rel in files:
            checked += 1
            if not os.path.exists(os.path.join(ROOT, rel)):
                missing.append((e.get("id"), rel))

print(f"checked {checked} evidence paths across {SOL}")
if missing:
    print("MISSING (unresolved evidence pointers):")
    for cid, rel in missing:
        print(f"  [{cid}] {rel}")
    sys.exit(1)
print("ALL_EVIDENCE_RESOLVES OK")
