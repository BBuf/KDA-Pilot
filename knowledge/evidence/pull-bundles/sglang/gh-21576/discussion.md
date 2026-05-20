# PR Discussion Digest

- Source PR: [sgl-project/sglang#21576](https://github.com/sgl-project/sglang/pull/21576)
- Source page: `sources/prs/sglang/PR-21576.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21576`
- Generated at: `2026-05-20T15:29:15.271146+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-28T01:45:00Z`
- Merged: `2026-04-01T19:55:06Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: b8zhong, zianglih
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-29T20:16:59Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/21576#pullrequestreview-4027212115)
- `2026-04-01T15:25:41Z` `APPROVED` by `b8zhong` - Q: Can we set it to flashinfer cutlass or flashinfer trtllm by default for SM100? (Unless it has ... (https://github.com/sgl-project/sglang/pull/21576#pullrequestreview-4045042627)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8_utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-01T19:28:13Z` `issue` by `zianglih`; signals: cutlass, flashinfer, gemm, perf, performance, sm100, triton; excerpt: "Q: Can we set it to flashinfer cutlass or flashinfer trtllm by default for SM100? (Unless it has numerical problems, or anything). In my ..." (https://github.com/sgl-project/sglang/pull/21576#issuecomment-4172475392)
- `2026-04-01T15:25:41Z` `review` `APPROVED` by `b8zhong`; signals: cutlass, flashinfer, gemm, perf, sm100, triton; excerpt: "Q: Can we set it to flashinfer cutlass or flashinfer trtllm by default for SM100? (Unless it has numerical problems, or anything). In my ..." (https://github.com/sgl-project/sglang/pull/21576#pullrequestreview-4045042627)
- `2026-03-29T20:16:59Z` `inline` by `zianglih` `python/sglang/srt/layers/quantization/fp8_utils.py`:984; signals: fp8, perf; excerpt: "Check if this has runtime perf overhead later." (https://github.com/sgl-project/sglang/pull/21576#discussion_r3006718006)
