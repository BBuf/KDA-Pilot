# PR Discussion Digest

- Source PR: [sgl-project/sglang#15888](https://github.com/sgl-project/sglang/pull/15888)
- Source page: `sources/prs/sglang/PR-15888.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-15888`
- Generated at: `2026-05-20T15:28:16.770167+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-26T10:31:47Z`
- Merged: `2025-12-30T06:30:22Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 10 (approved=1, commented=9)
- Inline review comments: 11
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: IPostYellow, mickqian, yhyang201
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 11

## Review Decisions

- `2025-12-26T10:34:28Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for the TurboWan2.1-T2V-1.3B-480P model, introducing Sparse Linear Attention (SLA) for improved ... (https://github.com/sgl-project/sglang/pull/15888#pullrequestreview-3613248810)
- `2025-12-29T02:28:14Z` `COMMENTED` by `IPostYellow` (https://github.com/sgl-project/sglang/pull/15888#pullrequestreview-3614942156)
- `2025-12-29T05:56:37Z` `COMMENTED` by `IPostYellow` (https://github.com/sgl-project/sglang/pull/15888#pullrequestreview-3615091915)
- `2025-12-30T06:03:08Z` `APPROVED` by `yhyang201` (https://github.com/sgl-project/sglang/pull/15888#pullrequestreview-3617351783)

## Inline Comment Hotspots

- `python/sglang/multimodal_gen/registry.py`: 4 inline comment(s)
- `python/sglang/multimodal_gen/runtime/layers/attention/turbo_layer.py`: 3 inline comment(s)
- `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py`: 2 inline comment(s)
- `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-29T02:28:14Z` `inline` by `IPostYellow` `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py`:102; signals: attention, pipeline; excerpt: "It's better to pass this part through the config file, because in the future attention type could also be sagesla." (https://github.com/sgl-project/sglang/pull/15888#discussion_r2650081262)
- `2025-12-27T00:36:08Z` `issue` by `IPostYellow`; signals: flashinfer; excerpt: "It seems that qwen-image has been dependent on flashinfer since the [51dbdb2]( while the AMD test environment does not have flashinfer installed. Below is ..." (https://github.com/sgl-project/sglang/pull/15888#issuecomment-3693521167)
- `2025-12-27T10:58:08Z` `issue` by `yhyang201`; signals: cuda; excerpt: "Once the CUDA test passes, that’s fine! I can’t access the model link you provided and we are considering whether we need to upload ..." (https://github.com/sgl-project/sglang/pull/15888#issuecomment-3693903789)
- `2025-12-27T13:11:16Z` `issue` by `IPostYellow`; signals: cuda; excerpt: "Once the CUDA test passes, that’s fine! I can’t access the model link you provided and we are considering whether we need to upload ..." (https://github.com/sgl-project/sglang/pull/15888#issuecomment-3693968670)
- `2025-12-29T05:56:37Z` `inline` by `IPostYellow` `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`:282; signals: general review; excerpt: "In Turbodiffusion, it is a fixed value; consider whether it needs to be moved into the WanVideoArchConfig." (https://github.com/sgl-project/sglang/pull/15888#discussion_r2650244090)
- `2025-12-26T11:44:35Z` `issue` by `IPostYellow`; signals: general review; excerpt: "hi @mickqian , I noticed that wan2 2 i2v a14b 2gpu in python/sglang/multimodal gen/test/server/testcase configs.py doesn't have num gpus=2. Is this expected?" (https://github.com/sgl-project/sglang/pull/15888#issuecomment-3692751403)
