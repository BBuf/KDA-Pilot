# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#10987](https://github.com/NVIDIA/TensorRT-LLM/pull/10987)
- Source page: `sources/prs/tensorrt-llm/PR-10987.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-10987`
- Generated at: `2026-05-20T15:17:39.916910+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-26T04:37:05Z`
- Merged: `2026-01-27T08:15:32Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 8 (approved=3, commented=5)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: coderabbitai, hyukn, kaiyux, liyuhannnnn, sherry-1001, syuoni, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-26T04:44:00Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Fix all issues with AI agents (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#pullrequestreview-3704627259)
- `2026-01-26T05:00:12Z` `COMMENTED` by `liyuhannnnn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#pullrequestreview-3704643625)
- `2026-01-26T05:18:05Z` `APPROVED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#pullrequestreview-3704665372)
- `2026-01-26T05:33:59Z` `APPROVED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#pullrequestreview-3704684238)
- `2026-01-26T09:03:49Z` `APPROVED` by `liyuhannnnn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#pullrequestreview-3705142895)
- `2026-01-27T03:29:02Z` `COMMENTED` by `sherry-1001` (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#pullrequestreview-3708933910)
- `2026-01-27T06:48:10Z` `COMMENTED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#pullrequestreview-3709397953)
- `2026-01-27T08:08:27Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#pullrequestreview-3709682217)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_finalize_fusion.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-26T04:43:59Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_finalize_fusion.py`:547; signals: blackwell, block, cute, dtype, gemm, kernel, layout, memory; excerpt: "⚠️ Potential issue 🟠 Major Fix shared‑memory sizing mismatch for blkred C staging (FP32 risk). c smem layout staged uses cta tile shape mnk[1] ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#discussion_r2726335880)
- `2026-01-26T04:43:56Z` `issue` by `coderabbitai`; signals: bf16, blackwell, block, cuda, cute, epilogue, gemm, hang; excerpt: "📝 Walkthrough Walkthrough A block-reduction (blkred) code path is introduced to a GEMM kernel, controlled by a new use blkred parameter. Changes include extended ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#issuecomment-3797881162)
- `2026-01-26T05:00:12Z` `inline` by `liyuhannnnn` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_finalize_fusion.py`:546; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "Unuseful code?" (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#discussion_r2726353653)
- `2026-01-27T03:29:01Z` `inline` by `sherry-1001` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:1308; signals: autotune, cache, cute, tensorrt; excerpt: "use blkred is false by default, and here I set it to always on. Is cache key used as an option for the autotuner?" (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#discussion_r2730090074)
- `2026-01-27T06:48:10Z` `inline` by `syuoni` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:1308; signals: autotune, cache, cute, tensorrt; excerpt: "Yes, it's mainly for autotuner. Currently, we only use use blkred=True in the PyTorch operator, so I suppose it's OK to not include it ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#discussion_r2730508513)
- `2026-01-26T05:32:20Z` `inline` by `hyukn` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:1308; signals: cache, cute, tensorrt; excerpt: "Do we need to put it into cache key, or is it guaranteed to be True?" (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#discussion_r2726392346)
- `2026-01-27T08:08:27Z` `inline` by `hyukn` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:1308; signals: cute, tensorrt; excerpt: "Make sense to me. Thanks" (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#discussion_r2730750891)
- `2026-01-26T04:44:00Z` `review` `COMMENTED` by `coderabbitai`; signals: general review; excerpt: "Actionable comments posted: 1 🤖 Fix all issues with AI agents" (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#pullrequestreview-3704627259)
- `2026-01-26T06:51:01Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 33528]( [ run ] completed with state SUCCESS. Commit: 18de6bf [/LLM/main/L0 MergeRequest PR pipeline 25864]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#issuecomment-3798125811)
- `2026-01-26T17:07:11Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 33612]( [ run ] completed with state SUCCESS. Commit: 18de6bf [/LLM/main/L0 MergeRequest PR pipeline 25930]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#issuecomment-3800684751)
- `2026-01-27T07:57:57Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 33673]( [ run ] completed with state SUCCESS. Commit: 731d020 [/LLM/main/L0 MergeRequest PR pipeline 25977]( completed with status: 'SUCCESS'" (https://github.com/NVIDIA/TensorRT-LLM/pull/10987#issuecomment-3803669934)
