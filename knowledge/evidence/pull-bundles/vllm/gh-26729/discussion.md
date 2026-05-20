# PR Discussion Digest

- Source PR: [vllm-project/vllm#26729](https://github.com/vllm-project/vllm/pull/26729)
- Source page: `sources/prs/vllm/PR-26729.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-26729`
- Generated at: `2026-05-20T15:38:08.236765+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-13T19:19:56Z`
- Merged: `2025-10-21T05:51:14Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 12 (approved=2, commented=10)
- Inline review comments: 10
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=1, outdated=4
- Human participants with discussion text: bnellnm, chatgpt-codex-connector, mergify, mgoin, nvpohanh, varun-sundar-rabindranath
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-10-13T19:22:24Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces fixes for running gpt-oss with w4a8 quantization on B200 hardware, specifically addressing ... (https://github.com/vllm-project/vllm/pull/26729#pullrequestreview-3332774820)
- `2025-10-13T19:26:19Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/26729#pullrequestreview-3332783461)
- `2025-10-13T19:37:10Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/26729#pullrequestreview-3332809614)
- `2025-10-13T19:39:18Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/26729#pullrequestreview-3332823866)
- `2025-10-13T19:52:09Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/26729#pullrequestreview-3332877288)
- `2025-10-13T20:16:51Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/26729#pullrequestreview-3332936940)
- `2025-10-16T18:49:07Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/26729#pullrequestreview-3346498648)
- `2025-10-16T19:02:29Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/26729#pullrequestreview-3346570963)
- `2025-10-16T19:04:04Z` `APPROVED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/26729#pullrequestreview-3346580546)
- `2025-10-16T20:50:37Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/26729#pullrequestreview-3346965405)
- `2025-10-20T23:46:27Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/26729#pullrequestreview-3358323141)

## Inline Comment Hotspots

- `vllm/model_executor/warmup/kernel_warmup.py`: 5 inline comment(s)
- `vllm/model_executor/layers/fused_moe/config.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-10-16T18:49:06Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/config.py`:522; signals: dtype, fp4, fp8, hang, moe, mxfp4; excerpt: "Yeah. The hurdle is that the weights are mxfp4 but the quant dtype for the a8 part is mxfp8. I can change it to, ..." (https://github.com/vllm-project/vllm/pull/26729#discussion_r2437102309)
- `2025-10-13T19:39:18Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/config.py`:537; signals: block, fp4, moe, mxfp4; excerpt: "Canonically for mxfp4 we don't provide a block shape as the block shape of 32 is in the mxfp4 standard itself and it is ..." (https://github.com/vllm-project/vllm/pull/26729#discussion_r2427177446)
- `2025-10-13T19:26:19Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/fused_moe/config.py`:537; signals: block, kernel, moe; excerpt: "tensor, pplx prepare finalize.moe kernel quantize input still sees block shape=None and validate scale shape asserts that non‑per‑token quantization must have exactly one scale. ..." (https://github.com/vllm-project/vllm/pull/26729#discussion_r2427149948)
- `2025-10-13T19:51:59Z` `inline` by `mgoin` `vllm/model_executor/warmup/kernel_warmup.py`:39; signals: blackwell, kernel, moe; excerpt: "We should add a skip failling test case to tests/quantization/test blackwell moe.py to keep track of known failures" (https://github.com/vllm-project/vllm/pull/26729#discussion_r2427211259)
- `2025-10-16T20:50:37Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/warmup/kernel_warmup.py`:39; signals: blackwell, cute, kernel; excerpt: "Done 👍 Updated blackwell tests to execute these cases. PTAL! Thanks!" (https://github.com/vllm-project/vllm/pull/26729#discussion_r2437436588)
- `2025-10-13T20:16:51Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/config.py`:522; signals: dtype, moe; excerpt: "I think quant dtype and weight dtype should be hardcoded since the name of the function implies particular types." (https://github.com/vllm-project/vllm/pull/26729#discussion_r2427255571)
- `2025-10-13T19:37:10Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/warmup/kernel_warmup.py`:34; signals: kernel; excerpt: "The error I am seeing in this case, My plan is to create an issue for this, when this PR lands. cc @mgoin" (https://github.com/vllm-project/vllm/pull/26729#discussion_r2427168664)
- `2025-10-13T19:26:19Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Your team has set up Codex ..." (https://github.com/vllm-project/vllm/pull/26729#pullrequestreview-3332783461)
- `2025-10-16T19:02:29Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/config.py`:522; signals: moe; excerpt: "I think the explicit name with no type parameters is a little clearer." (https://github.com/vllm-project/vllm/pull/26729#discussion_r2437153975)
- `2025-10-16T20:46:35Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @varun-sundar-rabindranath." (https://github.com/vllm-project/vllm/pull/26729#issuecomment-3412785691)
