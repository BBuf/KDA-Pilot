# PR Discussion Digest

- Source PR: [sgl-project/sglang#19794](https://github.com/sgl-project/sglang/pull/19794)
- Source page: `sources/prs/sglang/PR-19794.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19794`
- Generated at: `2026-05-20T15:28:55.659998+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-03T17:58:47Z`
- Merged: `2026-03-20T10:25:13Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 18 (approved=3, commented=15)
- Inline review comments: 19
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=3, outdated=5
- Human participants with discussion text: BBuf, DarkSharpness, HydraQYH, xingsy97
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-04T10:14:20Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3888444481)
- `2026-03-04T13:49:54Z` `COMMENTED` by `xingsy97` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3889557290)
- `2026-03-04T13:50:06Z` `COMMENTED` by `xingsy97` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3889558352)
- `2026-03-05T12:03:13Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3895988427)
- `2026-03-05T14:28:55Z` `COMMENTED` by `xingsy97` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3897054621)
- `2026-03-05T16:06:57Z` `APPROVED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3897764617)
- `2026-03-05T16:35:09Z` `COMMENTED` by `xingsy97` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3897975657)
- `2026-03-05T16:38:12Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3897989177)
- `2026-03-05T17:34:36Z` `COMMENTED` by `xingsy97` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3898424529)
- `2026-03-05T18:15:20Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3898678351)
- `2026-03-06T04:33:58Z` `COMMENTED` by `xingsy97` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3901228473)
- `2026-03-06T11:37:36Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3903209053)
- `2026-03-07T03:00:46Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3907113301)
- `2026-03-07T04:00:39Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3907269886)
- `2026-03-07T12:40:32Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3908711459)
- `2026-03-07T17:34:15Z` `COMMENTED` by `xingsy97` (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3909198990)
- `2026-03-18T12:11:54Z` `APPROVED` by `DarkSharpness` - LGTM. cc @BBuf @HydraQYH (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3967370720)
- `2026-03-20T10:25:03Z` `APPROVED` by `BBuf` - LGTM (https://github.com/sgl-project/sglang/pull/19794#pullrequestreview-3980682799)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/csrc/elementwise/qknorm_across_heads.cuh`: 9 inline comment(s)
- `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`: 6 inline comment(s)
- `python/sglang/jit_kernel/csrc/elementwise/fused_add_rmsnorm.cuh`: 2 inline comment(s)
- `python/sglang/jit_kernel/include/sgl_kernel/vec.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-05T17:34:36Z` `inline` by `xingsy97` `python/sglang/jit_kernel/csrc/elementwise/qknorm_across_heads.cuh`:61; signals: blackwell, block, compile, cuda, hang, kernel, pipeline; excerpt: "found a blocker for such change 1. SGL ARCH IS BLACKWELL PLUS relies on CUDA ARCH , which is only defined on the device ..." (https://github.com/sgl-project/sglang/pull/19794#discussion_r2891343880)
- `2026-03-05T16:06:51Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/csrc/elementwise/qknorm_across_heads.cuh`:61; signals: compile, hang, hopper, kernel; excerpt: "Given that we are testing the architecture from compile-time macros, we should remove this line and change the kernel dispatch logic based on the ..." (https://github.com/sgl-project/sglang/pull/19794#discussion_r2890964656)
- `2026-03-07T04:00:39Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/csrc/elementwise/qknorm_across_heads.cuh`:61; signals: blackwell, compile, cuda, kernel; excerpt: "Why we not do like this: That's because "SGL ARCH IS BLACKWELL PLUS relies on CUDA ARCH , which is only defined on the ..." (https://github.com/sgl-project/sglang/pull/19794#discussion_r2898897251)
- `2026-03-04T10:13:09Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/csrc/elementwise/fused_add_rmsnorm.cuh`:57; signals: blackwell, kernel, vector; excerpt: "If we've disabled invalid 256 bit load/store, then we should dispatch the kernel template based on the macro SGL ARCH IS BLACKWELL PLUS or ..." (https://github.com/sgl-project/sglang/pull/19794#discussion_r2882936269)
- `2026-03-05T16:02:36Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`:80; signals: blackwell, hopper, kernel; excerpt: "SGL ARCH IS HOPPER PLUS / SGL ARCH IS BLACKWELL PLUS . Can we improve the naming? Maybe we can refer to other open-source ..." (https://github.com/sgl-project/sglang/pull/19794#discussion_r2890938593)
- `2026-03-05T16:35:09Z` `inline` by `xingsy97` `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`:80; signals: blackwell, hopper, kernel; excerpt: "What about SGL ARCH HOPPER OR GREATER / SGL ARCH BLACKWELL OR GREATER, inspired by .NET macro naming. See ,it looks pretty clear" (https://github.com/sgl-project/sglang/pull/19794#discussion_r2891115352)
- `2026-03-05T16:38:12Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`:80; signals: hopper, kernel; excerpt: "I'm not sure here (though SGL ARCH HOPPER OR GREATER do look better to me). cc @HydraQYH @BBuf if you have any idea" (https://github.com/sgl-project/sglang/pull/19794#discussion_r2891126232)
- `2026-03-05T18:15:19Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/csrc/elementwise/qknorm_across_heads.cuh`:61; signals: compile, kernel; excerpt: "Actually, in Python-side, we can get the architecture information from torch. We may add some macros which indicate the target architecture (which works for ..." (https://github.com/sgl-project/sglang/pull/19794#discussion_r2891494844)
- `2026-03-05T11:58:50Z` `inline` by `HydraQYH` `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`:80; signals: cuda, kernel; excerpt: "We also need to check the CUDA version. As far as I know, CUDA = 12.9 is valid." (https://github.com/sgl-project/sglang/pull/19794#discussion_r2889546753)
- `2026-03-05T14:28:55Z` `inline` by `xingsy97` `python/sglang/jit_kernel/include/sgl_kernel/utils.cuh`:80; signals: cuda, kernel; excerpt: "added check for CUDA version" (https://github.com/sgl-project/sglang/pull/19794#discussion_r2890339794)
- `2026-03-18T12:02:48Z` `issue` by `xingsy97`; signals: blackwell, kernel; excerpt: "Hi @DarkSharpness, I rewrote this PR, rebased on 20103. Added inline constexpr kMaxVecBytes (derived from SGL ARCH BLACKWELL OR GREATER, consistent in host/device). Kernel ..." (https://github.com/sgl-project/sglang/pull/19794#issuecomment-4081988429)
- `2026-03-06T04:33:58Z` `inline` by `xingsy97` `python/sglang/jit_kernel/csrc/elementwise/qknorm_across_heads.cuh`:61; signals: kernel; excerpt: "Makes sense. I'll add the default architecture macro in load jit() and update the host-side dispatch in a separate PR, since it will have ..." (https://github.com/sgl-project/sglang/pull/19794#discussion_r2893765821)
