# TileRT DeepSeek-V3.2 kernel registry (decode + MTP)

Single source of truth for the KDA TileRT kernel tasks. Enumerates **every fused
kernel TileRT runs on the DeepSeek-V3.2 decode + MTP path**, with the authoritative
`(kSeqLen, KeComputeType)` specialization set **read directly from the SASS symbol
table** of the shipped `libtilert_dsv32.so` (`tilert_re/dsv32.kernels.demangled.txt`),
cross-checked against the op source modules in
`tilert_re/tilert/models/deepseek_v3_2/ops/*.py` and `TileRT_讨论材料.md` §3/§13/§16/§20/§22.

## How to read the variant columns

Each TileRT kernel is `…<Name>ExecutorImpl<DefaultSchedule, kPipeStages=4, kSmemBytes,
1, kSeqLen, KeComputeType>`. We parsed the mangled symbols to get, per kernel, the
**exact set of kSeqLen and KeComputeType the .so was AOT-compiled for** — i.e. the
shapes TileRT can actually dispatch at runtime. These are the shapes a KDA task's
`workloads.json` must cover.

- **kSeqLen** ∈ subset of {1,2,3,4,8,16}. Decode = 1; MTP verify = 4 (mtp_seq_len =
  num_mtp+1 = 4); prefill chunks extend to 8/16.
  **Finding (important):** only `FlashSparseMla` / `FlashSparseMlaDSv32DevB` are
  compiled for **kSeqLen=3**; every other kernel is compiled for {1,2,4,(8,16)} and
  **skips 3**. So "cover MTP q_len 1/2/3/4" is satisfied per-op by covering the op's
  *actual* compiled set: {1,2,4} (+3 only where the symbol table has it, +8/16 where
  present). We cover the full compiled set, which is a superset of MTP {1,2,4}.
- **KeComputeType**: 0=none(no MMA, pure mem/comm), 3=bf16 HMMA, 5/6=fp4 HMMA,
  7=fp8, 8=fp4-mma variant. A kernel compiled for multiple CTs runs that many
  precision variants (e.g. FusedMoe has fp4 **and** fp8 paths).

## Audit of the 4 pre-existing draft tasks (PR #50)

| task dir | kernel | status before this pass | gaps fixed |
|---|---|---|---|
| `b200_tilert_head_proj_gemm` | HeadProj | most complete (baseline+adapter+correctness+ref doc), workloads seq{1,2,4} | + seq{3} note, real-op oracle, ≥3× ncu, blog features |
| `b200_tilert_rmsnorm_quant` | RMSNormQuant | baseline+workloads{1,2,4}; no adapter/correctness/oracle/ref | + oracle+correctness, full seq set, ≥3× ncu |
| `b200_tilert_mla_decode` | PureMlaDsv32 | baseline+workloads{1,4}; latency = single profiler avg (35.2µs) | + S2, oracle, ≥3× isolated ncu |
| `b200_tilert_fused_moe` | FusedMoe | baseline+workloads{1}; latency = single profiler avg (22.4µs) | + S2/S4 + fp4/fp8 CT, oracle, ≥3× ncu |

All four are **starting points only** and are re-verified + completed in this pass.

## Full kernel set (DeepSeek-V3.2 decode + MTP critical path)

`std` column: can the op be measured standalone on 1 GPU via its `golden_forward`/
`tilert_forward` oracle (✅), or does `tilert_forward` need multi-GPU NVLink peer/flag
setup so it is only profilable in-graph (▲ comm)?

### 1. Norm / quant (KeComputeType 0/3)

| kernel (ExecutorImpl) | op module / torch.ops | kSeqLen (SASS) | CT (SASS) | smem | role | std |
|---|---|---|---|---|---|---|
| RMSNorm | (rmsnorm) | 1,2,4,8,16 | 3 | 32768 | plain RMSNorm | ✅ |
| RMSNormQuant | rmsnorm_quant_op | 1,2,4,8,16 | 3 | 32768 | RMSNorm + per-128 fp8 act-quant | ✅ |
| RmsnormKv | rmsnorm_kv | 1,2,4,8,16 | 3 | 40960 | RMSNorm of compressed KV latent | ✅ |
| RMSNormExpertProjDsv32 | rmsnorm_expert_proj | 1,2,4 | 0 | 32768 | RMSNorm + router gate proj → scores[256] | ✅ |

### 2. MLA projections + RoPE + KV-cache write (KeComputeType 3/5/6/7)

| kernel | op module | kSeqLen | CT | smem | role | std |
|---|---|---|---|---|---|---|
| ProjXWqkvaDSV32 | projx_wqkva / rmsnorm_projx_wqkva | 1,2,4 | 5(fp4) | 36864 | x→q_a[1536]+kv[512+64] (down-proj) | ✅ |
| RmsnormProjQWqbHMMA | rmsnorm_projq_wqb | 1,2,4 | 6,7 | 36864 | rmsnorm(q_a)+Wq_b→q[20,192] | ✅ |
| RmsnormProjQWqbFP4HMMA | rmsnorm_projq_wqb (fp4) | 1,2,4 | 8 | 16384 | fp4 variant of above | ✅ |
| RmsnormProjQWqiHMMA | rmsnorm_projq_wqi | 1,2,4 | 6,7 | 33792 | GPU0 indexer q_i proj | ✅ |
| ProjQWkvbDevBHMMA | projq_wqb | 1,2,4,8,16 | 6,7 | 17408 | absorbed W_UK (q·kv_b) | ✅ |
| ProjOWkvbDevBHMMA | projo_wkvb | 1,2,4,8,16 | 6,7 | 17408 | absorbed W_UV (o·kv_b) | ✅ |
| ProjXWqaki | projx_wqaki | 1,2,4 | 5 | 40960 | GPU0 x→index query+ki | ✅ |
| ProjXWis | projx_wis | 1,2,4,8,16 | 0,7 | 32768/40960 | indexer weight/scale proj | ✅ |
| QkvRope | qkv_rope | 1,2,4,8,16 | 3 | 40960 | QKV + RoPE | ✅ |
| Rotate | rotate | 1,2,4,8,16 | 3 | 40960 | standalone RoPE rotate | ✅ |
| RotateCompressed | rotate (compressed) | 1 | 3 | 40960 | rotate on compressed form | ✅ |
| **LayernormRopeRotate** | layernorm_rope_rotate | 1,2,4,8,16 | 3 | 40960 | **LayerNorm+RoPE+write k/pe/ki cache (KV WRITE)** | ✅ |

### 3. MLA attention core (reads KV cache)

| kernel | op module | kSeqLen | CT | smem | role | std |
|---|---|---|---|---|---|---|
| **PureMlaDsv32** | flash_sparse_mla (pure) | 1,2,4 | 3 | 36864 | **worker MLA decode, sparse gather top-2048 (52.8%)** | ✅ |
| SparseSelectMlaDsv32 | flash_sparse_mla (select) | 1,2,4 | 3,(4) | 36864 | GPU0 self-MLA over selected KV (7.6%) | ✅ |
| FlashSparseMla | flash_sparse_mla | 1,2,3,4 | 7 | 32768 | flash sparse MLA (prefill/MTP, **has seq=3**) | ✅ |
| FlashSparseMlaDSv32DevB | flash_sparse_mla (DevB) | 1,2,3,4 | 7 | 32768 | DevB variant (**has seq=3**) | ✅ |

### 4. DSA sparse index chain (reads ki cache, KeComputeType 0; tcgen05/TMEM)

| kernel | op module | kSeqLen | CT | smem | role | std |
|---|---|---|---|---|---|---|
| SparseIndex | sparse_index | 1,2,4 | 0 | 40960 | index scoring | ✅ |
| SparseIndexFusedDsv32 | sparse_index (fused) | 1,2,4 | 0 | 40960 | fused index scoring + select | ✅ |
| TopkAccurate | topk | 1,2,4,8,16 | 3 | 32768 | exact top-k | ✅ |
| TopkAccurate512R4 | topk (512/R4) | 1,2,4,8,16 | 3 | 32768 | top-k 512-reduce | ✅ |
| TopkAccurate1024R4 | topk (1024/R4) | 1,2,4,8,16 | 3 | 32768 | top-k 1024-reduce | ✅ |
| TopkAccurateFusedDsv32 | topk (fused) | 1,2,4 | 0 | 40960 | fused top-2048 select | ✅ |
| TopkApproximate | topk (approx) | 1 | 3 | 32768 | approximate top-k | ✅ |
| BroadcastSelectedTokenIds | broadcast_selected_token_ids | 1,2,4,8,16 | 0 | 32768 | GPU0→workers index bcast | ▲ comm |
| ReceiveSelectedTokenIds | receive_selected_token_ids | 1,2,4,8,16 | 0 | 32768 | workers recv indices | ▲ comm |

### 5. MoE / experts (KeComputeType 5/6/7/8 — FP4/FP8)

| kernel | op module | kSeqLen | CT | smem | role | std |
|---|---|---|---|---|---|---|
| **FusedMoe** | (fused moe) | 1,2,4 | 5(fp4),7(fp8) | 36864 | **full MoE decode (36.5%)** | ✅ |
| ExpertSelectUpGateSiLUDSv32 | expert_sel_up_gate_silu | 1,2,4 | 5,6,7,8 | 36864 | select top-8 + up+gate+silu (fp4) | ✅ |
| RMSNormUpGateSiLUDSv32 | rmsnorm_up_gate_silu | 1,2,4 | 5,6,7 | 36864 | dense MLP rmsnorm+up+gate+silu | ✅ |

### 6. Communication — flag-based NVLink allreduce (KeComputeType 0/6/7)

| kernel | op module | kSeqLen | CT | smem | role | std |
|---|---|---|---|---|---|---|
| DownAllreduce | down_allreduce | 1,2,4 | 0 | 32768 | dense MLP down + allreduce | ▲ comm |
| ExpertDownAllreduce | expert_down_allreduce | 1,2,4 | 0,7 | 32768 | expert down + allreduce | ▲ comm |
| UnprojOAllreduceDSV32DevB | unproj_o_allreduce | 1,2,4 | 6,7 | 40960 | o unproj + allreduce | ▲ comm |
| EHProjAllReduce | eh_proj_allreduce | 1,2,4,8 | 0 | 32768 | MTP eh_proj + allreduce | ▲ comm |
| PaddedAllReduceAdd | padded_allreduce_add | 1,2,4 | 0 | 4096 | padded allreduce add | ▲ comm |
| Top1Allreduce | (top1 allreduce) | 1,2,4,8,16 | 0 | 32768 | sampling argmax allreduce | ▲ comm |

### 7. LM head + sampling + MTP

| kernel | op module / torch.ops | kSeqLen | CT | smem/vocab | role | std |
|---|---|---|---|---|---|---|
| HeadProj | head_proj_op | 1,2,4,8,16 | 3 | 40960/49152/65536 | LM-head GEMM (39.2µs/78%HBM) | ✅ |
| RMSNormHeadProj | rmsnorm_head_proj | 1,2,4 | 3 | 40960 | fused final-norm + LM-head | ✅ |
| MTPPreProcess | mtp_preprocess | 1,2,4 | 0 | 40960 | cat(norm(emb),norm(prev))→eh_proj | ✅ |
| ExecuteTopP | top_p_op (ParallelTopPSampler) | 1,2,4 | — | vocab 16160 / 19360 | top-p sampler | ✅ |
| top1_bf16_singleblock_128b | (greedy top1) | — | — | — | greedy argmax sampler | ✅ |
| mtp_verifier::verify_kernel | (mtp verify) | num_mtp=3 | — | 2048/6144/7168 | MTP in-graph acceptance check | ✅ |
| llm_preprocess::pre_forward_kernel | (preprocess) | — | — | 2048/6144/7168, d∈{64,128} | embed/preprocess | ✅ |

## GLM-5 kernels in the same .so (EXCLUDED from DSV32 tasks)

`RMSNormGlm5`, `ProjXWqakisGLM5`, `ProjXWqakis`(GLM5 path), and everything under
`models/glm_5/` — the `libtilert_dsv32.so` is shared between DeepSeek-V3.2 and GLM-5;
these are GLM-5-specific and are **not** on the DS V3.2 decode path. Not tasked.

## KDA task plan

- **Tier 1 (critical path, full rigor — oracle + ≥3× ncu + full shape):**
  PureMlaDsv32, FusedMoe, HeadProj, RMSNormQuant (the 4 existing, completed),
  plus LayernormRopeRotate (KV write), SparseIndexFusedDsv32 + TopkAccurate (DSA),
  RmsnormProjQWqb, ProjXWqkva, RMSNormExpertProj, ExpertSelectUpGateSiLU,
  RMSNormHeadProj, MTPPreProcess.
- **Tier 2 (standalone-measurable, oracle + ≥3× ncu):** the remaining ✅ ops.
- **Tier 3 (▲ comm — golden_forward + shape spec + in-graph profiler number only):**
  the allreduce/broadcast/receive ops. `tilert_forward` needs NVLink peer_bufs/ll_buf
  + flag exchange (set up by `end2end.py`), so they are **not isolatable on 1 GPU**;
  documented with the in-graph profiler per-call time and a note.

## Correctness-oracle status (B3) — validated on B200

`harness/tilert_oracle.py` runs each op's `golden_forward` vs the **real
`torch.ops.tilert.*`** kernel on synthetic inputs (correct weight swizzle handled by
the modules). **16 standalone ops PASS** (bf16 rel <2e-2, fp8/fp4 <5e-2) — full table
+ synthesized input shapes in `harness/ORACLE_RESULTS.md`. Highlights: flash_sparse_mla
(PureMlaDsv32, #1) 3.0e-3 at seq 1/2/3/4; layernorm_rope_rotate (KV write) 3.5e-3;
qkv_rope / rmsnorm_kv bit-exact; head_proj 5.1e-3; projq_wqb/projo_wkvb (fp8) 3.x e-3.

Deferred (ABI: chained scores / 256-expert FP4 pack / cache-state / function-style
workspace): FusedMoe full-pack, ExpertSelectUpGateSiLU, ProjXWqkva, sparse_index/topk,
mtp_preprocess — their compute cores are covered by sibling oracle cases
(rmsnorm_up_gate_silu, rmsnorm_expert_proj). Comm ops: golden math reimplemented in the
task baselines; latency target = in-graph profiler time (not 1-GPU-isolatable).

## TileRT reference latencies (B5) — `docs/tilert_reference.md`

Each kernel's target = **median of ≥3 isolated ncu runs** (`gpu__time_duration.avg`)
on an idle B200, measured by `harness/sweep_ncu.py`. e.g. head_proj seq1 =
39.33 µs (disp 0.3%, HBM 77.9%) — matches the prior single-run 39.2 µs/78%.
