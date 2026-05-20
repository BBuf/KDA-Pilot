# PR Discussion Digest

- Source PR: [NVIDIA/cccl#7565](https://github.com/NVIDIA/cccl/pull/7565)
- Source page: `sources/prs/cccl-cub/PR-7565.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-7565`
- Generated at: `2026-05-20T15:20:12.492399+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-08T05:44:48Z`
- Merged: `2026-03-24T06:23:30Z`

## Discussion Counts

- Issue comments: 34
- Review submissions: 22 (approved=1, commented=21)
- Inline review comments: 36
- Review threads observed: 27
- Resolved/outdated thread markers: resolved=25, outdated=20
- Human participants with discussion text: alliepiper, bernhardmgruber, griwes
- Automation comments/reviews omitted from high-signal summary: 16
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-09T11:05:18Z` `COMMENTED` by `bernhardmgruber` - This looks really good already! Great work! (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3772035686)
- `2026-02-09T23:53:38Z` `COMMENTED` by `griwes` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3776022805)
- `2026-02-09T23:55:51Z` `COMMENTED` by `griwes` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3776027863)
- `2026-02-19T02:01:05Z` `COMMENTED` by `griwes` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3823097957)
- `2026-02-20T16:20:16Z` `COMMENTED` by `alliepiper` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3832929997)
- `2026-02-22T19:06:22Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3838479480)
- `2026-02-22T19:18:06Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3838489910)
- `2026-02-25T12:42:59Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3854024112)
- `2026-02-25T15:49:23Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3854217868)
- `2026-02-25T15:52:00Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3855162334)
- `2026-02-25T15:52:50Z` `COMMENTED` by `bernhardmgruber` - I see a lot of changes to the setup of the shared memory resources, which worry me. I ... (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3855167045)
- `2026-02-25T15:54:40Z` `COMMENTED` by `bernhardmgruber` - @griwes please try to refactor out anything that is not related to the new tuning API and ship ... (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3855177012)
- `2026-02-25T16:30:11Z` `COMMENTED` by `griwes` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3855383497)
- `2026-02-25T16:31:09Z` `COMMENTED` by `griwes` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3855388925)
- `2026-02-25T16:35:44Z` `COMMENTED` by `griwes` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3855414624)
- `2026-03-03T13:17:23Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3882202558)
- `2026-03-03T13:22:42Z` `COMMENTED` by `bernhardmgruber` - I still have to re-review the dispatch logic and the changes around the kernel, especially the refactoring to ... (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3882561501)
- `2026-03-04T22:53:41Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3889813652)
- `2026-03-13T17:33:37Z` `COMMENTED` by `griwes` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3945825106)
- `2026-03-23T14:24:21Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3992150423)
- `2026-03-23T14:57:19Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3992397892)
- `2026-03-23T19:18:58Z` `APPROVED` by `bernhardmgruber` - I have collected a few more pieces of refactorings, but I think those should go to a separate ... (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3994082355)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/dispatch_scan.cuh`: 7 inline comment(s)
- `cub/benchmarks/bench/scan/policy_selector.h`: 5 inline comment(s)
- `cub/cub/device/dispatch/kernels/kernel_scan.cuh`: 5 inline comment(s)
- `cub/cub/device/dispatch/kernels/kernel_scan_warpspeed.cuh`: 5 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_scan.cuh`: 4 inline comment(s)
- `cub/cub/device/dispatch/kernels/scan_warpspeed_policy.cuh`: 4 inline comment(s)
- `cub/cub/device/device_scan.cuh`: 2 inline comment(s)
- `c/parallel/src/scan.cu`: 1 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_radix_sort.cuh`: 1 inline comment(s)
- `ci/matrix.yaml`: 1 inline comment(s)
- `cub/test/catch2_test_device_scan_env.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-25T15:52:50Z` `review` `COMMENTED` by `bernhardmgruber`; signals: hang, kernel, memory, shared memory; excerpt: "I see a lot of changes to the setup of the shared memory resources, which worry me. I am almost certain those will introduce ..." (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3855167045)
- `2026-03-03T13:22:42Z` `review` `COMMENTED` by `bernhardmgruber`; signals: benchmark, hang, kernel; excerpt: "I still have to re-review the dispatch logic and the changes around the kernel, especially the refactoring to compute whether we can fit a ..." (https://github.com/NVIDIA/cccl/pull/7565#pullrequestreview-3882561501)
- `2026-02-25T16:28:09Z` `issue` by `griwes`; signals: hang, kernel, memory, shared memory; excerpt: "The setup of the resources is the same from the perspective of the kernel. The only thing that changes there is the ability to ..." (https://github.com/NVIDIA/cccl/pull/7565#issuecomment-3960472475)
- `2026-03-04T14:40:11Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/scan_warpspeed_policy.cuh`:22; signals: hang, kernel, warp; excerpt: "Remark: we should probably introduce an algorithm enum like in DeviceTransform before all the policies go public. No changes need for now." (https://github.com/NVIDIA/cccl/pull/7565#discussion_r2884171991)
- `2026-03-16T21:56:16Z` `issue` by `griwes`; signals: compile, hang, kernel; excerpt: "There is SASS changes. Here's a random assortment of kernels compared: I believe that there's a whole bunch of codegen artifacts here + some ..." (https://github.com/NVIDIA/cccl/pull/7565#issuecomment-4070856249)
- `2026-02-19T02:00:55Z` `inline` by `griwes` `cub/cub/device/dispatch/kernels/scan_warpspeed_policy.cuh`; signals: kernel, warp; excerpt: "Note: I need this struct in both kernel scan warpspeed.cuh and tuning scan.cuh, and cross-including them seems... bad. But putting it here is also ..." (https://github.com/NVIDIA/cccl/pull/7565#discussion_r2825293287)
- `2026-02-22T19:17:41Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_scan.cuh`:223; signals: kernel, warp; excerpt: "Suggestion: Since we just merged the warpspeed implementation, it's not on any release branch yet. We could entirely remove it from the legacy policy ..." (https://github.com/NVIDIA/cccl/pull/7565#discussion_r2838396645)
- `2026-02-25T14:11:58Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/scan_warpspeed_policy.cuh`; signals: kernel, warp; excerpt: "Just leave it here. It's fine. We should do a larger reorganization of files with CCCL 4.0 and move a lot more into a ..." (https://github.com/NVIDIA/cccl/pull/7565#discussion_r2853286765)
- `2026-02-25T15:52:00Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_scan_warpspeed.cuh`:899; signals: kernel, warp; excerpt: "Remark: This seems like a massive duplication of the logic allocResources does. I am extremely worried this will render the codebase brittle and unmaintainable. ..." (https://github.com/NVIDIA/cccl/pull/7565#discussion_r2853868668)
- `2026-02-25T16:30:10Z` `inline` by `griwes` `cub/cub/device/dispatch/kernels/kernel_scan_warpspeed.cuh`:899; signals: kernel, warp; excerpt: "This is, in fact, a reduction of the duplication. The only way to not have the parts that are duplicated duplicated is to entirely ..." (https://github.com/NVIDIA/cccl/pull/7565#discussion_r2854075208)
- `2026-02-25T16:31:08Z` `inline` by `griwes` `cub/cub/device/dispatch/kernels/kernel_scan_warpspeed.cuh`:899; signals: kernel, warp; excerpt: "The reason it is like this is that the current code is all written in terms of types and their statically known sizes. We ..." (https://github.com/NVIDIA/cccl/pull/7565#discussion_r2854080335)
- `2026-03-04T22:44:55Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_scan.cuh`:511; signals: compile, warp; excerpt: "Important: Please retain the compile-time check when possible. It helps a lot with development if we can turn on warpspeed unconditionally and just compile ..." (https://github.com/NVIDIA/cccl/pull/7565#discussion_r2886534378)
