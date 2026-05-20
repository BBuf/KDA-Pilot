# PR Discussion Digest

- Source PR: [sgl-project/sglang#22722](https://github.com/sgl-project/sglang/pull/22722)
- Source page: `sources/prs/sglang/PR-22722.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22722`
- Generated at: `2026-05-20T15:29:30.799023+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-13T18:33:36Z`
- Merged: `2026-04-14T07:30:12Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 2 (approved=1, changes_requested=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: HaiShaw, michaelzhang-ai
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-14T00:24:43Z` `CHANGES_REQUESTED` by `HaiShaw` - @michaelzhang-ai Please not to accurate mi35x tests for the model not on mxfp4 for now, keep the test ... (https://github.com/sgl-project/sglang/pull/22722#pullrequestreview-4102665583)
- `2026-04-14T03:33:11Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/22722#pullrequestreview-4103195275)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-04-14T00:24:43Z` `review` `CHANGES_REQUESTED` by `HaiShaw`; signals: fp4, hang, mxfp4; excerpt: "@michaelzhang-ai Please not to accurate mi35x tests for the model not on mxfp4 for now, keep the test cases is fine, just not to ..." (https://github.com/sgl-project/sglang/pull/22722#pullrequestreview-4102665583)
- `2026-04-14T02:14:35Z` `issue` by `michaelzhang-ai`; signals: fp4, hang, mxfp4; excerpt: "@michaelzhang-ai Please not to accurate mi35x tests for the model not on mxfp4 for now, keep the test cases is fine, just not to ..." (https://github.com/sgl-project/sglang/pull/22722#issuecomment-4240873150)
- `2026-04-13T19:31:53Z` `issue` by `michaelzhang-ai`; signals: hang; excerpt: "CI Runs v2 (with import fix + M2.5 replaced by M2.7) Root cause of v1 failure: minimax m2.py imported get bool env var from ..." (https://github.com/sgl-project/sglang/pull/22722#issuecomment-4239094786)
- `2026-04-14T02:55:38Z` `issue` by `michaelzhang-ai`; signals: kernel; excerpt: "Re: revert of get bool env var import fix @HaiShaw The import fix for minimax m2.py is necessary — get bool env var is ..." (https://github.com/sgl-project/sglang/pull/22722#issuecomment-4241010259)
- `2026-04-13T18:36:47Z` `issue` by `michaelzhang-ai`; signals: general review; excerpt: "CI Runs Triggered - Default ROCm : - Jobs: nightly-8-gpu-minimax-m27, nightly-8-gpu-mi35x-minimax-m27 - ROCm 7.2 : - Jobs: nightly-8-gpu-minimax-m27-rocm720, nightly-8-gpu-mi35x-minimax-m27-rocm720" (https://github.com/sgl-project/sglang/pull/22722#issuecomment-4238746700)
