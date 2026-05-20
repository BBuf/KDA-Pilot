# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12427](https://github.com/NVIDIA/TensorRT-LLM/pull/12427)
- Source page: `sources/prs/tensorrt-llm/PR-12427.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12427`
- Generated at: `2026-05-20T15:18:08.018162+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-22T01:36:28Z`
- Merged: `2026-04-04T21:53:16Z`

## Discussion Counts

- Issue comments: 47
- Review submissions: 12 (approved=4, commented=8)
- Inline review comments: 28
- Review threads observed: 23
- Resolved/outdated thread markers: resolved=23, outdated=13
- Human participants with discussion text: bmarimuthu-nv, coderabbitai, galagam, juney-nvidia, lucaslie, ruodil, suyoggupta, taylor-yb-lee, tensorrt-cicd, yuanjingx87
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-22T08:49:08Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 10 🧹 Nitpick comments (3) tensorrt llm/ torch/auto deploy/mlir/fusion/subgraph discovery.py (1) 168-168: Drop the unused ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#pullrequestreview-3987915546)
- `2026-03-23T12:17:25Z` `COMMENTED` by `galagam` - That's one impressive PR. I'm a bit concerned about enabling mlir elementwise fusion in the default config - ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#pullrequestreview-3991156407)
- `2026-03-23T12:20:02Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#pullrequestreview-3991332689)
- `2026-03-31T00:16:00Z` `APPROVED` by `juney-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#pullrequestreview-4033938164)
- `2026-03-31T01:52:29Z` `APPROVED` by `yuanjingx87` - Running license scanning, no risky license involved, LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#pullrequestreview-4034163225)
- `2026-03-31T20:31:24Z` `APPROVED` by `lucaslie` - Happy to approve the PR so we can test this system in practice. That being said, I'd love ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#pullrequestreview-4039919478)
- `2026-03-31T22:27:24Z` `COMMENTED` by `taylor-yb-lee` (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#pullrequestreview-4040554874)
- `2026-03-31T23:32:31Z` `COMMENTED` by `taylor-yb-lee` (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#pullrequestreview-4040823169)
- `2026-03-31T23:55:58Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#pullrequestreview-4040901263)
- `2026-04-01T02:46:41Z` `COMMENTED` by `suyoggupta` (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#pullrequestreview-4041352566)
- `2026-04-01T02:50:52Z` `COMMENTED` by `taylor-yb-lee` (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#pullrequestreview-4041374646)
- `2026-04-03T01:47:22Z` `APPROVED` by `ruodil` (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#pullrequestreview-4053903363)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/auto_deploy/mlir/codegen/triton_emitter.py`: 9 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/mlir/dialect.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/mlir/fx_to_mlir.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/mlir/fusion/subgraph_replace.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/mlir/fusion/subgraph_discovery.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/mlir/__init__.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/mlir/codegen/kernel_cache.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/mlir/mlir_to_fx.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/transform/library/mlir_elementwise_fusion.py`: 1 inline comment(s)
- `tests/unittest/auto_deploy/singlegpu/mlir/test_dialect.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/config/default.yaml`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/mlir/agent_learnings.md`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-22T08:49:02Z` `issue` by `coderabbitai`; signals: cache, correctness, dtype, fp8, hang, kernel, pipeline, register; excerpt: "📝 Walkthrough Walkthrough This PR introduces MLIR-based transformation and code generation infrastructure to TensorRT-LLM's auto-deploy module, including dialect definitions, FX-to-MLIR and MLIR-to-FX converters, decomposition ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#issuecomment-4105829637)
- `2026-03-22T08:49:08Z` `review` `COMMENTED` by `coderabbitai`; signals: cache, hang, kernel, register, tensorrt, triton; excerpt: "Actionable comments posted: 10 🧹 Nitpick comments (3) tensorrt llm/ torch/auto deploy/mlir/fusion/subgraph discovery.py (1) 168-168: Drop the unused gid loop variable. Iterating groups.values() (or ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#pullrequestreview-3987915546)
- `2026-03-30T21:58:43Z` `issue` by `coderabbitai`; signals: benchmark, hang, perf, performance, pipeline, regression, throughput; excerpt: "[!TIP] For best results, initiate chat on the files or code changes. The PR description image shows a "User TPS vs Output TPS by ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#issuecomment-4158429928)
- `2026-03-30T22:05:19Z` `issue` by `coderabbitai`; signals: block, cute, failing, flashinfer, hang, register, triton; excerpt: "[!TIP] For best results, initiate chat on the files or code changes. 🧩 Analysis chain 🏁 Script executed: Length of output: 126443 --- @suyoggupta ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#issuecomment-4158456821)
- `2026-03-24T02:06:29Z` `issue` by `suyoggupta`; signals: cache, dtype, fp8, kernel, register, triton; excerpt: "Thanks for the thorough review @coderabbitai and @galagam! Addressed the critical/major CodeRabbit comments in the latest commit: mlir/ init .py — Restructured to try/except/else ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#issuecomment-4114879794)
- `2026-03-22T08:49:06Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/mlir/codegen/triton_emitter.py`:135; signals: cache, kernel, register, tensorrt, triton; excerpt: "⚠️ Potential issue 🔴 Critical Include codegen attributes in the kernel cache key. KernelCache.hash subgraph() only fingerprints op names, operand connectivity, and result types, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#discussion_r2971265917)
- `2026-03-23T11:50:17Z` `inline` by `galagam` `tensorrt_llm/_torch/auto_deploy/mlir/codegen/triton_emitter.py`:291; signals: bf16, kernel, perf, tensorrt, triton; excerpt: "Surely not all hand-written kernels use f32 compute... We need f16/bf16 compute for better perf." (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#discussion_r2974551159)
- `2026-03-24T02:07:21Z` `issue` by `coderabbitai`; signals: cache, dtype, hang, kernel, triton; excerpt: "[!TIP] For best results, initiate chat on the files or code changes. @suyoggupta Thanks for the detailed summary — the fixes look comprehensive and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#issuecomment-4114882334)
- `2026-03-31T03:10:57Z` `issue` by `coderabbitai`; signals: cute, flashinfer, hang, register, triton; excerpt: "[!TIP] For best results, initiate chat on the files or code changes. 🧩 Analysis chain 🏁 Script executed: Length of output: 14787 --- @suyoggupta ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#issuecomment-4159554302)
- `2026-03-22T08:49:05Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/mlir/__init__.py`:47; signals: block, cute, hang, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 297 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#discussion_r2971265911)
- `2026-03-22T08:49:06Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/mlir/codegen/triton_emitter.py`:316; signals: dtype, register, tensorrt, triton; excerpt: "⚠️ Potential issue 🟠 Major Allocate outputs from each MLIR result dtype, not ref.dtype. Both the runtime launcher and register fake allocate every output ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#discussion_r2971265919)
- `2026-03-23T11:43:16Z` `inline` by `galagam` `tensorrt_llm/_torch/auto_deploy/mlir/codegen/triton_emitter.py`:135; signals: cache, kernel, tensorrt, triton; excerpt: "Maintaining two separate caches is confusing and error-prone. Consider: 1. Init session cache kernel cache from persistent cache generated op cache 2. During session, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12427#discussion_r2974520302)
