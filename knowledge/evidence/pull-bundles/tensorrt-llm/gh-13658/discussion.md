# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13658](https://github.com/NVIDIA/TensorRT-LLM/pull/13658)
- Source page: `sources/prs/tensorrt-llm/PR-13658.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13658`
- Generated at: `2026-05-20T15:18:49.452032+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-30T09:27:03Z`
- Merged: `2026-05-12T21:41:35Z`

## Discussion Counts

- Issue comments: 53
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 7
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=3
- Human participants with discussion text: coderabbitai, galagam, tcherckez-nvidia, tensorrt-cicd, xinhe-nv
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-30T09:35:53Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#pullrequestreview-4204048918)
- `2026-04-30T15:07:10Z` `APPROVED` by `galagam` (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#pullrequestreview-4206198024)
- `2026-04-30T15:07:17Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#pullrequestreview-4206265622)
- `2026-05-07T07:28:22Z` `COMMENTED` by `xinhe-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#pullrequestreview-4241955283)
- `2026-05-07T07:28:27Z` `APPROVED` by `xinhe-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#pullrequestreview-4241955680)

## Inline Comment Hotspots

- `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`: 4 inline comment(s)
- `tests/integration/test_lists/test-db/l0_dgx_b200.yml`: 3 inline comment(s)

## High-Signal Discussion

- `2026-04-30T09:28:31Z` `issue` by `coderabbitai`; signals: accuracy, attention, b200, benchmark, cache, cuda, flashinfer, fp4; excerpt: "📝 Walkthrough Walkthrough This pull request adds support for the Nemotron-Ultra-V3 model by introducing model registry configuration, accuracy reference benchmarks for GSM8K and MMLU, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#issuecomment-4351283633)
- `2026-04-30T09:35:53Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, b200, block, flashinfer, hang; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#pullrequestreview-4204048918)
- `2026-04-30T09:35:51Z` `inline` by `coderabbitai` `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`:809; signals: accuracy, b200, blackwell, fp4, nvfp4; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Gate Ultra V3 NVFP4 on Blackwell. This class only exercises the NVFP4 path, but it never ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#discussion_r3166984215)
- `2026-04-30T14:58:57Z` `inline` by `galagam` `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`:741; signals: accuracy; excerpt: "Need to be careful with over-parameterizing. I realize this is copied from SuperV3, but I don't think it's maintainable to keep testing all these ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#discussion_r3168852353)
- `2026-04-30T15:05:01Z` `inline` by `galagam` `tests/integration/test_lists/test-db/l0_dgx_b200.yml`:333; signals: b200; excerpt: "Config defines trtllm attn backend, so the most important config we want to target in pre-merge is anything else can go to post merge" (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#discussion_r3168891319)
- `2026-04-30T15:06:10Z` `inline` by `galagam` `tests/integration/test_lists/test-db/l0_dgx_b200.yml`:355; signals: b200; excerpt: "I see you put this in post merge to limit pre-merge runtime, that's good. I'd still stick with just the YAML config - this ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#discussion_r3168899640)
- `2026-04-30T15:07:17Z` `inline` by `coderabbitai` `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`:809; signals: accuracy; excerpt: "Seems like the humans are having a chat. I'll hop back into my burrow for now. If you need me again, just tag @coderabbitai ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#discussion_r3168907033)
- `2026-04-30T15:01:26Z` `inline` by `galagam` `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`:809; signals: accuracy; excerpt: "+1 @tcherckez-nvidia" (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#discussion_r3168868039)
- `2026-05-07T07:28:23Z` `inline` by `xinhe-nv` `tests/integration/test_lists/test-db/l0_dgx_b200.yml`:348; signals: b200; excerpt: "I think we should add the two cases into qa test list." (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#discussion_r3199650350)
- `2026-04-30T14:17:00Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46356]( [ run ] completed with state SUCCESS. Commit: 5f905e2 [/LLM/main/L0 MergeRequest PR pipeline 36443]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#issuecomment-4353212326)
- `2026-05-03T11:21:25Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46585]( [ run ] completed with state SUCCESS. Commit: eee2b19 [/LLM/main/L0 MergeRequest PR pipeline 36634]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#issuecomment-4366042430)
- `2026-05-06T11:44:17Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46927]( [ run ] completed with state SUCCESS. Commit: eee2b19 [/LLM/main/L0 MergeRequest PR pipeline 36933]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13658#issuecomment-4387589988)
