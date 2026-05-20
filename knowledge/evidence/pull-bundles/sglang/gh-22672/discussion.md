# PR Discussion Digest

- Source PR: [sgl-project/sglang#22672](https://github.com/sgl-project/sglang/pull/22672)
- Source page: `sources/prs/sglang/PR-22672.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22672`
- Generated at: `2026-05-20T15:29:28.889572+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-13T07:34:16Z`
- Merged: `2026-04-14T07:00:59Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 1 (commented=1)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: BBuf, mickqian
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-13T07:39:37Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request expands ModelOpt quantization support for diffusion models, introducing FP8 and NVFP4 compatibility for ... (https://github.com/sgl-project/sglang/pull/22672#pullrequestreview-4097090203)

## Inline Comment Hotspots

- `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`: 1 inline comment(s)
- `python/sglang/multimodal_gen/tools/build_modelopt_nvfp4_transformer.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-13T10:35:58Z` `issue` by `BBuf`; signals: b200, blackwell, cutlass, failing, flashinfer, fp4, gemm, kernel; excerpt: "I dug into the default sglang JIT/CUTLASS NVFP4 failure we saw on B200 without the FlashInfer override. The failure is not in initialize() or ..." (https://github.com/sgl-project/sglang/pull/22672#issuecomment-4235723873)
- `2026-04-14T01:12:16Z` `issue` by `BBuf`; signals: bf16, fp4, nvfp4; excerpt: "wan2.2 - bf16 - nvfp4" (https://github.com/sgl-project/sglang/pull/22672#issuecomment-4240609451)
- `2026-04-14T07:00:07Z` `issue` by `mickqian`; signals: b200; excerpt: "bypassing diffusion b200 ci since runner down" (https://github.com/sgl-project/sglang/pull/22672#issuecomment-4241861130)
