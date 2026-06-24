import os, re, glob, json
root = "/sgl-workspace/sglang/docs_new/cookbook/autoregressive"
rows = []
for f in sorted(glob.glob(root + "/**/*.mdx", recursive=True)):
    txt = open(f, errors="replace").read()
    # join line-continuations
    joined = re.sub(r"\\\s*\n", " ", txt)
    name = os.path.relpath(f, root).replace(".mdx","")
    # find all sglang serve commands
    serves = re.findall(r"sglang serve\s+([^\s\\]+)([^\n]*)", joined)
    tps=set(); models=set(); nnodes=set(); quants=set()
    for model, rest in serves:
        models.add(model.strip("\"'"))
        for m in re.findall(r"--tp(?:-size)?[= ]+(\d+)", rest): tps.add(int(m))
        for m in re.findall(r"--nnodes[= ]+(\d+)", rest): nnodes.add(int(m))
        for m in re.findall(r"--ep(?:-size)?[= ]+(\d+)", rest): tps.add(int(m))  # ep implies gpus
        for m in re.findall(r"--quantization[= ]+(\S+)", rest): quants.add(m.strip("\"'"))
    # also catch standalone --tp in text
    for m in re.findall(r"--tp(?:-size)?[= ]+(\d+)", joined): tps.add(int(m))
    for m in re.findall(r"--nnodes[= ]+(\d+)", joined): nnodes.add(int(m))
    mintp = min(tps) if tps else 1
    maxtp = max(tps) if tps else 1
    mn = max(nnodes) if nnodes else 1
    rows.append({"name":name,"models":sorted(models)[:2],"min_tp":mintp,"max_tp":maxtp,"nnodes":mn,"quants":sorted(quants)})
# sort by min_tp then name
rows.sort(key=lambda r:(r["nnodes"]>1, r["min_tp"], r["name"]))
print(f"{'recipe':<34}{'min_tp':>7}{'max_tp':>7}{'nnodes':>7}  model_id / quant")
for r in rows:
    mdl = r["models"][0] if r["models"] else "?"
    q = ",".join(r["quants"]) if r["quants"] else ""
    print(f"{r['name']:<34}{r['min_tp']:>7}{r['max_tp']:>7}{r['nnodes']:>7}  {mdl} {q}")
print(f"\nTOTAL recipes: {len(rows)}")
