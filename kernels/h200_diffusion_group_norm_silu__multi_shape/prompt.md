# h200_diffusion_group_norm_silu__multi_shape

Target GPU: NVIDIA H200.

Target SGLang diffusion entry points to copy as local baseline:

- `sglang.jit_kernel.diffusion.triton.group_norm_silu:triton_group_norm_silu`
- `sglang.jit_kernel.diffusion.group_norm_silu:apply_group_norm_silu`

Goal: optimize fused GroupNorm + SiLU diffusion VAE kernels for the production
diffusion shape set on H200.

Before writing an optimized kernel, read and follow:

- `../../docs/standalone_diffusion_benchmark.md`
- `../../docs/diffusion_kernel_rules.md`
- `../../docs/diffusion_correctness_contract.md`

Also read `../../docs/diffusion_benchmark_shape_coverage.md`. This task is not
ready for optimization until `bench/workloads.json` covers every retained live
shape row for this task family and target arch, and every current benchmark
preset missing from the retained rows has either a fresh capture row or a live
no-call note in `docs/benchmark_preset_audit.md`.

Required first milestone:

1. Copy the relevant upstream SGLang source files for these entry points into
   `baseline/`.
2. Record upstream URL, commit, and copied files in `docs/baseline_source.md`.
3. Expose the copied baseline through local low-overhead ABI entry points.
4. Expose the candidate through the exact same ABI in `solution/`.
5. Create `bench/workloads.json`, copy the standard template to
   `bench/benchmark.py`, implement `bench/adapter.py`, and create
   `bench/correctness.py`.

Do not import, patch, or monkey-patch SGLang during correctness or benchmark
runs. All benchmark code must call only files in this task directory.
