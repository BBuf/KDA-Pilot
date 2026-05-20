# PR Discussion Digest

- Source PR: [sgl-project/sglang#20214](https://github.com/sgl-project/sglang/pull/20214)
- Source page: `sources/prs/sglang/PR-20214.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-20214`
- Generated at: `2026-05-20T15:29:00.814737+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-09T23:16:42Z`
- Merged: `2026-03-22T18:17:02Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: Fridge003, zianglih
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-15T05:19:06Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/20214#pullrequestreview-3949714030)
- `2026-03-17T22:36:11Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/20214#pullrequestreview-3963995090)
- `2026-03-18T07:25:14Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/20214#pullrequestreview-3965633834)
- `2026-03-18T07:25:18Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/20214#pullrequestreview-3965634206)
- `2026-03-22T18:16:21Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/20214#pullrequestreview-3988407369)

## Inline Comment Hotspots

- `test/registered/rl/test_update_weights_from_disk_mxfp8.py`: 3 inline comment(s)
- `test/registered/rl/test_update_weights_blackwell.py`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/unquant.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-18T07:34:14Z` `issue` by `zianglih`; signals: blackwell, fp4, fp8, layout, mxfp4, nvfp4; excerpt: "I have renamed test update weights blackwell.py to test update weights from disk mxfp8.py and only test /update weights from disk, as it does ..." (https://github.com/sgl-project/sglang/pull/20214#issuecomment-4080336445)
- `2026-03-15T05:19:07Z` `inline` by `zianglih` `test/registered/rl/test_update_weights_from_disk_mxfp8.py`; signals: blackwell, fp8, register; excerpt: "We want a dedicated blackwell test file because mxfp/nvfp data types usually requires an extra weight swizzling step after weight update. We want a ..." (https://github.com/sgl-project/sglang/pull/20214#discussion_r2936273126)
- `2026-03-17T22:05:25Z` `inline` by `Fridge003` `test/registered/rl/test_update_weights_blackwell.py`:3; signals: blackwell, register; excerpt: "Maybe move it to stage-c-test. stage-b-test needs to be lightweight" (https://github.com/sgl-project/sglang/pull/20214#discussion_r2949791091)
- `2026-03-17T22:06:29Z` `inline` by `Fridge003` `test/registered/rl/test_update_weights_from_disk_mxfp8.py`:4; signals: fp8, register; excerpt: "Can we prune this test to maybe 200 seconds? 500 second is a little long" (https://github.com/sgl-project/sglang/pull/20214#discussion_r2949794856)
- `2026-03-18T07:25:14Z` `inline` by `zianglih` `test/registered/rl/test_update_weights_blackwell.py`:3; signals: blackwell, register; excerpt: "Done by" (https://github.com/sgl-project/sglang/pull/20214#discussion_r2951433368)
- `2026-03-18T07:25:18Z` `inline` by `zianglih` `test/registered/rl/test_update_weights_from_disk_mxfp8.py`:4; signals: fp8, register; excerpt: "Done by" (https://github.com/sgl-project/sglang/pull/20214#discussion_r2951433694)
