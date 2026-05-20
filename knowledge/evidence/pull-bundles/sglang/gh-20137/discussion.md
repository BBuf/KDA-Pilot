# PR Discussion Digest

- Source PR: [sgl-project/sglang#20137](https://github.com/sgl-project/sglang/pull/20137)
- Source page: `sources/prs/sglang/PR-20137.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-20137`
- Generated at: `2026-05-20T15:29:00.812022+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-08T18:32:34Z`
- Merged: `2026-03-25T00:28:26Z`

## Discussion Counts

- Issue comments: 20
- Review submissions: 1 (commented=1)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: RubiaCx, mickqian, ping1jing2, yhyang201, ykcai-daniel
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-08T18:36:04Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for NVFP4 quantization for Flux.2 models. The changes are extensive and ... (https://github.com/sgl-project/sglang/pull/20137#pullrequestreview-3911872332)

## Inline Comment Hotspots

- `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py`: 2 inline comment(s)
- `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-19T08:53:17Z` `issue` by `RubiaCx`; signals: bf16, block, fp4, nvfp4; excerpt: "Now this PR adds end-to-end support for --model-path black-forest-labs/FLUX.2-dev-NVFP4 in SGLang's diffusion backend. We tracked down and fixed four independent bugs: 1. modelopt quant.py: ..." (https://github.com/sgl-project/sglang/pull/20137#issuecomment-4088682240)
- `2026-03-19T16:08:48Z` `issue` by `RubiaCx`; signals: flashinfer, fp4; excerpt: "BTW, the core issue with our flashinfer integration was that the checkpoint's FP4 weights use lo hi nibble packing (cuBLAS format), but flashinfer expects ..." (https://github.com/sgl-project/sglang/pull/20137#issuecomment-4091326979)
