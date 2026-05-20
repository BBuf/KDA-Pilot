# PR Discussion Digest

- Source PR: [sgl-project/sglang#6641](https://github.com/sgl-project/sglang/pull/6641)
- Source page: `sources/prs/sglang/PR-6641.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6641`
- Generated at: `2026-05-20T15:30:43.506376+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-27T02:09:53Z`
- Merged: `2025-06-25T08:43:33Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 15 (approved=1, changes_requested=3, commented=11)
- Inline review comments: 19
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=3, outdated=7
- Human participants with discussion text: Alcanderian, chunyuan-w, mingfeima, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 7

## Review Decisions

- `2025-06-05T02:29:19Z` `CHANGES_REQUESTED` by `mingfeima` - for the mla decoding integration, skip our early stage parts, directly port forward absorb decode fused cpu (https://github.com/sgl-project/sglang/pull/6641#pullrequestreview-2898673317)
- `2025-06-05T05:49:39Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6641#pullrequestreview-2898952284)
- `2025-06-06T07:42:20Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6641#pullrequestreview-2904072742)
- `2025-06-06T07:42:53Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6641#pullrequestreview-2904073846)
- `2025-06-09T05:40:10Z` `CHANGES_REQUESTED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6641#pullrequestreview-2908957761)
- `2025-06-11T15:06:55Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6641#pullrequestreview-2917641841)
- `2025-06-12T02:02:44Z` `APPROVED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6641#pullrequestreview-2919143635)
- `2025-06-20T05:26:45Z` `CHANGES_REQUESTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/6641#pullrequestreview-2944599996)
- `2025-06-20T06:00:01Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6641#pullrequestreview-2944655135)
- `2025-06-20T06:01:08Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6641#pullrequestreview-2944656938)
- `2025-06-20T06:53:41Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/6641#pullrequestreview-2944778682)
- `2025-06-20T07:19:30Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6641#pullrequestreview-2944838495)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 6 inline comment(s)
- `python/sglang/srt/layers/vocab_parallel_embedding.py`: 4 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_native.py`: 2 inline comment(s)
- `python/sglang/srt/layers/linear.py`: 2 inline comment(s)
- `python/sglang/srt/utils.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-06-05T05:49:39Z` `inline` by `chunyuan-w` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:256; signals: kernel, moe, triton; excerpt: "I checked that our C++ kernel does not support apply router weight on input = True. I updated the check condition here." (https://github.com/sgl-project/sglang/pull/6641#discussion_r2128004308)
- `2025-06-05T02:12:48Z` `inline` by `mingfeima` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:256; signals: kernel, moe, triton; excerpt: "does our C++ kernels support apply router weight on input, if not, we need to let it use fallbacks." (https://github.com/sgl-project/sglang/pull/6641#discussion_r2127808065)
- `2025-06-09T05:32:44Z` `inline` by `mingfeima` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:262; signals: kernel, moe, triton; excerpt: "enable apply router weight on input in the next step in our C++ kernels." (https://github.com/sgl-project/sglang/pull/6641#discussion_r2135056931)
- `2025-06-05T02:27:13Z` `inline` by `mingfeima` `python/sglang/srt/models/deepseek_v2.py`:1017; signals: kernel, mla; excerpt: "I think we can skip this part. You can directly port forward absorb decode fused cpu from our developing branch (including qkv proj kernels), ..." (https://github.com/sgl-project/sglang/pull/6641#discussion_r2127819978)
- `2025-06-06T07:42:52Z` `inline` by `chunyuan-w` `python/sglang/srt/models/deepseek_v2.py`:1017; signals: kernel, mla; excerpt: "Added AttnForwardMethod.MLA FUSED ROPE CPU and will use the torch.ops.sgl kernel.fused qkv proj with rope kernel" (https://github.com/sgl-project/sglang/pull/6641#discussion_r2131687640)
- `2025-06-09T05:40:01Z` `inline` by `mingfeima` `python/sglang/srt/models/deepseek_v2.py`:1375; signals: fp8, kernel; excerpt: "we shouldn't have this part. both w vc and w kc should have been converted to bfloat16 when they got here. next step, once ..." (https://github.com/sgl-project/sglang/pull/6641#discussion_r2135063619)
- `2025-06-05T02:29:19Z` `review` `CHANGES_REQUESTED` by `mingfeima`; signals: mla; excerpt: "for the mla decoding integration, skip our early stage parts, directly port forward absorb decode fused cpu" (https://github.com/sgl-project/sglang/pull/6641#pullrequestreview-2898673317)
- `2025-06-20T07:19:30Z` `inline` by `chunyuan-w` `python/sglang/srt/layers/moe/fused_moe_native.py`:81; signals: moe; excerpt: "Just to make the inputs to this moe forward native function the same as the forward cpu function of UnquantizedFusedMoEMethod here:" (https://github.com/sgl-project/sglang/pull/6641#discussion_r2158229594)
- `2025-06-20T06:53:41Z` `inline` by `zhyncs` `python/sglang/srt/layers/moe/fused_moe_native.py`:81; signals: moe; excerpt: "QQ why do we need to add inplace and no combine parameters here?" (https://github.com/sgl-project/sglang/pull/6641#discussion_r2158192890)
- `2025-06-20T06:01:08Z` `inline` by `chunyuan-w` `python/sglang/srt/layers/vocab_parallel_embedding.py`:556; signals: general review; excerpt: "We will check the device inside PackWeightMethod. But to make this cleaner, I updated the code to check is cpu and is cpu amx ..." (https://github.com/sgl-project/sglang/pull/6641#discussion_r2158116016)
- `2025-06-05T02:27:39Z` `inline` by `mingfeima` `python/sglang/srt/models/deepseek_v2.py`:1091; signals: general review; excerpt: "same as above, skip this and use forward absorb decode fused cpu" (https://github.com/sgl-project/sglang/pull/6641#discussion_r2127820292)
- `2025-06-06T07:42:20Z` `inline` by `chunyuan-w` `python/sglang/srt/models/deepseek_v2.py`:1091; signals: general review; excerpt: "Fixed" (https://github.com/sgl-project/sglang/pull/6641#discussion_r2131686920)
