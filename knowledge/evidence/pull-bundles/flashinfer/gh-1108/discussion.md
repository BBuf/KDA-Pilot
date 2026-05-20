# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1108](https://github.com/flashinfer-ai/flashinfer/pull/1108)
- Source page: `sources/prs/flashinfer/PR-1108.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1108`
- Generated at: `2026-05-20T15:21:43.208334+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-02T05:43:23Z`
- Merged: `2025-06-17T09:23:14Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 18
- Review threads observed: 18
- Resolved/outdated thread markers: resolved=15, outdated=15
- Human participants with discussion text: yyihuang, yzh119
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-02T17:32:47Z` `COMMENTED` by `yzh119` - Please remove all usage of packed/unpacked data type and use vec t instead. (https://github.com/flashinfer-ai/flashinfer/pull/1108#pullrequestreview-2889032818)
- `2025-06-16T06:55:08Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1108#pullrequestreview-2930828267)
- `2025-06-16T16:30:19Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1108#pullrequestreview-2932789123)
- `2025-06-17T08:42:06Z` `APPROVED` by `yzh119` - I'm good with the PR, thanks so much for your contribution! Please refer to on how to simplify ... (https://github.com/flashinfer-ai/flashinfer/pull/1108#pullrequestreview-2934717464)

## Inline Comment Hotspots

- `include/flashinfer/comm/trtllm_moe_allreduce_fusion.cuh`: 16 inline comment(s)
- `tests/test_trtllm_moe_allreduce_fusion.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-06-02T17:30:38Z` `inline` by `yzh119` `include/flashinfer/comm/trtllm_moe_allreduce_fusion.cuh`:17; signals: dtype, flashinfer, moe; excerpt: "This value should be data type dependent, we should only fix number of bytes per access (16B). and elements per access (or VEC SIZE ..." (https://github.com/flashinfer-ai/flashinfer/pull/1108#discussion_r2121764847)
- `2025-06-02T17:25:41Z` `inline` by `yzh119` `include/flashinfer/comm/trtllm_moe_allreduce_fusion.cuh`:96; signals: flashinfer, hang, moe; excerpt: "Remove all usage of Packed type and change to vec t as in 1096" (https://github.com/flashinfer-ai/flashinfer/pull/1108#discussion_r2121756660)
- `2025-06-02T17:32:26Z` `inline` by `yzh119` `include/flashinfer/comm/trtllm_moe_allreduce_fusion.cuh`:355; signals: flashinfer, moe, tile; excerpt: "vec t has load global volatile member." (https://github.com/flashinfer-ai/flashinfer/pull/1108#discussion_r2121770743)
- `2025-06-02T15:48:53Z` `inline` by `yzh119` `include/flashinfer/comm/trtllm_moe_allreduce_fusion.cuh`:24; signals: flashinfer, moe; excerpt: "Remove it." (https://github.com/flashinfer-ai/flashinfer/pull/1108#discussion_r2121565042)
- `2025-06-02T17:26:35Z` `inline` by `yzh119` `include/flashinfer/comm/trtllm_moe_allreduce_fusion.cuh`:97; signals: flashinfer, moe; excerpt: "This function should be equivalent to vec add" (https://github.com/flashinfer-ai/flashinfer/pull/1108#discussion_r2121758104)
- `2025-06-02T17:26:49Z` `inline` by `yzh119` `include/flashinfer/comm/trtllm_moe_allreduce_fusion.cuh`:98; signals: flashinfer, moe; excerpt: "MathCount is VEC SIZE" (https://github.com/flashinfer-ai/flashinfer/pull/1108#discussion_r2121758549)
- `2025-06-02T17:27:13Z` `inline` by `yzh119` `include/flashinfer/comm/trtllm_moe_allreduce_fusion.cuh`:155; signals: flashinfer, moe; excerpt: "Use vec t.store instead" (https://github.com/flashinfer-ai/flashinfer/pull/1108#discussion_r2121759195)
- `2025-06-02T17:27:47Z` `inline` by `yzh119` `include/flashinfer/comm/trtllm_moe_allreduce_fusion.cuh`:171; signals: flashinfer, moe; excerpt: "Use neg zero defined in 1096" (https://github.com/flashinfer-ai/flashinfer/pull/1108#discussion_r2121759971)
- `2025-06-02T17:28:05Z` `inline` by `yzh119` `include/flashinfer/comm/trtllm_moe_allreduce_fusion.cuh`:875; signals: flashinfer, moe; excerpt: "The value can be obtained at python side (or let user specify)" (https://github.com/flashinfer-ai/flashinfer/pull/1108#discussion_r2121760454)
- `2025-06-02T17:31:19Z` `inline` by `yzh119` `include/flashinfer/comm/trtllm_moe_allreduce_fusion.cuh`:419; signals: flashinfer, moe; excerpt: "use argument value passed from python." (https://github.com/flashinfer-ai/flashinfer/pull/1108#discussion_r2121766460)
- `2025-06-16T06:49:58Z` `inline` by `yzh119` `include/flashinfer/comm/trtllm_moe_allreduce_fusion.cuh`:28; signals: flashinfer, moe; excerpt: "These utils should be unified to vec t in 1142 , but let's keep them in this PR." (https://github.com/flashinfer-ai/flashinfer/pull/1108#discussion_r2149170769)
- `2025-06-16T06:50:37Z` `inline` by `yzh119` `include/flashinfer/comm/trtllm_moe_allreduce_fusion.cuh`:1130; signals: flashinfer, moe; excerpt: "Write dispatcher for these repetitive patterns." (https://github.com/flashinfer-ai/flashinfer/pull/1108#discussion_r2149171757)
