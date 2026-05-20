# PR Discussion Digest

- Source PR: [vllm-project/vllm#40273](https://github.com/vllm-project/vllm/pull/40273)
- Source page: `sources/prs/vllm/PR-40273.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-40273`
- Generated at: `2026-05-20T15:40:48.533273+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-19T06:51:47Z`
- Merged: `2026-04-19T17:18:40Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 21 (approved=2, changes_requested=1, commented=18)
- Inline review comments: 22
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=7, outdated=7
- Human participants with discussion text: amitz-nv, claude, danisereb, netanel-haber, robertgshaw2-redhat, tomeras91
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-19T06:53:51Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces logic to force the Triton backend for unquantized MoE when LoRA is ... (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135586881)
- `2026-04-19T08:55:12Z` `COMMENTED` by `netanel-haber` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135717176)
- `2026-04-19T08:58:40Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135720715)
- `2026-04-19T09:08:42Z` `COMMENTED` by `netanel-haber` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135735163)
- `2026-04-19T09:11:21Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135737569)
- `2026-04-19T09:23:13Z` `COMMENTED` by `amitz-nv` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135746704)
- `2026-04-19T09:25:37Z` `COMMENTED` by `amitz-nv` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135748556)
- `2026-04-19T09:26:01Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135748925)
- `2026-04-19T09:29:57Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135751955)
- `2026-04-19T09:36:32Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135757206)
- `2026-04-19T09:36:44Z` `COMMENTED` by `claude` - Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer ... (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135757536)
- `2026-04-19T10:54:50Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135845778)
- `2026-04-19T12:58:14Z` `CHANGES_REQUESTED` by `tomeras91` - Thanks @danisereb! Added a few suggestions (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135927657)
- `2026-04-19T13:06:08Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135988118)
- `2026-04-19T13:07:23Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135989489)
- `2026-04-19T13:09:04Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4135991262)
- `2026-04-19T14:34:38Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4136124599)
- `2026-04-19T14:35:21Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4136125955)
- `2026-04-19T15:43:01Z` `APPROVED` by `tomeras91` - Much better now. Left a small nit (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4136192848)
- `2026-04-19T15:45:38Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4136199165)
- `2026-04-19T15:45:45Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/40273#pullrequestreview-4136199263)

## Inline Comment Hotspots

- `tests/kernels/moe/test_unquantized_backend_selection.py`: 12 inline comment(s)
- `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`: 10 inline comment(s)

## High-Signal Discussion

- `2026-04-19T09:26:01Z` `inline` by `danisereb` `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`:171; signals: fp4, fp8, hang, moe, mxfp4; excerpt: "I added the changes in select unquantized moe backend because other quantizations follow the same pattern. See select fp8 moe backend, select mxfp8 moe ..." (https://github.com/vllm-project/vllm/pull/40273#discussion_r3106573517)
- `2026-04-19T09:29:57Z` `inline` by `danisereb` `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`:230; signals: aligned, fp4, fp8, moe, mxfp4; excerpt: "Same answer as my previous comment, I aligned with the code in select fp8 moe backend, select mxfp8 moe backend, select gpt oss mxfp4 ..." (https://github.com/vllm-project/vllm/pull/40273#discussion_r3106577457)
- `2026-04-19T09:36:32Z` `inline` by `danisereb` `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`:230; signals: cutlass, flashinfer, hang, kernel, moe; excerpt: "More detailed answer to your question - Conceptually, yes — backend capability checks are cleaner when centralized in FusedMoEExperts.is supported config() with a per-backend ..." (https://github.com/vllm-project/vllm/pull/40273#discussion_r3106584027)
- `2026-04-19T10:54:49Z` `inline` by `danisereb` `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`:171; signals: bf16, cutlass, hang, moe, triton; excerpt: "One more point - this change will just revert to the old behavior (when Triton was default). This was probably broken when cutlass was ..." (https://github.com/vllm-project/vllm/pull/40273#discussion_r3106708627)
- `2026-04-19T12:20:55Z` `inline` by `tomeras91` `tests/kernels/moe/test_unquantized_backend_selection.py`:110; signals: fp8, kernel, moe, triton; excerpt: "Are we sure LoRA works with AITER on ROCm? in the FP8 path, with LoRA enabled triton is returned as the only available backend ..." (https://github.com/vllm-project/vllm/pull/40273#discussion_r3106808886)
- `2026-04-19T12:49:51Z` `inline` by `tomeras91` `tests/kernels/moe/test_unquantized_backend_selection.py`:110; signals: cuda, kernel, moe, triton; excerpt: "Had a deeper look at the code. LoRA is supported ONLY for the triton backend also for ROCm: Let's make sure the test reflects ..." (https://github.com/vllm-project/vllm/pull/40273#discussion_r3106848244)
- `2026-04-19T12:52:15Z` `inline` by `tomeras91` `tests/kernels/moe/test_unquantized_backend_selection.py`:221; signals: cuda, kernel, moe, triton; excerpt: "A few issues: 1. If this test is running on CUDA, the context manager mocking current platform is redundant. On CUDA, only current platform.is ..." (https://github.com/vllm-project/vllm/pull/40273#discussion_r3106851347)
- `2026-04-19T13:06:08Z` `inline` by `danisereb` `tests/kernels/moe/test_unquantized_backend_selection.py`:110; signals: cuda, hang, kernel, moe; excerpt: "Maybe you missed my last changed. I made sure to apply changes only for CUDA. I have no way of testing LoRA with ROCm." (https://github.com/vllm-project/vllm/pull/40273#discussion_r3106868018)
- `2026-04-19T13:09:04Z` `inline` by `danisereb` `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`:169; signals: cuda, hang, moe, triton; excerpt: "I did notice ROCm seems to support Triton, but I have no idea if that works and didn't want to send a "wrong message" ..." (https://github.com/vllm-project/vllm/pull/40273#discussion_r3106871661)
- `2026-04-19T12:57:57Z` `inline` by `tomeras91` `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`:169; signals: fp8, moe, triton; excerpt: "A few comments: 1. Again, this should be platform-agnostic 2. I want to reinforce previous review's comments - The approach here seems a bit ..." (https://github.com/vllm-project/vllm/pull/40273#discussion_r3106858207)
- `2026-04-19T13:07:23Z` `inline` by `danisereb` `tests/kernels/moe/test_unquantized_backend_selection.py`:221; signals: cuda, kernel, moe; excerpt: "1. I wanted to keep the same test "pattern". 2. I can't test ROCm, so I applied my fix only for case of CUDA ..." (https://github.com/vllm-project/vllm/pull/40273#discussion_r3106869509)
- `2026-04-19T14:34:38Z` `inline` by `danisereb` `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`:166; signals: aligned, fp8, moe; excerpt: "This logic is now aligned with select fp8 moe backend (early exit if LoRA is enabled)." (https://github.com/vllm-project/vllm/pull/40273#discussion_r3106987509)
