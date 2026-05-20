# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12664](https://github.com/NVIDIA/TensorRT-LLM/pull/12664)
- Source page: `sources/prs/tensorrt-llm/PR-12664.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12664`
- Generated at: `2026-05-20T15:18:15.653072+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-01T17:52:45Z`
- Merged: `2026-04-08T17:54:48Z`

## Discussion Counts

- Issue comments: 29
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 16
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=7
- Human participants with discussion text: coderabbitai, nvchenghaoz, suyoggupta, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-01T17:58:20Z` `COMMENTED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#pullrequestreview-4045986985)
- `2026-04-01T18:07:55Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 4 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#pullrequestreview-4046054518)
- `2026-04-01T20:27:38Z` `COMMENTED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#pullrequestreview-4046877250)
- `2026-04-01T20:28:10Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#pullrequestreview-4046879763)
- `2026-04-01T20:28:45Z` `COMMENTED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#pullrequestreview-4046882478)
- `2026-04-01T20:28:59Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#pullrequestreview-4046883735)
- `2026-04-01T20:35:57Z` `COMMENTED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#pullrequestreview-4046916605)
- `2026-04-01T20:36:17Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#pullrequestreview-4046918103)
- `2026-04-01T20:45:41Z` `COMMENTED` by `suyoggupta` (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#pullrequestreview-4046961146)
- `2026-04-01T21:04:18Z` `COMMENTED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#pullrequestreview-4047075971)
- `2026-04-01T21:11:07Z` `APPROVED` by `suyoggupta` - Approving to unblock. Please add a smoke test (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#pullrequestreview-4047116471)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/triton_mla.py`: 7 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/torch_backend_mla.py`: 4 inline comment(s)
- `tests/unittest/auto_deploy/singlegpu/custom_ops/mla/test_triton_mla_op.py`: 3 inline comment(s)
- `examples/auto_deploy/model_registry/configs/mistral_small_4_119b.yaml`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-01T17:54:38Z` `issue` by `coderabbitai`; signals: attention, cache, cuda, cudagraph, hang, kernel, mla, tensorrt; excerpt: "📝 Walkthrough Walkthrough This PR introduces a new Triton-based MLA (Multi-Head Latent Attention) backend alongside modifications to the existing torch-based implementation. Changes include: a ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#issuecomment-4171935381)
- `2026-04-01T18:07:54Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/triton_mla.py`:869; signals: cache, cute, mla, perf, race, tensorrt, triton; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 233 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#discussion_r3023750705)
- `2026-04-01T18:07:54Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/torch_backend_mla.py`:325; signals: benchmark, cache, cute, mla, register, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 132 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#discussion_r3023750686)
- `2026-04-01T18:07:54Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/triton_mla.py`:806; signals: block, cuda, cute, mla, tensorrt, triton; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 118 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#discussion_r3023750699)
- `2026-04-01T18:07:54Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/triton_mla.py`:578; signals: block, kernel, mla, tensorrt, triton; excerpt: "⚠️ Potential issue 🟠 Major Don't floor-divide away tail heads. head block = min(head block, num heads) only fixes the zero-grid case. Every num ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#discussion_r3023750697)
- `2026-04-01T18:07:55Z` `review` `COMMENTED` by `coderabbitai`; signals: hang, mla, tensorrt, triton; excerpt: "Actionable comments posted: 4 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#pullrequestreview-4046054518)
- `2026-04-01T20:36:17Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/triton_mla.py`:806; signals: cuda, mla, tensorrt, triton; excerpt: "@nvchenghaoz, glad it was helpful! Eliminating that D2H sync keeps the multi-sequence prefill path fully CUDA graph-compatible. Thanks for addressing it! 🎉 --- 🧠 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#discussion_r3024512906)
- `2026-04-01T20:45:41Z` `inline` by `suyoggupta` `examples/auto_deploy/model_registry/configs/mistral_small_4_119b.yaml`:12; signals: blackwell, flashinfer, hopper, triton; excerpt: "I think we need triton backend for hopper since flashinfer works for blackwell" (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#discussion_r3024554480)
- `2026-04-01T20:28:10Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/torch_backend_mla.py`:325; signals: cache, mla, tensorrt; excerpt: "@nvchenghaoz, thanks for the update! Restoring mutates args=("mla cache",) ensures PyTorch's export and functionalization systems correctly track the in-place writes to mla cache made ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#discussion_r3024475818)
- `2026-04-01T20:28:44Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/triton_mla.py`:578; signals: mla, tensorrt, triton; excerpt: "NAB, WNF" (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#discussion_r3024478379)
- `2026-04-01T20:28:59Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/triton_mla.py`:578; signals: mla, tensorrt, triton; excerpt: "@nvchenghaoz, understood — acknowledged and moving on. 😿 --- 🧠 Learnings used --- ---" (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#discussion_r3024479597)
- `2026-04-01T20:35:56Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/triton_mla.py`:806; signals: mla, tensorrt, triton; excerpt: "addressed, good point" (https://github.com/NVIDIA/TensorRT-LLM/pull/12664#discussion_r3024511407)
