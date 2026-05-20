# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#4867](https://github.com/NVIDIA/TensorRT-LLM/pull/4867)
- Source page: `sources/prs/tensorrt-llm/PR-4867.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-4867`
- Generated at: `2026-05-20T15:19:11.432469+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-03T11:28:32Z`
- Merged: `2025-06-16T03:30:58Z`

## Discussion Counts

- Issue comments: 47
- Review submissions: 19 (approved=3, commented=16)
- Inline review comments: 20
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=8
- Human participants with discussion text: Tracin, djns99, hlu1, juney-nvidia, suyoggupta, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-06-03T12:34:57Z` `COMMENTED` by `juney-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2892146904)
- `2025-06-03T12:35:32Z` `COMMENTED` by `juney-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2892148691)
- `2025-06-03T12:36:32Z` `COMMENTED` by `juney-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2892152241)
- `2025-06-03T21:23:38Z` `APPROVED` by `hlu1` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2894153238)
- `2025-06-03T21:24:38Z` `COMMENTED` by `hlu1` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2894159164)
- `2025-06-05T21:37:18Z` `COMMENTED` by `djns99` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2902491244)
- `2025-06-05T21:54:15Z` `COMMENTED` by `hlu1` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2902566484)
- `2025-06-06T02:50:43Z` `APPROVED` by `djns99` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2903634607)
- `2025-06-06T04:19:56Z` `COMMENTED` by `Tracin` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2903727650)
- `2025-06-06T21:24:30Z` `COMMENTED` by `hlu1` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2906175376)
- `2025-06-06T21:45:23Z` `COMMENTED` by `hlu1` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2906177783)
- `2025-06-09T02:33:24Z` `COMMENTED` by `Tracin` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2908789432)
- `2025-06-09T03:21:00Z` `COMMENTED` by `Tracin` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2908830649)
- `2025-06-09T03:25:55Z` `COMMENTED` by `Tracin` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2908837594)
- `2025-06-09T21:35:33Z` `COMMENTED` by `hlu1` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2911426371)
- `2025-06-10T05:00:13Z` `COMMENTED` by `hlu1` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2911963196)
- `2025-06-16T03:30:39Z` `COMMENTED` by `juney-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2930543083)
- `2025-06-16T03:30:56Z` `APPROVED` by `juney-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#pullrequestreview-2930543430)

## Inline Comment Hotspots

- `cpp/include/tensorrt_llm/common/quantization.h`: 8 inline comment(s)
- `tensorrt_llm/_torch/modules/linear.py`: 6 inline comment(s)
- `cpp/tensorrt_llm/cutlass_extensions/include/cutlass_extensions/epilogue/fusion/sm90_visitor_allreduce_tma_warpspecialized.hpp`: 2 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/quant.py`: 2 inline comment(s)
- `tests/unittest/_torch/thop/test_fp4_bmm_quantize.py`: 1 inline comment(s)
- `tests/unittest/_torch/thop/test_w4a8_mxfp4_mxfp8_gemm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-09T03:25:55Z` `inline` by `Tracin` `cpp/tensorrt_llm/cutlass_extensions/include/cutlass_extensions/epilogue/fusion/sm90_visitor_allreduce_tma_warpspecialized.hpp`:38; signals: compile, cutlass, epilogue, sm90, tensorrt, tma, warp; excerpt: "It was in the project and I think it then was [deleted]( by mistake. We will have compilation error when compile internalcutlass without this ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#discussion_r2134973465)
- `2025-06-06T21:26:01Z` `inline` by `hlu1` `cpp/tensorrt_llm/cutlass_extensions/include/cutlass_extensions/epilogue/fusion/sm90_visitor_allreduce_tma_warpspecialized.hpp`:38; signals: cutlass, epilogue, sm90, tensorrt, tma, warp; excerpt: "Why is this file in this PR?" (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#discussion_r2132926671)
- `2025-06-03T12:36:31Z` `inline` by `juney-nvidia` `cpp/include/tensorrt_llm/common/quantization.h`:122; signals: fp4, fp8, mxfp4, oom, tensorrt; excerpt: "For MXFP4, is it only used with per-tensor FP8 or in the future it can also be combined with MXFP8? Do we need to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#discussion_r2123682290)
- `2025-06-09T02:33:24Z` `inline` by `Tracin` `tensorrt_llm/_torch/modules/linear.py`:666; signals: attention, fp8, kernel, tensorrt; excerpt: "If previous operation (attention kernel) fuses FP8 quantization then a tuple (fp8 input, input scale) will be passed to linear forward." (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#discussion_r2134940379)
- `2025-06-16T03:30:39Z` `inline` by `juney-nvidia` `tensorrt_llm/_torch/auto_deploy/custom_ops/quant.py`:200; signals: fp4, gemm, nvfp4, tensorrt; excerpt: "@suyoggupta @lucaslie for vis. Based on the discussion with @Tracin , the removed "False" value is for the sf use ue8m0: boo argument and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#discussion_r2148983651)
- `2025-06-03T21:22:25Z` `inline` by `hlu1` `cpp/include/tensorrt_llm/common/quantization.h`:122; signals: fp4, fp8, mxfp4, tensorrt; excerpt: "w4a8Mxfp4Mxfp8 can be added if it's needed." (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#discussion_r2124950825)
- `2025-06-06T21:39:59Z` `inline` by `hlu1` `tests/unittest/_torch/thop/test_w4a8_mxfp4_mxfp8_gemm.py`:56; signals: fp4, fp8, gemm, mxfp4; excerpt: "Remove all the contiguous() calls. They don't do anything here." (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#discussion_r2132938989)
- `2025-06-03T21:24:38Z` `inline` by `hlu1` `cpp/include/tensorrt_llm/common/quantization.h`:382; signals: compile, tensorrt; excerpt: "We should remove the default values in fromDescription so the compiler will report an error if the wrong number if arguments are passed." (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#discussion_r2124955329)
- `2025-06-06T21:33:51Z` `inline` by `hlu1` `tensorrt_llm/_torch/modules/linear.py`:670; signals: memory, tensorrt; excerpt: "Create this with shape [max seq len, cols] in module and take a slice at run time. Unfortunately we may want to make it ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#discussion_r2132933545)
- `2025-06-03T12:35:32Z` `inline` by `juney-nvidia` `cpp/include/tensorrt_llm/common/quantization.h`:382; signals: tensorrt; excerpt: "Nit: I am a little bit scared of seeing so many member variable since it can easily bring trivial error." (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#discussion_r2123680488)
- `2025-06-05T21:37:17Z` `inline` by `djns99` `cpp/include/tensorrt_llm/common/quantization.h`:382; signals: tensorrt; excerpt: "Agree, I think we should just have a struct that defaults everything to false and we can set just the values we want" (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#discussion_r2130499142)
- `2025-06-06T04:19:56Z` `inline` by `Tracin` `cpp/include/tensorrt_llm/common/quantization.h`:214; signals: tensorrt; excerpt: "Remove default values in C++ but remain in Python. I think named parameters are useful. Not sure if this works for py-binding." (https://github.com/NVIDIA/TensorRT-LLM/pull/4867#discussion_r2131469244)
