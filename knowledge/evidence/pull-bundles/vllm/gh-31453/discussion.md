# PR Discussion Digest

- Source PR: [vllm-project/vllm#31453](https://github.com/vllm-project/vllm/pull/31453)
- Source page: `sources/prs/vllm/PR-31453.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-31453`
- Generated at: `2026-05-20T15:39:19.984394+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-28T13:15:49Z`
- Merged: `2025-12-30T19:20:15Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: JartX, mergify, mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-28T13:20:18Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request fixes a NotImplementedError when using LoRA with CompressedTensorsWNA16MoEMethod by implementing the select gemm ... (https://github.com/vllm-project/vllm/pull/31453#pullrequestreview-3614681767)
- `2025-12-28T14:42:30Z` `COMMENTED` by `yewentao256` - Thanks for the work! Could you also add a E2E eval report to make sure the accuracy is ... (https://github.com/vllm-project/vllm/pull/31453#pullrequestreview-3614712091)
- `2025-12-28T14:43:05Z` `COMMENTED` by `JartX` (https://github.com/vllm-project/vllm/pull/31453#pullrequestreview-3614712281)
- `2025-12-29T15:30:40Z` `COMMENTED` by `yewentao256` - Nice, let's run CI (https://github.com/vllm-project/vllm/pull/31453#pullrequestreview-3616144304)
- `2025-12-29T20:30:12Z` `COMMENTED` by `yewentao256` - Thanks for catching this, also CC @mgoin (https://github.com/vllm-project/vllm/pull/31453#pullrequestreview-3616700880)
- `2025-12-30T01:42:10Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31453#pullrequestreview-3617088570)
- `2025-12-30T14:27:14Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! (https://github.com/vllm-project/vllm/pull/31453#pullrequestreview-3618404562)
- `2025-12-30T19:18:53Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31453#pullrequestreview-3619078626)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-12-29T16:20:38Z` `issue` by `JartX`; signals: blackwell, moe, triton; excerpt: "Hi @yewentao256 from vllm.model executor.layers.fused moe import ( [2025-12-29T15:48:44Z] FusedMoE, [2025-12-29T15:48:44Z] FusedMoEActivationFormat, [2025-12-29T15:48:44Z] FusedMoEConfig, [2025-12-29T15:48:44Z] FusedMoEMethodBase, [2025-12-29T15:48:44Z] FusedMoEPermuteExpertsUnpermute, [2025-12-29T15:48:44Z] FusedMoeWeightScaleSupported, [2025-12-29T15:48:44Z] TritonExperts, [2025-12-29T15:48:44Z] UnquantizedFusedMoEMethod, ..." (https://github.com/vllm-project/vllm/pull/31453#issuecomment-3696951741)
- `2025-12-30T11:40:51Z` `issue` by `JartX`; signals: blackwell, hang, moe; excerpt: "@mgoin @yewentao256 passed the tests except for the Blackwell MOE test. With the requested and applied changes :)" (https://github.com/vllm-project/vllm/pull/31453#issuecomment-3699101166)
- `2025-12-28T14:43:04Z` `inline` by `JartX` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:1995; signals: fp8, moe; excerpt: "The error still occurs because the main implementation in fused MoE for LoRA support is missing. The implementation of expert parallel fused MoE and ..." (https://github.com/vllm-project/vllm/pull/31453#discussion_r2649741731)
- `2025-12-28T14:42:30Z` `review` `COMMENTED` by `yewentao256`; signals: accuracy; excerpt: "Thanks for the work! Could you also add a E2E eval report to make sure the accuracy is correct? lm eval ..." (https://github.com/vllm-project/vllm/pull/31453#pullrequestreview-3614712091)
- `2025-12-28T13:19:36Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @JartX, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/31453#issuecomment-3694742403)
- `2025-12-28T13:27:28Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @JartX, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/31453#issuecomment-3694747093)
- `2025-12-29T16:11:36Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @JartX, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/31453#issuecomment-3696932294)
- `2025-12-29T16:47:10Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @JartX, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/31453#issuecomment-3697015327)
- `2025-12-29T16:59:22Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @JartX, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/31453#issuecomment-3697038907)
- `2025-12-30T01:42:10Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:2019; signals: moe; excerpt: "Agreed, let's make the import lazy" (https://github.com/vllm-project/vllm/pull/31453#discussion_r2652053065)
- `2025-12-28T15:57:55Z` `issue` by `JartX`; signals: accuracy; excerpt: "@yewentao256 root@65aba4e9bed4:/app lm eval --model local-chat-completions --model args model=QWEN3VL,base url= --tasks chartqa --batch size auto --apply chat template --output path ./results/QWEN3VL chartqa eval.json Tasks ..." (https://github.com/vllm-project/vllm/pull/31453#issuecomment-3694847528)
- `2025-12-29T15:30:40Z` `review` `COMMENTED` by `yewentao256`; signals: general review; excerpt: "Nice, let's run CI" (https://github.com/vllm-project/vllm/pull/31453#pullrequestreview-3616144304)
