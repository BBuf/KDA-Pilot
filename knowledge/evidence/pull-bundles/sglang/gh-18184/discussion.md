# PR Discussion Digest

- Source PR: [sgl-project/sglang#18184](https://github.com/sgl-project/sglang/pull/18184)
- Source page: `sources/prs/sglang/PR-18184.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18184`
- Generated at: `2026-05-20T15:28:35.175885+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-03T15:00:19Z`
- Merged: `2026-03-14T20:03:31Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 9
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=2, outdated=4
- Human participants with discussion text: Fridge003, Oasis-Git, moehanabi, samuellees, xiaoweiw-nv
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-03T15:03:19Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds piecewise CUDA graph support for the Qwen3-Next FP8 flashinfer trtllm MoE backend. ... (https://github.com/sgl-project/sglang/pull/18184#pullrequestreview-3745814959)
- `2026-02-04T08:04:52Z` `COMMENTED` by `Oasis-Git` - In comments (https://github.com/sgl-project/sglang/pull/18184#pullrequestreview-3749549820)
- `2026-02-05T01:10:48Z` `COMMENTED` by `xiaoweiw-nv` (https://github.com/sgl-project/sglang/pull/18184#pullrequestreview-3754041413)
- `2026-02-05T04:47:54Z` `COMMENTED` by `Oasis-Git` (https://github.com/sgl-project/sglang/pull/18184#pullrequestreview-3754546096)
- `2026-02-09T08:46:58Z` `COMMENTED` by `xiaoweiw-nv` (https://github.com/sgl-project/sglang/pull/18184#pullrequestreview-3771947722)
- `2026-02-09T08:47:01Z` `COMMENTED` by `xiaoweiw-nv` (https://github.com/sgl-project/sglang/pull/18184#pullrequestreview-3771947897)
- `2026-03-12T06:41:00Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/18184#pullrequestreview-3934313661)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 5 inline comment(s)
- `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-03-04T12:27:13Z` `issue` by `moehanabi`; signals: accuracy, attention, cache, cuda, dtype, flashinfer, hang, moe; excerpt: "Hi @moehanabi , thanks for your feedback. I tested accuracy with PCG enabled and it's OK. I also tested a promt which generates 4096 ..." (https://github.com/sgl-project/sglang/pull/18184#issuecomment-3997242009)
- `2026-03-04T03:53:20Z` `issue` by `xiaoweiw-nv`; signals: accuracy, attention, cache, cuda, dtype, flashinfer, moe; excerpt: "Hi @moehanabi , thanks for your feedback. I tested accuracy with PCG enabled and it's OK. I also tested a promt which generates 4096 ..." (https://github.com/sgl-project/sglang/pull/18184#issuecomment-3995089225)
- `2026-02-05T01:10:47Z` `inline` by `xiaoweiw-nv` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:960; signals: bf16, flashinfer, moe, triton; excerpt: "Flashinfer's trtllm bf16 moe only supports bypassed topk so I removed the standard topk path" (https://github.com/sgl-project/sglang/pull/18184#discussion_r2766624171)
- `2026-02-04T08:04:45Z` `inline` by `Oasis-Git` `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`:186; signals: flashinfer, moe, register; excerpt: "by now we use @register custom op instead of using this function." (https://github.com/sgl-project/sglang/pull/18184#discussion_r2762705372)
- `2026-03-03T12:05:24Z` `issue` by `moehanabi`; signals: accuracy, cuda, fp8; excerpt: "hi, thanks for your pr. in my test (also Qwen3-Next-80B-A3B-Instruct-FP8), the output length will be much shorter than that with piece cuda graph disabled. ..." (https://github.com/sgl-project/sglang/pull/18184#issuecomment-3990579605)
- `2026-03-04T03:22:58Z` `issue` by `samuellees`; signals: accuracy, cuda, fp8; excerpt: "hi, thanks for your pr. in my test (also Qwen3-Next-80B-A3B-Instruct-FP8), the output length will be much shorter than that with piece cuda graph disabled. ..." (https://github.com/sgl-project/sglang/pull/18184#issuecomment-3994999172)
- `2026-03-04T03:37:10Z` `issue` by `moehanabi`; signals: accuracy, cuda, fp8; excerpt: "hi, thanks for your pr. in my test (also Qwen3-Next-80B-A3B-Instruct-FP8), the output length will be much shorter than that with piece cuda graph disabled. ..." (https://github.com/sgl-project/sglang/pull/18184#issuecomment-3995039906)
- `2026-02-04T08:02:49Z` `inline` by `Oasis-Git` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:960; signals: moe, triton; excerpt: "I think we may need to add the support for bypassed instead of directly cover the logic of standard?" (https://github.com/sgl-project/sglang/pull/18184#discussion_r2762699280)
- `2026-02-05T04:47:54Z` `inline` by `Oasis-Git` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:960; signals: moe, triton; excerpt: "We should provide different path solutions based on top k format" (https://github.com/sgl-project/sglang/pull/18184#discussion_r2767105372)
- `2026-02-09T08:46:58Z` `inline` by `xiaoweiw-nv` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:960; signals: moe, triton; excerpt: "Updated to include path for both standard and bypassed topk" (https://github.com/sgl-project/sglang/pull/18184#discussion_r2781354858)
- `2026-02-09T08:47:00Z` `inline` by `xiaoweiw-nv` `python/sglang/srt/layers/moe/flashinfer_trtllm_moe.py`:186; signals: flashinfer, moe; excerpt: "Updated" (https://github.com/sgl-project/sglang/pull/18184#discussion_r2781355019)
- `2026-02-04T08:04:52Z` `review` `COMMENTED` by `Oasis-Git`; signals: general review; excerpt: "In comments" (https://github.com/sgl-project/sglang/pull/18184#pullrequestreview-3749549820)
