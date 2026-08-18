# qwen38_nvfp4 (DSpark bs=1) — standalone kernel task selection

- Model: `RadixArk/Qwen3.8-27B-NVFP4` (mixed ModelOpt recipe: NVFP4 W4A4 MLP ×193 tensors + per-tensor-static FP8 attn/GDN projections ×208; pin revision `5b4377e580aebdd1b9a8e918b406cb28ad9bff8a`)
- Target GPU: NVIDIA RTX PRO 6000 Blackwell (SM120, 96 GB, ~1.46 TB/s)
- Serving goal: **bs=1 output-throughput with DSpark speculative decoding**, 4k-in / 1k-out
- Serving capture cmd (provenance):
  `python -m sglang.launch_server --model-path <snap> --trust-remote-code --tp-size 1 --disable-radix-cache --mem-fraction-static 0.85 --max-running-requests 8 --cuda-graph-max-bs 8 --mamba-ssm-dtype bfloat16 --kv-cache-dtype fp8_e4m3 --speculative-algorithm DSPARK --speculative-dspark-block-size 8`
- Bench cmd: `python -m sglang.bench_serving --backend sglang-oai --dataset-name random --random-input-len 4096 --random-output-len 1024 --random-range-ratio 1.0 --num-prompts 4 --max-concurrency 1 --seed 1234 --apply-chat-template`
- Task mode: standalone single-GPU kernel optimization on SM120; no live serve or e2e gate during RLCR.

## Evidence base

Plain-decode (non-spec) bs=1 step composition, measured from a real torch-profiler
trace on the target GPU (2026-08-14, tree=main-equivalent, wall/step 13.39 ms ==
measured ITL 13.36 ms; kernel table in each task's `docs/profile_evidence.md`):

| family | GPU/step | share | calls/step |
|---|---:|---:|---:|
| NVFP4 W4A4 GEMM (cutlass via flashinfer mm_fp4), M=1 | 7.09 ms | 50.5% | 129 |
| FP8 per-tensor GEMV (`sglang::sm120_fp8_gemv_kernel`), M=1 | 4.77 ms | 34.0% | 128 |
| in_proj_ba bf16 GEMV via cuBLAS `dot`+`reduce_1Block` | 0.54 ms | 3.8% | 96 |
| full attention (flashinfer BatchPrefill+merge) | 0.37 ms | 2.6% | 32 |
| norms + quant glue (`fused_add_rmsnorm`, `_static_quant_fp8`, fp4 quant) | ~0.7 ms | ~5% | ~450 |
| GDN decode (fused_recurrent + conv-update + gated LN) | ~0.31 ms | ~2.3% | ~144 |

**Why DSpark changes the task list**: with DSpark, decode steps become verify
forwards of `M = block_size(+1) ∈ [4, 9]`. Weight traffic per step is unchanged
(the BW floor stays ~11.9 ms) but each step yields `accept_len` tokens. The
throughput ceiling is therefore set by how little the M∈[2,16] step regresses
vs the M=1 step. Known cliffs on this path:

1. `sm120_fp8_gemv` is **M=1-only** — verify falls back to cuBLAS sm89 tiles
   (tile 64×128+, heavily padded at M≤16).
2. flashinfer `mm_fp4` tactic dispatch at M≤16 is untuned on SM120, and the
   per-call activation-quant kernels (`cvt_fp16_to_fp4`, block-scale quant)
   stay on the critical path even though compute is free at tiny M.
3. GDN verify (triton backend) scales sequentially with draft length.

## Selected tasks (ranked by expected verify-step share)

| task | category | entry family | evidence (bs=1 decode share) | DSpark relevance |
|---|---|---|---:|---|
| `qwen38_nvfp4__fp4_w4a4_skinny_gemm` | quant_gemm | flashinfer mm_fp4 | 50.5% | M∈[1,16] tactic + fold act-quant |
| `qwen38_nvfp4__sm120_fp8_gemv_multirow` | quant_gemm | sm120_fp8_gemv | 34.0% | extend M=1 fast path to M∈[1,16] |
| `qwen38_nvfp4__gdn_ba_proj_fold` | gemv_fusion | cuBLAS dot/reduce | 3.8% + 96 launches | flat cost every verify step |
| `qwen38_nvfp4__gdn_verify_fused_recurrent` | linear_attention | fla fused_recurrent | 2.3% @M=1, est 10-15% @T=8 | sequential-in-T today |

## Dropped / excluded

- full attention (2.6%): flashinfer BatchPrefill already tuned; verify T≤9 fine.
- norm/quant glue singles (<2% each): the serving-side fusions (sgl-project/sglang#34934)
  already cover the prefill instances; decode instances are launch-bound and
  hidden by CUDA graphs.

## Workload provenance / refresh

`bench/workloads.json` shapes are derived from the model config
(hidden 5120, intermediate 17408, attn 24q/4kv×256, GDN 16k/48v×128, conv 4,
vocab 248320) and the measured call counts — geometry is exact; they are marked
`"source": "derived_pending_capture"`. When the target box is reachable, refresh
with the real DSpark API capture:

    llm/scripts/sglang_capture_shape_sitecustomize.py  (attach to the serve cmd above,
    run the bench cmd, then regenerate workloads from docs/captured_kernel_api_shapes.json)

The DSpark verify M distribution (block size, accept histogram) must come from
that capture; until then tasks 1-3 use M ∈ {1, 2, 4, 6, 8, 16} tiers and task 4
uses T ∈ {2, 4, 8}.
