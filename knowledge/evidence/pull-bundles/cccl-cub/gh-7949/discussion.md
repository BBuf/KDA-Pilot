# PR Discussion Digest

- Source PR: [NVIDIA/cccl#7949](https://github.com/NVIDIA/cccl/pull/7949)
- Source page: `sources/prs/cccl-cub/PR-7949.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-7949`
- Generated at: `2026-05-20T15:20:23.804877+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-09T21:25:12Z`
- Merged: `2026-05-14T21:21:07Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 10
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=6, outdated=5
- Human participants with discussion text: bernhardmgruber, coderabbitai, davebayer, miscco
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-25T18:37:25Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4008339909)
- `2026-03-25T22:56:13Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4010297888)
- `2026-03-25T23:12:00Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4010457968)
- `2026-03-30T06:48:04Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4028403707)
- `2026-05-12T15:12:21Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4273654377)
- `2026-05-13T15:32:25Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4283113725)
- `2026-05-13T15:53:31Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4283266439)
- `2026-05-13T16:28:39Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4283557859)
- `2026-05-13T16:43:12Z` `COMMENTED` by `coderabbitai` - ♻️ Duplicate comments (1) cub/test/catch2 test device radix sort env.cu (1) 1154-1164: ⚠️ Potential issue 🟠 Major ⚡ ... (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4283670479)
- `2026-05-13T18:47:12Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 --- ℹ️ Review info ⚙️ Run configuration Configuration used : Path: .coderabbit.yaml Review profile ... (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4284477357)
- `2026-05-14T20:25:45Z` `APPROVED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4293187249)

## Inline Comment Hotspots

- `cub/benchmarks/bench/radix_sort/keys.cu`: 4 inline comment(s)
- `cub/benchmarks/bench/segmented_radix_sort/keys.cu`: 2 inline comment(s)
- `cub/cub/device/device_segmented_radix_sort.cuh`: 1 inline comment(s)
- `cub/cub/device/device_radix_sort.cuh`: 1 inline comment(s)
- `cub/test/catch2_test_device_radix_sort_env.cu`: 1 inline comment(s)
- `cub/benchmarks/bench/radix_sort/policy_selector.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-13T18:47:12Z` `inline` by `coderabbitai` `cub/benchmarks/bench/radix_sort/policy_selector.h`:119; signals: benchmark, correctness, cuda, memory, perf, performance, regression; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win important: Keep the onesweep gate on the same selector path as the temp-storage sizing. max temp ..." (https://github.com/NVIDIA/cccl/pull/7949#discussion_r3236680613)
- `2026-05-13T15:45:02Z` `issue` by `coderabbitai`; signals: benchmark, block, cute, hang, memory, nan, shared memory; excerpt: "[ cub/benchmarks/bench/radix sort/policy selector.h --- 📝 Walkthrough Summary by CodeRabbit Refactor Centralized radix-sort tuning and dispatch for more consistent, maintainable sorting behavior. Benchmarks simplified ..." (https://github.com/NVIDIA/cccl/pull/7949#issuecomment-4442754484)
- `2026-05-13T15:53:31Z` `review` `COMMENTED` by `coderabbitai`; signals: benchmark, cuda, hang; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4283266439)
- `2026-05-13T16:43:12Z` `review` `COMMENTED` by `coderabbitai`; signals: correctness, hang; excerpt: "♻️ Duplicate comments (1) cub/test/catch2 test device radix sort env.cu (1) 1154-1164: ⚠️ Potential issue 🟠 Major ⚡ Quick win important: These tuning tests ..." (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4283670479)
- `2026-05-13T18:47:12Z` `review` `COMMENTED` by `coderabbitai`; signals: benchmark, hang; excerpt: "Actionable comments posted: 1 --- ℹ️ Review info ⚙️ Run configuration Configuration used : Path: .coderabbit.yaml Review profile : CHILL Plan : Enterprise Run ..." (https://github.com/NVIDIA/cccl/pull/7949#pullrequestreview-4284477357)
- `2026-03-25T17:03:08Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/segmented_radix_sort/keys.cu`:21; signals: benchmark, hang; excerpt: "This is a breaking change of the benchmark and I need feedback whether we are ok with that. We previously tested segmented radix sort ..." (https://github.com/NVIDIA/cccl/pull/7949#discussion_r2989704670)
- `2026-05-13T15:53:29Z` `inline` by `coderabbitai` `cub/cub/device/device_radix_sort.cuh`:188; signals: cuda, cute; excerpt: "⚠️ Potential issue 🟠 Major 🏗️ Heavy lift 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/cccl Length of output: 97 --- 🏁 Script executed: ..." (https://github.com/NVIDIA/cccl/pull/7949#discussion_r3235642671)
- `2026-03-25T23:12:00Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/radix_sort/keys.cu`:53; signals: benchmark, deadlock; excerpt: "TODO: This deadlocks now during benchmark execution." (https://github.com/NVIDIA/cccl/pull/7949#discussion_r2991593061)
- `2026-05-13T15:32:25Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/radix_sort/keys.cu`:59; signals: benchmark, cuda; excerpt: "Using CCCL TRY CUDA API" (https://github.com/NVIDIA/cccl/pull/7949#discussion_r3235506660)
- `2026-03-25T22:32:03Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/radix_sort/keys.cu`:59; signals: benchmark; excerpt: "What to do here?" (https://github.com/NVIDIA/cccl/pull/7949#discussion_r2991448304)
- `2026-05-12T15:12:20Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/radix_sort/keys.cu`:53; signals: benchmark; excerpt: "Maybe this was also caused by 8901" (https://github.com/NVIDIA/cccl/pull/7949#discussion_r3227575193)
- `2026-05-13T16:28:39Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/segmented_radix_sort/keys.cu`:21; signals: benchmark; excerpt: "Moved this to a different PR" (https://github.com/NVIDIA/cccl/pull/7949#discussion_r3235887738)
