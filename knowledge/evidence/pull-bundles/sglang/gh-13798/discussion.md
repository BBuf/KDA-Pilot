# PR Discussion Digest

- Source PR: [sgl-project/sglang#13798](https://github.com/sgl-project/sglang/pull/13798)
- Source page: `sources/prs/sglang/PR-13798.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13798`
- Generated at: `2026-05-20T15:27:53.132492+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-23T14:03:54Z`
- Merged: `2025-12-12T06:56:13Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 10 (approved=2, commented=8)
- Inline review comments: 11
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=5, outdated=7
- Human participants with discussion text: SeanLi-OI, b8zhong, kaixih, samuellees
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-11-23T14:05:58Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables TRTLLM BF16 MoE on Blackwell GPUs, which is a valuable addition. The ... (https://github.com/sgl-project/sglang/pull/13798#pullrequestreview-3497791949)
- `2025-11-29T07:01:16Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/13798#pullrequestreview-3520511817)
- `2025-11-30T02:49:32Z` `COMMENTED` by `samuellees` (https://github.com/sgl-project/sglang/pull/13798#pullrequestreview-3520915261)
- `2025-12-03T07:44:26Z` `COMMENTED` by `SeanLi-OI` (https://github.com/sgl-project/sglang/pull/13798#pullrequestreview-3533617133)
- `2025-12-03T07:56:55Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/13798#pullrequestreview-3526058413)
- `2025-12-03T11:42:35Z` `COMMENTED` by `samuellees` (https://github.com/sgl-project/sglang/pull/13798#pullrequestreview-3534659261)
- `2025-12-03T12:40:59Z` `COMMENTED` by `samuellees` (https://github.com/sgl-project/sglang/pull/13798#pullrequestreview-3534861374)
- `2025-12-08T16:41:14Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/13798#pullrequestreview-3553007288)
- `2025-12-11T17:26:04Z` `APPROVED` by `kaixih` (https://github.com/sgl-project/sglang/pull/13798#pullrequestreview-3568525658)
- `2025-12-11T17:55:07Z` `APPROVED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/13798#pullrequestreview-3568641977)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 6 inline comment(s)
- `python/sglang/srt/layers/quantization/unquant.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 1 inline comment(s)
- `python/sglang/srt/server_args.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-03T07:44:26Z` `inline` by `SeanLi-OI` `python/sglang/srt/layers/quantization/unquant.py`:282; signals: layout, memory, oom; excerpt: "Convert all experts layout and stack may double the memory usage, which may cause oom when loading weights." (https://github.com/sgl-project/sglang/pull/13798#discussion_r2583987779)
- `2025-11-29T07:01:17Z` `inline` by `b8zhong` `python/sglang/srt/layers/moe/ep_moe/layer.py`:429; signals: block, moe; excerpt: "qq; do we need this except block, bc if i feel this import will not fail" (https://github.com/sgl-project/sglang/pull/13798#discussion_r2572846041)
- `2025-12-01T16:58:02Z` `inline` by `b8zhong` `python/sglang/srt/layers/moe/ep_moe/layer.py`:564; signals: fp8, moe; excerpt: "should it be quant config.get name() can be fp8 and modelopt fp8?" (https://github.com/sgl-project/sglang/pull/13798#discussion_r2577892662)
- `2025-11-30T02:49:32Z` `inline` by `samuellees` `python/sglang/srt/layers/moe/ep_moe/layer.py`:429; signals: moe; excerpt: "Yes, your are right. Removed, thanks!" (https://github.com/sgl-project/sglang/pull/13798#discussion_r2573309576)
- `2025-12-03T11:42:33Z` `inline` by `samuellees` `python/sglang/srt/layers/moe/ep_moe/layer.py`:564; signals: moe; excerpt: "Yes, it should be. Fixed" (https://github.com/sgl-project/sglang/pull/13798#discussion_r2584786252)
- `2025-12-09T09:32:36Z` `issue` by `samuellees`; signals: fp4; excerpt: "@samuellees I think this CI failure might be related Fixed by setting TopKOutputFormat correctly in this case. test/srt/test deepseek v3 fp4 4gpu.py passed on ..." (https://github.com/sgl-project/sglang/pull/13798#issuecomment-3631235467)
- `2025-11-24T11:31:44Z` `issue` by `samuellees`; signals: hang; excerpt: "cc @yizhang2077 Because this also supports Qwen3/Qwen3-Next models" (https://github.com/sgl-project/sglang/pull/13798#issuecomment-3570325414)
- `2025-12-08T16:41:14Z` `inline` by `b8zhong` `python/sglang/srt/server_args.py`:1594; signals: general review; excerpt: "Can we just add None to the list (to represent the bfloat16 case like on L1557), bc it may run into some issues in ..." (https://github.com/sgl-project/sglang/pull/13798#discussion_r2599332016)
- `2025-12-03T12:40:59Z` `inline` by `samuellees` `python/sglang/srt/layers/quantization/unquant.py`:282; signals: general review; excerpt: "This makes sense. Fixed by inplace convert." (https://github.com/sgl-project/sglang/pull/13798#discussion_r2584961119)
