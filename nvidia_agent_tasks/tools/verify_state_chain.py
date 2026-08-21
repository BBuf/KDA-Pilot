"""Verify that a captured decode chain is a valid ground truth.

    python verify_state_chain.py <task>/bench/tensors/<chain_dir>

Checks, for consecutive steps, that step[n+1]'s state-before equals step[n]'s
state-after byte for byte. If that holds, the chain can be replayed by a candidate
kernel and compared on the FINAL state, which is the gate for state-carrying
kernels (see docs/anti_hack_contract.md). It also prints the per-step relative
change of the state, i.e. the scale against which a deviation should be judged.
"""
import glob, os, sys, torch

d = sys.argv[1]
steps = sorted(glob.glob(os.path.join(d, "step*")))
static = os.path.join(d, "static")
if os.path.isdir(static):
    print("compact chain: %d tensors are per-step invariant and live in static/"
          % len(glob.glob(os.path.join(static, "*.pt"))))
if len(steps) < 2:
    raise SystemExit("need at least two steps in %s" % d)
names = {os.path.basename(f)[len("state_after_"):-3]
         for f in glob.glob(os.path.join(steps[0], "state_after_*.pt"))}
if not names:
    raise SystemExit("no state_after_*.pt in %s - not a state-carrying capture" % steps[0])
print("chain: %d steps, state tensors: %s" % (len(steps), ", ".join(sorted(names))))
ok = bad = 0
for name in sorted(names):
    print("\n== %s" % name)
    for i in range(len(steps) - 1):
        a = torch.load(os.path.join(steps[i], "state_after_%s.pt" % name), map_location="cpu")
        b_path = os.path.join(steps[i + 1], "state_before_%s.pt" % name)
        if not os.path.exists(b_path):
            print("  step%03d -> step%03d : no state_before, skipped" % (i, i + 1)); continue
        b = torch.load(b_path, map_location="cpu")
        same = a.shape == b.shape and torch.equal(a, b)
        rel = float((a.float() - torch.load(os.path.join(steps[i], "state_before_%s.pt" % name),
                                           map_location="cpu").float()).norm()
                    / max(float(a.float().norm()), 1e-30))
        print("  step%03d -> step%03d : %s   (this step changed the state by %.1f%%)"
              % (i, i + 1, "byte-identical" if same else "MISMATCH", 100 * rel))
        ok += int(same); bad += int(not same)
print("\n%d links byte-identical, %d mismatched" % (ok, bad))
print("verdict: %s" % ("chain is a valid ground truth - gate a candidate on the FINAL state"
                       if bad == 0 else "chain is broken; recapture with --disable-radix-cache"))
