# PR Discussion Digest

- Source PR: [sgl-project/sglang#16076](https://github.com/sgl-project/sglang/pull/16076)
- Source page: `sources/prs/sglang/PR-16076.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-16076`
- Generated at: `2026-05-20T15:28:20.406152+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-29T12:07:16Z`
- Merged: `2025-12-29T14:50:16Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 5 (commented=5)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: McZyWu, randgun
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-29T12:08:41Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enhances the accuracy for the kimi-vl-instruct-a3b model on NPU. The changes involve: 1. ... (https://github.com/sgl-project/sglang/pull/16076#pullrequestreview-3615733584)
- `2025-12-29T13:36:53Z` `COMMENTED` by `randgun` (https://github.com/sgl-project/sglang/pull/16076#pullrequestreview-3615900772)
- `2025-12-29T13:39:00Z` `COMMENTED` by `randgun` (https://github.com/sgl-project/sglang/pull/16076#pullrequestreview-3615904989)
- `2025-12-29T13:43:18Z` `COMMENTED` by `McZyWu` (https://github.com/sgl-project/sglang/pull/16076#pullrequestreview-3615913092)
- `2025-12-29T13:43:26Z` `COMMENTED` by `McZyWu` (https://github.com/sgl-project/sglang/pull/16076#pullrequestreview-3615913362)

## Inline Comment Hotspots

- `python/sglang/srt/hardware_backend/npu/moe/topk.py`: 3 inline comment(s)
- `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-29T13:36:53Z` `inline` by `randgun` `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`:103; signals: attention, cache, mla; excerpt: "Do not use callback func, use forward batch.token to kv pool.set kv buffer( m, forward batch.out cache loc, kv a.unsqueeze(1), k pe ) instead ..." (https://github.com/sgl-project/sglang/pull/16076#discussion_r2650995584)
- `2025-12-29T13:43:18Z` `inline` by `McZyWu` `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`:103; signals: attention, mla; excerpt: "Thank you. Your reviews are extremely valuable. I've adopted." (https://github.com/sgl-project/sglang/pull/16076#discussion_r2651007609)
- `2025-12-29T13:43:26Z` `inline` by `McZyWu` `python/sglang/srt/hardware_backend/npu/moe/topk.py`:41; signals: hang, moe; excerpt: "Thank you. Your advice has just helped me make the changes. Adopted" (https://github.com/sgl-project/sglang/pull/16076#discussion_r2651007823)
- `2025-12-29T13:39:00Z` `inline` by `randgun` `python/sglang/srt/hardware_backend/npu/moe/topk.py`:41; signals: moe; excerpt: "npu moe gating top k has supported router logits.shape[-1] <= 2048 in pta 7.2.0 version." (https://github.com/sgl-project/sglang/pull/16076#discussion_r2650999715)
