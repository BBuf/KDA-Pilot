# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13837](https://github.com/NVIDIA/TensorRT-LLM/pull/13837)
- Source page: `sources/prs/tensorrt-llm/PR-13837.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13837`
- Generated at: `2026-05-20T15:18:55.991145+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-07T06:31:39Z`
- Merged: `2026-05-13T01:20:25Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=0
- Human participants with discussion text: JennyLiu-nv, coderabbitai, ruodil, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-07T06:39:59Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 4 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#pullrequestreview-4241661666)
- `2026-05-11T02:39:32Z` `APPROVED` by `ruodil` (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#pullrequestreview-4260446196)
- `2026-05-12T03:32:06Z` `COMMENTED` by `JennyLiu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#pullrequestreview-4268921774)
- `2026-05-12T03:32:23Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#pullrequestreview-4268922435)
- `2026-05-12T03:38:56Z` `COMMENTED` by `JennyLiu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#pullrequestreview-4268939121)
- `2026-05-12T03:39:27Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#pullrequestreview-4268940389)

## Inline Comment Hotspots

- `tests/integration/defs/examples/serve/test_serve.py`: 5 inline comment(s)
- `tests/integration/test_lists/qa/llm_spark_perf.yml`: 3 inline comment(s)

## High-Signal Discussion

- `2026-05-07T06:39:55Z` `issue` by `coderabbitai`; signals: benchmark, block, cache, cuda, cute, cutlass, dtype, fp4; excerpt: "[ Summary --- --- Model Serving Configurations tests/integration/defs/examples/serve/test configs/ New Nemotron3 Nano Omni 30B NVFP4.yml defines KV cache (block reuse disabled, 0.80 GPU memory ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#issuecomment-4394704876)
- `2026-05-07T06:39:59Z` `review` `COMMENTED` by `coderabbitai`; signals: fp4, hang, nan, nvfp4, perf; excerpt: "Actionable comments posted: 4 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#pullrequestreview-4241661666)
- `2026-05-07T06:39:58Z` `inline` by `coderabbitai` `tests/integration/test_lists/qa/llm_spark_perf.yml`:25; signals: cute, nan, perf, register, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 1304 --- 🏁 Script executed: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#discussion_r3199378253)
- `2026-05-12T03:39:27Z` `inline` by `coderabbitai` `tests/integration/test_lists/qa/llm_spark_perf.yml`:25; signals: nan, perf, register; excerpt: "@JennyLiu-nv, thanks for the correction — noted that the default max num tokens is 8192, not 2048. That said, the conclusion still holds: since ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#discussion_r3223538408)
- `2026-05-07T06:39:58Z` `inline` by `coderabbitai` `tests/integration/defs/examples/serve/test_serve.py`:253; signals: hang; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Add the required SPDX/Apache header to this modified Python file. This file is changed in the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#discussion_r3199378222)
- `2026-05-07T06:39:58Z` `inline` by `coderabbitai` `tests/integration/defs/examples/serve/test_serve.py`:580; signals: benchmark; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win Guard the optional reasoning log in the tool-calling case. reasoning content is never asserted here, but ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#discussion_r3199378233)
- `2026-05-12T03:32:23Z` `inline` by `coderabbitai` `tests/integration/defs/examples/serve/test_serve.py`:580; signals: hang; excerpt: "@JennyLiu-nv That's a fair point — if the model is expected to produce reasoning content for tool-call responses (since it reasons before deciding to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#discussion_r3223520453)
- `2026-05-12T03:38:56Z` `inline` by `JennyLiu-nv` `tests/integration/test_lists/qa/llm_spark_perf.yml`:25; signals: perf; excerpt: "actually, the default max num tokens=8192, you can check the codebase, here I enabled the chunked prefill, so no need to set this maxnt:32768" (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#discussion_r3223537059)
- `2026-05-12T05:56:35Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47864]( [ run ] completed with state SUCCESS. Commit: 0204e26 [/LLM/main/L0 MergeRequest PR pipeline 37728]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#issuecomment-4427720328)
- `2026-05-12T13:18:50Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47943]( [ run ] completed with state SUCCESS. Commit: 0204e26 [/LLM/main/L0 MergeRequest PR pipeline 37788]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#issuecomment-4430883560)
- `2026-05-13T01:20:09Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48055]( [ run ] completed with state SUCCESS. Commit: 0204e26 [/LLM/main/L0 MergeRequest PR pipeline 37889]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#issuecomment-4436273152)
- `2026-05-07T06:39:58Z` `inline` by `coderabbitai` `tests/integration/defs/examples/serve/test_serve.py`:377; signals: general review; excerpt: "⚠️ Potential issue 🟠 Major 🏗️ Heavy lift Don't make these release tests depend on public media URLs. The image/video cases now rely on ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13837#discussion_r3199378228)
