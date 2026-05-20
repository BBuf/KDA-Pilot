# PR Discussion Digest

- Source PR: [vllm-project/vllm#28934](https://github.com/vllm-project/vllm/pull/28934)
- Source page: `sources/prs/vllm/PR-28934.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28934`
- Generated at: `2026-05-20T15:38:35.364008+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-18T11:19:46Z`
- Merged: `2025-11-25T04:25:20Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: ZJY0516, fhl2000, tdoublep
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-18T11:21:10Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables CUDA graph support for the LinearAttentionBackend. By setting cudagraph support to UNIFORM ... (https://github.com/vllm-project/vllm/pull/28934#pullrequestreview-3477177075)
- `2025-11-19T03:20:49Z` `APPROVED` by `fhl2000` - LGTM, surprised by just needing a few lines of code. It would be good to have some perf ... (https://github.com/vllm-project/vllm/pull/28934#pullrequestreview-3480624263)
- `2025-11-24T16:29:57Z` `APPROVED` by `tdoublep` - I think this looks fine. I checked what needed to be done for Mamba FCG support (e.g., [here]( ... (https://github.com/vllm-project/vllm/pull/28934#pullrequestreview-3501274218)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-11-19T03:20:49Z` `review` `APPROVED` by `fhl2000`; signals: perf; excerpt: "LGTM, surprised by just needing a few lines of code. It would be good to have some perf numbers, and if possible, also cover ..." (https://github.com/vllm-project/vllm/pull/28934#pullrequestreview-3480624263)
- `2025-11-19T03:26:32Z` `issue` by `ZJY0516`; signals: general review; excerpt: "Only minimax-m1 uses this backend. It's too large and I am still downloading it. I only test dummy load for now. @fhl2000" (https://github.com/vllm-project/vllm/pull/28934#issuecomment-3550541007)
- `2025-11-24T16:29:57Z` `review` `APPROVED` by `tdoublep`; signals: general review; excerpt: "I think this looks fine. I checked what needed to be done for Mamba FCG support (e.g., [here]( and it looks like the only ..." (https://github.com/vllm-project/vllm/pull/28934#pullrequestreview-3501274218)
