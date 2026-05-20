# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13630](https://github.com/NVIDIA/TensorRT-LLM/pull/13630)
- Source page: `sources/prs/tensorrt-llm/PR-13630.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13630`
- Generated at: `2026-05-20T15:18:49.421447+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-30T01:39:58Z`
- Merged: `2026-05-19T21:38:56Z`

## Discussion Counts

- Issue comments: 42
- Review submissions: 14 (approved=2, commented=12)
- Inline review comments: 16
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=8, outdated=3
- Human participants with discussion text: StanleySun639, bmarimuthu-nv, coderabbitai, galagam, nvchenghaoz, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-30T01:54:08Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🧹 Nitpick comments (2) examples/auto deploy/model registry/configs/gemma4 e2b.yaml (1) 7-30: 🏗️ Heavy lift Add ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4201945926)
- `2026-05-06T05:00:45Z` `COMMENTED` by `galagam` (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4233297639)
- `2026-05-06T05:02:20Z` `COMMENTED` by `galagam` (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4233305815)
- `2026-05-06T05:10:18Z` `APPROVED` by `StanleySun639` (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4233329243)
- `2026-05-06T17:57:42Z` `COMMENTED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4238221012)
- `2026-05-06T22:36:55Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4240072313)
- `2026-05-06T22:37:33Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4240074406)
- `2026-05-06T22:38:09Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4240076691)
- `2026-05-06T22:44:08Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4240098828)
- `2026-05-18T17:41:59Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4312379061)
- `2026-05-18T17:58:28Z` `APPROVED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4312436084)
- `2026-05-18T23:29:22Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4314643471)
- `2026-05-18T23:37:42Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4314675455)
- `2026-05-18T23:38:03Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4314677467)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/auto_deploy/compile/backends/torch_cudagraph.py`: 7 inline comment(s)
- `examples/auto_deploy/model_registry/configs/gemma4_e2b.yaml`: 4 inline comment(s)
- `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`: 2 inline comment(s)
- `tests/integration/defs/accuracy/references/mmlu.yaml`: 2 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_gemma3n.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-30T01:54:08Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, cute, gemm, hang, kernel, latency, perf, performance; excerpt: "Actionable comments posted: 1 🧹 Nitpick comments (2) examples/auto deploy/model registry/configs/gemma4 e2b.yaml (1) 7-30: 🏗️ Heavy lift Add a registry-level smoke test for the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#pullrequestreview-4201945926)
- `2026-04-30T01:53:49Z` `issue` by `bmarimuthu-nv`; signals: compile, cuda, cudagraph, cute, gemm, hang, tiling, triton; excerpt: "Gemma4 E2B Status Latest E2E Run Command: Result: passed with exit code 0. Key signals: - Used attn backend: triton paged. - Used compile ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#issuecomment-4349110954)
- `2026-04-30T01:54:04Z` `issue` by `coderabbitai`; signals: accuracy, attention, benchmark, cache, compile, cuda, cudagraph, cute; excerpt: "ℹ️ Recent review info ⚙️ Run configuration Configuration used : Path: .coderabbit.yaml Review profile : CHILL Plan : Enterprise Run ID : f4c0b023-6054-42c7-a89c-3ca31655d44b 📥 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#issuecomment-4349113052)
- `2026-05-06T22:44:08Z` `inline` by `bmarimuthu-nv` `tensorrt_llm/_torch/auto_deploy/compile/backends/torch_cudagraph.py`:252; signals: cache, compile, cuda, cudagraph, gemm, hang, tensorrt; excerpt: "torch-cudagraph decides clone/copy into the CUDA graph by position, but that split boundary was hard-coded: first N inputs = runtime/batched inputs everything after = ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#discussion_r3197960840)
- `2026-04-30T01:53:54Z` `issue` by `bmarimuthu-nv`; signals: compile, cuda, cudagraph, flashinfer, gemm, hang, tiling; excerpt: "Gemma3n E2B Status Latest E2E Run Command: Result: passed with exit code 0. Key signals: - Used attn backend: flashinfer. - Used compile backend: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#issuecomment-4349111647)
- `2026-05-18T17:57:03Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/compile/backends/torch_cudagraph.py`:368; signals: compile, cuda, cudagraph, tensorrt; excerpt: "dynamic extent is larger than the buffers allocated during capture Any real world example for this case? Wondering if the following code is not ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#discussion_r3260951619)
- `2026-05-18T23:29:22Z` `inline` by `bmarimuthu-nv` `tensorrt_llm/_torch/auto_deploy/compile/backends/torch_cudagraph.py`:368; signals: compile, cuda, cudagraph, tensorrt; excerpt: "Good question. This can happen when a CUDA graph input has a dynamic extent that is not the same quantity as the output extent. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#discussion_r3262765894)
- `2026-05-06T17:49:12Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/compile/backends/torch_cudagraph.py`:252; signals: compile, cuda, cudagraph, tensorrt; excerpt: "is this the reason that we need to order the kwargs in line 71?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#discussion_r3196563909)
- `2026-05-18T17:51:04Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/compile/backends/torch_cudagraph.py`:364; signals: compile, cuda, cudagraph, tensorrt; excerpt: "add a warning or should we just throw an error for this case?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#discussion_r3260918535)
- `2026-05-18T23:37:42Z` `inline` by `bmarimuthu-nv` `tensorrt_llm/_torch/auto_deploy/compile/backends/torch_cudagraph.py`:364; signals: compile, cuda, cudagraph, tensorrt; excerpt: "Done ✅ added!" (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#discussion_r3262791388)
- `2026-05-18T23:38:03Z` `inline` by `bmarimuthu-nv` `tensorrt_llm/_torch/auto_deploy/compile/backends/torch_cudagraph.py`:368; signals: compile, cuda, cudagraph, tensorrt; excerpt: "Cleaned up the redundant fallback" (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#discussion_r3262792941)
- `2026-04-30T01:54:07Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_gemma3n.py`:923; signals: cute, gemm, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 131 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13630#discussion_r3165219759)
