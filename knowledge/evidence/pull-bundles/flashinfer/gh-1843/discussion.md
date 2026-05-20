# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1843](https://github.com/flashinfer-ai/flashinfer/pull/1843)
- Source page: `sources/prs/flashinfer/PR-1843.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1843`
- Generated at: `2026-05-20T15:23:31.581293+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-02T01:33:41Z`
- Merged: `2025-10-03T23:12:18Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: happierpig, yzh119
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-02T01:35:47Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new warp-level persistent RMSNorm kernel (qk rmsnorm) optimized for QK normalization. ... (https://github.com/flashinfer-ai/flashinfer/pull/1843#pullrequestreview-3291792009)
- `2025-10-02T04:10:36Z` `COMMENTED` by `yzh119` - Do not support non-contiguous layout on the middle dimension Can you explain more? (https://github.com/flashinfer-ai/flashinfer/pull/1843#pullrequestreview-3292110134)
- `2025-10-02T05:48:39Z` `COMMENTED` by `happierpig` (https://github.com/flashinfer-ai/flashinfer/pull/1843#pullrequestreview-3292522788)
- `2025-10-02T06:06:34Z` `COMMENTED` by `yzh119` - So functionality-wise it should be a extension to the original rmsnorm API right? We support non-contiguous layout because ... (https://github.com/flashinfer-ai/flashinfer/pull/1843#pullrequestreview-3292592295)
- `2025-10-03T02:56:46Z` `COMMENTED` by `yzh119` - IMO this warp-level persistent version has less parallelism in hidden dim dim, which may fail short on normal ... (https://github.com/flashinfer-ai/flashinfer/pull/1843#pullrequestreview-3297174499)
- `2025-10-03T22:28:13Z` `APPROVED` by `yzh119` - LGTM (https://github.com/flashinfer-ai/flashinfer/pull/1843#pullrequestreview-3301180923)

## Inline Comment Hotspots

- `flashinfer/norm.py`: 2 inline comment(s)
- `csrc/flashinfer_norm_binding.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-02T06:06:34Z` `review` `COMMENTED` by `yzh119`; signals: kernel, layout; excerpt: "So functionality-wise it should be a extension to the original rmsnorm API right? We support non-contiguous layout because we passed the strides to the ..." (https://github.com/flashinfer-ai/flashinfer/pull/1843#pullrequestreview-3292592295)
- `2025-10-03T02:56:46Z` `review` `COMMENTED` by `yzh119`; signals: warp; excerpt: "IMO this warp-level persistent version has less parallelism in hidden dim dim, which may fail short on normal RMSNorm cases (i.e., [batch size, m ..." (https://github.com/flashinfer-ai/flashinfer/pull/1843#pullrequestreview-3297174499)
- `2025-10-02T04:10:36Z` `review` `COMMENTED` by `yzh119`; signals: layout; excerpt: "Do not support non-contiguous layout on the middle dimension Can you explain more?" (https://github.com/flashinfer-ai/flashinfer/pull/1843#pullrequestreview-3292110134)
- `2025-10-02T05:47:50Z` `issue` by `happierpig`; signals: layout, perf; excerpt: "Do not support non-contiguous layout on the middle dimension Can you explain more? Here is a detailed motivation example: When serivng Qwen3-8B, there is ..." (https://github.com/flashinfer-ai/flashinfer/pull/1843#issuecomment-3359231593)
- `2025-10-02T06:20:06Z` `issue` by `happierpig`; signals: kernel, layout; excerpt: "So functionality-wise it should be a extension to the original rmsnorm API right? We support non-contiguous layout because we passed the strides to the ..." (https://github.com/flashinfer-ai/flashinfer/pull/1843#issuecomment-3359323291)
- `2025-10-02T16:07:13Z` `issue` by `happierpig`; signals: kernel, warp; excerpt: "Original APi doesn't support this kind of non-contiguous. As there is only one stride (stride input) in the original API, [batch size, :num heads, ..." (https://github.com/flashinfer-ai/flashinfer/pull/1843#issuecomment-3362011424)
- `2025-10-02T04:09:59Z` `inline` by `yzh119` `csrc/flashinfer_norm_binding.cu`:22; signals: flashinfer; excerpt: "why do we need a new API for this?" (https://github.com/flashinfer-ai/flashinfer/pull/1843#discussion_r2396674484)
- `2025-10-02T05:48:39Z` `inline` by `happierpig` `csrc/flashinfer_norm_binding.cu`:22; signals: flashinfer; excerpt: "I see. We can keep the rmsnorm API, and dispatch to the persistent version if input.dim() == 3" (https://github.com/flashinfer-ai/flashinfer/pull/1843#discussion_r2397055015)
- `2025-10-02T07:03:07Z` `issue` by `yzh119`; signals: kernel; excerpt: "Original APi doesn't support this kind of non-contiguous. As there is only one stride (stride input) in the original API, [batch size, :num heads, ..." (https://github.com/flashinfer-ai/flashinfer/pull/1843#issuecomment-3359473905)
