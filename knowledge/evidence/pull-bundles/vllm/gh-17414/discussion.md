# PR Discussion Digest

- Source PR: [vllm-project/vllm#17414](https://github.com/vllm-project/vllm/pull/17414)
- Source page: `sources/prs/vllm/PR-17414.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-17414`
- Generated at: `2026-05-20T15:35:10.036136+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-29T20:56:46Z`
- Merged: `2025-05-08T19:56:59Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: mgoin, rasmith, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-29T23:18:09Z` `COMMENTED` by `rasmith` (https://github.com/vllm-project/vllm/pull/17414#pullrequestreview-2805298114)
- `2025-04-30T15:51:45Z` `APPROVED` by `rasmith` (https://github.com/vllm-project/vllm/pull/17414#pullrequestreview-2807573599)
- `2025-05-07T03:02:54Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/17414#pullrequestreview-2820197608)
- `2025-05-07T03:03:30Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/17414#pullrequestreview-2820198142)
- `2025-05-08T19:56:51Z` `APPROVED` by `tlrmchlsmth` - Thanks, this has been annoying me too (https://github.com/vllm-project/vllm/pull/17414#pullrequestreview-2826227639)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/kv_cache.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-04-29T23:18:08Z` `inline` by `rasmith` `vllm/model_executor/layers/quantization/kv_cache.py`:130; signals: cache, fp8; excerpt: "Why "uncalibrated"? I only see the warning once when I run it, doesn't seem to be very noisy. Depending on which lands first ( ..." (https://github.com/vllm-project/vllm/pull/17414#discussion_r2067568430)
- `2025-05-07T03:02:54Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/kv_cache.py`:130; signals: cache; excerpt: "I even see this when running INT4 models, this is triggered for most quantization methods" (https://github.com/vllm-project/vllm/pull/17414#discussion_r2076684736)
- `2025-05-07T03:03:30Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/kv_cache.py`:130; signals: cache; excerpt: "The scales are uncalibrated because they are 1.0" (https://github.com/vllm-project/vllm/pull/17414#discussion_r2076685034)
