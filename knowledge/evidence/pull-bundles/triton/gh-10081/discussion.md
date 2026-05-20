# PR Discussion Digest

- Source PR: [triton-lang/triton#10081](https://github.com/triton-lang/triton/pull/10081)
- Source page: `sources/prs/triton/PR-10081.md`
- Evidence bundle: `evidence/pull-bundles/triton/gh-10081`
- Generated at: `2026-05-20T15:33:20.031337+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-20T13:24:54Z`
- Merged: `2026-04-30T00:36:46Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 11 (approved=1, changes_requested=1, commented=9)
- Inline review comments: 16
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=3, outdated=6
- Human participants with discussion text: antiagainst, lijinpei-amd, zhanglx13
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-28T02:12:04Z` `CHANGES_REQUESTED` by `zhanglx13` - Thanks @lijinpei-amd This is much cleaner and reusing the existing infra. The only thing is the test size. (https://github.com/triton-lang/triton/pull/10081#pullrequestreview-4185335210)
- `2026-04-28T14:21:18Z` `COMMENTED` by `lijinpei-amd` (https://github.com/triton-lang/triton/pull/10081#pullrequestreview-4189626742)
- `2026-04-28T14:21:26Z` `COMMENTED` by `lijinpei-amd` (https://github.com/triton-lang/triton/pull/10081#pullrequestreview-4189628006)
- `2026-04-28T14:21:32Z` `COMMENTED` by `lijinpei-amd` (https://github.com/triton-lang/triton/pull/10081#pullrequestreview-4189628875)
- `2026-04-28T14:21:39Z` `COMMENTED` by `lijinpei-amd` (https://github.com/triton-lang/triton/pull/10081#pullrequestreview-4189629999)
- `2026-04-28T22:48:05Z` `COMMENTED` by `antiagainst` (https://github.com/triton-lang/triton/pull/10081#pullrequestreview-4192928764)
- `2026-04-29T02:21:04Z` `COMMENTED` by `lijinpei-amd` (https://github.com/triton-lang/triton/pull/10081#pullrequestreview-4193682024)
- `2026-04-29T02:21:30Z` `COMMENTED` by `lijinpei-amd` (https://github.com/triton-lang/triton/pull/10081#pullrequestreview-4193682883)
- `2026-04-29T02:30:51Z` `COMMENTED` by `lijinpei-amd` (https://github.com/triton-lang/triton/pull/10081#pullrequestreview-4193702168)
- `2026-04-29T03:04:06Z` `COMMENTED` by `antiagainst` (https://github.com/triton-lang/triton/pull/10081#pullrequestreview-4193798224)
- `2026-04-30T00:14:19Z` `APPROVED` by `zhanglx13` (https://github.com/triton-lang/triton/pull/10081#pullrequestreview-4201595405)

## Inline Comment Hotspots

- `test/TritonGPU/amd/amd-block-pingpong-asyncmark-multi-token.mlir`: 6 inline comment(s)
- `third_party/amd/lib/TritonAMDGPUTransforms/Pipeline.cpp`: 5 inline comment(s)
- `test/TritonGPU/amd/amd-update-async-wait-count-asyncmark.mlir`: 4 inline comment(s)
- `third_party/amd/lib/TritonAMDGPUTransforms/BlockPingpong.cpp`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-29T02:30:51Z` `inline` by `lijinpei-amd` `third_party/amd/lib/TritonAMDGPUTransforms/Pipeline.cpp`:128; signals: hang, pipeline, triton; excerpt: "[getAMDArch]( get arch from module attribute, which is added by [convert-triton-to-tritongpu pass]( which get it from [options.arch]( change amdgpu specific pass option name from ..." (https://github.com/triton-lang/triton/pull/10081#discussion_r3158283088)
- `2026-04-28T02:07:06Z` `inline` by `zhanglx13` `test/TritonGPU/amd/amd-block-pingpong-asyncmark-multi-token.mlir`:33; signals: block, triton; excerpt: "These are not used. Better to remove them." (https://github.com/triton-lang/triton/pull/10081#discussion_r3151160614)
- `2026-04-28T02:08:51Z` `inline` by `zhanglx13` `test/TritonGPU/amd/amd-block-pingpong-asyncmark-multi-token.mlir`:40; signals: block, triton; excerpt: "arg13 and 16 are not used either." (https://github.com/triton-lang/triton/pull/10081#discussion_r3151165299)
- `2026-04-28T02:08:54Z` `inline` by `zhanglx13` `test/TritonGPU/amd/amd-block-pingpong-asyncmark-multi-token.mlir`:46; signals: block, triton; excerpt: "Do we really need store? At lease we can remove the mask." (https://github.com/triton-lang/triton/pull/10081#discussion_r3151165488)
- `2026-04-28T14:21:18Z` `inline` by `lijinpei-amd` `test/TritonGPU/amd/amd-block-pingpong-asyncmark-multi-token.mlir`:33; signals: block, triton; excerpt: "done" (https://github.com/triton-lang/triton/pull/10081#discussion_r3154839390)
- `2026-04-28T14:21:26Z` `inline` by `lijinpei-amd` `test/TritonGPU/amd/amd-block-pingpong-asyncmark-multi-token.mlir`:40; signals: block, triton; excerpt: "done" (https://github.com/triton-lang/triton/pull/10081#discussion_r3154840465)
- `2026-04-28T14:21:32Z` `inline` by `lijinpei-amd` `test/TritonGPU/amd/amd-block-pingpong-asyncmark-multi-token.mlir`:46; signals: block, triton; excerpt: "done" (https://github.com/triton-lang/triton/pull/10081#discussion_r3154841179)
- `2026-04-28T22:33:16Z` `inline` by `antiagainst` `third_party/amd/lib/TritonAMDGPUTransforms/Pipeline.cpp`:2; signals: pipeline, triton; excerpt: "We can drop this explicit comment--too excessive just for an lint skip." (https://github.com/triton-lang/triton/pull/10081#discussion_r3157610000)
- `2026-04-28T22:33:43Z` `inline` by `antiagainst` `third_party/amd/lib/TritonAMDGPUTransforms/Pipeline.cpp`:128; signals: pipeline, triton; excerpt: "This needs to be updated after" (https://github.com/triton-lang/triton/pull/10081#discussion_r3157611920)
- `2026-04-28T22:44:34Z` `inline` by `antiagainst` `third_party/amd/lib/TritonAMDGPUTransforms/BlockPingpong.cpp`:862; signals: block, triton; excerpt: "@jungpark-mlir: I forgot what the issue was. Are we able to fix right now or still problematic?" (https://github.com/triton-lang/triton/pull/10081#discussion_r3157656997)
- `2026-04-29T02:21:04Z` `inline` by `lijinpei-amd` `third_party/amd/lib/TritonAMDGPUTransforms/Pipeline.cpp`:2; signals: pipeline, triton; excerpt: "done" (https://github.com/triton-lang/triton/pull/10081#discussion_r3158261671)
- `2026-04-29T03:04:06Z` `inline` by `antiagainst` `third_party/amd/lib/TritonAMDGPUTransforms/Pipeline.cpp`:128; signals: pipeline, triton; excerpt: "Sorry, I meant actually. Forgot that's not landed yet. Never mind I can clean it up later." (https://github.com/triton-lang/triton/pull/10081#discussion_r3158365555)
