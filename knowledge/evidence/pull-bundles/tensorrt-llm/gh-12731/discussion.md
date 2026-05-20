# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12731](https://github.com/NVIDIA/TensorRT-LLM/pull/12731)
- Source page: `sources/prs/tensorrt-llm/PR-12731.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12731`
- Generated at: `2026-05-20T15:18:15.680597+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-03T09:09:51Z`
- Merged: `2026-05-12T04:54:16Z`

## Discussion Counts

- Issue comments: 36
- Review submissions: 13 (approved=5, commented=8)
- Inline review comments: 16
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=9
- Human participants with discussion text: 2ez4bz, Wanli-Jiang, coderabbitai, hyukn, nv-guomingz, tensorrt-cicd, xxi-nv, zhenhuaw-me
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-03T09:22:38Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4054988290)
- `2026-04-07T13:17:46Z` `APPROVED` by `hyukn` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4068345907)
- `2026-04-08T03:48:26Z` `APPROVED` by `2ez4bz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4072632075)
- `2026-04-09T06:36:30Z` `APPROVED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4080158856)
- `2026-04-22T09:30:21Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4153584091)
- `2026-04-22T09:30:27Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4153584678)
- `2026-04-22T09:30:34Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4153585393)
- `2026-04-22T09:30:46Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4153586480)
- `2026-04-22T09:31:12Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4153588978)
- `2026-04-22T09:31:24Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4153590122)
- `2026-04-22T09:31:50Z` `COMMENTED` by `Wanli-Jiang` (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4153592541)
- `2026-05-11T02:21:50Z` `APPROVED` by `zhenhuaw-me` - VisualGen changes LGTM. (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4260402762)
- `2026-05-11T23:35:05Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4268140552)

## Inline Comment Hotspots

- `tests/unittest/_torch/models/test_nemotron_h_puzzle.py`: 6 inline comment(s)
- `tensorrt_llm/_torch/modules/mamba/ssd_combined.py`: 4 inline comment(s)
- `cpp/tensorrt_llm/kernels/noAuxTcKernels.cu`: 3 inline comment(s)
- `tensorrt_llm/_torch/models/modeling_nemotron_h.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/communication/nvlink_one_sided.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-03T09:22:38Z` `review` `COMMENTED` by `coderabbitai`; signals: block, flashinfer, hang, kernel, moe, regression, tensorrt; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#pullrequestreview-4054988290)
- `2026-04-03T09:22:34Z` `issue` by `coderabbitai`; signals: block, compile, flashinfer, hang, kernel, moe, nan, tensorrt; excerpt: "📝 Walkthrough Walkthrough The PR extends Nemotron model support with a "puzzle" variant featuring per-layer MoE configuration, refines MoE kernel dispatch conditions and workspace ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#issuecomment-4182697914)
- `2026-04-03T09:22:37Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/noAuxTcKernels.cu`:295; signals: hang, kernel, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major Keep the 8-entry kernel for low-topk Nemotron layers. This now routes topk DefaultMaxNumTopExperts. Suggested change 🤖 Prompt for AI ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#discussion_r3032148018)
- `2026-04-08T03:45:31Z` `inline` by `2ez4bz` `tensorrt_llm/_torch/modules/mamba/ssd_combined.py`:37; signals: flashinfer, kernel, tensorrt; excerpt: "Nit: get flashinfer ssd kernel?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#discussion_r3049061482)
- `2026-04-03T09:22:37Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/communication/nvlink_one_sided.py`:250; signals: moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Don't skip workspace compatibility checks on reallocation. If need alloc becomes True, the old max num tokens per rank ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#discussion_r3032148028)
- `2026-04-08T03:43:17Z` `inline` by `2ez4bz` `tensorrt_llm/_torch/models/modeling_nemotron_h.py`:734; signals: correctness, tensorrt; excerpt: "I don't think it matters other than for type analysis / correctness, but just for my understanding: we could technically have NemotronHPuzzleConfig here, right? ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#discussion_r3049055851)
- `2026-04-07T13:16:43Z` `inline` by `hyukn` `cpp/tensorrt_llm/kernels/noAuxTcKernels.cu`:292; signals: kernel, tensorrt; excerpt: "Is it confirmed that the kernel can support all the topk values between the range?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#discussion_r3045237599)
- `2026-04-08T03:45:14Z` `inline` by `2ez4bz` `tensorrt_llm/_torch/modules/mamba/ssd_combined.py`:34; signals: cache, tensorrt; excerpt: "Maybe stupid question: why not use a @functools.cache or similar mechanisms?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#discussion_r3049060797)
- `2026-04-22T09:31:12Z` `inline` by `Wanli-Jiang` `tensorrt_llm/_torch/modules/mamba/ssd_combined.py`:34; signals: cache, tensorrt; excerpt: "switch to use @functools.cache" (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#discussion_r3122958376)
- `2026-04-22T09:31:50Z` `inline` by `Wanli-Jiang` `cpp/tensorrt_llm/kernels/noAuxTcKernels.cu`:292; signals: kernel, tensorrt; excerpt: "it can support. and another PR is handling the cases." (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#discussion_r3122961833)
- `2026-04-08T03:47:29Z` `inline` by `2ez4bz` `tests/unittest/_torch/models/test_nemotron_h_puzzle.py`:46; signals: block; excerpt: "Nit: block configs." (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#discussion_r3049067032)
- `2026-04-22T09:30:46Z` `inline` by `Wanli-Jiang` `tensorrt_llm/_torch/modules/mamba/ssd_combined.py`:37; signals: tensorrt; excerpt: "done" (https://github.com/NVIDIA/TensorRT-LLM/pull/12731#discussion_r3122955867)
