# PR Discussion Digest

- Source PR: [vllm-project/vllm#21533](https://github.com/vllm-project/vllm/pull/21533)
- Source page: `sources/prs/vllm/PR-21533.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21533`
- Generated at: `2026-05-20T15:36:45.087788+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-24T13:51:23Z`
- Merged: `2025-08-01T01:01:55Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 9
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: MatthewBonanni, mgoin, tlrmchlsmth, yewentao256
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-24T13:52:48Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds the DeepGEMM library to the vllm-base Docker image by building it from ... (https://github.com/vllm-project/vllm/pull/21533#pullrequestreview-3051777984)
- `2025-07-24T14:17:52Z` `COMMENTED` by `yewentao256` - Thanks for the work! Perhaps we can do one more step, testing with DeepGemm using vllm/tests/kernels/moe/test deepgemm.py (https://github.com/vllm-project/vllm/pull/21533#pullrequestreview-3051877343)
- `2025-07-24T14:28:56Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/21533#pullrequestreview-3051927053)
- `2025-07-24T16:15:11Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/21533#pullrequestreview-3052334480)
- `2025-07-24T16:16:59Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/21533#pullrequestreview-3052340514)
- `2025-07-24T16:41:42Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/21533#pullrequestreview-3052415844)
- `2025-07-24T16:58:11Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/21533#pullrequestreview-3052480490)
- `2025-07-29T14:38:37Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/21533#pullrequestreview-3067909666)
- `2025-07-29T17:04:05Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/21533#pullrequestreview-3068449534)
- `2025-07-30T16:52:34Z` `APPROVED` by `mgoin` - LGTM, let's make sure to enable the Blackwell runner on this PR before landing (https://github.com/vllm-project/vllm/pull/21533#pullrequestreview-3072545324)
- `2025-07-31T21:09:07Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/21533#pullrequestreview-3076890150)

## Inline Comment Hotspots

- `docker/Dockerfile`: 9 inline comment(s)

## High-Signal Discussion

- `2025-07-24T14:17:52Z` `review` `COMMENTED` by `yewentao256`; signals: deepgemm, gemm, kernel, moe; excerpt: "Thanks for the work! Perhaps we can do one more step, testing with DeepGemm using vllm/tests/kernels/moe/test deepgemm.py" (https://github.com/vllm-project/vllm/pull/21533#pullrequestreview-3051877343)
- `2025-07-24T13:53:34Z` `issue` by `MatthewBonanni`; signals: cuda, deepgemm, gemm, perf, performance; excerpt: "As shown above, DeepGEMM warns that CUDA =12.9 should be used for optimal performance. Bumping CUDA to 12.9 causes issues with the version of ..." (https://github.com/vllm-project/vllm/pull/21533#issuecomment-3113569001)
- `2025-07-24T14:18:43Z` `issue` by `yewentao256`; signals: cuda, deepgemm, gemm, perf, performance; excerpt: "As shown above, DeepGEMM warns that CUDA =12.9 should be used for optimal performance. Bumping CUDA to 12.9 causes issues with the version of ..." (https://github.com/vllm-project/vllm/pull/21533#issuecomment-3113659531)
- `2025-07-29T14:38:37Z` `inline` by `mgoin` `docker/Dockerfile`:440; signals: block, cuda, deepgemm, gemm; excerpt: "What is the minimum required CUDA version to build deepgemm? We also use this Dockerfile to build CUDA 11.8 and 12.6 images at the ..." (https://github.com/vllm-project/vllm/pull/21533#discussion_r2240085235)
- `2025-07-24T21:03:21Z` `issue` by `mgoin`; signals: cuda, deepgemm, gemm, hang; excerpt: "Maybe the torch arch changes are too invasive and we could just filter on CUDA version since that seems like a requirement for DeepGEMM? ..." (https://github.com/vllm-project/vllm/pull/21533#issuecomment-3114941687)
- `2025-07-24T16:16:56Z` `inline` by `mgoin` `docker/Dockerfile`:440; signals: cuda, deepgemm, gemm; excerpt: "Is there concern that installing DeepGEMM on a machine without CC 9.0 or 10.0 may cause issues? For instance should we condition this on ..." (https://github.com/vllm-project/vllm/pull/21533#discussion_r2228970325)
- `2025-07-24T14:17:05Z` `inline` by `yewentao256` `docker/Dockerfile`:445; signals: deepgemm, gemm; excerpt: "Are we intentionally use this instead of ./install.sh provided by DeepGemm?" (https://github.com/vllm-project/vllm/pull/21533#discussion_r2228660936)
- `2025-07-24T14:28:56Z` `inline` by `MatthewBonanni` `docker/Dockerfile`:445; signals: hang; excerpt: "install.sh does essentially the same thing except it uses pip instead of uv pip. I thought it would be better to use uv pip ..." (https://github.com/vllm-project/vllm/pull/21533#discussion_r2228694312)
- `2025-07-24T16:15:11Z` `inline` by `mgoin` `docker/Dockerfile`:445; signals: general review; excerpt: "Better to use uv, but could you leave a comment with a link to the file this is based on to reference for future ..." (https://github.com/vllm-project/vllm/pull/21533#discussion_r2228966634)
- `2025-07-30T16:52:34Z` `review` `APPROVED` by `mgoin`; signals: blackwell; excerpt: "LGTM, let's make sure to enable the Blackwell runner on this PR before landing" (https://github.com/vllm-project/vllm/pull/21533#pullrequestreview-3072545324)
- `2025-07-24T16:41:41Z` `inline` by `MatthewBonanni` `docker/Dockerfile`:445; signals: general review; excerpt: "Done" (https://github.com/vllm-project/vllm/pull/21533#discussion_r2229021130)
- `2025-07-24T16:58:11Z` `inline` by `MatthewBonanni` `docker/Dockerfile`:440; signals: general review; excerpt: "Done" (https://github.com/vllm-project/vllm/pull/21533#discussion_r2229065747)
