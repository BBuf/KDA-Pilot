# PR Discussion Digest

- Source PR: [sgl-project/sglang#12353](https://github.com/sgl-project/sglang/pull/12353)
- Source page: `sources/prs/sglang/PR-12353.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-12353`
- Generated at: `2026-05-20T15:27:38.227101+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-29T20:29:41Z`
- Merged: `2025-11-05T02:54:55Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 10
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=6, outdated=3
- Human participants with discussion text: Fridge003, fzyzcjy, kaixih, lpc0220, trevor-m
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-29T20:32:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request fixes the cutedsl MoE backend by correcting the execution path for handling quantized ... (https://github.com/sgl-project/sglang/pull/12353#pullrequestreview-3396073365)
- `2025-10-30T20:11:34Z` `APPROVED` by `trevor-m` - LGTM (https://github.com/sgl-project/sglang/pull/12353#pullrequestreview-3401453444)
- `2025-10-30T20:15:11Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12353#pullrequestreview-3401467343)
- `2025-10-31T00:25:33Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12353#pullrequestreview-3402138640)
- `2025-10-31T06:12:10Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/12353#pullrequestreview-3402719726)
- `2025-11-04T00:34:02Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12353#pullrequestreview-3413479842)
- `2025-11-04T00:49:28Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/12353#pullrequestreview-3413508687)
- `2025-11-04T17:35:02Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/12353#pullrequestreview-3417841563)

## Inline Comment Hotspots

- `test/srt/run_suite.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/flashinfer_cutedsl_moe.py`: 2 inline comment(s)
- `.github/workflows/pr-test.yml`: 2 inline comment(s)
- `python/sglang/test/test_utils.py`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-03T17:39:32Z` `issue` by `kaixih`; signals: b200, block, cute, moe; excerpt: "@Fridge003 I commented off the e2e tests for now since there seems an issue of the GB200 CI runner + IBGDA ([issue]( To unblock ..." (https://github.com/sgl-project/sglang/pull/12353#issuecomment-3481738130)
- `2025-10-31T06:12:10Z` `inline` by `kaixih` `.github/workflows/pr-test.yml`:817; signals: b200, cute; excerpt: "Sure. I will remove the dsv3 test since it doesn't need to run the same test on 4xb200 and gb200 twice. The cutedsl one ..." (https://github.com/sgl-project/sglang/pull/12353#discussion_r2480262222)
- `2025-10-31T04:34:11Z` `issue` by `lpc0220`; signals: benchmark, moe; excerpt: "I am wondering why do we need so many different moe backends? in which case which moe backend would work best? Do we need ..." (https://github.com/sgl-project/sglang/pull/12353#issuecomment-3471308934)
- `2025-10-30T20:15:09Z` `inline` by `Fridge003` `test/srt/run_suite.py`:184; signals: b200; excerpt: "This will add too much burden to the CI machine (We only have 4 B200) Is there anyway to reduce its time. Like moving ..." (https://github.com/sgl-project/sglang/pull/12353#discussion_r2479397998)
- `2025-10-31T00:18:27Z` `inline` by `Fridge003` `.github/workflows/pr-test.yml`:817; signals: b200; excerpt: "Can we merge it into unit-test-backend-4-gpu-gb200 test? So we don't need to launch the environment twice" (https://github.com/sgl-project/sglang/pull/12353#discussion_r2479848882)
- `2025-11-01T19:04:25Z` `issue` by `Fridge003`; signals: b200, kernel; excerpt: "cc @kaixih 12480 added a kernel build flow for aarch64, which can be used for gb200 CI" (https://github.com/sgl-project/sglang/pull/12353#issuecomment-3476682354)
- `2025-11-04T00:49:22Z` `inline` by `kaixih` `python/sglang/test/test_utils.py`:60; signals: hang; excerpt: "For this one, when I use the R1 checkpoints, I remember the runner will hang there (preparing the datasets?) like forever. Then I change ..." (https://github.com/sgl-project/sglang/pull/12353#discussion_r2488281949)
- `2025-11-04T00:33:49Z` `inline` by `Fridge003` `test/srt/run_suite.py`:183; signals: cute; excerpt: "Keep this test until the cutedsl one can be run" (https://github.com/sgl-project/sglang/pull/12353#discussion_r2488260934)
- `2025-11-04T00:34:00Z` `inline` by `Fridge003` `python/sglang/test/test_utils.py`:60; signals: hang; excerpt: "Why changing the default model?" (https://github.com/sgl-project/sglang/pull/12353#discussion_r2488261315)
- `2025-11-04T17:35:02Z` `inline` by `kaixih` `test/srt/run_suite.py`:183; signals: general review; excerpt: "Done." (https://github.com/sgl-project/sglang/pull/12353#discussion_r2491476899)
- `2025-10-29T23:59:00Z` `issue` by `fzyzcjy`; signals: general review; excerpt: "oops. is it b/c you forget it or deliberately not add it? I personally forgot adding it many times... do you think this is ..." (https://github.com/sgl-project/sglang/pull/12353#issuecomment-3465321835)
- `2025-10-30T00:07:16Z` `issue` by `kaixih`; signals: general review; excerpt: "Oh, definitely not intentional. I think in many cases people just assume the codebase will magically pick up tests from files like test-xxx.py. Either ..." (https://github.com/sgl-project/sglang/pull/12353#issuecomment-3465382747)
