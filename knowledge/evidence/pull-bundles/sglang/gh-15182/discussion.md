# PR Discussion Digest

- Source PR: [sgl-project/sglang#15182](https://github.com/sgl-project/sglang/pull/15182)
- Source page: `sources/prs/sglang/PR-15182.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-15182`
- Generated at: `2026-05-20T15:28:09.220242+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-15T11:04:38Z`
- Merged: `2026-01-11T07:31:29Z`

## Discussion Counts

- Issue comments: 18
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: Fridge003, HydraQYH, Qiaolin-Yu, johnnynunez, yinghai
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-15T11:06:56Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request brings in upstream changes from FlashAttention 4, notably adding support for split KV ... (https://github.com/sgl-project/sglang/pull/15182#pullrequestreview-3577619318)
- `2025-12-21T03:59:40Z` `COMMENTED` by `yinghai` (https://github.com/sgl-project/sglang/pull/15182#pullrequestreview-3601454549)
- `2026-01-06T01:38:49Z` `COMMENTED` by `HydraQYH` - Hello Johnny. I'm working with @BBuf to update the flash-attention in sgl-kernel. I pulled your commit and built ... (https://github.com/sgl-project/sglang/pull/15182#pullrequestreview-3628999846)
- `2026-01-10T08:45:12Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/15182#pullrequestreview-3646605444)
- `2026-01-11T07:19:00Z` `APPROVED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/15182#pullrequestreview-3647474897)
- `2026-01-11T07:27:50Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/15182#pullrequestreview-3647479738)
- `2026-01-11T07:28:41Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/15182#pullrequestreview-3647480329)

## Inline Comment Hotspots

- `sgl-kernel/python/sgl_kernel/_fa4_interface.py`: 2 inline comment(s)
- `sgl-kernel/CMakeLists.txt`: 2 inline comment(s)
- `python/pyproject.toml`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-06T02:18:22Z` `issue` by `HydraQYH`; signals: attention, cute, cutlass, kernel, perf, performance, sm90; excerpt: "Hello Johnny. I'm working with @BBuf to update the flash-attention in sgl-kernel. I pulled your commit and built sgl-kernel, and I found that the ..." (https://github.com/sgl-project/sglang/pull/15182#issuecomment-3712839224)
- `2026-01-06T02:21:58Z` `issue` by `johnnynunez`; signals: attention, cute, cutlass, kernel, perf, performance, sm90; excerpt: "Hello Johnny. I'm working with @BBuf to update the flash-attention in sgl-kernel. I pulled your commit and built sgl-kernel, and I found that the ..." (https://github.com/sgl-project/sglang/pull/15182#issuecomment-3712845671)
- `2026-01-06T02:23:49Z` `issue` by `HydraQYH`; signals: attention, cute, cutlass, kernel, perf, performance, sm90; excerpt: "Hello Johnny. I'm working with @BBuf to update the flash-attention in sgl-kernel. I pulled your commit and built sgl-kernel, and I found that the ..." (https://github.com/sgl-project/sglang/pull/15182#issuecomment-3712849294)
- `2026-01-06T03:13:49Z` `issue` by `johnnynunez`; signals: attention, cute, cutlass, kernel, perf, performance, sm90; excerpt: "Hello Johnny. I'm working with @BBuf to update the flash-attention in sgl-kernel. I pulled your commit and built sgl-kernel, and I found that the ..." (https://github.com/sgl-project/sglang/pull/15182#issuecomment-3712942172)
- `2026-01-06T01:52:14Z` `issue` by `johnnynunez`; signals: attention, cute, cutlass, kernel, perf, performance; excerpt: "Hello Johnny. I'm working with @BBuf to update the flash-attention in sgl-kernel. I pulled your commit and built sgl-kernel, and I found that the ..." (https://github.com/sgl-project/sglang/pull/15182#issuecomment-3712787664)
- `2026-01-06T01:38:49Z` `review` `COMMENTED` by `HydraQYH`; signals: attention, kernel, perf, performance; excerpt: "Hello Johnny. I'm working with @BBuf to update the flash-attention in sgl-kernel. I pulled your commit and built sgl-kernel, and I found that the ..." (https://github.com/sgl-project/sglang/pull/15182#pullrequestreview-3628999846)
- `2026-01-11T07:25:13Z` `issue` by `johnnynunez`; signals: b200, cute, hang, sm100; excerpt: "b200 tests passed with newest cutedsl and tvm-ffi The last commit from FA4, changed a little bit the interface.py. We can update it, i ..." (https://github.com/sgl-project/sglang/pull/15182#issuecomment-3734170373)
- `2026-01-06T01:33:08Z` `inline` by `HydraQYH` `sgl-kernel/CMakeLists.txt`:95; signals: kernel, perf, performance; excerpt: "This version seems to have a significant performance difference compared to the upstream. perhaps this branch should be rebased." (https://github.com/sgl-project/sglang/pull/15182#discussion_r2663286954)
- `2025-12-21T03:59:40Z` `inline` by `yinghai` `sgl-kernel/python/sgl_kernel/_fa4_interface.py`:351; signals: cuda, cudagraph, kernel; excerpt: "is this cudagraph friendly?" (https://github.com/sgl-project/sglang/pull/15182#discussion_r2637528596)
- `2025-12-29T15:33:24Z` `issue` by `johnnynunez`; signals: attention, flash attention, kernel; excerpt: "@Qiaolin-Yu im on vacation right now... i updated to last commit flash attention, thanks to the other fixes. The basics in sgl-kernel are working" (https://github.com/sgl-project/sglang/pull/15182#issuecomment-3696832953)
- `2025-12-29T22:50:11Z` `issue` by `Qiaolin-Yu`; signals: attention, flash attention, kernel; excerpt: "@Qiaolin-Yu im on vacation right now... i updated to last commit flash attention, thanks to the other fixes. The basics in sgl-kernel are working ..." (https://github.com/sgl-project/sglang/pull/15182#issuecomment-3697700587)
- `2026-01-11T07:10:03Z` `issue` by `johnnynunez`; signals: b200, cute, hang; excerpt: "b200 tests passed with newest cutedsl and tvm-ffi The last commit from FA4, changed a little bit the interface.py. We can update it, i ..." (https://github.com/sgl-project/sglang/pull/15182#issuecomment-3734148877)
