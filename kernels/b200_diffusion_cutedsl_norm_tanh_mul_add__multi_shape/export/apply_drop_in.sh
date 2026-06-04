#!/usr/bin/env bash
# Self-contained drop-in installer for the native norm-tanh-modulation kernels.
#
# Usage: ./apply_drop_in.sh <sglang-checkout-root>
#
# Copies the device code + Python integration into the checkout and inserts the
# routing lines inside the existing torch.library.custom_op bodies (the
# registrations themselves are untouched). Idempotence guard: refuses to patch
# twice. Reverse with:
#   git -C <root> checkout -- python/sglang/jit_kernel/diffusion/cutedsl/norm_tanh_mul_add_norm_scale.py
#   rm python/sglang/jit_kernel/csrc/diffusion/norm_tanh_modulation.cuh \
#      python/sglang/jit_kernel/diffusion/norm_tanh_modulation.py
set -euo pipefail

SGL_ROOT="${1:?usage: apply_drop_in.sh <sglang-checkout-root>}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TASK_ROOT="$(cd "$HERE/.." && pwd)"

CUH_SRC="$TASK_ROOT/src/norm_tanh_cuda/norm_tanh_mul_add.cuh"
PY_SRC="$HERE/sglang_integration/norm_tanh_modulation.py"
CUH_DST="$SGL_ROOT/python/sglang/jit_kernel/csrc/diffusion/norm_tanh_modulation.cuh"
PY_DST="$SGL_ROOT/python/sglang/jit_kernel/diffusion/norm_tanh_modulation.py"
CUTEDSL="$SGL_ROOT/python/sglang/jit_kernel/diffusion/cutedsl/norm_tanh_mul_add_norm_scale.py"

echo "== manifest (sha256) =="
shasum -a 256 "$CUH_SRC" "$PY_SRC" 2>/dev/null || sha256sum "$CUH_SRC" "$PY_SRC"

grep -q "norm_tanh_modulation" "$CUTEDSL" && {
  echo "ERROR: $CUTEDSL already patched"; exit 1; }

cp "$CUH_SRC" "$CUH_DST"
cp "$PY_SRC" "$PY_DST"

python3 - "$CUTEDSL" <<'PYEOF'
import sys
from pathlib import Path

target = Path(sys.argv[1])
src = target.read_text()
anchor = "    stream = cuda.CUstream(torch.cuda.current_stream().cuda_stream)\n"
assert src.count(anchor) == 2, f"anchor count {src.count(anchor)} != 2"
v1_route = (
    "    from sglang.jit_kernel.diffusion.norm_tanh_modulation import (\n"
    "        native_supported, native_fused_norm_tanh_mul_add)\n"
    "    if native_supported(x, weight, bias, scale, shift, None, None, None, norm_type):\n"
    "        return native_fused_norm_tanh_mul_add(x, weight, bias, scale, shift, norm_type, eps)\n"
)
v2_route = (
    "    from sglang.jit_kernel.diffusion.norm_tanh_modulation import (\n"
    "        native_supported, native_fused_norm_tanh_mul_add_norm_scale)\n"
    "    if native_supported(x, weight, bias, scale, shift, weight2, bias2, scale2, norm_type):\n"
    "        return native_fused_norm_tanh_mul_add_norm_scale(\n"
    "            x, weight, bias, scale, shift, weight2, bias2, scale2, norm_type, eps)\n"
)
first = src.index(anchor)
second = src.index(anchor, first + len(anchor))
patched = src[:first] + v1_route + src[first:second] + v2_route + src[second:]
target.write_text(patched)
print("routing inserted into both custom-op bodies (registrations untouched)")
PYEOF

echo "drop-in applied to $SGL_ROOT"
