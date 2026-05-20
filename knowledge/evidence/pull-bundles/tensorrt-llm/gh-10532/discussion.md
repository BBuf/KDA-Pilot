# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#10532](https://github.com/NVIDIA/TensorRT-LLM/pull/10532)
- Source page: `sources/prs/tensorrt-llm/PR-10532.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-10532`
- Generated at: `2026-05-20T15:17:39.901236+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-08T05:34:08Z`
- Merged: `2026-01-14T09:38:59Z`

## Discussion Counts

- Issue comments: 53
- Review submissions: 19 (approved=3, commented=16)
- Inline review comments: 19
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=7
- Human participants with discussion text: coderabbitai, jmydurant, symphonylyh, tensorrt-cicd, xxi-nv, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-08T05:43:22Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Fix all issues with AI agents 🧹 Nitpick comments (3) tensorrt llm/ torch/modules/fused ... (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3637772081)
- `2026-01-09T06:45:17Z` `APPROVED` by `xxi-nv` - Overall looks good to me. (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3642568817)
- `2026-01-09T08:59:43Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3642992612)
- `2026-01-09T09:01:44Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3643000284)
- `2026-01-09T22:56:08Z` `APPROVED` by `symphonylyh` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3645818085)
- `2026-01-11T06:55:20Z` `COMMENTED` by `jmydurant` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3647461406)
- `2026-01-11T06:55:25Z` `COMMENTED` by `jmydurant` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3647461431)
- `2026-01-11T06:55:29Z` `COMMENTED` by `jmydurant` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3647461450)
- `2026-01-11T06:55:36Z` `COMMENTED` by `jmydurant` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3647461493)
- `2026-01-11T06:55:41Z` `COMMENTED` by `jmydurant` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3647461520)
- `2026-01-12T06:25:43Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3649312015)
- `2026-01-12T06:27:41Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3649316131)
- `2026-01-12T06:28:31Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3649317693)
- `2026-01-12T06:29:40Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3649319777)
- `2026-01-12T08:27:10Z` `COMMENTED` by `jmydurant` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3649601830)
- `2026-01-12T08:27:31Z` `COMMENTED` by `jmydurant` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3649603052)
- `2026-01-12T08:27:43Z` `COMMENTED` by `jmydurant` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3649603852)
- `2026-01-12T08:29:04Z` `COMMENTED` by `jmydurant` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3649608232)
- `2026-01-12T09:13:31Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3649783679)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/models/modeling_minimaxm2.py`: 17 inline comment(s)
- `tests/integration/test_lists/test-db/l0_dgx_h100.yml`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-08T05:43:22Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, attention, benchmark, block, cuda, dtype, flashinfer, fp8; excerpt: "Actionable comments posted: 1 🤖 Fix all issues with AI agents 🧹 Nitpick comments (3) tensorrt llm/ torch/modules/fused moe/routing.py (2) 372-386: Unused num experts ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#pullrequestreview-3637772081)
- `2026-01-08T05:43:18Z` `issue` by `coderabbitai`; signals: accuracy, attention, benchmark, block, dtype, fp8, hang, kernel; excerpt: "📝 Walkthrough Walkthrough This pull request introduces MiniMax M2 model support with mixture-of-experts (MoE) routing across kernel, Python model, and testing infrastructure. Changes include ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#issuecomment-3722056668)
- `2026-01-09T09:01:44Z` `inline` by `yuxianq` `tensorrt_llm/_torch/models/modeling_minimaxm2.py`:129; signals: dtype, gemm, tensorrt; excerpt: "All of pos embd params/skip rope/fuse qk norm rope/dtype/use gemma rms norm/is qk norm are unsued, please remove them and all related code." (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#discussion_r2675383101)
- `2026-01-09T06:22:54Z` `inline` by `xxi-nv` `tests/integration/test_lists/test-db/l0_dgx_h100.yml`:97; signals: b200, h100, hopper; excerpt: "It seems that you should add the test case to GB200 instead of Hopper." (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#discussion_r2675000822)
- `2026-01-09T06:43:32Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/models/modeling_minimaxm2.py`:79; signals: dtype, tensorrt; excerpt: "num experts, hidden size, intermediate size, dtype is not mandatory, you can input the model config instead. These parameters will be replaced by model ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#discussion_r2675042251)
- `2026-01-09T08:59:42Z` `inline` by `yuxianq` `tensorrt_llm/_torch/models/modeling_minimaxm2.py`:244; signals: attention, tensorrt; excerpt: "It seems that the fuse qk norm rope=True path is unused, please remove all code in this branch (including apply qk norm rope) to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#discussion_r2675376787)
- `2026-01-08T05:43:21Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/models/modeling_minimaxm2.py`:19; signals: tensorrt; excerpt: "🛠️ Refactor suggestion 🟠 Major Add NVIDIA SPDX copyright header This new source file is missing the standard NVIDIA SPDX header required for TensorRT‑LLM ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#discussion_r2670947269)
- `2026-01-11T06:55:20Z` `inline` by `jmydurant` `tests/integration/test_lists/test-db/l0_dgx_h100.yml`:97; signals: h100; excerpt: "Done" (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#discussion_r2679286199)
- `2026-01-11T06:55:25Z` `inline` by `jmydurant` `tensorrt_llm/_torch/models/modeling_minimaxm2.py`:1; signals: tensorrt; excerpt: "Done" (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#discussion_r2679286269)
- `2026-01-11T06:55:28Z` `inline` by `jmydurant` `tensorrt_llm/_torch/models/modeling_minimaxm2.py`:79; signals: tensorrt; excerpt: "Done" (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#discussion_r2679286299)
- `2026-01-11T06:55:35Z` `inline` by `jmydurant` `tensorrt_llm/_torch/models/modeling_minimaxm2.py`:244; signals: tensorrt; excerpt: "Done" (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#discussion_r2679286347)
- `2026-01-11T06:55:41Z` `inline` by `jmydurant` `tensorrt_llm/_torch/models/modeling_minimaxm2.py`:129; signals: tensorrt; excerpt: "Done" (https://github.com/NVIDIA/TensorRT-LLM/pull/10532#discussion_r2679286385)
