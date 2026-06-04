# Baseline Source Lineage

## Upstream

- Repository: `git@github.com:sgl-project/sglang.git` (https://github.com/sgl-project/sglang)
- Local checkout used for the copy: `/Users/bbuf/工作目录/Common/sglang`
- Checkout HEAD at copy time: `0689ba84b88c991684b0f99ee9b50c3ce485b483` (branch `kda/group_norm_silu_export`, working tree clean for the copied files)
- Copied file: `python/sglang/jit_kernel/diffusion/triton/scale_shift.py`
  - Last upstream commit touching it: `47979fb252ce0954d1076c67183879bb52e17476` (2026-05-20, "[diffusion] fix: fix GLM-Image /v1/images/edits support (#25697)")
  - md5 of the source file at copy time: `b4c069aca94ccb7b2bbea2d2571634a1`
- Correctness-oracle reference (consulted, not copied; harness re-implements its torch reference):
  `python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py`
  - Last upstream commit touching it: `b7d62bd7241402035167a53ed3d53df25ce0bff5` (2026-05-15)
  - md5 at consultation time: `050d5958d7b74b2f209e754d9fb18c23`

## Copied Files In This Workspace

- `baseline/scale_shift.py` — the three Triton kernels + Python wrappers, vendored.
- `baseline/__init__.py` — local re-export shim (new file, not from upstream).

## Local Edits To The Copy (complete list)

1. Added a provenance header comment block at the top of `baseline/scale_shift.py`.
2. Removed `from sglang.multimodal_gen.runtime.platforms import current_platform` (the only sglang import).
3. Removed the trailing platform-fallback re-binding block (`if current_platform.is_npu(): ... is_mps ... is_musa ... is_cpu ...`) that re-pointed `fuse_scale_shift_kernel` to non-CUDA fallbacks. This harness exercises the CUDA Triton path only; the deleted block is unreachable on the H200 target.

No other lines were changed; the Triton kernels and CUDA-path wrapper logic are byte-identical to upstream.

## Why Vendored

The kernel-pilot diffusion rules forbid importing or patching a live SGLang checkout during correctness/benchmark runtime (and the `sglang.jit_kernel.diffusion` import chain eagerly pulls `multimodal_gen`, which needs the heavy `[diffusion]` extra). The baseline therefore runs from this immutable local copy, exposed through the same thin local entry ABI as the candidate. `sglang.jit_kernel.utils.load_jit` is still used — strictly as the build utility for the candidate `.cuh` (absolute `cuda_files` path; zero writes into the checkout).

## Notable Baseline Behaviors (recovered contract, relevant to A/B fairness)

- `fuse_scale_shift_kernel(x, scale, shift, scale_constant=1.0, block_l=128, block_c=128)`:
  - asserts `x` CUDA (or XPU) and contiguous; returns `torch.empty_like(x)`; `numel()==0` early-return.
  - `scale_constant` is a `tl.constexpr` (compile-time specialization; production captures all pass `0`, default is `1.0`).
  - 2D/3D scale/shift are `expand()`ed to `(B, L, C)` and their (possibly non-contiguous / zero) strides are passed straight to the Triton kernel — NO copy (the wan-ti2v fp32 non-contiguous scale takes this path).
  - 4D `(B, F, 1, C)` scale path reshapes scale to `(B*F, C)` and shift to `(B*L, C)` with `.contiguous()` (no copy when inputs are contiguous); per-frame indexing `frame = t // (L / F)`; asserts `L % F == 0`; this path is `triton.autotune`d over `BLOCK_N` keyed on `inner_dim`.
  - scalar/scalar fast path: if both scale and shift are scalars AND both zero (checked via a host sync `.any().to("cpu", non_blocking=True)`), returns `output.copy_(x)`.
  - Math `y = x * (scale_constant + scale) + shift` computed in the promoted dtype of the operands (bf16 x + fp32 scale → fp32 compute, store rounds to x dtype).
- `fuse_layernorm_scale_shift_gate_select01_kernel(x, weight, bias, scale0, shift0, gate0, scale1, shift1, gate1, index, eps)`:
  - asserts x CUDA + contiguous; modulation tensors must be 2D `(B, C)` (each `.contiguous()`-enforced in the wrapper); `index` 2D `(B, L)` (contiguous-enforced); optional `weight`/`bias` 1D `[C]` (contiguous-enforced) with `HAS_WEIGHT/HAS_BIAS` constexpr flags (sentinel = `x_2d` when None).
  - One Triton program per row, grid `(B*L,)`, `BLOCK_N = next_pow2(C)` capped at `65536 // element_size` (raises beyond), `num_warps=4, num_stages=4`.
  - LayerNorm in fp32: `mean = sum(x)/C`; centered biased variance `sum((x-mean)^2 masked)/C`; `rstd = rsqrt(var+eps)`; optional `*weight`, `+bias`.
  - Per-row scalar `idx = index[b, l].to(int1)` selects modulation set 1 vs 0 (uniform branch, 3 loads); scale/shift load `.to(float32)`, gate loads in NATIVE dtype; `y = x_hat * (1.0 + scale) + shift` stored to output dtype; gate stored as loaded.
  - Returns `(output, gate_out)`, both `empty_like(x)`.
- `fuse_residual_layernorm_scale_shift_gate_select01_kernel(x, residual, residual_gate, weight, bias, scale0, shift0, gate0, scale1, shift1, gate1, index, eps)`:
  - additionally asserts residual/residual_gate contiguous and same shape as x.
  - `residual_out = residual + residual_gate * x` computed in fp32, stored (rounded to output dtype), and the LayerNorm consumes the UNROUNDED fp32 `residual_out` values.
  - Returns `(output, residual_out, gate_out)`.

## Equivalence Check (one-time, copied baseline vs live SGLang)

- Status: DONE — **EQUIVALENT, 21/21 cases bit-identical** (all 15 production rows + 6 grid extras covering fp16/fp32, 4D, scalar, broadcastable-3D, affine select01/residual).
- Host: `ion-h200-8`, container `sglang_bbuf`, GPU id 3 (NVIDIA H200, idle: 0% util / 0 MiB before run), torch 2.11.0+cu130, triton 3.6.0.
- Live module: `/home/sglang-omni/bbuf/repos/sglang/python/sglang/jit_kernel/diffusion/triton/scale_shift.py` at sglang commit `84e1108312b52f8e00032845af2d85a3073d8aae` — file md5 `b4c069aca94ccb7b2bbea2d2571634a1`, byte-identical to the copy source (different checkout HEAD, same file content).
- Command: `CUDA_VISIBLE_DEVICES=3 python bench/equivalence_check.py --sglang-python /home/sglang-omni/bbuf/repos/sglang/python --json $REMOTE_KDA_DIR/equivalence_report.json` from `$REMOTE_KDA_DIR/kernel` (REMOTE_KDA_DIR=`/home/sglang-omni/bbuf/kda_runs/h200_diffusion_fuse_scale_shift__multi_shape/20260604-rlcr-r0`).
- Raw report: `$REMOTE_KDA_DIR/equivalence_report.json` (remote). The copy is now FROZEN; all later correctness/benchmark runs use `baseline/` only.
