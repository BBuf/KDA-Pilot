# PR Discussion Digest

- Source PR: [sgl-project/sglang#15141](https://github.com/sgl-project/sglang/pull/15141)
- Source page: `sources/prs/sglang/PR-15141.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-15141`
- Generated at: `2026-05-20T15:28:07.576946+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-15T02:33:35Z`
- Merged: `2025-12-18T09:07:04Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 13 (approved=2, commented=11)
- Inline review comments: 12
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=3
- Human participants with discussion text: BBuf, Kevin-XiongC, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-15T02:35:18Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for partial rotary embeddings to the fused qk norm rope kernel, ... (https://github.com/sgl-project/sglang/pull/15141#pullrequestreview-3576191583)
- `2025-12-17T03:12:33Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/15141#pullrequestreview-3585827158)
- `2025-12-17T03:14:00Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/15141#pullrequestreview-3585829538)
- `2025-12-17T03:33:47Z` `COMMENTED` by `Kevin-XiongC` (https://github.com/sgl-project/sglang/pull/15141#pullrequestreview-3585873387)
- `2025-12-17T04:49:36Z` `COMMENTED` by `Kevin-XiongC` (https://github.com/sgl-project/sglang/pull/15141#pullrequestreview-3585994930)
- `2025-12-17T05:10:17Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/15141#pullrequestreview-3586036038)
- `2025-12-17T05:48:03Z` `COMMENTED` by `Kevin-XiongC` (https://github.com/sgl-project/sglang/pull/15141#pullrequestreview-3586111095)
- `2025-12-17T07:54:44Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/15141#pullrequestreview-3586449279)
- `2025-12-17T08:03:52Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/15141#pullrequestreview-3586475586)
- `2025-12-17T08:53:03Z` `COMMENTED` by `Kevin-XiongC` (https://github.com/sgl-project/sglang/pull/15141#pullrequestreview-3586650072)
- `2025-12-17T09:38:40Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/15141#pullrequestreview-3586837180)
- `2025-12-17T09:39:57Z` `APPROVED` by `yuan-luo` - LGTM. (https://github.com/sgl-project/sglang/pull/15141#pullrequestreview-3586845805)
- `2025-12-17T10:02:58Z` `APPROVED` by `BBuf` - LGTM (https://github.com/sgl-project/sglang/pull/15141#pullrequestreview-3586945185)

## Inline Comment Hotspots

- `sgl-kernel/csrc/moe/fused_qknorm_rope_kernel.cu`: 12 inline comment(s)

## High-Signal Discussion

- `2025-12-17T03:33:47Z` `inline` by `Kevin-XiongC` `sgl-kernel/csrc/moe/fused_qknorm_rope_kernel.cu`:203; signals: attention, hang, kernel, moe, warp; excerpt: "I think this is what the partial rotary factor parameter is designed to handle. For example, in models like GLM where this factor is ..." (https://github.com/sgl-project/sglang/pull/15141#discussion_r2625475762)
- `2025-12-17T03:14:00Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/fused_qknorm_rope_kernel.cu`:203; signals: kernel, moe; excerpt: "It turns out this function only works for in rotary lanes, this function can be refactored a bit to make it clear." (https://github.com/sgl-project/sglang/pull/15141#discussion_r2625440414)
- `2025-12-17T04:49:36Z` `inline` by `Kevin-XiongC` `sgl-kernel/csrc/moe/fused_qknorm_rope_kernel.cu`:203; signals: kernel, moe; excerpt: "It turns out this function only works for in rotary lanes, this function can be refactored a bit to make it clear. Done." (https://github.com/sgl-project/sglang/pull/15141#discussion_r2625586869)
- `2025-12-17T05:48:02Z` `inline` by `Kevin-XiongC` `sgl-kernel/csrc/moe/fused_qknorm_rope_kernel.cu`:200; signals: kernel, moe; excerpt: "The unrotated part still needs to be written back to qkv buffer, so we can not return. If it is not clear enough, maybe ..." (https://github.com/sgl-project/sglang/pull/15141#discussion_r2625686856)
- `2025-12-17T08:03:52Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/fused_qknorm_rope_kernel.cu`:222; signals: kernel, moe; excerpt: "Here needs to have the condition that half rotary lanes is power of 2. For example if rotary lanes = 24 and half = ..." (https://github.com/sgl-project/sglang/pull/15141#discussion_r2625999708)
- `2025-12-17T08:53:03Z` `inline` by `Kevin-XiongC` `sgl-kernel/csrc/moe/fused_qknorm_rope_kernel.cu`:222; signals: kernel, moe; excerpt: "Here needs to have the condition that half rotary lanes is power of 2. For example if rotary lanes = 24 and half = ..." (https://github.com/sgl-project/sglang/pull/15141#discussion_r2626143521)
- `2025-12-17T03:12:33Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/fused_qknorm_rope_kernel.cu`:203; signals: kernel, moe; excerpt: "If in rotary == false, no action is taken, is it expected?" (https://github.com/sgl-project/sglang/pull/15141#discussion_r2625438216)
- `2025-12-17T05:10:17Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/fused_qknorm_rope_kernel.cu`:200; signals: kernel, moe; excerpt: "Can we use guard clause here to avoid nested if else?" (https://github.com/sgl-project/sglang/pull/15141#discussion_r2625622744)
- `2025-12-17T07:54:44Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/fused_qknorm_rope_kernel.cu`:200; signals: kernel, moe; excerpt: "Accepted." (https://github.com/sgl-project/sglang/pull/15141#discussion_r2625976478)
- `2025-12-17T09:38:40Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/fused_qknorm_rope_kernel.cu`:222; signals: kernel, moe; excerpt: "Adding assertion is fine. Please add it. Thanks!" (https://github.com/sgl-project/sglang/pull/15141#discussion_r2626301022)
- `2025-12-17T02:51:33Z` `issue` by `Kevin-XiongC`; signals: general review; excerpt: "Could you paste the GLM4.6 test acc result? Either CI or manual will do. Okay. I've added results to the PR. However, the runnable ..." (https://github.com/sgl-project/sglang/pull/15141#issuecomment-3663401118)
- `2025-12-17T03:09:50Z` `issue` by `yuan-luo`; signals: general review; excerpt: "Could you paste the GLM4.6 test acc result? Either CI or manual will do. Okay. I've added results to the PR. However, the runnable ..." (https://github.com/sgl-project/sglang/pull/15141#issuecomment-3663436042)
