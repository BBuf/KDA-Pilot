# PR Discussion Digest

- Source PR: [vllm-project/vllm#21733](https://github.com/vllm-project/vllm/pull/21733)
- Source page: `sources/prs/vllm/PR-21733.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21733`
- Generated at: `2026-05-20T15:36:51.453608+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-28T09:01:20Z`
- Merged: `2025-08-02T01:12:20Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 7
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: JartX, mgoin
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-28T09:02:17Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for GPTQ quantized Mixture-of-Experts (MoE) models on ROCm platforms. The changes ... (https://github.com/vllm-project/vllm/pull/21733#pullrequestreview-3061375114)
- `2025-07-28T12:19:29Z` `COMMENTED` by `mgoin` - Looks reasonable to me, thanks just one nit! (https://github.com/vllm-project/vllm/pull/21733#pullrequestreview-3062321761)
- `2025-07-28T12:30:09Z` `COMMENTED` by `JartX` (https://github.com/vllm-project/vllm/pull/21733#pullrequestreview-3062379724)
- `2025-07-28T14:07:35Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/21733#pullrequestreview-3062956909)
- `2025-07-28T14:31:42Z` `COMMENTED` by `JartX` (https://github.com/vllm-project/vllm/pull/21733#pullrequestreview-3063084145)
- `2025-07-29T07:46:56Z` `COMMENTED` by `JartX` (https://github.com/vllm-project/vllm/pull/21733#pullrequestreview-3066021847)
- `2025-08-02T01:11:24Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/21733#pullrequestreview-3080826364)
- `2025-08-02T01:12:09Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/21733#pullrequestreview-3080826563)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/gptq.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-07-28T14:31:42Z` `inline` by `JartX` `vllm/model_executor/layers/fused_moe/fused_moe.py`:763; signals: cuda, hang, moe, triton; excerpt: "Understood. I thought you wanted me to change only ROCM, for code style reasons. Yours makes more sense, because it only runs the code ..." (https://github.com/vllm-project/vllm/pull/21733#discussion_r2236741125)
- `2025-07-28T12:18:17Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/fused_moe.py`:763; signals: cuda, moe; excerpt: "Could you just add current platform.is cuda() to the existing conditional instead?" (https://github.com/vllm-project/vllm/pull/21733#discussion_r2236164301)
- `2025-07-29T07:46:55Z` `inline` by `JartX` `vllm/model_executor/layers/quantization/gptq.py`:169; signals: hang; excerpt: "@mgoin Excuse me for asking. I understand the style change — adding the PEP8 format seems to only add a space in the import. ..." (https://github.com/vllm-project/vllm/pull/21733#discussion_r2238857474)
- `2025-07-28T12:30:09Z` `inline` by `JartX` `vllm/model_executor/layers/fused_moe/fused_moe.py`:763; signals: moe; excerpt: "Sure! Done :)" (https://github.com/vllm-project/vllm/pull/21733#discussion_r2236209614)
- `2025-07-28T14:07:35Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/fused_moe.py`:763; signals: moe; excerpt: "Sorry for the misunderstanding, I meant just" (https://github.com/vllm-project/vllm/pull/21733#discussion_r2236644110)
- `2025-07-28T12:19:29Z` `review` `COMMENTED` by `mgoin`; signals: general review; excerpt: "Looks reasonable to me, thanks just one nit!" (https://github.com/vllm-project/vllm/pull/21733#pullrequestreview-3062321761)
- `2025-08-02T01:11:24Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/gptq.py`:169; signals: general review; excerpt: "I just use the precommit hook with Python 3.12" (https://github.com/vllm-project/vllm/pull/21733#discussion_r2249050902)
- `2025-08-01T23:07:49Z` `issue` by `JartX`; signals: general review; excerpt: "Hi @mgoin , sorry to bother you — do you know when this PR might be merged? Would it also be possible to address ..." (https://github.com/vllm-project/vllm/pull/21733#issuecomment-3145972047)
