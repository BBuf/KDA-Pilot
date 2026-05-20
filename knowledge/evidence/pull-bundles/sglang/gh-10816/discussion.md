# PR Discussion Digest

- Source PR: [sgl-project/sglang#10816](https://github.com/sgl-project/sglang/pull/10816)
- Source page: `sources/prs/sglang/PR-10816.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-10816`
- Generated at: `2026-05-20T15:27:21.838200+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-23T17:19:00Z`
- Merged: `2025-09-30T02:16:17Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: samuellees, yizhang2077, zhyncs
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-23T17:21:30Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the attention backend registry to better support hybrid models like Qwen3-Next. It ... (https://github.com/sgl-project/sglang/pull/10816#pullrequestreview-3258969798)
- `2025-09-24T14:30:46Z` `COMMENTED` by `samuellees` (https://github.com/sgl-project/sglang/pull/10816#pullrequestreview-3263227939)
- `2025-09-24T15:19:24Z` `COMMENTED` by `samuellees` (https://github.com/sgl-project/sglang/pull/10816#pullrequestreview-3263436289)
- `2025-09-24T16:41:13Z` `APPROVED` by `yizhang2077` - Once ci pass, it can be merged (https://github.com/sgl-project/sglang/pull/10816#pullrequestreview-3263764783)
- `2025-09-25T06:38:41Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/10816#pullrequestreview-3265998693)

## Inline Comment Hotspots

- `python/sglang/srt/server_args.py`: 2 inline comment(s)
- `python/sglang/srt/layers/attention/attention_registry.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-24T14:30:46Z` `inline` by `samuellees` `python/sglang/srt/layers/attention/attention_registry.py`:70; signals: attention; excerpt: "I think it is optional since doing this will make the code harder to read." (https://github.com/sgl-project/sglang/pull/10816#discussion_r2376010980)
- `2025-09-24T15:19:24Z` `inline` by `samuellees` `python/sglang/srt/server_args.py`:769; signals: general review; excerpt: "Add a check and hint in attn backend wrapper for hybrid GDN model with NPU. cc @ping1jing2 for a very kindly remind, because I ..." (https://github.com/sgl-project/sglang/pull/10816#discussion_r2376156736)
