# Profile evidence: GDN chunk prefill (Qwen3-Next-80B-A3B)

| op | real calls | distinct signatures | rows kept |
| --- | ---: | ---: | ---: |
| `gdn_recompute_w_u` | 3744 | 13 | 11 |
| `gdn_chunk_delta_h` | 3744 | 13 | 11 |
| `gdn_chunk_o` | 3744 | 13 | 11 |
| `gdn_chunk_prefill` | 3744 | 13 | 11 |

Representative shapes:

- `gdn_recompute_w_u`: k[1, 103, 2, 128]:bfloat16, v[1, 103, 4, 128]:bfloat16, beta[1, 103, 4]:float32, g_cumsum[1, 103, 4]:float32, A[1, 103, 4, 64]:bfloat16, cu_seqlens[2]:int32, chunk_indices[2, 2]:int32
- `gdn_chunk_delta_h`: k[1, 103, 2, 128]:bfloat16, w[1, 103, 4, 128]:bfloat16, u[1, 103, 4, 128]:bfloat16, g[1, 103, 4]:float32, initial_state[10715, 4, 128, 128]:float32, initial_state_indices[1]:int32, cu_seqlens[2]:int32, chunk_indices[2, 2]:int32
- `gdn_chunk_o`: q[1, 103, 2, 128]:bfloat16, k[1, 103, 2, 128]:bfloat16, v[1, 103, 4, 128]:bfloat16, h[1, 2, 4, 128, 128]:bfloat16, g[1, 103, 4]:float32, cu_seqlens[2]:int32
- `gdn_chunk_prefill`: q[1, 103, 2, 128]:bfloat16, k[1, 103, 2, 128]:bfloat16, v[1, 103, 4, 128]:bfloat16, g[1, 103, 4]:float32, beta[1, 103, 4]:float32, initial_state[10715, 4, 128, 128]:float32, initial_state_indices[1]:int32, cu_seqlens[2]:int32, chunk_indices[2, 2]:int32

Read `capture_provenance.md` for the two findings that shape this task: the FLA
Triton chunk path is live on B300 while the FLA *recurrent decode* path is not, and
the synthetic-output groups were replaced by real GSM8K groups on this model.

## The decode kernel is Triton, and its state chain is verified

Measured tonight on the same box, with CUDA graphs **enabled** (the real deployment),
TP8, random 1024-in / 256-out at concurrency 16. Full table in
`../docs/profiles/kernel_shapes_qwen3_next.json`, 99.7% of GPU time accounted for:

| block | share | biggest single kernel |
| --- | ---: | --- |
| MoE (trtllm bmm / routing / finalize) | 30.79% | 8.44% |
| GEMM (nvjet / cublas) | 26.12% | 6.11% |
| collectives | 18.67% | 11.89% |
| full attention (Triton unified) | 6.39% | `_fwd_grouped_kernel_stage1` 3.43% |
| **GDN linear attention** | **4.39%** | **`fused_recurrent_gated_delta_rule_packed_decode_kernel` 3.56%** |
| causal conv1d | 1.67% | `_causal_conv1d_update_kernel` |
| elementwise / norm / act | 6.06% | `act_and_mul` 2.15% |

So the live GDN target on B300 is `TritonGDNKernel.packed_decode` at **3.56% of GPU
time** - a Triton kernel, above our 3% bar on its own. Decode is **not** served by the CuteDSL or
FlashInfer GDN kernels on this build - we wrapped all three and only the Triton one
fired.

The chunk-prefill kernels are small *at this operating point* (0.33% + 0.14% + 0.14%)
because the input is 1k tokens. They scale with prompt length, and the captured rows
include the real long-prompt shapes (T up to 16,289 from the 16-shot GSM8K groups), so
tune against those rows rather than against this profile's share.

### Verified decode state chains (the correctness oracle)

`bench/tensors/` ships two chains of 16 consecutive real decode steps, both **15/15
links byte-identical** (`tools/verify_state_chain.py`):

* `gdn_decode_packed_triton__mixed_qkv1x1024` - the GDN SSM state (`ssm_states` rows,
  sliced by `cache_indices`), 8.8 MB.
* `gdn_decode_causal_conv1d_update__x1x1024` - the conv state, 836 KB.

Prefill payloads (`bench/tensors_prefill/`) cover the chunk pipeline at T = 3,407 and
16,289 with the fp32 `initial_state` pool rows.

Chain capture needed two things to be right, both of which matter if you re-capture:
`--disable-radix-cache` (the mamba pool's `extra_buffer` strategy rewrites rows outside
the kernel call otherwise) and pinning the chain to one layer instance via its `A_log`
pointer - consecutive same-shape calls are different layers, not consecutive time steps.

## The share depends on the operating point - four of them, measured

One number was not enough here, so we profiled four points on the same server (TP8,
CUDA graphs on, B300). Raw tables: `../docs/profiles/qwen3_next_points/`.

| operating point | GDN family | of which `packed_decode` | chunk-prefill kernels | full attention (Triton) |
| --- | ---: | ---: | ---: | ---: |
| 8k in / 64 out, cc 8 | **5.34%** | 2.41% | **2.51%** | 24.60% |
| 32k in / 64 out, cc 4 | 2.76% | 2.04% | 0.52% | **50.78%** |
| 1k in / 256 out, cc 16 | 4.20% | 3.41% | 0.58% | 6.11% |
| 1k in / 1k out, cc 32 | 4.01% | 3.61% | 0.32% | 7.64% |

Reading it:

* **The GDN decode kernel is steady at 2.0-3.6%** of GPU time no matter the shape of the
  workload. That is the floor to expect from optimizing it, and it is a Triton kernel, so
  the floor is reachable.
* **The chunk-prefill kernels peak at 2.51% around 8k input** and fall off on both sides:
  at 1k there is barely any prefill to do, and at 32k the *full-attention* layers take
  over the profile so everything else shrinks in relative terms.
* **The real story at long context is the other kernel family**: Qwen3-Next is a hybrid,
  and its 1-in-4 full-attention layers run on the Triton unified backend -
  `_fwd_grouped_kernel_stage1` alone is **35.9%** of GPU time at 32k input, and the family
  is **50.8%**. That is the same kernel as `glm47_flash__triton_attention`, whose task
  already ships a Qwen3-Next shape family (`bench/workloads_qwen3_next_secondary.json`
  there). If you only have budget for one Qwen3-Next kernel, that is the one.

Why the absolute numbers are modest for an 80B model: at TP8 the linear-attention state is
split 8 ways (2 K/V heads and 4 V heads per rank), while MoE (21-31%), GEMM (20-26%) and
collectives (16-19%) are what the GPU spends its time on. A linear-attention kernel being
a few percent is the architecture working as intended, not the kernel being unimportant -
it is per-token work that never grows with context.


> Carved out of `qwen3_next__gdn_chunk_prefill` by `tools/split_task_op.py`: this task is the single op
> `gdn_decode_packed_triton`. The capture run, the operating points and the environment above are the
> ones that package recorded - the same serving run, narrowed to one kernel.
