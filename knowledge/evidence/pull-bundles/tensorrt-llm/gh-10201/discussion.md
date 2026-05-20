# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#10201](https://github.com/NVIDIA/TensorRT-LLM/pull/10201)
- Source page: `sources/prs/tensorrt-llm/PR-10201.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-10201`
- Generated at: `2026-05-20T15:17:34.546959+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-22T14:13:10Z`
- Merged: `2025-12-25T14:04:20Z`

## Discussion Counts

- Issue comments: 23
- Review submissions: 16 (approved=4, commented=12)
- Inline review comments: 13
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=3
- Human participants with discussion text: coderabbitai, hyukn, liyuhannnnn, sherry-1001, syuoni, tensorrt-cicd, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-22T14:27:56Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 🧹 Nitpick comments (4) tests/unittest/ torch/thop/parallel/test cute dsl moe.py (1) 396-405: Expanded tile size ... (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3604291575)
- `2025-12-23T10:27:17Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3607474946)
- `2025-12-23T10:32:07Z` `APPROVED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3607501184)
- `2025-12-23T13:21:13Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3607891501)
- `2025-12-24T03:08:09Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3609804579)
- `2025-12-24T03:11:26Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3609807501)
- `2025-12-24T05:01:59Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3609932070)
- `2025-12-24T06:23:23Z` `COMMENTED` by `liyuhannnnn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3610046817)
- `2025-12-24T06:29:46Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3610056748)
- `2025-12-24T06:42:55Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3610076369)
- `2025-12-24T08:36:57Z` `APPROVED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3610304550)
- `2025-12-24T09:00:00Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3610371154)
- `2025-12-24T09:00:30Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3610372054)
- `2025-12-24T09:00:53Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3610372763)
- `2025-12-24T10:08:26Z` `APPROVED` by `liyuhannnnn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3610541826)
- `2025-12-24T12:06:15Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3610832196)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/autotuner.py`: 6 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`: 5 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-22T14:27:56Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, alignment, blackwell, block, correctness, cute, cutlass, dtype; excerpt: "Actionable comments posted: 0 🧹 Nitpick comments (4) tests/unittest/ torch/thop/parallel/test cute dsl moe.py (1) 396-405: Expanded tile size sweep to include 256 looks correct. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#pullrequestreview-3604291575)
- `2025-12-22T14:27:53Z` `issue` by `coderabbitai`; signals: aligned, autotune, blackwell, block, correctness, cute, dtype, epilogue; excerpt: "📝 Walkthrough Walkthrough The changes optimize custom GEMM kernel configurations by expanding tactic search space and relaxing validation constraints in the custom ops layer. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#issuecomment-3682313088)
- `2025-12-24T06:23:23Z` `inline` by `liyuhannnnn` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:286; signals: blackwell, block, cute, gemm, hang, kernel, tensorrt; excerpt: "Also changed it in PR maybe have some conflicts here." (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#discussion_r2644908025)
- `2025-12-24T12:06:15Z` `inline` by `syuoni` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_swiglu_fusion.py`:286; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "Update, thanks." (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#discussion_r2645549291)
- `2025-12-24T06:29:46Z` `inline` by `hyukn` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`:195; signals: compile, cute, moe, tensorrt; excerpt: "Sounds like a good solution to keep the code clean. Thanks for the suggestion! The torch custom op wrapper is actually not mandatory. It ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#discussion_r2644917310)
- `2025-12-24T09:00:53Z` `inline` by `syuoni` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`:276; signals: aligned, cute, moe, tensorrt; excerpt: "Offline aligned, closing." (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#discussion_r2645184404)
- `2025-12-23T10:25:52Z` `inline` by `syuoni` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`:195; signals: cute, moe, tensorrt; excerpt: "Hi @hyukn , I finally choose to implement the MoE-level autotuning logic in fused moe cute dsl.py, instead of a separate Torch operator. This ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#discussion_r2642707742)
- `2025-12-24T06:42:34Z` `inline` by `hyukn` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`:276; signals: cute, moe, tensorrt; excerpt: "Could you help me understand how this work without using capture-replay API calling during the tuning process. I found that these restrictions are applied ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#discussion_r2644937277)
- `2025-12-24T09:00:00Z` `inline` by `syuoni` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`:195; signals: cute, moe, tensorrt; excerpt: "Thanks for the confirmation. Closing." (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#discussion_r2645182873)
- `2025-12-24T09:00:29Z` `inline` by `syuoni` `tensorrt_llm/_torch/autotuner.py`:715; signals: aligned, autotune, tensorrt; excerpt: "Offline aligned with @hyukn , closing." (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#discussion_r2645183769)
- `2025-12-23T12:41:03Z` `inline` by `hyukn` `tensorrt_llm/_torch/autotuner.py`:673; signals: autotune, tensorrt; excerpt: "nits: valid comb = all(checker(pairs) for checker in runner tactic comb checkers) may be more simple." (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#discussion_r2643068672)
- `2025-12-23T12:43:26Z` `inline` by `hyukn` `tensorrt_llm/_torch/autotuner.py`:715; signals: autotune, tensorrt; excerpt: "This means we want to check if (runner, tactic) is a valid option. But I am trying to understand why invalid pairs can be ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10201#discussion_r2643074055)
