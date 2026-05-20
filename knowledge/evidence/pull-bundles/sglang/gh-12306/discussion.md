# PR Discussion Digest

- Source PR: [sgl-project/sglang#12306](https://github.com/sgl-project/sglang/pull/12306)
- Source page: `sources/prs/sglang/PR-12306.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-12306`
- Generated at: `2026-05-20T15:27:38.222597+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-29T01:38:54Z`
- Merged: `2025-11-29T08:05:37Z`

## Discussion Counts

- Issue comments: 21
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: FlamingoPg, Kangyan-Zhou, Qiaolin-Yu, elvischenv, nvpohanh
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-13T06:49:50Z` `APPROVED` by `FlamingoPg` (https://github.com/sgl-project/sglang/pull/12306#pullrequestreview-3457849261)
- `2025-11-21T01:41:03Z` `COMMENTED` by `Qiaolin-Yu` - Does auto-tuning also work well for low-latency cases? Or could we control this feature using server parameters? (https://github.com/sgl-project/sglang/pull/12306#pullrequestreview-3490810442)
- `2025-11-21T07:21:15Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/12306#pullrequestreview-3491508377)
- `2025-11-22T20:04:30Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/12306#pullrequestreview-3496928852)
- `2025-11-25T08:55:01Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/12306#pullrequestreview-3503968857)
- `2025-11-26T04:30:34Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/12306#pullrequestreview-3508598525)
- `2025-11-26T04:31:58Z` `APPROVED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/12306#pullrequestreview-3508603169)

## Inline Comment Hotspots

- `python/sglang/srt/model_executor/model_runner.py`: 3 inline comment(s)
- `python/sglang/srt/server_args.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-25T08:55:01Z` `inline` by `elvischenv` `python/sglang/srt/model_executor/model_runner.py`:2193; signals: autotune, b200, cuda, flashinfer, kernel, latency, regression; excerpt: "Does auto-tuning also work well for low-latency cases? Without autotuning, Flashinfer is selecting the kernels by some heuristics. Autotuning will tune the possible kernels ..." (https://github.com/sgl-project/sglang/pull/12306#discussion_r2559118019)
- `2025-10-29T07:59:21Z` `issue` by `elvischenv`; signals: autotune, b200, block, flashinfer, fp4, kernel, moe; excerpt: "@FlamingoPg May I ask how long a single tuning run takes now? For B200+gpt-oss-120b, it takes about 1 min from my local test: Is ..." (https://github.com/sgl-project/sglang/pull/12306#issuecomment-3460260521)
- `2025-11-21T05:14:24Z` `issue` by `nvpohanh`; signals: latency, perf, performance, regression; excerpt: "Does auto-tuning also work well for low-latency cases? Or could we control this feature using server parameters? What does "work well" mean? At least ..." (https://github.com/sgl-project/sglang/pull/12306#issuecomment-3561431152)
- `2025-11-21T01:41:03Z` `review` `COMMENTED` by `Qiaolin-Yu`; signals: latency; excerpt: "Does auto-tuning also work well for low-latency cases? Or could we control this feature using server parameters?" (https://github.com/sgl-project/sglang/pull/12306#pullrequestreview-3490810442)
- `2025-11-21T07:21:11Z` `inline` by `elvischenv` `python/sglang/srt/server_args.py`:2892; signals: autotune, flashinfer; excerpt: "@Qiaolin-Yu @nvpohanh Added a flag --enable-flashinfer-autotune, and turn off autotuning by default." (https://github.com/sgl-project/sglang/pull/12306#discussion_r2548788632)
- `2025-11-20T01:43:57Z` `issue` by `nvpohanh`; signals: oom, pipeline; excerpt: "The two GPU pipeline failures seem to be caused by OOM, not related to this PR. @FlamingoPg could you re-run these two pipelines? Thanks!" (https://github.com/sgl-project/sglang/pull/12306#issuecomment-3555394880)
- `2025-11-22T20:04:30Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/model_executor/model_runner.py`:2193; signals: autotune; excerpt: "Could we just add autotune before Does this part of the logic duplicate existing code?" (https://github.com/sgl-project/sglang/pull/12306#discussion_r2553330548)
- `2025-10-29T05:39:19Z` `issue` by `FlamingoPg`; signals: kernel; excerpt: "Great work! May I ask how long a single tuning run takes now? Is there a switch to control whether the kernel is tuned?" (https://github.com/sgl-project/sglang/pull/12306#issuecomment-3459883752)
- `2025-11-07T01:51:04Z` `issue` by `nvpohanh`; signals: failing; excerpt: "@FlamingoPg There are quite a few CI failures. Are all of them caused by this PR? Or are some of them known failing issues?" (https://github.com/sgl-project/sglang/pull/12306#issuecomment-3500128440)
- `2025-11-26T04:30:33Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/model_executor/model_runner.py`:2193; signals: general review; excerpt: "make sense" (https://github.com/sgl-project/sglang/pull/12306#discussion_r2563016176)
- `2025-11-13T06:49:34Z` `issue` by `FlamingoPg`; signals: general review; excerpt: "Hi @FlamingoPg, It seems that CI failures are not related to my PR. Could you help confirm? Thanks! Sure" (https://github.com/sgl-project/sglang/pull/12306#issuecomment-3525821534)
- `2025-11-19T05:18:39Z` `issue` by `elvischenv`; signals: general review; excerpt: "@elvischenv do you think this failure is related to this PR? Should be related to a PR that merged 2 weeks ago: 11133. Pushed ..." (https://github.com/sgl-project/sglang/pull/12306#issuecomment-3550852315)
