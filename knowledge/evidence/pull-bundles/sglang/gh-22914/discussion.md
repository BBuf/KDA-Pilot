# PR Discussion Digest

- Source PR: [sgl-project/sglang#22914](https://github.com/sgl-project/sglang/pull/22914)
- Source page: `sources/prs/sglang/PR-22914.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22914`
- Generated at: `2026-05-20T15:29:32.574680+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-16T00:29:13Z`
- Merged: `2026-04-20T04:35:36Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 5
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=4
- Human participants with discussion text: Fridge003, kpham-sgl
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-16T05:33:33Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/22914#pullrequestreview-4118439337)
- `2026-04-17T20:27:01Z` `APPROVED` by `kpham-sgl` (https://github.com/sgl-project/sglang/pull/22914#pullrequestreview-4131897098)
- `2026-04-18T02:13:23Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/22914#pullrequestreview-4133260267)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 1 inline comment(s)
- `python/sglang/srt/models/deepseek_nextn.py`: 1 inline comment(s)
- `python/sglang/srt/layers/attention/nsa/utils.py`: 1 inline comment(s)
- `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`: 1 inline comment(s)
- `python/sglang/srt/layers/utils/cp_utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-18T02:13:20Z` `inline` by `Fridge003` `python/sglang/srt/layers/utils/cp_utils.py`:511; signals: hang, moe; excerpt: "For the change here. Maybe we should check whether the model applies nsa cp, since get topk ragged with cp isn't called for other ..." (https://github.com/sgl-project/sglang/pull/22914#discussion_r3104284319)
- `2026-04-16T05:07:57Z` `inline` by `Fridge003` `python/sglang/srt/models/deepseek_v2.py`:2297; signals: aligned; excerpt: "The metadata here shouldn't be set as True. It should get aligned with the codes before refactor" (https://github.com/sgl-project/sglang/pull/22914#discussion_r3090886675)
- `2026-04-16T05:08:11Z` `inline` by `Fridge003` `python/sglang/srt/models/deepseek_nextn.py`:277; signals: aligned; excerpt: "The metadata here shouldn't be set as True. It should get aligned with the codes before refactor" (https://github.com/sgl-project/sglang/pull/22914#discussion_r3090887289)
- `2026-04-16T05:27:26Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa/utils.py`:299; signals: attention; excerpt: "Move this part of comments to cp all gather reorganized into tensor function in cp utils.py" (https://github.com/sgl-project/sglang/pull/22914#discussion_r3090944560)
- `2026-04-17T20:26:30Z` `inline` by `kpham-sgl` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:864; signals: attention; excerpt: "Nice!" (https://github.com/sgl-project/sglang/pull/22914#discussion_r3103073908)
