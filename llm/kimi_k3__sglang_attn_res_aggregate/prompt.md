# KDA Prompt: kimi_k3__sglang_attn_res_aggregate

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `sglang.srt.layers.attn_residual._aggregate`

**18.2% of total serving GPU time** on `moonshotai/Kimi-K3` (cookbook-aligned
profile, peak `sharegpt_high`) — a serving-profile headroom signal used to select this
standalone kernel task. Family `attn_residual`, category `attention`.

Kimi-K3 is a 3T-parameter hybrid model whose weights need 2 nodes, so the cookbook profile and the kernel-API shapes were captured on a 2x4 GB300 (sm_103) TP=8 deployment; the standalone kernel optimization itself runs single-GPU on the B200 lane (all three kernels require only SM100+). The captured shapes are the contract, not the capture host.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU and GPU kernel
selection provenance, then use `bench/workloads.json` as the standalone shape
source. For the normal RLCR loop, optimize and validate via the task-local
standalone benchmark on one idle target GPU, without adding external
runtime-readiness or fleet-level A/B gates. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
