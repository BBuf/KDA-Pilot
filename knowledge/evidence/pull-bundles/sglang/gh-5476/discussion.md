# PR Discussion Digest

- Source PR: [sgl-project/sglang#5476](https://github.com/sgl-project/sglang/pull/5476)
- Source page: `sources/prs/sglang/PR-5476.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-5476`
- Generated at: `2026-05-20T15:30:26.163437+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-16T16:01:15Z`
- Merged: `2025-04-18T08:13:57Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 6
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: Edenzzzz, Fridge003, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-16T18:58:23Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/5476#pullrequestreview-2773554727)
- `2025-04-16T19:46:09Z` `COMMENTED` by `Edenzzzz` (https://github.com/sgl-project/sglang/pull/5476#pullrequestreview-2773668163)
- `2025-04-16T22:37:27Z` `COMMENTED` by `Edenzzzz` (https://github.com/sgl-project/sglang/pull/5476#pullrequestreview-2774022981)
- `2025-04-17T00:37:15Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/5476#pullrequestreview-2774218735)
- `2025-04-17T00:37:46Z` `APPROVED` by `Fridge003` - LGTM (https://github.com/sgl-project/sglang/pull/5476#pullrequestreview-2774219535)
- `2025-04-17T01:55:09Z` `COMMENTED` by `Edenzzzz` (https://github.com/sgl-project/sglang/pull/5476#pullrequestreview-2774326294)
- `2025-04-17T02:12:05Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/5476#pullrequestreview-2774343645)
- `2025-04-18T08:13:48Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5476#pullrequestreview-2778035662)

## Inline Comment Hotspots

- `docs/backend/server_arguments.md`: 6 inline comment(s)

## High-Signal Discussion

- `2025-04-16T18:58:11Z` `inline` by `Fridge003` `docs/backend/server_arguments.md`:197; signals: attention, cache, kv cache, throughput; excerpt: "There is a little mistake here: ragged prefill saves kv cache before doing attention. I think ragged prefill increases throughput by using multi-head attention ..." (https://github.com/sgl-project/sglang/pull/5476#discussion_r2047562814)
- `2025-04-17T00:37:15Z` `inline` by `Fridge003` `docs/backend/server_arguments.md`:197; signals: attention, cache, kv cache; excerpt: "For vanilla attention, the kv cache is saved before doing attention." (https://github.com/sgl-project/sglang/pull/5476#discussion_r2047994551)
- `2025-04-16T19:46:09Z` `inline` by `Edenzzzz` `docs/backend/server_arguments.md`:197; signals: attention; excerpt: "In the case of vanilla attention this is correct?" (https://github.com/sgl-project/sglang/pull/5476#discussion_r2047637068)
- `2025-04-17T02:12:05Z` `inline` by `Fridge003` `docs/backend/server_arguments.md`:197; signals: attention; excerpt: "I mean before the computation part of attention" (https://github.com/sgl-project/sglang/pull/5476#discussion_r2048077420)
- `2025-04-16T22:37:27Z` `inline` by `Edenzzzz` `docs/backend/server_arguments.md`:197; signals: general review; excerpt: "fixed" (https://github.com/sgl-project/sglang/pull/5476#discussion_r2047867257)
- `2025-04-17T01:55:08Z` `inline` by `Edenzzzz` `docs/backend/server_arguments.md`:197; signals: general review; excerpt: "Actually it's after?" (https://github.com/sgl-project/sglang/pull/5476#discussion_r2048065051)
