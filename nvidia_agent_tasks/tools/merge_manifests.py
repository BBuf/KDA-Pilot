"""Merge the per-process shape manifests written by nvcap into one file.

    python merge_manifests.py <capture_dir>          # writes shape_manifest.json

Records are keyed by (op, group, signature) and their counts are summed, so a
TP-parallel or worker-parallel run yields one manifest with the total real-traffic
call count. A signature that appears in any real group is removed from the
warmup-only list.
"""
import glob, json, os, sys

d = sys.argv[1]
real, warm, pids = {}, {}, []
for p in sorted(glob.glob(os.path.join(d, "shape_manifest_pid*.json"))):
    try:
        m = json.load(open(p))
    except Exception as exc:
        print("skip %s: %r" % (p, exc)); continue
    pids.append(m.get("pid"))
    for bucket, dst in (("real_workload_shapes", real), ("warmup_only_shapes", warm)):
        for r in m.get(bucket, []):
            k = (r["op"], r["group"], r["signature"])
            if k in dst:
                dst[k]["count"] += r["count"]
            else:
                dst[k] = dict(r)
for k in list(warm):
    if any(k[0] == rk[0] and k[2] == rk[2] for rk in real):
        del warm[k]
out = {
    "capture_tool": "nvcap.py + merge_manifests.py",
    "processes_merged": pids,
    "note": ("counts are summed across every process that ran a wrapped op "
             "(TP ranks, diffusion workers). warmup_only_shapes holds signatures "
             "never seen while a capture-group label was active."),
    "real_workload_shapes": sorted(real.values(), key=lambda r: -r["count"]),
    "warmup_only_shapes": sorted(warm.values(), key=lambda r: -r["count"]),
}
json.dump(out, open(os.path.join(d, "shape_manifest.json"), "w"), indent=2)
print("merged %d processes -> %d real / %d warmup signatures"
      % (len(pids), len(out["real_workload_shapes"]), len(out["warmup_only_shapes"])))
