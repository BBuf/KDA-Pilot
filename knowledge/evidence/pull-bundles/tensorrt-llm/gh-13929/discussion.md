# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13929](https://github.com/NVIDIA/TensorRT-LLM/pull/13929)
- Source page: `sources/prs/tensorrt-llm/PR-13929.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13929`
- Generated at: `2026-05-20T15:18:58.018453+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-09T04:26:43Z`
- Merged: `2026-05-14T05:12:50Z`

## Discussion Counts

- Issue comments: 34
- Review submissions: 18 (approved=4, commented=14)
- Inline review comments: 18
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=6
- Human participants with discussion text: coderabbitai, hyukn, lfr-0531, limin2021, litaotju, tensorrt-cicd, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-09T04:39:23Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 🧹 Nitpick comments (2) tests/unittest/ torch/attention/sparse/test cute dsl fp4 paged mqa logits.py (2) 441-479: ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4256810681)
- `2026-05-12T04:00:23Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4269015141)
- `2026-05-12T04:01:52Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4269020436)
- `2026-05-12T09:35:21Z` `APPROVED` by `hyukn` - Overall LGTM. Btw: I am not sure if a 6000-line cute dsl custom ops.py is proper. Should we ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4270971088)
- `2026-05-12T11:27:51Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4271793064)
- `2026-05-12T11:27:54Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4271793518)
- `2026-05-12T11:29:22Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4271805226)
- `2026-05-12T12:33:47Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4272268760)
- `2026-05-13T01:05:46Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4277385016)
- `2026-05-13T01:11:43Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4277415271)
- `2026-05-13T01:24:00Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4277475537)
- `2026-05-13T02:28:49Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4277759958)
- `2026-05-13T06:51:37Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4279056259)
- `2026-05-13T06:51:44Z` `COMMENTED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4279057165)
- `2026-05-13T06:55:19Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4279079628)
- `2026-05-13T06:57:01Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4279090810)
- `2026-05-13T07:00:50Z` `APPROVED` by `litaotju` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4279118040)
- `2026-05-13T08:35:32Z` `APPROVED` by `lfr-0531` (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4279810930)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 4 inline comment(s)
- `tests/unittest/_torch/attention/sparse/test_cute_dsl_fp4_paged_mqa_logits.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/fp4_paged_mqa_logits.py`: 2 inline comment(s)
- `tests/integration/defs/accuracy/test_llm_api_pytorch.py`: 2 inline comment(s)
- `tests/scripts/cute_dsl_kernels/paged_mqa_logits/run_fp4.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-09T04:39:23Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, attention, blackwell, cache, cute, fp4, hang, kernel; excerpt: "Actionable comments posted: 3 🧹 Nitpick comments (2) tests/unittest/ torch/attention/sparse/test cute dsl fp4 paged mqa logits.py (2) 441-479: ⚡ Quick win Gate verbose accuracy ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#pullrequestreview-4256810681)
- `2026-05-09T04:34:34Z` `issue` by `coderabbitai`; signals: aligned, alignment, attention, blackwell, block, cache, compile, cute; excerpt: "📝 Walkthrough Walkthrough This PR adds two PyTorch custom op implementations of paged MQA logits computation for Blackwell SM100: one for FP8-quantized queries and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#issuecomment-4411451730)
- `2026-05-09T04:39:22Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:6780; signals: block, cute, dtype, failing, fp4, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Validate FP4 paged-MQA shapes before the reshapes. CuteDSLFP4PagedMQALogitsRunner.forward() later reinterprets q, sf q, and weights as ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#discussion_r3212461318)
- `2026-05-09T04:39:22Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:6986; signals: benchmark, cache, cute, kernel, tensorrt, tile; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win Reject unsupported num epi subtiles values at the API boundary. The docstring constrains num epi subtiles ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#discussion_r3212461320)
- `2026-05-12T09:31:12Z` `inline` by `hyukn` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/fp4_paged_mqa_logits.py`:35; signals: blackwell, cute, fp4, kernel, tensorrt; excerpt: "Maybe we should replace this with an English phrase?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#discussion_r3225274142)
- `2026-05-12T11:29:21Z` `inline` by `limin2021` `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/fp4_paged_mqa_logits.py`:35; signals: blackwell, cute, fp4, kernel, tensorrt; excerpt: "done." (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#discussion_r3225993990)
- `2026-05-09T04:39:22Z` `inline` by `coderabbitai` `tests/unittest/_torch/attention/sparse/test_cute_dsl_fp4_paged_mqa_logits.py`:204; signals: attention, block, cute, fp4; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win Remove unused unpacked variables in ref paged mqa logits. num heads and num block are unpacked ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#discussion_r3212461321)
- `2026-05-13T01:05:46Z` `inline` by `yuxianq` `tests/integration/defs/accuracy/test_llm_api_pytorch.py`:3569; signals: accuracy, b200, fp4, nvfp4; excerpt: "We have not added these new tests to any test list, please add them to the same test list of accuracy/test llm api pytorch.py::TestDeepSeekV32::test ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#discussion_r3230792190)
- `2026-05-13T01:24:00Z` `inline` by `limin2021` `tests/unittest/_torch/attention/sparse/test_cute_dsl_fp4_paged_mqa_logits.py`:265; signals: attention, cute, dtype, fp4; excerpt: "(torch.float32, torch.bfloat16) is the production dtype. For other dtypes, will open/enable it when e2e precision test is ok." (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#discussion_r3230860572)
- `2026-05-13T01:11:43Z` `inline` by `yuxianq` `tests/unittest/_torch/attention/sparse/test_cute_dsl_fp4_paged_mqa_logits.py`:265; signals: attention, cute, fp4; excerpt: "Why do we comment out these configs?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#discussion_r3230812794)
- `2026-05-13T02:28:49Z` `inline` by `yuxianq` `tests/scripts/cute_dsl_kernels/paged_mqa_logits/run_fp4.py`:160; signals: cute, fp4, kernel; excerpt: "It seems that seq offset is always 0, can we remove it?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#discussion_r3231094085)
- `2026-05-13T06:51:44Z` `inline` by `limin2021` `tests/scripts/cute_dsl_kernels/paged_mqa_logits/run_fp4.py`:160; signals: cute, fp4, kernel; excerpt: "removed." (https://github.com/NVIDIA/TensorRT-LLM/pull/13929#discussion_r3232097956)
