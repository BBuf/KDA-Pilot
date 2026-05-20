# PR Discussion Digest

- Source PR: [vllm-project/vllm#18564](https://github.com/vllm-project/vllm/pull/18564)
- Source page: `sources/prs/vllm/PR-18564.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-18564`
- Generated at: `2026-05-20T15:35:21.077101+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-22T20:09:42Z`
- Merged: `2025-06-04T14:48:45Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: IwakuraRein, mgoin
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-05-28T23:40:47Z` `COMMENTED` by `mgoin` - The heuristics are fairly difficult to read now due to separating the tile scalars from the MmaTileShape, but ... (https://github.com/vllm-project/vllm/pull/18564#pullrequestreview-2876698872)
- `2025-06-04T14:44:48Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/18564#pullrequestreview-2897059689)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-05-28T23:40:47Z` `review` `COMMENTED` by `mgoin`; signals: accuracy, hang, sm100, tile; excerpt: "The heuristics are fairly difficult to read now due to separating the tile scalars from the MmaTileShape, but overall these changes seem reasonable. Could ..." (https://github.com/vllm-project/vllm/pull/18564#pullrequestreview-2876698872)
- `2025-05-28T23:06:18Z` `issue` by `mgoin`; signals: block, cutlass, fp8, sm100; excerpt: "Thanks @IwakuraRein, should be separate as it only touches scaled mm sm100 fp8 dispatch.cuh, not the blockwise fp8 path. Would appreciate help tuning for ..." (https://github.com/vllm-project/vllm/pull/18564#issuecomment-2917808143)
- `2025-05-30T00:09:14Z` `issue` by `IwakuraRein`; signals: block, fp8, kernel, triton; excerpt: "@mgoin Hi. I have run the tests on following problem shapes and compared to the triton kernel triton fp8 fp8 fp16 scaled mm blockwise. ..." (https://github.com/vllm-project/vllm/pull/18564#issuecomment-2920854242)
