# PR Discussion Digest

- Source PR: [sgl-project/sglang#7884](https://github.com/sgl-project/sglang/pull/7884)
- Source page: `sources/prs/sglang/PR-7884.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7884`
- Generated at: `2026-05-20T15:31:21.453860+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-09T06:10:36Z`
- Merged: `2025-07-17T11:33:02Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 16 (approved=2, changes_requested=1, commented=13)
- Inline review comments: 19
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=8, outdated=7
- Human participants with discussion text: Alcanderian, ispobock, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-09T06:10:57Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @yuan-luo, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3000125284)
- `2025-07-09T06:12:09Z` `COMMENTED` by `gemini-code-assist` - Code Review The code changes introduce block scan warp scan in fused MoE path moe align block size ... (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3000131286)
- `2025-07-09T07:39:45Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3000414512)
- `2025-07-09T08:06:29Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3000494076)
- `2025-07-09T08:26:22Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3000553294)
- `2025-07-09T13:59:39Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3001655954)
- `2025-07-10T02:11:18Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3003632018)
- `2025-07-10T02:26:29Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3003651490)
- `2025-07-10T02:27:09Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3003652849)
- `2025-07-10T02:39:36Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3003673100)
- `2025-07-10T02:40:10Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3003673742)
- `2025-07-10T02:40:52Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3003674734)
- `2025-07-10T15:15:05Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3006198939)
- `2025-07-11T07:52:18Z` `APPROVED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3009084445)
- `2025-07-14T02:56:31Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3014646660)
- `2025-07-14T07:05:18Z` `CHANGES_REQUESTED` by `ispobock` - It seems all the AMD tests are failed. This kernel is also used on AMD GPUs. Please have ... (https://github.com/sgl-project/sglang/pull/7884#pullrequestreview-3015008231)

## Inline Comment Hotspots

- `sgl-kernel/csrc/moe/moe_align_kernel.cu`: 19 inline comment(s)

## High-Signal Discussion

- `2025-07-09T08:06:29Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/moe_align_kernel.cu`:137; signals: kernel, moe, overflow, warp; excerpt: "If nw is smaller than lane id, val will directly obtains 0, so there's no "process elements beyond the valid range of warp sums, ..." (https://github.com/sgl-project/sglang/pull/7884#discussion_r2194353248)
- `2025-07-11T05:57:30Z` `issue` by `yuan-luo`; signals: attention, benchmark, fp8, throughput; excerpt: "Why the Output throughput of this PR is much less than the main branch? Could you try Qwen/Qwen3-235B-A22B-FP8? My test machine H20 is shared ..." (https://github.com/sgl-project/sglang/pull/7884#issuecomment-3060700652)
- `2025-07-09T07:39:45Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/moe_align_kernel.cu`:135; signals: kernel, moe, warp; excerpt: "It will not lead to incorrect results. In case the invalid lane (tid = scan size) scan, v returns 0, the scan tree add ..." (https://github.com/sgl-project/sglang/pull/7884#discussion_r2194299498)
- `2025-07-09T08:26:22Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/moe_align_kernel.cu`:116; signals: kernel, moe, warp; excerpt: "The warp sums[k] stores the k-th warp's valid lanes' inclusive sum. If use warp sums[std::min(((scan size + WARP SIZE - 1) 5) - 1, ..." (https://github.com/sgl-project/sglang/pull/7884#discussion_r2194393303)
- `2025-07-09T13:54:26Z` `inline` by `ispobock` `sgl-kernel/csrc/moe/moe_align_kernel.cu`:109; signals: kernel, moe, warp; excerpt: "I see you use (scan size + WARP SIZE - 1) / WARP SIZE for many time. There are some duplicated computation. Please store ..." (https://github.com/sgl-project/sglang/pull/7884#discussion_r2195101855)
- `2025-07-09T13:50:45Z` `inline` by `ispobock` `sgl-kernel/csrc/moe/moe_align_kernel.cu`:100; signals: kernel, moe, warp; excerpt: "5 assumes that WARP SIZE always 32?" (https://github.com/sgl-project/sglang/pull/7884#discussion_r2195093237)
- `2025-07-09T13:52:39Z` `inline` by `ispobock` `sgl-kernel/csrc/moe/moe_align_kernel.cu`:102; signals: kernel, moe, warp; excerpt: "Could you make the variable name more readable? For example, num warps for scan?" (https://github.com/sgl-project/sglang/pull/7884#discussion_r2195097703)
- `2025-07-10T02:11:18Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/moe_align_kernel.cu`:109; signals: kernel, moe, warp; excerpt: "OK, it is num warps for scan. Refactored." (https://github.com/sgl-project/sglang/pull/7884#discussion_r2196351020)
- `2025-07-10T02:40:10Z` `inline` by `yuan-luo` `sgl-kernel/csrc/moe/moe_align_kernel.cu`:100; signals: kernel, moe, warp; excerpt: "Revised to "/ WARP SIZE"." (https://github.com/sgl-project/sglang/pull/7884#discussion_r2196383167)
- `2025-07-09T13:49:07Z` `inline` by `ispobock` `sgl-kernel/csrc/moe/moe_align_kernel.cu`:91; signals: kernel, moe; excerpt: "why introduce one more variable?" (https://github.com/sgl-project/sglang/pull/7884#discussion_r2195089445)
- `2025-07-09T13:57:19Z` `inline` by `ispobock` `sgl-kernel/csrc/moe/moe_align_kernel.cu`:116; signals: kernel, moe; excerpt: "Why introduce one more variable?" (https://github.com/sgl-project/sglang/pull/7884#discussion_r2195110089)
- `2025-07-09T13:58:24Z` `inline` by `ispobock` `sgl-kernel/csrc/moe/moe_align_kernel.cu`:149; signals: kernel, moe; excerpt: "Do we still need to keep prefix?" (https://github.com/sgl-project/sglang/pull/7884#discussion_r2195112513)
