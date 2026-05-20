# PR Discussion Digest

- Source PR: [triton-lang/triton#9883](https://github.com/triton-lang/triton/pull/9883)
- Source page: `sources/prs/triton/PR-9883.md`
- Evidence bundle: `evidence/pull-bundles/triton/gh-9883`
- Generated at: `2026-05-20T15:33:34.104458+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-30T04:58:46Z`
- Merged: `2026-04-14T06:44:17Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 5 (approved=2, changes_requested=2, commented=1)
- Inline review comments: 13
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=11, outdated=11
- Human participants with discussion text: AlexAUT, antiagainst, xuzhao9, zhanglx13
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2026-04-01T08:48:37Z` `CHANGES_REQUESTED` by `AlexAUT` - Probably as a follow up PR but I believe we can remove the alias groups from the new ... (https://github.com/triton-lang/triton/pull/9883#pullrequestreview-4042549781)
- `2026-04-03T03:56:15Z` `CHANGES_REQUESTED` by `antiagainst` - Nice cleanup! In addition to Alex's comments, I have a few nits. (https://github.com/triton-lang/triton/pull/9883#pullrequestreview-4054127815)
- `2026-04-05T20:46:10Z` `COMMENTED` by `zhanglx13` (https://github.com/triton-lang/triton/pull/9883#pullrequestreview-4059824483)
- `2026-04-06T22:39:54Z` `APPROVED` by `antiagainst` (https://github.com/triton-lang/triton/pull/9883#pullrequestreview-4064900978)
- `2026-04-09T08:10:23Z` `APPROVED` by `AlexAUT` - LGTM, one optional super nit pick (https://github.com/triton-lang/triton/pull/9883#pullrequestreview-4080703136)

## Inline Comment Hotspots

- `third_party/amd/lib/TritonAMDGPUToLLVM/LoadStoreOpToLLVM.cpp`: 4 inline comment(s)
- `test/TritonGPU/amd/amd-update-async-wait-count.mlir`: 3 inline comment(s)
- `third_party/amd/lib/TritonAMDGPUToLLVM/BufferOpsEmitter.cpp`: 2 inline comment(s)
- `third_party/amd/lib/TritonAMDGPUTransforms/UpdateAsyncWaitCount.cpp`: 1 inline comment(s)
- `third_party/amd/lib/TritonAMDGPUToLLVM/TargetInfo.h`: 1 inline comment(s)
- `test/Conversion/amd/async_ops_to_llvm.mlir`: 1 inline comment(s)
- `test/TritonGPU/amd/amd-update-async-wait-count-without-token.mlir`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-03T03:55:02Z` `inline` by `antiagainst` `test/TritonGPU/amd/amd-update-async-wait-count.mlir`:629; signals: hang, triton; excerpt: "Similar here--changed accidentally?" (https://github.com/triton-lang/triton/pull/9883#discussion_r3031316248)
- `2026-04-01T08:27:30Z` `inline` by `AlexAUT` `third_party/amd/lib/TritonAMDGPUTransforms/UpdateAsyncWaitCount.cpp`:418; signals: triton; excerpt: "I think it would be better to not rewrite ttg.AsyncWait to amdgpu.AsyncWait for architectures supporting AsyncMarks. The amdgpu variant does represent the number of ..." (https://github.com/triton-lang/triton/pull/9883#discussion_r3020585717)
- `2026-04-01T08:30:28Z` `inline` by `AlexAUT` `third_party/amd/lib/TritonAMDGPUToLLVM/BufferOpsEmitter.cpp`:150; signals: triton; excerpt: "Those instructions are gfx942 and gfx950 specific, do we want to remove the logic and just emit the async variant? Would also make other ..." (https://github.com/triton-lang/triton/pull/9883#discussion_r3020600228)
- `2026-04-01T08:37:36Z` `inline` by `AlexAUT` `third_party/amd/lib/TritonAMDGPUToLLVM/LoadStoreOpToLLVM.cpp`:2371; signals: triton; excerpt: "Just to keep track, but I think this should be the lowering for ttg.async wait and we can remove the asyncCnt clamp since LLVM ..." (https://github.com/triton-lang/triton/pull/9883#discussion_r3020636347)
- `2026-04-01T08:46:12Z` `inline` by `AlexAUT` `test/TritonGPU/amd/amd-update-async-wait-count-without-token.mlir`:28; signals: triton; excerpt: "We have to adjust all tests to use gfx1250 since for GFX950 they no longer test anything since we simply rewrite with the same ..." (https://github.com/triton-lang/triton/pull/9883#discussion_r3020678347)
- `2026-04-01T08:30:54Z` `inline` by `AlexAUT` `third_party/amd/lib/TritonAMDGPUToLLVM/LoadStoreOpToLLVM.cpp`:831; signals: triton; excerpt: "If emitLoadToLds will always return RawPtrBufferLoadAsyncLdsOp we can remove this part." (https://github.com/triton-lang/triton/pull/9883#discussion_r3020602122)
- `2026-04-01T08:47:38Z` `inline` by `AlexAUT` `test/TritonGPU/amd/amd-update-async-wait-count.mlir`:1; signals: triton; excerpt: "Similar to the other file, we should only run those tests on gfx1250." (https://github.com/triton-lang/triton/pull/9883#discussion_r3020685157)
- `2026-04-01T08:48:37Z` `review` `CHANGES_REQUESTED` by `AlexAUT`; signals: general review; excerpt: "Probably as a follow up PR but I believe we can remove the alias groups from the new async intrinsic since they should not ..." (https://github.com/triton-lang/triton/pull/9883#pullrequestreview-4042549781)
- `2026-04-03T03:47:10Z` `inline` by `antiagainst` `test/TritonGPU/amd/amd-update-async-wait-count.mlir`:607; signals: triton; excerpt: "This is not using async mark?" (https://github.com/triton-lang/triton/pull/9883#discussion_r3031302419)
- `2026-04-03T03:53:39Z` `inline` by `antiagainst` `third_party/amd/lib/TritonAMDGPUToLLVM/LoadStoreOpToLLVM.cpp`:1017; signals: triton; excerpt: "requiresAliasInfoForAsyncOps is for CDNA3/CDNA4. Do we still need such alias info given async marks?" (https://github.com/triton-lang/triton/pull/9883#discussion_r3031313743)
- `2026-04-05T20:46:10Z` `inline` by `zhanglx13` `third_party/amd/lib/TritonAMDGPUToLLVM/LoadStoreOpToLLVM.cpp`:1017; signals: triton; excerpt: "we don't. I plan to remove aliasInfo related code in the next PR" (https://github.com/triton-lang/triton/pull/9883#discussion_r3037335641)
- `2026-04-09T08:05:33Z` `inline` by `AlexAUT` `third_party/amd/lib/TritonAMDGPUToLLVM/BufferOpsEmitter.cpp`:125; signals: triton; excerpt: "Nit: We can returnRawPtrBufferLoadAsyncLdsOp which would avoid the cast at the call site." (https://github.com/triton-lang/triton/pull/9883#discussion_r3056361195)
