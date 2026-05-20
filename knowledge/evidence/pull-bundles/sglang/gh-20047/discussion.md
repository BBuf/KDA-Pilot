# PR Discussion Digest

- Source PR: [sgl-project/sglang#20047](https://github.com/sgl-project/sglang/pull/20047)
- Source page: `sources/prs/sglang/PR-20047.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-20047`
- Generated at: `2026-05-20T15:28:59.154392+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-06T16:52:21Z`
- Merged: `2026-03-09T21:13:08Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: Fridge003, b8zhong, mratsim, voipmonitor
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-03-06T16:56:33Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request changes the default FP4 GEMM backend to auto to address a NaN issue ... (https://github.com/sgl-project/sglang/pull/20047#pullrequestreview-3904884030)
- `2026-03-06T17:35:46Z` `COMMENTED` by `b8zhong` - @Fridge003 , since do you still think this PR is hacky to set it to auto? Because, it ... (https://github.com/sgl-project/sglang/pull/20047#pullrequestreview-3905066149)
- `2026-03-09T20:29:03Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/20047#pullrequestreview-3918035766)
- `2026-03-09T20:31:47Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/20047#pullrequestreview-3918048062)
- `2026-03-09T21:12:06Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/20047#pullrequestreview-3918244370)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp4_utils.py`: 2 inline comment(s)
- `python/sglang/srt/server_args.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-07T01:32:31Z` `issue` by `voipmonitor`; signals: compile, cutlass, flashinfer, nan, race, sm100, sm120; excerpt: "Root cause found — FlashInfer missing GDC compile flags The NaN crash is caused by missing -DCUTLASS ENABLE GDC FOR SM100=1 compile flags in ..." (https://github.com/sgl-project/sglang/pull/20047#issuecomment-4015155562)
- `2026-03-09T20:31:47Z` `inline` by `b8zhong` `python/sglang/srt/layers/quantization/fp4_utils.py`:90; signals: cutlass, flashinfer, fp4, memory, sm100, sm120; excerpt: "Actually, before this was the case (sm100/103 and sm120 will both pick flashinfer cutlass, due to to a memory leak). So it's alright I ..." (https://github.com/sgl-project/sglang/pull/20047#discussion_r2907783734)
- `2026-03-06T17:35:46Z` `review` `COMMENTED` by `b8zhong`; signals: cutlass, sm100, sm120; excerpt: "@Fridge003 , since do you still think this PR is hacky to set it to auto? Because, it looks like the SM120 CUTLASS-based implementation ..." (https://github.com/sgl-project/sglang/pull/20047#pullrequestreview-3905066149)
- `2026-03-09T21:12:00Z` `issue` by `Fridge003`; signals: fp4, gemm, nvfp4; excerpt: "nvfp4 gemm test passed" (https://github.com/sgl-project/sglang/pull/20047#issuecomment-4026945115)
- `2026-03-06T17:35:39Z` `inline` by `b8zhong` `python/sglang/srt/server_args.py`:4243; signals: sm120; excerpt: "QQ: @Fridge003 do you still think this is hacky? Because it looks like the SM120 impl has a bug, and now the two devices ..." (https://github.com/sgl-project/sglang/pull/20047#discussion_r2897009806)
