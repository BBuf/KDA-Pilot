# PR Discussion Digest

- Source PR: [sgl-project/sglang#12787](https://github.com/sgl-project/sglang/pull/12787)
- Source page: `sources/prs/sglang/PR-12787.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-12787`
- Generated at: `2026-05-20T15:27:42.944117+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-06T19:41:07Z`
- Merged: `2026-03-17T17:02:46Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 17
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=11, outdated=6
- Human participants with discussion text: Fridge003, hlu1, mmangkad, nvpohanh, samuellees, wenscarl, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-12T12:19:05Z` `COMMENTED` by `nvpohanh` (https://github.com/sgl-project/sglang/pull/12787#pullrequestreview-3790673381)
- `2026-02-12T16:23:17Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/12787#pullrequestreview-3792034972)
- `2026-02-13T08:00:16Z` `COMMENTED` by `nvpohanh` (https://github.com/sgl-project/sglang/pull/12787#pullrequestreview-3795614401)
- `2026-02-13T10:09:49Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12787#pullrequestreview-3796351029)
- `2026-02-13T20:49:22Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/12787#pullrequestreview-3799452935)
- `2026-02-24T14:02:14Z` `APPROVED` by `nvpohanh` (https://github.com/sgl-project/sglang/pull/12787#pullrequestreview-3848112142)
- `2026-02-24T17:46:45Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/12787#pullrequestreview-3849590306)
- `2026-03-03T22:47:51Z` `COMMENTED` by `hlu1` (https://github.com/sgl-project/sglang/pull/12787#pullrequestreview-3885472661)
- `2026-03-05T19:47:56Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/12787#pullrequestreview-3899240588)
- `2026-03-07T04:28:07Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12787#pullrequestreview-3907258664)
- `2026-03-17T17:02:19Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12787#pullrequestreview-3962362713)

## Inline Comment Hotspots

- `python/sglang/srt/server_args.py`: 8 inline comment(s)
- `docs/references/environment_variables.md`: 5 inline comment(s)
- `python/sglang/srt/layers/flashinfer_comm_fusion.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-03-06T19:27:46Z` `issue` by `wenscarl`; signals: h100, hopper, kernel, memory, sm100, sm90; excerpt: "@mmangkad Hi @wenscarl, didn't see this PR before opening (which also adds standalone TP AR). I see the mnnvl SM100 restriction here, but I ..." (https://github.com/sgl-project/sglang/pull/12787#issuecomment-4013647268)
- `2026-03-06T19:38:47Z` `issue` by `mmangkad`; signals: h100, hopper, kernel, memory, sm100, sm90; excerpt: "@mmangkad Hi @wenscarl, didn't see this PR before opening 19586 (which also adds standalone TP AR). I see the mnnvl SM100 restriction here, but ..." (https://github.com/sgl-project/sglang/pull/12787#issuecomment-4013733432)
- `2026-02-12T21:10:56Z` `issue` by `wenscarl`; signals: b200, hopper, sm100, sm90; excerpt: "Are you sure it works for sm90? I was working on the similar task and realized that it only worked on sm100+ GPU. It ..." (https://github.com/sgl-project/sglang/pull/12787#issuecomment-3893409203)
- `2026-03-09T19:24:26Z` `issue` by `wenscarl`; signals: b200, benchmark, flashinfer; excerpt: "@wenscarl The benchmark data looks great. But since we enable auto backend by default, can you add a line for auto backend in the ..." (https://github.com/sgl-project/sglang/pull/12787#issuecomment-4026182408)
- `2026-02-12T15:38:14Z` `issue` by `yuan-luo`; signals: sm100, sm90; excerpt: "Are you sure it works for sm90? I was working on the similar task and realized that it only worked on sm100+ GPU." (https://github.com/sgl-project/sglang/pull/12787#issuecomment-3891672860)
- `2026-02-13T08:00:56Z` `issue` by `nvpohanh`; signals: b200, hopper; excerpt: "It only targets (G)B200 system with multinode-nvlink. Hopper is not supported. If it does not work on Hopper, let's make sure that we print ..." (https://github.com/sgl-project/sglang/pull/12787#issuecomment-3895478003)
- `2026-03-02T07:46:26Z` `issue` by `mmangkad`; signals: sm100, sm90; excerpt: "Hi @wenscarl, didn't see this PR before opening 19586 (which also adds standalone TP AR). I see the mnnvl SM100 restriction here, but I ..." (https://github.com/sgl-project/sglang/pull/12787#issuecomment-3982690363)
- `2026-03-07T04:33:40Z` `issue` by `Fridge003`; signals: b200, benchmark; excerpt: "@wenscarl The benchmark data looks great. But since we enable auto backend by default, can you add a line for auto backend in the ..." (https://github.com/sgl-project/sglang/pull/12787#issuecomment-4015527275)
- `2025-11-10T13:55:16Z` `issue` by `wenscarl`; signals: flashinfer, kernel; excerpt: "@wenscarl Is this PR ready for review? There is still some issue with the kernel in flashinfer." (https://github.com/sgl-project/sglang/pull/12787#issuecomment-3511799630)
- `2026-02-12T12:16:10Z` `inline` by `nvpohanh` `docs/references/environment_variables.md`:48; signals: moe; excerpt: "@Fridge003 Question: In general, how does SGLang decide if a new knob should be an environment variable or a server arg? For example, I ..." (https://github.com/sgl-project/sglang/pull/12787#discussion_r2798567592)
- `2026-02-12T16:23:17Z` `inline` by `wenscarl` `docs/references/environment_variables.md`:48; signals: flashinfer; excerpt: "For this case, since there is already server arg: --enable-flashinfer-allreduce-fusion, thus a additional env var: SGLANG FLASHINFER ALLREDUCE FUSION BACKEND. Or we can do ..." (https://github.com/sgl-project/sglang/pull/12787#discussion_r2799817576)
- `2026-02-13T10:09:48Z` `inline` by `Fridge003` `docs/references/environment_variables.md`:48; signals: flashinfer; excerpt: "@wenscarl We can use the new argument --flashinfer-allreduce-fusion-backend, and handle the deprecated one with handle deprecated args here" (https://github.com/sgl-project/sglang/pull/12787#discussion_r2803397237)
