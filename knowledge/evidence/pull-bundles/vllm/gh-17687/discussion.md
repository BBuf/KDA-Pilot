# PR Discussion Digest

- Source PR: [vllm-project/vllm#17687](https://github.com/vllm-project/vllm/pull/17687)
- Source page: `sources/prs/vllm/PR-17687.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-17687`
- Generated at: `2026-05-20T15:35:12.613703+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-06T02:06:47Z`
- Merged: `2025-05-11T02:58:49Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 12
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=8, outdated=4
- Human participants with discussion text: jinzhen-lin, mgoin, pavanimajety
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-05-06T10:59:55Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/17687#pullrequestreview-2817743640)
- `2025-05-06T11:11:46Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/17687#pullrequestreview-2817863777)
- `2025-05-06T11:13:12Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/17687#pullrequestreview-2817873748)
- `2025-05-06T12:49:27Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/17687#pullrequestreview-2818146836)
- `2025-05-06T12:51:17Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/17687#pullrequestreview-2818153879)
- `2025-05-07T16:51:20Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/17687#pullrequestreview-2822512584)
- `2025-05-09T17:05:49Z` `APPROVED` by `mgoin` - Excellent work here! I need to run another smoke test since the scales change to fp8, but I ... (https://github.com/vllm-project/vllm/pull/17687#pullrequestreview-2829097676)
- `2025-05-10T17:23:17Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/17687#pullrequestreview-2830999421)

## Inline Comment Hotspots

- `csrc/quantization/gptq_marlin/gptq_marlin.cu`: 3 inline comment(s)
- `tests/kernels/quantization/test_marlin_gemm.py`: 3 inline comment(s)
- `csrc/quantization/gptq_marlin/dequant.h`: 2 inline comment(s)
- `csrc/quantization/gptq_marlin/marlin_template.h`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/marlin_utils.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-05-06T10:31:31Z` `inline` by `mgoin` `csrc/quantization/gptq_marlin/gptq_marlin.cu`:261; signals: block, fp4, nvfp4; excerpt: "Let's specify nvfp4 here since that is the case for group blocks == 1" (https://github.com/vllm-project/vllm/pull/17687#discussion_r2075183416)
- `2025-05-06T10:42:44Z` `inline` by `mgoin` `tests/kernels/quantization/test_marlin_gemm.py`:196; signals: fp4, gemm, kernel; excerpt: "Please put this [16] in marlin utils fp4 so it is clear where it comes from" (https://github.com/vllm-project/vllm/pull/17687#discussion_r2075199669)
- `2025-05-06T10:43:11Z` `inline` by `mgoin` `tests/kernels/quantization/test_marlin_gemm.py`:252; signals: gemm, kernel; excerpt: "Why remove this opcheck?" (https://github.com/vllm-project/vllm/pull/17687#discussion_r2075200363)
- `2025-05-06T12:49:27Z` `inline` by `jinzhen-lin` `tests/kernels/quantization/test_marlin_gemm.py`:252; signals: gemm, kernel; excerpt: "Accidentally removed. Already added back." (https://github.com/vllm-project/vllm/pull/17687#discussion_r2075403989)
- `2025-05-09T17:05:49Z` `review` `APPROVED` by `mgoin`; signals: fp8, hang; excerpt: "Excellent work here! I need to run another smoke test since the scales change to fp8, but I think this is all good to ..." (https://github.com/vllm-project/vllm/pull/17687#pullrequestreview-2829097676)
- `2025-05-08T23:11:45Z` `issue` by `mgoin`; signals: failing, moe; excerpt: "Fused marlin moe test is failing" (https://github.com/vllm-project/vllm/pull/17687#issuecomment-2864657834)
- `2025-05-07T16:51:20Z` `inline` by `pavanimajety` `csrc/quantization/gptq_marlin/dequant.h`:202; signals: fp4; excerpt: "Nice! We can also start using these functions for the fp4 scaled mm tests!" (https://github.com/vllm-project/vllm/pull/17687#discussion_r2078069055)
- `2025-05-06T11:13:12Z` `inline` by `jinzhen-lin` `csrc/quantization/gptq_marlin/marlin_template.h`:712; signals: general review; excerpt: "Some test cases was failed on specail devices (since the out-of-range scales have overwritten sh a). I'm not sure why this issue didn't occur ..." (https://github.com/vllm-project/vllm/pull/17687#discussion_r2075243434)
- `2025-05-06T12:51:17Z` `inline` by `jinzhen-lin` `vllm/model_executor/layers/quantization/utils/marlin_utils.py`:51; signals: general review; excerpt: "- has zp is True: return quant types that has zero points - has zp is False: return quant types that has not zero ..." (https://github.com/vllm-project/vllm/pull/17687#discussion_r2075407392)
- `2025-05-06T10:28:11Z` `inline` by `mgoin` `csrc/quantization/gptq_marlin/dequant.h`; signals: general review; excerpt: "I appreciate the separation of flop and the description at the top, great work!" (https://github.com/vllm-project/vllm/pull/17687#discussion_r2075178453)
- `2025-05-06T10:34:20Z` `inline` by `mgoin` `csrc/quantization/gptq_marlin/gptq_marlin.cu`:471; signals: general review; excerpt: "Update message" (https://github.com/vllm-project/vllm/pull/17687#discussion_r2075187750)
- `2025-05-06T10:34:23Z` `inline` by `mgoin` `csrc/quantization/gptq_marlin/gptq_marlin.cu`:798; signals: general review; excerpt: "Update message" (https://github.com/vllm-project/vllm/pull/17687#discussion_r2075187842)
