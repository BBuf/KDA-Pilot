# PR Discussion Digest

- Source PR: [sgl-project/sglang#6837](https://github.com/sgl-project/sglang/pull/6837)
- Source page: `sources/prs/sglang/PR-6837.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6837`
- Generated at: `2026-05-20T15:30:51.937242+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-03T09:46:29Z`
- Merged: `2025-06-05T07:33:47Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 13 (approved=2, changes_requested=1, commented=10)
- Inline review comments: 16
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=10, outdated=7
- Human participants with discussion text: Alcanderian, BBuf, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-03T09:46:50Z` `COMMENTED` by `gemini-code-assist` - Hello @yuan-luo, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post my feedback shortly. ... (https://github.com/sgl-project/sglang/pull/6837#pullrequestreview-2891569232)
- `2025-06-03T09:49:00Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This pull request introduces a CUDA kernel implementation for moe ep post reorder, aiming to improve ... (https://github.com/sgl-project/sglang/pull/6837#pullrequestreview-2891579365)
- `2025-06-04T03:03:15Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6837#pullrequestreview-2894833060)
- `2025-06-04T05:56:46Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6837#pullrequestreview-2895317124)
- `2025-06-04T12:58:02Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6837#pullrequestreview-2896631090)
- `2025-06-04T15:04:02Z` `APPROVED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6837#pullrequestreview-2897126158)
- `2025-06-04T15:49:19Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6837#pullrequestreview-2897273093)
- `2025-06-04T15:50:41Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6837#pullrequestreview-2897283537)
- `2025-06-04T16:31:57Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6837#pullrequestreview-2897402316)
- `2025-06-05T00:12:59Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6837#pullrequestreview-2898488575)
- `2025-06-05T01:43:35Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6837#pullrequestreview-2898639898)
- `2025-06-05T01:43:45Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6837#pullrequestreview-2898640057)
- `2025-06-05T01:43:53Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6837#pullrequestreview-2898640262)

## Inline Comment Hotspots

- `sgl-kernel/csrc/moe/ep_moe_reorder_kernel.cu`: 7 inline comment(s)
- `sgl-kernel/tests/test_ep_moe_post_reorder_kernel.py`: 6 inline comment(s)
- `sgl-kernel/benchmark/bench_moe_ep_post_reorder.py`: 2 inline comment(s)
- `sgl-kernel/include/sgl_kernel_ops.h`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-04T15:47:13Z` `inline` by `BBuf` `sgl-kernel/benchmark/bench_moe_ep_post_reorder.py`:69; signals: benchmark, kernel, moe, perf, performance; excerpt: "The allocation of input tensors can be moved outside to more accurately reflect kernel performance." (https://github.com/sgl-project/sglang/pull/6837#discussion_r2126928339)
- `2025-06-04T12:58:01Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/ep_moe_reorder_kernel.cu`:162; signals: aligned, dtype, kernel, moe; excerpt: "token topk weights' dtype should be aligned with scalar t. Fixing in progress." (https://github.com/sgl-project/sglang/pull/6837#discussion_r2126538185)
- `2025-06-05T01:43:35Z` `inline` by `yuan-luo` `sgl-kernel/benchmark/bench_moe_ep_post_reorder.py`:69; signals: benchmark, kernel, moe; excerpt: "done." (https://github.com/sgl-project/sglang/pull/6837#discussion_r2127784277)
- `2025-06-05T01:44:56Z` `issue` by `yuan-luo`; signals: benchmark, perf, performance; excerpt: "Updated performance result after revising benchmark time consuming calculation." (https://github.com/sgl-project/sglang/pull/6837#issuecomment-2942427628)
- `2025-06-04T03:03:04Z` `inline` by `Alcanderian` `sgl-kernel/csrc/moe/ep_moe_reorder_kernel.cu`:93; signals: kernel, moe; excerpt: "As gemini said, we do not need computed flag." (https://github.com/sgl-project/sglang/pull/6837#discussion_r2125418282)
- `2025-06-04T05:56:46Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/ep_moe_reorder_kernel.cu`:93; signals: kernel, moe; excerpt: "Removed computed flag." (https://github.com/sgl-project/sglang/pull/6837#discussion_r2125712013)
- `2025-06-04T15:49:12Z` `inline` by `BBuf` `sgl-kernel/tests/test_ep_moe_post_reorder_kernel.py`:159; signals: kernel, moe; excerpt: "add atol=1e-5 rtol=1e-5" (https://github.com/sgl-project/sglang/pull/6837#discussion_r2126932097)
- `2025-06-04T16:31:57Z` `inline` by `yuan-luo` `sgl-kernel/tests/test_ep_moe_post_reorder_kernel.py`:159; signals: kernel, moe; excerpt: "Already added." (https://github.com/sgl-project/sglang/pull/6837#discussion_r2127010047)
- `2025-06-05T01:43:45Z` `inline` by `yuan-luo` `sgl-kernel/tests/test_ep_moe_post_reorder_kernel.py`:159; signals: kernel, moe; excerpt: "done." (https://github.com/sgl-project/sglang/pull/6837#discussion_r2127784389)
- `2025-06-05T01:43:53Z` `inline` by `yuan-luo` `sgl-kernel/tests/test_ep_moe_post_reorder_kernel.py`:96; signals: kernel, moe; excerpt: "done." (https://github.com/sgl-project/sglang/pull/6837#discussion_r2127784507)
- `2025-06-04T04:18:53Z` `issue` by `Alcanderian`; signals: bf16, kernel; excerpt: "Hello @yuan-luo , we have to support fp16/bf16/fp32 for this kernel. Ref:" (https://github.com/sgl-project/sglang/pull/6837#issuecomment-2938422062)
- `2025-06-04T04:21:55Z` `issue` by `yuan-luo`; signals: bf16, kernel; excerpt: "Hello @yuan-luo , we have to support fp16/bf16/fp32 for this kernel. Ref: 6858 Will follow up." (https://github.com/sgl-project/sglang/pull/6837#issuecomment-2938432982)
