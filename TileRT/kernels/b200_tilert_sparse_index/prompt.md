# b200_tilert_sparse_index
Target GPU: NVIDIA B200 (sm_100).

## Problem
fused index scoring + top-2048 select (tcgen05). Matches TileRT `SparseIndexFusedDsv32ExecutorImpl`.

**Decode share:** 7.6% of TileRT decode CUDA time.

Math: see `baseline/sparse_index.py` (a faithful port of TileRT's own `golden_forward`,
validated against the real op by `../../harness/tilert_oracle.py`).

## Shapes (decode + MTP)
- kSeqLen (from SASS symbol table) = [1, 2, 4]  (MTP q_len subset = [1, 2, 4]; decode=1, MTP verify=4)
- KeComputeType variants = [0=none]
- model dims: dim=7168, q_lora=1536, kv_lora=512, qk_nope=128, qk_rope=64,
  v_head=128, n_local_heads=20 (7-worker padded), n_routed=256, moe_inter=2048,
  index_topk=2048, vocab/8=16160.
- Full per-shape list: `bench/workloads.json`.

## TileRT reference (the target to match)
Measured from the real `libtilert_dsv32.so` op via ncu, **median of >=3 runs**
(see `config.toml [reference]` and `../../docs/tilert_reference.md`). Method:
`../../docs/benchmark_method.md`.

## Design levers to exploit (TileRT blog + SASS)
- **Tile-level overlap (warp specialization + mbarrier double-buffer, §4/§13):** Prefetcher warps stream weights/acts GMEM->SMEM via TMA while Consumer warps run warpgroup MMA; an mbarrier ring overlaps tile t+1 load with tile t compute.
- **Bandwidth levers (§16/§20):** FP4 (MXFP4) expert weights (~4x less HBM); DSA sparse top-2048 KV so decode KV-read scales with 2048, not seq_len; compressed MLA latent cache (kv_c 512 + pe 64).
- **tcgen05/TMEM only for DSA index (§16):** the index/topk path uses tcgen05 (UTCHMMA); everything else is warpgroup HMMA. Default to warpgroup HMMA.

See `../../docs/tilert_design_levers.md` for the full lever catalog.

## Goal
A B200 CUDA kernel matching `baseline/sparse_index.py` on **every** workload shape
(tolerances in `../../docs/tilert_correctness_contract.md`: bf16 <2e-2,
fp8/fp4 <5e-2) and reaching TileRT's measured latency on each shape.
