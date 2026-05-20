# PR Discussion Digest

- Source PR: [vllm-project/vllm#38083](https://github.com/vllm-project/vllm/pull/38083)
- Source page: `sources/prs/vllm/PR-38083.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38083`
- Generated at: `2026-05-20T15:40:28.630435+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-25T07:58:30Z`
- Merged: `2026-03-26T08:21:47Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: WynnD, claude, sgunasekar, vadiklyutiy, ywang96
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2026-03-25T08:04:25Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces new Qwen3.5 model configurations for GSM8K evaluation, including specific accuracy thresholds and ... (https://github.com/vllm-project/vllm/pull/38083#pullrequestreview-4004735590)
- `2026-03-26T05:07:09Z` `APPROVED` by `ywang96` (https://github.com/vllm-project/vllm/pull/38083#pullrequestreview-4011451630)
- `2026-03-26T07:14:52Z` `COMMENTED` by `claude` (https://github.com/vllm-project/vllm/pull/38083#pullrequestreview-4011921932)
- `2026-03-26T07:54:44Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/38083#pullrequestreview-4012092795)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/fp8.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/input_quant_fp8.py`: 1 inline comment(s)
- `vllm/config/vllm.py`: 1 inline comment(s)
- `vllm/utils/deep_gemm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-26T07:14:53Z` `inline` by `claude` `vllm/model_executor/layers/quantization/fp8.py`:286; signals: accuracy, attention, blackwell, block, cute, cutlass, deepgemm, flashinfer; excerpt: "🔴 The fix is incomplete: Fp8MoEMethod never reads quant config.use deep gemm and still selects the DeepGemm backend for routed expert layers via select ..." (https://github.com/vllm-project/vllm/pull/38083#discussion_r2992928980)
- `2026-03-26T07:14:53Z` `inline` by `claude` `vllm/config/vllm.py`:724; signals: accuracy, b200, benchmark, blackwell, deepgemm, fp8, gemm, moe; excerpt: "🟡 The auto-disable for Qwen3.5 on Blackwell cannot be overridden by VLLM USE DEEP GEMM=1, despite the PR description stating "VLLM USE DEEP GEMM ..." (https://github.com/vllm-project/vllm/pull/38083#discussion_r2992928986)
- `2026-03-26T07:14:53Z` `inline` by `claude` `vllm/utils/deep_gemm.py`:44; signals: accuracy, b200, blackwell, block, correctness, cutlass, deepgemm, fp8; excerpt: "🟡 should auto disable deep gemm() fires spuriously when DeepGemm is not active: it checks is device capability family(100) and model type but not ..." (https://github.com/vllm-project/vllm/pull/38083#discussion_r2992928987)
- `2026-03-26T07:54:43Z` `inline` by `vadiklyutiy` `vllm/model_executor/layers/quantization/fp8.py`:286; signals: fp8, gemm, moe; excerpt: "I want to disable gemm only, don't attempt to disable deephemm's MoE" (https://github.com/vllm-project/vllm/pull/38083#discussion_r2993087924)
- `2026-03-25T23:41:54Z` `issue` by `vadiklyutiy`; signals: fp4, fp8, nvfp4; excerpt: "Updated expected result and tolerance (expected=mean, tol=3 sigma) according the following results Run Qwen3.5-35B-A3B Qwen3.5-35B-A3B-FP8 Qwen3.5-397B-NVFP4 ------------- --------------- ------------------- ------------------ 0.8438 0.7998 0.8908 0.8415 ..." (https://github.com/vllm-project/vllm/pull/38083#issuecomment-4130547336)
