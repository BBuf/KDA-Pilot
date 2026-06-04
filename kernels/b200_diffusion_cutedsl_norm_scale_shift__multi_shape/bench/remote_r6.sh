#!/usr/bin/env bash
# Round-1 evidence run: correctness at current HEAD + r6-final benchmark with
# locally-auditable idle proof, plus NCU session text exports for the five
# profile runs. Executed inside sglang_bbuf on ion-b200.
set -euo pipefail

RKD=/home/sglang-omni/bbuf/kda_runs/b200_diffusion_cutedsl_norm_scale_shift__multi_shape/2026-06-04_15-19-43
WS="$RKD/workspace"
GPU="${REMOTE_GPU_ID:-1}"
EV="$WS/bench/evidence/r6-final"

cd "$WS"
mkdir -p "$EV"

snapshot() {  # full all-GPU state + compute apps, taken OUTSIDE any CUDA process
  {
    echo "# $1 $(date -u +%Y-%m-%dT%H:%M:%SZ) host=$(hostname) selected_gpu=$GPU"
    echo "## nvidia-smi --query-gpu=index,name,uuid,utilization.gpu,memory.used"
    nvidia-smi --query-gpu=index,name,uuid,utilization.gpu,memory.used --format=csv,noheader,nounits
    echo "## nvidia-smi --query-compute-apps=gpu_uuid,pid,process_name,used_memory"
    nvidia-smi --query-compute-apps=gpu_uuid,pid,process_name,used_memory --format=csv,noheader,nounits || true
  } > "$EV/allgpu_$1.txt"
}

echo "=== correctness at current HEAD ==="
CUDA_VISIBLE_DEVICES=$GPU KDA_RUN_CORRECTNESS=1 KDA_IMPL=candidate \
  timeout 2400 python -m pytest tests/test_correctness.py -x -q 2>&1 | tail -3
rc=${PIPESTATUS[0]}
[ $rc -ne 0 ] && { echo CORRECTNESS_FAILED; exit $rc; }

echo "=== external pre-run snapshot ==="
snapshot before

echo "=== r6-final benchmark (idle-gated) ==="
CUDA_VISIBLE_DEVICES=$GPU REMOTE_GPU_ID=$GPU timeout 3000 \
  python bench/benchmark.py --impl both --gpu-id "$GPU" --run-id r6-final \
  --candidate-layer shipping 2>&1 | tail -6
rc=${PIPESTATUS[0]}

echo "=== external post-exit snapshot ==="
snapshot after
[ $rc -ne 0 ] && { echo BENCHMARK_REJECTED_OR_FAILED rc=$rc; exit $rc; }

echo "=== NCU session text exports + hashes for the five profile runs ==="
for rep in profile/*/reports/*.ncu-rep; do
  txt="${rep%.ncu-rep}_session.txt"
  ncu -i "$rep" --page session > "$txt" 2>/dev/null || echo "(session export failed for $rep)" > "$txt"
  sha256sum "$rep" >> "$WS/profile/ncu_report_hashes.txt"
done
sort -u "$WS/profile/ncu_report_hashes.txt" -o "$WS/profile/ncu_report_hashes.txt"
echo "R5_DONE"
