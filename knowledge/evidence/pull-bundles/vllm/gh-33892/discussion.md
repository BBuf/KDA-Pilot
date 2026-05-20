# PR Discussion Digest

- Source PR: [vllm-project/vllm#33892](https://github.com/vllm-project/vllm/pull/33892)
- Source page: `sources/prs/vllm/PR-33892.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-33892`
- Generated at: `2026-05-20T15:39:43.035457+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-05T09:32:23Z`
- Merged: `2026-04-09T00:50:39Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 37 (approved=2, commented=35)
- Inline review comments: 43
- Review threads observed: 21
- Resolved/outdated thread markers: resolved=9, outdated=11
- Human participants with discussion text: LucasWilkinson, maralbahari, mergify, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-05T09:35:42Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a significant and well-designed refactoring of the FP8 block-scaled linear kernel integration. ... (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3755629900)
- `2026-02-05T09:59:41Z` `COMMENTED` by `maralbahari` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3755774461)
- `2026-02-25T10:08:20Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853192127)
- `2026-02-25T10:08:58Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853196016)
- `2026-02-25T10:09:05Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853196599)
- `2026-02-25T10:09:12Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853197221)
- `2026-02-25T10:09:23Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853198180)
- `2026-02-25T10:09:34Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853199262)
- `2026-02-25T10:09:58Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853201720)
- `2026-02-25T10:10:09Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853202878)
- `2026-02-25T10:10:24Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853204590)
- `2026-02-25T10:10:30Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853205286)
- `2026-02-25T10:11:33Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853211765)
- `2026-02-25T10:15:37Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853234339)
- `2026-02-25T10:23:02Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853276216)
- `2026-02-25T10:30:41Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3853324813)
- `2026-02-26T05:38:28Z` `COMMENTED` by `maralbahari` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3858570205)
- `2026-02-26T05:38:58Z` `COMMENTED` by `maralbahari` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3858571512)
- `2026-02-26T05:39:41Z` `COMMENTED` by `maralbahari` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3858573208)
- `2026-02-26T05:46:16Z` `COMMENTED` by `maralbahari` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3858580407)
- `2026-02-26T15:28:58Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3861747289)
- `2026-02-27T03:16:18Z` `COMMENTED` by `maralbahari` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3864623598)
- `2026-03-02T02:12:49Z` `COMMENTED` by `maralbahari` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3873776404)
- `2026-03-04T11:43:22Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/33892#pullrequestreview-3888915938)
- ... 13 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/kernels/linear/scaled_mm/cuda.py`: 18 inline comment(s)
- `vllm/model_executor/kernels/linear/scaled_mm/deep_gemm.py`: 8 inline comment(s)
- `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`: 5 inline comment(s)
- `vllm/model_executor/kernels/linear/scaled_mm/flashinfer.py`: 4 inline comment(s)
- `vllm/model_executor/kernels/linear/scaled_mm/BlockScaledMMLinearKernel.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/modelopt.py`: 2 inline comment(s)
- `tests/compile/passes/test_fusion.py`: 2 inline comment(s)
- `tests/utils.py`: 1 inline comment(s)
- `tests/conftest.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-20T03:21:02Z` `inline` by `maralbahari` `vllm/model_executor/kernels/linear/scaled_mm/cuda.py`:95; signals: block, cuda, cutlass, deepgemm, dtype, flashinfer, fp8, gemm; excerpt: "flashinfer-deepgemm and deepgemm are relying on weight shape and output dtype and input dtype (in should use deepgemm for fp8 linear and should use ..." (https://github.com/vllm-project/vllm/pull/33892#discussion_r2963751806)
- `2026-03-20T05:10:22Z` `inline` by `maralbahari` `vllm/model_executor/kernels/linear/scaled_mm/cuda.py`:95; signals: block, cuda, cutlass, deepgemm, dtype, flashinfer, fp8, gemm; excerpt: "@LucasWilkinson so can we remove the assertion of input dtype==torch.bfloat16 check in should use flashinfer for blockscale fp8 gemm or keep it? so there ..." (https://github.com/vllm-project/vllm/pull/33892#discussion_r2963996999)
- `2026-02-25T10:08:58Z` `inline` by `tjtanaa` `vllm/model_executor/kernels/linear/scaled_mm/cuda.py`:102; signals: block, cuda, deepgemm, flashinfer, fp8, gemm, kernel; excerpt: "This is set to true because FlashInferFp8DeepGEMMDynamicBlockScaledKernel is flashinfer fp8 blockscale gemm supported() is evaluated in the init () So, this condition self.flashinfer deepgemm ..." (https://github.com/vllm-project/vllm/pull/33892#discussion_r2852068563)
- `2026-03-02T02:12:49Z` `inline` by `maralbahari` `vllm/model_executor/kernels/linear/scaled_mm/cuda.py`:102; signals: block, cuda, dtype, flashinfer, fp8, gemm, kernel; excerpt: "to use this should use flashinfer for blockscale fp8 gemm function we need access to weight shape, input dtype and output dtype. since weight ..." (https://github.com/vllm-project/vllm/pull/33892#discussion_r2870211519)
- `2026-03-20T02:54:57Z` `inline` by `maralbahari` `vllm/model_executor/kernels/linear/scaled_mm/cuda.py`:63; signals: cuda, cutlass, deepgemm, flashinfer, gemm, kernel, triton; excerpt: "on cuda the priority order is as follow: 1. flashinfer-deepgemm 2. deepgemm 3. cutlass 4. triton so the fallback kernels can be either cutlass ..." (https://github.com/vllm-project/vllm/pull/33892#discussion_r2963705050)
- `2026-02-27T03:15:58Z` `inline` by `maralbahari` `tests/compile/passes/test_fusion.py`:84; signals: block, compile, cuda, fp8, kernel, triton; excerpt: "@tjtanaa added (TritonFp8BlockScaledMMKernel, GroupShape(1, 64)) for rocm similar to cuda." (https://github.com/vllm-project/vllm/pull/33892#discussion_r2862285542)
- `2026-02-25T10:09:04Z` `inline` by `tjtanaa` `vllm/model_executor/kernels/linear/scaled_mm/cuda.py`:102; signals: cuda, deepgemm, flashinfer, gemm, kernel; excerpt: "Benefit of doing this self.flashinfer deepgemm kernel is not None first is that it short-circuits the conditions." (https://github.com/vllm-project/vllm/pull/33892#discussion_r2852069093)
- `2026-02-25T10:09:23Z` `inline` by `tjtanaa` `vllm/model_executor/kernels/linear/scaled_mm/cuda.py`:104; signals: cuda, deepgemm, fp8, gemm, kernel; excerpt: "The reason that the last argument of should use deepgemm for fp8 linear can be set to True is the same as in" (https://github.com/vllm-project/vllm/pull/33892#discussion_r2852070797)
- `2026-02-25T10:09:34Z` `inline` by `tjtanaa` `vllm/model_executor/kernels/linear/scaled_mm/cuda.py`:109; signals: cuda, deepgemm, fp8, gemm, kernel; excerpt: "The reason that the last argument of should use deepgemm for fp8 linear can be set to True is the same as in" (https://github.com/vllm-project/vllm/pull/33892#discussion_r2852071883)
- `2026-02-25T10:10:30Z` `inline` by `tjtanaa` `vllm/model_executor/kernels/linear/scaled_mm/deep_gemm.py`:47; signals: deepgemm, flashinfer, gemm, kernel, register; excerpt: "FlashInfer and DeepGEMM are not following current abstraction. They are wrapping the quant ops in a direct register custom op as shown in and" (https://github.com/vllm-project/vllm/pull/33892#discussion_r2852077109)
- `2026-02-26T05:45:59Z` `inline` by `maralbahari` `vllm/model_executor/kernels/linear/scaled_mm/BlockScaledMMLinearKernel.py`:53; signals: block, fp8, gemm, kernel, triton; excerpt: "@tjtanaa for the base Fp8BlockScaledMMLinear added use ue8m0=False and for each provider (eg. triton, deep gemm, etc) would override and instantiate quant fp8 as ..." (https://github.com/vllm-project/vllm/pull/33892#discussion_r2857047429)
- `2026-03-19T14:43:36Z` `inline` by `LucasWilkinson` `vllm/model_executor/kernels/linear/scaled_mm/cuda.py`:63; signals: block, cuda, fp8, kernel, triton; excerpt: "is this the only place that uses ordered fallback kernels? if so feels like it always resolves to TritonFp8BlockScaledMMKernel?" (https://github.com/vllm-project/vllm/pull/33892#discussion_r2960555363)
