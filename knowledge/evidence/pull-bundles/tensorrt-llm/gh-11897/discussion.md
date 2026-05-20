# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11897](https://github.com/NVIDIA/TensorRT-LLM/pull/11897)
- Source page: `sources/prs/tensorrt-llm/PR-11897.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11897`
- Generated at: `2026-05-20T15:17:52.973809+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete via REST overflow fallback`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-04T06:49:30Z`
- Merged: `2026-05-07T02:40:52Z`

## Discussion Counts

- Issue comments: 120
- Review submissions: 9 (approved=6, commented=3)
- Inline review comments: 11
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=4
- Human participants with discussion text: LarryXFly, QiJune, StanleySun639, coderabbitai, liji-nv, peaceh-nv, tburt-nv, tensorrt-cicd, zongfeijing
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-04T06:58:40Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 7 🧹 Nitpick comments (4) tensorrt llm/ torch/custom ops/ init .py (1) 38-41: Use module ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#pullrequestreview-3887535443)
- `2026-03-13T09:28:58Z` `APPROVED` by `StanleySun639` (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#pullrequestreview-3942727232)
- `2026-03-23T05:55:38Z` `COMMENTED` by `peaceh-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#pullrequestreview-3989497149)
- `2026-03-25T01:25:33Z` `APPROVED` by `LarryXFly` (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#pullrequestreview-4003371713)
- `2026-04-01T04:48:22Z` `APPROVED` by `zongfeijing` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#pullrequestreview-4041644609)
- `2026-04-10T01:19:48Z` `APPROVED` by `QiJune` (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#pullrequestreview-4086506413)
- `2026-04-13T08:46:52Z` `APPROVED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#pullrequestreview-4097333775)
- `2026-04-14T08:57:52Z` `COMMENTED` by `peaceh-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#pullrequestreview-4104618083)
- `2026-04-21T17:52:12Z` `APPROVED` by `tburt-nv` - I'm not sure what file triggered the trt-llm-oss-compliance review requirement, but I don't see any dependency changes here, ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#pullrequestreview-4149788549)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 2 inline comment(s)
- `tests/scripts/cute_dsl_kernels/run_custom_op_dense_gemm_swiglu.py`: 2 inline comment(s)
- `tests/integration/test_lists/test-db/l0_b200.yml`: 2 inline comment(s)
- `tests/integration/defs/accuracy/test_llm_api_pytorch.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/gated_mlp.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/modules/linear.py`: 1 inline comment(s)
- `tests/scripts/cute_dsl_kernels/run_dense_blockscaled_gemm_swiglu_fusion.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-04T06:58:40Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, blackwell, block, cache, cute, gemm, hang, kernel; excerpt: "Actionable comments posted: 7 🧹 Nitpick comments (4) tensorrt llm/ torch/custom ops/ init .py (1) 38-41: Use module import style in this new CuTe ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#pullrequestreview-3887535443)
- `2026-03-04T06:58:38Z` `inline` by `coderabbitai` `tests/scripts/cute_dsl_kernels/run_custom_op_dense_gemm_swiglu.py`:310; signals: bf16, cute, fp4, gemm, kernel; excerpt: "⚠️ Potential issue 🟠 Major FP4 output test can pass even with an invalid output width. At Line 304-Line 306, or fp4 out.shape[0] == ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#discussion_r2882156817)
- `2026-03-04T06:58:38Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/linear.py`:1773; signals: alignment, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 45 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#discussion_r2882156804)
- `2026-03-04T06:58:38Z` `inline` by `coderabbitai` `tests/scripts/cute_dsl_kernels/run_custom_op_dense_gemm_swiglu.py`:349; signals: benchmark, cute, gemm, kernel; excerpt: "⚠️ Potential issue 🟡 Minor Avoid broad exception catching in the size sweep loop. Line 347 catches Exception, which can hide unexpected errors and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#discussion_r2882156827)
- `2026-03-04T06:58:38Z` `inline` by `coderabbitai` `tests/scripts/cute_dsl_kernels/run_dense_blockscaled_gemm_swiglu_fusion.py`:688; signals: block, cute, gemm, kernel; excerpt: "⚠️ Potential issue 🟡 Minor Chain the exception to preserve context. When re-raising as a different exception type, use raise ... from err to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#discussion_r2882156837)
- `2026-03-04T06:58:37Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:1475; signals: benchmark, cute, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Remove extraneous f prefix from string literal. Same issue as line 1097 — the f-string has no placeholders. 🐛 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#discussion_r2882156791)
- `2026-03-04T06:58:37Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:1137; signals: cute, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Remove extraneous f prefix from string literal. The f-string has no placeholders, making the f prefix unnecessary. 🐛 Fix ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#discussion_r2882156784)
- `2026-03-04T06:58:38Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/gated_mlp.py`:187; signals: fp4, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Guard FP4-out fusion when down proj.pre quant scale is set. At Line 172-Line 180, the FP4-out eligibility check is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#discussion_r2882156802)
- `2026-04-13T08:25:05Z` `inline` by `liji-nv` `tests/integration/defs/accuracy/test_llm_api_pytorch.py`:2139; signals: accuracy, compile; excerpt: "Why not test with torch compile?" (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#discussion_r3071720660)
- `2026-04-14T08:57:52Z` `inline` by `peaceh-nv` `tests/integration/defs/accuracy/test_llm_api_pytorch.py`:2139; signals: accuracy, compile; excerpt: "Add torch compile test in the latest commit." (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#discussion_r3078267675)
- `2026-03-13T09:28:54Z` `inline` by `StanleySun639` `tests/integration/test_lists/test-db/l0_b200.yml`:42; signals: b200; excerpt: "Could you add new test cases in QA test [list]( also? Thanks!" (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#discussion_r2930054705)
- `2026-03-23T05:55:38Z` `inline` by `peaceh-nv` `tests/integration/test_lists/test-db/l0_b200.yml`:42; signals: b200; excerpt: "Done" (https://github.com/NVIDIA/TensorRT-LLM/pull/11897#discussion_r2973017427)
