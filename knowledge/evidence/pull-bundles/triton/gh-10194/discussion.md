# PR Discussion Digest

- Source PR: [triton-lang/triton#10194](https://github.com/triton-lang/triton/pull/10194)
- Source page: `sources/prs/triton/PR-10194.md`
- Evidence bundle: `evidence/pull-bundles/triton/gh-10194`
- Generated at: `2026-05-20T15:33:26.055636+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-01T15:08:24Z`
- Merged: `2026-05-05T21:02:15Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 10 (approved=2, commented=8)
- Inline review comments: 10
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: antiagainst, jerryyin, jungpark-mlir
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-01T17:53:59Z` `COMMENTED` by `jungpark-mlir` - Set 0 looks correct to me but I'm not sure what has been changed in the pipeliner, which ... (https://github.com/triton-lang/triton/pull/10194#pullrequestreview-4212485872)
- `2026-05-01T17:54:35Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10194#pullrequestreview-4212539519)
- `2026-05-01T19:17:03Z` `COMMENTED` by `jerryyin` (https://github.com/triton-lang/triton/pull/10194#pullrequestreview-4212935820)
- `2026-05-01T21:23:29Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10194#pullrequestreview-4213490323)
- `2026-05-01T21:50:36Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10194#pullrequestreview-4213565354)
- `2026-05-04T14:29:30Z` `COMMENTED` by `jerryyin` (https://github.com/triton-lang/triton/pull/10194#pullrequestreview-4220779302)
- `2026-05-05T11:17:16Z` `COMMENTED` by `jungpark-mlir` (https://github.com/triton-lang/triton/pull/10194#pullrequestreview-4227452080)
- `2026-05-05T12:19:55Z` `APPROVED` by `jungpark-mlir` - LGTM! (https://github.com/triton-lang/triton/pull/10194#pullrequestreview-4227847685)
- `2026-05-05T12:21:38Z` `COMMENTED` by `jerryyin` (https://github.com/triton-lang/triton/pull/10194#pullrequestreview-4227861121)
- `2026-05-05T21:01:55Z` `APPROVED` by `antiagainst` (https://github.com/triton-lang/triton/pull/10194#pullrequestreview-4231581313)

## Inline Comment Hotspots

- `third_party/amd/lib/TritonAMDGPUTransforms/BlockPingpong.cpp`: 10 inline comment(s)

## High-Signal Discussion

- `2026-05-04T14:29:26Z` `inline` by `jerryyin` `third_party/amd/lib/TritonAMDGPUTransforms/BlockPingpong.cpp`:1284; signals: block, kernel, pipeline, triton; excerpt: "Note that asyncmark.wait intrinsic still needs a number (although triton pipeliner abstract it as token based). - Assuming I understand your question correctly. and ..." (https://github.com/triton-lang/triton/pull/10194#discussion_r3182254091)
- `2026-05-01T17:52:56Z` `inline` by `jungpark-mlir` `third_party/amd/lib/TritonAMDGPUTransforms/BlockPingpong.cpp`:1284; signals: block, pipeline, triton; excerpt: "I don't understand why pipeliner needs to set any n at all? It's token based and just can use different token whenever needed?" (https://github.com/triton-lang/triton/pull/10194#discussion_r3174430517)
- `2026-05-01T21:23:29Z` `inline` by `jungpark-mlir` `third_party/amd/lib/TritonAMDGPUTransforms/BlockPingpong.cpp`:877; signals: block, hang, triton; excerpt: "I see, just managed to understand the recent change. But then why do we need to set num=0? just calling updateWaits should fix?" (https://github.com/triton-lang/triton/pull/10194#discussion_r3175277727)
- `2026-05-04T14:14:24Z` `inline` by `jerryyin` `third_party/amd/lib/TritonAMDGPUTransforms/BlockPingpong.cpp`:877; signals: block, correctness, triton; excerpt: "Sorry just saw the comment now. Yes, since updateWaits will update and recalculate the correct num, any num value will work. But I want ..." (https://github.com/triton-lang/triton/pull/10194#discussion_r3182159792)
- `2026-05-05T11:17:16Z` `inline` by `jungpark-mlir` `third_party/amd/lib/TritonAMDGPUTransforms/BlockPingpong.cpp`:877; signals: block, pipeline, triton; excerpt: "I see what you mean. The earlier updateWaits in the pipeliner already consumed the original token based num and current num is newly generated ..." (https://github.com/triton-lang/triton/pull/10194#discussion_r3187980612)
- `2026-05-05T12:21:38Z` `inline` by `jerryyin` `third_party/amd/lib/TritonAMDGPUTransforms/BlockPingpong.cpp`:877; signals: block, pipeline, triton; excerpt: "Comment added. We may want to revisit the whole updateWaits flow later since this will happen every time we reorder async copy and pipeliner ..." (https://github.com/triton-lang/triton/pull/10194#discussion_r3188342861)
- `2026-05-01T17:53:59Z` `review` `COMMENTED` by `jungpark-mlir`; signals: hang, pipeline; excerpt: "Set 0 looks correct to me but I'm not sure what has been changed in the pipeliner, which looks little odd to me." (https://github.com/triton-lang/triton/pull/10194#pullrequestreview-4212485872)
- `2026-05-01T17:54:35Z` `inline` by `jungpark-mlir` `third_party/amd/lib/TritonAMDGPUTransforms/BlockPingpong.cpp`:1284; signals: block, hang, triton; excerpt: "can you please point me the relevant change?" (https://github.com/triton-lang/triton/pull/10194#discussion_r3174436930)
- `2026-05-01T17:45:00Z` `inline` by `jungpark-mlir` `third_party/amd/lib/TritonAMDGPUTransforms/BlockPingpong.cpp`:877; signals: block, triton; excerpt: "This is not waitcnt based amdg.async wait but ttg.async wait, which is still token based. The num allows that many commit group to be ..." (https://github.com/triton-lang/triton/pull/10194#discussion_r3174397643)
- `2026-05-01T19:17:03Z` `inline` by `jerryyin` `third_party/amd/lib/TritonAMDGPUTransforms/BlockPingpong.cpp`:877; signals: block, triton; excerpt: "Agreed 0 is correct here. To be precise on why: num matters on asyncmark targets. TTGAsyncWaitOpConversion (third party/amd/lib/TritonAMDGPUToLLVM/LoadStoreOpToLLVM.cpp:2363-2391) lowers ttg.async wait to rocdl.wait.asyncmark(op.getNum()) and ..." (https://github.com/triton-lang/triton/pull/10194#discussion_r3174780011)
- `2026-05-01T21:50:36Z` `inline` by `jungpark-mlir` `third_party/amd/lib/TritonAMDGPUTransforms/BlockPingpong.cpp`:877; signals: block, triton; excerpt: "I mean still the token is valid and updateWaits should be able to recalculate the correct num based on the token?" (https://github.com/triton-lang/triton/pull/10194#discussion_r3175353029)
