# PR Discussion Digest

- Source PR: [sgl-project/sglang#20394](https://github.com/sgl-project/sglang/pull/20394)
- Source page: `sources/prs/sglang/PR-20394.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-20394`
- Generated at: `2026-05-20T15:29:02.493215+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-12T00:51:41Z`
- Merged: `2026-04-02T06:02:07Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 6
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=4
- Human participants with discussion text: Fridge003, JustinTong0323, trevor-m, zianglih
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-17T05:57:16Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/20394#pullrequestreview-3958381775)
- `2026-03-17T08:11:46Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/20394#pullrequestreview-3958880025)
- `2026-03-17T18:23:09Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/20394#pullrequestreview-3962859824)
- `2026-03-17T18:26:27Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/20394#pullrequestreview-3962876950)
- `2026-03-31T20:45:16Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/20394#pullrequestreview-4040072498)
- `2026-03-31T20:47:10Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/20394#pullrequestreview-4040080989)
- `2026-04-01T20:45:44Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/20394#pullrequestreview-4046961326)
- `2026-04-02T06:01:55Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/20394#pullrequestreview-4048537469)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`: 3 inline comment(s)
- `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8.py`: 1 inline comment(s)
- `python/sglang/srt/layers/moe/topk.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-17T08:11:46Z` `inline` by `zianglih` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:409; signals: accuracy, flashinfer, hang, moe; excerpt: "FlashInfer internally still uses this type for routing/rescaling even if using the routed moe backend. It is not a noop. Previous code is required ..." (https://github.com/sgl-project/sglang/pull/20394#discussion_r2945062003)
- `2026-03-17T06:01:14Z` `issue` by `zianglih`; signals: block, flashinfer, kernel, moe; excerpt: "Hi @trevor-m , the key motivation to the original explicit --moe-runner-backend=flashinfer trtllm routed flag is to support MoE expert rollout routing replay for RL ..." (https://github.com/sgl-project/sglang/pull/20394#issuecomment-4072576973)
- `2026-03-17T05:57:16Z` `inline` by `zianglih` `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`:189; signals: flashinfer, moe, register; excerpt: "Can we keep routed unit tests since routed and fused are 2 separate code paths?" (https://github.com/sgl-project/sglang/pull/20394#discussion_r2944570974)
- `2026-03-31T20:47:05Z` `inline` by `Fridge003` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:444; signals: flashinfer, moe; excerpt: "@trevor-m Is it included in flashinfer 0.6.7? We will upgrade to this version this week" (https://github.com/sgl-project/sglang/pull/20394#discussion_r3018318392)
- `2026-04-01T20:45:43Z` `inline` by `trevor-m` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:444; signals: flashinfer, moe; excerpt: "Looks like the fix was merged 2 days ago, but its not in any release branch" (https://github.com/sgl-project/sglang/pull/20394#discussion_r3024554626)
- `2026-03-17T18:23:09Z` `inline` by `zianglih` `python/sglang/srt/layers/quantization/fp8.py`:1185; signals: fp8; excerpt: "should we revert here since both backends require the same swizzling" (https://github.com/sgl-project/sglang/pull/20394#discussion_r2948729968)
- `2026-03-17T18:26:27Z` `inline` by `zianglih` `python/sglang/srt/layers/moe/topk.py`:240; signals: moe; excerpt: "this seems unused now" (https://github.com/sgl-project/sglang/pull/20394#discussion_r2948747471)
