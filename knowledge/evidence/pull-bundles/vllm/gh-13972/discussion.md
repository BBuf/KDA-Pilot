# PR Discussion Digest

- Source PR: [vllm-project/vllm#13972](https://github.com/vllm-project/vllm/pull/13972)
- Source page: `sources/prs/vllm/PR-13972.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-13972`
- Generated at: `2026-05-20T15:34:17.020597+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-27T15:52:58Z`
- Merged: `2025-03-27T00:54:44Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 50 (approved=1, changes_requested=1, commented=48)
- Inline review comments: 86
- Review threads observed: 58
- Resolved/outdated thread markers: resolved=36, outdated=52
- Human participants with discussion text: ElizaWszola, LucasWilkinson, ProExpertProg, dsikka, li2haipeng, mergify, pavanimajety, shixianc, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-03-03T15:01:43Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2654325451)
- `2025-03-03T15:04:00Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2654399523)
- `2025-03-03T15:33:33Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2654489604)
- `2025-03-03T15:36:27Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2654497271)
- `2025-03-03T15:37:37Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2654500377)
- `2025-03-03T15:43:18Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2654515703)
- `2025-03-03T16:11:02Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2654593640)
- `2025-03-03T16:17:19Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2654609841)
- `2025-03-03T16:18:08Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2654611806)
- `2025-03-03T16:27:22Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2654635363)
- `2025-03-03T16:56:22Z` `CHANGES_REQUESTED` by `dsikka` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2654707551)
- `2025-03-03T17:08:45Z` `COMMENTED` by `dsikka` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2654741828)
- `2025-03-04T06:57:41Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2656181512)
- `2025-03-04T07:01:28Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2656191803)
- `2025-03-05T14:19:42Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2661271024)
- `2025-03-05T14:32:45Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2661312069)
- `2025-03-05T14:36:42Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2661323847)
- `2025-03-05T15:10:31Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2661429345)
- `2025-03-05T15:11:15Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2661431515)
- `2025-03-07T06:25:06Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2666365270)
- `2025-03-12T12:10:52Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2678230125)
- `2025-03-12T18:06:01Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2679427056)
- `2025-03-12T19:41:33Z` `COMMENTED` by `ProExpertProg` - Yeah I agree with Rob here, unless we really want to merge for 0.8.0, we should try to ... (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2679651018)
- `2025-03-12T20:44:38Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/13972#pullrequestreview-2679818617)
- ... 25 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 17 inline comment(s)
- `csrc/quantization/cutlass_w8a8/grouped_mm_c3x.cuh`: 10 inline comment(s)
- `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`: 10 inline comment(s)
- `csrc/quantization/cutlass_w8a8/grouped_mm_c3x.cu`: 7 inline comment(s)
- `tests/kernels/test_cutlass.py`: 6 inline comment(s)
- `csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c3x.hpp`: 5 inline comment(s)
- `vllm/model_executor/layers/quantization/kernels/scaled_mm/grouped_cutlass.py`: 4 inline comment(s)
- `csrc/torch_bindings.cpp`: 4 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/kernels/scaled_mm/GroupedMMLinearKernel.py`: 3 inline comment(s)
- `csrc/quantization/cutlass_w8a8/moe/grouped_mm_c3x.cu`: 3 inline comment(s)
- `csrc/quantization/cutlass_w8a8/get_group_starts.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2025-03-03T14:40:17Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:266; signals: compile, cuda, cutlass, fp8, kernel, moe; excerpt: "For this, I think we should export a function like cutlass fp8 supported, especially because this depends on the CUDA version used to compile ..." (https://github.com/vllm-project/vllm/pull/13972#discussion_r1977632713)
- `2025-03-13T14:28:58Z` `inline` by `tlrmchlsmth` `benchmarks/kernels/benchmark_grouped_gemm_cutlass.py`:324; signals: benchmark, cutlass, gemm, kernel, perf, performance; excerpt: "A --tp-sizes argument with the same behavior as in benchmarks/cutlass benchmarks/w8a8 benchmarks.py would be very nice to have, especially to compare and contrast performance ..." (https://github.com/vllm-project/vllm/pull/13972#discussion_r1993655697)
- `2025-03-12T21:30:28Z` `inline` by `pavanimajety` `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`:213; signals: compile, cuda, cutlass, kernel, sm90; excerpt: "get grouped mm data seems to be generic cuda kernels, any reason this has to be compiled only for SM90? These are helpful for ..." (https://github.com/vllm-project/vllm/pull/13972#discussion_r1992322816)
- `2025-03-13T17:25:07Z` `inline` by `tlrmchlsmth` `tests/kernels/test_cutlass.py`:518; signals: cutlass, fp8, gemm, kernel, sm90; excerpt: "I think this actually needs to test for exactly sm90a. Can query check cutlass group gemm supported for this. But need to skip the ..." (https://github.com/vllm-project/vllm/pull/13972#discussion_r1994001724)
- `2025-03-12T18:06:01Z` `inline` by `pavanimajety` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1588; signals: block, cutlass, fp8, moe; excerpt: "A few nits: Could you please add a doc comment regarding the expectation of shapes and datatypes for weights, scales and hidden states? Eg: ..." (https://github.com/vllm-project/vllm/pull/13972#discussion_r1992038748)
- `2025-03-26T18:02:26Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/grouped_mm_c3x.cuh`:15; signals: blackwell, cutlass, h100, kernel; excerpt: "This needs to be: Otherwise it will break on Blackwell, as these H100 CUTLASS kernel are not forward-compatible" (https://github.com/vllm-project/vllm/pull/13972#discussion_r2014750889)
- `2025-03-26T18:30:25Z` `inline` by `tlrmchlsmth` `CMakeLists.txt`:349; signals: block, compile, cuda, kernel; excerpt: "These need to go in their own block that's compiled for CUDA 12.3 or later. For example see what we do for the 2:4 ..." (https://github.com/vllm-project/vllm/pull/13972#discussion_r2014789885)
- `2025-03-26T18:44:59Z` `inline` by `ElizaWszola` `tests/kernels/test_cutlass.py`:523; signals: cutlass, gemm, kernel, moe; excerpt: "We don't need bias in fused moe - I added this TODO when the gemm implementation was less MoE specific, so I think it's ..." (https://github.com/vllm-project/vllm/pull/13972#discussion_r2014809618)
- `2025-03-03T16:17:19Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:148; signals: cutlass, kernel, moe; excerpt: "actually ideally this would be in CutlassGroupMMLinearKernel sorry didn't see that implemented GroupMMLinearKernel before" (https://github.com/vllm-project/vllm/pull/13972#discussion_r1977799681)
- `2025-03-03T16:27:21Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/quantization/kernels/scaled_mm/GroupedMMLinearKernel.py`:18; signals: cutlass, kernel, moe; excerpt: "hmmm should this be FusedMOELayerImpl maybe? the only annoying part is the activation function, might have to add the activation to the "Config". Then ..." (https://github.com/vllm-project/vllm/pull/13972#discussion_r1977815089)
- `2025-03-12T12:10:51Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:444; signals: kernel, moe, triton; excerpt: "Would it make sense to fall back to triton kernel inside this function when one of these conditions is not met? Or should it ..." (https://github.com/vllm-project/vllm/pull/13972#discussion_r1991357796)
- `2025-03-13T17:23:16Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/grouped_mm_c3x.cuh`:17; signals: cuda, cutlass, gemm; excerpt: "We will need a function like bool cutlass group gemm supported(int64 t cuda device capability) that checks the CUDA VERSION to report if cutlass ..." (https://github.com/vllm-project/vllm/pull/13972#discussion_r1993998466)
