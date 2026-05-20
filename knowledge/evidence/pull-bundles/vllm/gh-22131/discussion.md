# PR Discussion Digest

- Source PR: [vllm-project/vllm#22131](https://github.com/vllm-project/vllm/pull/22131)
- Source page: `sources/prs/vllm/PR-22131.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-22131`
- Generated at: `2026-05-20T15:36:56.154462+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-02T23:37:48Z`
- Merged: `2025-08-08T02:18:29Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: 0xjunhao, aabbccddwasd, mgoin, voipmonitor
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-08-02T23:40:08Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for block FP8 GEMM kernels on SM120 (Blackwell) GPUs. The changes ... (https://github.com/vllm-project/vllm/pull/22131#pullrequestreview-3081582884)
- `2025-08-03T01:29:22Z` `COMMENTED` by `0xjunhao` (https://github.com/vllm-project/vllm/pull/22131#pullrequestreview-3081601943)
- `2025-08-07T17:33:38Z` `APPROVED` by `mgoin` - LGTM, nice work! (https://github.com/vllm-project/vllm/pull/22131#pullrequestreview-3098149684)

## Inline Comment Hotspots

- `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm120_fp8_dispatch.cuh`: 3 inline comment(s)

## High-Signal Discussion

- `2025-08-04T22:11:04Z` `issue` by `0xjunhao`; signals: block, cutlass, fp8, speedup, triton; excerpt: "Yes, looks like cutlass is much faster right now. FYI, here’s something interesting: 😂 Here are the results on 5090 at the moment: MKN ..." (https://github.com/vllm-project/vllm/pull/22131#issuecomment-3152545741)
- `2025-08-03T01:29:22Z` `inline` by `0xjunhao` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm120_fp8_dispatch.cuh`:41; signals: block, cutlass, fp8, sm120; excerpt: "ColumnMajor is used for B to match the CUTLASS convention." (https://github.com/vllm-project/vllm/pull/22131#discussion_r2249481846)
- `2025-08-04T20:30:29Z` `issue` by `mgoin`; signals: block, fp8, kernel, triton; excerpt: "Have you compared against the triton block fp8 kernel? I'm curious if this is much better for this class of hardware" (https://github.com/vllm-project/vllm/pull/22131#issuecomment-3152319478)
- `2025-08-05T11:45:06Z` `issue` by `0xjunhao`; signals: block, cutlass, fp8, memory; excerpt: "My implementation is based on cutlass. IIUC blockwise fp8 is expected to be slightly slower than the non-block fp8 due to extra requirements such ..." (https://github.com/vllm-project/vllm/pull/22131#issuecomment-3154874345)
- `2025-08-05T04:18:22Z` `issue` by `aabbccddwasd`; signals: block, cutlass, kernel; excerpt: "it's still a bit slower than none-block models. have you utilized cutlass kernel?" (https://github.com/vllm-project/vllm/pull/22131#issuecomment-3153236291)
- `2025-08-07T23:03:32Z` `issue` by `0xjunhao`; signals: hang; excerpt: "The errors are not related to these changes." (https://github.com/vllm-project/vllm/pull/22131#issuecomment-3166087323)
