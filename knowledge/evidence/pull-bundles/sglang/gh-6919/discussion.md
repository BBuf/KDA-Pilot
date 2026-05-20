# PR Discussion Digest

- Source PR: [sgl-project/sglang#6919](https://github.com/sgl-project/sglang/pull/6919)
- Source page: `sources/prs/sglang/PR-6919.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6919`
- Generated at: `2026-05-20T15:30:54.559934+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-06T09:37:21Z`
- Merged: `2025-06-12T03:43:09Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 17 (approved=3, changes_requested=1, commented=13)
- Inline review comments: 19
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=11, outdated=12
- Human participants with discussion text: Alcanderian, BBuf, merrymercy, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-06T09:37:42Z` `COMMENTED` by `gemini-code-assist` - Hello @yuan-luo, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post my feedback shortly. ... (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2904390322)
- `2025-06-06T09:38:51Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This pull request introduces a new CUDA kernel ep moe silu and mul for Mixture-of-Experts, along ... (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2904392880)
- `2025-06-09T05:17:52Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2908939305)
- `2025-06-09T05:20:16Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2908941881)
- `2025-06-09T05:26:33Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2908948981)
- `2025-06-09T05:27:52Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2908951418)
- `2025-06-09T05:28:14Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2908952119)
- `2025-06-09T06:01:52Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2908999304)
- `2025-06-09T06:34:10Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2909063542)
- `2025-06-09T06:36:28Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2909073294)
- `2025-06-09T08:04:48Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2909290590)
- `2025-06-09T08:05:39Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2909293574)
- `2025-06-09T09:11:26Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2909446822)
- `2025-06-09T13:08:04Z` `APPROVED` by `BBuf` - LGTM. (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2910021035)
- `2025-06-09T15:40:08Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2910473383)
- `2025-06-09T17:26:46Z` `APPROVED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2910775849)
- `2025-06-10T11:56:03Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/6919#pullrequestreview-2913224039)

## Inline Comment Hotspots

- `sgl-kernel/csrc/moe/ep_moe_silu_and_mul_kernel.cu`: 8 inline comment(s)
- `sgl-kernel/csrc/moe/ep_moe_silu_and_mul.cu`: 7 inline comment(s)
- `sgl-kernel/tests/test_ep_moe_silu_and_mul_kernel.py`: 2 inline comment(s)
- `sgl-kernel/benchmark/bench_moe_silu_and_mul.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-06-09T09:11:26Z` `inline` by `Alcanderian` `sgl-kernel/csrc/moe/ep_moe_silu_and_mul_kernel.cu`:95; signals: block, kernel, moe, perf, performance; excerpt: "improve performance with dynamic block size refer to:" (https://github.com/sgl-project/sglang/pull/6919#discussion_r2135351263)
- `2025-06-09T05:20:16Z` `inline` by `BBuf` `sgl-kernel/benchmark/bench_moe_silu_and_mul.py`:27; signals: benchmark, kernel, moe; excerpt: "Can these variables also take different value combinations in the configs above?" (https://github.com/sgl-project/sglang/pull/6919#discussion_r2135046404)
- `2025-06-08T08:48:07Z` `issue` by `yuan-luo`; signals: benchmark, cuda, triton; excerpt: "Benchmark result, CUDA gains 10% improvement over Triton." (https://github.com/sgl-project/sglang/pull/6919#issuecomment-2953774244)
- `2025-06-09T05:26:32Z` `inline` by `BBuf` `sgl-kernel/csrc/moe/ep_moe_silu_and_mul_kernel.cu`:61; signals: kernel, moe; excerpt: "It might be worth considering how to handle the tail elements when hidden size is not divisible by vec size." (https://github.com/sgl-project/sglang/pull/6919#discussion_r2135051559)
- `2025-06-09T05:17:52Z` `inline` by `BBuf` `sgl-kernel/tests/test_ep_moe_silu_and_mul_kernel.py`:81; signals: kernel, moe; excerpt: "The function can be deleted now?" (https://github.com/sgl-project/sglang/pull/6919#discussion_r2135044637)
- `2025-06-09T05:27:52Z` `inline` by `BBuf` `sgl-kernel/csrc/moe/ep_moe_silu_and_mul_kernel.cu`:77; signals: kernel, moe; excerpt: "It's no necessary?" (https://github.com/sgl-project/sglang/pull/6919#discussion_r2135052696)
- `2025-06-09T06:01:52Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/ep_moe_silu_and_mul_kernel.cu`:77; signals: kernel, moe; excerpt: "Removed." (https://github.com/sgl-project/sglang/pull/6919#discussion_r2135083615)
- `2025-06-09T06:34:10Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/ep_moe_silu_and_mul_kernel.cu`:61; signals: kernel, moe; excerpt: "Added logic to handle tail elements when hidden size is not divisible by vec size." (https://github.com/sgl-project/sglang/pull/6919#discussion_r2135120027)
- `2025-06-09T06:36:28Z` `inline` by `yuan-luo` `sgl-kernel/tests/test_ep_moe_silu_and_mul_kernel.py`:81; signals: kernel, moe; excerpt: "Replaced by torch.testing.assert close." (https://github.com/sgl-project/sglang/pull/6919#discussion_r2135123806)
- `2025-06-09T08:05:39Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/ep_moe_silu_and_mul_kernel.cu`:91; signals: kernel, moe; excerpt: "Removed." (https://github.com/sgl-project/sglang/pull/6919#discussion_r2135251905)
- `2025-06-09T15:40:07Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/ep_moe_silu_and_mul_kernel.cu`:95; signals: kernel, moe; excerpt: "Resolved." (https://github.com/sgl-project/sglang/pull/6919#discussion_r2135963089)
