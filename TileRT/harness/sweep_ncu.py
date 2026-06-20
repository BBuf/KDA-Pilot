"""Drive >=3x ncu measurements across all validated oracle ops (task B5).

For each op: kernel-name regex + the seq list to measure. Runs measure_ncu.one_run
RUNS times per (op, seq), records min/median/max + dispersion, writes a markdown
table to docs/tilert_reference.md and a json sidecar. Run on an idle B200, GPU7.

    CUDA_VISIBLE_DEVICES=7 python sweep_ncu.py --runs 3
"""
import argparse
import json
import os
import statistics

from measure_ncu import one_run

# op (tilert_oracle CASES key) -> (kernel-name regex, [seqs to measure])
OPS = {
    "rmsnorm":            ("RMSNormExecutorImpl",        [1, 2, 4]),
    "rmsnorm_quant":      ("RMSNormQuantExecutorImpl",   [1, 2, 4]),
    "head_proj":          ("HeadProjExecutorImpl",       [1, 2, 4]),
    "rmsnorm_head_proj":  ("RMSNormHeadProjExecutorImpl", [1, 2, 4]),
    "rmsnorm_expert_proj":("RMSNormExpertProj",          [1, 2, 4]),
    "projx_wis":          ("ProjXWis",                   [1, 2, 4]),
    "projq_wqb":          ("ProjQWkvb",                  [1, 2, 4]),
    "projo_wkvb":         ("ProjOWkvb",                  [1, 2, 4]),
    "flash_sparse_mla":   ("Mla",                        [1, 2, 3, 4]),  # PureMlaDsv32 #1
    "rotate":             ("RotateExecutorImpl",         [1, 2, 4]),
    "qkv_rope":           ("QkvRope",                    [1, 2, 4]),
    "rmsnorm_kv":         ("RmsnormKv",                  [1, 2, 4]),
    "layernorm_rope_rotate": ("LayernormRopeRotate",     [1, 2, 4]),
    "rmsnorm_projq_wqb":  ("RmsnormProjQWqb",            [1, 2, 4]),
    "rmsnorm_projq_wqi":  ("RmsnormProjQWqi",            [1, 2, 4]),
    "rmsnorm_up_gate_silu": ("RMSNormUpGateSiLU",        [1, 2, 4]),
}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--dev", default="cuda:0")
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    only = set(a.only.split(",")) if a.only else set(OPS)

    results = {}
    for op, (kern, seqs) in OPS.items():
        if op not in only:
            continue
        for seq in seqs:
            durs, hbms, kname = [], [], None
            for _ in range(a.runs):
                res, err = one_run(op, seq, kern, a.dev)
                if res is None:
                    continue
                d, h = res
                durs.append(d)
                if h is not None:
                    hbms.append(h)
            if durs:
                med = statistics.median(durs)
                disp = (max(durs) - min(durs)) / med * 100 if med else 0
                hmed = statistics.median(hbms) if hbms else None
                results[f"{op}_s{seq}"] = dict(op=op, seq=seq, kernel=kern, n=len(durs),
                    min=round(min(durs), 3), median=round(med, 3), max=round(max(durs), 3),
                    disp_pct=round(disp, 1), hbm_pct=round(hmed, 1) if hmed else None)
                print(f"[{op} s{seq}] median={med:.3f}us disp={disp:.1f}% hbm={hmed} n={len(durs)}")
            else:
                results[f"{op}_s{seq}"] = dict(op=op, seq=seq, kernel=kern, n=0, error="no data")
                print(f"[{op} s{seq}] NO DATA (regex {kern})")

    # write json + markdown (robust to flat layouts: fall back to script dir)
    hdir = os.path.join(ROOT, "harness")
    ddir = os.path.join(ROOT, "docs")
    if not os.path.isdir(hdir):
        hdir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.isdir(ddir):
        ddir = hdir
    jpath = os.path.join(hdir, "ncu_results.json")
    json.dump(results, open(jpath, "w"), indent=2)
    md = ["# TileRT reference latencies (>=%d ncu runs, B200, median)\n" % a.runs,
          "Measured from the real `libtilert_dsv32.so` ops via ncu "
          "`gpu__time_duration.avg` on an idle B200 (GPU7). Median of >=%d isolated "
          "runs; dispersion = (max-min)/median. Only the **median** is the KDA target.\n" % a.runs,
          "| op | kernel | seq | median µs | min | max | disp%% | HBM%% |",
          "|---|---|---:|---:|---:|---:|---:|---:|"]
    for k, r in results.items():
        if r.get("n"):
            md.append(f"| {r['op']} | {r['kernel']} | {r['seq']} | **{r['median']}** | "
                      f"{r['min']} | {r['max']} | {r['disp_pct']} | {r['hbm_pct']} |")
        else:
            md.append(f"| {r['op']} | {r['kernel']} | {r['seq']} | — | — | — | — | (no data) |")
    open(os.path.join(ddir, "tilert_reference.md"), "w").write("\n".join(md) + "\n")
    print(f"\nwrote {ddir}/tilert_reference.md and {jpath}")


if __name__ == "__main__":
    main()
