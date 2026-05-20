# PR Discussion Digest

- Source PR: [vllm-project/vllm#14447](https://github.com/vllm-project/vllm/pull/14447)
- Source page: `sources/prs/vllm/PR-14447.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14447`
- Generated at: `2026-05-20T15:34:26.077171+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-07T16:34:12Z`
- Merged: `2025-04-15T03:05:22Z`

## Discussion Counts

- Issue comments: 37
- Review submissions: 13 (approved=1, commented=12)
- Inline review comments: 13
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=6, outdated=1
- Human participants with discussion text: LagPixelLOL, LucasWilkinson, davidsyoung, jinzhen-lin, mergify, mgoin, tlrmchlsmth, vivienfanghuagood
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-04-02T15:56:42Z` `COMMENTED` by `tlrmchlsmth` - One fairly large issue with this PR is that it dramatically increases the size of the wheel file. ... (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2736823239)
- `2025-04-05T18:27:38Z` `COMMENTED` by `mgoin` - It seems we could also remove the moe wna16 cuda kernel as there isn't a clear need to ... (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2744959771)
- `2025-04-05T18:47:01Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2744965287)
- `2025-04-05T18:48:23Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2744965469)
- `2025-04-05T18:58:01Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2744966937)
- `2025-04-05T19:09:13Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2744968784)
- `2025-04-08T18:46:50Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2751088202)
- `2025-04-08T19:16:48Z` `COMMENTED` by `LucasWilkinson` - Does this mean we can delete csrc/moe/marlin kernels? (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2751155869)
- `2025-04-08T19:25:54Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2751174221)
- `2025-04-09T06:55:03Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2752285513)
- `2025-04-11T03:17:38Z` `APPROVED` by `mgoin` - LGTM! I still would like to compile locally and validate on a few models/evals. I should have time ... (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2759052561)
- `2025-04-11T17:58:02Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2761122506)
- `2025-04-12T08:37:38Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2762115848)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/fused_marlin_moe.py`: 4 inline comment(s)
- `csrc/moe/marlin_moe_wna16/generate_kernels.py`: 4 inline comment(s)
- `csrc/quantization/gptq_marlin/marlin_dtypes.cuh`: 2 inline comment(s)
- `csrc/moe/marlin_moe_wna16/marlin_template.h`: 2 inline comment(s)
- `csrc/moe/marlin_moe_wna16/kernel.h`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-30T07:29:40Z` `issue` by `jinzhen-lin`; signals: block, hang, kernel, layout, memory, moe, shared memory, speedup; excerpt: "UPDATED: I made a series of minor optimizations to this kernel, mainly including the following: 1. Fused mul(sub(quantized weight, zero points), scale) into fma(quantized ..." (https://github.com/vllm-project/vllm/pull/14447#issuecomment-2764428720)
- `2025-03-11T05:45:38Z` `issue` by `jinzhen-lin`; signals: benchmark, kernel, perf, performance, pipeline, triton; excerpt: "kernel benchmarks (on A800): shapes of DeepSeek-V3-AWQ (with TP=8) have better performance than old marlin kernel (main). 2. The performance of marlin kernel is ..." (https://github.com/vllm-project/vllm/pull/14447#issuecomment-2712722377)
- `2025-04-05T18:27:38Z` `review` `COMMENTED` by `mgoin`; signals: cuda, kernel, moe, triton; excerpt: "It seems we could also remove the moe wna16 cuda kernel as there isn't a clear need to use the moe wna16 triton/cuda kernels ..." (https://github.com/vllm-project/vllm/pull/14447#pullrequestreview-2744959771)
- `2025-04-04T16:40:02Z` `issue` by `jinzhen-lin`; signals: block, kernel, moe, perf, performance; excerpt: "@tlrmchlsmth I optimized the wheel size with through two ways: - Remove old moe marlin kernel - Remove int8 with zero point kernel. Generally, ..." (https://github.com/vllm-project/vllm/pull/14447#issuecomment-2779258243)
- `2025-03-11T05:48:00Z` `issue` by `jinzhen-lin`; signals: accuracy, mla, perf, performance; excerpt: "Performance on DeepSeek-V3-AWQ (on 8 A800), with VLLM MARLIN USE ATOMIC ADD=1 MLA-main MLA-PR no-MLA-main no-MLA-PR -- -- -- -- -- prefill 4735.7 7986.5 ..." (https://github.com/vllm-project/vllm/pull/14447#issuecomment-2712731129)
- `2025-04-02T16:44:50Z` `issue` by `jinzhen-lin`; signals: block, kernel, perf, performance; excerpt: "One fairly large issue with this PR is that it dramatically increases the size of the wheel file. (This is a problem due to ..." (https://github.com/vllm-project/vllm/pull/14447#issuecomment-2773159792)
- `2025-04-05T19:01:59Z` `issue` by `jinzhen-lin`; signals: cuda, kernel, moe, triton; excerpt: "It seems we could also remove the moe wna16 cuda kernel as there isn't a clear need to use the moe wna16 triton/cuda kernels ..." (https://github.com/vllm-project/vllm/pull/14447#issuecomment-2781044745)
- `2025-04-05T18:47:00Z` `inline` by `jinzhen-lin` `csrc/moe/marlin_moe_wna16/generate_kernels.py`:44; signals: block, kernel, moe; excerpt: "1. group blocks=0 is the act order case, this is the setting of gptq marlin dense linear kernel. 2. Yes. group blocks=8 means group ..." (https://github.com/vllm-project/vllm/pull/14447#discussion_r2029944710)
- `2025-04-05T19:09:12Z` `inline` by `jinzhen-lin` `csrc/quantization/gptq_marlin/marlin_dtypes.cuh`:61; signals: bf16, cuda, dtype; excerpt: "In host part (cpu part) compilation, CUDA ARCH is not defined. My code requires the bf16 num conversion functions are available for cpu code ..." (https://github.com/vllm-project/vllm/pull/14447#discussion_r2029948556)
- `2025-04-08T18:45:17Z` `inline` by `tlrmchlsmth` `csrc/moe/marlin_moe_wna16/kernel.h`; signals: compile, kernel, moe; excerpt: "Could we generate these at compile time instead of checking the generated files into the repo? We could do something similar to what we ..." (https://github.com/vllm-project/vllm/pull/14447#discussion_r2033839084)
- `2025-04-08T19:25:54Z` `inline` by `LucasWilkinson` `csrc/moe/marlin_moe_wna16/generate_kernels.py`:1; signals: compile, kernel, moe; excerpt: "Thanks for creating a generator! do you know how bad the compile times are on these files? there seems to be many kernels per ..." (https://github.com/vllm-project/vllm/pull/14447#discussion_r2033891456)
- `2025-04-11T17:49:05Z` `inline` by `tlrmchlsmth` `csrc/moe/marlin_moe_wna16/marlin_template.h`:493; signals: kernel, moe, overflow; excerpt: "Can prob n prob k overflow and int32? If so, could you use int64 t instead? (This looks like it's probably fine, since we'd ..." (https://github.com/vllm-project/vllm/pull/14447#discussion_r2040024240)
