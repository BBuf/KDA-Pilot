# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1412](https://github.com/flashinfer-ai/flashinfer/pull/1412)
- Source page: `sources/prs/flashinfer/PR-1412.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1412`
- Generated at: `2026-05-20T15:22:35.430260+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-07T23:44:02Z`
- Merged: `2025-08-09T20:40:07Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: aleozlx, azhurkevich, yzh119, zhyncs
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-07T23:44:19Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @aleozlx, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1412#pullrequestreview-3099066239)
- `2025-08-07T23:46:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a caching mechanism for permutation indices to speed up weight processing in ... (https://github.com/flashinfer-ai/flashinfer/pull/1412#pullrequestreview-3099071513)
- `2025-08-07T23:58:48Z` `COMMENTED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/1412#pullrequestreview-3099098451)
- `2025-08-08T00:12:48Z` `COMMENTED` by `azhurkevich` (https://github.com/flashinfer-ai/flashinfer/pull/1412#pullrequestreview-3099111816)
- `2025-08-09T20:40:00Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1412#pullrequestreview-3103246406)

## Inline Comment Hotspots

- `tests/test_trtllm_gen_fused_moe.py`: 3 inline comment(s)
- `flashinfer/fused_moe/core.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-07T23:58:48Z` `inline` by `aleozlx` `tests/test_trtllm_gen_fused_moe.py`:490; signals: cache, moe; excerpt: "i'll just leave it be as a poc here and not to disrupt/complicate regular functional testing. and i disabled it in regular testing. bool ..." (https://github.com/flashinfer-ai/flashinfer/pull/1412#discussion_r2261670568)
- `2025-08-08T00:12:48Z` `inline` by `azhurkevich` `tests/test_trtllm_gen_fused_moe.py`:490; signals: cache, moe; excerpt: "lets nuke default uncached version and only keep cached one" (https://github.com/flashinfer-ai/flashinfer/pull/1412#discussion_r2261681348)
- `2025-08-07T23:45:30Z` `issue` by `aleozlx`; signals: fp4, moe; excerpt: "pytest -x tests/test trtllm gen fused moe.py -k FP4 18 passed, 72 skipped, 180 deselected in 132.28s (0:02:12)" (https://github.com/flashinfer-ai/flashinfer/pull/1412#issuecomment-3166148607)
- `2025-08-07T23:55:15Z` `issue` by `aleozlx`; signals: hang, moe; excerpt: "testing results as of lastest change pytest -x tests/test trtllm gen fused moe.py 60 passed, 210 skipped in 243.93s (0:04:03) ready to merge from ..." (https://github.com/flashinfer-ai/flashinfer/pull/1412#issuecomment-3166167460)
- `2025-08-08T00:30:20Z` `issue` by `aleozlx`; signals: fp4, moe; excerpt: "pytest -x tests/test trtllm gen fused moe.py -k FP4 18 passed, 72 skipped, 180 deselected in 129.88s (0:02:09)" (https://github.com/flashinfer-ai/flashinfer/pull/1412#issuecomment-3166216134)
- `2025-08-08T01:59:56Z` `issue` by `aleozlx`; signals: aligned, cache; excerpt: "after some discussion on if we want to only test cached code path and remove older version. we are aligned on only testing cached ..." (https://github.com/flashinfer-ai/flashinfer/pull/1412#issuecomment-3166331786)
