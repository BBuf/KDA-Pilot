# PR Discussion Digest

- Source PR: [triton-lang/triton#10056](https://github.com/triton-lang/triton/pull/10056)
- Source page: `sources/prs/triton/PR-10056.md`
- Evidence bundle: `evidence/pull-bundles/triton/gh-10056`
- Generated at: `2026-05-20T15:33:20.020786+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-16T17:52:03Z`
- Merged: `2026-05-13T16:42:56Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 40 (approved=2, changes_requested=2, commented=36)
- Inline review comments: 60
- Review threads observed: 29
- Resolved/outdated thread markers: resolved=15, outdated=24
- Human participants with discussion text: ThomasRaoux, antiagainst, jungpark-mlir, lezcano, peterbell10
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-16T17:55:33Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4123259986)
- `2026-04-16T18:32:03Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4123483060)
- `2026-04-16T19:00:33Z` `CHANGES_REQUESTED` by `antiagainst` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4123635885)
- `2026-04-16T21:06:39Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4124449203)
- `2026-04-17T01:37:23Z` `COMMENTED` by `antiagainst` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4125547547)
- `2026-04-17T02:46:25Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4125736034)
- `2026-04-22T04:01:23Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4151944792)
- `2026-04-24T15:29:32Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4171564876)
- `2026-05-01T12:31:47Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4211120921)
- `2026-05-01T16:00:13Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4211982071)
- `2026-05-01T17:31:56Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4212424141)
- `2026-05-02T20:34:18Z` `CHANGES_REQUESTED` by `antiagainst` - Much nicer; thanks Jungwook for revising the design and impl! (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4215361635)
- `2026-05-03T19:12:45Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4216715906)
- `2026-05-03T19:14:13Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4216717145)
- `2026-05-03T19:14:29Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4216717411)
- `2026-05-03T19:27:11Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4216729031)
- `2026-05-04T01:56:54Z` `APPROVED` by `antiagainst` - Thanks @jungpark-mlir for iterating on it! This looks good to me now. Please wait for Thomas to take ... (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4217147344)
- `2026-05-06T00:25:46Z` `COMMENTED` by `ThomasRaoux` - That mostly looks good to me but I think it would be great if we could simplify a ... (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4232416905)
- `2026-05-06T14:32:29Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4236993303)
- `2026-05-06T19:15:13Z` `COMMENTED` by `peterbell10` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4238782458)
- `2026-05-06T19:16:18Z` `COMMENTED` by `peterbell10` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4238789219)
- `2026-05-06T19:37:43Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4238939118)
- `2026-05-06T19:55:57Z` `COMMENTED` by `peterbell10` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4239063261)
- `2026-05-06T20:02:52Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10056#pullrequestreview-4239113096)
- ... 16 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `third_party/amd/python/examples/gluon/f16_gemm_warp_pipeline_gfx1250.py`: 24 inline comment(s)
- `third_party/amd/lib/Dialect/TritonAMDGPU/IR/Dialect.cpp`: 10 inline comment(s)
- `third_party/amd/python/test/test_tdm_copy.py`: 7 inline comment(s)
- `python/triton/experimental/gluon/language/amd/gfx1250/tdm.py`: 6 inline comment(s)
- `third_party/amd/lib/TritonAMDGPUToLLVM/TDMUtility.cpp`: 6 inline comment(s)
- `third_party/amd/include/Dialect/TritonAMDGPU/IR/TritonAMDGPUOps.td`: 4 inline comment(s)
- `include/triton/Dialect/TritonGPU/IR/LinearLayoutConversions.h`: 2 inline comment(s)
- `lib/Dialect/TritonGPU/IR/LinearLayoutConversions.cpp`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-01T12:31:47Z` `inline` by `jungpark-mlir` `third_party/amd/lib/TritonAMDGPUToLLVM/TDMUtility.cpp`:542; signals: block, hang, kernel, perf, performance, tile, triton, warp; excerpt: "@ThomasRaoux I missed this comment actually, this is very important design point we need to discuss. The goal is to copy the full block ..." (https://github.com/triton-lang/triton/pull/10056#discussion_r3173165417)
- `2026-05-07T11:14:42Z` `inline` by `jungpark-mlir` `third_party/amd/python/examples/gluon/f16_gemm_warp_pipeline_gfx1250.py`:371; signals: block, gemm, hang, layout, memory, pipeline, shared memory, tile; excerpt: "I'm also curious if only one warp group is able to handle the load, then how are load and async copy handled? Do they ..." (https://github.com/triton-lang/triton/pull/10056#discussion_r3200988284)
- `2026-05-01T17:31:56Z` `inline` by `jungpark-mlir` `third_party/amd/lib/TritonAMDGPUToLLVM/TDMUtility.cpp`:542; signals: block, hang, perf, performance, tile, triton, warp; excerpt: "Yes, if I understood correctly. But to be precise, the logical TDM copy size is not reduced. What changed is the per-warp tile encoded ..." (https://github.com/triton-lang/triton/pull/10056#discussion_r3174346912)
- `2026-05-06T22:15:50Z` `inline` by `peterbell10` `third_party/amd/python/examples/gluon/f16_gemm_warp_pipeline_gfx1250.py`:371; signals: compile, gemm, layout, perf, performance, pipeline, warp; excerpt: "I'm leaning towards this shouldn't be exposed in gluon. If the compiler is able to merge the loads of A and B, then it ..." (https://github.com/triton-lang/triton/pull/10056#discussion_r3197841092)
- `2026-04-16T18:53:48Z` `inline` by `antiagainst` `third_party/amd/python/examples/gluon/f16_gemm_warp_pipeline_gfx1250.py`:104; signals: block, cute, gemm, layout, pipeline, warp; excerpt: "In my mental model this should not break the block programming--all warps are still collectively programmed and they go through uniform control flow paths. ..." (https://github.com/triton-lang/triton/pull/10056#discussion_r3095636250)
- `2026-04-16T21:06:38Z` `inline` by `ThomasRaoux` `third_party/amd/python/examples/gluon/f16_gemm_warp_pipeline_gfx1250.py`:104; signals: gemm, layout, memory, pipeline, shared memory, warp; excerpt: "ok, maybe I need to spend more time understand this. The TDM copy from global to shared memory so there shouldn't be any warp ..." (https://github.com/triton-lang/triton/pull/10056#discussion_r3096377871)
- `2026-04-22T03:50:39Z` `inline` by `ThomasRaoux` `python/triton/experimental/gluon/language/amd/gfx1250/tdm.py`:180; signals: hang, layout, perf, performance, triton, warp; excerpt: "I think we need a better description. Few things I think could help: - Make it clear it is a performance hint and doesn't ..." (https://github.com/triton-lang/triton/pull/10056#discussion_r3121458032)
- `2026-05-06T21:01:31Z` `inline` by `jungpark-mlir` `third_party/amd/python/examples/gluon/f16_gemm_warp_pipeline_gfx1250.py`:371; signals: compile, gemm, perf, performance, pipeline, warp; excerpt: "The actual HW instruction for a TDM copy uses a per-warp descriptor. Today we partition the tensor evenly across all warps in the workgroup, ..." (https://github.com/triton-lang/triton/pull/10056#discussion_r3197471502)
- `2026-05-06T22:39:55Z` `inline` by `jungpark-mlir` `third_party/amd/python/examples/gluon/f16_gemm_warp_pipeline_gfx1250.py`:371; signals: compile, gemm, layout, perf, pipeline, warp; excerpt: "What this PR does is 1) user to define warp mapping by predication 2) compiler to get the warp number actively participating the copy ..." (https://github.com/triton-lang/triton/pull/10056#discussion_r3197945627)
- `2026-05-07T15:39:50Z` `inline` by `peterbell10` `third_party/amd/python/examples/gluon/f16_gemm_warp_pipeline_gfx1250.py`:371; signals: gemm, kernel, latency, layout, pipeline, warp; excerpt: "Sorry, I meant async copy.global load to shared so a non-tdm async copy. In that case you have to pass a tensor of pointers, ..." (https://github.com/triton-lang/triton/pull/10056#discussion_r3202736828)
- `2026-04-23T11:29:01Z` `issue` by `jungpark-mlir`; signals: block, hang, kernel, layout, tile, warp; excerpt: "Can we just decide on what warps will participate rather than representing this as such a fine grain control? If we instead just add ..." (https://github.com/triton-lang/triton/pull/10056#issuecomment-4303994479)
- `2026-04-23T16:00:44Z` `issue` by `ThomasRaoux`; signals: block, hang, kernel, layout, tile, warp; excerpt: "Can we just decide on what warps will participate rather than representing this as such a fine grain control? If we instead just add ..." (https://github.com/triton-lang/triton/pull/10056#issuecomment-4305923562)
