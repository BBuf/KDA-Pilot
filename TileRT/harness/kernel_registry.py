"""Machine-readable TileRT DeepSeek-V3.2 kernel registry (single source of truth).

Drives: workloads.json shape coverage (B2), per-kernel prompt blog levers (B6),
and the config.toml [reference] targets (B5). The (seq, ct) sets are the
AOT-compiled specialization sets read from the SASS symbol table
(tilert_re/dsv32.kernels.demangled.txt) — i.e. the shapes TileRT actually
dispatches. See ../KERNEL_REGISTRY.md for the human-readable version.

ct codes: 0=none(no-MMA mem/comm), 3=bf16, 5/6/8=fp4, 7=fp8.
std: 'yes' = isolatable on 1 GPU via golden_forward/tilert_forward oracle;
     'comm' = needs multi-GPU NVLink peer/flag setup (not isolatable).
levers: which design levers from docs/tilert_design_levers.md the prompt cites.
"""

# dim constants (model_args.py)
DIM = 7168
QLORA = 1536
KVLORA = 512
QK_NOPE = 128
QK_ROPE = 64
V_HEAD = 128
N_HEADS = 128
N_LOCAL_HEADS = 20      # 7-worker padded (§14)
INDEX_N_HEADS = 64
INDEX_HEAD_DIM = 128
INDEX_TOPK = 2048
MOE_INTER = 2048
N_ROUTED = 256
N_ACT = 8
VOCAB = 129280
VOCAB_PER_DEV = VOCAB // 8   # 16160
BLOCK = 128

REGISTRY = {
    # ---- norm / quant ----
    "rmsnorm_quant": dict(executor="RMSNormQuant", op="rmsnorm_quant_op",
        seqs=[1, 2, 4, 8, 16], cts=[3], std="yes", group="norm",
        role="RMSNorm + per-128 fp8(e4m3) activation quant",
        levers=["L1", "L2"]),
    "rmsnorm": dict(executor="RMSNorm", op="rmsnorm_op",
        seqs=[1, 2, 4, 8, 16], cts=[3], std="yes", group="norm",
        role="plain RMSNorm", levers=["L1", "L2"]),
    "rmsnorm_kv": dict(executor="RmsnormKv", op="rmsnorm_kv_op",
        seqs=[1, 2, 4, 8, 16], cts=[3], std="yes", group="norm",
        role="RMSNorm of compressed KV latent (writes kv_cache)", levers=["L1", "L2"]),
    "rmsnorm_expert_proj": dict(executor="RMSNormExpertProjDsv32", op="rmsnorm_expert_proj_op",
        seqs=[1, 2, 4], cts=[0], std="yes", group="moe",
        role="RMSNorm + router gate proj -> scores[256]", levers=["L1", "L2"]),
    # ---- MLA projections + RoPE + KV write ----
    "rmsnorm_projx_wqkva": dict(executor="ProjXWqkvaDSV32", op="projx_wqkva_op",
        seqs=[1, 2, 4], cts=[5], std="yes", group="proj",
        role="x -> q_a[1536] + kv[512+64] (down-proj, fp4)", levers=["L1", "L2", "L3"]),
    "rmsnorm_projq_wqb": dict(executor="RmsnormProjQWqbHMMA", op="rmsnorm_proj_qb_op",
        seqs=[1, 2, 4], cts=[6, 7], std="yes", group="proj",
        role="rmsnorm(q_a) + Wq_b -> q[20,192]", levers=["L1", "L2", "L3"]),
    "rmsnorm_projq_wqi": dict(executor="RmsnormProjQWqiHMMA", op="rmsnorm_proj_qi_op",
        seqs=[1, 2, 4], cts=[6, 7], std="yes", group="proj",
        role="GPU0 indexer q_i proj", levers=["L1", "L2", "L3"]),
    "projq_wqb": dict(executor="ProjQWkvbDevBHMMA", op="projq_wqb_op",
        seqs=[1, 2, 4, 8, 16], cts=[6, 7], std="yes", group="proj",
        role="absorbed W_UK (q . kv_b)", levers=["L1", "L2", "L3"]),
    "projo_wkvb": dict(executor="ProjOWkvbDevBHMMA", op="projo_wkvb_op",
        seqs=[1, 2, 4, 8, 16], cts=[6, 7], std="yes", group="proj",
        role="absorbed W_UV (o . kv_b)", levers=["L1", "L2", "L3"]),
    "projx_wqaki": dict(executor="ProjXWqaki", op="projx_wqaki_op",
        seqs=[1, 2, 4], cts=[5], std="yes", group="proj",
        role="GPU0 x -> index query + ki (fp4)", levers=["L1", "L2", "L3"]),
    "projx_wis": dict(executor="ProjXWis", op="proj_w_op",
        seqs=[1, 2, 4, 8, 16], cts=[0, 7], std="yes", group="proj",
        role="indexer weight/scale proj", levers=["L1", "L2"]),
    "qkv_rope": dict(executor="QkvRope", op="qkv_rope_op",
        seqs=[1, 2, 4, 8, 16], cts=[3], std="yes", group="rope",
        role="QKV + RoPE", levers=["L1", "L2"]),
    "rotate": dict(executor="Rotate", op="rotate_op",
        seqs=[1, 2, 4, 8, 16], cts=[3], std="yes", group="rope",
        role="standalone RoPE rotate + hadamard", levers=["L1", "L2"]),
    "layernorm_rope_rotate": dict(executor="LayernormRopeRotate", op="layernorm_rope_rotate_op",
        seqs=[1, 2, 4, 8, 16], cts=[3], std="yes", group="kvwrite",
        role="LayerNorm + RoPE + write k/pe/ki cache (KV WRITE)", levers=["L1", "L2", "L5"]),
    # ---- MLA attention (reads KV cache) ----
    "mla_decode": dict(executor="PureMlaDsv32", op="flash_sparse_mla_op",
        seqs=[1, 2, 4], cts=[3], std="yes", group="mla", decode_pct=52.8,
        role="worker MLA decode, sparse gather top-2048 (#1 cost)", levers=["L1", "L2", "L5"]),
    "sparse_select_mla": dict(executor="SparseSelectMlaDsv32", op="flash_sparse_mla_op",
        seqs=[1, 2, 4], cts=[3], std="yes", group="mla", decode_pct=7.6,
        role="GPU0 self-MLA over selected KV", levers=["L1", "L2", "L5"]),
    "flash_sparse_mla": dict(executor="FlashSparseMlaDSv32DevB", op="flash_sparse_mla_op",
        seqs=[1, 2, 3, 4], cts=[7], std="yes", group="mla",
        role="flash sparse MLA (prefill/MTP, has seq=3)", levers=["L1", "L2", "L5"]),
    # ---- DSA index chain ----
    "sparse_index": dict(executor="SparseIndexFusedDsv32", op="sparse_index_topk_dsv32_op",
        seqs=[1, 2, 4], cts=[0], std="yes", group="dsa", decode_pct=7.6,
        role="fused index scoring + top-2048 select (tcgen05)", levers=["L1", "L5", "L6"]),
    "topk": dict(executor="TopkAccurateFusedDsv32", op="topk_accurate_op",
        seqs=[1, 2, 4], cts=[0], std="yes", group="dsa",
        role="top-2048 accurate select", levers=["L1", "L6"]),
    # ---- MoE ----
    "fused_moe": dict(executor="FusedMoe", op="fused_moe",
        seqs=[1, 2, 4], cts=[5, 7], std="yes", group="moe", decode_pct=36.5,
        role="full MoE decode (#2 cost, FP4 experts)", levers=["L1", "L2", "L3", "L5"]),
    "expert_select_up_gate_silu": dict(executor="ExpertSelectUpGateSiLUDSv32",
        op="expert_select_up_gate_silu_op",
        seqs=[1, 2, 4], cts=[5, 6, 7], std="yes", group="moe",
        role="select top-8 + up + gate + silu (fp4)", levers=["L1", "L2", "L3", "L5"]),
    "rmsnorm_up_gate_silu": dict(executor="RMSNormUpGateSiLUDSv32", op="rmsnorm_up_gate_silu_op",
        seqs=[1, 2, 4], cts=[5, 6, 7], std="yes", group="moe",
        role="dense MLP rmsnorm + up + gate + silu", levers=["L1", "L2", "L3"]),
    # ---- LM head + sampling + MTP ----
    "head_proj_gemm": dict(executor="HeadProj", op="head_proj_op",
        seqs=[1, 2, 4, 8, 16], cts=[3], std="yes", group="head",
        role="LM-head GEMM (bandwidth-bound)", levers=["L1", "L2", "L3"]),
    "rmsnorm_head_proj": dict(executor="RMSNormHeadProj", op="rmsnorm_head_proj_op",
        seqs=[1, 2, 4], cts=[3], std="yes", group="head",
        role="fused final-norm + LM-head", levers=["L1", "L2", "L3"]),
    "mtp_preprocess": dict(executor="MTPPreProcess", op="mtp_preprocess_layer",
        seqs=[1, 2, 4], cts=[0], std="yes", group="mtp",
        role="cat(norm(emb),norm(prev)) -> eh_proj", levers=["L1", "L2"]),
    # ---- comm (not isolatable on 1 GPU) ----
    "down_allreduce": dict(executor="DownAllreduce", op="down_allreduce_op",
        seqs=[1, 2, 4], cts=[0], std="comm", group="comm",
        role="dense MLP down + NVLink allreduce", levers=["L1", "L3", "L4"]),
    "expert_down_allreduce": dict(executor="ExpertDownAllreduce", op="expert_down_allreduce_op",
        seqs=[1, 2, 4], cts=[0, 7], std="comm", group="comm",
        role="expert down + NVLink allreduce", levers=["L1", "L3", "L4"]),
    "unproj_o_allreduce": dict(executor="UnprojOAllreduceDSV32DevB", op="unproj_o_allreduce_op",
        seqs=[1, 2, 4], cts=[6, 7], std="comm", group="comm",
        role="o unproj + NVLink allreduce", levers=["L1", "L3", "L4"]),
    "eh_proj_allreduce": dict(executor="EHProjAllReduce", op="eh_proj_allreduce_op",
        seqs=[1, 2, 4, 8], cts=[0], std="comm", group="comm",
        role="MTP eh_proj + NVLink allreduce", levers=["L1", "L4"]),
    "padded_allreduce_add": dict(executor="PaddedAllReduceAdd", op="padded_allreduce_add_op",
        seqs=[1, 2, 4], cts=[0], std="comm", group="comm",
        role="padded allreduce add", levers=["L4"]),
    "broadcast_selected_token_ids": dict(executor="BroadcastSelectedTokenIds",
        op="broadcast_selected_token_ids_op",
        seqs=[1, 2, 4, 8, 16], cts=[0], std="comm", group="comm",
        role="GPU0 -> workers index broadcast", levers=["L4"]),
    "receive_selected_token_ids": dict(executor="ReceiveSelectedTokenIds",
        op="receive_selected_token_ids_op",
        seqs=[1, 2, 4, 8, 16], cts=[0], std="comm", group="comm",
        role="workers receive indices", levers=["L4"]),
}

CT_NAME = {0: "none", 3: "bf16", 5: "fp4", 6: "fp4", 7: "fp8", 8: "fp4"}

# B5: ≥3× isolated ncu medians (us) + HBM% per seq, measured on idle B200
# (harness/sweep_ncu.py). seq->(median_us, hbm_pct). See docs/tilert_reference.md.
MEASURED = {
    "rmsnorm":            {1: (7.46, 0.1),  2: (7.65, 0.13), 4: (7.36, 0.18)},
    "rmsnorm_quant":      {1: (8.74, 0.11), 2: (8.96, 0.12), 4: (9.02, 0.16)},
    "head_proj_gemm":     {1: (39.42, 77.6), 2: (39.55, 77.4), 4: (42.24, 72.4)},
    "rmsnorm_head_proj":  {1: (43.97, 69.6), 2: (43.90, 69.7), 4: (46.46, 65.9)},
    "rmsnorm_expert_proj":{1: (8.22, 5.96), 2: (9.02, 5.44), 4: (10.62, 4.67)},
    "projx_wis":          {1: (6.11, 2.03), 2: (5.98, 2.09), 4: (6.59, 1.96)},
    "projq_wqb":          {1: (5.92, 2.97), 2: (6.21, 2.84), 4: (7.84, 2.26)},
    "projo_wkvb":         {1: (6.14, 2.88), 2: (6.59, 2.74), 4: (7.90, 2.35)},
    "mla_decode":         {1: (11.68, 2.72), 2: (12.45, 2.56), 4: (12.48, 2.59)},
    "flash_sparse_mla":   {1: (11.68, 2.72), 2: (12.45, 2.56), 3: (12.29, 2.61), 4: (12.48, 2.59)},
    "rotate":             {1: (7.23, 0.05), 2: (7.23, 0.08), 4: (6.85, 0.15)},
    "qkv_rope":           {1: (6.66, 0.02), 2: (6.82, 0.03), 4: (6.82, 0.04)},
    "rmsnorm_kv":         {1: (6.08, 0.03), 2: (6.66, 0.03), 4: (6.88, 0.04)},
    "layernorm_rope_rotate": {1: (6.88, 0.04), 2: (7.04, 0.04), 4: (7.17, 0.04)},
    "rmsnorm_projq_wqb":  {1: (7.23, 10.81), 2: (7.68, 10.2), 4: (8.48, 9.24)},
    "rmsnorm_projq_wqi":  {1: (8.42, 19.71), 2: (8.86, 18.68), 4: (9.44, 17.59)},
    "rmsnorm_up_gate_silu": {1: (12.13, 35.79), 2: (14.72, 29.54), 4: (20.58, 21.13)},
}

# in-graph profiler targets (us) for ops not isolatable as a single launch (§16)
INGRAPH = {
    "fused_moe": 22.4, "sparse_index": 35.4, "sparse_select_mla": 35.4,
    "down_allreduce": 8.2, "expert_down_allreduce": 9.0, "unproj_o_allreduce": 11.0,
}


def mtp_note(seqs):
    """MTP q_len full set {1,2,3,4}: covered by this op's compiled seqs intersect."""
    have = [s for s in (1, 2, 3, 4) if s in seqs]
    return have


if __name__ == "__main__":
    yes = [k for k, v in REGISTRY.items() if v["std"] == "yes"]
    comm = [k for k, v in REGISTRY.items() if v["std"] == "comm"]
    print(f"{len(REGISTRY)} kernels: {len(yes)} standalone, {len(comm)} comm")
    for k, v in REGISTRY.items():
        cts = "/".join(CT_NAME[c] for c in v["cts"])
        print(f"  {k:30s} seq={v['seqs']} ct={cts} std={v['std']} mtp={mtp_note(v['seqs'])}")
