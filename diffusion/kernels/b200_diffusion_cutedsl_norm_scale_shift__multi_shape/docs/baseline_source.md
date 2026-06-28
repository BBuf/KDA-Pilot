# Baseline Source Lineage

## Upstream

- Project: SGLang — https://github.com/sgl-project/sglang
- Pinned baseline commit: `edb1b3f8f5ab066af1e9b6ee8e8738fadcfa77e7`
  (`[NPU] add Ascend NPU Accuracy Evaluation and Faq docs (#24777)`)
- Provenance: this is the commit of the SGLang tree that `import sglang`
  resolves to inside the `sglang_bbuf` container on `ion-b200`
  (`/sgl-workspace/sglang`, editable install, pip version
  `0.0.0.dev1+gedb1b3f8f`, working tree clean at recovery time). This is the
  same environment that produced `docs/captured_shapes_b200.jsonl`.
- Distractor noted: `/home/sglang-omni/bbuf/repos/sglang` in the same container
  is a different checkout (`0b65588c1`, dirty working tree). It is NOT the
  import source and is not used as the baseline.

## Recovery environment

- Host: `ion-b200`, container: `sglang_bbuf`
- GPU for this task: `REMOTE_GPU_ID=0`, NVIDIA B200,
  uuid `GPU-a4d97fda-2684-94c9-4291-c6b291c0eb33` (idle at selection: 0% util,
  0 MiB used; GPUs 4-7 were busy with an unrelated sglang serving job)
- Stack: torch `2.11.0+cu130`, CUDA `13.0`, `nvidia-cutlass-dsl` (CuTe DSL)
  `4.5.0`, ncu present at `/usr/local/cuda/bin/ncu`
- Remote task workspace: `REMOTE_KDA_DIR=/home/sglang-omni/bbuf/kda_runs/b200_diffusion_cutedsl_norm_scale_shift__multi_shape/2026-06-04_15-19-43`
  (subdirs: `logs/ parity/ bench/ build/`; created from inside the container —
  host-level writes to `/home/sglang-omni/bbuf` are permission-denied for the
  ssh user)
- Recovery date: 2026-06-04

## Copied files

- `baseline/upstream_jit_kernel/jit_kernel/**` — snapshot of
  `/sgl-workspace/sglang/python/sglang/jit_kernel` at the pinned commit,
  fetched verbatim via `docker exec ... tar | tar -x` (272 files,
  `__pycache__` excluded) and later **pruned to a 17-file functional
  subtree** before the PR, per the task's PR-content rule ("only
  kernel-related code, harnesses, small provenance notes, per-shape
  results"). Every retained file is byte-identical to the verbatim fetch
  (key module sha256 below unchanged); the pruned set is exactly what the
  harness needs: the baseline module + its CuTe-DSL helpers
  (`diffusion/cutedsl/**`), the jit_kernel build stack (`utils.py`), the
  core `include/sgl_kernel/` headers our candidate compiles against, the
  upstream oracle test, the (empty) package `__init__.py`, and
  `csrc/diffusion/qknorm_rope.cuh` — kept both as the documented host-API
  pattern source AND because `utils.py::_resolve_kernel_path` requires a
  `csrc/` directory beside `include/` to resolve the package root. Dropped:
  unrelated kernels/csrc/benchmarks and the self-contained
  `include/sgl_kernel/{deepseek_v4,distributed}` plus six headers
  referenced by nothing retained (`tile/cta/atomic/impl-norm/scalar_type/
  ffi`). The one-time parity run (below) was executed against the full
  verbatim snapshot; pruning removes only files that run never imported,
  and the full correctness suite was re-run against the pruned tree with a
  cleared JIT cache to prove the retained include set builds.
- Key files for this task within the snapshot:
  - `jit_kernel/diffusion/cutedsl/scale_residual_norm_scale_shift.py`
    (sha256 `d6818e5da8d3c5ace3950313e996a22b4c051edc29ab7026eb8cb9d79e414df9`)
    — the two wrapped entry points + validators + CuTe-DSL kernel class.
  - `jit_kernel/diffusion/cutedsl/common/norm_fusion.py` — `apply_norm_cta`
    (fp32 accumulation; two-pass layer variance), `broadcast_tensor_for_bsfd`,
    `tensor_slice_for_bsfd` (runtime frame indexing).
  - `jit_kernel/diffusion/cutedsl/common/reduce.py` — warp shuffle-tree +
    smem CTA reductions.
  - `jit_kernel/diffusion/cutedsl/utils.py` — `TORCH_TO_CUTE_DTYPE`, `WARP_SIZE`.
  - `jit_kernel/tests/diffusion/test_fused_norm_scale_shift.py` — correctness
    oracle; pinned-commit grid: `SHAPES = [(1,115200,1,3072), (1,32760,1,1536),
    (1,6,1,3072), (1,1024,8,3072), (4,512,16,3072)]` (supersedes the draft's
    two-shape summary), dtypes fp16/bf16/fp32, norm layer/rms, affine D/NAT,
    index modes BSD/1/1SD/BD/B1D/D/1D/11D/BF1D, tol 1e-5 (fp32) / 5e-2 (else),
    eps 1e-5.
  - `jit_kernel/utils.py` — `load_jit` / `make_cpp_args` / `cache_once`,
    default flags `-std=c++20 -O3 --expt-relaxed-constexpr` + arch flag
    (no `--use_fast_math`), `is_arch_support_pdl`.
  - `jit_kernel/csrc/diffusion/qknorm_rope.cuh` + `jit_kernel/include/sgl_kernel/`
    (`tensor.h`, `runtime.cuh`, `type.cuh`, `utils.cuh`, `vec.cuh`, `warp.cuh`)
    — the tvm-ffi host/launch pattern the native candidate mirrors.

## Local edits

- None inside the snapshot (verbatim copy). Runtime shims live OUTSIDE the
  snapshot: `baseline/loader.py` (sys.modules alias + snapshot-only guard) and
  `baseline/entry.py` (local entry ABI resolving to the snapshot's custom-op
  wrappers). See `baseline/README.md`.

## Parity evidence (copy vs real SGLang op)

- Command: `bench/remote_parity.sh` (three separate processes:
  `bench/parity_check.py --side real`, `--side copy`, `--compare`).
- Result: **PARITY PASS — 39/39 unique captured signatures bitwise-identical**
  (`torch.equal`) between the real `sglang` public ops
  (`/sgl-workspace/sglang`, commit `edb1b3f8f5`) and the `baseline/` snapshot
  alias, on `ion-b200` / `sglang_bbuf` / `CUDA_VISIBLE_DEVICES=0` (B200,
  idle before and after; GPUs 4-7 carried an unrelated job throughout).
- Logs: `REMOTE_KDA_DIR/logs/parity_{real,copy,compare}.log`,
  `REMOTE_KDA_DIR/logs/parity_gpu_{before,after}.txt`; outputs under
  `REMOTE_KDA_DIR/parity/{real,copy}/`.
- Run date: 2026-06-04.
