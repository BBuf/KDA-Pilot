# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13219](https://github.com/NVIDIA/TensorRT-LLM/pull/13219)
- Source page: `sources/prs/tensorrt-llm/PR-13219.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13219`
- Generated at: `2026-05-20T15:18:34.850106+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-20T11:51:22Z`
- Merged: `2026-05-09T04:03:37Z`

## Discussion Counts

- Issue comments: 87
- Review submissions: 42 (approved=3, commented=39)
- Inline review comments: 51
- Review threads observed: 21
- Resolved/outdated thread markers: resolved=21, outdated=15
- Human participants with discussion text: Superjomn, coderabbitai, hyukn, limin2021, tburt-nv, tensorrt-cicd, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-20T12:00:40Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 5 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4139705785)
- `2026-04-21T04:34:15Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4145039651)
- `2026-04-21T04:35:14Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4145042162)
- `2026-04-21T04:36:50Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4145046319)
- `2026-04-21T04:37:01Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4145046845)
- `2026-04-21T04:37:06Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4145047045)
- `2026-04-21T04:37:14Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4145047391)
- `2026-04-21T04:37:22Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4145047811)
- `2026-04-21T04:38:23Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4145051807)
- `2026-04-21T04:52:22Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4145105552)
- `2026-04-21T04:53:11Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4145108736)
- `2026-04-21T09:02:25Z` `APPROVED` by `Superjomn` - LGTM on the llmapi changes (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4146416310)
- `2026-04-21T09:52:08Z` `APPROVED` by `hyukn` - Overall LGTM. Some code cleanup is required. (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4146677551)
- `2026-04-21T10:50:18Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4147069661)
- `2026-04-21T10:51:10Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4147074078)
- `2026-04-21T10:57:26Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4147106698)
- `2026-04-21T16:17:09Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4149249178)
- `2026-04-21T16:17:16Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4149249815)
- `2026-04-22T08:03:24Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4152982128)
- `2026-04-22T08:16:29Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4153057991)
- `2026-04-22T08:36:12Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4153171037)
- `2026-04-22T09:00:16Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4153376250)
- `2026-04-22T09:07:48Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4152998495)
- `2026-04-22T09:09:25Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4153454703)
- ... 18 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/fp8_paged_mqa_logits.py`: 20 inline comment(s)
- `tests/unittest/_torch/attention/sparse/test_cute_dsl_fp8_paged_mqa_logits.py`: 13 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 8 inline comment(s)
- `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`: 7 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/__init__.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-04-20T12:00:37Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:5288; signals: benchmark, correctness, cuda, cute, kernel, latency, perf, performance; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🌐 Web query: In PyTorch custom CUDA operators, if input tensors are produced on torch.cuda.current stream(), ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#discussion_r3110445771)
- `2026-04-22T09:47:39Z` `inline` by `yuxianq` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/fp8_paged_mqa_logits.py`:574; signals: blackwell, cuda, cute, fp8, kernel, latency, memory, tensorrt; excerpt: "Speculative mContextLens[batch size] OOB read for zero-work CTAs Every CTA unconditionally issues during the prologue for latency hiding, before checking has work. For CTAs ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#discussion_r3123049372)
- `2026-04-20T12:00:40Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, blackwell, cute, fp8, hang, kernel, tensorrt; excerpt: "Actionable comments posted: 5 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#pullrequestreview-4139705785)
- `2026-04-20T12:00:34Z` `issue` by `coderabbitai`; signals: attention, b200, benchmark, blackwell, correctness, cute, deepgemm, dtype; excerpt: "📝 Walkthrough Walkthrough This change introduces a new CuTE DSL-based FP8 paged MQA logits kernel for SM100+ GPUs as an alternative to the existing ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#issuecomment-4280481878)
- `2026-04-20T12:00:38Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/__init__.py`:16; signals: benchmark, blackwell, cute, fp8, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Make the re-export explicit with all . Line 16 is a public re-export pattern, but without all this triggers ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#discussion_r3110445819)
- `2026-04-20T12:00:38Z` `inline` by `coderabbitai` `tests/unittest/_torch/attention/sparse/test_cute_dsl_fp8_paged_mqa_logits.py`:187; signals: attention, cute, deepgemm, fp8, gemm, kernel; excerpt: "⚠️ Potential issue 🟠 Major Don’t skip this test when DeepGEMM is missing. The file already has a pure PyTorch fallback reference, so gating ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#discussion_r3110445831)
- `2026-04-21T04:34:14Z` `inline` by `limin2021` `tests/unittest/_torch/attention/sparse/test_cute_dsl_fp8_paged_mqa_logits.py`:187; signals: attention, cute, fp8, gemm, kernel, tensorrt; excerpt: "The has deep gemm() check is intentional here. While the reference path does fall back to pure PyTorch, line 216 unconditionally calls from tensorrt ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#discussion_r3115042498)
- `2026-04-21T04:35:14Z` `inline` by `coderabbitai` `tests/unittest/_torch/attention/sparse/test_cute_dsl_fp8_paged_mqa_logits.py`:187; signals: attention, cute, deepgemm, fp8, gemm, kernel; excerpt: "🧩 Analysis chain 🏁 Script executed: Length of output: 1957 --- @limin2021, you're right — I missed that. The get paged mqa logits metadata ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#discussion_r3115044985)
- `2026-04-21T04:53:11Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:1117; signals: attention, block, cute, fp8, hang, tensorrt; excerpt: "🧩 Analysis chain 🏁 Script executed: Length of output: 809 --- 🏁 Script executed: Length of output: 1686 --- @limin2021 The fix doesn't appear ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#discussion_r3115108894)
- `2026-04-22T08:36:12Z` `inline` by `yuxianq` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/fp8_paged_mqa_logits.py`:2060; signals: accuracy, blackwell, cute, fp8, kernel, tensorrt; excerpt: "Cannot find paged mqa logits helpers, is run test broken? Our CI cannot cover run test/main/dsl fp8 paged mqa logits dg fullk in this ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#discussion_r3122601511)
- `2026-04-22T09:09:53Z` `inline` by `yuxianq` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/fp8_paged_mqa_logits.py`:219; signals: blackwell, cute, fp8, kernel, tensorrt, tile; excerpt: "Should we also check self.num heads % 4 != 0 when num epi subtiles == 1?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#discussion_r3122836951)
- `2026-04-20T12:00:37Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:1117; signals: attention, cute, fp8, register, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 4646 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13219#discussion_r3110445762)
