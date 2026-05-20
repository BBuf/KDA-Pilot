# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#10043](https://github.com/NVIDIA/TensorRT-LLM/pull/10043)
- Source page: `sources/prs/tensorrt-llm/PR-10043.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-10043`
- Generated at: `2026-05-20T15:17:34.499438+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-16T10:36:28Z`
- Merged: `2025-12-20T08:12:41Z`

## Discussion Counts

- Issue comments: 31
- Review submissions: 14 (approved=3, commented=11)
- Inline review comments: 10
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: QiJune, coderabbitai, dc3671, hyukn, kaiyux, syuoni, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-16T10:45:01Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3582451390)
- `2025-12-17T02:41:23Z` `APPROVED` by `kaiyux` - Do we have multi-gpu accuracy test using cutedsl? I'm wondering if we should include multi-gpu pipeline. (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3585778952)
- `2025-12-17T07:24:22Z` `COMMENTED` by `dc3671` (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3586359180)
- `2025-12-17T07:24:41Z` `COMMENTED` by `dc3671` (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3586359949)
- `2025-12-17T07:24:54Z` `COMMENTED` by `dc3671` (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3586360606)
- `2025-12-17T07:25:03Z` `COMMENTED` by `dc3671` (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3586361035)
- `2025-12-17T07:25:12Z` `COMMENTED` by `dc3671` (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3586361424)
- `2025-12-17T12:51:20Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3587589575)
- `2025-12-18T02:02:30Z` `APPROVED` by `hyukn` - LGTM. FYI: Currently we have noticed that some tactics with PDL enabled in Cutlass MoE might bring significant ... (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3590382361)
- `2025-12-19T01:40:29Z` `APPROVED` by `QiJune` (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3596117344)
- `2025-12-19T03:02:16Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3596554335)
- `2025-12-19T03:17:55Z` `COMMENTED` by `dc3671` (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3596607400)
- `2025-12-19T03:19:28Z` `COMMENTED` by `dc3671` (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3596612029)
- `2025-12-19T03:20:26Z` `COMMENTED` by `dc3671` (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3596613808)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`: 6 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_finalize_fusion.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_swiglu_fusion.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/dense_blockscaled_gemm_persistent.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-16T10:45:01Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, alignment, attention, bf16, blackwell, block, compile, correctness; excerpt: "Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#pullrequestreview-3582451390)
- `2025-12-16T10:44:58Z` `issue` by `coderabbitai`; signals: bf16, blackwell, block, correctness, cute, epilogue, gemm, hang; excerpt: "📝 Walkthrough Walkthrough Changes centralize DSL utility operations (fmin, sigmoid f32, silu f32, atomic add functions) into a dedicated utils module, add grid dependency ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#issuecomment-3659902228)
- `2025-12-19T03:02:15Z` `inline` by `syuoni` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:2262; signals: blackwell, block, cute, gemm, hang, kernel, tensorrt; excerpt: "Hi @dc3671 , According to the nsys timeline, early preexit causes significant interference between FC1 and FC2, resulting in longer critical path: Without PDL: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#discussion_r2633413864)
- `2025-12-19T03:17:55Z` `inline` by `dc3671` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:2262; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "What's the batch size or num tokens in your case? Probably too early for this small GEMM case and prefetches of child kernel are ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#discussion_r2633441452)
- `2025-12-17T07:24:23Z` `inline` by `dc3671` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:2262; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "griddepcontrol launch dependents() can be put just after griddepcontrol wait()" (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#discussion_r2625898108)
- `2025-12-17T07:24:41Z` `inline` by `dc3671` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm.py`:1608; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "ditto" (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#discussion_r2625898782)
- `2025-12-17T07:24:54Z` `inline` by `dc3671` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_finalize_fusion.py`:1889; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "ditto" (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#discussion_r2625899204)
- `2025-12-17T07:25:03Z` `inline` by `dc3671` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_swiglu_fusion.py`:1929; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "ditto" (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#discussion_r2625899571)
- `2025-12-17T07:25:12Z` `inline` by `dc3671` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/dense_blockscaled_gemm_persistent.py`:1480; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "ditto" (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#discussion_r2625899950)
- `2025-12-17T12:51:19Z` `inline` by `syuoni` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:2262; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "Done, thanks!" (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#discussion_r2626946615)
- `2025-12-19T03:19:28Z` `inline` by `dc3671` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:2262; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "Can you share the nsys file to me on slack?" (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#discussion_r2633446684)
- `2025-12-19T03:20:26Z` `inline` by `dc3671` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:2262; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "You can revert it for now. I'll follow this case in future PR." (https://github.com/NVIDIA/TensorRT-LLM/pull/10043#discussion_r2633447838)
