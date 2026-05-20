# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12799](https://github.com/NVIDIA/TensorRT-LLM/pull/12799)
- Source page: `sources/prs/tensorrt-llm/PR-12799.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12799`
- Generated at: `2026-05-20T15:18:20.218787+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-07T08:05:39Z`
- Merged: `2026-04-13T01:56:08Z`

## Discussion Counts

- Issue comments: 33
- Review submissions: 6 (approved=4, commented=2)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=0
- Human participants with discussion text: StanleySun639, coderabbitai, longlee0622, nv-guomingz, tensorrt-cicd, xinhe-nv, xxi-nv
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-07T08:09:54Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#pullrequestreview-4066644445)
- `2026-04-08T09:30:44Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#pullrequestreview-4074147935)
- `2026-04-08T09:45:35Z` `APPROVED` by `longlee0622` (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#pullrequestreview-4074229728)
- `2026-04-10T05:51:31Z` `APPROVED` by `StanleySun639` (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#pullrequestreview-4087557931)
- `2026-04-10T06:35:02Z` `COMMENTED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#pullrequestreview-4087811783)
- `2026-04-13T01:53:36Z` `APPROVED` by `xinhe-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#pullrequestreview-4096056755)

## Inline Comment Hotspots

- `tests/integration/test_lists/test-db/l0_dgx_b200.yml`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`: 1 inline comment(s)
- `tests/integration/defs/accuracy/test_llm_api_pytorch.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-07T08:09:50Z` `issue` by `coderabbitai`; signals: accuracy, b200, cute, fp4, hang, moe, nvfp4, tensorrt; excerpt: "📝 Walkthrough Walkthrough The changes add an optional allow partial loading parameter to the CuteDslFusedMoE.load weights method and expand integration test coverage by parametrizing ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#issuecomment-4197501172)
- `2026-04-07T08:09:54Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, b200, cute, hang, moe, tensorrt; excerpt: "Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#pullrequestreview-4066644445)
- `2026-04-07T08:09:53Z` `inline` by `coderabbitai` `tests/integration/defs/accuracy/test_llm_api_pytorch.py`:5785; signals: accuracy, cute, fp4, moe, nvfp4; excerpt: "⚠️ Potential issue 🟠 Major Add backend-specific SM skip guards for the new moe backend matrix. test nvfp4 now parametrizes moe backend, but it ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#discussion_r3043679169)
- `2026-04-07T08:09:53Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`:984; signals: cute, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Align load weights signature with the base MoE contract. Line 983 annotates weights as Dict[str, torch.Tensor], but the parent ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#discussion_r3043679162)
- `2026-04-10T05:51:25Z` `inline` by `StanleySun639` `tests/integration/test_lists/test-db/l0_dgx_b200.yml`:22; signals: b200; excerpt: "Could you add the new feature test into QA [test list]( also, thanks!" (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#discussion_r3062363811)
- `2026-04-10T06:35:02Z` `inline` by `nv-guomingz` `tests/integration/test_lists/test-db/l0_dgx_b200.yml`:22; signals: b200; excerpt: "Got it." (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#discussion_r3062578349)
- `2026-04-07T10:16:13Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42111]( [ run ] completed with state SUCCESS. Commit: 5c8eaa5 [/LLM/main/L0 MergeRequest PR pipeline 32949]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#issuecomment-4198244814)
- `2026-04-07T12:29:02Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42136]( [ run ] completed with state SUCCESS. Commit: 89132bd [/LLM/main/L0 MergeRequest PR pipeline 32971]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#issuecomment-4198944039)
- `2026-04-07T23:59:31Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42152]( [ run ] completed with state SUCCESS. Commit: 89132bd [/LLM/main/L0 MergeRequest PR pipeline 32984]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#issuecomment-4202897444)
- `2026-04-08T08:31:55Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42276]( [ run ] completed with state SUCCESS. Commit: 4566e57 [/LLM/main/L0 MergeRequest PR pipeline 33074]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#issuecomment-4204901374)
- `2026-04-08T17:00:43Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42330]( [ run ] completed with state SUCCESS. Commit: 4566e57 [/LLM/main/L0 MergeRequest PR pipeline 33119]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#issuecomment-4208000278)
- `2026-04-09T09:41:11Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 42453]( [ run ] completed with state SUCCESS. Commit: 4566e57 [/LLM/main/L0 MergeRequest PR pipeline 33217]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12799#issuecomment-4213165079)
