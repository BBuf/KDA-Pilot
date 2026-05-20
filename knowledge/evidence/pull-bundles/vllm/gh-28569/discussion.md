# PR Discussion Digest

- Source PR: [vllm-project/vllm#28569](https://github.com/vllm-project/vllm/pull/28569)
- Source page: `sources/prs/vllm/PR-28569.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28569`
- Generated at: `2026-05-20T15:38:29.441688+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-12T17:20:32Z`
- Merged: `2025-11-17T02:02:42Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 9 (approved=2, commented=7)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=2
- Human participants with discussion text: jiahanc, mgoin, pavanimajety, yewentao256
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-12T19:23:16Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/28569#pullrequestreview-3455076200)
- `2025-11-12T19:25:04Z` `COMMENTED` by `jiahanc` (https://github.com/vllm-project/vllm/pull/28569#pullrequestreview-3455081589)
- `2025-11-12T19:39:02Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/28569#pullrequestreview-3455132776)
- `2025-11-13T02:55:01Z` `COMMENTED` by `jiahanc` (https://github.com/vllm-project/vllm/pull/28569#pullrequestreview-3456912159)
- `2025-11-13T22:33:09Z` `COMMENTED` by `yewentao256` - Thanks for the work! (https://github.com/vllm-project/vllm/pull/28569#pullrequestreview-3461956998)
- `2025-11-13T22:44:00Z` `COMMENTED` by `jiahanc` (https://github.com/vllm-project/vllm/pull/28569#pullrequestreview-3461997789)
- `2025-11-13T22:45:15Z` `COMMENTED` by `jiahanc` (https://github.com/vllm-project/vllm/pull/28569#pullrequestreview-3462003068)
- `2025-11-13T23:10:08Z` `APPROVED` by `pavanimajety` - Thanks for the fix, LGTM. (https://github.com/vllm-project/vllm/pull/28569#pullrequestreview-3462085540)
- `2025-11-14T17:46:19Z` `APPROVED` by `mgoin` - LGTM, thank you (https://github.com/vllm-project/vllm/pull/28569#pullrequestreview-3466065128)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/modelopt.py`: 8 inline comment(s)

## High-Signal Discussion

- `2025-11-12T19:39:02Z` `inline` by `pavanimajety` `vllm/model_executor/layers/quantization/modelopt.py`:1657; signals: block, flashinfer, fp4, fp8, moe; excerpt: "should we leave instead leave this abstraction to be handled inside flashinfer implementation of trtllm fp4 block scale moe and potentially trtllm fp8 block ..." (https://github.com/vllm-project/vllm/pull/28569#discussion_r2519559000)
- `2025-11-12T19:25:04Z` `inline` by `jiahanc` `vllm/model_executor/layers/quantization/modelopt.py`:942; signals: flashinfer, hang; excerpt: "it is default when flashinfer is installed. Made a mistake in the code change, fixed now" (https://github.com/vllm-project/vllm/pull/28569#discussion_r2519521443)
- `2025-11-13T02:55:01Z` `inline` by `jiahanc` `vllm/model_executor/layers/quantization/modelopt.py`:1657; signals: flashinfer; excerpt: "agree, will update on flashinfer side but before that let's keep it here :)" (https://github.com/vllm-project/vllm/pull/28569#discussion_r2521034694)
- `2025-11-13T22:45:15Z` `inline` by `jiahanc` `vllm/model_executor/layers/quantization/modelopt.py`:1691; signals: flashinfer; excerpt: "Yes, the flashinfer has recently supports None as input and logic of none is updated in C++ code" (https://github.com/vllm-project/vllm/pull/28569#discussion_r2525171028)
- `2025-11-13T22:33:09Z` `review` `COMMENTED` by `yewentao256`; signals: general review; excerpt: "Thanks for the work!" (https://github.com/vllm-project/vllm/pull/28569#pullrequestreview-3461956998)
- `2025-11-13T22:33:02Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/modelopt.py`:1660; signals: general review; excerpt: "Seems different with original logic as well, use llama4 routing to float32, now we need DeepSeekV3 as well?" (https://github.com/vllm-project/vllm/pull/28569#discussion_r2525142829)
- `2025-11-13T22:44:00Z` `inline` by `jiahanc` `vllm/model_executor/layers/quantization/modelopt.py`:1660; signals: general review; excerpt: "The logic is the same. Previously only support DS V3 and Llam4 routing. DS V3 requires float32, that's why original is Only convert to ..." (https://github.com/vllm-project/vllm/pull/28569#discussion_r2525167322)
- `2025-11-12T19:23:16Z` `inline` by `pavanimajety` `vllm/model_executor/layers/quantization/modelopt.py`:942; signals: general review; excerpt: "we may want to do this as default or the final elif/else" (https://github.com/vllm-project/vllm/pull/28569#discussion_r2519517199)
- `2025-11-13T22:31:23Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/modelopt.py`:1691; signals: general review; excerpt: "Are we sure it is safe to delete the if else logic?" (https://github.com/vllm-project/vllm/pull/28569#discussion_r2525139231)
