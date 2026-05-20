# PR Discussion Digest

- Source PR: [sgl-project/sglang#10180](https://github.com/sgl-project/sglang/pull/10180)
- Source page: `sources/prs/sglang/PR-10180.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-10180`
- Generated at: `2026-05-20T15:27:16.562006+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-08T21:17:31Z`
- Merged: `2025-09-12T10:20:30Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 14 (approved=1, commented=13)
- Inline review comments: 14
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=9
- Human participants with discussion text: Fridge003, elfiegg, fzyzcjy, kushanam, wenscarl, yzh119, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-09T00:16:06Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3198576289)
- `2025-09-09T19:03:30Z` `COMMENTED` by `wenscarl` - Work around cutlass kernel for chunked prefix (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3202897656)
- `2025-09-09T19:44:14Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3203041296)
- `2025-09-09T23:21:09Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3203719739)
- `2025-09-10T03:10:41Z` `APPROVED` by `Fridge003` - LGTM (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3204196147)
- `2025-09-10T03:28:43Z` `COMMENTED` by `yzh119` (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3204273744)
- `2025-09-10T20:59:25Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3207812949)
- `2025-09-10T21:03:33Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3207822649)
- `2025-09-10T21:33:50Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3207914542)
- `2025-09-10T22:26:19Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3208016692)
- `2025-09-10T23:04:15Z` `COMMENTED` by `elfiegg` - Thanks for the quick fix! (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3208078394)
- `2025-09-10T23:24:30Z` `COMMENTED` by `elfiegg` (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3208156107)
- `2025-09-10T23:40:30Z` `COMMENTED` by `elfiegg` (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3208182186)
- `2025-09-11T18:41:06Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3212977801)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 9 inline comment(s)
- `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-09-10T21:03:33Z` `inline` by `wenscarl` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:235; signals: accuracy, attention, cache, flashinfer, kernel, mla; excerpt: "@zhyncs it's not head dim vo though I missed that in the reproducer. The cause is still from kernel for certain shape. It's not ..." (https://github.com/sgl-project/sglang/pull/10180#discussion_r2337908837)
- `2025-09-09T21:49:32Z` `issue` by `Fridge003`; signals: accuracy, flashinfer, fp4, hang, kernel, nvfp4; excerpt: "@wenscarl Will the accuracy of dpsk-r1 nvfp4 be back to normal after changing flashinfer kernel to fa2 version?" (https://github.com/sgl-project/sglang/pull/10180#issuecomment-3272394794)
- `2025-09-09T23:12:51Z` `issue` by `wenscarl`; signals: accuracy, flashinfer, fp4, hang, kernel, nvfp4; excerpt: "@wenscarl Will the accuracy of dpsk-r1 nvfp4 be back to normal after changing flashinfer kernel to fa2 version? Yes. It's in the description." (https://github.com/sgl-project/sglang/pull/10180#issuecomment-3272571009)
- `2025-09-09T19:44:14Z` `inline` by `zhyncs` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:235; signals: attention, flashinfer, mla; excerpt: "hi @yzh119 can you help take a look" (https://github.com/sgl-project/sglang/pull/10180#discussion_r2334603859)
- `2025-09-09T23:21:09Z` `inline` by `wenscarl` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:235; signals: attention, flashinfer, mla; excerpt: "to track." (https://github.com/sgl-project/sglang/pull/10180#discussion_r2335065621)
- `2025-09-10T03:28:42Z` `inline` by `yzh119` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:235; signals: attention, flashinfer, mla; excerpt: "Adding head dim vo field in plan function should address the issue." (https://github.com/sgl-project/sglang/pull/10180#discussion_r2335447878)
- `2025-09-10T20:59:25Z` `inline` by `zhyncs` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:235; signals: attention, flashinfer, mla; excerpt: "@wenscarl can you try this" (https://github.com/sgl-project/sglang/pull/10180#discussion_r2337901816)
- `2025-09-09T19:03:30Z` `review` `COMMENTED` by `wenscarl`; signals: cutlass, kernel; excerpt: "Work around cutlass kernel for chunked prefix" (https://github.com/sgl-project/sglang/pull/10180#pullrequestreview-3202897656)
- `2025-09-10T16:42:04Z` `issue` by `elfiegg`; signals: cutlass, fp8, perf; excerpt: "can we route the logic based on quantization temporarily ? FP8 model works well with cutlass backend, and using FA2 the perf would drop ..." (https://github.com/sgl-project/sglang/pull/10180#issuecomment-3275716789)
- `2025-09-10T23:24:30Z` `inline` by `elfiegg` `python/sglang/srt/models/deepseek_v2.py`:1095; signals: fp4, kernel; excerpt: "We might not need to differentiate fp4 quant now as original mode is not None original mode.is decode() is triggering problematic kernels" (https://github.com/sgl-project/sglang/pull/10180#discussion_r2338148441)
- `2025-09-10T23:40:18Z` `inline` by `elfiegg` `python/sglang/srt/models/deepseek_v2.py`:1090; signals: kernel, mla; excerpt: "You should probably directly do instead of MHA when hit this branch. You want to call MLA kernel in this case which doesn't involve ..." (https://github.com/sgl-project/sglang/pull/10180#discussion_r2338168223)
- `2025-09-11T17:36:41Z` `inline` by `Fridge003` `python/sglang/srt/models/deepseek_v2.py`:1096; signals: mla; excerpt: "we can directly return dispatch mla subtype() here and remove the skip chunked mha variable" (https://github.com/sgl-project/sglang/pull/10180#discussion_r2341887020)
