# TileRT per-op correctness oracle — results

Per-op golden_forward (TileRT's own PyTorch reference = the KDA baseline) vs the
**real fused `torch.ops.tilert.*` kernel**, on synthetic random inputs, with
correctly-swizzled weights (handled by each module's `init_random_weights()` +
weight converter). Run on B200 GPU7, container `sglang_bbuf`, tilert 0.1.4.

Reproduce: `cd /data/bbuf/kda_harness && CUDA_VISIBLE_DEVICES=7 python tilert_oracle.py`
(or `--op <name> --seq <n>`). Source: `KDA-Pilot/TileRT/harness/tilert_oracle.py`.

Tolerance (contract): bf16 rel < 2e-2; fp8/fp4 rel < 5e-2. **All 16 PASS.**

## Standalone-isolatable ops (golden vs real op) — PASS

| op (case) | TileRT kernel | s1 | s2 | s4 | (s3) | dtype | activation inputs synthesized |
|---|---|---|---|---|---|---|---|
| rmsnorm | RMSNorm | 1.7e-3 | 1.7e-3 | 1.7e-3 | — | bf16 | hidden[1,s,7168]bf16, gamma[7168]f32 |
| rmsnorm_quant | RMSNormQuant | 1.7e-3 | 1.7e-3 | 1.7e-3 | — | bf16/fp8 | hidden[1,s,7168]bf16, gamma[7168]f32 → +q[fp8]+scale[1,s,56]f32 |
| head_proj | HeadProj | 5.2e-3 | 5.1e-3 | 5.1e-3 | — | bf16 | h[1,s,7168]bf16, W[16160,7168]bf16 (16×1024 swizzle) |
| rmsnorm_head_proj | RMSNormHeadProj | 5.4e-3 | 5.4e-3 | 5.3e-3 | — | bf16 | hidden[1,s,7168]bf16 → logits[1,s,16160]f32 |
| rmsnorm_expert_proj | RMSNormExpertProjDsv32 | 1e-7 | 2e-7 | 2e-7 | — | bf16 | x[1,s,7168]bf16 → scores[1,s,256]f32 (router) |
| projx_wis | ProjXWis | 5.9e-3 | 5.0e-3 | 5.2e-3 | — | bf16 | x_norm[1,s,7168]bf16 → idx_scores[1,s,64]bf16 |
| projq_wqb | ProjQWkvbDevBHMMA | 3.5e-3 | 3.4e-3 | 3.3e-3 | — | fp8 | q_nope[1,s,20,128]bf16 → [1,s,20,512] (absorbed W_UK) |
| projo_wkvb | ProjOWkvbDevBHMMA | 3.2e-3 | 3.2e-3 | 3.2e-3 | — | fp8 | o[1,s,20,512]bf16 → [1,s,20,128] (absorbed W_UV) |
| **flash_sparse_mla** | **PureMlaDsv32** (52.8%) | **3.1e-3** | 3.0e-3 | 2.9e-3 | **3.0e-3** | bf16 | q_nope[1,s,16,512], q_pe[1,s,16,64], kv_cache[1,2048,512], pe_cache[1,2048,64] bf16, idx[1,s,2048]i32, cur_pos[1]i32 → o[1,s,16,512]bf16 |
| rotate | Rotate | 2.8e-3 | 2.8e-3 | 2.9e-3 | — | bf16 | idx_q[1,s,64,128]bf16, freqs_cis[s,32]cf64 → [1,s,64,128] |
| qkv_rope | QkvRope | 0.0 | 0.0 | 0.0 | — | bf16 | q_pe[1,s,16,64]bf16, pe_cache[1,s,64]bf16, freqs[1,s,32]cf64 (writes pe_cache) |
| rmsnorm_kv | RmsnormKv | 0.0 | 0.0 | 0.0 | — | bf16 | kv[1,s,512]bf16, kv_cache[1,≥16,512]bf16 (writes cache) |
| **layernorm_rope_rotate** | **LayernormRopeRotate** (KV write) | 3.5e-3 | 3.5e-3 | 3.5e-3 | — | bf16 | idx_k[1,s,128]bf16, freqs_cis[s,32]cf64 → k_idx_cache[1,s,128]bf16 |
| rmsnorm_projq_wqb | RmsnormProjQWqbHMMA | 3.3e-3 | 3.2e-3 | 3.2e-3 | — | fp8 | q[1,s,1536]bf16 → q_nope[1,s,20,128]+q_pe[1,s,20,64] |
| rmsnorm_projq_wqi | RmsnormProjQWqiHMMA | 3.2e-3 | 3.2e-3 | 3.1e-3 | — | fp8 | q[1,s,1536]bf16 → iq[1,s,64,128] (GPU0 indexer) |
| rmsnorm_up_gate_silu | RMSNormUpGateSiLUDSv32 | 3.4e-2 | 3.5e-2 | 3.4e-2 | — | fp8 | x[1,s,7168]bf16 → [1,s,9,256]bf16 (dense MLP up/gate/silu, fp8) |

Notes:
- `qkv_rope` / `rmsnorm_kv` are bit-exact (0.0) — pure RoPE/RMSNorm cache writes.
- `rmsnorm_up_gate_silu` 3.4e-2 is the fp8 MMA path (within the 5e-2 fp8 bar).
- MLA q/o projections shard 128 heads over **7 workers → 20 padded heads** (§14).
- `flash_sparse_mla` covers PureMlaDsv32 (worker) and is the seq=3 carrier (MTP).

## Quirks discovered (encoded in the harness, reusable for any op)

1. Call `golden_forward`/`tilert_forward` **directly** — `__call__` is inconsistent
   across modules, and `enable_tilert()` calls a missing `to_tilert_weights` on some.
2. Constructor arg ORDER differs per module → always pass kwargs.
3. Some modules have `init_tilert_vars(b,seq)`; others allocate inside `tilert_forward`
   with bare `torch.zeros` → wrap construction+forward in `with torch.device(dev)`.
4. `golden`/`tilert` may return tuples → pick compared element by `out_idx`.
5. `init_random_weights` sometimes makes a GEMM ref weight f32 where the op / golden
   matmul wants bf16 → `post_init` casts it (keeping golden==tilert weights so the
   comparison isolates kernel numerical error). Affected: rmsnorm_expert_proj,
   projq_wqb, projo_wkvb, rmsnorm_projq_wqb, rmsnorm_projq_wqi.
6. Some fused-proj modules need `set_algorithm(FP16MMA)` BEFORE `init_random_weights`.
7. `flash_sparse_mla` topk_indices = arange(kv_len) (dense for kv_len=topk=2048);
   cur_pos = kv_len − seq drives the causal mask for seq>1.

## Deferred / not isolatable

| op | reason |
|---|---|
| FusedMoe (full) | needs the full 256-expert FP4/FP8 weight pack + router scores; not a 1-call module standalone. Its compute core is covered by `rmsnorm_up_gate_silu` (up/gate/silu) + `rmsnorm_expert_proj` (routing). Deferred: full-pack ABI. |
| ExpertSelectUpGateSiLUDSv32 | needs scores[256] + bias from rmsnorm_expert_proj (chained) + packed expert up/gate (FP4); `init_tilert_vars(b,seq,device)` extra arg. Deferred: chained-input ABI (>10 min). |
| ProjXWqkvaDSV32 / RMSNormProjxWqkva | `init_tilert_vars(b,seq,max_len)` + needs cur_pos + pe_cache; 3-tuple output (q_a/kv/pe). Deferred: cache-state ABI. |
| sparse_index / sparse_index_topk / topk | function-style (not TileRTModule); need logits[1,seq,cache_len]f32 + i32 workspace; topk=2048 fixed. Deferred: workspace ABI. |
| mtp_preprocess (MTPPreProcess) | custom op signature (params/temp_vars lists); needs emb + last_hidden + eh_proj swizzle. Deferred: custom-ABI. |
| down_allreduce, expert_down_allreduce, unproj_o_allreduce, eh_proj_allreduce, padded_allreduce_add, broadcast/receive_selected_token_ids | **▲ comm — NOT isolatable on 1 GPU**: `tilert_forward` needs NVLink `peer_bufs`/`ll_buf` ptr exchange + flag sync (set up by end2end.py across 8 GPUs). golden_forward math IS reimplementable (down-proj + sum + allreduce + residual); use in-graph profiler time for the latency target. |
