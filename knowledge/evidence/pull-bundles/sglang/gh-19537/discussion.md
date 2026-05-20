# PR Discussion Digest

- Source PR: [sgl-project/sglang#19537](https://github.com/sgl-project/sglang/pull/19537)
- Source page: `sources/prs/sglang/PR-19537.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19537`
- Generated at: `2026-05-20T15:28:53.875007+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-28T02:13:37Z`
- Merged: `2026-03-10T22:37:58Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=1
- Human participants with discussion text: Fridge003, zianglih
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-10T02:21:03Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/19537#pullrequestreview-3918369785)
- `2026-03-10T02:51:30Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/19537#pullrequestreview-3919379646)
- `2026-03-10T02:54:18Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/19537#pullrequestreview-3919388503)
- `2026-03-10T02:54:34Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/19537#pullrequestreview-3919389326)
- `2026-03-10T02:54:47Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/19537#pullrequestreview-3919389972)
- `2026-03-10T22:37:49Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/19537#pullrequestreview-3925852676)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8.py`: 4 inline comment(s)
- `docs/advanced_features/server_arguments.md`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8_utils.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-10T02:51:29Z` `inline` by `zianglih` `python/sglang/srt/layers/quantization/fp8_utils.py`:294; signals: aligned, fp8, gemm; excerpt: "This API is stable. The is to stay aligned with the surrounding gemm fp8 nt groupwise raw gemm fp8 nt groupwise:" (https://github.com/sgl-project/sglang/pull/19537#discussion_r2909006828)
- `2026-03-09T23:39:04Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/fp8.py`:112; signals: fp8; excerpt: "We can lazily import this function in process mxfp8 linear weight scale" (https://github.com/sgl-project/sglang/pull/19537#discussion_r2908513841)
- `2026-03-09T23:42:12Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/fp8.py`:1508; signals: fp8; excerpt: "can we keep this comment" (https://github.com/sgl-project/sglang/pull/19537#discussion_r2908521745)
- `2026-03-10T02:20:46Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/fp8_utils.py`:294; signals: fp8; excerpt: "Is this API stable? Since it has prefix, not sure whether it will be deprecated in the future" (https://github.com/sgl-project/sglang/pull/19537#discussion_r2908905344)
- `2026-03-10T02:54:18Z` `inline` by `zianglih` `python/sglang/srt/layers/quantization/fp8.py`:112; signals: fp8; excerpt: "Done by" (https://github.com/sgl-project/sglang/pull/19537#discussion_r2909015758)
- `2026-03-10T02:54:34Z` `inline` by `zianglih` `python/sglang/srt/layers/quantization/fp8.py`:1508; signals: fp8; excerpt: "Done by" (https://github.com/sgl-project/sglang/pull/19537#discussion_r2909016633)
- `2026-03-04T00:52:43Z` `issue` by `zianglih`; signals: accuracy; excerpt: "The accuracy discrepancy between routed and non-routed backend has been eliminated by fused baseline routed BEFORE routed AFTER" (https://github.com/sgl-project/sglang/pull/19537#issuecomment-3994521286)
- `2026-03-03T04:53:36Z` `issue` by `zianglih`; signals: compile; excerpt: "Fixing a torch compile related failure" (https://github.com/sgl-project/sglang/pull/19537#issuecomment-3988656267)
- `2026-03-03T06:17:09Z` `issue` by `zianglih`; signals: cuda; excerpt: "Previous failure is fixed by This PR is now piecewise CUDA graph compatible." (https://github.com/sgl-project/sglang/pull/19537#issuecomment-3988909154)
- `2026-03-09T21:38:01Z` `inline` by `Fridge003` `docs/advanced_features/server_arguments.md`:315; signals: general review; excerpt: "Please also update this documentation" (https://github.com/sgl-project/sglang/pull/19537#discussion_r2908075756)
- `2026-03-10T02:54:47Z` `inline` by `zianglih` `docs/advanced_features/server_arguments.md`:315; signals: general review; excerpt: "Done by" (https://github.com/sgl-project/sglang/pull/19537#discussion_r2909017453)
