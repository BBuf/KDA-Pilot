# PR Discussion Digest

- Source PR: [sgl-project/sglang#22051](https://github.com/sgl-project/sglang/pull/22051)
- Source page: `sources/prs/sglang/PR-22051.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22051`
- Generated at: `2026-05-20T15:29:20.205304+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-03T14:36:46Z`
- Merged: `2026-04-10T21:18:39Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 16 (approved=2, commented=14)
- Inline review comments: 17
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=8, outdated=7
- Human participants with discussion text: Fridge003, froststeam, yeahdongcn
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-03T14:39:52Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for the MUSA (Moore Threads GPU) hardware backend, specifically focusing on ... (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4055988319)
- `2026-04-03T14:49:26Z` `COMMENTED` by `froststeam` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4056020284)
- `2026-04-03T14:50:34Z` `COMMENTED` by `froststeam` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4056025129)
- `2026-04-03T14:51:23Z` `COMMENTED` by `froststeam` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4056028416)
- `2026-04-05T13:19:33Z` `COMMENTED` by `yeahdongcn` - I think it would be better to split this into two commits: one carrying over changes from the ... (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4059468636)
- `2026-04-06T11:13:23Z` `COMMENTED` by `froststeam` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4061658271)
- `2026-04-06T13:20:29Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4062197453)
- `2026-04-06T13:22:11Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4062204746)
- `2026-04-06T13:22:33Z` `APPROVED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4062206238)
- `2026-04-08T08:51:48Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4073916100)
- `2026-04-08T19:16:20Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4077659592)
- `2026-04-09T08:19:06Z` `COMMENTED` by `froststeam` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4080776166)
- `2026-04-09T08:21:35Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4080764716)
- `2026-04-09T11:57:32Z` `COMMENTED` by `froststeam` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4082081817)
- `2026-04-09T11:58:41Z` `COMMENTED` by `froststeam` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4082089831)
- `2026-04-10T21:18:23Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4092538034)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/flashattention_backend.py`: 7 inline comment(s)
- `python/sglang/srt/hardware_backend/musa/attention/flash_attention.py`: 6 inline comment(s)
- `python/sglang/srt/layers/attention/attention_registry.py`: 2 inline comment(s)
- `python/sglang/srt/hardware_backend/musa/attention/flashattention_backend.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-09T08:19:06Z` `inline` by `froststeam` `python/sglang/srt/layers/attention/flashattention_backend.py`:1; signals: attention, cuda, hang, perf, performance; excerpt: "Thanks for the suggestion. The changes have already been refactored into a standalone MUSA mixin class. Previously I tried to merge them into the ..." (https://github.com/sgl-project/sglang/pull/22051#discussion_r3056427897)
- `2026-04-05T13:19:33Z` `review` `COMMENTED` by `yeahdongcn`; signals: hang, kernel, regression; excerpt: "I think it would be better to split this into two commits: one carrying over changes from the previous PR, and another fixing the ..." (https://github.com/sgl-project/sglang/pull/22051#pullrequestreview-4059468636)
- `2026-04-06T13:20:29Z` `inline` by `yeahdongcn` `python/sglang/srt/layers/attention/flashattention_backend.py`:753; signals: attention, kernel, regression; excerpt: "The key updates to resolve the previous regression in FA3/FA4 kernel wiring on NVIDIA GPUs should be here, since upstream main now selects and ..." (https://github.com/sgl-project/sglang/pull/22051#discussion_r3039638700)
- `2026-04-08T08:51:48Z` `inline` by `yeahdongcn` `python/sglang/srt/layers/attention/flashattention_backend.py`:753; signals: attention, flash attention, kernel; excerpt: "This comment is outdated, as the logic has been moved to python/sglang/jit kernel/flash attention.py." (https://github.com/sgl-project/sglang/pull/22051#discussion_r3050220979)
- `2026-04-03T14:49:26Z` `inline` by `froststeam` `python/sglang/srt/hardware_backend/musa/attention/flash_attention.py`:151; signals: attention, cache; excerpt: "Since multiple concurrent requests are processed together in a single forward pass, they share the same ctx.prefix key in the global cache." (https://github.com/sgl-project/sglang/pull/22051#discussion_r3033153932)
- `2026-04-08T19:16:03Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/flashattention_backend.py`:1; signals: attention, hang; excerpt: "Is it possible to migrate all the changes in this file to a standalone file, like creating a mixin class for MUSA?" (https://github.com/sgl-project/sglang/pull/22051#discussion_r3053638771)
- `2026-04-09T08:21:11Z` `inline` by `yeahdongcn` `python/sglang/srt/hardware_backend/musa/attention/flashattention_backend.py`:43; signals: attention, tma; excerpt: "I don't know if FlashAttentionContext and FlashAttentionContextManager are still necessary here. Because this time, we choose to inherit from FlashAttentionBackend. If I remember this ..." (https://github.com/sgl-project/sglang/pull/22051#discussion_r3056437990)
- `2026-04-03T14:51:23Z` `inline` by `froststeam` `python/sglang/srt/hardware_backend/musa/attention/flash_attention.py`:160; signals: attention; excerpt: "Will be fixed once MUSA support is added. Currently this parameter has no real effect, so ignoring it is safe for now." (https://github.com/sgl-project/sglang/pull/22051#discussion_r3033161354)
- `2026-04-06T13:22:10Z` `inline` by `yeahdongcn` `python/sglang/srt/layers/attention/flashattention_backend.py`:753; signals: attention; excerpt: "I'll go ahead and approve this PR to trigger CI. Could @Fridge003 and @Kangyan-Zhou please take a final look? Thanks!" (https://github.com/sgl-project/sglang/pull/22051#discussion_r3039645599)
- `2026-04-03T14:50:33Z` `inline` by `froststeam` `python/sglang/srt/hardware_backend/musa/attention/flash_attention.py`:25; signals: attention; excerpt: "Each GPU runs a separate process, so per-device isolation is already guaranteed." (https://github.com/sgl-project/sglang/pull/22051#discussion_r3033158191)
- `2026-04-05T13:15:25Z` `inline` by `yeahdongcn` `python/sglang/srt/layers/attention/flashattention_backend.py`:439; signals: attention; excerpt: "IMO, it would be clearer:" (https://github.com/sgl-project/sglang/pull/22051#discussion_r3036852265)
- `2026-04-06T11:13:23Z` `inline` by `froststeam` `python/sglang/srt/layers/attention/flashattention_backend.py`:439; signals: attention; excerpt: "Thanks for the suggestion! I've already updated the code accordingly." (https://github.com/sgl-project/sglang/pull/22051#discussion_r3039155100)
