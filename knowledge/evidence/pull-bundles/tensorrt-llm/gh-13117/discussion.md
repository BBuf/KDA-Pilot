# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13117](https://github.com/NVIDIA/TensorRT-LLM/pull/13117)
- Source page: `sources/prs/tensorrt-llm/PR-13117.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13117`
- Generated at: `2026-05-20T15:18:31.333070+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-16T08:06:48Z`
- Merged: `2026-04-24T09:27:36Z`

## Discussion Counts

- Issue comments: 32
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=0
- Human participants with discussion text: Tracin, coderabbitai, hyukn, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-16T08:15:57Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 🧹 Nitpick comments (2) tests/unittest/ torch/thop/parallel/test arcquant fp4.py (1) 9-40: Add return type annotations ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#pullrequestreview-4119284139)
- `2026-04-24T09:24:27Z` `APPROVED` by `hyukn` - LGTM. (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#pullrequestreview-4169385436)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/thop/fp4Quantize.cpp`: 2 inline comment(s)
- `cpp/tensorrt_llm/thop/fp4Quantize.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-16T08:15:53Z` `issue` by `coderabbitai`; signals: alignment, benchmark, bf16, block, correctness, cuda, dtype, fp4; excerpt: "📝 Walkthrough Walkthrough This PR adds a new ARCQuant FP4 quantization kernel nvfp4 quantize residual with block size with block-based residual computation support. The ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#issuecomment-4258433186)
- `2026-04-16T08:15:57Z` `review` `COMMENTED` by `coderabbitai`; signals: fp4, hang, kernel, layout, tensorrt; excerpt: "Actionable comments posted: 3 🧹 Nitpick comments (2) tests/unittest/ torch/thop/parallel/test arcquant fp4.py (1) 9-40: Add return type annotations to the new helpers. These utilities ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#pullrequestreview-4119284139)
- `2026-04-16T08:15:56Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/fp4Quantize.cpp`:328; signals: block, dtype, fp4, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Validate the new public op inputs before launching the kernel. fp4 quantize with residual only dtype-checks input scale, and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#discussion_r3091702320)
- `2026-04-16T08:15:56Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/fp4Quantize.cpp`:314; signals: fp4, hang, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Update the modified-file copyright year. This source file now contains 2026 changes, but the NVIDIA copyright line still ends ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#discussion_r3091702336)
- `2026-04-16T08:15:56Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/fp4Quantize.h`:40; signals: fp4, hang, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Update the modified-file copyright year. This header was changed in 2026, but the NVIDIA copyright line still ends at ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#discussion_r3091702344)
- `2026-04-16T10:04:22Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 43721]( [ run ] completed with state FAILURE. Commit: aa78617 [/LLM/main/L0 MergeRequest PR pipeline 34204]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#issuecomment-4259155314)
- `2026-04-17T02:38:02Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 43886]( [ run ] completed with state FAILURE. Commit: 5f971f0 [/LLM/main/L0 MergeRequest PR pipeline 34338]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#issuecomment-4264904847)
- `2026-04-20T03:47:58Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 44265]( [ run ] completed with state FAILURE. Commit: f430438 [/LLM/main/L0 MergeRequest PR pipeline 34688]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#issuecomment-4277695852)
- `2026-04-20T05:59:19Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 44323]( [ run ] completed with state FAILURE. Commit: f430438 [/LLM/main/L0 MergeRequest PR pipeline 34746]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#issuecomment-4278225870)
- `2026-04-20T11:10:12Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 44397]( [ run ] completed with state FAILURE. Commit: f430438 [/LLM/main/L0 MergeRequest PR pipeline 34814]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#issuecomment-4280123510)
- `2026-04-21T12:32:00Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 44660]( [ run ] completed with state SUCCESS. Commit: e454c56 [/LLM/main/L0 MergeRequest PR pipeline 35034]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#issuecomment-4288540880)
- `2026-04-22T11:29:39Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 44899]( [ run ] completed with state SUCCESS. Commit: e454c56 [/LLM/main/L0 MergeRequest PR pipeline 35234]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13117#issuecomment-4295789229)
