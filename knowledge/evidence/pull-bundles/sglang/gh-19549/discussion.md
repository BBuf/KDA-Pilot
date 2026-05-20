# PR Discussion Digest

- Source PR: [sgl-project/sglang#19549](https://github.com/sgl-project/sglang/pull/19549)
- Source page: `sources/prs/sglang/PR-19549.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19549`
- Generated at: `2026-05-20T15:28:53.878477+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-28T06:58:01Z`
- Merged: `2026-03-10T20:11:08Z`

## Discussion Counts

- Issue comments: 24
- Review submissions: 20 (approved=1, commented=19)
- Inline review comments: 19
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=8, outdated=6
- Human participants with discussion text: Ratish1, ericcurtin, mickqian, yeahdongcn, yhyang201
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-04T03:48:43Z` `COMMENTED` by `mickqian` - well done! Should we consider splitting this PR into two, supporting mps on llm/diffusion one by one? (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3886533080)
- `2026-03-04T04:47:12Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3886667077)
- `2026-03-04T07:40:54Z` `COMMENTED` by `Ratish1` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3887706643)
- `2026-03-04T07:41:19Z` `COMMENTED` by `Ratish1` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3887708434)
- `2026-03-04T07:45:13Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3887723656)
- `2026-03-04T07:55:29Z` `COMMENTED` by `Ratish1` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3887761744)
- `2026-03-04T09:11:43Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3888099494)
- `2026-03-04T09:20:38Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3888147341)
- `2026-03-04T10:10:49Z` `COMMENTED` by `Ratish1` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3888431552)
- `2026-03-04T10:33:38Z` `COMMENTED` by `Ratish1` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3888556296)
- `2026-03-04T10:53:12Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3888661555)
- `2026-03-04T11:09:23Z` `COMMENTED` by `Ratish1` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3888743946)
- `2026-03-04T12:15:08Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3889074628)
- `2026-03-04T12:18:12Z` `COMMENTED` by `Ratish1` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3889090082)
- `2026-03-05T22:54:40Z` `COMMENTED` by `ericcurtin` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3900186585)
- `2026-03-06T01:37:59Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3900696625)
- `2026-03-06T03:20:33Z` `COMMENTED` by `mickqian` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3901042032)
- `2026-03-06T03:20:36Z` `APPROVED` by `mickqian` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3901042198)
- `2026-03-06T03:50:01Z` `COMMENTED` by `yeahdongcn` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3901124282)
- `2026-03-06T11:52:16Z` `COMMENTED` by `ericcurtin` (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3903285479)

## Inline Comment Hotspots

- `python/sglang/srt/configs/device_config.py`: 5 inline comment(s)
- `docs/diffusion/installation.md`: 5 inline comment(s)
- `python/sglang/srt/managers/scheduler.py`: 4 inline comment(s)
- `python/sglang/_mps_stub.py`: 3 inline comment(s)
- `python/sglang/jit_kernel/diffusion/triton/mps_fallback.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-04T10:33:38Z` `inline` by `Ratish1` `python/sglang/jit_kernel/diffusion/triton/mps_fallback.py`:94; signals: kernel, triton; excerpt: "Does this line break valid 2D modulation broadcasting?. x (scale constant + scale) + shift is not broadcast-compatible for x:[B,L,C] with scale/shift:[B,C] when L ..." (https://github.com/sgl-project/sglang/pull/19549#discussion_r2883029589)
- `2026-03-04T10:53:12Z` `inline` by `yeahdongcn` `python/sglang/jit_kernel/diffusion/triton/mps_fallback.py`:94; signals: kernel, triton; excerpt: "You are totally right. [B, C] should be converted to [B, 1, C] for 2D. Please see the new commit. Thanks!" (https://github.com/sgl-project/sglang/pull/19549#discussion_r2883115550)
- `2026-03-04T07:55:29Z` `inline` by `Ratish1` `python/sglang/srt/managers/scheduler.py`:3208; signals: hang; excerpt: "Will this cause error for non-mps devices?. This introduces local-variable shadowing and breaks non-MPS startup. It seems to be a breaking change. I tested ..." (https://github.com/sgl-project/sglang/pull/19549#discussion_r2882342686)
- `2026-03-06T11:52:16Z` `inline` by `ericcurtin` `python/sglang/srt/configs/device_config.py`:14; signals: memory; excerpt: "I'm about to board a plane and can't refresh my memory so quickly, but the weirdness might be intentional, can't say right now" (https://github.com/sgl-project/sglang/pull/19549#discussion_r2895376064)
- `2026-03-04T03:48:43Z` `review` `COMMENTED` by `mickqian`; signals: general review; excerpt: "well done! Should we consider splitting this PR into two, supporting mps on llm/diffusion one by one?" (https://github.com/sgl-project/sglang/pull/19549#pullrequestreview-3886533080)
- `2026-03-04T07:41:19Z` `inline` by `Ratish1` `python/sglang/_mps_stub.py`:30; signals: hang; excerpt: "shall we change this comment also as it looks weird" (https://github.com/sgl-project/sglang/pull/19549#discussion_r2882294002)
- `2026-03-04T09:20:38Z` `inline` by `yeahdongcn` `python/sglang/srt/managers/scheduler.py`:3208; signals: cuda; excerpt: "Could you please do a double-check on CUDA? Thanks!" (https://github.com/sgl-project/sglang/pull/19549#discussion_r2882689671)
- `2026-03-04T04:53:23Z` `issue` by `yeahdongcn`; signals: hang; excerpt: "Should we consider splitting this PR into two, supporting mps on llm/diffusion one by one? I had considered splitting the PR, but in practice, ..." (https://github.com/sgl-project/sglang/pull/19549#issuecomment-3995264858)
- `2026-03-04T07:40:54Z` `inline` by `Ratish1` `python/sglang/_mps_stub.py`:18; signals: general review; excerpt: "Should we remove these kind of comments or just add a normal comment. Since we also add docstrings to the class?" (https://github.com/sgl-project/sglang/pull/19549#discussion_r2882292566)
- `2026-03-04T07:45:13Z` `inline` by `yeahdongcn` `python/sglang/_mps_stub.py`:18; signals: general review; excerpt: "No problem. I'll clean up those comments (I was trying to use AI to enhance them, but it looks like some unnecessary content was ..." (https://github.com/sgl-project/sglang/pull/19549#discussion_r2882307327)
- `2026-03-05T22:54:40Z` `inline` by `ericcurtin` `python/sglang/srt/configs/device_config.py`:14; signals: general review; excerpt: "You may want to call things like this metal rather than mps. mlx has sorta outgrown mps. If you call it metal, you have ..." (https://github.com/sgl-project/sglang/pull/19549#discussion_r2892805093)
- `2026-03-06T01:37:59Z` `inline` by `yeahdongcn` `python/sglang/srt/configs/device_config.py`:14; signals: general review; excerpt: "Hi Eric, Thanks for taking a look at this PR. Yes, Metal might be a more appropriate identifier for macOS in general. In this ..." (https://github.com/sgl-project/sglang/pull/19549#discussion_r2893292436)
