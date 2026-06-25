# b200_diffusion_attention_concat_copy__multi_model

Target GPU: NVIDIA B200.

Target SGLang diffusion source patterns to copy as local baseline:

- `sglang.multimodal_gen.runtime.layers.attention.layer:USPAttention._forward_with_replicated_prefix`
- `sglang.multimodal_gen.runtime.layers.attention.layer:USPAttention._forward_with_replicated_kv_prefix_split`
- The local `contiguous()` plus `torch.cat(..., dim=1)` attention layout
  patterns in the same file.

Goal: replace repeated attention-prefix slice, contiguous-copy, and sequence
concat materialization with standalone CUDA kernels for real recent diffusion
model shapes on B200.

Before writing an optimized kernel, read and follow:

- `../../docs/standalone_diffusion_benchmark.md`
- `../../docs/diffusion_kernel_rules.md`
- `../../docs/diffusion_correctness_contract.md`
- `../../docs/sglang_recent_diffusion_b200_profile_audit_2026-06-24.md`

Profile evidence:

- JoyAI Image Edit, 1024x1024, 40 steps, 2-GPU CFG parallel:
  - `aten::contiguous` on `[1,8048,32,128]`: 3200 calls, 748.6 ms CPU op time
  - `aten::copy_` on `[1,8048,32,128]`: 3200 calls, 705.1 ms CPU op time
  - `aten::contiguous` on `[1,1004,32,128]`: 3200 calls, 78.7 ms CPU op time
  - `aten::cat` for `[[1,8048,32,128], [1,1004,32,128]]`: 4800 calls,
    71.6 ms CPU op time
  - CUDA trace showed `CatArrayBatchedCopy` at 521.5 ms
- FLUX.2 Klein Base, 1024x1024, 50 steps:
  - `aten::copy_` on `[1,4608,24,128]`: 4000 calls, 154.9 ms CPU op time
  - `aten::cat` for `[[1,512,24,128], [1,4096,24,128]]`: 1500 calls,
    51.2 ms CPU op time
- Trace paths:
  - `/tmp/sglang_profile_b200/outputs/diffusion_profiles/joyai-edit_nocompile_all/f2159a93-363e-4c7c-8bd4-4a93017b3985-full_stages-global-rank0.trace.json.gz`
  - `/tmp/sglang_profile_b200/outputs/diffusion_profiles/flux2-klein-base_nocompile_all/df2cd86f-354e-4576-a41a-6d428f974685-full_stages-global-rank0.trace.json.gz`

Required production workload rows:

- `concat_sequence`: bf16 `a=[1,512,24,128]`, `b=[1,4096,24,128]`,
  output `[1,4608,24,128]`
- `concat_sequence`: bf16 `a=[1,8048,32,128]`, `b=[1,1004,32,128]`,
  output `[1,9052,32,128]`
- `copy_contiguous`: bf16 `[1,4608,24,128]`
- `copy_contiguous`: bf16 `[1,8048,32,128]`
- `copy_contiguous`: bf16 `[1,1004,32,128]`
- `slice_heads_then_concat_sequence`: bf16 prefix plus shard inputs matching
  the replicated-prefix source pattern. Include FLUX.2 prefix length 512,
  shard length 4096, heads 24, head dim 128; include JoyAI lengths 1004 and
  8048, heads 32, head dim 128.

The benchmark should preserve workload type labels so the result can tell
whether the win comes from plain concat, plain copy, or fused slice+concat.

Expected optimization direction:

- Do not reimplement FlashAttention or collective communication.
- Keep this task scoped to local memory movement immediately around attention:
  head slicing, contiguous copies, and sequence-dim concatenation.
- A useful candidate should fuse source head slicing and concatenation when the
  source pattern would otherwise materialize a contiguous prefix before
  `torch.cat`.
- For pure concat/copy rows, use vectorized loads/stores and split large rows
  into enough CTAs to saturate B200 memory bandwidth.
- Validate both source orders used by profiles: `[prefix, shard]` and
  `[shard, prefix]`.

Required first milestone:

1. Copy the relevant upstream SGLang source snippets into `baseline/` and
   record the exact source commit in `docs/baseline_source.md`.
2. Implement local baseline adapters that reproduce PyTorch
   `contiguous()`/`torch.cat` behavior for each workload type.
3. Expose the candidate through the exact same ABI in `solution/`.
4. Create `bench/workloads.json`, copy the standard template to
   `bench/benchmark.py`, implement `bench/adapter.py`, and create
   `bench/correctness.py`.

Do not import, patch, or monkey-patch SGLang during correctness or benchmark
runs. All benchmark code must call only files in this task directory.
