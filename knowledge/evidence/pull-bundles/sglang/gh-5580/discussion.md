# PR Discussion Digest

- Source PR: [sgl-project/sglang#5580](https://github.com/sgl-project/sglang/pull/5580)
- Source page: `sources/prs/sglang/PR-5580.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-5580`
- Generated at: `2026-05-20T15:30:28.034717+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-20T19:08:46Z`
- Merged: `2025-04-21T23:52:53Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: Alcanderian, Fridge003, whybeyoung, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-04-20T19:29:52Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/5580#pullrequestreview-2780316195)
- `2025-04-20T23:52:21Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5580#pullrequestreview-2780362688)
- `2025-04-21T02:32:42Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/5580#pullrequestreview-2780436069)
- `2025-04-21T03:30:39Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/5580#pullrequestreview-2780472117)
- `2025-04-21T06:37:37Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5580#pullrequestreview-2780656292)
- `2025-04-21T07:30:44Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/5580#pullrequestreview-2780734945)
- `2025-04-21T08:10:02Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/5580#pullrequestreview-2780791504)
- `2025-04-21T22:17:12Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5580#pullrequestreview-2782339112)
- `2025-04-21T23:52:27Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5580#pullrequestreview-2782438119)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/deep_gemm.py`: 6 inline comment(s)
- `python/sglang/srt/managers/scheduler.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-21T22:17:11Z` `inline` by `zhyncs` `python/sglang/srt/layers/quantization/deep_gemm.py`:166; signals: attention, compile, gemm, hang; excerpt: "Pay attention to compile and tune as it has introduced breaking changes before." (https://github.com/sgl-project/sglang/pull/5580#discussion_r2053056251)
- `2025-04-21T02:32:42Z` `inline` by `Alcanderian` `python/sglang/srt/layers/quantization/deep_gemm.py`:124; signals: gemm; excerpt: "Multithreading by tqdm is enough here because the main cost is on nvcc subprocess. I am going to let only first rank of a ..." (https://github.com/sgl-project/sglang/pull/5580#discussion_r2051887007)
- `2025-04-21T07:30:44Z` `inline` by `Alcanderian` `python/sglang/srt/layers/quantization/deep_gemm.py`:124; signals: gemm; excerpt: "Offline discussion with @zhyncs : Compilation with all ranks in one node cannnot get significantly speed up and may be harmful if we launch ..." (https://github.com/sgl-project/sglang/pull/5580#discussion_r2052075970)
- `2025-04-20T19:29:52Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/deep_gemm.py`:14; signals: gemm; excerpt: "Do we need to set these vars to true by default after this PR? @zhyncs" (https://github.com/sgl-project/sglang/pull/5580#discussion_r2051791990)
- `2025-04-20T23:52:21Z` `inline` by `zhyncs` `python/sglang/srt/layers/quantization/deep_gemm.py`:124; signals: gemm; excerpt: "Can we do this using multiprocessing? And can we use multiple GPU devices simultaneously?" (https://github.com/sgl-project/sglang/pull/5580#discussion_r2051835417)
- `2025-04-21T06:37:37Z` `inline` by `zhyncs` `python/sglang/srt/layers/quantization/deep_gemm.py`:124; signals: gemm; excerpt: "Will it be faster if we use all ranks?" (https://github.com/sgl-project/sglang/pull/5580#discussion_r2052027603)
- `2025-04-21T06:31:45Z` `issue` by `zhyncs`; signals: gemm; excerpt: "Parallel JIT pre-compilation module for deep gemm, scaning M from 1 to 65536. 16384 is ok @Alcanderian" (https://github.com/sgl-project/sglang/pull/5580#issuecomment-2817749456)
- `2025-04-21T03:30:39Z` `inline` by `Alcanderian` `python/sglang/srt/managers/scheduler.py`:1990; signals: general review; excerpt: "Please confirm whether modifying the environment variables here is appropriate lol @zhyncs" (https://github.com/sgl-project/sglang/pull/5580#discussion_r2051912200)
- `2025-04-21T08:10:02Z` `inline` by `Alcanderian` `python/sglang/srt/managers/scheduler.py`:1990; signals: general review; excerpt: "Will try to move it to TpWorker/ModelRunner" (https://github.com/sgl-project/sglang/pull/5580#discussion_r2052111783)
