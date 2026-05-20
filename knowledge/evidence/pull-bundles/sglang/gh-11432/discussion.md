# PR Discussion Digest

- Source PR: [sgl-project/sglang#11432](https://github.com/sgl-project/sglang/pull/11432)
- Source page: `sources/prs/sglang/PR-11432.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-11432`
- Generated at: `2026-05-20T15:27:23.463795+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-10T15:09:59Z`
- Merged: `2025-10-13T03:19:21Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 9
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: BBuf, zhyncs
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-10T15:13:03Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces "Expert Specialization" for grouped GEMM to enhance performance, particularly for unbalanced workloads ... (https://github.com/sgl-project/sglang/pull/11432#pullrequestreview-3324201216)
- `2025-10-11T15:51:10Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/11432#pullrequestreview-3327369589)
- `2025-10-11T15:57:18Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/11432#pullrequestreview-3327377221)
- `2025-10-11T15:58:36Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/11432#pullrequestreview-3327377863)
- `2025-10-11T15:59:00Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/11432#pullrequestreview-3327377970)
- `2025-10-12T05:31:03Z` `APPROVED` by `zhyncs` - Overall LGTM, we just need to address @BBuf's review comment (https://github.com/sgl-project/sglang/pull/11432#pullrequestreview-3327901327)

## Inline Comment Hotspots

- `sgl-kernel/csrc/expert_specialization/es_fp8_blockwise_launcher.cuh`: 4 inline comment(s)
- `sgl-kernel/csrc/expert_specialization/es_fp8_blockwise.cu`: 2 inline comment(s)
- `sgl-kernel/csrc/common_extension.cc`: 1 inline comment(s)
- `sgl-kernel/python/sgl_kernel/expert_specilization.py`: 1 inline comment(s)
- `sgl-kernel/python/sgl_kernel/__init__.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-11T15:51:10Z` `inline` by `BBuf` `sgl-kernel/csrc/expert_specialization/es_fp8_blockwise_launcher.cuh`:54; signals: block, fp8, kernel; excerpt: "Maybe we can simplify replicate code here -" (https://github.com/sgl-project/sglang/pull/11432#discussion_r2422975598)
- `2025-10-11T15:57:18Z` `inline` by `BBuf` `sgl-kernel/csrc/expert_specialization/es_fp8_blockwise_launcher.cuh`:224; signals: block, fp8, kernel; excerpt: "Better create a tool func in sglang/sgl-kernel/include/utils.h ." (https://github.com/sgl-project/sglang/pull/11432#discussion_r2422981873)
- `2025-10-11T15:58:36Z` `inline` by `BBuf` `sgl-kernel/python/sgl_kernel/expert_specilization.py`:1; signals: kernel; excerpt: "File name should be expert specialization.py?" (https://github.com/sgl-project/sglang/pull/11432#discussion_r2422982599)
