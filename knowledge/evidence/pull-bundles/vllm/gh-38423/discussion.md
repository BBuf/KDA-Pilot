# PR Discussion Digest

- Source PR: [vllm-project/vllm#38423](https://github.com/vllm-project/vllm/pull/38423)
- Source page: `sources/prs/vllm/PR-38423.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38423`
- Generated at: `2026-05-20T15:40:30.416725+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-28T07:58:01Z`
- Merged: `2026-03-30T16:36:18Z`

## Discussion Counts

- Issue comments: 18
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: claude, eugr, gbanyan, johnnynunez, mergify, mgoin, wzhao18, yewentao256
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-03-28T07:58:05Z` `COMMENTED` by `claude` - Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer ... (https://github.com/vllm-project/vllm/pull/38423#pullrequestreview-4025219929)
- `2026-03-28T08:00:18Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the CUTLASS revision to v4.4.2 and upgrades FlashInfer to version 0.6.7 across ... (https://github.com/vllm-project/vllm/pull/38423#pullrequestreview-4025221438)
- `2026-03-28T13:31:01Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/38423#pullrequestreview-4025585282)
- `2026-03-29T20:58:11Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/38423#pullrequestreview-4027245327)
- `2026-03-30T02:09:37Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/38423#pullrequestreview-4027664832)
- `2026-03-30T02:25:25Z` `COMMENTED` by `johnnynunez` (https://github.com/vllm-project/vllm/pull/38423#pullrequestreview-4027701499)
- `2026-03-30T02:25:32Z` `COMMENTED` by `johnnynunez` (https://github.com/vllm-project/vllm/pull/38423#pullrequestreview-4027701685)
- `2026-03-30T14:25:12Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/38423#pullrequestreview-4031001102)
- `2026-03-30T15:28:16Z` `COMMENTED` by `yewentao256` - There is a flashiner version update PR here, not sure if we want to land it separately (https://github.com/vllm-project/vllm/pull/38423#pullrequestreview-4031440805)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-03-29T04:40:20Z` `issue` by `johnnynunez`; signals: block, compile, cutlass, gemm, moe, overflow, sm100, sm120; excerpt: "Related bug some models: SM120/SM121 (DGX Spark, RTX 50) has only 99KB SMEM vs 228KB on SM100. The K=128 block-scaled MoE GEMM tiles compile ..." (https://github.com/vllm-project/vllm/pull/38423#issuecomment-4149419039)
- `2026-03-29T08:13:50Z` `issue` by `gbanyan`; signals: cuda, cutlass, flashinfer, fp4, nvfp4, overflow, perf, tile; excerpt: "Test Report: PR 38423 on DGX Spark SM121 with Qwen3.5-122B-A10B-NVFP4 Hardware: Single DGX Spark GB10 (SM121, 128GB UMA) Model: Sehyo/Qwen3.5-122B-A10B-NVFP4 (compressed-tensors) vLLM: 0.18.1rc1 from ..." (https://github.com/vllm-project/vllm/pull/38423#issuecomment-4149678249)
- `2026-03-29T22:49:21Z` `issue` by `johnnynunez`; signals: cache, cuda, cutlass, flashinfer, fp4, nvfp4, overflow, perf; excerpt: "Test Report: PR 38423 on DGX Spark SM121 with Qwen3.5-122B-A10B-NVFP4 Hardware: Single DGX Spark GB10 (SM121, 128GB UMA) Model: Sehyo/Qwen3.5-122B-A10B-NVFP4 (compressed-tensors) vLLM: 0.18.1rc1 from ..." (https://github.com/vllm-project/vllm/pull/38423#issuecomment-4151244923)
- `2026-03-30T15:47:01Z` `issue` by `mgoin`; signals: accuracy, b200, flashinfer, fp4, fp8, h100, h200, hang; excerpt: "- Distributed DP Tests (2 GPUs) should be fine, this is a flaky test and for FlashAttn v1/distributed/test eagle dp.py::test run eagle dp[FLASH ATTN]. ..." (https://github.com/vllm-project/vllm/pull/38423#issuecomment-4156077553)
- `2026-03-30T14:25:12Z` `inline` by `wzhao18` `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`:412; signals: accuracy, flashinfer, fp4, fp8, moe, nan, nvfp4; excerpt: "WIth new FI version, there are various CI failures with accuracy collapse. I rooted down the cause to these. For reproducing the issue, can ..." (https://github.com/vllm-project/vllm/pull/38423#discussion_r3010168498)
- `2026-03-30T02:02:19Z` `issue` by `johnnynunez`; signals: accuracy, b200, benchmark, fp4, nvfp4, perf; excerpt: "ready to merge! @mgoin Now it is working perfectly and B200 accuracy tests passed for NVFP4 Nemotron Super NVFP4 - DGX Spark Results (Benchmark ..." (https://github.com/vllm-project/vllm/pull/38423#issuecomment-4151663058)
- `2026-03-29T20:57:58Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:6; signals: flashinfer, fp4, hang, moe, nvfp4; excerpt: "This change breaks pre-commit, please revert flashinfer import placement @johnnynunez Also merge with latest main to fix a few tests" (https://github.com/vllm-project/vllm/pull/38423#discussion_r3006763242)
- `2026-03-30T02:09:17Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:325; signals: fp4, moe, nvfp4; excerpt: "Ditto" (https://github.com/vllm-project/vllm/pull/38423#discussion_r3007185858)
- `2026-03-30T02:25:32Z` `inline` by `johnnynunez` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:325; signals: fp4, moe, nvfp4; excerpt: "same @wzhao18" (https://github.com/vllm-project/vllm/pull/38423#discussion_r3007215316)
- `2026-03-29T01:50:35Z` `issue` by `johnnynunez`; signals: cuda, cutlass, flashinfer; excerpt: "Getting consistent Illegal Instruction crashes with this PR. Building Flashinfer from main with FLASHINFER CUDA ARCH LIST=12.1a vLLM from main with this PR applied ..." (https://github.com/vllm-project/vllm/pull/38423#issuecomment-4149212441)
- `2026-03-29T10:40:45Z` `issue` by `johnnynunez`; signals: cuda, cutlass, overflow; excerpt: "Update: 128K without MTP is also intermittently unstable. It passed initial tests (1024 tokens completed) but later crashes with cudaErrorIllegalInstruction on subsequent requests. The ..." (https://github.com/vllm-project/vllm/pull/38423#issuecomment-4149883132)
- `2026-03-30T02:08:47Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`:412; signals: fp8, moe; excerpt: "@pavanimajety do you know if this is right? I thought we fixed this issue for trtllm MoE across the board" (https://github.com/vllm-project/vllm/pull/38423#discussion_r3007185075)
