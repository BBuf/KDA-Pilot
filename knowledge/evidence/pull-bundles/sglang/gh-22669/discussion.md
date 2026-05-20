# PR Discussion Digest

- Source PR: [sgl-project/sglang#22669](https://github.com/sgl-project/sglang/pull/22669)
- Source page: `sources/prs/sglang/PR-22669.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22669`
- Generated at: `2026-05-20T15:29:28.887442+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-13T06:49:22Z`
- Merged: `2026-05-20T07:36:27Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 13 (approved=1, changes_requested=1, commented=10, dismissed=1)
- Inline review comments: 15
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=7, outdated=8
- Human participants with discussion text: YAMY1234, bobboli, ch-wan, leejnau, nvpohanh, samuellees, trevor-m
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-13T07:10:10Z` `COMMENTED` by `YAMY1234` (https://github.com/sgl-project/sglang/pull/22669#pullrequestreview-4096938411)
- `2026-04-13T07:12:32Z` `COMMENTED` by `YAMY1234` (https://github.com/sgl-project/sglang/pull/22669#pullrequestreview-4096948929)
- `2026-04-13T07:30:55Z` `COMMENTED` by `YAMY1234` (https://github.com/sgl-project/sglang/pull/22669#pullrequestreview-4097048117)
- `2026-04-13T20:19:44Z` `CHANGES_REQUESTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/22669#pullrequestreview-4101614564)
- `2026-04-13T22:28:10Z` `DISMISSED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/22669#pullrequestreview-4102323678)
- `2026-04-14T23:29:37Z` `COMMENTED` by `leejnau` (https://github.com/sgl-project/sglang/pull/22669#pullrequestreview-4109879239)
- `2026-04-15T23:40:48Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/22669#pullrequestreview-4117531266)
- `2026-04-15T23:41:12Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/22669#pullrequestreview-4117532443)
- `2026-04-15T23:41:40Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/22669#pullrequestreview-4117533633)
- `2026-04-30T12:45:13Z` `COMMENTED` by `bobboli` (https://github.com/sgl-project/sglang/pull/22669#pullrequestreview-4205195648)
- `2026-05-06T09:06:47Z` `COMMENTED` by `samuellees` (https://github.com/sgl-project/sglang/pull/22669#pullrequestreview-4234687715)
- `2026-05-20T06:01:29Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/22669#pullrequestreview-4325576616)
- `2026-05-20T06:04:55Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/22669#pullrequestreview-4325596975)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`: 7 inline comment(s)
- `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutedsl.py`: 4 inline comment(s)
- `python/sglang/srt/server_args.py`: 3 inline comment(s)
- `test/registered/moe/test_flashinfer_a2a_cutedsl_v2.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-13T20:19:33Z` `inline` by `trevor-m` `python/sglang/srt/server_args.py`:2759; signals: cutlass, flashinfer, fp4, moe, nvfp4, perf; excerpt: "We should be able to support nvfp4 dispatch and it's necessary for good perf, see for trtllm gen moe example and the flashinfer cutlass ..." (https://github.com/sgl-project/sglang/pull/22669#discussion_r3075578788)
- `2026-04-13T07:30:55Z` `inline` by `YAMY1234` `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutedsl.py`:411; signals: cute, flashinfer, fp4, moe, nvfp4; excerpt: "Optional: Are we able to verify this path? If it is not supported, could we consider forcibly disabling NVFP4 DISPATCH in server args when ..." (https://github.com/sgl-project/sglang/pull/22669#discussion_r3071464083)
- `2026-04-14T23:29:37Z` `inline` by `leejnau` `python/sglang/srt/server_args.py`:2875; signals: cute, flashinfer, fp4, moe, nvfp4; excerpt: "The flashinfer cutedsl MoE backend currently requires that SGLANG MOE NVFP4 DISPATCH is set to False. We can manually set it to False on ..." (https://github.com/sgl-project/sglang/pull/22669#discussion_r3083105476)
- `2026-04-15T23:40:43Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:218; signals: flashinfer, kernel, moe, perf; excerpt: "This will trigger moe a2a sanitize expert ids kernel, we should confirm if it's necessary otherwise it will reduce the perf" (https://github.com/sgl-project/sglang/pull/22669#discussion_r3090010954)
- `2026-05-20T06:01:29Z` `inline` by `ch-wan` `test/registered/moe/test_flashinfer_a2a_cutedsl_v2.py`:21; signals: cute, flashinfer, moe, register; excerpt: "let's move it to stage="extra-b"" (https://github.com/sgl-project/sglang/pull/22669#discussion_r3271546407)
- `2026-04-13T20:18:54Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutedsl.py`:411; signals: cute, flashinfer, moe; excerpt: "Why are we not able to verify this?" (https://github.com/sgl-project/sglang/pull/22669#discussion_r3075575944)
- `2026-04-13T22:28:05Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutedsl.py`:411; signals: cute, flashinfer, moe; excerpt: "See we can skip the interleave depending on which moe runner is used" (https://github.com/sgl-project/sglang/pull/22669#discussion_r3076168156)
- `2026-04-15T23:41:40Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutedsl.py`:411; signals: cute, flashinfer, moe; excerpt: "pushed commit to support this" (https://github.com/sgl-project/sglang/pull/22669#discussion_r3090013477)
- `2026-04-13T07:12:32Z` `inline` by `YAMY1234` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:169; signals: flashinfer, moe; excerpt: "Will these still be needed in other places? since we are removing the usage of these variables in this file" (https://github.com/sgl-project/sglang/pull/22669#discussion_r3071382489)
- `2026-04-13T20:15:13Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:103; signals: flashinfer, moe; excerpt: "8192 seems quite large for the default, I don't think the batch size will ever be this high for decode. For DEP32 this will ..." (https://github.com/sgl-project/sglang/pull/22669#discussion_r3075558746)
- `2026-04-30T12:45:13Z` `inline` by `bobboli` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:218; signals: flashinfer, moe; excerpt: "This is necessary, the recv buffer of A2A is allocated redundantly. If the invalid slots are not sanitized, they will be sent for useless ..." (https://github.com/sgl-project/sglang/pull/22669#discussion_r3167992105)
- `2026-04-13T07:10:10Z` `inline` by `YAMY1234` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:175; signals: flashinfer, moe; excerpt: "Maybe we could rename it, something like is idle rank for better clarity?" (https://github.com/sgl-project/sglang/pull/22669#discussion_r3071372440)
