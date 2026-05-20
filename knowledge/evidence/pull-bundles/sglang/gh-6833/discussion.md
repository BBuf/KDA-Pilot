# PR Discussion Digest

- Source PR: [sgl-project/sglang#6833](https://github.com/sgl-project/sglang/pull/6833)
- Source page: `sources/prs/sglang/PR-6833.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6833`
- Generated at: `2026-05-20T15:30:49.032663+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-03T08:45:27Z`
- Merged: `2025-06-10T08:08:15Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 15 (approved=3, changes_requested=4, commented=8)
- Inline review comments: 22
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=9, outdated=5
- Human participants with discussion text: mingfeima, zhyncs
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-03T08:45:47Z` `COMMENTED` by `gemini-code-assist` - Hello @yanbing-j, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post my feedback shortly. ... (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2891339478)
- `2025-06-03T08:47:42Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This pull request introduces significant optimizations for decode performance, particularly targeting AVX512-capable CPUs by mapping algorithms ... (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2891345702)
- `2025-06-04T05:08:21Z` `CHANGES_REQUESTED` by `mingfeima` - i think we can add all the diffs from our developing branch to this one. (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2895178256)
- `2025-06-09T05:08:10Z` `COMMENTED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2908927900)
- `2025-06-09T05:08:51Z` `COMMENTED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2908928608)
- `2025-06-09T05:09:33Z` `COMMENTED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2908929330)
- `2025-06-09T05:11:30Z` `COMMENTED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2908931741)
- `2025-06-09T05:12:03Z` `COMMENTED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2908932436)
- `2025-06-09T05:12:16Z` `COMMENTED` by `gemini-code-assist` (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2908932681)
- `2025-06-09T05:24:35Z` `CHANGES_REQUESTED` by `mingfeima` - almost done, just some minor issues to address to. (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2908932866)
- `2025-06-10T01:40:34Z` `CHANGES_REQUESTED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2911743024)
- `2025-06-10T02:37:21Z` `COMMENTED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2911810712)
- `2025-06-10T02:37:40Z` `APPROVED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2911811031)
- `2025-06-10T07:17:28Z` `APPROVED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2912272936)
- `2025-06-10T08:07:53Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/6833#pullrequestreview-2912438060)

## Inline Comment Hotspots

- `sgl-kernel/csrc/cpu/decode.cpp`: 10 inline comment(s)
- `sgl-kernel/csrc/cpu/qkv_proj.cpp`: 6 inline comment(s)
- `sgl-kernel/csrc/cpu/extend.cpp`: 4 inline comment(s)
- `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`: 1 inline comment(s)
- `test/srt/cpu/test_norm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-09T05:11:30Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/decode.cpp`:1305; signals: hang, kernel, memory; excerpt: "at::vec::map requires contiguous memory inputs. So change to n size won't work properly. And also working on non-valid data is not a issue, this ..." (https://github.com/sgl-project/sglang/pull/6833#discussion_r2135040005)
- `2025-06-04T05:19:16Z` `issue` by `mingfeima`; signals: hang, kernel, mla; excerpt: "@yanbing-j to simplify upstreaming efforts, put all the diffs from in sgl-kernel to this one. change the PR title to be something like "CPU: ..." (https://github.com/sgl-project/sglang/pull/6833#issuecomment-2938604146)
- `2025-06-09T05:08:51Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/decode.cpp`:39; signals: kernel, mla; excerpt: "add "head size == head size v + 64" when entering mla kernels." (https://github.com/sgl-project/sglang/pull/6833#discussion_r2135038017)
- `2025-06-09T05:21:46Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/torch_extension_cpu.cpp`:185; signals: hang, kernel; excerpt: "change the func name." (https://github.com/sgl-project/sglang/pull/6833#discussion_r2135047623)
- `2025-06-10T02:37:21Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/qkv_proj.cpp`:663; signals: kernel, vector; excerpt: "forgot split returns a vector instead of tuple, skip this." (https://github.com/sgl-project/sglang/pull/6833#discussion_r2136805299)
- `2025-06-09T05:21:18Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/qkv_proj.cpp`:660; signals: kernel; excerpt: "use torch.split and since we are spliting dim0, you don't need .contiguous(). The result tensors should be contiguous anyway, you may double check that." (https://github.com/sgl-project/sglang/pull/6833#discussion_r2135047327)
- `2025-06-09T05:08:10Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/decode.cpp`:1451; signals: kernel; excerpt: "let's put tighter restrict here:" (https://github.com/sgl-project/sglang/pull/6833#discussion_r2135037559)
- `2025-06-09T05:09:32Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/decode.cpp`:83; signals: kernel; excerpt: "this is checked when convert weight to vnni format." (https://github.com/sgl-project/sglang/pull/6833#discussion_r2135038502)
- `2025-06-09T05:12:03Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/decode.cpp`:1451; signals: kernel; excerpt: "fix gemini code review" (https://github.com/sgl-project/sglang/pull/6833#discussion_r2135040418)
- `2025-06-09T05:12:28Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/extend.cpp`:92; signals: kernel; excerpt: "same as above." (https://github.com/sgl-project/sglang/pull/6833#discussion_r2135040681)
- `2025-06-09T05:12:59Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/extend.cpp`:133; signals: kernel; excerpt: "covered in weight prepacking logic." (https://github.com/sgl-project/sglang/pull/6833#discussion_r2135040998)
- `2025-06-09T05:15:47Z` `inline` by `mingfeima` `sgl-kernel/csrc/cpu/qkv_proj.cpp`:633; signals: kernel; excerpt: "not a very good naming ..." (https://github.com/sgl-project/sglang/pull/6833#discussion_r2135043052)
