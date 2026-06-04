# SGLang jit_kernel export — continuation round (tilev1)

> **Historical note**: the previous version of this document described the
> normv5 overlay export (`kda_kernels.install()` monkey-patch) and its
> `1.4223x` claim. That number was measured through a plain-callable overlay
> that bypassed the production custom-op layer — **historical overlay
> evidence, superseded** (kernel-pilot rule change `cc17c1149`). The promotion
> arbiter is now the in-SGLang dispatch-symmetric A/B below.

## PR-facing benchmark — vs sglang MAIN (`8933ec8772`)

Per the standing ruling (PR baseline = sglang main, never a container pin),
the promotion numbers below were re-anchored against an origin/main worktree
(`git fetch origin main` → task-owned detached worktree → everything resolved
with the worktree first on `PYTHONPATH`). The baseline slice has ZERO drift
between the loop's container pin `84e1108312` and main `8933ec8772`
(`norm.py`, `rmsnorm_onepass.py`, `custom_op.py` byte-identical; only
`jit_kernel/utils.py` gained a JIT source-hash cache improvement), so the
4-file shipping patch is byte-identical against either tree.

| shape | main wall/dev (us) | native wall/dev (us) | wall x | dev-rate x |
|---|---|---|---|---|
| helios fp32 [8640,5120] | 111.19 / 90.92 | 100.09 / 89.18 | 1.111 | 1.020 |
| hunyuan bf16 [648720,128] | 108.48 / 81.83 | 95.28 / 81.02 | 1.139 | 1.010 |
| hunyuan bf16 [1320,128] | 32.61 / 24.87 | 17.45 / 11.28 | 1.869 | 2.205 |
| hunyuan bf16 [650040,128] | 108.76 / 82.28 | 95.51 / 81.25 | 1.139 | 1.013 |
| zimage bf16 [16384,128] | 32.67 / 24.76 | 17.72 / 11.26 | 1.844 | 2.199 |
| zimage bf16 [4096,128] | 32.23 / 24.89 | 17.39 / 11.35 | 1.853 | 2.194 |
| **geomean** | | | **1.4475** | 1.493 |

Same methodology as the pin-anchored arbiter below (2 alternated off/on
process pairs, idle-gated, wall = per-call median, dev = stream-saturated
batched rate). On the main worktree: oracle **288/288** with native ON (and
OFF), all fallback/compile probes pass, and the workspace regression suite is
**405/405** with `PYTHONPATH` resolving sglang from main. Raw artifacts:
`arbiter_main_{off,on}_{1,2}.json` under `REMOTE_KDA_DIR`; ledger rows:
`benchmark.csv` `mode=intree_arbiter_vs_main*`.

## Promotion arbiter (PASS) — in-tree dispatch-symmetric env-toggle A/B (loop evidence vs container pin `84e1108312`)

- **Mechanism**: ONE patched SGLang worktree (task-owned, detached at the
  container's commit `84e1108312`: `REMOTE_KDA_DIR/sglang_arbiter`). The
  native fast paths are inserted INSIDE the unchanged public bodies —
  `norm_infer` (plain function) and `_triton_one_pass_rms_norm_cuda` (the
  `@register_custom_op(op_name="triton_one_pass_rms_norm_cuda", out_shape="x")`
  body; decorator byte-unchanged) — gated PER TENSOR DEVICE to Hopper
  (CC 9.0, the only validated architecture:
  `torch.cuda.get_device_capability(x.device.index) == (9, 0)`, cache keyed
  on the device index so heterogeneous multi-GPU processes decide per
  device), by `SGLANG_NATIVE_NORM_INFER` / `SGLANG_NATIVE_ONE_PASS_RMS_NORM`
  (default on), and by a successful jit build performed under the tensor's
  device context (`with torch.cuda.device(x.device.index)`, so SGLang's
  current-device-based JIT arch selection compiles for the launching
  device), using the `qknorm_rope.py`
  in-tree pattern (`@cache_once` + `@torch.compiler.assume_constant_result`
  static gate, lazy `load_jit` loader, automatic fallback to the Triton path).
  Both A/B legs run the SAME patched checkout — wrapper, registration, and the
  inserted dispatch branch are byte-identical; only the env toggle differs.
  Clean-vs-patched comparisons were not used.
- **SGLang files touched** (shipping patch: `docs/sglang_export.patch`, 4 files):
  - `python/sglang/jit_kernel/diffusion/triton/norm.py` (fast path inside
    `norm_infer` + gate/loader)
  - `python/sglang/jit_kernel/diffusion/triton/rmsnorm_onepass.py` (fast path
    inside the registered op body + gate/loader)
  - `python/sglang/jit_kernel/csrc/diffusion/rms_norm_d128_tile16.cuh` (new)
  - `python/sglang/jit_kernel/csrc/diffusion/layer_norm_n5120.cuh` (new)
- **load_jit wiring** (in-tree build path, flags match SGLang, no
  `--use_fast_math`):
  - LN: `load_jit("kda_layer_norm", *make_cpp_args(5120, True, False,
    torch.float32), cuda_files=["diffusion/layer_norm_n5120.cuh"],
    cuda_wrappers=[("layer_norm", f"LayerNormKernel<{targs}>::run")])`
  - RMS: `load_jit("kda_rms_norm_tile", *make_cpp_args(128, 8, 128, False,
    False, torch.bfloat16), cuda_files=["diffusion/rms_norm_d128_tile16.cuh"],
    cuda_wrappers=[("rms_norm_tile", f"RmsNormTileKernel<{targs}>::run")])`
- **Benchmark** (ion8-h200 GPU 0, idle-gated before/after each run; 4
  alternated process runs off,on,off,on; pair medians within ~1%; wall =
  per-call median, dev = stream-saturated batched rate):

| shape | off wall/dev (us) | on wall/dev (us) | wall x | dev-rate x |
|---|---|---|---|---|
| helios fp32 [8640,5120] | 111.29 / 90.96 | 100.18 / 89.30 | 1.111 | 1.019 |
| hunyuan bf16 [648720,128] | 108.81 / 81.87 | 95.44 / 81.13 | 1.140 | 1.009 |
| hunyuan bf16 [1320,128] | 33.31 / 24.63 | 17.74 / 11.39 | 1.878 | 2.163 |
| hunyuan bf16 [650040,128] | 108.73 / 82.17 | 95.70 / 81.36 | 1.136 | 1.010 |
| zimage bf16 [16384,128] | 33.29 / 24.64 | 17.95 / 11.40 | 1.854 | 2.161 |
| zimage bf16 [4096,128] | 32.28 / 24.39 | 17.70 / 11.36 | 1.823 | 2.148 |
| **geomean** | | | **1.4458** | 1.478 |

  Decomposition: the three bandwidth-bound shapes are device-parity-plus at
  the HBM bound (NCU: identical 77.66us single-launch on [648720,128], 82.67%
  vs 82.17% DRAM — `profile/ncu_tilev1/REPORT.md`); their wall delta and the
  small-shape ~1.8-1.9x are host-side launcher wins (Triton runtime launch →
  cached tvm-ffi call) under the byte-identical public op + registration —
  admissible per the standing decomposition ruling, reported with the
  device/host split in `benchmark.csv` (`mode=intree_arbiter*`).
- **Oracle**: `python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py`
  inside the patched worktree: **288/288 with native ON** (and 288/288 with
  OFF — the toggled-off path is upstream-identical).
- **Fallback probes** (native ON): fp16 RMS and non-contiguous bf16 RMS —
  guard evaluates False AND public output equals the torch fp32 reference;
  `is_rms_norm=True` on `norm_infer` bypasses the LN fast path and matches the
  reference.
- **torch.compile smoke**: `torch.ops.sglang.triton_one_pass_rms_norm_cuda`
  present; compiled callable == eager bitwise on bf16 [4096,128].
- Raw artifacts: `arbiter_{off,on}_{1,2}.json` under
  `REMOTE_KDA_DIR=/home/sglang-omni/bbuf/kda_runs/h200_diffusion_norm_infer__multi_shape/r20260604-rlcr184616`.

## kda_kernels overlay export (secondary distribution channel, refreshed)

- `python3 scripts/export_kda_kernels/export.py h200_diffusion_norm_infer__multi_shape`
  regenerated `kda_kernels/diffusion/norm_infer/_impls/h200/` from `src/`
  (now shipping `rms_norm_d128_tile16.cuh`; the prior `rms_norm_d128.cuh`
  warp kernel is retained unrouted for reference). `EXPORTS` in
  `src/register.py` stays bare-exec-safe; `src/wrapper.py` keeps the
  relative-first import.
- Strict validation on ion8-h200 GPU 0 (`validate_install.py`, overlay
  install path): both symbols swapped; all six perf shapes pass the strict
  contract (shape/dtype/NaN/Inf + vs-baseline AND vs-fp32-reference);
  fallback cases exact; select01 oracle OK; smoke 4096x128 2.00x,
  648720x128 1.14x; **VALIDATE_OK exit 0**.
- Stamped metadata: `KDA_EXPORTS.json` / `KDA_STATUS.md` report the arbiter
  geomean `1.4458x`. Commit lineage convention (unchanged from prior rounds):
  the `commit` stamp is the **export-source commit** — kernel-pilot git HEAD
  when the export tool ran; the continuation sources land in the SUCCESSOR
  commit, so the stamp marks the generation point (kernel files are the
  byte-anchor), and `git show <commit>` is not expected to reproduce the
  package tree.

## Reproduction

```bash
# arbiter (inside sglang_bbuf on ion8/ion9-h200; worktree first on PYTHONPATH)
PYTHONPATH=$REMOTE_KDA_DIR/sglang_arbiter/python REMOTE_GPU_ID=0 CUDA_VISIBLE_DEVICES=0 \
  python3 bench_intree_arbiter.py --toggle off --iters 200 --json off.json
PYTHONPATH=$REMOTE_KDA_DIR/sglang_arbiter/python REMOTE_GPU_ID=0 CUDA_VISIBLE_DEVICES=0 \
  python3 bench_intree_arbiter.py --toggle on --iters 200 --probes --json on.json

# overlay validation (repo root on PYTHONPATH)
PYTHONPATH=<repo-root> REMOTE_GPU_ID=0 CUDA_VISIBLE_DEVICES=0 \
  python3 kernels/h200_diffusion_norm_infer__multi_shape/validate_install.py
```
