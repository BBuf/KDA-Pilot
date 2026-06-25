# b200_diffusion_causal_conv3d_cat_pad__multi_shape

Target GPU: NVIDIA B200.

Target SGLang diffusion entry point to copy as local baseline:

- `sglang.jit_kernel.diffusion.triton.causal_conv3d_pad:fused_causal_conv3d_cat_pad`

Goal: optimize the fused 5D causal Conv3D cat/pad copy path for recent video
diffusion VAE workloads on B200.

Before writing an optimized kernel, read and follow:

- `../../docs/standalone_diffusion_benchmark.md`
- `../../docs/diffusion_kernel_rules.md`
- `../../docs/diffusion_correctness_contract.md`
- `../../docs/sglang_recent_diffusion_b200_profile_audit_2026-06-24.md`

Profile evidence:

- Model: `nvidia/Cosmos3-Nano`, preset `cosmos3-nano-t2v`
- Benchmark: 832x480, 9 frames, 4 denoise steps
- Clean no-compile latency: denoise 169.55 ms, end-to-end 216.8 ms
- All-stage trace: `_fused_cat_pad_5d_kernel` took 11.94 ms
- Trace path:
  `/tmp/sglang_profile_b200/outputs/diffusion_profiles/cosmos3-nano-t2v_nocompile_all/bfc39a58-f657-4c3c-86a4-728c58484da6-full_stages-global-rank0.trace.json.gz`
- Shape capture:
  `/tmp/sglang_profile_b200/outputs/shape_captures/cosmos3-nano-t2v_no_compile_v2.jsonl`

Required production workload rows:

- bf16 contiguous: `x=[1,1024,1,30,52]`, `cache=[1,1024,1,30,52]`,
  padding `[1,1,1,1,2,0]`
- bf16 contiguous: `x=[1,1024,1,30,52]`, `cache=[1,1024,2,30,52]`,
  padding `[1,1,1,1,2,0]`
- bf16 contiguous: `x=[1,1024,2,60,104]`, `cache=[1,1024,1,60,104]`,
  padding `[1,1,1,1,2,0]`
- bf16 contiguous: `x=[1,1024,2,60,104]`, `cache=[1,1024,2,60,104]`,
  padding `[1,1,1,1,2,0]`
- bf16 contiguous: `x=[1,512,4,120,208]`, `cache=[1,512,1,120,208]`,
  padding `[1,1,1,1,2,0]`
- bf16 contiguous: `x=[1,512,4,120,208]`, `cache=[1,512,2,120,208]`,
  padding `[1,1,1,1,2,0]`
- bf16 contiguous: `x=[1,256,4,240,416]`, `cache=[1,256,1,240,416]`,
  padding `[1,1,1,1,2,0]`
- bf16 contiguous: `x=[1,256,4,240,416]`, `cache=[1,256,2,240,416]`,
  padding `[1,1,1,1,2,0]`

Also include cache-null rows and no-pad rows from the capture as regression
workloads, but do not let them dominate the score unless they occur frequently.

Expected optimization direction:

- The copied SGLang baseline is a Triton kernel with scalarized index math and
  one element per output location.
- A CUDA candidate should focus on coalesced/vectorized copy for interior
  regions and handle spatial/depth pad borders with a separate slow path or
  predicated tail.
- Preserve the exact semantics for cache-present, cache-null, contiguous, and
  captured non-contiguous rows.

Required first milestone:

1. Copy the upstream SGLang source for this entry point into `baseline/`.
2. Record upstream URL, commit, and copied files in `docs/baseline_source.md`.
3. Expose the copied baseline through a local low-overhead ABI.
4. Expose the candidate through the exact same ABI in `solution/`.
5. Create `bench/workloads.json`, copy the standard template to
   `bench/benchmark.py`, implement `bench/adapter.py`, and create
   `bench/correctness.py`.

Do not import, patch, or monkey-patch SGLang during correctness or benchmark
runs. All benchmark code must call only files in this task directory.
