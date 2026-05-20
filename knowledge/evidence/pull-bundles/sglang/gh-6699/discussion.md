# PR Discussion Digest

- Source PR: [sgl-project/sglang#6699](https://github.com/sgl-project/sglang/pull/6699)
- Source page: `sources/prs/sglang/PR-6699.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6699`
- Generated at: `2026-05-20T15:30:46.483784+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-28T09:17:36Z`
- Merged: `2025-06-02T03:49:01Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 30 (approved=3, changes_requested=3, commented=24)
- Inline review comments: 34
- Review threads observed: 21
- Resolved/outdated thread markers: resolved=20, outdated=19
- Human participants with discussion text: Alcanderian, BBuf, guoyuhong, yuan-luo, zhyncs
- Automation comments/reviews omitted from high-signal summary: 13
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-05-28T09:18:03Z` `COMMENTED` by `gemini-code-assist` - Hello @yuan-luo, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post my feedback shortly. ... (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2874254626)
- `2025-05-28T09:19:25Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This pull request introduces a CUDA kernel for MoE (Mixture of Experts) pre-reordering, aiming to replace ... (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2874259430)
- `2025-05-28T10:46:18Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This pull request introduces a new CUDA kernel for MoE (Mixture of Experts) pre-reordering, along with ... (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2874524267)
- `2025-05-28T13:08:13Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This pull request introduces a new CUDA kernel for moe pre reorder, aiming to replace the ... (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2874984838)
- `2025-05-29T03:39:23Z` `COMMENTED` by `guoyuhong` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2876955417)
- `2025-05-29T15:37:55Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2878729488)
- `2025-05-29T15:41:14Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2878741313)
- `2025-05-29T16:01:07Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2878811764)
- `2025-05-29T16:04:31Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2878823416)
- `2025-05-30T14:39:36Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2881571838)
- `2025-05-30T14:44:23Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2881584884)
- `2025-05-30T14:44:45Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2881585842)
- `2025-05-30T14:56:44Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2881617361)
- `2025-05-30T15:07:02Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2881644017)
- `2025-05-30T15:07:17Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2881644603)
- `2025-05-31T10:29:37Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2883868416)
- `2025-05-31T10:29:49Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2883868714)
- `2025-05-31T11:32:53Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2883961398)
- `2025-05-31T11:33:04Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2883961567)
- `2025-05-31T13:06:23Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2884067541)
- `2025-05-31T13:45:41Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2884117730)
- `2025-05-31T15:07:45Z` `APPROVED` by `BBuf` - LGTM! (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2884208154)
- `2025-05-31T15:34:44Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2884217954)
- `2025-06-01T02:35:33Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6699#pullrequestreview-2884964745)
- ... 6 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `sgl-kernel/csrc/moe/ep_moe_reorder_kernel.cu`: 10 inline comment(s)
- `sgl-kernel/csrc/moe/moe_reorder_kernel.cu`: 9 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 8 inline comment(s)
- `sgl-kernel/csrc/common_extension.cc`: 3 inline comment(s)
- `sgl-kernel/python/sgl_kernel/moe.py`: 2 inline comment(s)
- `sgl-kernel/CMakeLists.txt`: 2 inline comment(s)

## High-Signal Discussion

- `2025-05-29T06:39:45Z` `issue` by `yuan-luo`; signals: benchmark, cuda, kernel, moe, perf, performance, triton; excerpt: "I wrote a benchmark for the cuda kernel. The result shows it gains 5x times performance improvement comparing to the triton kernel. bench cuda ..." (https://github.com/sgl-project/sglang/pull/6699#issuecomment-2918466002)
- `2025-05-30T16:17:08Z` `issue` by `yuan-luo`; signals: benchmark, cuda, kernel, perf, performance, triton; excerpt: "Finally, the kernel benchmark script also needs to be updated to utilize the Triton Benchmark tool to compare performance differences in various scenarios, and ..." (https://github.com/sgl-project/sglang/pull/6699#issuecomment-2922816186)
- `2025-05-31T13:45:41Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/ep_moe_reorder_kernel.cu`:10; signals: coalesc, kernel, moe, perf, performance; excerpt: "The coalesce kernel's performance is not idealisic:" (https://github.com/sgl-project/sglang/pull/6699#discussion_r2117868216)
- `2025-05-30T14:47:21Z` `issue` by `BBuf`; signals: benchmark, kernel, perf, performance, triton; excerpt: "Finally, the kernel benchmark script also needs to be updated to utilize the Triton Benchmark tool to compare performance differences in various scenarios, and ..." (https://github.com/sgl-project/sglang/pull/6699#issuecomment-2922601574)
- `2025-05-30T15:09:41Z` `issue` by `yuan-luo`; signals: benchmark, kernel, perf, performance, triton; excerpt: "Finally, the kernel benchmark script also needs to be updated to utilize the Triton Benchmark tool to compare performance differences in various scenarios, and ..." (https://github.com/sgl-project/sglang/pull/6699#issuecomment-2922657878)
- `2025-05-31T15:33:08Z` `inline` by `Alcanderian` `sgl-kernel/csrc/moe/ep_moe_reorder_kernel.cu`:38; signals: kernel, memory, moe, vector; excerpt: "Could you please modify this core loop with vectorization ld/st to increase the memory bandwidth? It is quite useful XD. Thanks! refer to: 1. ..." (https://github.com/sgl-project/sglang/pull/6699#discussion_r2117964863)
- `2025-06-01T10:29:00Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/ep_moe_reorder_kernel.cu`:38; signals: kernel, moe, perf, performance; excerpt: "New kernel gains better performance." (https://github.com/sgl-project/sglang/pull/6699#discussion_r2119001171)
- `2025-05-30T14:44:45Z` `inline` by `BBuf` `sgl-kernel/csrc/moe/moe_reorder_kernel.cu`:44; signals: hang, kernel, moe; excerpt: "For the input Tensor, the function signature does not need to add the suffix ptr. This is also consistent with the code style in ..." (https://github.com/sgl-project/sglang/pull/6699#discussion_r2116065163)
- `2025-06-01T10:54:35Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/ep_moe_reorder_kernel.cu`:38; signals: kernel, moe, triton; excerpt: "Since @ch-wan added use per token if dynamic in pre reorder Triton kernel I need to update code accordingly. Please wait for the internal ..." (https://github.com/sgl-project/sglang/pull/6699#discussion_r2119018475)
- `2025-06-01T11:20:17Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/ep_moe_reorder_kernel.cu`:38; signals: cuda, kernel, moe; excerpt: "@Alcanderian @ch-wan Address all the comments and updated cuda kernel based on latest signature. Please help to review." (https://github.com/sgl-project/sglang/pull/6699#discussion_r2119042582)
- `2025-05-30T14:56:44Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/moe_reorder_kernel.cu`:44; signals: hang, kernel, moe; excerpt: "Sure. Changed." (https://github.com/sgl-project/sglang/pull/6699#discussion_r2116086080)
- `2025-05-31T13:06:23Z` `inline` by `BBuf` `sgl-kernel/csrc/moe/ep_moe_reorder_kernel.cu`:10; signals: coalesc, kernel, moe; excerpt: "Maybe you can try a coalesced version, such as :" (https://github.com/sgl-project/sglang/pull/6699#discussion_r2117821645)
