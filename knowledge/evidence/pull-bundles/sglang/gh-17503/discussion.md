# PR Discussion Digest

- Source PR: [sgl-project/sglang#17503](https://github.com/sgl-project/sglang/pull/17503)
- Source page: `sources/prs/sglang/PR-17503.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-17503`
- Generated at: `2026-05-20T15:28:29.144439+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-21T13:01:27Z`
- Merged: `2026-02-16T15:03:51Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 28 (approved=1, changes_requested=1, commented=26)
- Inline review comments: 46
- Review threads observed: 25
- Resolved/outdated thread markers: resolved=23, outdated=15
- Human participants with discussion text: HandH1998, JustinTong0323, TamirBaydasov, ping1jing2
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2026-01-21T13:06:26Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the Mixture of Experts (MoE) schemes for compressed tensors by moving them ... (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3687159039)
- `2026-01-27T09:53:44Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3710197872)
- `2026-01-27T09:54:13Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3710199902)
- `2026-01-27T09:54:31Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3710201267)
- `2026-01-28T11:30:43Z` `CHANGES_REQUESTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3716015531)
- `2026-01-28T11:46:40Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3716266110)
- `2026-01-28T11:46:41Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3716266222)
- `2026-01-28T11:53:24Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3716296780)
- `2026-01-28T11:58:07Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3716321015)
- `2026-01-28T13:06:49Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3716607160)
- `2026-01-28T13:06:54Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3716607534)
- `2026-01-28T14:06:12Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3716905485)
- `2026-01-28T14:39:31Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3717075465)
- `2026-01-28T14:40:20Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3717079542)
- `2026-01-28T14:40:59Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3717082747)
- `2026-01-28T14:41:17Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3717084167)
- `2026-01-28T14:41:25Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3717084802)
- `2026-01-28T14:41:32Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3717085424)
- `2026-01-28T14:41:40Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3717086063)
- `2026-01-28T14:53:34Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3717146701)
- `2026-01-28T14:55:21Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3717156559)
- `2026-01-28T15:04:37Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3717205887)
- `2026-01-28T15:37:11Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3717419070)
- `2026-01-28T15:37:20Z` `COMMENTED` by `TamirBaydasov` (https://github.com/sgl-project/sglang/pull/17503#pullrequestreview-3717419732)
- ... 2 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`: 13 inline comment(s)
- `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxint4_moe.py`: 12 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 10 inline comment(s)
- `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a8_int8_moe.py`: 7 inline comment(s)
- `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4_moe.py`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_int8_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-27T09:54:13Z` `inline` by `TamirBaydasov` `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4_moe.py`:300; signals: fp4, moe, nvfp4; excerpt: "Done" (https://github.com/sgl-project/sglang/pull/17503#discussion_r2731173350)
- `2026-02-16T15:03:25Z` `issue` by `ping1jing2`; signals: cuda, failing, hang; excerpt: "i merge it since both HandH1998 and AniZpZ approved it. The single failing AMD UT([Exception: Capture cuda graph failed: Could not find CUDA installation. ..." (https://github.com/sgl-project/sglang/pull/17503#issuecomment-3908964129)
- `2026-01-28T10:54:22Z` `inline` by `ping1jing2` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:683; signals: moe, triton; excerpt: "what's the current status about the TODO ? please help to check and list these TODOs into roadmap issue." (https://github.com/sgl-project/sglang/pull/17503#discussion_r2736079655)
- `2026-01-28T11:58:07Z` `inline` by `TamirBaydasov` `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxint4_moe.py`:184; signals: block, moe; excerpt: "I am not the author of MXInt4MoE method so I can't write a good docstring about this code block. We will need to ask ..." (https://github.com/sgl-project/sglang/pull/17503#discussion_r2736306230)
- `2026-01-28T14:06:12Z` `inline` by `TamirBaydasov` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`:978; signals: hang, kernel; excerpt: "We can, but it will require changing every quantization algorithm file, which is best done under "Kernel call and weight init split" step of ..." (https://github.com/sgl-project/sglang/pull/17503#discussion_r2736805845)
- `2026-01-28T10:49:20Z` `inline` by `ping1jing2` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:683; signals: moe, triton; excerpt: "what's the current status about this TODO ?" (https://github.com/sgl-project/sglang/pull/17503#discussion_r2736060399)
- `2026-01-28T10:53:10Z` `inline` by `ping1jing2` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:674; signals: moe, triton; excerpt: "how about code like below" (https://github.com/sgl-project/sglang/pull/17503#discussion_r2736075241)
- `2026-01-28T10:57:47Z` `inline` by `ping1jing2` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:897; signals: moe, triton; excerpt: "ditto" (https://github.com/sgl-project/sglang/pull/17503#discussion_r2736092326)
- `2026-01-28T11:07:10Z` `inline` by `ping1jing2` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`:187; signals: hang, moe; excerpt: "how about changing the code into layer.scheme = self.get moe scheme(layer=layer, layer name=prefix)?" (https://github.com/sgl-project/sglang/pull/17503#discussion_r2736127241)
- `2026-01-28T11:46:39Z` `inline` by `TamirBaydasov` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:683; signals: moe, triton; excerpt: "Added to roadmap, will look into it" (https://github.com/sgl-project/sglang/pull/17503#discussion_r2736264808)
- `2026-01-28T11:46:41Z` `inline` by `TamirBaydasov` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:683; signals: moe, triton; excerpt: "Added to roadmap, will look into it" (https://github.com/sgl-project/sglang/pull/17503#discussion_r2736264862)
- `2026-01-28T13:06:49Z` `inline` by `TamirBaydasov` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:674; signals: moe, triton; excerpt: "Done" (https://github.com/sgl-project/sglang/pull/17503#discussion_r2736554146)
