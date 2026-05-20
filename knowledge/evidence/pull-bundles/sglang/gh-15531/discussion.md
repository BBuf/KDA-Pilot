# PR Discussion Digest

- Source PR: [sgl-project/sglang#15531](https://github.com/sgl-project/sglang/pull/15531)
- Source page: `sources/prs/sglang/PR-15531.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-15531`
- Generated at: `2026-05-20T15:28:12.966570+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-20T13:39:09Z`
- Merged: `2025-12-21T06:50:33Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 5 (commented=5)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: b8zhong, ispobock
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-12-20T13:41:47Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for piecewise CUDA graphs for DeepSeek V3 FP4 models, which is ... (https://github.com/sgl-project/sglang/pull/15531#pullrequestreview-3601113621)
- `2025-12-21T01:27:21Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/15531#pullrequestreview-3601409723)
- `2025-12-21T06:49:06Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/15531#pullrequestreview-3601552923)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py`: 4 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-21T01:27:21Z` `inline` by `b8zhong` `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py`:157; signals: fp4, nvfp4; excerpt: "QQ: we can just delete this wrapper now probably right" (https://github.com/sgl-project/sglang/pull/15531#discussion_r2637480857)
- `2025-12-21T06:49:06Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4.py`:157; signals: fp4, nvfp4; excerpt: "yes, we can check the usage of it" (https://github.com/sgl-project/sglang/pull/15531#discussion_r2637628309)
