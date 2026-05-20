# PR Discussion Digest

- Source PR: [sgl-project/sglang#6890](https://github.com/sgl-project/sglang/pull/6890)
- Source page: `sources/prs/sglang/PR-6890.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6890`
- Generated at: `2026-05-20T15:30:54.556294+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-05T08:12:57Z`
- Merged: `2025-06-05T18:37:05Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 3 (approved=1, changes_requested=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: Alcanderian, fzyzcjy, zhyncs
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-05T08:13:18Z` `COMMENTED` by `gemini-code-assist` - Hello @fzyzcjy, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post my feedback shortly. ... (https://github.com/sgl-project/sglang/pull/6890#pullrequestreview-2899301851)
- `2025-06-05T08:14:18Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This PR aims to utilize deepgemm more broadly by adjusting the shape support checks in deepgemm ... (https://github.com/sgl-project/sglang/pull/6890#pullrequestreview-2899304629)
- `2025-06-05T18:36:57Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/6890#pullrequestreview-2901653552)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8_utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-05T14:52:44Z` `issue` by `Alcanderian`; signals: h100, perf, performance; excerpt: "We have some H100 with 500W TGP so that some performance teat failed" (https://github.com/sgl-project/sglang/pull/6890#issuecomment-2944876642)
- `2025-06-05T09:32:13Z` `issue` by `Alcanderian`; signals: aligned; excerpt: "n aligned to 64 is reasonable because n of fused qkv a proj with mqa is (1536 + 576)" (https://github.com/sgl-project/sglang/pull/6890#issuecomment-2943449246)
- `2025-06-05T09:49:01Z` `issue` by `fzyzcjy`; signals: triton; excerpt: "Yes I find it to be multiple of 64 and not 128 and thus without the PR it goes to triton" (https://github.com/sgl-project/sglang/pull/6890#issuecomment-2943501249)
- `2025-06-05T09:16:13Z` `issue` by `Alcanderian`; signals: general review; excerpt: "Oops, there are some mistakes, the correct constraint is shape supported = weight.shape[0] % 64 == 0 and weight.shape[1] % 128 == 0 ref: ..." (https://github.com/sgl-project/sglang/pull/6890#issuecomment-2943395737)
