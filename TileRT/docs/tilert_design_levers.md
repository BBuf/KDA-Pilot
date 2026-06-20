# TileRT design levers (what a KDA candidate kernel should borrow)

Canonical list of the TileRT engine design points exposed by the blog + confirmed
in the SASS (`TileRT_讨论材料.md` §0/§4/§7/§13/§16/§20). Each kernel task's
`prompt.md` cites the **subset relevant to that kernel** so the optimizing agent
knows which techniques to reach for. Source section in parentheses.

## L1 — Tile-level overlap via warp specialization + mbarrier double-buffer (§4, §13)
The persistent CTA splits its 384 threads into a **Prefetcher** warpgroup (128 thr)
that issues TMA bulk copies GMEM→SMEM (`cp.async.bulk` / `UBLKCP`, 897 in SASS) and
a **Consumer** warpgroup (256 thr) that runs tensor-core MMA. A ring of `mbarrier`s
(`ARRIVE.TRANS64`, 2300+ in SASS; `ELECT` leader election 1028) hands buffers
between them so weight/activation movement for tile *t+1* overlaps MMA on tile *t*.
→ Relevant to every GEMM/attention/MoE kernel: hide HBM latency behind compute.

## L2 — Intermediate activations never round-trip GMEM (§13.3)
Within a fused op, all intermediate activations stay in **SMEM/TMEM**; only the
final result is written to GMEM. E.g. `RmsnormProjQWqb` keeps the normalized q_a in
SMEM between the RMSNorm and the Wq_b GEMM; `ExpertSelectUpGateSiLU` keeps up/gate
products on-chip through the SiLU. → Relevant to all fused (rmsnorm+proj, proj+act)
kernels: fuse to avoid the extra GMEM write+read of the intermediate.

## L3 — Weight read once via TMA + occupancy=1 persistent grid (§4)
Grid = **148 CTAs = B200 SM count**, 1 CTA/SM (occupancy=1), forced by pushing
registers to ~168 × 384 thr ≈ 64.5K ≈ the full 65,536-register file/SM. Each weight
tile is streamed **once** through TMA into the resident CTA; no re-fetch, no L2
thrash. → Relevant to bandwidth-bound kernels (LM-head, projections, MoE): the
target HBM% (e.g. head_proj 78%) is only reachable with a purpose-built persistent
GEMV that consumes the weight in TileRT's swizzle, not a generic tiled GEMM (~58%).

## L4 — Communication fused into the op: flag-based NVLink allreduce (§7)
The down/expert-down/unproj-o/eh-proj kernels **fuse the cross-GPU allreduce into
the compute kernel**: peer LL buffers + device-pointer exchange (`peer_bufs`/`ll_buf`)
+ a `flag` token; `RED`/`ATOM` (1098/3488) do P2P read-modify-write over NVLink and
`BAR.ALL.GPU` (142) does grid-level sync. No separate NCCL launch; put/wait overlaps
with the tail of the GEMM at tile granularity. → Relevant to the comm kernels.

## L5 — Bandwidth levers: FP4 experts + DSA sparse top-2048 KV (§16, §20)
- **FP4 (MXFP4) expert weights**: MoE up/gate read at 4 bits → ~4× less HBM than
  bf16. The decode MoE (`FusedMoe`, 22.4µs) only hits its target with FP4 + an
  M=1-specialized GEMM; a bf16 grouped GEMM caps ~58% HBM at 157µs (§17).
- **DSA sparse attention**: the indexer selects **top-2048** KV; workers read only
  those rows of the compressed latent cache (kv_c 512 + pe 64), so decode KV-read
  bandwidth scales with 2048, **not** seq_len. → Relevant to MLA decode + MoE.

## L6 — tcgen05 / TMEM only for the DSA index path; everything else warpgroup HMMA (§16)
`UTCHMMA`/tcgen05 appears only in `SparseIndex`/`SparseSelectMla` (the DSA indexer);
all MLA / MoE / MLP / projection / LM-head compute is **warpgroup BF16/FP8/FP4 HMMA**
(`HMMA.16816.F32.BF16`, 3328 in SASS). → A candidate should default to warpgroup
HMMA and only consider tcgen05 for the index/topk kernels.

## Per-kernel lever map (which Lx each task's prompt cites)

| kernel family | L1 | L2 | L3 | L4 | L5 | L6 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| head_proj / rmsnorm_head_proj (LM-head) | ✓ | ✓ | ✓ |  |  |  |
| rmsnorm_quant / rmsnorm / rmsnorm_kv | ✓ | ✓ |  |  |  |  |
| rmsnorm_projx_wqkva / projq_wqb / projo_wkvb / projx_* | ✓ | ✓ | ✓ |  | fp8/fp4 |  |
| layernorm_rope_rotate (KV write) | ✓ | ✓ |  |  | latent KV |  |
| pure_mla / flash_sparse_mla (MLA decode) | ✓ | ✓ |  |  | ✓ DSA |  |
| sparse_index / topk (DSA index) | ✓ |  |  |  | ✓ | ✓ tcgen05 |
| rmsnorm_expert_proj (router) | ✓ | ✓ |  |  |  |  |
| expert_select_up_gate_silu / fused_moe | ✓ | ✓ | ✓ |  | ✓ FP4 |  |
| down/expert_down/unproj_o/eh_proj/padded allreduce | ✓ |  | ✓ | ✓ |  |  |
| mtp_preprocess | ✓ | ✓ |  |  |  |  |
| broadcast/receive_selected_token_ids | ✓ |  |  | ✓ |  |  |
