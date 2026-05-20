# PR Discussion Digest

- Source PR: [sgl-project/sglang#17449](https://github.com/sgl-project/sglang/pull/17449)
- Source page: `sources/prs/sglang/PR-17449.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-17449`
- Generated at: `2026-05-20T15:28:29.137824+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-21T01:38:02Z`
- Merged: `2026-01-29T13:33:58Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: HydraQYH, fxmarty-amd, ispobock, zianglih
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2026-01-29T13:33:28Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/17449#pullrequestreview-3722751381)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-24T15:21:26Z` `issue` by `HydraQYH`; signals: fp8, gemm, kernel, perf, performance; excerpt: "@zianglih I am very pleased to see the progress of mxfp8. There is still an unmerged for the online quantization kernel of the mxfp8 ..." (https://github.com/sgl-project/sglang/pull/17449#issuecomment-3794805974)
- `2026-01-23T03:36:37Z` `issue` by `zianglih`; signals: fp8, moe; excerpt: "Right now serving already qunatized mxfp8 MoE model does not work due to scaling factor swizzling. I am working on it." (https://github.com/sgl-project/sglang/pull/17449#issuecomment-3788010496)
- `2026-01-26T22:45:35Z` `issue` by `zianglih`; signals: fp8, moe; excerpt: "Implemented a few minor fixes for /update weights from disk. Test for online mxfp8 quantization: Test for Qwen3-4B-Instruct-2507-MXFP8 (dense), with /update weights from disk: ..." (https://github.com/sgl-project/sglang/pull/17449#issuecomment-3802118241)
- `2026-01-24T02:36:41Z` `issue` by `zianglih`; signals: fp8; excerpt: "Serving offline quantized mxfp8 model now works. GSM8K results for serving Qwen/Qwen3-30B-A3B-Instruct-2507 converted from" (https://github.com/sgl-project/sglang/pull/17449#issuecomment-3793561522)
