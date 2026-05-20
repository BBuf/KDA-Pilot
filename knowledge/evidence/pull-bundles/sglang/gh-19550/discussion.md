# PR Discussion Digest

- Source PR: [sgl-project/sglang#19550](https://github.com/sgl-project/sglang/pull/19550)
- Source page: `sources/prs/sglang/PR-19550.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19550`
- Generated at: `2026-05-20T15:28:53.882705+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-28T07:08:20Z`
- Merged: `2026-03-05T03:50:56Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: HaiShaw, haohui, hubertlu-tw
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-04T00:53:38Z` `APPROVED` by `hubertlu-tw` - I previously added the triton path for AMD GPUs. I believe we lost AMD CI registration for AWQ ... (https://github.com/sgl-project/sglang/pull/19550#pullrequestreview-3886124520)
- `2026-03-04T04:50:44Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/19550#pullrequestreview-3886673694)
- `2026-03-04T09:04:55Z` `COMMENTED` by `haohui` (https://github.com/sgl-project/sglang/pull/19550#pullrequestreview-3888066345)

## Inline Comment Hotspots

- `docs/advanced_features/quantization.md`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-04T04:50:17Z` `inline` by `HaiShaw` `docs/advanced_features/quantization.md`:42; signals: fp4, nvfp4; excerpt: "petit nvfp4 This shall work on AMD (Dense Layer only). cc @haohui" (https://github.com/sgl-project/sglang/pull/19550#discussion_r2881783782)
- `2026-03-04T09:04:55Z` `inline` by `haohui` `docs/advanced_features/quantization.md`:42; signals: fp4, mxfp4; excerpt: "FYI adds the support of mxfp4 on dense layer" (https://github.com/sgl-project/sglang/pull/19550#discussion_r2882619984)
- `2026-03-04T00:53:38Z` `review` `APPROVED` by `hubertlu-tw`; signals: triton; excerpt: "I previously added the triton path for AMD GPUs. I believe we lost AMD CI registration for AWQ functionality during the overhaul of SGLang ..." (https://github.com/sgl-project/sglang/pull/19550#pullrequestreview-3886124520)
