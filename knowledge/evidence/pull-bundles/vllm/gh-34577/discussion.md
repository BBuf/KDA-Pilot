# PR Discussion Digest

- Source PR: [vllm-project/vllm#34577](https://github.com/vllm-project/vllm/pull/34577)
- Source page: `sources/prs/vllm/PR-34577.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-34577`
- Generated at: `2026-05-20T15:39:51.744548+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-15T11:08:39Z`
- Merged: `2026-03-17T20:48:43Z`

## Discussion Counts

- Issue comments: 18
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 12
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=3, outdated=7
- Human participants with discussion text: eugr, jinzhen-lin, mergify, mgoin, ricky-chaoju
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2026-02-15T11:10:27Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a stability scaling mechanism for NVFP4 Marlin dense and MoE layers to ... (https://github.com/vllm-project/vllm/pull/34577#pullrequestreview-3804368611)
- `2026-02-25T11:23:58Z` `APPROVED` by `jinzhen-lin` - Thank you. The new fix LGTM. Just some more suggestions. (https://github.com/vllm-project/vllm/pull/34577#pullrequestreview-3853603656)
- `2026-02-25T13:51:13Z` `COMMENTED` by `ricky-chaoju` (https://github.com/vllm-project/vllm/pull/34577#pullrequestreview-3854399993)
- `2026-02-25T13:51:26Z` `COMMENTED` by `ricky-chaoju` (https://github.com/vllm-project/vllm/pull/34577#pullrequestreview-3854401406)
- `2026-02-26T17:54:05Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/34577#pullrequestreview-3862612379)
- `2026-02-27T02:00:37Z` `COMMENTED` by `ricky-chaoju` (https://github.com/vllm-project/vllm/pull/34577#pullrequestreview-3864455725)
- `2026-02-27T02:01:33Z` `COMMENTED` by `ricky-chaoju` (https://github.com/vllm-project/vllm/pull/34577#pullrequestreview-3864457570)
- `2026-03-17T18:11:47Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/34577#pullrequestreview-3962799929)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py`: 12 inline comment(s)

## High-Signal Discussion

- `2026-02-17T11:54:27Z` `issue` by `ricky-chaoju`; signals: accuracy, bf16, dtype, fp4, fp8, hang, kernel, nvfp4; excerpt: "Thanks for the review! After investigating more deeply, I found a pre-existing kernel bug that was causing completely garbled output for all BF16 NVFP4 ..." (https://github.com/vllm-project/vllm/pull/34577#issuecomment-3914301710)
- `2026-02-15T17:20:47Z` `issue` by `mgoin`; signals: dtype, fp4, hang, kernel, nvfp4, perf, performance; excerpt: "The obvious issue with this is the impact on performance due to needing to dynamically generate scales for activations and apply them, so a ..." (https://github.com/vllm-project/vllm/pull/34577#issuecomment-3904858562)
- `2026-02-25T11:03:55Z` `issue` by `ricky-chaoju`; signals: accuracy, dtype, fp4, hang, kernel, moe, nvfp4; excerpt: "@jinzhen-lin Thanks for the suggestion! I've implemented the rescaling approach in marlin utils fp4.py: - Added nvfp4 compute scale factor() that computes a power-of-2 ..." (https://github.com/vllm-project/vllm/pull/34577#issuecomment-3958479965)
- `2026-02-24T12:56:00Z` `issue` by `ricky-chaoju`; signals: accuracy, bf16, dtype, fp4, nvfp4; excerpt: "Hi @mgoin, done! I've stripped the PR down to just the BF16 exponent widening fix in dequant.h. FP16 stability scaling has been removed entirely. ..." (https://github.com/vllm-project/vllm/pull/34577#issuecomment-3951595351)
- `2026-02-24T15:28:37Z` `issue` by `ricky-chaoju`; signals: fp4, gemm, kernel, nan, nvfp4; excerpt: "Thanks for the suggestion @jinzhen-lin! I tested the rescaling approach on GLM-4.7-Flash-NVFP4 and found that several layers contain zero-valued weight scales, which causes scale ..." (https://github.com/vllm-project/vllm/pull/34577#issuecomment-3952934916)
- `2026-02-25T13:51:12Z` `inline` by `ricky-chaoju` `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py`:44; signals: dtype, fp4, nvfp4; excerpt: "Good point, done. nvfp4 compute scale factor now returns sf.item() / 1.0 directly, and I removed all .to(device, dtype) at the call sites." (https://github.com/vllm-project/vllm/pull/34577#discussion_r2853169789)
- `2026-02-24T15:01:07Z` `issue` by `jinzhen-lin`; signals: bf16, fp4, perf; excerpt: "Thanks you @ricky-chaoju . Previously, I assumed that after multiplying the E4M3 scales by 2 7, the result would always be greater than 2, ..." (https://github.com/vllm-project/vllm/pull/34577#issuecomment-3952665324)
- `2026-02-24T15:42:24Z` `issue` by `jinzhen-lin`; signals: perf, performance, regression; excerpt: "Could you try filling the zeros in weight scale with other values and then re-run the calculation? Modifying it here could help avoid potential ..." (https://github.com/vllm-project/vllm/pull/34577#issuecomment-3953016980)
- `2026-02-25T11:19:13Z` `inline` by `jinzhen-lin` `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py`:44; signals: dtype, fp4; excerpt: "I suggest returning a Python float (sf.item() and 1.0) directly instead of a Tensor. This avoids the need to manually manage the tensor's device ..." (https://github.com/vllm-project/vllm/pull/34577#discussion_r2852434188)
- `2026-02-25T11:22:59Z` `inline` by `jinzhen-lin` `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py`:38; signals: fp4, nvfp4; excerpt: "Since you're rescaling in nvfp4 marlin process scales, why not do scales (2 7) before computing the scale factor? It makes the min val ..." (https://github.com/vllm-project/vllm/pull/34577#discussion_r2852455409)
- `2026-02-25T13:51:25Z` `inline` by `ricky-chaoju` `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py`:38; signals: fp4, nvfp4; excerpt: "Done! Moved the (2 7) into nvfp4 compute scale factor, so the threshold is now min val < 2 instead of min val < ..." (https://github.com/vllm-project/vllm/pull/34577#discussion_r2853171055)
- `2026-02-27T02:01:33Z` `inline` by `ricky-chaoju` `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py`:449; signals: fp4, nvfp4; excerpt: "The .to(torch.half) was unnecessary since nvfp4 compute scale factor immediately converts to .float() internally. Removed in the latest push." (https://github.com/vllm-project/vllm/pull/34577#discussion_r2862126840)
