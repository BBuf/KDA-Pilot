# b200_diffusion_residual_gate_add__multi_shape

Target GPU: NVIDIA B200.

Target SGLang diffusion source patterns to copy as local baseline:

- `sglang.multimodal_gen.runtime.models.dits.ltx_2:LTX2TransformerBlock.forward`
- `sglang.multimodal_gen.runtime.models.dits.ideogram:Ideogram4TransformerBlock.forward`
- FLUX.2 modulation and residual gate patterns in
  `sglang.multimodal_gen.runtime.models.dits.flux_2`

Goal: optimize memory-bound residual gate updates and small broadcast adds that
show up repeatedly in recent diffusion DiT blocks on B200.

This is a standalone CUDA task. It should not try to replace GEMM, attention,
RMSNorm, QKNorm+RoPE, or the existing CuTe DSL norm/scale/shift kernels.

Before writing an optimized kernel, read and follow:

- `../../docs/standalone_diffusion_benchmark.md`
- `../../docs/diffusion_kernel_rules.md`
- `../../docs/diffusion_correctness_contract.md`
- `../../docs/sglang_recent_diffusion_b200_profile_audit_2026-06-24.md`

Profile evidence:

- LTX-2.3 HQ two-stage, 1920x1088, 121 frames:
  - CUDA trace aggregate had elementwise add at 7260.2 ms and mul at
    4022.4 ms.
  - `aten::add` `[1,8160,4096] + [1,8160,4096]`: 27,927 calls,
    228.5 ms CPU op time.
  - `aten::mul` `[1,8160,4096] * [1,8160,4096]`: 25,143 calls,
    239.1 ms CPU op time.
  - `aten::add` `[1,32640,4096] + [1,32640,4096]`: 4332 calls,
    296.1 ms CPU op time.
  - `aten::add` `[1,126,2048] + [1,126,2048]`: 33,123 calls,
    691.4 ms CPU op time.
  - `aten::mul` `[1,126,2048] * [1,126,2048]`: 26,877 calls,
    226.3 ms CPU op time.
  - Broadcast add `[1,1,3,2048] + [1,126,3,2048]`: 13,392 calls,
    3139.4 ms CPU op time.
- Ideogram4 FP8, 1024x1024:
  - `aten::mul` `[1,1,4608] * [1,4096,4608]`: 1360 calls,
    150.7 ms CPU op time.
  - Source has `x = x + gate * norm(...)` around both attention and MLP.
- FLUX.2 Klein Base, 1024x1024:
  - `aten::mul` `[1,1,3072] * [1,4608,3072]`: 4000 calls,
    33.7 ms CPU op time.
  - `aten::add` `[1,4608,3072] + [1,4608,3072]`: 2000 calls,
    19.9 ms CPU op time.
  - Prefix and image split rows also occur at sequence lengths 512 and 4096.

Trace paths:

- `/tmp/sglang_profile_b200/outputs/diffusion_profiles/ltx23-hq-two-stage_nocompile_all/70769941-6405-49c2-8663-a632325a001b-full_stages-global-rank0.trace.json.gz`
- `/tmp/sglang_profile_b200/outputs/diffusion_profiles/ideogram4-fp8_nocompile_all/bf5ca92b-9bc5-41a8-bf2a-8f2db371b9d4-full_stages-global-rank0.trace.json.gz`
- `/tmp/sglang_profile_b200/outputs/diffusion_profiles/flux2-klein-base_nocompile_all/df2cd86f-354e-4576-a41a-6d428f974685-full_stages-global-rank0.trace.json.gz`

Required production workload rows:

- `residual_gate_add`: bf16 `residual=[1,8160,4096]`,
  `update=[1,8160,4096]`, `gate=[1,8160,4096]`
- `residual_gate_add`: bf16 `residual=[1,32640,4096]`,
  `update=[1,32640,4096]`, `gate=[1,1,4096]`
- `residual_gate_add`: bf16 `residual=[1,126,2048]`,
  `update=[1,126,2048]`, `gate=[1,126,2048]`
- `residual_gate_add`: bf16 `residual=[1,4096,4608]`,
  `update=[1,4096,4608]`, `gate=[1,1,4608]`
- `residual_gate_add`: bf16 `residual=[1,4608,3072]`,
  `update=[1,4608,3072]`, `gate=[1,1,3072]`
- `residual_gate_add`: bf16 `residual=[1,4096,3072]`,
  `update=[1,4096,3072]`, `gate=[1,1,3072]`
- `residual_gate_add`: bf16 `residual=[1,512,3072]`,
  `update=[1,512,3072]`, `gate=[1,1,3072]`
- `broadcast_add_4d`: bf16 `a=[1,1,3,2048]`, `b=[1,126,3,2048]`,
  output `[1,126,3,2048]`

Expected optimization direction:

- Implement `out = residual + update * gate` in one pass, with support for
  full-shape gate and `[B,1,D]` broadcast gate.
- Implement the LTX broadcast-add row separately if it needs a different
  dispatch path; do not force it into the residual-gate kernel if that hurts
  the main rows.
- Use vectorized loads/stores and enough CTAs per row bucket to approach B200
  memory bandwidth. This task is expected to be bandwidth-bound.
- Keep numerics equivalent to PyTorch bf16 elementwise behavior within the
  correctness contract tolerance.

Required first milestone:

1. Copy the relevant upstream SGLang source snippets into `baseline/` and
   record the exact source commit in `docs/baseline_source.md`.
2. Implement local baseline adapters that reproduce PyTorch
   `residual + update * gate` and broadcast-add behavior for the workload rows.
3. Expose the candidate through the exact same ABI in `solution/`.
4. Create `bench/workloads.json`, copy the standard template to
   `bench/benchmark.py`, implement `bench/adapter.py`, and create
   `bench/correctness.py`.

Do not import, patch, or monkey-patch SGLang during correctness or benchmark
runs. All benchmark code must call only files in this task directory.
