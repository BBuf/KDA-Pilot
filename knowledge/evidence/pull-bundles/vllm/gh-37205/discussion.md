# PR Discussion Digest

- Source PR: [vllm-project/vllm#37205](https://github.com/vllm-project/vllm/pull/37205)
- Source page: `sources/prs/vllm/PR-37205.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-37205`
- Generated at: `2026-05-20T15:40:17.893096+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-16T16:12:28Z`
- Merged: `2026-03-18T15:15:56Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 14 (approved=1, commented=13)
- Inline review comments: 18
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=7, outdated=8
- Human participants with discussion text: mergify, mgoin, xyang16
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-16T16:17:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces an optimized GEMM kernel for the gpt-oss router, which demonstrates performance improvements ... (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3955080503)
- `2026-03-16T16:40:05Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3955196599)
- `2026-03-16T21:09:01Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3956676140)
- `2026-03-16T21:09:07Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3956676542)
- `2026-03-16T21:09:13Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3956676966)
- `2026-03-16T21:09:19Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3956677440)
- `2026-03-16T21:09:54Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3956679863)
- `2026-03-16T22:59:42Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3957231760)
- `2026-03-17T00:09:22Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3957452185)
- `2026-03-17T19:34:16Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3963284876)
- `2026-03-17T19:40:53Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3963318689)
- `2026-03-17T21:27:51Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3963862402)
- `2026-03-17T21:35:34Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3963893151)
- `2026-03-18T15:15:36Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/37205#pullrequestreview-3968646334)

## Inline Comment Hotspots

- `csrc/moe/tinygemm2.cu`: 6 inline comment(s)
- `vllm/model_executor/layers/fused_moe/router/gate_linear.py`: 4 inline comment(s)
- `csrc/moe/gpt_oss_router_gemm.cuh`: 2 inline comment(s)
- `benchmarks/kernels/benchmark_router_gemm.py`: 2 inline comment(s)
- `csrc/moe/torch_bindings.cpp`: 2 inline comment(s)
- `vllm/model_executor/models/gpt_oss.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-16T16:36:30Z` `inline` by `mgoin` `benchmarks/kernels/benchmark_router_gemm.py`; signals: benchmark, gemm, kernel; excerpt: "nit: could you maybe update this to include the deepseek router gemm too? we could select the model as an argument" (https://github.com/vllm-project/vllm/pull/37205#discussion_r2941564372)
- `2026-03-17T00:09:22Z` `inline` by `xyang16` `benchmarks/kernels/benchmark_router_gemm.py`; signals: benchmark, gemm, kernel; excerpt: "@mgoin I have updated the benchmark script to include deepseek router gemm. It can be run like below now:" (https://github.com/vllm-project/vllm/pull/37205#discussion_r2943657472)
- `2026-03-17T19:40:53Z` `inline` by `xyang16` `vllm/model_executor/layers/fused_moe/router/gate_linear.py`:123; signals: compile, gemm, moe; excerpt: "Yes, ideally the check should be: But I found if I have x.shape[0] <= 128 check like above, the custom router gemm is never ..." (https://github.com/vllm-project/vllm/pull/37205#discussion_r2949163411)
- `2026-03-17T21:35:33Z` `inline` by `xyang16` `vllm/model_executor/layers/fused_moe/router/gate_linear.py`:123; signals: bf16, gemm, moe; excerpt: "Thanks! And since the cublas ops.router gemm bf16 fp32 doesn't support bias, so it's basically the same as before." (https://github.com/vllm-project/vllm/pull/37205#discussion_r2949685804)
- `2026-03-17T23:28:16Z` `issue` by `xyang16`; signals: flashinfer, gemm, kernel; excerpt: "It seems we might be able to get this gemm directly from flashinfer? 37244 @mgoin Do you prefer flashinfer or include this kernel in ..." (https://github.com/vllm-project/vllm/pull/37205#issuecomment-4078639656)
- `2026-03-18T13:36:05Z` `issue` by `xyang16`; signals: flashinfer, gemm, kernel; excerpt: "It seems we might be able to get this gemm directly from flashinfer? 37244 @mgoin I tried the flashinfer tinygemm, but it breaks test ..." (https://github.com/vllm-project/vllm/pull/37205#issuecomment-4082622102)
- `2026-03-16T16:38:05Z` `inline` by `mgoin` `csrc/moe/torch_bindings.cpp`:140; signals: gemm, moe; excerpt: "Do you know this gemm is only useful for gpt-oss shapes, or is it general for other router-sized gemms? If it is specific, we ..." (https://github.com/vllm-project/vllm/pull/37205#discussion_r2941573927)
- `2026-03-16T16:40:01Z` `inline` by `mgoin` `vllm/model_executor/models/gpt_oss.py`:194; signals: gemm, moe; excerpt: "Could this be folded into GateLinear at vllm/model executor/layers/fused moe/router/gate linear.py? This layer is already used in deepseek and nemotron models for custom router ..." (https://github.com/vllm-project/vllm/pull/37205#discussion_r2941585160)
- `2026-03-16T21:09:01Z` `inline` by `xyang16` `csrc/moe/tinygemm2.cu`:55; signals: gemm, moe; excerpt: "Fixed" (https://github.com/vllm-project/vllm/pull/37205#discussion_r2942989212)
- `2026-03-16T21:09:07Z` `inline` by `xyang16` `csrc/moe/tinygemm2.cu`:67; signals: gemm, moe; excerpt: "Fixed" (https://github.com/vllm-project/vllm/pull/37205#discussion_r2942989608)
- `2026-03-16T21:09:13Z` `inline` by `xyang16` `csrc/moe/gpt_oss_router_gemm.cuh`:50; signals: gemm, moe; excerpt: "Fixed" (https://github.com/vllm-project/vllm/pull/37205#discussion_r2942990060)
- `2026-03-16T21:09:19Z` `inline` by `xyang16` `csrc/moe/tinygemm2.cu`:117; signals: gemm, moe; excerpt: "Fixed" (https://github.com/vllm-project/vllm/pull/37205#discussion_r2942990529)
