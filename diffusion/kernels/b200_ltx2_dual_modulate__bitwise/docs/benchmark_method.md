# Benchmark Method

Status: validated on B200 (full-op TVM-FFI CUDA ABI for both baseline and
candidate). Per-shape numbers and provenance are in `docs/results.md`.

## Harness
- `bench/benchmark.py` is copied verbatim from
  `../../docs/standalone_diffusion_benchmark_template.py` (do not fork the timing
  policy). Task-specific tensor construction and the two ABI calls live in
  `bench/adapter.py`.
- Correctness gate uses `torch.equal` (zero tolerance) via an adapter-level
  `compare_outputs`, overriding the template's default allclose comparator.

## Compile flags (must be symmetric on baseline and candidate)
- Host: `-std=c++17 -O3`
- Device: `-std=c++17 -O3 -gencode=arch=compute_100,code=sm_100` (gencode
  auto-derived from `torch.cuda.get_device_capability()` at build time)
- Link: torch library paths + `-lc10 -lc10_cuda -ltorch_cpu -ltorch_cuda` + rpath
- **No `--use_fast_math`** (upstream does not use it; both sides must match)
- Build path: `tvm_ffi.cpp.load` into `<side>/.build/` (gitignored)

## Numerics policy (bitwise)
- Target: bit-for-bit equality with the PyTorch eager baseline
  (`F.rms_norm` + per-op-boundary bf16 affine). See `docs/baseline_source.md`.
- Round at every PyTorch operation boundary; no `fma`/reassociation; no
  single-shot fp32 collapse. For the CA path: fp32 table -> bf16, table+temb ->
  bf16, `1+scale` -> bf16, multiply -> bf16, final add -> bf16.

## Run protocol (remote B200)
- Host `ion-b200`; select an idle B200 via `nvidia-smi`; export `REMOTE_GPU_ID`
  and reuse it (via `CUDA_VISIBLE_DEVICES`) for build, correctness, benchmark,
  profiler, and NCU. Record before/after idle state and toolchain versions.

## Versions (recorded from the validation run)
- torch `2.11.0+cu130`, CUDA runtime `13.0`, nvcc `13.0.88`, tvm-ffi `0.1.9`,
  Python `3.12.3`.
- Host `innomatrix-us-adc-smb200-0003`, container `sglang_bbuf_pr29315`,
  GPU NVIDIA B200 (`REMOTE_GPU_ID=5`).
- See `docs/results.md` for per-shape numbers and the headline geomean speedup
  (8/8 bitwise); that file is the single source of truth for the measured numbers.
