# PR Discussion Digest

- Source PR: [sgl-project/sglang#4643](https://github.com/sgl-project/sglang/pull/4643)
- Source page: `sources/prs/sglang/PR-4643.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4643`
- Generated at: `2026-05-20T15:30:12.932375+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-21T03:28:22Z`
- Merged: `2025-03-22T21:30:34Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 3 (changes_requested=1, commented=2)
- Inline review comments: 8
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=0, outdated=6
- Human participants with discussion text: Edenzzzz, Huixxi, ch-wan, xutizhou
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-03-21T05:54:47Z` `CHANGES_REQUESTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/4643#pullrequestreview-2704770682)
- `2025-03-21T21:04:25Z` `COMMENTED` by `Edenzzzz` (https://github.com/sgl-project/sglang/pull/4643#pullrequestreview-2707256398)
- `2025-03-21T21:19:07Z` `COMMENTED` by `Edenzzzz` (https://github.com/sgl-project/sglang/pull/4643#pullrequestreview-2707283326)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/ep_moe/kernels.py`: 6 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/token_dispatcher.py`: 1 inline comment(s)
- `python/sglang/srt/models/deepseek_v2.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-21T05:42:41Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:21; signals: kernel, moe, triton; excerpt: "compute src2dst triton kernel and deepep compute src2dst triton kernel are defined twice." (https://github.com/sgl-project/sglang/pull/4643#discussion_r2006884129)
- `2025-03-21T05:45:28Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:32; signals: kernel, moe, triton; excerpt: "Why developing a triton kernel is necessary? Is it faster?" (https://github.com/sgl-project/sglang/pull/4643#discussion_r2006887390)
- `2025-03-21T05:29:11Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:45; signals: kernel, moe; excerpt: "It can be init using torch.empty" (https://github.com/sgl-project/sglang/pull/4643#discussion_r2006873981)
- `2025-03-21T05:30:05Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:61; signals: kernel, moe; excerpt: "debugging code?" (https://github.com/sgl-project/sglang/pull/4643#discussion_r2006874530)
- `2025-03-21T05:47:29Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:21; signals: kernel, moe; excerpt: "It is defined twice." (https://github.com/sgl-project/sglang/pull/4643#discussion_r2006889080)
- `2025-03-21T05:48:40Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:98; signals: kernel, moe; excerpt: "It is defined twice." (https://github.com/sgl-project/sglang/pull/4643#discussion_r2006890001)
- `2025-03-21T21:04:25Z` `inline` by `Edenzzzz` `python/sglang/srt/layers/moe/ep_moe/token_dispatcher.py`:355; signals: moe; excerpt: "Use torch.empty?" (https://github.com/sgl-project/sglang/pull/4643#discussion_r2008327965)
- `2025-03-21T21:19:07Z` `inline` by `Edenzzzz` `python/sglang/srt/models/deepseek_v2.py`:297; signals: general review; excerpt: "Should we add some short comments on the meaning/examples of reorder topk ids and seg indptr for readability?" (https://github.com/sgl-project/sglang/pull/4643#discussion_r2008344853)
