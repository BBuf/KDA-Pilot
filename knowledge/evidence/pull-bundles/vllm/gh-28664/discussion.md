# PR Discussion Digest

- Source PR: [vllm-project/vllm#28664](https://github.com/vllm-project/vllm/pull/28664)
- Source page: `sources/prs/vllm/PR-28664.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28664`
- Generated at: `2026-05-20T15:38:32.003007+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-13T15:52:32Z`
- Merged: `2026-01-22T08:33:18Z`

## Discussion Counts

- Issue comments: 17
- Review submissions: 30 (approved=3, changes_requested=1, commented=26)
- Inline review comments: 35
- Review threads observed: 17
- Resolved/outdated thread markers: resolved=13, outdated=10
- Human participants with discussion text: Duyi-Wang, HAIAI, SageMoore, alexsun07, bnellnm, cursor, mergify, sunway513, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-11-13T15:54:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces MoRI-EP as a high-performance all2all backend for Mixture-of-Experts models on ROCm platforms. ... (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3460484954)
- `2025-11-13T16:04:40Z` `COMMENTED` by `alexsun07` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3460531071)
- `2025-11-13T16:24:33Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3460624416)
- `2025-11-13T20:45:42Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3461613591)
- `2025-11-14T01:11:59Z` `COMMENTED` by `alexsun07` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3462340019)
- `2025-11-14T01:15:04Z` `COMMENTED` by `alexsun07` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3462346054)
- `2025-11-18T17:31:27Z` `COMMENTED` by `SageMoore` - This looks good. Will accept once the test is added. Thanks for the contribution! (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3478976247)
- `2025-11-20T15:57:44Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3488622056)
- `2025-11-20T16:05:54Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3488657797)
- `2025-11-20T16:08:28Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3488672324)
- `2025-11-21T02:26:59Z` `COMMENTED` by `Duyi-Wang` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3490906855)
- `2025-11-21T02:27:03Z` `COMMENTED` by `Duyi-Wang` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3490906919)
- `2025-11-21T02:27:06Z` `COMMENTED` by `Duyi-Wang` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3490907012)
- `2025-11-21T02:57:42Z` `APPROVED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3490996101)
- `2025-11-21T13:35:27Z` `APPROVED` by `SageMoore` - Looks good. Thanks for the contribution! Excited to try this out. (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3492796946)
- `2025-11-28T14:31:20Z` `APPROVED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3519206766)
- `2025-12-01T18:06:24Z` `CHANGES_REQUESTED` by `HAIAI` - @alexsun07 mostly comments with some notable suggestions. (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3524327017)
- `2025-12-02T03:20:01Z` `COMMENTED` by `alexsun07` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3527970434)
- `2025-12-02T12:39:26Z` `COMMENTED` by `Duyi-Wang` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3529874186)
- `2025-12-02T12:41:51Z` `COMMENTED` by `Duyi-Wang` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3529883425)
- `2025-12-02T12:51:13Z` `COMMENTED` by `Duyi-Wang` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3529924629)
- `2025-12-02T13:15:22Z` `COMMENTED` by `Duyi-Wang` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3530063207)
- `2025-12-03T09:35:13Z` `COMMENTED` by `Duyi-Wang` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3534075443)
- `2025-12-03T09:35:35Z` `COMMENTED` by `Duyi-Wang` (https://github.com/vllm-project/vllm/pull/28664#pullrequestreview-3534077247)
- ... 6 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tests/kernels/moe/test_modular_kernel_combinations.py`: 6 inline comment(s)
- `vllm/distributed/device_communicators/all2all.py`: 5 inline comment(s)
- `vllm/model_executor/layers/fused_moe/mori_prepare_finalize.py`: 4 inline comment(s)
- `vllm/model_executor/models/deepseek_v2.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_aiter_moe.py`: 2 inline comment(s)
- `tests/kernels/moe/modular_kernel_tools/mk_objects.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/fp8.py`: 2 inline comment(s)
- `vllm/config/parallel.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/all2all_utils.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/config.py`: 2 inline comment(s)
- `vllm/utils/import_utils.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-20T11:35:51Z` `inline` by `cursor` `vllm/_aiter_ops.py`:125; signals: compile, dtype, moe; excerpt: "Fake function ignores output dtype parameter for torch.compile Medium Severity The rocm aiter fused moe fake function was updated to accept the new output ..." (https://github.com/vllm-project/vllm/pull/28664#discussion_r2707973313)
- `2025-11-13T16:24:33Z` `inline` by `tjtanaa` `vllm/model_executor/layers/fused_moe/mori_prepare_finalize.py`:80; signals: cuda, cudagraph, moe; excerpt: "Is this part of code included in CUDAGraph?" (https://github.com/vllm-project/vllm/pull/28664#discussion_r2524116752)
- `2025-11-13T20:59:20Z` `issue` by `bnellnm`; signals: kernel, moe, register; excerpt: "A test in tests/kernels/moe would be good. It probably wouldn't be too hard to add the new Mori kernels to tests/kernels/moe/test modular kernel combinations.py ..." (https://github.com/vllm-project/vllm/pull/28664#issuecomment-3529690336)
- `2025-11-14T01:09:41Z` `issue` by `alexsun07`; signals: kernel, moe, register; excerpt: "A test in tests/kernels/moe would be good. It probably wouldn't be too hard to add the new Mori kernels to tests/kernels/moe/test modular kernel combinations.py ..." (https://github.com/vllm-project/vllm/pull/28664#issuecomment-3530382850)
- `2025-11-14T01:15:04Z` `inline` by `alexsun07` `vllm/model_executor/layers/fused_moe/mori_prepare_finalize.py`:80; signals: fp8, moe; excerpt: "I’m not sure if I understand your question. Here is to do the FP8 quant before dispatch so that we can reduce communication overhead" (https://github.com/vllm-project/vllm/pull/28664#discussion_r2525416004)
- `2025-11-20T15:57:43Z` `inline` by `bnellnm` `tests/kernels/moe/modular_kernel_tools/mk_objects.py`:512; signals: kernel, moe; excerpt: "nit: I think it would be better to make the support checks asserts under each branch rather than making the construction conditional on them." (https://github.com/vllm-project/vllm/pull/28664#discussion_r2546647378)
- `2025-11-20T16:05:54Z` `inline` by `bnellnm` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:955; signals: block, moe; excerpt: "Should this be moved to the elif self.rocm aiter moe enabled block? Otherwise we might be trying to import it in cases where aiter ..." (https://github.com/vllm-project/vllm/pull/28664#discussion_r2546675965)
- `2025-12-03T09:35:12Z` `inline` by `Duyi-Wang` `tests/kernels/moe/test_modular_kernel_combinations.py`:50; signals: kernel, moe; excerpt: "The check for mori has been removed for now. We’ll reintroduce it again when MORI adds support for other MoE backends" (https://github.com/vllm-project/vllm/pull/28664#discussion_r2584335924)
- `2025-11-14T01:11:58Z` `inline` by `alexsun07` `vllm/model_executor/layers/fused_moe/fused_aiter_moe.py`:90; signals: kernel, moe; excerpt: "Yes. Will talk with kernel team. Probably would not be included in this PR." (https://github.com/vllm-project/vllm/pull/28664#discussion_r2525411083)
- `2025-11-21T02:26:59Z` `inline` by `Duyi-Wang` `tests/kernels/moe/modular_kernel_tools/mk_objects.py`:512; signals: kernel, moe; excerpt: "done" (https://github.com/vllm-project/vllm/pull/28664#discussion_r2548326460)
- `2025-12-01T10:41:42Z` `inline` by `HAIAI` `tests/kernels/moe/test_modular_kernel_combinations.py`:50; signals: kernel, moe; excerpt: "MoRI EP has dependency on aiter, should we enforce that?" (https://github.com/vllm-project/vllm/pull/28664#discussion_r2576555258)
- `2025-12-01T10:44:10Z` `inline` by `HAIAI` `tests/kernels/moe/test_modular_kernel_combinations.py`:45; signals: kernel, moe; excerpt: "How to code aiter dependency?" (https://github.com/vllm-project/vllm/pull/28664#discussion_r2576564147)
