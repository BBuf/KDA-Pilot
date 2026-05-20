# PR Discussion Digest

- Source PR: [sgl-project/sglang#4068](https://github.com/sgl-project/sglang/pull/4068)
- Source page: `sources/prs/sglang/PR-4068.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4068`
- Generated at: `2026-05-20T15:30:04.230499+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-04T15:10:06Z`
- Merged: `2025-05-25T00:39:07Z`

## Discussion Counts

- Issue comments: 28
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 5
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: FrontierSetter, GreatBryan, Iamleos, Jacki1223, Kim1230, UnlceYang, ZJLi2013, agiping, amd-danli103, fzyzcjy, nannaer, yanbing-j, yizhang2077, zhyncs, ziyuhuang123
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 9

## Review Decisions

- `2025-03-27T08:35:14Z` `COMMENTED` by `agiping` (https://github.com/sgl-project/sglang/pull/4068#pullrequestreview-2719973422)
- `2025-03-27T14:35:05Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/4068#pullrequestreview-2721971193)
- `2025-04-02T03:02:30Z` `COMMENTED` by `agiping` (https://github.com/sgl-project/sglang/pull/4068#pullrequestreview-2734549842)
- `2025-04-24T06:35:53Z` `COMMENTED` by `amd-danli103` (https://github.com/sgl-project/sglang/pull/4068#pullrequestreview-2789883649)
- `2025-04-24T07:15:53Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/4068#pullrequestreview-2790006518)
- `2025-05-24T16:54:47Z` `APPROVED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/4068#pullrequestreview-2866385977)
- `2025-05-25T00:38:57Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/4068#pullrequestreview-2866689983)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-05-23T08:35:47Z` `issue` by `Iamleos`; signals: compile, cuda, latency, moe, race; excerpt: "There is a cuda capture error when enable tbo feature in low-latency deepep mode based on deepseek ep branch. Could you try cuda graph ..." (https://github.com/sgl-project/sglang/pull/4068#issuecomment-2903707525)
- `2025-03-27T08:05:15Z` `inline` by `agiping` `python/sglang/srt/models/deepseek_v2.py`:1240; signals: cute, oom, pipeline; excerpt: "I checked the pipeline design (stage(ops) seperation and overlaping execution defined by execute two batch raw function in python/sglang/srt/two batch overlap.py) , the actual ..." (https://github.com/sgl-project/sglang/pull/4068#discussion_r2015877675)
- `2025-04-24T06:35:53Z` `inline` by `amd-danli103` `python/sglang/srt/models/deepseek_v2.py`:1240; signals: deepgemm, gemm, moe; excerpt: "Thanks, I will recheck this later. BTW, does the current TBO implementation work under EPMoE (without DeepEP)? hi @fzyzcjy , I'd like to ask ..." (https://github.com/sgl-project/sglang/pull/4068#discussion_r2057647704)
- `2025-03-20T05:40:20Z` `issue` by `fzyzcjy`; signals: deepgemm, gemm; excerpt: "@agiping Hi, this PR is currently still in the state of "Draft PR", i.e. I am working on it. When it is done, I ..." (https://github.com/sgl-project/sglang/pull/4068#issuecomment-2739235765)
- `2025-04-11T14:30:46Z` `issue` by `fzyzcjy`; signals: kernel, perf; excerpt: "enable tbo almost dropped 70% perf Yes, especially given that the batch sizes are so tiny, we still do not have the needed kernels, ..." (https://github.com/sgl-project/sglang/pull/4068#issuecomment-2797086324)
- `2025-04-02T03:02:30Z` `inline` by `agiping` `python/sglang/srt/models/deepseek_v2.py`:1240; signals: moe; excerpt: "Thanks, I will recheck this later. BTW, does the current TBO implementation work under EPMoE (without DeepEP)?" (https://github.com/sgl-project/sglang/pull/4068#discussion_r2023997882)
- `2025-04-24T07:15:53Z` `inline` by `fzyzcjy` `python/sglang/srt/models/deepseek_v2.py`:1240; signals: kernel; excerpt: "Theoretically yes, if you integrate some non-deepep communication kernels." (https://github.com/sgl-project/sglang/pull/4068#discussion_r2057709594)
- `2025-04-10T10:00:32Z` `issue` by `ZJLi2013`; signals: moe; excerpt: "btw, is there chance to decouple this feature dependency on deepep-moe ? for non-NV chips, there is no easy replacement for ibgdr/nvsmem yet. thanks ..." (https://github.com/sgl-project/sglang/pull/4068#issuecomment-2792217596)
- `2025-04-10T15:11:35Z` `issue` by `fzyzcjy`; signals: moe; excerpt: "btw, is there chance to decouple this feature dependency on deepep-moe ? for non-NV chips, there is no easy replacement for ibgdr/nvsmem yet. thanks ..." (https://github.com/sgl-project/sglang/pull/4068#issuecomment-2794165185)
- `2025-04-11T05:06:41Z` `issue` by `FrontierSetter`; signals: oom; excerpt: "Have you tried testing with the --random-output parameter set to greater than 1? I tested using the : error occurred . The environment I ..." (https://github.com/sgl-project/sglang/pull/4068#issuecomment-2795845867)
- `2025-04-11T10:37:08Z` `issue` by `ZJLi2013`; signals: oom; excerpt: "Have you tried testing with the --random-output parameter set to greater than 1? I tested using the : error occurred . The environment I ..." (https://github.com/sgl-project/sglang/pull/4068#issuecomment-2796532649)
- `2025-04-11T10:48:04Z` `issue` by `ZJLi2013`; signals: perf; excerpt: "I will get back to two batch overlap after EPLB right now with smaller tokens b128 isl256 osl1, enable tbo almost dropped 70% perf ..." (https://github.com/sgl-project/sglang/pull/4068#issuecomment-2796554108)
