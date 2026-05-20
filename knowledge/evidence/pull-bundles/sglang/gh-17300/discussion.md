# PR Discussion Digest

- Source PR: [sgl-project/sglang#17300](https://github.com/sgl-project/sglang/pull/17300)
- Source page: `sources/prs/sglang/PR-17300.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-17300`
- Generated at: `2026-05-20T15:28:27.009978+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-18T13:44:38Z`
- Merged: `2026-02-05T07:10:26Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: Fridge003, b8zhong, danielafrimi, netanel-haber
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-18T13:46:50Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces padding for FP4 quantized weights and activations to ensure they meet the ... (https://github.com/sgl-project/sglang/pull/17300#pullrequestreview-3675487863)
- `2026-01-21T18:26:27Z` `COMMENTED` by `b8zhong` - Thanks. Btw, what models with weird hidden dim are there issues with? (guess: nemotron? Just curious). Because recently ... (https://github.com/sgl-project/sglang/pull/17300#pullrequestreview-3688769387)
- `2026-01-29T18:39:43Z` `APPROVED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/17300#pullrequestreview-3724398712)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-19T14:11:42Z` `issue` by `Fridge003`; signals: cutlass, flashinfer, fp4, gemm, hang, kernel; excerpt: "@danielafrimi Have you tried other fp4 gemm implementations other than cutlass? We have two other options (flashinfer trtllm and flashinfer cudnn). If any of ..." (https://github.com/sgl-project/sglang/pull/17300#issuecomment-3768533613)
- `2026-02-02T14:05:07Z` `issue` by `danielafrimi`; signals: cutlass, flashinfer, fp4, kernel, nan, nvfp4; excerpt: "@b8zhong @Fridge003 Tried other FP4 kernels (flashinfer trtllm and flashinfer cudnn) in addition to cutlass one. flashinfer cudnn and flashinfer cutlass have the same ..." (https://github.com/sgl-project/sglang/pull/17300#issuecomment-3835337903)
- `2026-01-21T18:25:38Z` `inline` by `b8zhong` `python/sglang/srt/layers/quantization/modelopt_quant.py`:1317; signals: block; excerpt: "QQ: if this comment is accurate, we also need to pad it for the trtllm backend? should we also do it under the block ..." (https://github.com/sgl-project/sglang/pull/17300#discussion_r2713821355)
- `2026-01-21T18:26:27Z` `review` `COMMENTED` by `b8zhong`; signals: general review; excerpt: "Thanks. Btw, what models with weird hidden dim are there issues with? (guess: nemotron? Just curious). Because recently we fixd something related to GLM ..." (https://github.com/sgl-project/sglang/pull/17300#pullrequestreview-3688769387)
