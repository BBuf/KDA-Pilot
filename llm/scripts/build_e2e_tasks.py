#!/usr/bin/env python3
"""Build e2e-filtered kernel tasks from torch-profiler kernel_shapes_*.json.

Grouping is KERNEL-FAMILY primary (from the GPU kernel name) so a kernel is
never swept under an incidental Python op (e.g. a rope op showing up in an
attention kernel's CPU-op provenance). A clean sglang/sgl_kernel/jit_kernel op
is used only to NAME a family when their keywords agree. Excludes communication
and the vendor TRTLLM fused-MoE path (moe::dev / *_trtllm_*_moe_wrapper); keeps
the optimizable Triton fused_experts. Records per task the
model/scenario/dataset/concurrency/%-of-GPU + shapes as serving-profile
headroom proof. Generated tasks are standalone single-GPU kernel tasks; the
serving command is provenance, not the validation path.
"""
import argparse, json, os, re
from collections import defaultdict

LABELS = ["random_low","random_mid","random_high","sharegpt_low","sharegpt_mid","sharegpt_high"]
CONC = {"low":"1","mid":"32","high":"100"}

FAMILIES = [
    ("_chunk_scan","mamba2_ssm"),("_chunk_state","mamba2_ssm"),("_state_passing","mamba2_ssm"),
    ("segsum","mamba2_ssm"),("mamba","mamba2_ssm"),("selective_scan","mamba2_ssm"),
    ("causal_conv","causal_conv1d"),
    ("fused_add_rmsnorm","fused_add_rmsnorm"),("rmsnorm","rmsnorm"),("rms_norm","rmsnorm"),("layernorm","layernorm"),
    ("apply_rope","rope"),("rotary","rope"),("rope","rope"),
    ("moe_align","moe_align_block_size"),
    ("fused_experts","fused_moe_triton"),("fused_moe","fused_moe_triton"),
    ("merge_state","merge_state"),
    # Kimi-K3 kernel families (hybrid KDA/MLA stack, latent MoE)
    ("attn_res","attn_residual"),
    ("kda_decode_fusion","kda_fused_decode"),("kda_","kda_linear_attn"),
    ("route_radix","moe_route_radix"),("situ_and_mul","situ_and_mul"),

    # structural kernel types BEFORE activation keys (a gemm/bmm with a fused
    # silu/swiglu/gelu EPILOGUE is still a gemm/bmm, not a standalone activation):
    ("bmm","fp8_bmm"),
    ("fmha","attention"),("flashinfer","attention"),("batchprefill","attention"),("batchdecode","attention"),
    ("paged","attention"),("flash_fwd","attention"),("fwd_kernel","attention"),("mla","attention_mla"),("attention","attention"),
    ("splitkreduce","linear_gemm"),
    ("deep_gemm","linear_gemm"),("scaled_mm","linear_gemm"),("nvjet","linear_gemm"),("cutlass","linear_gemm"),
    ("w8a8","linear_gemm"),("sgemm","linear_gemm"),("gemm","linear_gemm"),
    ("static_quant","quant_fp8"),("per_token_group_quant","per_token_group_quant"),("per_token_quant","quant_fp8"),("quant","quant_fp8"),
    # activation keys LAST — only match standalone activation kernels:
    ("silu_and_mul","silu_and_mul"),("swiglu","silu_and_mul"),("silu","silu_and_mul"),
    ("gelu","gelu_and_mul"),("run_activation","activation"),("activation","activation"),
]
FAMILY_KEYWORDS = {
    "mamba2_ssm":["mamba","ssm","chunk","state_passing","scan"],"causal_conv1d":["causal_conv","conv1d","conv"],
    "attention":["attention","mha","flash","paged","prefill","decode"],"attention_mla":["mla","attention"],
    "rope":["rope","rotary"],"fused_moe_triton":["fused_experts","fused_moe","experts"],
    "moe_align_block_size":["moe_align"],"merge_state":["merge_state"],
    "attn_residual":["attn_res","aggregate"],"kda_fused_decode":["kda","fused_decode"],
    "kda_linear_attn":["kda","linear_attn"],"moe_route_radix":["route_radix","radix","gate"],
    "situ_and_mul":["situ"],
    "rmsnorm":["rmsnorm","rms_norm"],"fused_add_rmsnorm":["rmsnorm","fused_add"],"layernorm":["layernorm"],
    "silu_and_mul":["silu","swiglu","mul","gate_up"],"gelu_and_mul":["gelu"],"activation":["activation"],
    "fp8_bmm":["bmm"],"quant_fp8":["quant"],"per_token_group_quant":["quant","group"],
    "linear_gemm":["gemm","scaled_mm","linear"],
}

def slugify(v,n=160):
    v=re.sub(r"([A-Z]+)([A-Z][a-z])",r"\1_\2",v); v=re.sub(r"([a-z0-9])([A-Z])",r"\1_\2",v)
    out=re.sub(r"[^a-zA-Z0-9]+","_",v.lower()).strip("_")
    return (re.sub(r"_+","_",out)[:n].strip("_") or "kernel")

def kernel_family(name):
    n=name.lower()
    for k,v in FAMILIES:
        if k in n: return v
    return slugify(name,32)

def clean_op(samples, top):
    cands=[s.get("cpu_op") for s in (samples or []) if s.get("cpu_op")]+list(top or [])
    for c in cands:
        m=re.match(r"(sglang|sgl_kernel|jit_kernel)::([A-Za-z0-9_]+)", c or "")
        if m: return f"{m.group(1)}.{m.group(2)}"
    return None

IFACE_MAP = []  # from --interface-map: [(prefix_lower, interface, exclude, task_name)]


def iface_lookup(kname):
    interface, exclude, _ = iface_lookup3(kname)
    return interface, exclude


def iface_lookup3(kname):
    n = kname.lower()
    for prefix, interface, exclude, task_name in IFACE_MAP:
        if prefix in n:
            return interface, exclude, task_name
    return None, None, None


def excluded(cat, kname, co):
    n=kname.lower(); c=(co or "").lower()
    _, mapped_exclude = iface_lookup(kname)
    if mapped_exclude: return mapped_exclude
    if cat=="comm": return "comm"
    if any(t in n for t in ("moe::dev","routingcustom","finalizekernel","activationkernel")): return "fused_moe_trtllm"
    if ("trtllm" in c and "moe" in c) or ("trtllm" in n and "moe" in n): return "fused_moe_trtllm"
    if any(t in n for t in ("all_reduce","all_to_all","reduce_scatter","all_gather","nccl","alltoall",
                            "cross_device_reduce","device_reduce","custom_all_reduce")): return "comm"
    if any(t in c for t in ("all_reduce","outplace_all_reduce","moe_a2a","cross_device_reduce")): return "comm"
    return None

def name_family(fam, clean_weights):
    kws=FAMILY_KEYWORDS.get(fam,[fam])
    best=None
    for op,w in sorted(clean_weights.items(), key=lambda x:-x[1]):
        base=op.split(".")[-1].lower()
        if any(kw in base for kw in kws): best=op; break
    return best or fam

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--shapes-dir",required=True); ap.add_argument("--model",required=True)
    ap.add_argument("--model-slug",required=True); ap.add_argument("--cookbook-cmd",required=True)
    ap.add_argument("--tp",default="1"); ap.add_argument("--out-dir",required=True); ap.add_argument("--threshold",type=float,default=3.0)
    ap.add_argument("--provenance-note",default="",
                    help="extra sentence for prompt.md / profile_evidence.md, e.g. when the capture "
                         "host differs from the single-GPU optimization target")
    ap.add_argument("--interface-map",help="optional JSON of kernel-prefix -> Python interface (+ optional "
                                          "exclude reason); used for vendor exclusions and for naming kernels "
                                          "whose launcher registers no torch op")
    a=ap.parse_args()

    if a.interface_map:
        for row in json.load(open(a.interface_map))["map"]:
            IFACE_MAP.append((row["kernel_prefix"].lower(), row["interface"],
                              row.get("exclude"), row.get("task_name")))

    ops=defaultdict(lambda:{"labels":defaultdict(float),"kernels":set(),"cats":defaultdict(float),
                            "shapes":set(),"prov":set(),"clean":defaultdict(float)})
    dropped=[]
    for lab in LABELS:
        p=os.path.join(a.shapes_dir,f"kernel_shapes_{lab}.json")
        if not os.path.exists(p): continue
        for r in json.load(open(p)).get("rows",[]):
            co=clean_op(r.get("samples"),r.get("top_cpu_ops"))
            ex=excluded(r["category"],r["kernel"],co)
            if ex: dropped.append((r["kernel"][:55],r["category"],r["pct_of_gpu"],ex)); continue
            fam=kernel_family(r["kernel"]); e=ops[fam]
            e["labels"][lab]+=r["pct_of_gpu"]; e["kernels"].add(r["kernel"][:90])
            e["cats"][r["category"]]+=r["pct_of_gpu"]
            if co: e["clean"][co]+=r["pct_of_gpu"]
            for c in (r.get("top_cpu_ops") or [])[:3]:
                if c: e["prov"].add(c)
            for s in (r.get("samples") or [])[:3]:
                sa=s.get("shape_args",{}).get("Input Dims")
                if sa: e["shapes"].add(str(sa)[:80])

    ranked=sorted(ops.items(),key=lambda kv:max(kv[1]["labels"].values()),reverse=True)
    os.makedirs(a.out_dir,exist_ok=True)
    summary=[]; lowpct=[]
    for fam,e in ranked:
        maxpct=max(e["labels"].values())
        if maxpct<a.threshold: lowpct.append((fam,maxpct)); continue
        name=name_family(fam,e["clean"]); clean=name in e["clean"]
        mapped=None; mapped_task_name=None
        if not clean:
            for kname in sorted(e["kernels"]):
                mapped,_,mapped_task_name=iface_lookup3(kname)
                if mapped: break
            if mapped: name=mapped
        op_slug=slugify(mapped_task_name or name); task=f"{a.model_slug}__{op_slug}"
        d=os.path.join(a.out_dir,task); os.makedirs(os.path.join(d,"docs"),exist_ok=True)
        for sub in ("baseline","solution","bench","tests"):
            os.makedirs(os.path.join(d,sub),exist_ok=True); open(os.path.join(d,sub,".gitkeep"),"w").close()
        cat=max(e["cats"],key=lambda x:e["cats"][x])
        per={l:round(e["labels"][l],2) for l in LABELS if e["labels"].get(l,0)>0}
        best=max(e["labels"],key=lambda l:e["labels"][l]); dset,conc=best.rsplit("_",1)
        entry=name if (clean or mapped) else f"fresh_capture_required::{fam}"
        note=""
        if fam=="fused_moe_triton": note="Triton MoE expert-GEMM (sglang's own fused_experts/fused_moe kernel) — single-GPU optimizable; NOT the comm-fused trtllm MoE path (excluded)."
        if fam=="activation": note="Activation (SiLU/GELU+mul). Prior guidance: limited headroom — deprioritize."
        open(os.path.join(d,"config.toml"),"w").write(f"""[task]
slug = "{task}"
arch = "b200"
target_gpu = "NVIDIA B200"
family = "{cat}"
kernel_family = "{fam}"
model = "{a.model}"
model_slug = "{a.model_slug}"
entry_points = [
  "{entry}",
]
evidence_json = "docs/profile_evidence.json"
shape_source_json = "docs/captured_kernel_api_shapes.json"
workloads_json = "bench/workloads.json"

[selection]
method = "serving-profile GPU-time headroom (extract_kernel_shapes >2%, family-grouped; provenance only)"
max_pct_of_gpu = {round(maxpct,2)}
best_scenario = "{best}"
dataset = "{dset}"
concurrency = "{CONC.get(conc,conc)}"

[build]
language = "python/cuda"
baseline_entry_point = "baseline/<copied_sglang_interface>::baseline"
candidate_entry_point = "solution/<candidate_interface>::candidate"

[benchmark]
warmup_runs = 10
iterations = 200
num_trials = 7
use_isolated_runner = true
required_matched_ratio = 1.0
""")
        ev={"model":a.model,"model_slug":a.model_slug,
            "cookbook_cmd":"omitted from standalone kernel task; use bench/workloads.json and docs/captured_kernel_api_shapes.json for RLCR",
            "tp":a.tp,"capture_provenance_note":a.provenance_note,
            "python_interface":entry,"kernel_family":fam,"profiler_op_provenance":sorted(e["prov"])[:6],
            "category":cat,"gpu_kernels":sorted(e["kernels"]),"pct_of_gpu_by_scenario":per,
            "max_pct_of_gpu":round(maxpct,2),"best_scenario":best,"input_shapes":[],
            "input_shapes_replaced_by":"docs/captured_kernel_api_shapes.json",
            "standalone_workloads_json":"bench/workloads.json",
            "scenarios":"random/sharegpt x low(conc1)/mid(conc32)/high(conc100), ISL~1000 OSL~1000"}
        if note: ev["note"]=note
        json.dump(ev,open(os.path.join(d,"docs","profile_evidence.json"),"w"),indent=2)
        per_md="\n".join(f"| {l.rsplit('_',1)[0]} | conc {CONC.get(l.rsplit('_',1)[1],'')} | {e['labels'][l]:.2f}% |"
                         for l in LABELS if e["labels"].get(l,0)>0)
        open(os.path.join(d,"docs","profile_evidence.md"),"w").write(f"""# Profile evidence — {task}

**Standalone kernel target: {maxpct:.1f}% of total serving GPU time** (max across scenarios) on
`{a.model}`, from the exact cookbook-aligned profile. This is target-selection
provenance and headroom context, not the validation path. {'Clean Python interface (profiler provenance).' if clean else 'Profiler kernel-family; fresh kernel API workload capture required before RLCR.'}
{(chr(10)+'> '+note+chr(10)) if note else ''}
- Model: `{a.model}` (slug `{a.model_slug}`, tp={a.tp})
{('- Capture provenance: ' + a.provenance_note + chr(10)) if a.provenance_note else ''}
- Python interface: `{entry}`
- Kernel family: `{fam}`  ·  Category: `{cat}`
- GPU kernel(s): {', '.join('`'+k+'`' for k in sorted(e['kernels']))}

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
{per_md}

**Peak: {maxpct:.1f}% in `{best}` ({dset}, concurrency {CONC.get(conc,conc)}).**

## Fresh captured kernel API shapes

- Shape source: `docs/captured_kernel_api_shapes.json`
- Standalone workloads: `bench/workloads.json`

Populate these files from a real model execution before starting RLCR. Do not
use profiler shape strings as benchmark inputs.

## Validation Policy

Normal RLCR kernel work is a standalone single-GPU optimization task. Use the
captured workload set above for correctness and benchmark acceptance on one idle
target GPU, and keep external runtime-readiness or fleet-level A/B gates out of
the task loop.
""")
        open(os.path.join(d,"prompt.md"),"w").write(f"""# KDA Prompt: {task}

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `{entry}`

**{maxpct:.1f}% of total serving GPU time** on `{a.model}` (cookbook-aligned
profile, peak `{best}`) — a serving-profile headroom signal used to select this
standalone kernel task. Family `{fam}`, category `{cat}`.{(' '+note) if note else ''}

{(a.provenance_note + chr(10) + chr(10)) if a.provenance_note else ''}See `docs/profile_evidence.md` for the per-scenario %-of-GPU and GPU kernel
selection provenance, then use `bench/workloads.json` as the standalone shape
source. For the normal RLCR loop, optimize and validate via the task-local
standalone benchmark on one idle target GPU, without adding external
runtime-readiness or fleet-level A/B gates. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
""")
        summary.append((task,cat,fam,maxpct,best,"yes" if clean else ("mapped" if mapped else "role")))

    with open(os.path.join(a.out_dir,f"_INDEX_{a.model_slug}.md"),"w") as f:
        f.write(f"# {a.model_slug} — standalone kernel task selection\n\n- Model: `{a.model}` (tp={a.tp})\n")
        f.write("- Task mode: standalone single-GPU kernel optimization from captured workload files.\n")
        f.write(f"- Kept: max serving-profile GPU-time share `>= {a.threshold}%`, non-comm, non-trtllm-MoE\n\n")
        f.write("| task | category | family | max % GPU | peak scenario | clean op |\n|---|---|---|---:|---|---|\n")
        for t,cat,fam,mp,bl,cl in sorted(summary,key=lambda x:-x[3]):
            f.write(f"| `{t}` | {cat} | {fam} | {mp:.1f}% | {bl} | {cl} |\n")
        f.write(f"\n## Dropped < {a.threshold}%\n\n");
        for nm,mp in sorted(lowpct,key=lambda x:-x[1])[:15]: f.write(f"- {nm}: {mp:.1f}%\n")
        f.write("\n## Excluded (comm / trtllm fused-MoE)\n\n"); seen=set()
        for kn,cat,pct,sr in sorted(dropped,key=lambda x:-x[2]):
            if kn in seen or pct<2.0: continue
            seen.add(kn); f.write(f"- {kn} ({cat}, {sr}): up to {pct:.1f}%\n")

    print(f"KEPT {len(summary)} (>= {a.threshold}%):")
    for t,cat,fam,mp,bl,cl in sorted(summary,key=lambda x:-x[3]):
        print(f"  {mp:5.1f}%  {t}  [{cat}/{fam}, {bl}, {cl}]")
    print(f"  dropped<thr: {len(lowpct)}; excluded comm/trtllm-moe: {len(set(d[0] for d in dropped))}")

if __name__=="__main__": main()
