# PR Discussion Digest

- Source PR: [sgl-project/sglang#16014](https://github.com/sgl-project/sglang/pull/16014)
- Source page: `sources/prs/sglang/PR-16014.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-16014`
- Generated at: `2026-05-20T15:28:18.584171+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-28T12:53:27Z`
- Merged: `2026-01-08T15:52:22Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: Fridge003, copilot-pull-request-reviewer, mmangkad
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-28T12:55:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a performance optimization for MXFP4 Triton kernels on Hopper (sm90) GPUs by ... (https://github.com/sgl-project/sglang/pull/16014#pullrequestreview-3614672542)
- `2025-12-28T12:58:19Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview This PR applies a performance optimization for MXFP4 Triton kernels on Hopper (sm90) GPUs by ... (https://github.com/sgl-project/sglang/pull/16014#pullrequestreview-3614673664)
- `2026-01-05T08:14:45Z` `APPROVED` by `Fridge003` - Nice catch (https://github.com/sgl-project/sglang/pull/16014#pullrequestreview-3625861076)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/mxfp4.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-28T12:58:19Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: bf16, fp4, hang, hopper, kernel, mxfp4, perf, performance; excerpt: "Pull request overview This PR applies a performance optimization for MXFP4 Triton kernels on Hopper (sm90) GPUs by forcing split k=1 to ensure bf16 ..." (https://github.com/sgl-project/sglang/pull/16014#pullrequestreview-3614673664)
- `2026-01-05T04:49:22Z` `issue` by `mmangkad`; signals: accuracy, hang, perf, performance, regression, throughput; excerpt: "Do you have accuracy data, and performance data before and after this change? bs=8 Before: After: bs=256 Before: After: Accuracies after bs = 8 ..." (https://github.com/sgl-project/sglang/pull/16014#issuecomment-3708932198)
- `2026-01-08T15:48:21Z` `issue` by `Fridge003`; signals: failing, fp4, kernel, mxfp4; excerpt: "What's the problem with this? The failing tests are unrelated to mxfp4 kernel. I think it's OK to merge" (https://github.com/sgl-project/sglang/pull/16014#issuecomment-3724480247)
- `2026-01-05T02:03:22Z` `issue` by `Fridge003`; signals: accuracy, hang, perf, performance; excerpt: "Do you have accuracy data, and performance data before and after this change?" (https://github.com/sgl-project/sglang/pull/16014#issuecomment-3708694149)
