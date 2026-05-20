# PR Discussion Digest

- Source PR: [vllm-project/vllm#19757](https://github.com/vllm-project/vllm/pull/19757)
- Source page: `sources/prs/vllm/PR-19757.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-19757`
- Generated at: `2026-05-20T15:35:33.388090+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-17T16:59:49Z`
- Merged: `2025-07-04T18:58:04Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 19 (approved=1, commented=18)
- Inline review comments: 23
- Review threads observed: 16
- Resolved/outdated thread markers: resolved=5, outdated=13
- Human participants with discussion text: ElizaWszola, bnellnm, djmmoss, mergify, mgoin, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-17T17:00:21Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @djmmoss, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2936441101)
- `2025-06-17T17:03:29Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new CUTLASS block-scaled grouped GEMM kernel specifically for SM100 (Blackwell) architectures, ... (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2936449695)
- `2025-06-17T17:05:43Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2936455446)
- `2025-06-17T17:09:19Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2936464288)
- `2025-06-17T21:06:48Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2937094886)
- `2025-06-18T01:39:15Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2937477416)
- `2025-06-18T06:51:24Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2937945012)
- `2025-06-18T11:58:58Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2938918392)
- `2025-06-24T22:12:19Z` `COMMENTED` by `tlrmchlsmth` - Are there any benchmarks for these kernels that you could report @djmmoss? (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2955518332)
- `2025-06-25T04:11:07Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2956413092)
- `2025-06-25T04:12:47Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2956420624)
- `2025-06-25T04:13:51Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2956424759)
- `2025-06-30T21:02:57Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2972706407)
- `2025-07-01T16:30:43Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2976163257)
- `2025-07-01T21:14:54Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2976973176)
- `2025-07-01T22:14:28Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2977093162)
- `2025-07-02T19:21:30Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2980370654)
- `2025-07-02T20:24:55Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2980532882)
- `2025-07-03T19:24:57Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2984433016)

## Inline Comment Hotspots

- `CMakeLists.txt`: 6 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 5 inline comment(s)
- `tests/kernels/moe/test_cutlass_grouped_gemm.py`: 4 inline comment(s)
- `csrc/quantization/cutlass_w8a8/moe/blockwise_scaled_group_mm_sm100.cu`: 4 inline comment(s)
- `vllm/envs.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/cutlass_moe.py`: 1 inline comment(s)
- `csrc/torch_bindings.cpp`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-25T03:48:37Z` `issue` by `djmmoss`; signals: b200, deepgemm, gemm, hang, latency, moe, perf, performance; excerpt: "@tlrmchlsmth I had a look over I could likely integrate the SM100 changes fairly simply if the CompressedTensorsMoEMethod's is prefer to the DeepGEMM style ..." (https://github.com/vllm-project/vllm/pull/19757#issuecomment-3002894459)
- `2025-06-17T17:05:43Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1190; signals: cutlass, gemm, kernel, moe, perf, performance, triton; excerpt: "The N 512 check for deep gemm was only for performance reasons. Does the triton kernel actually beat cutlass for N <= 512?" (https://github.com/vllm-project/vllm/pull/19757#discussion_r2152764166)
- `2025-06-24T22:08:11Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/moe/blockwise_scaled_group_mm_sm100.cu`:36; signals: block, cutlass, fp8, gemm, moe, sm100; excerpt: "Does this do the same thing as get group gemm starts blockscale fp8 in 19983? Checking to see what we can consolidate between the ..." (https://github.com/vllm-project/vllm/pull/19757#discussion_r2165015900)
- `2025-06-17T17:09:19Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:540; signals: cutlass, gemm, hang, moe, triton; excerpt: "Can you also integrate this with triton deep gemm moe.py (maybe we should change this name) so it can be used with EP?" (https://github.com/vllm-project/vllm/pull/19757#discussion_r2152769843)
- `2025-06-24T22:09:50Z` `inline` by `tlrmchlsmth` `csrc/quantization/cutlass_w8a8/moe/blockwise_scaled_group_mm_sm100.cu`:173; signals: block, cutlass, moe, sm100, sm90; excerpt: "Could we make ArchTag a template parameter? And then reuse this class for both SM90 and SM100?" (https://github.com/vllm-project/vllm/pull/19757#discussion_r2165017802)
- `2025-06-25T04:12:47Z` `inline` by `djmmoss` `tests/kernels/moe/test_cutlass_grouped_gemm.py`:121; signals: cutlass, gemm, kernel, moe; excerpt: "done, although given the sizes of the test there are some outliers compared to the FP32 baseline, this is why the atol is fairly ..." (https://github.com/vllm-project/vllm/pull/19757#discussion_r2165668131)
- `2025-06-17T21:06:48Z` `inline` by `bnellnm` `tests/kernels/moe/test_cutlass_grouped_gemm.py`:121; signals: cutlass, gemm, kernel, moe; excerpt: "Can you use torch.testing.assert close here?" (https://github.com/vllm-project/vllm/pull/19757#discussion_r2153170922)
- `2025-06-18T11:58:58Z` `inline` by `ElizaWszola` `tests/kernels/moe/test_cutlass_grouped_gemm.py`; signals: cutlass, gemm, kernel, moe; excerpt: "Can you also add a test for the full fused MoE operation?" (https://github.com/vllm-project/vllm/pull/19757#discussion_r2154417270)
- `2025-06-25T04:13:51Z` `inline` by `djmmoss` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1190; signals: cutlass, moe, perf; excerpt: "removed, at the moment cutlass is performing better" (https://github.com/vllm-project/vllm/pull/19757#discussion_r2165670718)
- `2025-06-24T22:12:19Z` `review` `COMMENTED` by `tlrmchlsmth`; signals: benchmark, kernel; excerpt: "Are there any benchmarks for these kernels that you could report @djmmoss?" (https://github.com/vllm-project/vllm/pull/19757#pullrequestreview-2955518332)
- `2025-06-18T06:51:24Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1201; signals: cutlass, moe; excerpt: "Would it make sense for the usage of CUTLASS to be decided on the quantized method level? For example, the same way CUTLASS MoE ..." (https://github.com/vllm-project/vllm/pull/19757#discussion_r2153786718)
- `2025-06-26T14:46:10Z` `issue` by `mgoin`; signals: moe, sm100; excerpt: "FYI I include moe data for sm100 here" (https://github.com/vllm-project/vllm/pull/19757#issuecomment-3008757151)
