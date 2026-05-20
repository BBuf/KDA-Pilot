# PR Discussion Digest

- Source PR: [sgl-project/sglang#19425](https://github.com/sgl-project/sglang/pull/19425)
- Source page: `sources/prs/sglang/PR-19425.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19425`
- Generated at: `2026-05-20T15:28:51.370637+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-26T12:23:59Z`
- Merged: `2026-02-27T01:11:59Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 4 (approved=2, changes_requested=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: BowenBao, HaiShaw
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-26T12:25:54Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors how quantization exclusion layers are handled in QuarkConfig, making the logic more ... (https://github.com/sgl-project/sglang/pull/19425#pullrequestreview-3860597361)
- `2026-02-26T17:19:49Z` `APPROVED` by `BowenBao` (https://github.com/sgl-project/sglang/pull/19425#pullrequestreview-3862453370)
- `2026-02-26T20:35:33Z` `CHANGES_REQUESTED` by `HaiShaw` - Ideally we should update model, instead of changing common code to adapt to old model produced. Can you ... (https://github.com/sgl-project/sglang/pull/19425#pullrequestreview-3863409925)
- `2026-02-26T23:28:50Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/19425#pullrequestreview-3864113777)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/quark/quark.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-26T20:35:33Z` `review` `CHANGES_REQUESTED` by `HaiShaw`; signals: hang; excerpt: "Ideally we should update model, instead of changing common code to adapt to old model produced. Can you help look into this? @BowenBao" (https://github.com/sgl-project/sglang/pull/19425#pullrequestreview-3863409925)
- `2026-02-26T21:50:04Z` `issue` by `BowenBao`; signals: general review; excerpt: "@HaiShaw this is on sglang side. The mtp layers in original deepseek r1 0528 model are named as model.layers.61. see Quark's exclude pattern is ..." (https://github.com/sgl-project/sglang/pull/19425#issuecomment-3969440025)
