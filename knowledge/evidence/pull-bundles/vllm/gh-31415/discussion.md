# PR Discussion Digest

- Source PR: [vllm-project/vllm#31415](https://github.com/vllm-project/vllm/pull/31415)
- Source page: `sources/prs/vllm/PR-31415.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-31415`
- Generated at: `2026-05-20T15:39:19.980065+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-27T18:45:58Z`
- Merged: `2026-01-08T00:42:34Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 32 (approved=2, commented=30)
- Inline review comments: 32
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=8, outdated=7
- Human participants with discussion text: bnellnm, mergify, mgoin, robertgshaw2-redhat, zyongye
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-27T18:47:32Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the Fused MoE backend selection logic by moving Fp8MoeBackend and get fp8 ... (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3614403399)
- `2025-12-29T20:16:31Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3616674358)
- `2026-01-07T15:50:04Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3635541019)
- `2026-01-07T15:54:15Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3635557855)
- `2026-01-07T16:03:49Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3635603711)
- `2026-01-07T16:10:29Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3635631341)
- `2026-01-07T16:16:14Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3635654206)
- `2026-01-07T16:24:23Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3635686436)
- `2026-01-07T17:17:03Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3635918707)
- `2026-01-07T17:17:50Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3635922573)
- `2026-01-07T17:21:51Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3635944670)
- `2026-01-07T17:22:43Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3635949632)
- `2026-01-07T17:42:55Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3636069769)
- `2026-01-07T18:11:35Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3636197597)
- `2026-01-07T18:14:40Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3636207680)
- `2026-01-07T18:16:23Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3636213201)
- `2026-01-07T18:18:16Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3636219670)
- `2026-01-07T18:46:41Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3636331260)
- `2026-01-07T19:10:01Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3636424640)
- `2026-01-07T19:12:57Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3636367064)
- `2026-01-07T19:17:33Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3636448744)
- `2026-01-07T19:17:45Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3636449440)
- `2026-01-07T19:37:32Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3636510590)
- `2026-01-07T19:38:05Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31415#pullrequestreview-3636512119)
- ... 8 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/oracle/fp8.py`: 9 inline comment(s)
- `vllm/model_executor/layers/fused_moe/triton_cutlass_moe.py`: 9 inline comment(s)
- `vllm/model_executor/layers/fused_moe/cutlass_moe.py`: 5 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fallback.py`: 2 inline comment(s)
- `vllm/model_executor/models/llama4.py`: 2 inline comment(s)
- `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-cutlass.yaml`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`: 2 inline comment(s)
- `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-07T18:11:35Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/triton_cutlass_moe.py`:75; signals: cutlass, deepgemm, gemm, hang, moe, triton; excerpt: "okay, I remember why I could not do this The reason is that for the DeepGEMM case, we have different logic for workspace vs ..." (https://github.com/vllm-project/vllm/pull/31415#discussion_r2669586245)
- `2026-01-07T17:21:51Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/triton_cutlass_moe.py`:75; signals: cutlass, deepgemm, gemm, moe, triton; excerpt: "I originally had it that way, but I thought there might be times that the workspace shapes selection and gemm impl selection might not ..." (https://github.com/vllm-project/vllm/pull/31415#discussion_r2669354476)
- `2025-12-29T20:16:31Z` `inline` by `robertgshaw2-redhat` `benchmarks/kernels/benchmark_cutlass_moe_fp8.py`:130; signals: benchmark, cutlass, fp8, kernel, moe; excerpt: "this function was unused" (https://github.com/vllm-project/vllm/pull/31415#discussion_r2651700883)
- `2026-01-07T20:01:56Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/triton_cutlass_moe.py`:75; signals: cutlass, deepgemm, gemm, moe, triton; excerpt: "I think we could avoid having the weights. We need to cleanup the logic for deepgemm selection" (https://github.com/vllm-project/vllm/pull/31415#discussion_r2669901834)
- `2026-01-07T19:38:05Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/triton_cutlass_moe.py`:65; signals: b200, cutlass, moe, triton; excerpt: "addressed. I hadnt actually hooked up CutlassOrTritonExperts I also added a test to ensure it runs on B200" (https://github.com/vllm-project/vllm/pull/31415#discussion_r2669833695)
- `2026-01-07T16:16:13Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/triton_cutlass_moe.py`:75; signals: cutlass, moe, triton; excerpt: "Would it make more sense to have a select experts (or maybe use primary) method that returns a bool instead that indicates primary or ..." (https://github.com/vllm-project/vllm/pull/31415#discussion_r2669099890)
- `2026-01-07T17:17:50Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/oracle/fp8.py`:290; signals: fp8, hang, moe; excerpt: "yeah I think that could work. I would prefer to make the change in a separate PR though as this one already has a ..." (https://github.com/vllm-project/vllm/pull/31415#discussion_r2669331918)
- `2026-01-07T18:16:23Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:267; signals: cutlass, kernel, moe; excerpt: "I think 10MB per layer for llama maverick. So something like 0.5GB Given this kernel is not the most critical, I think we should ..." (https://github.com/vllm-project/vllm/pull/31415#discussion_r2669598465)
- `2026-01-07T18:18:15Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/oracle/fp8.py`:131; signals: fp8, kernel, moe; excerpt: "I tend to agree that the oracle should validate. That being said, the spirit of this PR is to move from several places that ..." (https://github.com/vllm-project/vllm/pull/31415#discussion_r2669604123)
- `2026-01-07T19:11:58Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/triton_cutlass_moe.py`:65; signals: cutlass, moe, triton; excerpt: "Shouldn't this be select experts impl since select experts impl is marked as abstract in FallbackExperts" (https://github.com/vllm-project/vllm/pull/31415#discussion_r2669762764)
- `2026-01-07T19:40:09Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/triton_cutlass_moe.py`:75; signals: cutlass, moe, triton; excerpt: "Do you know if it needs the actual weights or just the weight shapes? Either way, I'm fine with deferring this til later." (https://github.com/vllm-project/vllm/pull/31415#discussion_r2669839343)
- `2026-01-07T20:02:33Z` `inline` by `robertgshaw2-redhat` `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-fi-cutlass.yaml`:5; signals: cutlass, fp8, moe; excerpt: "yeah, thats a good idea. It makes the logs much easier to read by not logging out /completions every request" (https://github.com/vllm-project/vllm/pull/31415#discussion_r2669903772)
