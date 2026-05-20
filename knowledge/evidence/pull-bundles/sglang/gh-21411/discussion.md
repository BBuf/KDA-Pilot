# PR Discussion Digest

- Source PR: [sgl-project/sglang#21411](https://github.com/sgl-project/sglang/pull/21411)
- Source page: `sources/prs/sglang/PR-21411.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21411`
- Generated at: `2026-05-20T15:29:13.659096+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-25T13:46:42Z`
- Merged: `2026-03-29T04:02:07Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 14
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=8, outdated=2
- Human participants with discussion text: BBuf, kaixih, yizhang2077, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-25T13:53:02Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the gated delta rule (GDN) attention mechanism by introducing a new fused ... (https://github.com/sgl-project/sglang/pull/21411#pullrequestreview-4006870660)
- `2026-03-26T04:58:57Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/21411#pullrequestreview-4011424946)
- `2026-03-26T05:57:28Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/21411#pullrequestreview-4011634379)
- `2026-03-26T07:12:19Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/21411#pullrequestreview-4011904282)
- `2026-03-26T12:03:01Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/21411#pullrequestreview-4013557534)
- `2026-03-26T12:14:49Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/21411#pullrequestreview-4013637591)
- `2026-03-27T03:09:41Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/21411#pullrequestreview-4018576527)
- `2026-03-27T03:30:20Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/21411#pullrequestreview-4018659916)
- `2026-03-27T03:40:24Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/21411#pullrequestreview-4018684097)
- `2026-03-27T03:42:25Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/21411#pullrequestreview-4018687814)
- `2026-03-29T04:01:46Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21411#pullrequestreview-4026321582)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/fla/chunk_fwd.py`: 7 inline comment(s)
- `python/sglang/srt/layers/attention/fla/chunk.py`: 5 inline comment(s)
- `python/sglang/srt/layers/attention/fla/utils.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-27T03:49:35Z` `issue` by `yuan-luo`; signals: kernel, memory, overflow, perf, performance, register; excerpt: "I tried to fuse all three kernels into one kernel, it passed all the tests, but the performance dropped. The reason is because the ..." (https://github.com/sgl-project/sglang/pull/21411#issuecomment-4139954971)
- `2026-03-26T12:14:48Z` `inline` by `yuan-luo` `python/sglang/srt/layers/attention/fla/chunk_fwd.py`:31; signals: attention, autotune, hang, kernel; excerpt: "@yizhang2077 BK is a parameter for this kernel, if we remove autotune, it will crash as following: Currently kda.py is also using similar mechanism:" (https://github.com/sgl-project/sglang/pull/21411#discussion_r2994466270)
- `2026-03-26T12:03:01Z` `inline` by `yuan-luo` `python/sglang/srt/layers/attention/fla/chunk.py`:40; signals: attention, hang, kernel; excerpt: "@yizhang2077 After double check I prefer to keep the recompute w u fwd into chunk gated delta rule fwd intra. The reason is both ..." (https://github.com/sgl-project/sglang/pull/21411#discussion_r2994405436)
- `2026-03-26T07:10:26Z` `inline` by `yizhang2077` `python/sglang/srt/layers/attention/fla/chunk_fwd.py`:31; signals: attention, autotune, block; excerpt: "remove autotune since it may block inference" (https://github.com/sgl-project/sglang/pull/21411#discussion_r2992912843)
- `2026-03-27T03:09:33Z` `inline` by `kaixih` `python/sglang/srt/layers/attention/fla/chunk_fwd.py`:382; signals: attention, kernel; excerpt: "do we need to assert this to be 64? or this also works with other values (it seems original unfused kernel supports 12/32/64." (https://github.com/sgl-project/sglang/pull/21411#discussion_r2998749857)
- `2026-03-27T03:40:24Z` `inline` by `yuan-luo` `python/sglang/srt/layers/attention/fla/chunk_fwd.py`:382; signals: attention, kernel; excerpt: "We don't need to assert this to 64, it also support other size, but just sets default value to 64. The original unfused kernel ..." (https://github.com/sgl-project/sglang/pull/21411#discussion_r2998804880)
- `2026-03-26T04:58:52Z` `inline` by `yizhang2077` `python/sglang/srt/layers/attention/fla/chunk_fwd.py`:407; signals: attention, kernel; excerpt: "recompute w u fwd does not be fused into kernel" (https://github.com/sgl-project/sglang/pull/21411#discussion_r2992472862)
- `2026-03-26T05:57:28Z` `inline` by `yuan-luo` `python/sglang/srt/layers/attention/fla/chunk_fwd.py`:407; signals: attention, kernel; excerpt: "Right, recompute w u fwd launched kernel separately. I revised the title." (https://github.com/sgl-project/sglang/pull/21411#discussion_r2992659451)
- `2026-03-27T02:53:46Z` `inline` by `kaixih` `python/sglang/srt/layers/attention/fla/chunk.py`:14; signals: attention, kernel; excerpt: "curious, do we need to remove the "unfused" api/kernels from the code base?" (https://github.com/sgl-project/sglang/pull/21411#discussion_r2998717809)
- `2026-03-26T07:11:57Z` `inline` by `yizhang2077` `python/sglang/srt/layers/attention/fla/chunk.py`:40; signals: attention; excerpt: "keep recompute w u fwd outside if we do not fuse it into chunk gated delta rule fwd intra." (https://github.com/sgl-project/sglang/pull/21411#discussion_r2992918028)
- `2026-03-27T02:50:56Z` `inline` by `kaixih` `python/sglang/srt/layers/attention/fla/utils.py`:344; signals: attention; excerpt: "why do we need these variables? also they are seemingly already defined above." (https://github.com/sgl-project/sglang/pull/21411#discussion_r2998711456)
- `2026-03-27T03:30:20Z` `inline` by `yuan-luo` `python/sglang/srt/layers/attention/fla/chunk.py`:14; signals: attention; excerpt: "It is to be compliant with FLA implementation. Only use the fused API." (https://github.com/sgl-project/sglang/pull/21411#discussion_r2998787876)
