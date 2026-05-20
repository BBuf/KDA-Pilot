# PR Discussion Digest

- Source PR: [vllm-project/vllm#21837](https://github.com/vllm-project/vllm/pull/21837)
- Source page: `sources/prs/vllm/PR-21837.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21837`
- Generated at: `2026-05-20T15:36:53.577230+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-29T14:25:50Z`
- Merged: `2025-08-01T17:14:38Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: bnellnm, tlrmchlsmth, varun-sundar-rabindranath
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-29T14:28:23Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a performance optimization for MoE layers using DeepEPHighThroughput with block quantization (e.g., ... (https://github.com/vllm-project/vllm/pull/21837#pullrequestreview-3067864877)
- `2025-07-31T14:33:41Z` `APPROVED` by `tlrmchlsmth` - Thanks! (https://github.com/vllm-project/vllm/pull/21837#pullrequestreview-3075701746)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-07-30T20:18:02Z` `issue` by `varun-sundar-rabindranath`; signals: block; excerpt: "So we still go down the "quantize after" codepath if the quantization is per-tensor? Is there some reason that quantization can't happen beforehand in ..." (https://github.com/vllm-project/vllm/pull/21837#issuecomment-3137698186)
- `2025-07-29T15:06:16Z` `issue` by `bnellnm`; signals: general review; excerpt: "So we still go down the "quantize after" codepath if the quantization is per-tensor? Is there some reason that quantization can't happen beforehand in ..." (https://github.com/vllm-project/vllm/pull/21837#issuecomment-3132963424)
- `2025-07-29T15:35:54Z` `issue` by `varun-sundar-rabindranath`; signals: general review; excerpt: "So we still go down the "quantize after" codepath if the quantization is per-tensor? Is there some reason that quantization can't happen beforehand in ..." (https://github.com/vllm-project/vllm/pull/21837#issuecomment-3133064240)
- `2025-07-29T16:22:32Z` `issue` by `bnellnm`; signals: general review; excerpt: "So we still go down the "quantize after" codepath if the quantization is per-tensor? Is there some reason that quantization can't happen beforehand in ..." (https://github.com/vllm-project/vllm/pull/21837#issuecomment-3133223336)
