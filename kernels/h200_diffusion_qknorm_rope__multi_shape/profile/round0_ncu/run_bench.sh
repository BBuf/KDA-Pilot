#!/bin/bash
# Benchmark driver (run inside the container, from the cand root). Captures GPU idleness
# BEFORE and AFTER EACH run, appended as a timestamped section so EVERY benchmark.csv run has
# committed raw before/after evidence (benchmark provenance). Records the exact reproducible command + NCU
# provenance once, runs benchmark.py (which stamps the same command into every CSV row), and
# propagates benchmark.py's exit code.
set -u
GPU="${KDA_GPU_ID:-7}"
HOST="${KDA_HOST:-ion8-h200}"
CONTAINER="${KDA_CONTAINER:-sglang_omni_bbuf_kda}"
WORKDIR="$(pwd)"
PYP="${PYTHONPATH:-/home/sglang-omni/bbuf/repos/sglang/python}"
ND=profile/round0_ncu
STATE="$ND/gpu_state.md"
QUERY="index,name,utilization.gpu,memory.used,memory.total"
mkdir -p "$ND"

export KDA_CMD="ssh ${HOST} 'docker exec ${CONTAINER} env CUDA_VISIBLE_DEVICES=${GPU} KDA_HOST=${HOST} KDA_GPU_ID=${GPU} KDA_CONTAINER=${CONTAINER} KDA_REMOTE_WORKDIR=${WORKDIR} PYTHONPATH=${PYP} bash -lc \"cd ${WORKDIR} && bash ${ND}/run_bench.sh\"'"
export KDA_GPU_STATE_FILE="$STATE"
export KDA_CONTAINER="$CONTAINER"
export KDA_REMOTE_WORKDIR="$WORKDIR"
RUNTS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# Static header + command + NCU provenance: written ONCE (first run only); per-run idleness
# sections accumulate below so multiple benchmark.csv runs each keep raw before/after evidence.
if [ ! -f "$STATE" ]; then
  {
    echo "# GPU-state + command provenance -- h200_diffusion_qknorm_rope__multi_shape"
    echo
    echo "- Host: ${HOST}  Container: ${CONTAINER}  GPU id: ${GPU}"
    echo "- Workdir (in container): ${WORKDIR}"
    echo "- sglang PYTHONPATH: ${PYP}"
    echo
    echo "## Exact benchmark command (reproducible)"
    echo '```bash'
    echo "${KDA_CMD}"
    echo '```'
    echo
    echo "## NCU collection provenance"
    echo "NCU \`--set full\` profiles were collected on the same idle GPU ${GPU} via \`${ND}/run_full.sh\`:"
    echo '```bash'
    echo "ncu --set full --target-processes all --kernel-name regex:fused_qknorm_rope \\"
    echo "    --launch-skip 60 --launch-count 1 -o ${ND}/reports/full_<bucket> -f \\"
    echo "    python ${ND}/harness/prof_entry.py <T> <H>"
    echo '```'
    echo "The 2-head production kernel is byte-identical across round-0/1/2 source hashes (only a"
    echo "1-head A/B entrypoint and a Python fallback reference were added), so the metrics hold."
    echo
    echo "## Per-run nvidia-smi idleness (one BEFORE/AFTER section per benchmark.csv run)"
  } > "$STATE"
fi

{
  echo
  echo "### Run ${RUNTS} -- BEFORE"
  echo 'index, name, util.gpu(%), mem.used(MiB), mem.total(MiB)'
  echo '```'
  nvidia-smi -i "${GPU}" --query-gpu=${QUERY} --format=csv,noheader,nounits
  echo '```'
} >> "$STATE"

python benchmark.py
RC=$?

{
  echo "### Run ${RUNTS} -- AFTER (benchmark rc=${RC})"
  echo '```'
  nvidia-smi -i "${GPU}" --query-gpu=${QUERY} --format=csv,noheader,nounits
  echo '```'
} >> "$STATE"
echo "benchmark rc=${RC}; appended run ${RUNTS} to ${STATE}"
exit ${RC}
