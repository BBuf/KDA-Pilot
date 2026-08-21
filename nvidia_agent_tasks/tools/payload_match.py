"""The rule that decides whether a shipped payload belongs to a workload row.

Kept free of torch so `tools/coverage.py` and `tools/check_task.py` can use it on a
laptop, while `tools/workload.py` uses the same function at run time on the box.
"""

from __future__ import annotations

import os
import re


def payload_conflicts(payload_dir: str, row: dict) -> bool:
    """Does this payload folder come from a call with different shapes than this row?

    A payload folder is named `[<group>__]<op>__<arg><dims>_<arg><dims>`, which records the
    call it was taken from. Scoring by matched tensors alone is not enough: when the large
    tensors were too big to ship, two rows of very different sequence length can match a
    payload equally well on their small arguments - and then the row silently runs with
    another call's `cu_seqlens`, which indexes out of bounds. Rejecting a payload whose
    recorded shapes contradict the row keeps a row on its own capture or on nothing.
    """
    name = os.path.basename(payload_dir.rstrip("/"))
    parts = name.split("__")
    if len(parts) < 2:
        return False
    # both layouts are in use: `<group>__<op>__<shapes>` and `<op>__<shapes>`
    for tok in parts[-1].split("_"):
        m = re.match(r"([A-Za-z][A-Za-z0-9]*?)((?:\d+x)*\d+)$", tok)
        if not m:
            continue
        arg, dims = m.group(1), tuple(int(x) for x in m.group(2).split("x"))
        info = row["args"].get(arg)
        if isinstance(info, dict) and "shape" in info and tuple(info["shape"]) != dims:
            return True
    return False
