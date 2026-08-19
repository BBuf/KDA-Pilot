# qwen38_nvfp4__fp4_w4a4_skinny_gemm

Target GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (sm_120). Model: RadixArk/Qwen3.8-27B-NVFP4 (NVFP4 W4A4 MLP + FP8 projections, mixed ModelOpt).

**40.7% of the DSpark verify step and 50.5% of the plain-decode step** live in the
flashinfer `mm_fp4` cutlass path plus its standalone activation-quant kernels
(`fp4_quantize` 2.2%, `silu+quant` fused where the serving stack enables it). At the
production tiers - M=1 decode, **M=9 DSpark verify** (block 8, fixed), M~4.4k prefill -
the GEMM is weight-bound: a weight-streaming skinny GEMM that consumes bf16 activations
directly (mm_bf16_fp4-style, folding the quant kernels) has the whole quant time plus
the tiny-M tactic gap as headroom.

bs=1 4k-in/1k-out: no-spec 66.7 tok/s (ITL 14.78 ms); DSpark 153.3 tok/s (ITL 3.48 ms, accept 3.47) - 2.30x. Verify forwards are fixed M=T=9 (block 8 + 1).

Beat the baseline OPS on the workload rows (geomean, no row regression), correctness
per `docs/measurement_contract.md`. Real captured activations ship for the quantize
ops at M in {1, 8, 9} and T in {9, 4096, 4369}; weights reconstruct from shape
metadata. Evidence: `docs/profile_evidence.md`.
