# PR Discussion Digest

- Source PR: [sgl-project/sglang#15347](https://github.com/sgl-project/sglang/pull/15347)
- Source page: `sources/prs/sglang/PR-15347.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-15347`
- Generated at: `2026-05-20T15:28:11.120930+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-18T00:14:32Z`
- Merged: `2026-01-19T03:50:16Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 7 (approved=3, changes_requested=3, commented=1)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=0
- Human participants with discussion text: Fridge003, leejnau, trevor-m, yzh119
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-18T22:50:20Z` `CHANGES_REQUESTED` by `trevor-m` - Thanks! I left some comments. Can you also add a unit test which instantiates the TopK class such ... (https://github.com/sgl-project/sglang/pull/15347#pullrequestreview-3595013618)
- `2025-12-22T17:08:55Z` `APPROVED` by `trevor-m` - Thanks, looks good! Can you run pre-commit to fix the linting? (https://github.com/sgl-project/sglang/pull/15347#pullrequestreview-3604903473)
- `2025-12-22T19:08:04Z` `CHANGES_REQUESTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/15347#pullrequestreview-3605378400)
- `2025-12-22T19:38:09Z` `APPROVED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/15347#pullrequestreview-3605469498)
- `2026-01-07T13:47:09Z` `CHANGES_REQUESTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/15347#pullrequestreview-3634981082)
- `2026-01-07T22:57:22Z` `COMMENTED` by `leejnau` (https://github.com/sgl-project/sglang/pull/15347#pullrequestreview-3637110440)
- `2026-01-16T03:48:24Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/15347#pullrequestreview-3668622166)

## Inline Comment Hotspots

- `test/registered/kernels/test_fused_topk_deepseek.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/topk.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-12T16:26:54Z` `issue` by `Fridge003`; signals: accuracy, b200, fp4; excerpt: "@leejnau Can you please test this PR on DeepSeek R1/V3.2 with the GPQA dataset with this command I just tested gpqa on dpsk fp4 ..." (https://github.com/sgl-project/sglang/pull/15347#issuecomment-3739415948)
- `2026-01-13T05:19:13Z` `issue` by `leejnau`; signals: accuracy, b200, fp4; excerpt: "@leejnau Can you please test this PR on DeepSeek R1/V3.2 with the GPQA dataset with this command I just tested gpqa on dpsk fp4 ..." (https://github.com/sgl-project/sglang/pull/15347#issuecomment-3742008595)
- `2025-12-18T20:57:28Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/topk.py`:747; signals: flashinfer, moe; excerpt: "We should keep the code path for moe fused gate. fused topk deepseek should have higher priority and should be used it's is available ..." (https://github.com/sgl-project/sglang/pull/15347#discussion_r2632602864)
- `2025-12-22T19:08:00Z` `inline` by `trevor-m` `test/registered/kernels/test_fused_topk_deepseek.py`; signals: kernel, register; excerpt: "Can you move this test file to python/sglang/test? This directory is for tests for the sgl-kernel library" (https://github.com/sgl-project/sglang/pull/15347#discussion_r2640952772)
- `2025-12-18T22:50:20Z` `review` `CHANGES_REQUESTED` by `trevor-m`; signals: kernel; excerpt: "Thanks! I left some comments. Can you also add a unit test which instantiates the TopK class such that this new kernel is called ..." (https://github.com/sgl-project/sglang/pull/15347#pullrequestreview-3595013618)
- `2026-01-07T13:47:05Z` `inline` by `Fridge003` `test/registered/kernels/test_fused_topk_deepseek.py`:1; signals: kernel, register; excerpt: "Please move this test to test/registered/kernels and register it as nightly-1-gpu. Like this one" (https://github.com/sgl-project/sglang/pull/15347#discussion_r2668527805)
- `2026-01-07T22:57:22Z` `inline` by `leejnau` `test/registered/kernels/test_fused_topk_deepseek.py`:1; signals: kernel, register; excerpt: "done [21e4828](" (https://github.com/sgl-project/sglang/pull/15347#discussion_r2670329233)
- `2026-01-07T22:39:41Z` `issue` by `leejnau`; signals: flashinfer; excerpt: "@leejnau Is this PR depending on Flashinfer with version newer than 0.5.3? For the optimized path (fused topk deepseek) it relies upon flashinfer Release ..." (https://github.com/sgl-project/sglang/pull/15347#issuecomment-3721110032)
- `2026-01-07T01:48:01Z` `issue` by `Fridge003`; signals: flashinfer; excerpt: "@leejnau Is this PR depending on Flashinfer with version newer than 0.5.3?" (https://github.com/sgl-project/sglang/pull/15347#issuecomment-3717008070)
- `2026-01-15T06:05:59Z` `issue` by `yzh119`; signals: flashinfer; excerpt: "Might be relevant to which is fixed in flashinfer v0.6.1." (https://github.com/sgl-project/sglang/pull/15347#issuecomment-3753037688)
- `2026-01-16T03:36:31Z` `issue` by `Fridge003`; signals: accuracy; excerpt: "Just tested again with v0.6.1, and the accuracy restored to expected number @leejnau @yzh119" (https://github.com/sgl-project/sglang/pull/15347#issuecomment-3757968689)
- `2026-01-16T03:48:42Z` `issue` by `Fridge003`; signals: flashinfer; excerpt: "Waiting for upgrade of flashinfer" (https://github.com/sgl-project/sglang/pull/15347#issuecomment-3757992578)
