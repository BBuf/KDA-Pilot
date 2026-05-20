# PR Discussion Digest

- Source PR: [vllm-project/vllm#33506](https://github.com/vllm-project/vllm/pull/33506)
- Source page: `sources/prs/vllm/PR-33506.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-33506`
- Generated at: `2026-05-20T15:39:38.979252+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-01T08:58:11Z`
- Merged: `2026-02-12T21:06:58Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 11
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=0, outdated=5
- Human participants with discussion text: amitz-nv, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-01T09:00:06Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for non-gated Mixture of Experts (MoE) models using FlashInfer with FP8 ... (https://github.com/vllm-project/vllm/pull/33506#pullrequestreview-3735284272)
- `2026-02-10T23:34:38Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/33506#pullrequestreview-3782148527)
- `2026-02-11T15:23:20Z` `COMMENTED` by `amitz-nv` (https://github.com/vllm-project/vllm/pull/33506#pullrequestreview-3785505977)
- `2026-02-11T18:08:05Z` `COMMENTED` by `amitz-nv` (https://github.com/vllm-project/vllm/pull/33506#pullrequestreview-3786422791)
- `2026-02-11T18:21:13Z` `COMMENTED` by `amitz-nv` (https://github.com/vllm-project/vllm/pull/33506#pullrequestreview-3786499447)
- `2026-02-12T10:34:15Z` `COMMENTED` by `amitz-nv` (https://github.com/vllm-project/vllm/pull/33506#pullrequestreview-3790098979)
- `2026-02-12T17:41:40Z` `APPROVED` by `mgoin` - LGTM nice work! Will manually trigger MoE refactor tests (https://github.com/vllm-project/vllm/pull/33506#pullrequestreview-3792587312)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`: 5 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`: 4 inline comment(s)
- `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/modelopt.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-10T23:34:22Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`:513; signals: block, flashinfer, fp4, moe, nvfp4; excerpt: "If we are in NVFP4, why would we expect weight block size in any case?" (https://github.com/vllm-project/vllm/pull/33506#discussion_r2790779002)
- `2026-02-11T15:23:20Z` `inline` by `amitz-nv` `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`:513; signals: flashinfer, fp4, fp8, moe; excerpt: "It was copied from the FP8 flow, removing it" (https://github.com/vllm-project/vllm/pull/33506#discussion_r2793903351)
- `2026-02-11T18:08:05Z` `inline` by `amitz-nv` `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`:427; signals: flashinfer, kernel, nan; excerpt: "That's what the current Flashinfer kernels require, otherwise it doesn't find a suitable kernel. For example, Nemotron 3 Nano TP=1 would fail unless it's ..." (https://github.com/vllm-project/vllm/pull/33506#discussion_r2794732506)
- `2026-02-10T23:29:31Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`:294; signals: flashinfer, moe; excerpt: "Let's remove the default value to always be explicit" (https://github.com/vllm-project/vllm/pull/33506#discussion_r2790767558)
- `2026-02-10T23:31:55Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`:36; signals: flashinfer, moe; excerpt: "Would be nice if we could have this use the MoEActivation refactor, hopefully landing soon" (https://github.com/vllm-project/vllm/pull/33506#discussion_r2790773288)
- `2026-02-12T10:16:10Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @amitz-nv, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/33506#issuecomment-3889966183)
- `2026-02-11T18:21:13Z` `inline` by `amitz-nv` `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`:36; signals: flashinfer; excerpt: "Nice, I definitely agree that refactor is necessary! Regarding the order, I think it depends on when the refactor PR is merged" (https://github.com/vllm-project/vllm/pull/33506#discussion_r2794787986)
- `2026-02-10T23:33:29Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`:427; signals: flashinfer; excerpt: "Is there some justification for 128 we can reference?" (https://github.com/vllm-project/vllm/pull/33506#discussion_r2790776956)
- `2026-02-12T10:34:15Z` `inline` by `amitz-nv` `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`:36; signals: flashinfer; excerpt: "Done" (https://github.com/vllm-project/vllm/pull/33506#discussion_r2798062408)
- `2026-02-12T17:41:40Z` `review` `APPROVED` by `mgoin`; signals: moe; excerpt: "LGTM nice work! Will manually trigger MoE refactor tests" (https://github.com/vllm-project/vllm/pull/33506#pullrequestreview-3792587312)
- `2026-02-12T17:41:07Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/modelopt.py`:943; signals: general review; excerpt: "Note: we need to update the compressed tensors side too, can do in followup PR" (https://github.com/vllm-project/vllm/pull/33506#discussion_r2800213286)
- `2026-02-01T08:58:46Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @amitz-nv." (https://github.com/vllm-project/vllm/pull/33506#issuecomment-3830665857)
