# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12738](https://github.com/NVIDIA/TensorRT-LLM/pull/12738)
- Source page: `sources/prs/tensorrt-llm/PR-12738.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12738`
- Generated at: `2026-05-20T15:18:17.536455+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete via REST overflow fallback`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-03T14:54:07Z`
- Merged: `2026-04-30T13:44:49Z`

## Discussion Counts

- Issue comments: 128
- Review submissions: 6 (approved=3, commented=3)
- Inline review comments: 10
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=9
- Human participants with discussion text: EmmaQiaoCh, HuiGao-NV, LarryXFly, coderabbitai, nv-guomingz, rosenrodt, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-03T15:06:53Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 6 🧹 Nitpick comments (3) tests/integration/defs/accuracy/test llm api pytorch.py (2) 5963-5973: Assert the selected MoE ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#pullrequestreview-4056086731)
- `2026-04-05T05:15:50Z` `APPROVED` by `LarryXFly` (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#pullrequestreview-4059123070)
- `2026-04-05T19:48:25Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#pullrequestreview-4059781183)
- `2026-04-06T06:19:45Z` `COMMENTED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#pullrequestreview-4060588464)
- `2026-04-13T04:57:31Z` `APPROVED` by `EmmaQiaoCh` (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#pullrequestreview-4096473549)
- `2026-04-13T09:13:12Z` `APPROVED` by `HuiGao-NV` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#pullrequestreview-4097593077)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`: 3 inline comment(s)
- `tests/integration/test_lists/waives.txt`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/moe_op_backend.py`: 1 inline comment(s)
- `tests/integration/test_lists/test-db/l0_b200.yml`: 1 inline comment(s)
- `tests/unittest/_torch/modules/moe/moe_test_utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-03T15:06:53Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, aligned, b200, bf16, cache, cuda, fp4, hang; excerpt: "Actionable comments posted: 6 🧹 Nitpick comments (3) tests/integration/defs/accuracy/test llm api pytorch.py (2) 5963-5973: Assert the selected MoE backend in the BF16 matrix. This ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#pullrequestreview-4056086731)
- `2026-04-03T15:06:51Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`:82; signals: bf16, cutlass, dtype, flashinfer, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Honor call-site dtype overrides when resolving the BF16 backend. resolve moe cls() takes dtype, but the unquantized BF16 branch ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#discussion_r3033219719)
- `2026-04-03T15:06:51Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:325; signals: benchmark, bf16, flashinfer, hang, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Fix the hanging indent in supports flashinfer bf16 routing method. Flake8 is already reporting E125 here, so the lint ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#discussion_r3033219725)
- `2026-04-03T15:06:51Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/moe_op_backend.py`:808; signals: accuracy, bf16, flashinfer, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Fail fast on the BF16 direct-routing kernel for now. TRTLLMGenFusedMoE. requires separated routing() now documents that FlashInfer BF16 direct ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#discussion_r3033219733)
- `2026-04-03T15:06:52Z` `inline` by `coderabbitai` `tests/unittest/_torch/modules/moe/moe_test_utils.py`:240; signals: bf16, block, flashinfer, kernel, moe; excerpt: "⚠️ Potential issue 🟠 Major Don't apply the TRTLLM C++ routing skips to the BF16 FlashInfer path. quant algo is None now reaches should ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#discussion_r3033219749)
- `2026-04-13T09:10:49Z` `inline` by `HuiGao-NV` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:318; signals: cache, moe, tensorrt; excerpt: "This can be static value after initialization. Can use a instance variable to cache it." (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#discussion_r3071956301)
- `2026-04-03T15:06:51Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`:195; signals: moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Config freeze/skip flags are not safely restored across all paths. Line 193 and Line 195 force frozen=True instead of ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#discussion_r3033219710)
- `2026-04-03T15:06:51Z` `inline` by `coderabbitai` `tests/integration/test_lists/test-db/l0_b200.yml`:80; signals: b200, benchmark; excerpt: "⚠️ Potential issue 🟠 Major tp2 cases are inconsistent with this single-GPU lane. Line 77–Line 80 add tp2 test IDs under a condition constrained ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#discussion_r3033219739)
- `2026-04-05T19:48:16Z` `inline` by `rosenrodt` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:325; signals: moe, tensorrt; excerpt: "Note: this will be addressed by" (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#discussion_r3037277092)
- `2026-04-03T23:15:43Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 41692]( [ run ] completed with state SUCCESS. Commit: 2319281 [/LLM/main/L0 MergeRequest PR pipeline 32595]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#issuecomment-4185559992)
- `2026-04-04T01:37:38Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 41778]( [ run ] completed with state FAILURE. Commit: 2319281 [/LLM/main/L0 MergeRequest PR pipeline 32673]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#issuecomment-4185953797)
- `2026-04-04T13:38:09Z` `issue` by `tensorrt-cicd`; signals: nan; excerpt: "[PR Github 41826]( [ run ] completed with state DISABLED CI server is currently disabled for scheduled maintenance. Estimated completion time: 9 PM PST ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12738#issuecomment-4187130996)
