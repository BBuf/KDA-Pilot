# PR Discussion Digest

- Source PR: [vllm-project/vllm#30336](https://github.com/vllm-project/vllm/pull/30336)
- Source page: `sources/prs/vllm/PR-30336.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-30336`
- Generated at: `2026-05-20T15:38:59.292716+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-09T12:41:37Z`
- Merged: `2025-12-10T01:17:26Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 9 (approved=3, commented=6)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: ElizaWszola, bnellnm, chatgpt-codex-connector, jhaotingc, mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-12-09T12:43:11Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to fix compilation issues for fp8 DeepGemm by refactoring how device capabilities ... (https://github.com/vllm-project/vllm/pull/30336#pullrequestreview-3557221183)
- `2025-12-09T15:05:08Z` `COMMENTED` by `yewentao256` - Why is deepgemm e8m0 could not be used? If it is because of the @cache, I am thinking ... (https://github.com/vllm-project/vllm/pull/30336#pullrequestreview-3557944859)
- `2025-12-09T17:18:16Z` `APPROVED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/30336#pullrequestreview-3558638428)
- `2025-12-09T21:36:49Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/30336#pullrequestreview-3559846130)
- `2025-12-10T00:58:24Z` `COMMENTED` by `jhaotingc` (https://github.com/vllm-project/vllm/pull/30336#pullrequestreview-3560304045)
- `2025-12-10T00:58:44Z` `COMMENTED` by `jhaotingc` (https://github.com/vllm-project/vllm/pull/30336#pullrequestreview-3560304542)
- `2025-12-10T01:17:16Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/30336#pullrequestreview-3560337412)
- `2025-12-10T01:17:21Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/30336#pullrequestreview-3560337864)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/fp8_utils.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-12-09T15:05:08Z` `review` `COMMENTED` by `yewentao256`; signals: blackwell, cache, deepgemm, gemm; excerpt: "Why is deepgemm e8m0 could not be used? If it is because of the @cache, I am thinking we should have something like instead ..." (https://github.com/vllm-project/vllm/pull/30336#pullrequestreview-3557944859)
- `2025-12-09T15:49:14Z` `issue` by `yewentao256`; signals: block, cache, deepgemm, fp8, gemm; excerpt: "@yewentao256 It's because of torch. dynamo.exc.Unsupported: can't handle functions not implemented in python - this is the error I had also run into a ..." (https://github.com/vllm-project/vllm/pull/30336#issuecomment-3632960722)
- `2025-12-10T01:17:16Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:272; signals: blackwell, fp8; excerpt: "IIUC this is specifically for the case where e8m0 scales need to be packed , which is a Blackwell only case" (https://github.com/vllm-project/vllm/pull/30336#discussion_r2604866882)
- `2025-12-10T00:58:24Z` `inline` by `jhaotingc` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:272; signals: fp8, hopper; excerpt: "Shouldn't e8m0 also compatible with hopper?" (https://github.com/vllm-project/vllm/pull/30336#discussion_r2604839317)
- `2025-12-09T15:12:22Z` `issue` by `ElizaWszola`; signals: block, fp8; excerpt: "@yewentao256 It's because of torch. dynamo.exc.Unsupported: can't handle functions not implemented in python - this is the error I had also run into a ..." (https://github.com/vllm-project/vllm/pull/30336#issuecomment-3632782435)
- `2025-12-09T16:14:18Z` `issue` by `ElizaWszola`; signals: hang, perf; excerpt: "@yewentao256 Isn't from oracle() a static method? Alternatively, before cleaning up this PR, I had implemented this kind of changes: but this felt a ..." (https://github.com/vllm-project/vllm/pull/30336#issuecomment-3633088468)
- `2025-12-09T20:16:28Z` `issue` by `yewentao256`; signals: hang, perf; excerpt: "@yewentao256 Isn't from oracle() a static method? Alternatively, before cleaning up this PR, I had implemented this kind of changes: [aea97d1]( but this felt ..." (https://github.com/vllm-project/vllm/pull/30336#issuecomment-3634092569)
- `2025-12-10T00:58:44Z` `inline` by `jhaotingc` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:272; signals: fp8; excerpt: "cc @yewentao256 , thanks!" (https://github.com/vllm-project/vllm/pull/30336#discussion_r2604839774)
- `2025-12-09T12:41:43Z` `issue` by `chatgpt-codex-connector`; signals: general review; excerpt: "Codex usage limits have been reached for code reviews. Please check with the admins of this repo to increase the limits by adding credits." (https://github.com/vllm-project/vllm/pull/30336#issuecomment-3632071136)
