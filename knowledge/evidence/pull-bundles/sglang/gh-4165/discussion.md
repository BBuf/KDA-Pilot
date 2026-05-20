# PR Discussion Digest

- Source PR: [sgl-project/sglang#4165](https://github.com/sgl-project/sglang/pull/4165)
- Source page: `sources/prs/sglang/PR-4165.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4165`
- Generated at: `2026-05-20T15:30:07.129711+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-07T07:04:33Z`
- Merged: `2025-03-10T07:35:07Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 5 (approved=1, changes_requested=1, commented=3)
- Inline review comments: 10
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=9
- Human participants with discussion text: CUHKSZzxy, FlamingoPg, HandH1998, inkhare, laixinn, lishicheng1996, sleepcoo, tbzhang, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 6

## Review Decisions

- `2025-03-07T07:18:10Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/4165#pullrequestreview-2666446297)
- `2025-03-08T20:45:48Z` `CHANGES_REQUESTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/4165#pullrequestreview-2669261099)
- `2025-03-09T09:17:53Z` `COMMENTED` by `laixinn` (https://github.com/sgl-project/sglang/pull/4165#pullrequestreview-2669358928)
- `2025-03-10T07:22:55Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/4165#pullrequestreview-2669993988)
- `2025-03-10T07:33:06Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/4165#pullrequestreview-2670013909)

## Inline Comment Hotspots

- `sgl-kernel/setup.py`: 3 inline comment(s)
- `.gitmodules`: 3 inline comment(s)
- `sgl-kernel/build.sh`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8_kernel.py`: 1 inline comment(s)
- `scripts/ci_install_dependency.sh`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-09T09:17:53Z` `inline` by `laixinn` `sgl-kernel/setup.py`:89; signals: deepgemm, gemm, kernel; excerpt: "no it is not necessary, copying deepgemm/deep gemm to python/site-packages is enough" (https://github.com/sgl-project/sglang/pull/4165#discussion_r1986261856)
- `2025-03-08T12:24:37Z` `issue` by `FlamingoPg`; signals: deepgemm, gemm, kernel; excerpt: "Test We fix deepgemm build with JIT module. 1. Install command: 2. Test script is copied from deepgemm/tests/test core.py Deepgemm test result below: How ..." (https://github.com/sgl-project/sglang/pull/4165#issuecomment-2708240206)
- `2025-03-09T09:41:50Z` `issue` by `laixinn`; signals: deepgemm, gemm, kernel; excerpt: "@zhyncs Symlinks are necessary for the head files of JIT. DeepGemm tests are forked into sgl-kernel tests." (https://github.com/sgl-project/sglang/pull/4165#issuecomment-2708761479)
- `2025-03-07T07:18:10Z` `inline` by `zhyncs` `python/sglang/srt/layers/quantization/fp8_kernel.py`:610; signals: fp8, kernel; excerpt: "this is duplicate" (https://github.com/sgl-project/sglang/pull/4165#discussion_r1984569263)
- `2025-03-08T20:43:35Z` `inline` by `zhyncs` `scripts/ci_install_dependency.sh`:29; signals: hang; excerpt: "don't change scripts/ci install dependency.sh for now" (https://github.com/sgl-project/sglang/pull/4165#discussion_r1986151299)
- `2025-03-08T20:43:50Z` `inline` by `zhyncs` `sgl-kernel/build.sh`:19; signals: kernel; excerpt: "remove this" (https://github.com/sgl-project/sglang/pull/4165#discussion_r1986151331)
- `2025-03-08T20:44:04Z` `inline` by `zhyncs` `sgl-kernel/build.sh`:28; signals: kernel; excerpt: "remove this" (https://github.com/sgl-project/sglang/pull/4165#discussion_r1986151355)
- `2025-03-08T20:45:30Z` `inline` by `zhyncs` `sgl-kernel/setup.py`:89; signals: kernel; excerpt: "Why use symlink? Do we need to copy instead?" (https://github.com/sgl-project/sglang/pull/4165#discussion_r1986151575)
- `2025-03-07T09:05:18Z` `issue` by `HandH1998`; signals: general review; excerpt: "Please fix build error It seems that the version of setuptools in CI is old. We succeed to build it with = 75.0.0 locally. ..." (https://github.com/sgl-project/sglang/pull/4165#issuecomment-2705906287)
- `2025-03-10T07:31:44Z` `issue` by `zhyncs`; signals: general review; excerpt: "Thank you all! The code is functional but messy. I will work on improving it later, but for now I will merge it." (https://github.com/sgl-project/sglang/pull/4165#issuecomment-2709664452)
