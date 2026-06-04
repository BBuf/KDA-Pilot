#!/usr/bin/env bash
# In-SGLang export + drop-in replacement test (the promotion arbiter).
# Runs inside sglang_bbuf on ion-b200. Task-owned clone only; the shared
# /sgl-workspace/sglang checkout is never modified.
set -euo pipefail

RKD=/home/sglang-omni/bbuf/kda_runs/b200_diffusion_cutedsl_norm_scale_shift__multi_shape/2026-06-04_15-19-43
WS="$RKD/workspace"
EXPORT="$RKD/sglang_export"
GPU="${REMOTE_GPU_ID:-0}"
PIN=edb1b3f8f5ab066af1e9b6ee8e8738fadcfa77e7

mkdir -p "$RKD/logs"
nvidia-smi --query-gpu=index,utilization.gpu,memory.used --format=csv,noheader,nounits | sed -n "$((GPU+1))p" > "$RKD/logs/export_gpu_before.txt"

echo "=== 1. task-owned editable checkout at the pinned commit ==="
if [ ! -d "$EXPORT/.git" ]; then
  git clone --shared --no-checkout /sgl-workspace/sglang "$EXPORT"
fi
cd "$EXPORT"
git checkout -f "$PIN" 2>&1 | tail -1
git clean -fdq python/sglang/jit_kernel || true

echo "=== 2. place candidate .cuh + native glue in-tree ==="
cp "$WS/src/csrc/norm_scale_shift.cuh" "$EXPORT/python/sglang/jit_kernel/csrc/diffusion/norm_scale_shift.cuh"
cp "$WS/export/norm_scale_shift_native.py" "$EXPORT/python/sglang/jit_kernel/diffusion/norm_scale_shift_native.py"

echo "=== 3. patch the public op bodies (registration untouched) ==="
python "$WS/export/apply_patch.py" "$EXPORT/python/sglang/jit_kernel/diffusion/cutedsl/scale_residual_norm_scale_shift.py"

echo "=== 4. import resolution check ==="
cd "$WS"
PYTHONPATH="$EXPORT/python" python - << 'PYEOF'
import sglang, pathlib
p = pathlib.Path(sglang.__file__).resolve()
assert "sglang_export" in str(p), f"resolved wrong sglang: {p}"
print(f"[ok] import sglang -> {p}")
PYEOF

echo "=== 5. official SGLang oracle (full grid) on the patched checkout ==="
CUDA_VISIBLE_DEVICES=$GPU PYTHONPATH="$EXPORT/python" \
  timeout 2400 python -m pytest "$EXPORT/python/sglang/jit_kernel/tests/diffusion/test_fused_norm_scale_shift.py" -q \
  2>&1 | tail -4 | tee "$RKD/logs/export_pytest_tail.log"

echo "=== 6. drop-in smoke: correctness echo + symmetric A/B + fallback probe ==="
CUDA_VISIBLE_DEVICES=$GPU PYTHONPATH="$EXPORT/python" \
  timeout 1200 python "$WS/export/smoke_bench.py" 2>&1 | tee "$RKD/logs/export_smoke.log"

echo "=== 7. files touched in the export checkout ==="
cd "$EXPORT" && git status --short python/sglang/jit_kernel | tee "$RKD/logs/export_files.log"

nvidia-smi --query-gpu=index,utilization.gpu,memory.used --format=csv,noheader,nounits | sed -n "$((GPU+1))p" > "$RKD/logs/export_gpu_after.txt"
echo "=== gpu before/after ==="
cat "$RKD/logs/export_gpu_before.txt" "$RKD/logs/export_gpu_after.txt"
echo "EXPORT_TEST_DONE"
