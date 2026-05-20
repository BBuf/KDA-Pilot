# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12861](https://github.com/NVIDIA/TensorRT-LLM/pull/12861)
- Source page: `sources/prs/tensorrt-llm/PR-12861.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12861`
- Generated at: `2026-05-20T15:18:20.249852+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-08T21:52:52Z`
- Merged: `2026-05-04T23:58:57Z`

## Discussion Counts

- Issue comments: 87
- Review submissions: 25 (approved=3, commented=22)
- Inline review comments: 32
- Review threads observed: 17
- Resolved/outdated thread markers: resolved=17, outdated=14
- Human participants with discussion text: bmarimuthu-nv, coderabbitai, galagam, lucaslie, tensorrt-cicd, xinhe-nv
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-08T21:53:38Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4078491200)
- `2026-04-08T21:54:51Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4078497691)
- `2026-04-08T21:55:10Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4078499087)
- `2026-04-08T22:38:06Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4078705736)
- `2026-04-09T02:25:11Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 4 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4079366762)
- `2026-04-09T16:50:27Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4084000266)
- `2026-04-09T16:50:36Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4084001072)
- `2026-04-09T16:50:43Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4084001715)
- `2026-04-09T16:50:55Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4084002661)
- `2026-04-09T16:50:59Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4084003081)
- `2026-04-09T16:51:02Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4084003327)
- `2026-04-09T21:02:02Z` `COMMENTED` by `lucaslie` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4085345179)
- `2026-04-10T18:50:21Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4091831824)
- `2026-04-10T18:51:27Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4091840754)
- `2026-04-10T19:04:07Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4091902741)
- `2026-04-10T19:04:39Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4091905056)
- `2026-04-10T19:04:58Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4091906855)
- `2026-04-10T19:59:03Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4092195855)
- `2026-04-13T15:07:13Z` `APPROVED` by `lucaslie` - just a minor suggestion. lgtm otherwise now. Awesome work adding an infra for custom masking to AutoDeploy. Will ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4099702746)
- `2026-04-13T16:50:53Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4100463613)
- `2026-04-14T06:23:25Z` `APPROVED` by `xinhe-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4103721962)
- `2026-04-14T08:02:36Z` `COMMENTED` by `galagam` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4104308646)
- `2026-04-14T08:02:43Z` `APPROVED` by `galagam` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4104309634)
- `2026-04-14T16:51:28Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4107726229)
- ... 1 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_paged_attention.py`: 5 inline comment(s)
- `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/llm.py`: 4 inline comment(s)
- `tests/unittest/auto_deploy/_utils_test/torch_attention_reference.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/shim/ad_executor.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/transform/library/kvcache.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/transform/semantic_mask_registry.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/models/custom/gemma4_multimodal_mask.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_gemma4.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/transform/library/kvcache_transformers.py`: 1 inline comment(s)
- `tests/unittest/auto_deploy/singlegpu/models/test_gemma4.py`: 1 inline comment(s)
- `tests/unittest/auto_deploy/singlegpu/transformations/library/test_inject_custom_attention_mask.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-09T02:25:11Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, attention, cache, gemm, hang, kv cache, tensorrt, triton; excerpt: "Actionable comments posted: 4 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#pullrequestreview-4079366762)
- `2026-04-09T02:25:06Z` `issue` by `coderabbitai`; signals: accuracy, attention, bf16, cache, gemm, hang, kernel, kv cache; excerpt: "📝 Walkthrough Walkthrough This pull request adds multimodal attention masking support to Gemma4 models. New custom operations generate semantic masks for multimodal token sequences, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#issuecomment-4211042129)
- `2026-04-09T02:25:09Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_paged_attention.py`:955; signals: attention, cache, cute, kernel, kv cache, tensorrt, triton; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 3463 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#discussion_r3055160888)
- `2026-04-09T03:59:02Z` `issue` by `bmarimuthu-nv`; signals: accuracy, attention, cache, gemm, hang, regression, triton; excerpt: "Addressed the CodeRabbit feedback in c837584d4b. Fixed: - cached torch reference helper arg ordering - readonly torch cached attention so explicit prepared masks stay ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#issuecomment-4211362354)
- `2026-04-09T16:51:02Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_paged_attention.py`:955; signals: attention, cache, correctness, kv cache, tensorrt, triton; excerpt: "@bmarimuthu-nv, thanks for the fix! The cache len offset ensures query positions and kv positions are in the same absolute KV-coordinate space, which is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#discussion_r3059388430)
- `2026-04-09T21:01:59Z` `inline` by `lucaslie` `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_gemma4.py`:1264; signals: attention, cache, gemm, kv cache, tensorrt; excerpt: "Okay, maybe my initial instructions weren't clear, but my suggestion was not to make the eager code dependent on our cached attention metadata. Instead, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#discussion_r3060635044)
- `2026-04-09T02:25:10Z` `inline` by `coderabbitai` `tests/unittest/auto_deploy/_utils_test/torch_attention_reference.py`:72; signals: attention, cache, cute, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 5487 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#discussion_r3055160892)
- `2026-04-09T02:25:09Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/multimodal_mask.py`:174; signals: attention, cute, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 45 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#discussion_r3055160885)
- `2026-04-09T20:58:42Z` `inline` by `lucaslie` `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_paged_attention.py`:1326; signals: attention, tensorrt, triton; excerpt: "This shouldn't be a new category that can be part of the QKV category. I know we named that initial category QKV and never ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#discussion_r3060620683)
- `2026-04-10T18:50:21Z` `inline` by `bmarimuthu-nv` `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_paged_attention.py`:1326; signals: attention, tensorrt, triton; excerpt: "Agreed, it is not dynamic in the as in dynamic/constant. it's more like optional input. Putting it along wth QKV requires making every following ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#discussion_r3066172103)
- `2026-04-09T16:50:43Z` `inline` by `bmarimuthu-nv` `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_paged_attention.py`:955; signals: attention, tensorrt, triton; excerpt: "Fixed" (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#discussion_r3059386775)
- `2026-04-09T02:25:10Z` `inline` by `coderabbitai` `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`:1020; signals: accuracy, block; excerpt: "⚠️ Potential issue 🟡 Minor Unused sampling params and commented-out evaluation code. 1. Line 1006: self.get default sampling params() is called but the return ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12861#discussion_r3055160890)
