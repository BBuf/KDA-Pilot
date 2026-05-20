# PR Discussion Digest

- Source PR: [sgl-project/sglang#6404](https://github.com/sgl-project/sglang/pull/6404)
- Source page: `sources/prs/sglang/PR-6404.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6404`
- Generated at: `2026-05-20T15:30:39.762082+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-19T02:29:14Z`
- Merged: `2025-05-23T09:01:55Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 5
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: chunyuan-w, mingfeima, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-05-20T04:55:10Z` `APPROVED` by `mingfeima` - LGTM (https://github.com/sgl-project/sglang/pull/6404#pullrequestreview-2852611146)
- `2025-05-20T04:58:14Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/6404#pullrequestreview-2852618245)
- `2025-05-20T05:25:56Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6404#pullrequestreview-2852656047)
- `2025-05-20T05:29:46Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/6404#pullrequestreview-2852662867)
- `2025-05-20T05:41:26Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6404#pullrequestreview-2852681061)
- `2025-05-20T07:56:36Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6404#pullrequestreview-2853097262)

## Inline Comment Hotspots

- `sgl-kernel/csrc/cpu/CMakeLists.txt`: 5 inline comment(s)

## High-Signal Discussion

- `2025-05-23T07:12:34Z` `issue` by `mingfeima`; signals: attention, compile, gemm, hang, kernel, vector; excerpt: "@zhyncs two types of errors here: 1. for the error "ImportError: cannot import name 'extend attention cpu' from 'sgl kernel.common ops' (/usr/local/lib/python3.10/dist-packages/sgl kernel/common ops.cpython-310-x86 ..." (https://github.com/sgl-project/sglang/pull/6404#issuecomment-2903493495)
- `2025-05-20T05:29:46Z` `inline` by `zhyncs` `sgl-kernel/csrc/cpu/CMakeLists.txt`:48; signals: kernel; excerpt: "And can we delete setup cpu.py after 6419 BTW we don't recommend to use pybind11, because we want to use one whl for all ..." (https://github.com/sgl-project/sglang/pull/6404#discussion_r2096955438)
- `2025-05-20T05:41:26Z` `inline` by `chunyuan-w` `sgl-kernel/csrc/cpu/CMakeLists.txt`:48; signals: kernel; excerpt: "@mingfeima I think it's fine that we remove setup cpu.py after Do you have any other concern? @blzheng is checking how to avoid introducing ..." (https://github.com/sgl-project/sglang/pull/6404#discussion_r2096967794)
- `2025-05-20T04:58:14Z` `inline` by `zhyncs` `sgl-kernel/csrc/cpu/CMakeLists.txt`:48; signals: kernel; excerpt: "QQ Are we currently using CMake or setup? Can you please share the build commands? Thank you!" (https://github.com/sgl-project/sglang/pull/6404#discussion_r2096924135)
- `2025-05-20T05:25:56Z` `inline` by `chunyuan-w` `sgl-kernel/csrc/cpu/CMakeLists.txt`:48; signals: kernel; excerpt: "is needed to fix the CMake build issue. The CMake build command to use with will be:" (https://github.com/sgl-project/sglang/pull/6404#discussion_r2096950817)
- `2025-05-20T07:56:36Z` `inline` by `chunyuan-w` `sgl-kernel/csrc/cpu/CMakeLists.txt`:48; signals: kernel; excerpt: "I confirmed offline with Mingfei that we will remove setup cpu.py after" (https://github.com/sgl-project/sglang/pull/6404#discussion_r2097252329)
- `2025-05-23T01:32:36Z` `issue` by `chunyuan-w`; signals: hang; excerpt: "Hi @zhyncs could you please share the CPU type you used (the output of lscpu should be fine)? For this error s8s8 compensation not ..." (https://github.com/sgl-project/sglang/pull/6404#issuecomment-2903012074)
