# PR Discussion Digest

- Source PR: [vllm-project/vllm#19085](https://github.com/vllm-project/vllm/pull/19085)
- Source page: `sources/prs/vllm/PR-19085.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-19085`
- Generated at: `2026-05-20T15:35:27.374055+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-03T13:08:37Z`
- Merged: `2025-06-11T07:14:46Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 17 (approved=3, commented=14)
- Inline review comments: 15
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=3, outdated=5
- Human participants with discussion text: artetaout, bnellnm, mgoin, shixianc, tlrmchlsmth, youkaichao
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-04T14:10:44Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2896894121)
- `2025-06-04T14:17:32Z` `COMMENTED` by `artetaout` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2896934721)
- `2025-06-04T14:17:39Z` `COMMENTED` by `artetaout` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2896935886)
- `2025-06-04T15:04:27Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2897127471)
- `2025-06-04T15:10:55Z` `COMMENTED` by `artetaout` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2897148419)
- `2025-06-05T12:30:50Z` `COMMENTED` by `artetaout` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2900134485)
- `2025-06-05T12:31:01Z` `COMMENTED` by `artetaout` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2900135398)
- `2025-06-05T12:33:02Z` `COMMENTED` by `artetaout` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2900142198)
- `2025-06-05T23:25:47Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2902989419)
- `2025-06-06T04:35:13Z` `COMMENTED` by `artetaout` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2903742856)
- `2025-06-06T19:41:11Z` `COMMENTED` by `mgoin` - Nice simplification work, this looks much better! Just one nit and I'll help you look at the CI ... (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2905990251)
- `2025-06-06T22:53:43Z` `COMMENTED` by `artetaout` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2906355607)
- `2025-06-08T17:59:38Z` `COMMENTED` by `shixianc` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2908594150)
- `2025-06-09T02:55:30Z` `COMMENTED` by `artetaout` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2908809689)
- `2025-06-10T17:42:07Z` `APPROVED` by `shixianc` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2914528493)
- `2025-06-10T17:47:01Z` `APPROVED` by `mgoin` - LGTM, thank you for the contribution! We should aim to document this and possibly make a script/tool for ... (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2914550585)
- `2025-06-10T19:41:10Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/19085#pullrequestreview-2914848993)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/fp8_utils.py`: 10 inline comment(s)
- `vllm/model_executor/layers/quantization/deepgemm.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-06-04T14:10:37Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:123; signals: deepgemm, dtype, fp8, gemm, hopper; excerpt: "Make these names more specific e.g. dg supported dtype. Also doesn't deepgemm only support Hopper GPUs? So we should be checking compute capability" (https://github.com/vllm-project/vllm/pull/19085#discussion_r2126706308)
- `2025-06-06T04:35:13Z` `inline` by `artetaout` `vllm/model_executor/layers/quantization/deepgemm.py`:293; signals: bf16, compile, deepgemm, fp8, gemm; excerpt: "Can you explain how this method is different than deep gemm.gemm fp8 fp8 bf16 nt? There's a lot of lower level code copied from ..." (https://github.com/vllm-project/vllm/pull/19085#discussion_r2131479120)
- `2025-06-08T17:59:38Z` `inline` by `shixianc` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:148; signals: block, deepgemm, fp8, gemm, register; excerpt: "After registering custom op in vllm, I thought we need to call using torch.ops.vllm.w8a8 block fp8 matmul deepgemm instead of calling directly?" (https://github.com/vllm-project/vllm/pull/19085#discussion_r2134786735)
- `2025-06-06T05:56:10Z` `issue` by `shixianc`; signals: block, deepgemm, fp8, gemm, kernel; excerpt: "Does this deepgemm kernel only work for block quant (fine-grained) fp8 models? Can it work with general per-tensor/channel quant fp8 models?" (https://github.com/vllm-project/vllm/pull/19085#issuecomment-2948185812)
- `2025-06-06T06:55:43Z` `issue` by `artetaout`; signals: block, deepgemm, fp8, gemm, kernel; excerpt: "Does this deepgemm kernel only work for block quant (fine-grained) fp8 models? Can it work with general per-tensor/channel quant fp8 models? I've never try ..." (https://github.com/vllm-project/vllm/pull/19085#issuecomment-2948285701)
- `2025-06-05T23:25:47Z` `inline` by `bnellnm` `vllm/model_executor/layers/quantization/deepgemm.py`:293; signals: bf16, deepgemm, fp8, gemm; excerpt: "Can you explain how this method is different than deep gemm.gemm fp8 fp8 bf16 nt? There's a lot of lower level code copied from ..." (https://github.com/vllm-project/vllm/pull/19085#discussion_r2130899801)
- `2025-06-05T12:32:11Z` `issue` by `artetaout`; signals: accuracy, benchmark, perf, performance; excerpt: "currently ONLY support vLLM V0 Why is this the case and could you support V1? We will deprecate V0 soon For your benchmarking, what ..." (https://github.com/vllm-project/vllm/pull/19085#issuecomment-2944061104)
- `2025-06-06T17:22:20Z` `issue` by `shixianc`; signals: block, deepgemm, fp8, gemm; excerpt: "@artetaout I'm testing on our own model that quantized with AutoFP8 (per-tensor fp8) Here's one on HF: RedHatAI/Mixtral-8x7B-Instruct-v0.1-AutoFP8 However I were looking at the ..." (https://github.com/vllm-project/vllm/pull/19085#issuecomment-2949938747)
- `2025-06-06T18:38:47Z` `issue` by `artetaout`; signals: block, deepgemm, fp8, gemm; excerpt: "@artetaout I'm testing on our own model that quantized with AutoFP8 (per-tensor fp8) Here's one on HF: RedHatAI/Mixtral-8x7B-Instruct-v0.1-AutoFP8 However I were looking at the ..." (https://github.com/vllm-project/vllm/pull/19085#issuecomment-2950148175)
- `2025-06-04T15:04:26Z` `inline` by `youkaichao` `vllm/model_executor/layers/quantization/deepgemm.py`:49; signals: compile, deepgemm, gemm; excerpt: "to support torch.compile, i think you can wrap the function inside a custom op, examples here:" (https://github.com/vllm-project/vllm/pull/19085#discussion_r2126838320)
- `2025-06-05T12:33:02Z` `inline` by `artetaout` `vllm/model_executor/layers/quantization/deepgemm.py`:49; signals: compile, deepgemm, gemm; excerpt: "The torch.compile is SUPPORTED. the result is updated as well" (https://github.com/vllm-project/vllm/pull/19085#discussion_r2128746587)
- `2025-06-06T19:40:06Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:111; signals: fp8, hopper; excerpt: "This should use the new is device capability function to check for exact match (you might need to merge from main), since Hopper is ..." (https://github.com/vllm-project/vllm/pull/19085#discussion_r2132815343)
