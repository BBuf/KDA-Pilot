# PR Discussion Digest

- Source PR: [sgl-project/sglang#14668](https://github.com/sgl-project/sglang/pull/14668)
- Source page: `sources/prs/sglang/PR-14668.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14668`
- Generated at: `2026-05-20T15:28:03.090850+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-08T20:36:17Z`
- Merged: `2026-01-24T14:59:55Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 20 (approved=2, commented=18)
- Inline review comments: 29
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=13, outdated=10
- Human participants with discussion text: Fridge003, ch-wan, djns99, fzyzcjy, trevor-m
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-08T20:51:38Z` `APPROVED` by `djns99` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3553968676)
- `2025-12-09T00:07:32Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3554647609)
- `2025-12-09T00:07:50Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3554648640)
- `2025-12-09T00:10:09Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3554654653)
- `2025-12-09T00:11:39Z` `COMMENTED` by `djns99` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3554658295)
- `2025-12-09T00:14:28Z` `COMMENTED` by `djns99` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3554666572)
- `2025-12-09T00:36:38Z` `COMMENTED` by `djns99` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3554728491)
- `2025-12-10T00:44:42Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3560270019)
- `2025-12-10T01:48:01Z` `COMMENTED` by `djns99` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3560392219)
- `2025-12-11T01:54:37Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3565289050)
- `2025-12-12T09:25:24Z` `COMMENTED` by `ch-wan` - We also need to update this document: (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3570941280)
- `2025-12-17T01:41:11Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3585652802)
- `2025-12-17T01:41:33Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3585653766)
- `2025-12-17T01:48:33Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3585669916)
- `2025-12-17T02:00:53Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3585703570)
- `2025-12-17T02:00:59Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3585703838)
- `2025-12-17T02:01:21Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3585704882)
- `2025-12-18T19:30:13Z` `COMMENTED` by `ch-wan` - LGTM in general. Can we add a unittest for this new feature? Also, we need to update this ... (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3594715848)
- `2025-12-22T23:09:09Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3606041874)
- `2026-01-17T07:18:00Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/14668#pullrequestreview-3673565396)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`: 26 inline comment(s)
- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 2 inline comment(s)
- `python/sglang/test/test_flashinfer_dispatcher.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-22T23:36:25Z` `issue` by `trevor-m`; signals: block, cute, cutlass, flashinfer, fp4, hang, moe; excerpt: "@trevor-m: I can give it a try Hi, is there any updates about that? if I understand correctly trtllm moe should be used for ..." (https://github.com/sgl-project/sglang/pull/14668#issuecomment-3787304933)
- `2025-12-09T00:07:32Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:144; signals: accuracy, flashinfer, fp4, moe; excerpt: "The dummy token still has to go through fp4 quantize and moe so I want the values initialized to something valid that won't affect ..." (https://github.com/sgl-project/sglang/pull/14668#discussion_r2600578542)
- `2025-12-09T00:10:09Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:103; signals: alignment, flashinfer, moe; excerpt: "Thanks, done. FYI I had to pad to 512mb alignment otherwise i hit this error. Maybe we should add an alignment check somewhere." (https://github.com/sgl-project/sglang/pull/14668#discussion_r2600582853)
- `2025-12-09T00:14:28Z` `inline` by `djns99` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:103; signals: block, flashinfer, moe; excerpt: "Hmm good catch, that seems like a bug in the implementation. We shouldn't be flattening it if we have non-contiguous MNNVL blocks. I believe ..." (https://github.com/sgl-project/sglang/pull/14668#discussion_r2600591916)
- `2025-12-09T00:36:38Z` `inline` by `djns99` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:103; signals: flashinfer, hang, moe; excerpt: "Can you test making this change to moe a2a wrap payload tensor in workspace in flashinfer and seeing if it works for you. I ..." (https://github.com/sgl-project/sglang/pull/14668#discussion_r2600635151)
- `2025-12-10T00:44:41Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:103; signals: flashinfer, hang, moe; excerpt: "I tried your change and it appears to have the same issue: Based on the log, it looks like the internal Mnnvl buffer has ..." (https://github.com/sgl-project/sglang/pull/14668#discussion_r2604810419)
- `2025-12-12T09:06:59Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:145; signals: flashinfer, memory, moe; excerpt: "What's the size of one workspace? Each layer may have an independent workspace, which wastes a lot of memory. Can we have a global ..." (https://github.com/sgl-project/sglang/pull/14668#discussion_r2613472262)
- `2025-12-09T00:07:50Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:48; signals: cutlass, flashinfer, moe; excerpt: "Thanks, for now I will only enable this for flashinfer cutlass moe path." (https://github.com/sgl-project/sglang/pull/14668#discussion_r2600579219)
- `2025-12-17T01:41:11Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:133; signals: flashinfer, moe; excerpt: "This "Mapping" class is a bit confusing because it comes from the internals of TRT-LLM and has a bunch of functionality that is unused ..." (https://github.com/sgl-project/sglang/pull/14668#discussion_r2625296667)
- `2025-12-17T01:48:33Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:173; signals: flashinfer, moe; excerpt: "Currently the flashinfer a2a requires at least 1 token per rank, but in sglang some dp workers can have 0 tokens. To work around ..." (https://github.com/sgl-project/sglang/pull/14668#discussion_r2625308853)
- `2026-01-17T07:17:58Z` `inline` by `Fridge003` `python/sglang/test/test_flashinfer_dispatcher.py`:1; signals: flashinfer, register; excerpt: "Can we move this test to test/srt/ep and register it at nightly test. Can open a following PR for this" (https://github.com/sgl-project/sglang/pull/14668#discussion_r2700718457)
- `2025-12-08T20:41:23Z` `inline` by `djns99` `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`:103; signals: flashinfer, moe; excerpt: "We should calculate the workspace size using the helper function instead of doing this now" (https://github.com/sgl-project/sglang/pull/14668#discussion_r2600060409)
