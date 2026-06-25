# Baseline Source Provenance

## Upstream Resolution

| Field | Value |
|-------|-------|
| Repository URL | `https://github.com/sgl-project/sglang` |
| Branch | `main` |
| Resolved commit SHA | `67b2a9ed0cfba8ec625d3f26548e502646fd914d` |
| Resolution method | `git ls-remote --heads https://github.com/sgl-project/sglang.git main` |
| Resolved at (UTC) | `2026-06-25T01:36:04Z` |
| Target GPU | NVIDIA B200 (sm_100) |
| Task slug | `b200_diffusion_attention_concat_copy__multi_model` |

The latest `main` commit was resolved fresh at baseline-recovery time (not a stale pinned commit, not the local production checkout, not copied from a prior KDA task). The source file content was fetched read-only at that exact SHA via GitHub raw; no SGLang checkout was modified in place.

## Copied Files

| Local path | Upstream path @ `67b2a9ed` | What it is | sha256 |
|------------|----------------------------|------------|--------|
| `baseline/sglang_uspattention_excerpt.py.txt` | `python/sglang/multimodal_gen/runtime/layers/attention/layer.py` (lines 809–990) | Verbatim excerpt of the `USPAttention` replicated-prefix / replicated-kv-prefix / replicated-suffix methods — the exact attention prefix head-slice + `.contiguous()` + `torch.cat(dim=1)` memory-movement pattern this task models | `e87694fddcf3d26ac7ea368ee829624be9db42820b06e82c2f2a87a29c133dcf` (excerpt, incl. header) |

Full-file checksum (the upstream `layer.py` blob @ `67b2a9ed`, before excerpting): `094bd4ccc9171a61230f9ed10a4e2a23a4dd0dd91b6917a068cc25e8f0d4665b` (990 lines).

### Memory-movement pattern recovered (the part this task optimizes)

From `USPAttention._forward_with_replicated_prefix` (q/k/v each):
```python
h_local = q_shard.shape[2]          # = H_full // sp_size
h_start = sp_rank * h_local
h_end   = h_start + h_local
q_rep = q_rep[:, :, h_start:h_end, :].contiguous()   # slice heads (dim=2) -> contiguous copy
q     = torch.cat([q_rep, q_shard], dim=1)           # concat on sequence dim (dim=1)
```
`_forward_with_replicated_kv_prefix_split` performs the same for K and V only.
`_forward_with_replicated_suffix` rotates the replicated suffix to the front, reuses the prefix path, then returns `torch.cat([out_shard, out_rep], dim=1)` — i.e. the **`[shard, prefix]`** materialization order (suffix models, e.g. JoyAI), versus the **`[prefix, shard]`** order of prefix models (e.g. FLUX.2).

Tensors are `[B, S, H, D]`, bf16. The three standalone workload types modeled from this pattern:
- `copy_contiguous` — the `.contiguous()` materialization of a non-contiguous (head-sliced) view.
- `concat_sequence` — `torch.cat([a, b], dim=1)` of two equal-head tensors on the sequence dim.
- `slice_heads_then_concat_sequence` — fused `cat(prefix[:, :, h_start:h_end, :].contiguous(), shard, dim=1)`.

## Local Files (not copied from upstream)
- `baseline/binding.py` — task-local destination-passing ABI adapter that reproduces the PyTorch memory-movement behavior (`.contiguous()` / `torch.cat(dim=1)` / copy) for the three workload types. Written for this task; see "Why the baseline stays Python (ATen)" below.
- `solution/` — the optimized candidate CUDA kernel and its loader.
- `bench/` — frozen workloads, correctness oracle, benchmark adapter, and the standard timing harness.

## Local Edit Log (complete)
1. `baseline/sglang_uspattention_excerpt.py.txt`: prepended a non-behavioral provenance header comment block (source URL/commit/path/lines/checksums/resolution time). The method bodies (lines 809–990) are otherwise verbatim from the upstream blob. No code lines were altered.

## Why The Baseline Stays Python (ATen)

The upstream USPAttention memory movement is **PyTorch/ATen** (`.contiguous()` + `torch.cat`), not a hand-written CUDA kernel. Per `standalone_diffusion_benchmark.md` ("If the copied SGLang implementation is Triton, CuTe DSL, or Python, keep it local and build a local baseline adapter with the same benchmark ABI used by the candidate") and the established sibling-task convention (`b200_diffusion_fuse_scale_shift__multi_shape`, `b200_diffusion_group_norm_silu__multi_shape`), the runnable baseline is a Python `baseline/binding.py` that calls the upstream ops directly. This makes the headline-speedup baseline the **actual profiled cost** (ATen `CatArrayBatchedCopy` / copy kernels), not a strawman naive CUDA transcription.

`config.toml` declares `baseline_entry_point = "baseline/kernel.cu::attention_concat_copy_baseline"` as the CUDA-baseline template default. For this PyTorch-source task that placeholder is **overridden**: the baseline entry point is `baseline/binding.py::attention_concat_copy_baseline`. Both baseline and candidate are driven through the same `bench/adapter.py` `call_baseline`/`call_candidate` with matched wrapper overhead, and timed with CUDA events over the GPU op region only. This override is also documented in `docs/benchmark_method.md`.
