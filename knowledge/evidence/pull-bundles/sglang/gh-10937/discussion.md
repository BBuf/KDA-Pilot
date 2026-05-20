# PR Discussion Digest

- Source PR: [sgl-project/sglang#10937](https://github.com/sgl-project/sglang/pull/10937)
- Source page: `sources/prs/sglang/PR-10937.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-10937`
- Generated at: `2026-05-20T15:27:21.842365+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-26T03:25:56Z`
- Merged: `2025-10-08T07:54:20Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 6 (approved=2, changes_requested=1, commented=3)
- Inline review comments: 7
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: Swipe4057, cicirori, lifuhuang, zhyncs
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-26T03:27:53Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for MHA prefill with FlashAttention 4 by removing assertions that previously ... (https://github.com/sgl-project/sglang/pull/10937#pullrequestreview-3270019806)
- `2025-09-26T04:17:48Z` `COMMENTED` by `lifuhuang` (https://github.com/sgl-project/sglang/pull/10937#pullrequestreview-3270083255)
- `2025-09-26T05:04:25Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/10937#pullrequestreview-3270152173)
- `2025-09-26T07:33:42Z` `COMMENTED` by `lifuhuang` (https://github.com/sgl-project/sglang/pull/10937#pullrequestreview-3270588812)
- `2025-10-07T04:16:46Z` `CHANGES_REQUESTED` by `zhyncs` - @lifuhuang can u upgrade sgl-kernel v0.3.15 in this pr (https://github.com/sgl-project/sglang/pull/10937#pullrequestreview-3308273833)
- `2025-10-08T07:54:05Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/10937#pullrequestreview-3313469241)

## Inline Comment Hotspots

- `python/sglang/srt/model_executor/model_runner.py`: 2 inline comment(s)
- `python/sglang/srt/server_args.py`: 2 inline comment(s)
- `sgl-kernel/python/sgl_kernel/flash_attn.py`: 2 inline comment(s)
- `python/sglang/srt/utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-01T20:01:20Z` `issue` by `cicirori`; signals: blackwell, h100, h200, sm100, sm90; excerpt: "The H100-H200 series is not supported by FA4, right? It was restricted to sm100 because of we only tested this on blackwell primary optimization ..." (https://github.com/sgl-project/sglang/pull/10937#issuecomment-3357931686)
- `2025-10-07T04:16:46Z` `review` `CHANGES_REQUESTED` by `zhyncs`; signals: kernel; excerpt: "@lifuhuang can u upgrade sgl-kernel v0.3.15 in this pr" (https://github.com/sgl-project/sglang/pull/10937#pullrequestreview-3308273833)
- `2025-09-27T05:55:58Z` `issue` by `Swipe4057`; signals: h100, h200; excerpt: "The H100-H200 series is not supported by FA4, right?" (https://github.com/sgl-project/sglang/pull/10937#issuecomment-3341284988)
- `2025-09-26T04:17:48Z` `inline` by `lifuhuang` `sgl-kernel/python/sgl_kernel/flash_attn.py`:158; signals: kernel; excerpt: "TODO: Need to check in first and bump up sgl-kernel." (https://github.com/sgl-project/sglang/pull/10937#discussion_r2380817915)
- `2025-09-26T07:33:42Z` `inline` by `lifuhuang` `sgl-kernel/python/sgl_kernel/flash_attn.py`:158; signals: kernel; excerpt: "waiting for to merge first." (https://github.com/sgl-project/sglang/pull/10937#discussion_r2381180140)
- `2025-10-08T04:16:43Z` `issue` by `lifuhuang`; signals: kernel; excerpt: "@lifuhuang can u upgrade sgl-kernel v0.3.15 in this pr done" (https://github.com/sgl-project/sglang/pull/10937#issuecomment-3379504723)
