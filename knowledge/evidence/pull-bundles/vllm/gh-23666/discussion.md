# PR Discussion Digest

- Source PR: [vllm-project/vllm#23666](https://github.com/vllm-project/vllm/pull/23666)
- Source page: `sources/prs/vllm/PR-23666.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23666`
- Generated at: `2026-05-20T15:37:35.071532+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-26T15:44:05Z`
- Merged: `2025-08-27T14:09:09Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 15 (approved=5, changes_requested=1, commented=9)
- Inline review comments: 7
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=5
- Human participants with discussion text: eric8810, mgoin, tlrmchlsmth, yewentao256, youkaichao
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-08-26T15:45:59Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for Hopper DeepGEMM E8M0, which was previously only enabled for Blackwell ... (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3156278527)
- `2025-08-26T16:16:45Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3156404778)
- `2025-08-26T16:17:48Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3156408278)
- `2025-08-26T16:18:05Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3156408866)
- `2025-08-26T17:35:51Z` `COMMENTED` by `mgoin` - We should test that this works without DeepGEMM if we should enable this by default for V3.1 Many ... (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3156654262)
- `2025-08-26T18:16:16Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3156793764)
- `2025-08-26T18:20:40Z` `CHANGES_REQUESTED` by `mgoin` - . (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3156804884)
- `2025-08-26T19:55:49Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3157114671)
- `2025-08-27T08:44:54Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3158912605)
- `2025-08-27T09:25:54Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3159043441)
- `2025-08-27T09:27:16Z` `APPROVED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3159047326)
- `2025-08-27T11:31:21Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3159403588)
- `2025-08-27T11:39:59Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3159430007)
- `2025-08-27T12:27:44Z` `APPROVED` by `mgoin` - LGTM, although we shouldn't need two environment variables for this. I hope we can clean up afterwards. (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3159578333)

## Inline Comment Hotspots

- `vllm/transformers_utils/config.py`: 5 inline comment(s)
- `vllm/utils/deep_gemm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-26T17:35:51Z` `review` `COMMENTED` by `mgoin`; signals: cutlass, deepgemm, gemm, hopper, triton; excerpt: "We should test that this works without DeepGEMM if we should enable this by default for V3.1 Many users won't have DeepGEMM installed and ..." (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3156654262)
- `2025-08-26T20:10:53Z` `issue` by `yewentao256`; signals: cutlass, deepgemm, gemm, hopper, triton; excerpt: "We should test that this works without DeepGEMM if we should enable this by default for V3.1 Many users won't have DeepGEMM installed and ..." (https://github.com/vllm-project/vllm/pull/23666#issuecomment-3225586852)
- `2025-08-26T16:09:01Z` `issue` by `yewentao256`; signals: b200, hopper; excerpt: "did this feature enable deepseek v3.1 running on B200? It is for Hopper, B200 should have been supported" (https://github.com/vllm-project/vllm/pull/23666#issuecomment-3224839439)
- `2025-08-26T19:55:49Z` `inline` by `yewentao256` `vllm/utils/deep_gemm.py`:54; signals: gemm; excerpt: "Fixed, thanks!" (https://github.com/vllm-project/vllm/pull/23666#discussion_r2302001961)
- `2025-08-26T18:20:40Z` `review` `CHANGES_REQUESTED` by `mgoin`; signals: general review; excerpt: "." (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3156804884)
- `2025-08-26T19:56:41Z` `issue` by `yewentao256`; signals: hopper; excerpt: "@mgoin Now we have env and config 1. set default False on Hopper 2. Read config from model first 3. If env set by ..." (https://github.com/vllm-project/vllm/pull/23666#issuecomment-3225547017)
- `2025-08-26T15:52:16Z` `issue` by `eric8810`; signals: b200; excerpt: "did this feature enable deepseek v3.1 running on B200?" (https://github.com/vllm-project/vllm/pull/23666#issuecomment-3224773536)
- `2025-08-27T08:44:54Z` `inline` by `youkaichao` `vllm/transformers_utils/config.py`:512; signals: general review; excerpt: "does it really work? envs do not support setting env var this way:" (https://github.com/vllm-project/vllm/pull/23666#discussion_r2303290322)
- `2025-08-27T12:27:44Z` `review` `APPROVED` by `mgoin`; signals: general review; excerpt: "LGTM, although we shouldn't need two environment variables for this. I hope we can clean up afterwards." (https://github.com/vllm-project/vllm/pull/23666#pullrequestreview-3159578333)
