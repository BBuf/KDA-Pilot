# PR Discussion Digest

- Source PR: [vllm-project/vllm#29691](https://github.com/vllm-project/vllm/pull/29691)
- Source page: `sources/prs/vllm/PR-29691.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29691`
- Generated at: `2026-05-20T15:38:47.426288+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-28T17:03:19Z`
- Merged: `2025-12-09T03:29:06Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 11 (approved=2, changes_requested=1, commented=8)
- Inline review comments: 18
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=9, outdated=6
- Human participants with discussion text: LucasWilkinson, czhu-cohere, dsikka, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-28T17:17:22Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for W4A8 Grouped GEMM on Hopper GPUs, which is a significant ... (https://github.com/vllm-project/vllm/pull/29691#pullrequestreview-3519587574)
- `2025-11-28T17:17:59Z` `COMMENTED` by `czhu-cohere` (https://github.com/vllm-project/vllm/pull/29691#pullrequestreview-3519588664)
- `2025-11-28T17:18:32Z` `COMMENTED` by `czhu-cohere` (https://github.com/vllm-project/vllm/pull/29691#pullrequestreview-3519589459)
- `2025-12-02T17:44:31Z` `COMMENTED` by `dsikka` - The CT integration looks clean to me! Do we have a test model we can add? (https://github.com/vllm-project/vllm/pull/29691#pullrequestreview-3531401155)
- `2025-12-03T21:36:04Z` `APPROVED` by `LucasWilkinson` - LGTM! Thanks; amazing work! (https://github.com/vllm-project/vllm/pull/29691#pullrequestreview-3537009219)
- `2025-12-04T07:11:10Z` `COMMENTED` by `czhu-cohere` (https://github.com/vllm-project/vllm/pull/29691#pullrequestreview-3538477408)
- `2025-12-05T01:43:06Z` `CHANGES_REQUESTED` by `mgoin` - Nice work! I have a fundamental concern about the weight format as I find the need for two ... (https://github.com/vllm-project/vllm/pull/29691#pullrequestreview-3542735791)
- `2025-12-05T01:59:29Z` `COMMENTED` by `czhu-cohere` (https://github.com/vllm-project/vllm/pull/29691#pullrequestreview-3542831409)
- `2025-12-05T02:03:17Z` `COMMENTED` by `czhu-cohere` (https://github.com/vllm-project/vllm/pull/29691#pullrequestreview-3542837435)
- `2025-12-05T02:08:05Z` `COMMENTED` by `czhu-cohere` (https://github.com/vllm-project/vllm/pull/29691#pullrequestreview-3542843538)
- `2025-12-09T03:27:57Z` `APPROVED` by `mgoin` - Very nice work! Thanks for iterating (https://github.com/vllm-project/vllm/pull/29691#pullrequestreview-3555187429)

## Inline Comment Hotspots

- `csrc/quantization/cutlass_w4a8/w4a8_grouped_mm_entry.cu`: 9 inline comment(s)
- `vllm/model_executor/layers/fused_moe/cutlass_moe.py`: 5 inline comment(s)
- `csrc/quantization/cutlass_w4a8/get_group_starts.cuh`: 2 inline comment(s)
- `csrc/torch_bindings.cpp`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/config.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-05T02:29:07Z` `issue` by `czhu-cohere`; signals: bf16, epilogue, fp4, fp8, gemm, nvfp4; excerpt: "@mgoin thanks for the detailed review and feedback! We already have this for NVFP4 Let me look closer at what's being done for nvfp4 ..." (https://github.com/vllm-project/vllm/pull/29691#issuecomment-3615060242)
- `2025-12-05T01:59:29Z` `inline` by `czhu-cohere` `csrc/quantization/cutlass_w4a8/w4a8_grouped_mm_entry.cu`:39; signals: cutlass, fp8, tile, wgmma; excerpt: "@LucasWilkinson if I'm reading this correctly it looks like the k-extent is always 32 for fp8 wgmma. The [implementation]( checks which means the tileshape ..." (https://github.com/vllm-project/vllm/pull/29691#discussion_r2591163029)
- `2025-11-28T17:17:59Z` `inline` by `czhu-cohere` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:1111; signals: cutlass, gemm, kernel, moe; excerpt: "the underlying grouped gemm kernel does not support fp16, that could be added in the future" (https://github.com/vllm-project/vllm/pull/29691#discussion_r2572191991)
- `2025-11-28T17:18:32Z` `inline` by `czhu-cohere` `csrc/quantization/cutlass_w4a8/get_group_starts.cuh`:83; signals: cutlass, gemm, kernel; excerpt: "the get group kernel supports fp16 but the grouped gemm kernel itself does not, we can remove this check when the underlying grouped gemm ..." (https://github.com/vllm-project/vllm/pull/29691#discussion_r2572192784)
- `2025-12-03T21:32:30Z` `inline` by `LucasWilkinson` `csrc/quantization/cutlass_w4a8/w4a8_grouped_mm_entry.cu`:39; signals: cutlass, fp4, mxfp4; excerpt: "any chance this could be extended to mxfp4 too? would be nice if we could make this compatible with gpt-oss (could be done in ..." (https://github.com/vllm-project/vllm/pull/29691#discussion_r2586678912)
- `2025-12-04T07:11:10Z` `inline` by `czhu-cohere` `csrc/quantization/cutlass_w4a8/w4a8_grouped_mm_entry.cu`:39; signals: cutlass, fp4, mxfp4; excerpt: "mxfp4 is an e8m0 scaling factor for every 32 elements? I think there is a group size limitation of 128 here though because the ..." (https://github.com/vllm-project/vllm/pull/29691#discussion_r2587842897)
- `2025-12-05T01:43:06Z` `review` `CHANGES_REQUESTED` by `mgoin`; signals: fp4, nvfp4; excerpt: "Nice work! I have a fundamental concern about the weight format as I find the need for two sets of scales for the weights ..." (https://github.com/vllm-project/vllm/pull/29691#pullrequestreview-3542735791)
- `2025-12-05T02:08:05Z` `inline` by `czhu-cohere` `csrc/quantization/cutlass_w4a8/w4a8_grouped_mm_entry.cu`:252; signals: cutlass, fp8; excerpt: "good point, I see the [fp8 path]( currently does this too I guess we need to somehow call get workspace size and pass the ..." (https://github.com/vllm-project/vllm/pull/29691#discussion_r2591174724)
- `2025-12-05T01:31:05Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:1113; signals: cutlass, moe; excerpt: "Can you add group size to the msg?" (https://github.com/vllm-project/vllm/pull/29691#discussion_r2591110406)
- `2025-12-05T01:31:36Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:1116; signals: cutlass, moe; excerpt: "Print the sizes please. Users might see this if they do too aggressive TP" (https://github.com/vllm-project/vllm/pull/29691#discussion_r2591111166)
- `2025-12-05T01:31:49Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:1119; signals: cutlass, moe; excerpt: "Use a normal comment" (https://github.com/vllm-project/vllm/pull/29691#discussion_r2591111431)
- `2025-12-05T01:29:17Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/config.py`:156; signals: moe; excerpt: "I don't understand why we need groupwise and channelwise scales for the weights. This point is rather confusing for me. Can we get good ..." (https://github.com/vllm-project/vllm/pull/29691#discussion_r2591107965)
