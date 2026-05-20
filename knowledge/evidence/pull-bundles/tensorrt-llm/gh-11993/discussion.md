# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11993](https://github.com/NVIDIA/TensorRT-LLM/pull/11993)
- Source page: `sources/prs/tensorrt-llm/PR-11993.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11993`
- Generated at: `2026-05-20T15:17:56.812221+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-06T20:37:04Z`
- Merged: `2026-03-18T22:24:03Z`

## Discussion Counts

- Issue comments: 18
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 11
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=4
- Human participants with discussion text: coderabbitai, nvchenghaoz, taylor-yb-lee, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-06T20:50:35Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 9 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#pullrequestreview-3905958550)
- `2026-03-09T18:38:10Z` `COMMENTED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#pullrequestreview-3917460799)
- `2026-03-09T18:38:40Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#pullrequestreview-3917463007)
- `2026-03-13T21:27:38Z` `APPROVED` by `taylor-yb-lee` (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#pullrequestreview-3947042904)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/auto_deploy/compile/piecewise_runner.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_attention.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/flashinfer_mla.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/triton_backend_mamba.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/utils/torch_gather_logits.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/transform/library/compile_model.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-06T20:50:35Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, block, cache, compile, correctness, cuda, cudagraph, flashinfer; excerpt: "Actionable comments posted: 9 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#pullrequestreview-3905958550)
- `2026-03-06T20:50:33Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_attention.py`:301; signals: attention, compile, cute, dtype, kernel, race, register, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 137 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#discussion_r2897806041)
- `2026-03-06T20:50:33Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/triton_backend_mamba.py`:148; signals: alignment, cute, dtype, hang, kernel, register, tensorrt, triton; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🌐 Web query: For PyTorch torch.library.custom op operators with register fake, should the fake implementation preserve ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#discussion_r2897806052)
- `2026-03-06T20:50:30Z` `issue` by `coderabbitai`; signals: attention, cache, compile, cuda, cudagraph, dtype, flashinfer, hang; excerpt: "📝 Walkthrough Walkthrough This PR implements dynamic output buffering and enhanced memory-aware pipelining for piecewise CUDA graph capture. It introduces wrapper classes for metadata ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#issuecomment-4014070747)
- `2026-03-06T20:50:33Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/flashinfer_mla.py`:539; signals: attention, cache, flashinfer, fp8, kv cache, mla, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Keep the cache cast separate from the tensors used for attention math. compressed kv flat and kpe flat are ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#discussion_r2897806053)
- `2026-03-06T20:50:33Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_attention.py`:337; signals: attention, cache, cute, tensorrt, triton; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 783 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#discussion_r2897806048)
- `2026-03-06T20:50:33Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/flashinfer_mla.py`:765; signals: compile, cute, flashinfer, mla, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 131 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#discussion_r2897806055)
- `2026-03-06T20:50:33Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/compile/piecewise_runner.py`:241; signals: compile, hang, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Warmup is still creating bucket entries. SegmentEntry() is allocated before the phase check, so the first warmup call already ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#discussion_r2897806035)
- `2026-03-06T20:50:33Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/utils/torch_gather_logits.py`:60; signals: hang, memory, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Skip the extra clone when out is present. The no-gather branch still materializes a full hidden states.clone(...), then copies ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#discussion_r2897806058)
- `2026-03-06T20:50:33Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/compile/piecewise_runner.py`:225; signals: compile, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Track dynamic buffers per wrapped op, not per runner. next dynamic out info and SegmentEntry.dynamic out buf are singletons. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#discussion_r2897806032)
- `2026-03-06T20:50:33Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/transform/library/compile_model.py`:101; signals: compile, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Don't clamp prefill buckets to the mixed-batch ceiling. Line 101 computes a mixed-batch limit, but Lines 127-135 apply it ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#discussion_r2897806064)
- `2026-03-09T18:38:40Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/compile/piecewise_runner.py`:225; signals: compile, tensorrt; excerpt: "@nvchenghaoz, confirmed — the fix is reflected in the current file. next dynamic out infos is now a Dict[int, OutputInfo] keyed by dynamic submod ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11993#discussion_r2907257025)
