# b200_tilert_padded_allreduce_add
Target GPU: NVIDIA B200 (sm_100).

## Problem
padded allreduce add. Matches TileRT `PaddedAllReduceAddExecutorImpl`.

> NOTE: this is a **communication kernel** — the real `torch.ops.tilert.padded_allreduce_add_op` needs multi-GPU NVLink peer_bufs/ll_buf + flag setup, so it is profiled **in-graph** (not isolatable on 1 GPU). The PyTorch baseline still captures the compute (down/unproj GEMM) + the allreduce-sum semantics.

Math: see `baseline/padded_allreduce_add.py` (a faithful port of TileRT's own `golden_forward`,
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
- **Comm fused into the op (flag-based NVLink allreduce, §7):** peer LL buffers + device-ptr exchange + a flag token; P2P read-modify-write over NVLink overlaps the GEMM tail at tile granularity (no separate NCCL launch).

See `../../docs/tilert_design_levers.md` for the full lever catalog.

## Goal
A B200 CUDA kernel matching `baseline/padded_allreduce_add.py` on **every** workload shape
(tolerances in `../../docs/tilert_correctness_contract.md`: bf16 <2e-2,
fp8/fp4 <5e-2) and reaching TileRT's measured latency on each shape.
