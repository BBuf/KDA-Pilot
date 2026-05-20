# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11869](https://github.com/NVIDIA/TensorRT-LLM/pull/11869)
- Source page: `sources/prs/tensorrt-llm/PR-11869.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11869`
- Generated at: `2026-05-20T15:17:51.128795+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-03T19:04:36Z`
- Merged: `2026-04-04T07:29:45Z`

## Discussion Counts

- Issue comments: 59
- Review submissions: 28 (approved=3, commented=25)
- Inline review comments: 42
- Review threads observed: 23
- Resolved/outdated thread markers: resolved=23, outdated=18
- Human participants with discussion text: NVShreyas, chang-l, coderabbitai, karljang, liji-nv, tensorrt-cicd, yibinl-nvidia
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-03T22:21:13Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 🧹 Nitpick comments (5) cpp/tensorrt llm/kernels/fusedDiTQKNormRopeKernel.h (1) 17-17: Replace pragma once with the required ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-3885386059)
- `2026-03-04T15:28:24Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-3890154903)
- `2026-03-04T15:30:36Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-3890168102)
- `2026-03-04T16:17:54Z` `COMMENTED` by `karljang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-3890476379)
- `2026-03-04T16:24:17Z` `COMMENTED` by `karljang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-3890513758)
- `2026-03-25T15:47:19Z` `APPROVED` by `yibinl-nvidia` - LGTM for LTX-2 model changes. (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4007790372)
- `2026-03-25T17:40:13Z` `COMMENTED` by `karljang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4008558677)
- `2026-03-25T17:41:33Z` `COMMENTED` by `karljang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4008569055)
- `2026-03-27T17:18:27Z` `COMMENTED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4022186613)
- `2026-03-28T00:26:00Z` `COMMENTED` by `karljang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4024303922)
- `2026-03-28T00:27:15Z` `COMMENTED` by `karljang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4024306493)
- `2026-03-28T01:01:13Z` `COMMENTED` by `karljang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4024411127)
- `2026-03-28T01:35:44Z` `COMMENTED` by `karljang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4024477601)
- `2026-03-28T01:38:38Z` `COMMENTED` by `karljang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4024480710)
- `2026-03-28T03:35:01Z` `COMMENTED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4024671066)
- `2026-03-28T04:27:11Z` `COMMENTED` by `karljang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4024787664)
- `2026-03-30T22:47:00Z` `COMMENTED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4033684062)
- `2026-03-31T00:44:39Z` `COMMENTED` by `karljang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4034003964)
- `2026-03-31T23:32:26Z` `COMMENTED` by `karljang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4040822597)
- `2026-03-31T23:33:15Z` `COMMENTED` by `karljang` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4040825684)
- `2026-04-01T03:26:41Z` `COMMENTED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4041431040)
- `2026-04-01T05:19:07Z` `APPROVED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4041730671)
- `2026-04-01T05:27:01Z` `COMMENTED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4041752910)
- `2026-04-01T05:29:12Z` `APPROVED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-4041762076)
- ... 4 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tensorrt_llm/_torch/visual_gen/modules/attention.py`: 10 inline comment(s)
- `tensorrt_llm/_torch/visual_gen/models/flux/attention.py`: 9 inline comment(s)
- `cpp/tensorrt_llm/kernels/fusedDiTQKNormRopeKernel.cu`: 5 inline comment(s)
- `tensorrt_llm/_torch/visual_gen/config.py`: 5 inline comment(s)
- `examples/visual_gen/visual_gen_flux.py`: 4 inline comment(s)
- `tests/unittest/_torch/thop/parallel/test_fused_dit_qk_norm_rope.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/visual_gen/models/ltx2/transformer_ltx2.py`: 3 inline comment(s)
- `cpp/tensorrt_llm/thop/fusedDiTQKNormRopeOp.cpp`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-03T22:21:13Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, cuda, hang, kernel, occupancy, tensorrt, throughput; excerpt: "Actionable comments posted: 3 🧹 Nitpick comments (5) cpp/tensorrt llm/kernels/fusedDiTQKNormRopeKernel.h (1) 17-17: Replace pragma once with the required TRTLLM header guard macro. This header ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#pullrequestreview-3885386059)
- `2026-03-03T22:21:09Z` `issue` by `coderabbitai`; signals: attention, cuda, hang, kernel, perf, performance, tensorrt; excerpt: "📝 Walkthrough Walkthrough The pull request introduces a fused CUDA kernel for efficient per-head QK normalization and RoPE transformation in Diffusion Transformers. It includes ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#issuecomment-3993931348)
- `2026-03-03T22:21:12Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/fusedDiTQKNormRopeKernel.cu`:66; signals: benchmark, kernel, race, tensorrt; excerpt: "🛠️ Refactor suggestion 🟠 Major Add braces around the early return statement. As per coding guidelines: "The statement forming the body of a switch, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#discussion_r2880799916)
- `2026-03-04T15:30:36Z` `inline` by `NVShreyas` `tensorrt_llm/_torch/visual_gen/models/flux/attention.py`:328; signals: attention, cuda, kernel, tensorrt; excerpt: "if the cuda kernel is always better and accurate, can we remove the old path?" (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#discussion_r2884458668)
- `2026-03-03T22:21:12Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/visual_gen/models/flux/attention.py`:416; signals: attention, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Missing None check for image rotary emb could raise TypeError. The fused prepare qkv unconditionally unpacks image rotary emb ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#discussion_r2880799924)
- `2026-03-25T17:40:13Z` `inline` by `karljang` `tensorrt_llm/_torch/visual_gen/models/flux/attention.py`:328; signals: attention, hang, tensorrt; excerpt: "Based on discussion with @chang-l , the fused path has been integrated to Attention class itself, so now no additional wiring is needed :)" (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#discussion_r2989909304)
- `2026-03-30T22:47:00Z` `inline` by `chang-l` `tensorrt_llm/_torch/visual_gen/modules/attention.py`:252; signals: attention, kernel, tensorrt; excerpt: "Is it possible to avoid these reshape/contiguous ops before launching the fused kernel? For example, can we pre-compute freq cos/sin in the same format?" (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#discussion_r3012561555)
- `2026-03-31T00:44:39Z` `inline` by `karljang` `tensorrt_llm/_torch/visual_gen/modules/attention.py`:252; signals: attention, block, tensorrt; excerpt: "I had the same feeling we might be able to take it out of attention block, moving to a higher model level instead. But ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#discussion_r3012871683)
- `2026-03-04T16:24:17Z` `inline` by `karljang` `tensorrt_llm/_torch/visual_gen/models/flux/attention.py`:328; signals: attention, hang, tensorrt; excerpt: "@chang-l , do you agree on removing un-fused path? we'll be able to reduce code complexity a lot." (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#discussion_r2884767078)
- `2026-03-27T16:42:27Z` `inline` by `chang-l` `tensorrt_llm/_torch/visual_gen/modules/attention.py`:201; signals: attention, hang, tensorrt; excerpt: "Can we change this part back?" (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#discussion_r3002041823)
- `2026-03-27T17:13:49Z` `inline` by `chang-l` `tensorrt_llm/_torch/visual_gen/modules/attention.py`:100; signals: attention, hang, tensorrt; excerpt: "can you remove any unnecessary or unrelated changes in this PR?" (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#discussion_r3002209710)
- `2026-03-27T17:16:41Z` `inline` by `chang-l` `tensorrt_llm/_torch/visual_gen/modules/attention.py`:295; signals: attention, layout, tensorrt; excerpt: "Can you add back the comments including each attention backend has different layout?" (https://github.com/NVIDIA/TensorRT-LLM/pull/11869#discussion_r3002222023)
