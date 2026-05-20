# PR Discussion Digest

- Source PR: [sgl-project/sglang#17499](https://github.com/sgl-project/sglang/pull/17499)
- Source page: `sources/prs/sglang/PR-17499.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-17499`
- Generated at: `2026-05-20T15:28:29.143583+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-21T12:38:24Z`
- Merged: `2026-01-28T19:36:31Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 2 (commented=2)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: yeahdongcn
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-21T12:41:43Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces comprehensive support for MUSA (Meta-computing Unified System Architecture) GPUs across SGLang's distributed ... (https://github.com/sgl-project/sglang/pull/17499#pullrequestreview-3687041219)
- `2026-01-23T07:29:59Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/17499#pullrequestreview-3696057948)

## Inline Comment Hotspots

- `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`: 2 inline comment(s)
- `python/sglang/srt/distributed/device_communicators/cuda_wrapper.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-23T07:25:56Z` `inline` by `yeahdongcn` `python/sglang/srt/distributed/device_communicators/cuda_wrapper.py`:116; signals: cuda, hang; excerpt: "It may be more straightforward to use "libcudart" if not is musa else "libmusart" and keep the existing assertion unchanged." (https://github.com/sgl-project/sglang/pull/17499#discussion_r2719937237)
- `2026-01-23T07:26:23Z` `inline` by `yeahdongcn` `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`:58; signals: general review; excerpt: "Should this be 128MB?" (https://github.com/sgl-project/sglang/pull/17499#discussion_r2719938425)
