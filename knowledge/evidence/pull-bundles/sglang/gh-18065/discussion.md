# PR Discussion Digest

- Source PR: [sgl-project/sglang#18065](https://github.com/sgl-project/sglang/pull/18065)
- Source page: `sources/prs/sglang/PR-18065.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18065`
- Generated at: `2026-05-20T15:28:33.114696+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-01T10:38:37Z`
- Merged: `2026-02-03T12:32:49Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 6 (approved=2, commented=4)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: Fridge003, b8zhong, elvischenv
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-01T10:41:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request fixes a bug in Mistral Large 3 NVFP4 MoE support by refactoring the ... (https://github.com/sgl-project/sglang/pull/18065#pullrequestreview-3735515911)
- `2026-02-01T17:31:07Z` `APPROVED` by `b8zhong` - Thanks. Sorry, we will be more careful in the future. (https://github.com/sgl-project/sglang/pull/18065#pullrequestreview-3736280186)
- `2026-02-01T18:06:38Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/18065#pullrequestreview-3736359309)
- `2026-02-01T20:38:55Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/18065#pullrequestreview-3736617210)
- `2026-02-01T22:19:07Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/18065#pullrequestreview-3736732622)
- `2026-02-03T12:27:27Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/18065#pullrequestreview-3744976566)

## Inline Comment Hotspots

- `test/registered/8-gpu-models/test_mistral_large3.py`: 3 inline comment(s)
- `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-01T18:06:33Z` `inline` by `elvischenv` `test/registered/8-gpu-models/test_mistral_large3.py`:15; signals: fp4, nvfp4, register; excerpt: "Hi @b8zhong, thanks for the review. I just added nvfp4 model to unit test, could you also help trigger it?" (https://github.com/sgl-project/sglang/pull/18065#discussion_r2751734880)
- `2026-02-01T20:38:55Z` `inline` by `b8zhong` `test/registered/8-gpu-models/test_mistral_large3.py`:15; signals: register; excerpt: "@elvischenv Sure, it looks like it has passed. Btw, can you help increase this time out as well? Since this is a relatively large ..." (https://github.com/sgl-project/sglang/pull/18065#discussion_r2751923290)
