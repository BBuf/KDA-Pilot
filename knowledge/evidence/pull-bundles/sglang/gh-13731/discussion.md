# PR Discussion Digest

- Source PR: [sgl-project/sglang#13731](https://github.com/sgl-project/sglang/pull/13731)
- Source page: `sources/prs/sglang/PR-13731.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13731`
- Generated at: `2026-05-20T15:27:49.575055+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-21T12:08:44Z`
- Merged: `2025-12-04T02:09:09Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 8 (commented=8)
- Inline review comments: 15
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=11, outdated=9
- Human participants with discussion text: BBuf, HydraQYH, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 11
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-21T12:12:55Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for CUTLASS-based MXFP8 Grouped GEMM on the Blackwell architecture, along with ... (https://github.com/sgl-project/sglang/pull/13731#pullrequestreview-3492498606)
- `2025-11-21T15:43:15Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/13731#pullrequestreview-3493322636)
- `2025-11-22T14:36:02Z` `COMMENTED` by `BBuf` - Great job! We can also conside improve many memory bound kernel's HBM bandwidth with 256 bit LDG/STS in ... (https://github.com/sgl-project/sglang/pull/13731#pullrequestreview-3496779445)
- `2025-11-23T09:19:51Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/13731#pullrequestreview-3497522346)
- `2025-11-23T09:31:19Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/13731#pullrequestreview-3497554159)
- `2025-11-24T14:25:34Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/13731#pullrequestreview-3500688959)
- `2025-11-24T15:00:21Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/13731#pullrequestreview-3500854379)
- `2025-11-24T15:12:29Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/13731#pullrequestreview-3500905900)

## Inline Comment Hotspots

- `sgl-kernel/csrc/expert_specialization/es_sm100_mxfp8_blockscaled_group_quant.cuh`: 7 inline comment(s)
- `sgl-kernel/tests/test_es_mxfp8_blockscaled_moe.py`: 2 inline comment(s)
- `sgl-kernel/csrc/expert_specialization/es_sm100_mxfp8_blockscaled_functor.cuh`: 2 inline comment(s)
- `sgl-kernel/csrc/expert_specialization/es_sm100_mxfp8_blockscaled_launcher.cuh`: 2 inline comment(s)
- `sgl-kernel/csrc/expert_specialization/es_sm100_mxfp8_blockscaled.cu`: 1 inline comment(s)
- `sgl-kernel/csrc/expert_specialization/es_sm100_mxfp8_blockscaled_group_quant.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-24T14:25:34Z` `inline` by `HydraQYH` `sgl-kernel/csrc/expert_specialization/es_sm100_mxfp8_blockscaled_group_quant.cuh`:276; signals: block, coalesc, fp8, kernel, latency, layout, memory, perf; excerpt: "For each 128 128 tile, its scale factor is a 512-byte chunk located in Global Memory. Within this 512-byte chunk, the Scale Factors is ..." (https://github.com/sgl-project/sglang/pull/13731#discussion_r2556510277)
- `2025-11-24T14:00:16Z` `issue` by `HydraQYH`; signals: attention, fp8, gemm, kernel, memory, sm100, sm90, tma; excerpt: "Awesome workpiece! The design spirit is quite similar with DeepSeek DSA Indexer, using a pre-compute kernel to avoid massive computing. Whereas Indexer is to ..." (https://github.com/sgl-project/sglang/pull/13731#issuecomment-3570928253)
- `2025-11-24T14:12:57Z` `issue` by `HydraQYH`; signals: block, cute, fp8, kernel, perf, sm100; excerpt: "For sm100, SGLang has sm100 fp8 blockwise group mm dispatch shape to do dispatch based on shape. The dispatch principle seems to be similar ..." (https://github.com/sgl-project/sglang/pull/13731#issuecomment-3570985939)
- `2025-11-24T15:14:18Z` `issue` by `yuan-luo`; signals: block, cute, fp8, kernel, perf, sm100; excerpt: "For sm100, SGLang has sm100 fp8 blockwise group mm dispatch shape to do dispatch based on shape. The dispatch principle seems to be similar ..." (https://github.com/sgl-project/sglang/pull/13731#issuecomment-3571284380)
- `2025-11-22T15:01:22Z` `issue` by `yuan-luo`; signals: attention, fp8, gemm, kernel, sm100; excerpt: "Awesome workpiece! The design spirit is quite similar with DeepSeek DSA Indexer, using a pre-compute kernel to avoid massive computing. Whereas Indexer is to ..." (https://github.com/sgl-project/sglang/pull/13731#issuecomment-3566781260)
- `2025-11-23T09:04:28Z` `issue` by `yuan-luo`; signals: block, cute, fp8, kernel, sm100; excerpt: "For sm100, SGLang has sm100 fp8 blockwise group mm dispatch shape to do dispatch based on shape. The dispatch principle seems to be similar ..." (https://github.com/sgl-project/sglang/pull/13731#issuecomment-3567650069)
- `2025-11-21T15:43:15Z` `inline` by `HydraQYH` `sgl-kernel/csrc/expert_specialization/es_sm100_mxfp8_blockscaled_group_quant.cuh`:278; signals: block, fp8, kernel, sm100; excerpt: "Transform Groupwise Schedule into a more efficient Schedule will release in next PR." (https://github.com/sgl-project/sglang/pull/13731#discussion_r2550186931)
- `2025-11-22T14:36:02Z` `review` `COMMENTED` by `BBuf`; signals: b200, kernel, memory; excerpt: "Great job! We can also conside improve many memory bound kernel's HBM bandwidth with 256 bit LDG/STS in b200." (https://github.com/sgl-project/sglang/pull/13731#pullrequestreview-3496779445)
- `2025-11-23T09:19:51Z` `inline` by `yuan-luo` `sgl-kernel/csrc/expert_specialization/es_sm100_mxfp8_blockscaled_group_quant.cuh`:37; signals: block, fp8, kernel, sm100; excerpt: "I think here we'd better add the reference from NV trt-llm." (https://github.com/sgl-project/sglang/pull/13731#discussion_r2553903089)
- `2025-11-23T09:31:19Z` `inline` by `yuan-luo` `sgl-kernel/csrc/expert_specialization/es_sm100_mxfp8_blockscaled_group_quant.cuh`:276; signals: block, fp8, kernel, sm100; excerpt: "Since we already have a sf, why do we need a scale factor shared here?" (https://github.com/sgl-project/sglang/pull/13731#discussion_r2553926373)
- `2025-11-24T15:00:21Z` `inline` by `HydraQYH` `sgl-kernel/csrc/expert_specialization/es_sm100_mxfp8_blockscaled_group_quant.cuh`:37; signals: block, fp8, kernel, sm100; excerpt: "Done." (https://github.com/sgl-project/sglang/pull/13731#discussion_r2556640184)
- `2025-11-24T15:12:29Z` `inline` by `yuan-luo` `sgl-kernel/csrc/expert_specialization/es_sm100_mxfp8_blockscaled_group_quant.cuh`:276; signals: block, fp8, kernel, sm100; excerpt: "Got it. Thanks." (https://github.com/sgl-project/sglang/pull/13731#discussion_r2556681581)
