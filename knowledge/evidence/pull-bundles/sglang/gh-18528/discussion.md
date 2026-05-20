# PR Discussion Digest

- Source PR: [sgl-project/sglang#18528](https://github.com/sgl-project/sglang/pull/18528)
- Source page: `sources/prs/sglang/PR-18528.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18528`
- Generated at: `2026-05-20T15:28:39.898621+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-10T08:39:23Z`
- Merged: `2026-02-11T07:23:48Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 4 (approved=1, changes_requested=1, commented=2)
- Inline review comments: 6
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=4
- Human participants with discussion text: 1am9trash, HaiShaw
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-10T08:45:26Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request integrates an FP8 prefill attention kernel to improve performance, controlled by the SGLANG ... (https://github.com/sgl-project/sglang/pull/18528#pullrequestreview-3777550268)
- `2026-02-10T09:01:58Z` `CHANGES_REQUESTED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/18528#pullrequestreview-3777636517)
- `2026-02-10T14:14:34Z` `COMMENTED` by `1am9trash` (https://github.com/sgl-project/sglang/pull/18528#pullrequestreview-3779242368)
- `2026-02-11T07:22:02Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/18528#pullrequestreview-3783223177)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/aiter_backend.py`: 6 inline comment(s)

## High-Signal Discussion

- `2026-02-10T14:14:34Z` `inline` by `1am9trash` `python/sglang/srt/layers/attention/aiter_backend.py`:1192; signals: accuracy, attention, fp8, kernel; excerpt: "The kernel is only supported on MI355, so the FP8 prefill flag is now gated as follows: Additionally, the .clamp(fp min, fp max) operation ..." (https://github.com/sgl-project/sglang/pull/18528#discussion_r2788216396)
- `2026-02-10T09:01:38Z` `inline` by `HaiShaw` `python/sglang/srt/layers/attention/aiter_backend.py`:1192; signals: attention, fp8, kernel; excerpt: "448.0 applies to gfx950 (fp8 e4m3fn), use 224.0 for gfx942 (fp8 e4m3fnuz), also check kernel for gfx942" (https://github.com/sgl-project/sglang/pull/18528#discussion_r2786690597)
