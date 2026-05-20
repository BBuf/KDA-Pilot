# PR Discussion Digest

- Source PR: [vllm-project/vllm#27190](https://github.com/vllm-project/vllm/pull/27190)
- Source page: `sources/prs/vllm/PR-27190.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-27190`
- Generated at: `2026-05-20T15:38:13.568323+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-20T09:19:10Z`
- Merged: `2025-10-26T07:08:52Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: DarkLight1337, JartX, tjtanaa, zhewenl
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-10-20T09:21:17Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a bug where ViT FlashAttention was incorrectly enabled on ROCm RDNA3 devices, ... (https://github.com/vllm-project/vllm/pull/27190#pullrequestreview-3355667192)
- `2025-10-21T07:10:33Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/27190#pullrequestreview-3359054045)
- `2025-10-21T07:12:47Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/27190#pullrequestreview-3359063491)
- `2025-10-21T07:13:25Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/27190#pullrequestreview-3359066039)
- `2025-10-21T07:25:21Z` `COMMENTED` by `JartX` (https://github.com/vllm-project/vllm/pull/27190#pullrequestreview-3359113065)
- `2025-10-25T16:08:22Z` `APPROVED` by `DarkLight1337` - Thanks for fixing! (https://github.com/vllm-project/vllm/pull/27190#pullrequestreview-3380114028)

## Inline Comment Hotspots

- `vllm/attention/layer.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-10-22T11:35:41Z` `issue` by `JartX`; signals: attention, cuda, dtype; excerpt: "@tjtanaa dont need edit the rocm.py it works fine, the problem is in attention/layer.py Your recommendation fails, because: FA support is detected for on ..." (https://github.com/vllm-project/vllm/pull/27190#issuecomment-3431933852)
- `2025-10-21T07:25:21Z` `inline` by `JartX` `vllm/attention/layer.py`:106; signals: attention, hang; excerpt: "@tjtanaa The first step was simply to check if it was rocm and if it was on gfx1x and if so, return Backend.TORCH SDPA, ..." (https://github.com/vllm-project/vllm/pull/27190#discussion_r2447010650)
- `2025-10-21T07:10:33Z` `inline` by `tjtanaa` `vllm/attention/layer.py`:107; signals: attention; excerpt: "We shouldn't need this condition, whether to use the Backend.ROCM AITER FA, it is determined in those model.py files." (https://github.com/vllm-project/vllm/pull/27190#discussion_r2446964538)
- `2025-10-21T07:12:47Z` `inline` by `tjtanaa` `vllm/attention/layer.py`:106; signals: attention; excerpt: "This condition was crafted for ROCm platform (on gfx9()). On on gfx9(), we will always attempt to use flash attn, but if it does ..." (https://github.com/vllm-project/vllm/pull/27190#discussion_r2446971899)
- `2025-10-21T07:13:25Z` `inline` by `tjtanaa` `vllm/attention/layer.py`:111; signals: attention; excerpt: "As mentioned above, this condition and its content is also applicable to ROCm on gfx9." (https://github.com/vllm-project/vllm/pull/27190#discussion_r2446973803)
- `2025-10-21T10:29:30Z` `issue` by `tjtanaa`; signals: attention; excerpt: "Suggestions 1. Add torch sdpa fallback 2. Update the default CC @DarkLight1337 (as I am not familiar the latest abstraction of decoupling ViT Attention ..." (https://github.com/vllm-project/vllm/pull/27190#issuecomment-3425864398)
- `2025-10-22T14:52:38Z` `issue` by `tjtanaa`; signals: attention; excerpt: "@JartX Your suggestions LGTM. But can you update the rocm.py as well? If you look for get vit attn backend, you will see that ..." (https://github.com/vllm-project/vllm/pull/27190#issuecomment-3432778545)
- `2025-10-22T15:17:00Z` `issue` by `JartX`; signals: general review; excerpt: "@JartX Tus sugerencias LGTM. rocm.py¿Pero también se puede actualizar [ ?]? Si buscas [ get vit attn backend, verás que llaman a esta función ..." (https://github.com/vllm-project/vllm/pull/27190#issuecomment-3432964215)
- `2025-10-25T16:29:21Z` `issue` by `JartX`; signals: general review; excerpt: "Sorry @DarkLight1337 the pre-commit was missing now all its okays, can you reenable the auto-merge, please? many thanks (L)" (https://github.com/vllm-project/vllm/pull/27190#issuecomment-3446881753)
