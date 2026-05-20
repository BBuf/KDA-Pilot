# PR Discussion Digest

- Source PR: [sgl-project/sglang#16685](https://github.com/sgl-project/sglang/pull/16685)
- Source page: `sources/prs/sglang/PR-16685.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-16685`
- Generated at: `2026-05-20T15:28:21.908781+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-08T00:48:21Z`
- Merged: `2026-02-03T04:45:14Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: b8zhong, ch-wan
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-28T10:18:13Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/16685#pullrequestreview-3714568313)
- `2026-01-29T19:09:40Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/16685#pullrequestreview-3724511258)
- `2026-02-03T04:45:06Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/16685#pullrequestreview-3742921006)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 2 inline comment(s)
- `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-29T19:09:39Z` `inline` by `b8zhong` `python/sglang/srt/layers/quantization/modelopt_quant.py`:1546; signals: block, flashinfer, fp4, fp8, moe, register; excerpt: "Yeah, I think it would be good. The problem is (to my undersatnding), since we can only register 1 fused function for flashinfer trtllm, ..." (https://github.com/sgl-project/sglang/pull/16685#discussion_r2743104496)
- `2026-01-28T05:12:07Z` `inline` by `ch-wan` `python/sglang/srt/layers/quantization/modelopt_quant.py`:1546; signals: general review; excerpt: "why not using runner?" (https://github.com/sgl-project/sglang/pull/16685#discussion_r2734890688)
