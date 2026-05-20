# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12079](https://github.com/NVIDIA/TensorRT-LLM/pull/12079)
- Source page: `sources/prs/tensorrt-llm/PR-12079.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12079`
- Generated at: `2026-05-20T15:18:04.484694+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-10T09:39:26Z`
- Merged: `2026-03-23T14:12:50Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=0
- Human participants with discussion text: coderabbitai, liyuhannnnn, sherry-1001, syuoni, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-10T09:50:34Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🧹 Nitpick comments (1) tests/scripts/cute dsl kernels/run blockscaled contiguous grouped gemm finalize fusion.py (1) ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#pullrequestreview-3921122372)
- `2026-03-17T08:53:36Z` `APPROVED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#pullrequestreview-3959093367)
- `2026-03-17T09:34:27Z` `APPROVED` by `sherry-1001` (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#pullrequestreview-3959310470)
- `2026-03-18T02:04:21Z` `COMMENTED` by `liyuhannnnn` (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#pullrequestreview-3964604373)
- `2026-03-18T02:04:37Z` `COMMENTED` by `liyuhannnnn` (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#pullrequestreview-3964604905)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm.py`: 4 inline comment(s)
- `tests/scripts/cute_dsl_kernels/run_blockscaled_contiguous_grouped_gemm_finalize_fusion.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-10T09:50:33Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm.py`:68; signals: blackwell, block, cute, cutlass, gemm, kernel, layout, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 2615 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#discussion_r2910569204)
- `2026-03-10T09:50:34Z` `review` `COMMENTED` by `coderabbitai`; signals: blackwell, block, cute, gemm, hang, kernel, tensorrt; excerpt: "Actionable comments posted: 2 🧹 Nitpick comments (1) tests/scripts/cute dsl kernels/run blockscaled contiguous grouped gemm finalize fusion.py (1) 1074-1097: Use keyword arguments for the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#pullrequestreview-3921122372)
- `2026-03-10T09:50:30Z` `issue` by `coderabbitai`; signals: blackwell, block, cute, gemm, hang, kernel, layout, moe; excerpt: "📝 Walkthrough Walkthrough The changes introduce a new raster along m scheduling parameter to the Blackwell block-scaled GEMM kernel, enabling an alternative fast-divmod-based tile ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#issuecomment-4030068574)
- `2026-03-10T09:50:33Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm.py`:90; signals: blackwell, block, cute, gemm, kernel, layout, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 602 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#discussion_r2910569221)
- `2026-03-17T09:28:49Z` `inline` by `sherry-1001` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm.py`:63; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "I’m wondering: once the newest CUTE DSL is released, do we still need this hook?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#discussion_r2945449220)
- `2026-03-18T02:04:21Z` `inline` by `liyuhannnnn` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm.py`:63; signals: blackwell, block, cute, gemm, kernel, tensorrt; excerpt: "TRTLLM still uses 4.3.4, we need it for now. Once TRTLLM switch to 4.4.x, we could remove this hook." (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#discussion_r2950440926)
- `2026-03-17T09:34:12Z` `inline` by `sherry-1001` `tests/scripts/cute_dsl_kernels/run_blockscaled_contiguous_grouped_gemm_finalize_fusion.py`:503; signals: block, cute, gemm, kernel; excerpt: "Maybe later we can remove this and only keep blkreg" (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#discussion_r2945480979)
- `2026-03-18T02:04:37Z` `inline` by `liyuhannnnn` `tests/scripts/cute_dsl_kernels/run_blockscaled_contiguous_grouped_gemm_finalize_fusion.py`:503; signals: block, cute, gemm, kernel; excerpt: "Sure." (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#discussion_r2950441503)
- `2026-03-10T14:24:43Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 38425]( [ run ] completed with state SUCCESS. Commit: a6a01d5 [/LLM/main/L0 MergeRequest PR pipeline 29786]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#issuecomment-4031794719)
- `2026-03-18T05:38:07Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 39352]( [ run ] completed with state SUCCESS. Commit: 75b1471 [/LLM/main/L0 MergeRequest PR pipeline 30596]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#issuecomment-4079885659)
- `2026-03-19T09:55:01Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 39579]( [ run ] completed with state SUCCESS. Commit: 75b1471 [/LLM/main/L0 MergeRequest PR pipeline 30792]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#issuecomment-4088992406)
- `2026-03-23T04:45:41Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 39853]( [ run ] completed with state SUCCESS. Commit: a0c42e3 [/LLM/main/L0 MergeRequest PR pipeline 31027]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12079#issuecomment-4107955296)
