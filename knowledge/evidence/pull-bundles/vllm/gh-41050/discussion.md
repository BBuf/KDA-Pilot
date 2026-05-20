# PR Discussion Digest

- Source PR: [vllm-project/vllm#41050](https://github.com/vllm-project/vllm/pull/41050)
- Source page: `sources/prs/vllm/PR-41050.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-41050`
- Generated at: `2026-05-20T15:40:51.834849+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-27T21:03:14Z`
- Merged: `2026-05-01T03:37:44Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 8
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=3, outdated=4
- Human participants with discussion text: LopezCastroRoberto, ZJY0516, claude, juhi10071998, mergify, pavanimajety
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 6

## Review Decisions

- `2026-04-27T21:03:18Z` `COMMENTED` by `claude` - Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer ... (https://github.com/vllm-project/vllm/pull/41050#pullrequestreview-4184176407)
- `2026-04-27T21:05:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables GELU activation support for the TRTLLM NvFP4 MoE backend and introduces a ... (https://github.com/vllm-project/vllm/pull/41050#pullrequestreview-4184188482)
- `2026-04-28T10:14:34Z` `APPROVED` by `LopezCastroRoberto` - The PR looks clean and correct (https://github.com/vllm-project/vllm/pull/41050#pullrequestreview-4187726759)
- `2026-04-28T15:01:12Z` `COMMENTED` by `juhi10071998` (https://github.com/vllm-project/vllm/pull/41050#pullrequestreview-4189963552)
- `2026-04-29T21:16:30Z` `APPROVED` by `pavanimajety` - Thanks for the PR @juhi10071998! Looks good to me, let's link the Flashinfer issue for TP 4 here ... (https://github.com/vllm-project/vllm/pull/41050#pullrequestreview-4200779174)

## Inline Comment Hotspots

- `tests/kernels/moe/test_trtllm_nvfp4_moe.py`: 6 inline comment(s)
- `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-28T15:01:11Z` `inline` by `juhi10071998` `tests/kernels/moe/test_trtllm_nvfp4_moe.py`:202; signals: bf16, correctness, cutlass, fp4, kernel, moe, nvfp4; excerpt: "yes, that's something I noted as well. The new test uses tolerances chosen from data, not bumped from a prior baseline — TRT-LLM × ..." (https://github.com/vllm-project/vllm/pull/41050#discussion_r3155125153)
- `2026-04-30T16:30:51Z` `issue` by `juhi10071998`; signals: flashinfer, fp4, gemm, moe, nvfp4; excerpt: "Currently vLLM/ Flashinfer fails when running the nvfp4 Gemma4-26 MoE ckpts with TP=4 only (no EP) configuration. Opened an issue in the Flashinfer with ..." (https://github.com/vllm-project/vllm/pull/41050#issuecomment-4354274834)
- `2026-04-28T10:13:35Z` `inline` by `LopezCastroRoberto` `tests/kernels/moe/test_trtllm_nvfp4_moe.py`:202; signals: fp4, kernel, moe, nvfp4; excerpt: "nit: is it actually needed to increase tolerances w.r.t. other equivalent tests? e.g.," (https://github.com/vllm-project/vllm/pull/41050#discussion_r3153227567)
- `2026-04-29T21:37:58Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @juhi10071998, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/41050#issuecomment-4347687292)
- `2026-04-27T21:03:18Z` `review` `COMMENTED` by `claude`; signals: general review; excerpt: "Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer can comment @claude review to run ..." (https://github.com/vllm-project/vllm/pull/41050#pullrequestreview-4184176407)
- `2026-04-29T21:16:30Z` `review` `APPROVED` by `pavanimajety`; signals: flashinfer; excerpt: "Thanks for the PR @juhi10071998! Looks good to me, let's link the Flashinfer issue for TP 4 here so that it is trackable!" (https://github.com/vllm-project/vllm/pull/41050#pullrequestreview-4200779174)
