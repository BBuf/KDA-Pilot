# PR Discussion Digest

- Source PR: [sgl-project/sglang#11737](https://github.com/sgl-project/sglang/pull/11737)
- Source page: `sources/prs/sglang/PR-11737.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-11737`
- Generated at: `2026-05-20T15:27:27.062188+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-17T00:14:35Z`
- Merged: `2025-10-29T19:25:17Z`

## Discussion Counts

- Issue comments: 17
- Review submissions: 20 (approved=2, commented=18)
- Inline review comments: 22
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: AichenF, Fridge003, HydraQYH, jiahe7ay, johnnynunez, voipmonitor, weireweire
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-10-17T00:16:42Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for FP4 kernels on SM120 (GeForce RTX 50 series) GPUs. The ... (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3347520843)
- `2025-10-20T02:31:14Z` `COMMENTED` by `HydraQYH` - Great job. By the way, can you provide the results of the benchmark and unit tests? Ref: 1. ... (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3354855556)
- `2025-10-20T06:21:31Z` `COMMENTED` by `AichenF` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3355131157)
- `2025-10-20T06:54:07Z` `COMMENTED` by `AichenF` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3355193236)
- `2025-10-20T07:00:42Z` `COMMENTED` by `AichenF` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3355208695)
- `2025-10-20T12:03:30Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3356219377)
- `2025-10-20T12:08:30Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3356231997)
- `2025-10-21T13:25:12Z` `COMMENTED` by `AichenF` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3360734150)
- `2025-10-21T14:51:01Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3361232071)
- `2025-10-22T03:22:48Z` `COMMENTED` by `AichenF` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3363562630)
- `2025-10-22T09:45:33Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3364765263)
- `2025-10-22T09:48:05Z` `COMMENTED` by `HydraQYH` - There's only one issue left, and I think I can approve this PR once it's resolved. (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3364774798)
- `2025-10-22T15:22:49Z` `COMMENTED` by `AichenF` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3366337315)
- `2025-10-23T06:28:44Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3368410257)
- `2025-10-23T07:26:13Z` `COMMENTED` by `AichenF` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3368582381)
- `2025-10-23T07:29:24Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3368595160)
- `2025-10-23T07:30:01Z` `APPROVED` by `HydraQYH` - LGTM (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3368597479)
- `2025-10-24T06:31:45Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3374732333)
- `2025-10-24T12:41:17Z` `COMMENTED` by `AichenF` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3376401560)
- `2025-10-29T19:24:58Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3395717877)

## Inline Comment Hotspots

- `sgl-kernel/csrc/gemm/nvfp4_scaled_mm_kernels.cu`: 11 inline comment(s)
- `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`: 7 inline comment(s)
- `sgl-kernel/CMakeLists.txt`: 2 inline comment(s)
- `sgl-kernel/csrc/gemm/nvfp4_quant_entry.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-22T09:45:32Z` `inline` by `HydraQYH` `sgl-kernel/csrc/gemm/nvfp4_scaled_mm_kernels.cu`:430; signals: cuda, fp4, gemm, hang, kernel, moe, nvfp4; excerpt: "Got it! For general GEMMs, dynamically acquiring the workspace is not incompatible with CUDA Graph. However, for Grouped GEMMs used in MoE scenarios, dynamically ..." (https://github.com/sgl-project/sglang/pull/11737#discussion_r2451277931)
- `2025-10-23T06:28:43Z` `inline` by `HydraQYH` `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`:365; signals: block, cuda, fp4, hang, kernel, moe, nvfp4; excerpt: "Thank you so much. Could you please help me modify this script slightly? Each time you replay the CUDA graph, static topk weights and ..." (https://github.com/sgl-project/sglang/pull/11737#discussion_r2454054643)
- `2025-10-22T09:46:50Z` `inline` by `HydraQYH` `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`:365; signals: block, cuda, fp4, gemm, kernel, moe, nvfp4; excerpt: "Could you please test the compatibility of nvfp4 Grouped GEMM with CUDA Graph?" (https://github.com/sgl-project/sglang/pull/11737#discussion_r2451285801)
- `2025-10-24T12:41:16Z` `inline` by `AichenF` `sgl-kernel/csrc/gemm/nvfp4_quant_entry.cu`:19; signals: cutlass, fp4, gemm, kernel, nvfp4, sm100, sm120; excerpt: "Should be sm100a sm120? quite reasonable, cutlass uses sm100a and sm120a" (https://github.com/sgl-project/sglang/pull/11737#discussion_r2460254791)
- `2025-10-24T12:27:20Z` `issue` by `AichenF`; signals: b200, fp4, gemm, kernel, nvfp4, sm100, sm120; excerpt: "Will the modification on nvfp4 kernels break the function of nvfp4 on sm100? Can you post the result of test fp4 gemm.py on both ..." (https://github.com/sgl-project/sglang/pull/11737#issuecomment-3442873094)
- `2025-10-20T02:31:14Z` `review` `COMMENTED` by `HydraQYH`; signals: benchmark, fp4, gemm, kernel, nvfp4; excerpt: "Great job. By the way, can you provide the results of the benchmark and unit tests? Ref: 1. sgl-kernel/benchmark/bench fp4 gemm.py 2. sgl-kernel/benchmark/bench nvfp4 ..." (https://github.com/sgl-project/sglang/pull/11737#pullrequestreview-3354855556)
- `2025-10-20T06:21:31Z` `inline` by `AichenF` `sgl-kernel/csrc/gemm/nvfp4_scaled_mm_kernels.cu`:122; signals: fp4, gemm, kernel, nvfp4, sm120, tma; excerpt: "Cluster shape has to be 1x1x1, for sm120 do not support multicast feature of TMA load, see:" (https://github.com/sgl-project/sglang/pull/11737#discussion_r2443906191)
- `2025-10-22T15:22:49Z` `inline` by `AichenF` `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`:365; signals: block, cuda, fp4, kernel, moe, nvfp4; excerpt: "of course, here is the test results and test script. [test fp4 moe cuda graph.py](" (https://github.com/sgl-project/sglang/pull/11737#discussion_r2452480132)
- `2025-10-23T07:26:13Z` `inline` by `AichenF` `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`:365; signals: block, cuda, fp4, kernel, moe, nvfp4; excerpt: "i modified the script as you recommended, here is the new results: [test fp4 moe cuda graph v2.py](" (https://github.com/sgl-project/sglang/pull/11737#discussion_r2454180386)
- `2025-10-23T07:29:24Z` `inline` by `HydraQYH` `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`:365; signals: block, cuda, fp4, kernel, moe, nvfp4; excerpt: "It looks like this implementation is CUDA Graph compatible." (https://github.com/sgl-project/sglang/pull/11737#discussion_r2454188260)
- `2025-10-24T06:30:34Z` `inline` by `Fridge003` `sgl-kernel/csrc/gemm/nvfp4_quant_entry.cu`:19; signals: fp4, gemm, kernel, nvfp4, sm100, sm120; excerpt: "Should be sm100a sm120?" (https://github.com/sgl-project/sglang/pull/11737#discussion_r2459033864)
- `2025-10-24T06:33:41Z` `issue` by `Fridge003`; signals: fp4, gemm, kernel, nvfp4, sm100, sm120; excerpt: "Will the modification on nvfp4 kernels break the function of nvfp4 on sm100? Can you post the result of test fp4 gemm.py on both ..." (https://github.com/sgl-project/sglang/pull/11737#issuecomment-3441310656)
