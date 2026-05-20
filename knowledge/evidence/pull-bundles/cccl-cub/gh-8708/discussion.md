# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8708](https://github.com/NVIDIA/cccl/pull/8708)
- Source page: `sources/prs/cccl-cub/PR-8708.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8708`
- Generated at: `2026-05-20T15:20:53.429660+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-28T09:43:37Z`
- Merged: `2026-05-07T18:53:13Z`

## Discussion Counts

- Issue comments: 38
- Review submissions: 13 (approved=4, changes_requested=4, commented=5)
- Inline review comments: 33
- Review threads observed: 28
- Resolved/outdated thread markers: resolved=10, outdated=18
- Human participants with discussion text: NaderAlAwar, bernhardmgruber, davebayer, fbusato, miscco, oleksandr-pavlyk, rmalani-nv
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-28T12:45:45Z` `APPROVED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8708#pullrequestreview-4188858660)
- `2026-04-28T14:08:30Z` `COMMENTED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8708#pullrequestreview-4189430302)
- `2026-04-28T14:33:47Z` `CHANGES_REQUESTED` by `davebayer` - I am missing docs and tests (https://github.com/NVIDIA/cccl/pull/8708#pullrequestreview-4189724392)
- `2026-04-28T14:45:17Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8708#pullrequestreview-4189846662)
- `2026-04-28T15:07:03Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/8708#pullrequestreview-4190008152)
- `2026-04-28T17:48:08Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/8708#pullrequestreview-4191197723)
- `2026-04-28T17:54:04Z` `CHANGES_REQUESTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/8708#pullrequestreview-4191205842)
- `2026-04-29T19:13:23Z` `CHANGES_REQUESTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/8708#pullrequestreview-4199985233)
- `2026-04-30T09:55:19Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/8708#pullrequestreview-4204155447)
- `2026-05-05T05:56:52Z` `APPROVED` by `davebayer` - Code looks fine now, please address @fbusato's comments regarding the documentation. Thank you! (https://github.com/NVIDIA/cccl/pull/8708#pullrequestreview-4225600106)
- `2026-05-05T16:53:16Z` `CHANGES_REQUESTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/8708#pullrequestreview-4229993030)
- `2026-05-06T17:09:26Z` `APPROVED` by `fbusato` - looks good. Please address the consteval comment, then we can merge it (https://github.com/NVIDIA/cccl/pull/8708#pullrequestreview-4238099459)
- `2026-05-07T08:08:59Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8708#pullrequestreview-4242204091)

## Inline Comment Hotspots

- `libcudacxx/include/cuda/__functional/always_true_false.h`: 12 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_transform.cuh`: 3 inline comment(s)
- `docs/libcudacxx/extended_api/functional.rst`: 3 inline comment(s)
- `cub/test/catch2_test_device_partition_if.cu`: 2 inline comment(s)
- `cub/test/catch2_test_device_select_if.cu`: 2 inline comment(s)
- `libcudacxx/test/libcudacxx/cuda/functional/always_true_false.pass.cpp`: 1 inline comment(s)
- `libcudacxx/include/cuda/std/__type_traits/always_false.h`: 1 inline comment(s)
- `cub/cub/device/dispatch/kernels/kernel_transform.cuh`: 1 inline comment(s)
- `cub/cub/device/dispatch/dispatch_copy_mdspan.cuh`: 1 inline comment(s)
- `cub/cub/device/device_find.cuh`: 1 inline comment(s)
- `cub/cub/device/device_transform.cuh`: 1 inline comment(s)
- `libcudacxx/include/cuda/std/__pstl/cuda/copy_n.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-29T16:08:50Z` `issue` by `rmalani-nv`; signals: cuda, hang, kernel; excerpt: "✅ All review comments addressed in commit f07c79b. Here's a summary of changes: Changes made 1. Renamed always true t → always true and ..." (https://github.com/NVIDIA/cccl/pull/8708#issuecomment-4345460145)
- `2026-05-05T00:50:30Z` `issue` by `rmalani-nv`; signals: cuda, hang, kernel; excerpt: "✅ Feedback addressed in commit db44010. Changes: 1. Removed always true predicate alias — use ::cuda::always true directly (davebayer) - Removed the using always ..." (https://github.com/NVIDIA/cccl/pull/8708#issuecomment-4375694238)
- `2026-05-06T16:50:24Z` `issue` by `rmalani-nv`; signals: cuda, hang, kernel; excerpt: "✅ Addressed fbusato's review feedback in commit fe13101de3. Changes: 1. Added missing include (fbusato: "header inclusion is probably missing here") Files that directly use ..." (https://github.com/NVIDIA/cccl/pull/8708#issuecomment-4390220337)
- `2026-05-06T18:03:09Z` `issue` by `rmalani-nv`; signals: compile, cuda, hang; excerpt: "Done. Pushed commit 8ae1f1bb3a to address the reviewer's consteval comment. What I did: Changed operator() in both always true and always false from constexpr ..." (https://github.com/NVIDIA/cccl/pull/8708#issuecomment-4390689453)
- `2026-04-29T22:54:55Z` `issue` by `rmalani-nv`; signals: cuda, hang; excerpt: "✅ Feedback addressed in commit 7941d6b. Changes: 1. Simplified documentation (always true false.h) — Removed verbose @par Overview and @par Example doxygen sections, keeping ..." (https://github.com/NVIDIA/cccl/pull/8708#issuecomment-4348109277)
- `2026-05-05T16:22:24Z` `issue` by `rmalani-nv`; signals: cuda, hang; excerpt: "✅ Documentation comment addressed in commit d17efe7c51. The review feedback was requesting proper extended API documentation for cuda::always true and cuda::always false. This has ..." (https://github.com/NVIDIA/cccl/pull/8708#issuecomment-4381094410)
- `2026-04-28T13:57:09Z` `inline` by `NaderAlAwar` `cub/cub/device/dispatch/tuning/tuning_transform.cuh`:36; signals: cuda; excerpt: "Suggestion: I don't see a real need to keep this type alias. We should just use cuda::always true t directly" (https://github.com/NVIDIA/cccl/pull/8708#discussion_r3154669333)
- `2026-04-28T13:58:38Z` `inline` by `NaderAlAwar` `cub/test/catch2_test_device_partition_if.cu`:29; signals: cuda; excerpt: "Nit: in .cu files we don't fully qualify the cuda namespace. So you can just do Same applies to other test files" (https://github.com/NVIDIA/cccl/pull/8708#discussion_r3154679188)
- `2026-04-28T14:45:17Z` `inline` by `miscco` `libcudacxx/include/cuda/__functional/always_true_false.h`:63; signals: cuda; excerpt: "I mean that is the style of CPOs, but I am not sure whether we want those as CPOs given the current restrictions" (https://github.com/NVIDIA/cccl/pull/8708#discussion_r3155027788)
- `2026-04-28T15:07:03Z` `inline` by `davebayer` `libcudacxx/include/cuda/__functional/always_true_false.h`:63; signals: cuda; excerpt: "I don't see the motivation for these CPOs. We also don't have cuda::std::plus cpo or something similar, those are just ordinary functors, too. So, ..." (https://github.com/NVIDIA/cccl/pull/8708#discussion_r3155162833)
- `2026-04-29T19:11:26Z` `inline` by `fbusato` `libcudacxx/include/cuda/__functional/always_true_false.h`:28; signals: cuda; excerpt: "about the documentation, I was referring to docs/libcudacxx/extended api. For libcu++, we don't generate the documentation with Doxygen. I would avoid detailed description in ..." (https://github.com/NVIDIA/cccl/pull/8708#discussion_r3163538849)
- `2026-04-28T14:08:27Z` `inline` by `NaderAlAwar` `libcudacxx/include/cuda/__functional/always_true_false.h`:63; signals: cuda; excerpt: "Suggestion: instead of inline constexpr, we should use CCCL GLOBAL CONSTANT." (https://github.com/NVIDIA/cccl/pull/8708#discussion_r3154749769)
