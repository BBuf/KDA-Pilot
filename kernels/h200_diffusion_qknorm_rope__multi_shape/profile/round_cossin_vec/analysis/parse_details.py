import csv, statistics

WANT = ["Duration", "Registers Per Thread", "Achieved Occupancy", "Theoretical Occupancy",
        "DRAM Throughput", "Compute (SM) Throughput", "Memory Throughput", "L2 Hit Rate",
        "Waves Per SM", "Grid Size", "Block Size", "Stall Long Scoreboard",
        "Warp Cycles Per Issued Instruction", "Executed Ipc Active", "Achieved Active Warps Per SM"]

def load(path):
    metrics = {}
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh):
            name = row.get("Metric Name", "")
            if name in WANT:
                val = row.get("Metric Value", "").replace(" ", "").replace(",", "")
                try:
                    metrics.setdefault((name, row.get("Metric Unit", "")), []).append(float(val))
                except ValueError:
                    pass
    return metrics

for tag, path in [("VARIANT", "full_variant_details.csv"), ("INCUMBENT", "full_incumbent_details.csv")]:
    print(f"== {tag} (median over launches) ==")
    m = load(path)
    for (name, unit), vals in sorted(m.items()):
        print(f"  {name:38s} {statistics.median(vals):12.3f} {unit}  (n={len(vals)})")
