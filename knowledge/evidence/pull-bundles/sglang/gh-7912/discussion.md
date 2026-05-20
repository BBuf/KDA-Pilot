# PR Discussion Digest

- Source PR: [sgl-project/sglang#7912](https://github.com/sgl-project/sglang/pull/7912)
- Source page: `sources/prs/sglang/PR-7912.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7912`
- Generated at: `2026-05-20T15:31:21.455420+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-09T23:54:20Z`
- Merged: `2025-09-03T03:56:03Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 6
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: Edwardf0t1
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-09T23:54:56Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @jingyu-ml, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7912#pullrequestreview-3003423567)
- `2025-07-09T23:56:00Z` `COMMENTED` by `gemini-code-assist` - Code Review This PR adds support for Qwen FP8 quantization with ModelOPT. I've identified a critical issue with ... (https://github.com/sgl-project/sglang/pull/7912#pullrequestreview-3003425220)
- `2025-08-20T18:57:49Z` `COMMENTED` by `Edwardf0t1` - @jingyu-ml Please rebase and resolve the conflict and let's test Qwen FP4 as well. -- (https://github.com/sgl-project/sglang/pull/7912#pullrequestreview-3137862236)
- `2025-08-29T22:46:48Z` `COMMENTED` by `Edwardf0t1` (https://github.com/sgl-project/sglang/pull/7912#pullrequestreview-3170574501)
- `2025-09-02T22:37:43Z` `APPROVED` by `Edwardf0t1` - LGTM. Approve to unblock modelopt fp8/fp4 Qwen support in SGLang. cc @zhyncs (https://github.com/sgl-project/sglang/pull/7912#pullrequestreview-3178359528)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 2 inline comment(s)
- `python/sglang/srt/server_args.py`: 1 inline comment(s)
- `python/sglang/srt/configs/model_config.py`: 1 inline comment(s)
- `python/sglang/srt/model_loader/loader.py`: 1 inline comment(s)
- `python/sglang/srt/model_loader/weight_utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-02T22:37:43Z` `review` `APPROVED` by `Edwardf0t1`; signals: block, fp4, fp8; excerpt: "LGTM. Approve to unblock modelopt fp8/fp4 Qwen support in SGLang. cc @zhyncs" (https://github.com/sgl-project/sglang/pull/7912#pullrequestreview-3178359528)
- `2025-08-20T18:57:49Z` `review` `COMMENTED` by `Edwardf0t1`; signals: fp4; excerpt: "@jingyu-ml Please rebase and resolve the conflict and let's test Qwen FP4 as well. --" (https://github.com/sgl-project/sglang/pull/7912#pullrequestreview-3137862236)
- `2025-08-29T22:46:34Z` `inline` by `Edwardf0t1` `python/sglang/srt/layers/quantization/modelopt_quant.py`:521; signals: general review; excerpt: "If parsing group size in config.json failed, could we fallback to parse hf quant config.json instead? Let's thinkg about it for a follow-up PR. ..." (https://github.com/sgl-project/sglang/pull/7912#discussion_r2311534735)
