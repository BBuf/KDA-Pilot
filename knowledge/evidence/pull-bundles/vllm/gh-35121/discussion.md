# PR Discussion Digest

- Source PR: [vllm-project/vllm#35121](https://github.com/vllm-project/vllm/pull/35121)
- Source page: `sources/prs/vllm/PR-35121.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-35121`
- Generated at: `2026-05-20T15:39:58.121527+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-23T17:45:26Z`
- Merged: `2026-02-27T00:51:29Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 6 (commented=6)
- Inline review comments: 10
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: mgoin, roikoren755
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-23T17:48:15Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request introduces a cuBLAS fallback for the MoE router GEMM (bf16 x bf16 - ... (https://github.com/vllm-project/vllm/pull/35121#pullrequestreview-3842614809)
- `2026-02-25T21:26:34Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/35121#pullrequestreview-3857074833)
- `2026-02-26T15:56:01Z` `COMMENTED` by `roikoren755` (https://github.com/vllm-project/vllm/pull/35121#pullrequestreview-3861909376)
- `2026-02-26T17:17:46Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/35121#pullrequestreview-3862192480)
- `2026-02-26T18:28:36Z` `COMMENTED` by `roikoren755` (https://github.com/vllm-project/vllm/pull/35121#pullrequestreview-3862843342)
- `2026-02-26T18:30:43Z` `COMMENTED` by `roikoren755` (https://github.com/vllm-project/vllm/pull/35121#pullrequestreview-3862853632)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/router/gate_linear.py`: 7 inline comment(s)
- `csrc/moe/router_gemm.cu`: 3 inline comment(s)

## High-Signal Discussion

- `2026-02-25T21:26:32Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/router/gate_linear.py`:109; signals: cuda, moe, perf, performance; excerpt: "If this is going to run across all batch sizes and CUDA arches, can we validate with some performance sweeps? I don't want this ..." (https://github.com/vllm-project/vllm/pull/35121#discussion_r2855593697)
- `2026-02-26T15:56:01Z` `inline` by `roikoren755` `vllm/model_executor/layers/fused_moe/router/gate_linear.py`:109; signals: kernel, moe, perf, performance; excerpt: "Updated PR description with sweep. As noted there, the kernels won't currently get chosen for sm80 and sm121, as there's some performance drop there ..." (https://github.com/vllm-project/vllm/pull/35121#discussion_r2859842926)
- `2026-02-26T16:41:37Z` `inline` by `mgoin` `csrc/moe/router_gemm.cu`:10; signals: compile, cuda, gemm, moe; excerpt: "Does this require any minimum CUDA version to compile?" (https://github.com/vllm-project/vllm/pull/35121#discussion_r2860093941)
- `2026-02-25T21:24:27Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/router/gate_linear.py`:33; signals: dtype, hang, moe; excerpt: "I'm not sure the default out dtype should be set or float32. I feel this should be opt-in to change the out dtype from ..." (https://github.com/vllm-project/vllm/pull/35121#discussion_r2855582998)
- `2026-02-26T18:30:43Z` `inline` by `roikoren755` `csrc/moe/router_gemm.cu`:10; signals: cuda, gemm, moe; excerpt: "Should work with CUDA 11 and higher" (https://github.com/vllm-project/vllm/pull/35121#discussion_r2860663042)
- `2026-02-25T21:23:02Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/router/gate_linear.py`:88; signals: dtype, moe; excerpt: "nit: we could do all these checks AOT in the constructor except for x.dtype == torch.bfloat16. side note: if we are including bias, should ..." (https://github.com/vllm-project/vllm/pull/35121#discussion_r2855575903)
- `2026-02-26T17:16:42Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/router/gate_linear.py`:114; signals: moe; excerpt: "It seems like output bias is only returned from ReplicatedLinear.forward in some cases, so should we deal with this? The return type is torch.Tensor ..." (https://github.com/vllm-project/vllm/pull/35121#discussion_r2860302295)
- `2026-02-26T18:28:36Z` `inline` by `roikoren755` `vllm/model_executor/layers/fused_moe/router/gate_linear.py`:114; signals: moe; excerpt: "if ReplicatedLinear is initialized with return bias=True (the default), it always returns a tuple. Both places that use this new GateLinear (and all other ..." (https://github.com/vllm-project/vllm/pull/35121#discussion_r2860654688)
