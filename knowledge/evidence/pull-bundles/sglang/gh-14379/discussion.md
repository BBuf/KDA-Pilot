# PR Discussion Digest

- Source PR: [sgl-project/sglang#14379](https://github.com/sgl-project/sglang/pull/14379)
- Source page: `sources/prs/sglang/PR-14379.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14379`
- Generated at: `2026-05-20T15:28:00.662089+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-04T01:18:45Z`
- Merged: `2025-12-09T20:05:57Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 18 (approved=2, changes_requested=2, commented=13, dismissed=1)
- Inline review comments: 25
- Review threads observed: 16
- Resolved/outdated thread markers: resolved=15, outdated=10
- Human participants with discussion text: Fridge003, b8zhong, copilot-pull-request-reviewer, kaixih
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-04T04:33:29Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview This PR adds a new CLI flag --fp8-gemm-runner-backend (with alias --fp8-gemm-backend) to allow users to ... (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3538002604)
- `2025-12-04T04:36:34Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3538017527)
- `2025-12-04T04:36:39Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3538018039)
- `2025-12-04T04:53:38Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview Copilot reviewed 7 out of 7 changed files in this pull request and generated 2 ... (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3538073044)
- `2025-12-04T04:57:25Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3538084280)
- `2025-12-04T20:37:58Z` `CHANGES_REQUESTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3541573097)
- `2025-12-04T20:41:33Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3542012328)
- `2025-12-05T00:15:11Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3542632422)
- `2025-12-05T00:17:36Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3542636470)
- `2025-12-06T00:42:05Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview Copilot reviewed 10 out of 10 changed files in this pull request and generated 4 ... (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3546798152)
- `2025-12-08T03:10:43Z` `CHANGES_REQUESTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3549957497)
- `2025-12-08T17:18:56Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3553168254)
- `2025-12-08T17:50:00Z` `COMMENTED` by `kaixih` - Sorry for the late reply. Just leave a minor comment. (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3553285787)
- `2025-12-08T21:03:09Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3554052543)
- `2025-12-08T21:08:48Z` `APPROVED` by `kaixih` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3554072398)
- `2025-12-08T21:34:52Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3554155011)
- `2025-12-09T01:38:50Z` `DISMISSED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3554866243)
- `2025-12-09T06:30:35Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3555698899)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8_utils.py`: 9 inline comment(s)
- `python/sglang/srt/managers/scheduler.py`: 4 inline comment(s)
- `test/srt/test_fp8_blockwise_gemm.py`: 4 inline comment(s)
- `python/sglang/srt/server_args.py`: 3 inline comment(s)
- `docs/references/environment_variables.md`: 3 inline comment(s)
- `python/sglang/srt/utils/common.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-04T04:33:29Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: benchmark, blackwell, block, cutlass, flashinfer, fp8, gemm, hang; excerpt: "Pull request overview This PR adds a new CLI flag --fp8-gemm-runner-backend (with alias --fp8-gemm-backend) to allow users to explicitly configure the FP8 GEMM backend ..." (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3538002604)
- `2025-12-04T20:51:13Z` `issue` by `Fridge003`; signals: blackwell, cutlass, deepgemm, flashinfer, fp8, gemm, kernel, triton; excerpt: "Also please add a per-commit CI test (on 4-GPU Blackwell) for fp8 gemm. It should cover Triton/DeepGemm/Flashinfer/TRTLLM kernels (cutlass is unimportant), and uses qwen3-fp8 ..." (https://github.com/sgl-project/sglang/pull/14379#issuecomment-3614274133)
- `2025-12-09T01:38:47Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/fp8_utils.py`:253; signals: accuracy, blackwell, cutlass, deepgemm, flashinfer, fp8, gemm; excerpt: "Please put deepgemm backend after flashinfer/cutlass backend. Since on Blackwell deepgemm can only be applied to ue8m0 scale, and might cause accuracy drops on ..." (https://github.com/sgl-project/sglang/pull/14379#discussion_r2600741401)
- `2025-12-06T00:42:04Z` `inline` by `copilot-pull-request-reviewer` `test/srt/test_fp8_blockwise_gemm.py`:68; signals: b200, block, fp4, fp8, gemm, triton; excerpt: "The class name TestFp8BlockwiseGemmTriton uses lowercase Fp8, which is inconsistent with the codebase convention. Based on similar test classes (e.g., TestLlama31FP4B200 in test llama31 ..." (https://github.com/sgl-project/sglang/pull/14379#discussion_r2594293528)
- `2025-12-06T00:42:04Z` `inline` by `copilot-pull-request-reviewer` `test/srt/test_fp8_blockwise_gemm.py`:63; signals: b200, block, deepgemm, fp4, fp8, gemm; excerpt: "The class name TestFp8BlockwiseGemmDeepGemm uses lowercase Fp8, which is inconsistent with the codebase convention. Based on similar test classes (e.g., TestLlama31FP4B200 in test llama31 ..." (https://github.com/sgl-project/sglang/pull/14379#discussion_r2594293543)
- `2025-12-06T00:42:04Z` `inline` by `copilot-pull-request-reviewer` `test/srt/test_fp8_blockwise_gemm.py`:68; signals: b200, block, flashinfer, fp4, fp8, gemm; excerpt: "The class name TestFp8BlockwiseGemmFlashinferTrtllm uses lowercase Fp8, which is inconsistent with the codebase convention. Based on similar test classes (e.g., TestLlama31FP4B200 in test llama31 ..." (https://github.com/sgl-project/sglang/pull/14379#discussion_r2594293550)
- `2025-12-04T04:53:38Z` `inline` by `copilot-pull-request-reviewer` `python/sglang/srt/server_args.py`:2974; signals: attention, fp8, gemm, hang, moe; excerpt: "The CLI flag name --fp8-gemm-backend should map to internal field name fp8 gemm backend for consistency with other backend flags (e.g., --moe-runner-backend → moe ..." (https://github.com/sgl-project/sglang/pull/14379#discussion_r2587525501)
- `2025-12-06T00:42:04Z` `inline` by `copilot-pull-request-reviewer` `test/srt/test_fp8_blockwise_gemm.py`:17; signals: b200, block, fp4, fp8, gemm; excerpt: "The class name Fp8BlockwiseGemmBase uses lowercase Fp8, which is inconsistent with the codebase convention. Based on similar test classes (e.g., TestLlama31FP4B200 in test llama31 ..." (https://github.com/sgl-project/sglang/pull/14379#discussion_r2594293521)
- `2025-12-06T00:42:05Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: flashinfer, fp8, gemm, hang; excerpt: "Pull request overview Copilot reviewed 10 out of 10 changed files in this pull request and generated 4 comments. Comments suppressed due to low ..." (https://github.com/sgl-project/sglang/pull/14379#pullrequestreview-3546798152)
- `2025-12-05T23:18:44Z` `issue` by `b8zhong`; signals: deepgemm, flashinfer, fp8, gemm, triton; excerpt: "New test covers DeepGEMM/Triton/Flashinfer TRTLLM impl on Qwen/Qwen3-4B-Instruct-2507-FP8: DeepGEMM Flashinfer TRTLLM Triton" (https://github.com/sgl-project/sglang/pull/14379#issuecomment-3618937738)
- `2025-12-08T03:10:40Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/fp8_utils.py`:252; signals: flashinfer, fp8, gemm, hang; excerpt: "Can we handle the two deprecated environs here? For example, if the user passes in SGLANG ENABLE FLASHINFER FP8 GEMM, we need to set ..." (https://github.com/sgl-project/sglang/pull/14379#discussion_r2596904195)
- `2025-12-05T18:48:10Z` `issue` by `Fridge003`; signals: flashinfer, fp8, gemm, hang; excerpt: "cc @kaixih @leejnau We might need to fix some documents/recipes after this change, since the flashinfer fp8 gemm environ var is deprecated." (https://github.com/sgl-project/sglang/pull/14379#issuecomment-3618117254)
