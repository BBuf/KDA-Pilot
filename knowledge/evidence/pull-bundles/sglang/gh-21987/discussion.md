# PR Discussion Digest

- Source PR: [sgl-project/sglang#21987](https://github.com/sgl-project/sglang/pull/21987)
- Source page: `sources/prs/sglang/PR-21987.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21987`
- Generated at: `2026-05-20T15:29:20.200476+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-03T02:31:45Z`
- Merged: `2026-04-03T08:45:13Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 6 (approved=2, commented=4)
- Inline review comments: 4
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: Fridge003, Qiaolin-Yu, kpham-sgl
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-03T03:54:26Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/21987#pullrequestreview-4054145142)
- `2026-04-03T04:53:28Z` `COMMENTED` by `kpham-sgl` (https://github.com/sgl-project/sglang/pull/21987#pullrequestreview-4054266472)
- `2026-04-03T05:13:14Z` `COMMENTED` by `kpham-sgl` (https://github.com/sgl-project/sglang/pull/21987#pullrequestreview-4054302854)
- `2026-04-03T05:15:55Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/21987#pullrequestreview-4054307768)
- `2026-04-03T05:16:31Z` `APPROVED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/21987#pullrequestreview-4054308789)
- `2026-04-03T07:00:33Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/21987#pullrequestreview-4054560204)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/trtllm_mla_backend.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-04-03T04:53:28Z` `inline` by `kpham-sgl` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:550; signals: attention, block, mla; excerpt: "AFAIU this codeblock (capture) applies to both spec v1 and v2, so it is safe to modify replay accordingly" (https://github.com/sgl-project/sglang/pull/21987#discussion_r3031433408)
- `2026-04-03T05:13:14Z` `inline` by `kpham-sgl` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:550; signals: attention, mla; excerpt: "Inforward extend under if ( forward batch.forward mode.is target verify() or forward batch.forward mode.is draft extend(include v2=True)): q is also padded" (https://github.com/sgl-project/sglang/pull/21987#discussion_r3031471685)
- `2026-04-03T03:54:26Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:550; signals: attention, mla; excerpt: "I think it makes sense for spec v2. But is this correct for spec v1?" (https://github.com/sgl-project/sglang/pull/21987#discussion_r3031315167)
- `2026-04-03T05:15:55Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:550; signals: attention, mla; excerpt: "Oh, you're right. I just remembered the padding." (https://github.com/sgl-project/sglang/pull/21987#discussion_r3031476588)
