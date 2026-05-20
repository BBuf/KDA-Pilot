# PR Discussion Digest

- Source PR: [sgl-project/sglang#21321](https://github.com/sgl-project/sglang/pull/21321)
- Source page: `sources/prs/sglang/PR-21321.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21321`
- Generated at: `2026-05-20T15:29:13.651122+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-24T14:56:30Z`
- Merged: `2026-04-29T08:28:22Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 6 (approved=1, changes_requested=1, commented=4)
- Inline review comments: 12
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=9, outdated=9
- Human participants with discussion text: Fridge003, danielafrimi, netanel-haber
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-24T15:04:52Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request extends FlashInfer TRT-LLM MoE kernel support to include relu2 activation in addition to ... (https://github.com/sgl-project/sglang/pull/21321#pullrequestreview-3999995884)
- `2026-03-24T15:13:43Z` `COMMENTED` by `danielafrimi` (https://github.com/sgl-project/sglang/pull/21321#pullrequestreview-4000059106)
- `2026-04-09T06:23:44Z` `CHANGES_REQUESTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/21321#pullrequestreview-4079440055)
- `2026-04-15T10:26:06Z` `COMMENTED` by `danielafrimi` (https://github.com/sgl-project/sglang/pull/21321#pullrequestreview-4112743011)
- `2026-04-17T00:08:21Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/21321#pullrequestreview-4125012510)
- `2026-04-21T23:38:17Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/21321#pullrequestreview-4151316625)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`: 5 inline comment(s)
- `python/sglang/srt/layers/quantization/utils.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 2 inline comment(s)
- `test/registered/kernels/test_trtllm_moe_non_gated.py`: 1 inline comment(s)
- `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-15T10:39:42Z` `issue` by `danielafrimi`; signals: accuracy, alignment, flashinfer, fp4, fp8, kernel, nvfp4; excerpt: "@Fridge003 Added 2 tests 1. Added kernel-level unit tests that verify the non-gated weight alignment padding (FP8/FP4/MXFP8), activation type mapping (relu2 to Relu2 enum), ..." (https://github.com/sgl-project/sglang/pull/21321#issuecomment-4251312517)
- `2026-04-16T23:23:40Z` `inline` by `Fridge003` `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`:254; signals: flashinfer, fp4, moe, nvfp4, register; excerpt: "Looks like the tests in test/registered/4-gpu-models/test nvidia nemotron 3 super nvfp4.py can protect this PR after the moe runner backend is set to trtllm ..." (https://github.com/sgl-project/sglang/pull/21321#discussion_r3096943355)
- `2026-04-16T23:20:17Z` `inline` by `Fridge003` `test/registered/kernels/test_trtllm_moe_non_gated.py`:1; signals: kernel, moe, register; excerpt: "We don't need this test" (https://github.com/sgl-project/sglang/pull/21321#discussion_r3096931941)
- `2026-04-09T06:23:16Z` `inline` by `Fridge003` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:106; signals: flashinfer, moe; excerpt: "Can we create new functions for aligning weights on non-gated models? Adding if-else like this can easily break current logic" (https://github.com/sgl-project/sglang/pull/21321#discussion_r3055839636)
- `2026-03-24T15:13:44Z` `inline` by `danielafrimi` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:648; signals: flashinfer, moe; excerpt: "removed from FI 0.6.6" (https://github.com/sgl-project/sglang/pull/21321#discussion_r2982343520)
- `2026-04-16T23:58:59Z` `inline` by `Fridge003` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:503; signals: flashinfer, moe; excerpt: "We can remove the at the start of this function, since it is imported in other files" (https://github.com/sgl-project/sglang/pull/21321#discussion_r3097081861)
- `2026-04-09T02:54:56Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/utils.py`:584; signals: general review; excerpt: "Why not use round up multiple? They are the same" (https://github.com/sgl-project/sglang/pull/21321#discussion_r3055233792)
- `2026-04-15T10:26:06Z` `inline` by `danielafrimi` `python/sglang/srt/layers/quantization/utils.py`:584; signals: general review; excerpt: "fixed" (https://github.com/sgl-project/sglang/pull/21321#discussion_r3085741645)
- `2026-04-16T23:48:43Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/utils.py`:584; signals: general review; excerpt: "@danielafrimi Please remove the round up to multiple function and restore these lines" (https://github.com/sgl-project/sglang/pull/21321#discussion_r3097040602)
