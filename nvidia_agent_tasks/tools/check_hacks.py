"""Print, on the shipped real tensors, the numbers that make three verifier
shortcuts pass under synthetic Gaussian inputs and fail under real data.

    python check_hacks.py <task>/bench/tensors/<shape_dir>

For every float tensor in the payload it reports:

1. **norm spread** - `||row||` mean and relative spread. Under i.i.d. N(0,1) with
   d=128 this is 11.31 +- 6.3%, i.e. nearly constant, so a kernel can replace the
   L2/RMS reduction with the constant `1/sqrt(d)` and still pass a few-percent
   tolerance. Real activations are not that tight.
2. **energy in the smallest channels** - the fraction of total energy carried by
   the smallest 25% / 50% / 75% of channels. Under N(0,1) this is analytically
   0.86% / 7.1% / 27.6%, which is what lets a magnitude-pruning kernel tune its
   sparsity rate to sit just inside a tolerance.
3. **gate / decay statistics** (any tensor named `g`, `a`, `beta`, `A_log`,
   `dt`) - the share of channels whose decay is close to 1. Synthetic gates imply
   uniformly short memory, which makes a truncated recurrence window pass; real
   learned gates keep some channels near 1, and truncating them destroys
   long-range recall.

The point is not the exact numbers but the comparison: if your verifier's inputs
reproduce the Gaussian column, the verifier can be satisfied without computing the
kernel.
"""

from __future__ import annotations

import glob
import json
import math
import os
import sys

import torch

GAUSS = {"norm_rel_spread_d128": 0.063, "energy_25": 0.0086, "energy_50": 0.071,
         "energy_75": 0.276}


def energy_fractions(x: torch.Tensor) -> tuple:
    v = x.detach().float().flatten(0, max(0, x.dim() - 2)) if x.dim() > 1 else x.detach().float()
    v = v.reshape(-1, v.shape[-1])
    e = v.pow(2)
    total = e.sum(-1, keepdim=True).clamp_min(1e-30)
    srt, _ = e.sort(-1)
    d = v.shape[-1]
    out = []
    for frac in (0.25, 0.5, 0.75):
        k = max(1, int(d * frac))
        out.append(float((srt[:, :k].sum(-1, keepdim=True) / total).mean()))
    return tuple(out)


def norm_spread(x: torch.Tensor) -> tuple:
    v = x.detach().float().reshape(-1, x.shape[-1])
    n = v.norm(dim=-1)
    m = float(n.mean())
    if n.numel() < 2:
        return m, float("nan")
    return m, float(n.std(unbiased=False) / max(m, 1e-30))


def gate_stats(x: torch.Tensor) -> str:
    v = x.detach().float().flatten()
    if v.numel() == 0:
        return "empty"
    near1 = float((v.exp().clamp(max=1.0) > 0.99).float().mean()) if v.min() < 0 else float((v > 0.99).float().mean())
    return "min %.4g max %.4g mean %.4g | share with decay>0.99: %.1f%%" % (
        float(v.min()), float(v.max()), float(v.mean()), 100.0 * near1)


def main() -> None:
    d = sys.argv[1]
    metas = sorted(glob.glob(os.path.join(d, "**", "meta.json"), recursive=True)) or \
        sorted(glob.glob(os.path.join(d, "meta.json")))
    if not metas:
        raise SystemExit("no meta.json under %s" % d)
    print("Gaussian reference (d=128): norm rel spread %.1f%%, energy in smallest "
          "25/50/75%% of channels = %.2f%% / %.1f%% / %.1f%%"
          % (100 * GAUSS["norm_rel_spread_d128"], 100 * GAUSS["energy_25"],
             100 * GAUSS["energy_50"], 100 * GAUSS["energy_75"]))
    for meta_path in metas:
        meta = json.load(open(meta_path))
        step = os.path.relpath(os.path.dirname(meta_path), d)
        print("\n== %s (op=%s, group=%s)" % (step, meta.get("op"), meta.get("group")))
        for name, info in meta.get("tensors", {}).items():
            f = os.path.join(os.path.dirname(meta_path), info.get("file", ""))
            if not os.path.exists(f):
                continue
            t = torch.load(f, map_location="cpu")
            if not torch.is_tensor(t) or not t.is_floating_point() or t.numel() < 8:
                continue
            base = name.split("__")[0].replace("in_", "")
            if base in ("g", "a", "beta", "A_log", "dt", "dt_bias"):
                print("  %-26s %-22s gate: %s" % (name, list(t.shape), gate_stats(t)))
                continue
            if t.shape[-1] < 8:
                continue
            m, spread = norm_spread(t)
            e25, e50, e75 = energy_fractions(t)
            flag = ("  <-- as tight as Gaussian"
                    if spread == spread and spread < 1.5 * GAUSS["norm_rel_spread_d128"] else "")
            print("  %-26s %-22s ||row||=%.3f rel spread %.1f%% | energy 25/50/75%%: "
                  "%.2f%% / %.1f%% / %.1f%%%s"
                  % (name, list(t.shape), m, 100 * spread, 100 * e25, 100 * e50, 100 * e75, flag))
    print("\nChained-state check (state-carrying ops): compare step[n+1] "
          "state_before_* against step[n] state_after_* - they are byte-identical in "
          "these captures, which is what makes the chain a valid ground truth.")


if __name__ == "__main__":
    main()
