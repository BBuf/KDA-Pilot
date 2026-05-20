# PR Discussion Digest

- Source PR: [vllm-project/vllm#29213](https://github.com/vllm-project/vllm/pull/29213)
- Source page: `sources/prs/vllm/PR-29213.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29213`
- Generated at: `2026-05-20T15:38:38.878131+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-22T00:21:52Z`
- Merged: `2026-01-07T15:53:54Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 11
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=2, outdated=3
- Human participants with discussion text: chatgpt-codex-connector, jhaotingc, mergify, robertgshaw2-redhat, yewentao256
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-12-11T20:20:32Z` `COMMENTED` by `yewentao256` - Thanks for the work! A few thoughts: 1. has nothing to do with deepgemm, please update the title ... (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3569156135)
- `2026-01-02T15:58:40Z` `COMMENTED` by `yewentao256` - Nice work! A few thoughts Also, please update the PR title and description to Flashinfer DeepGEMM, which is ... (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3623400372)
- `2026-01-05T21:35:32Z` `COMMENTED` by `jhaotingc` (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3628501042)
- `2026-01-05T21:44:48Z` `COMMENTED` by `jhaotingc` (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3628522529)
- `2026-01-05T21:44:59Z` `COMMENTED` by `jhaotingc` (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3628522948)
- `2026-01-06T21:45:32Z` `COMMENTED` by `yewentao256` - Thanks! A few more thoughts And please do not force push, it might swallow previous commits and comments (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3632625685)
- `2026-01-07T00:34:39Z` `COMMENTED` by `jhaotingc` (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3632956529)
- `2026-01-07T00:35:31Z` `COMMENTED` by `jhaotingc` (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3632958981)
- `2026-01-07T00:35:36Z` `COMMENTED` by `jhaotingc` (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3632959105)
- `2026-01-07T15:46:11Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! Maybe we can consider set VLLM BLOCKSCALE FP8 GEMM FLASHINFER default to True ... (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3635525111)
- `2026-01-07T15:53:47Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3635556101)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/fp8_utils.py`: 11 inline comment(s)

## High-Signal Discussion

- `2025-12-12T19:14:52Z` `issue` by `jhaotingc`; signals: accuracy, attention, block, deepgemm, flashinfer, fp8, gemm, h200; excerpt: "Purpose Per TRTLLM has fp8 gemm kernel swapAB kernel for blockscale FP8 gemm in linear layer. This PR (and FlashInfer PR brings the gemm ..." (https://github.com/vllm-project/vllm/pull/29213#issuecomment-3647807470)
- `2025-12-20T01:32:30Z` `issue` by `jhaotingc`; signals: accuracy, attention, benchmark, compile, deepgemm, flashinfer, fp8, gemm; excerpt: "Benchmarking DeepSeek-V3.1 8xH200 TP8 @ conc=4 Main with VLLM USE DEEP GEMM=1,VLLM MOE USE DEEP GEMM=0,VLLM USE DEEP GEMM E8M0=1 This PR with VLLM ..." (https://github.com/vllm-project/vllm/pull/29213#issuecomment-3677187669)
- `2026-01-05T21:44:48Z` `inline` by `jhaotingc` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:234; signals: compile, cuda, deepgemm, fp8, gemm, perf, performance; excerpt: "How would you like to split it? The main issue is that we need M 95). In order to keep this logic and still ..." (https://github.com/vllm-project/vllm/pull/29213#discussion_r2662891269)
- `2025-12-11T20:20:32Z` `review` `COMMENTED` by `yewentao256`; signals: benchmark, deepgemm, gemm, perf, performance; excerpt: "Thanks for the work! A few thoughts: 1. has nothing to do with deepgemm, please update the title and description 2. Please benchmark and ..." (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3569156135)
- `2026-01-02T15:55:42Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:234; signals: deepgemm, flashinfer, fp8, gemm; excerpt: "Could we split this function? I don't think it is a good idea to bind flashinfer deepgemm and real deepgemm together." (https://github.com/vllm-project/vllm/pull/29213#discussion_r2657953317)
- `2026-01-06T21:42:57Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:283; signals: deepgemm, flashinfer, fp8, gemm; excerpt: "Please comment with more context as we discussed before, and it is needed to pack deepgemm func and flashinfer func together" (https://github.com/vllm-project/vllm/pull/29213#discussion_r2666389435)
- `2026-01-02T15:58:40Z` `review` `COMMENTED` by `yewentao256`; signals: deepgemm, flashinfer, gemm; excerpt: "Nice work! A few thoughts Also, please update the PR title and description to Flashinfer DeepGEMM, which is not doing the swap with the ..." (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3623400372)
- `2026-01-06T21:33:21Z` `issue` by `jhaotingc`; signals: deepgemm, flashinfer, gemm, hang; excerpt: "Nice work! A few thoughts Also, please update the PR title and description to Flashinfer DeepGEMM, which is not doing the swap with the ..." (https://github.com/vllm-project/vllm/pull/29213#issuecomment-3716445276)
- `2026-01-07T15:46:11Z` `review` `APPROVED` by `yewentao256`; signals: block, flashinfer, fp8, gemm; excerpt: "LGTM, thanks for the work! Maybe we can consider set VLLM BLOCKSCALE FP8 GEMM FLASHINFER default to True as a following up PR (more ..." (https://github.com/vllm-project/vllm/pull/29213#pullrequestreview-3635525111)
- `2026-01-05T21:35:31Z` `inline` by `jhaotingc` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:333; signals: compile, fp8; excerpt: "This is a must have, for torch compile to do dummy run. I tried to use the plain function, but it broke at torch ..." (https://github.com/vllm-project/vllm/pull/29213#discussion_r2662871626)
- `2026-01-02T15:56:59Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:333; signals: fp8; excerpt: "Is this a must-have? If not compling related, we can directly call without registing a custom op" (https://github.com/vllm-project/vllm/pull/29213#discussion_r2657956674)
- `2026-01-05T21:44:59Z` `inline` by `jhaotingc` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:234; signals: fp8; excerpt: "And thanks for the review!!" (https://github.com/vllm-project/vllm/pull/29213#discussion_r2662891613)
