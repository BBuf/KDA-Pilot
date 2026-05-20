# PR Discussion Digest

- Source PR: [vllm-project/vllm#22797](https://github.com/vllm-project/vllm/pull/22797)
- Source page: `sources/prs/vllm/PR-22797.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-22797`
- Generated at: `2026-05-20T15:37:11.958412+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-13T07:38:50Z`
- Merged: `2025-08-28T09:03:23Z`

## Discussion Counts

- Issue comments: 21
- Review submissions: 10 (approved=2, commented=8)
- Inline review comments: 10
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=3
- Human participants with discussion text: JartX, Readon, fernandaspets, mgoin, russellb, yewentao256
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 7

## Review Decisions

- `2025-08-13T07:40:43Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a TypeError during model loading by adding the return success parameter to ... (https://github.com/vllm-project/vllm/pull/22797#pullrequestreview-3114326001)
- `2025-08-16T15:57:03Z` `COMMENTED` by `JartX` (https://github.com/vllm-project/vllm/pull/22797#pullrequestreview-3125919284)
- `2025-08-25T20:26:27Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/22797#pullrequestreview-3152911374)
- `2025-08-25T22:02:52Z` `COMMENTED` by `JartX` (https://github.com/vllm-project/vllm/pull/22797#pullrequestreview-3153161715)
- `2025-08-25T22:04:24Z` `COMMENTED` by `JartX` (https://github.com/vllm-project/vllm/pull/22797#pullrequestreview-3153164034)
- `2025-08-26T03:17:52Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/22797#pullrequestreview-3153712836)
- `2025-08-26T07:47:41Z` `COMMENTED` by `JartX` (https://github.com/vllm-project/vllm/pull/22797#pullrequestreview-3154387972)
- `2025-08-26T08:01:37Z` `COMMENTED` by `JartX` (https://github.com/vllm-project/vllm/pull/22797#pullrequestreview-3154453967)
- `2025-08-26T13:46:47Z` `APPROVED` by `mgoin` - Thank you! (https://github.com/vllm-project/vllm/pull/22797#pullrequestreview-3155724498)
- `2025-08-26T15:30:26Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! (https://github.com/vllm-project/vllm/pull/22797#pullrequestreview-3156213294)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/moe_wna16.py`: 10 inline comment(s)

## High-Signal Discussion

- `2025-08-25T20:26:17Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/moe_wna16.py`:329; signals: dtype, moe; excerpt: "Why remove topk indices dtype?" (https://github.com/vllm-project/vllm/pull/22797#discussion_r2299049819)
- `2025-08-16T15:59:02Z` `issue` by `JartX`; signals: moe, triton; excerpt: "Hi @yewentao256 would you be so kind as to review the PR? required to be able to charge MOE GTPQ models with Triton, thank ..." (https://github.com/vllm-project/vllm/pull/22797#issuecomment-3193754221)
- `2025-08-16T15:57:03Z` `inline` by `JartX` `vllm/model_executor/layers/quantization/moe_wna16.py`:401; signals: moe; excerpt: "Solved here :" (https://github.com/vllm-project/vllm/pull/22797#discussion_r2280487285)
- `2025-08-25T20:25:54Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/moe_wna16.py`:183; signals: moe; excerpt: "You need to keep this around in order to match the new MoE interface" (https://github.com/vllm-project/vllm/pull/22797#discussion_r2299048611)
- `2025-08-25T20:26:08Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/moe_wna16.py`:310; signals: moe; excerpt: "Why remove the assert?" (https://github.com/vllm-project/vllm/pull/22797#discussion_r2299049387)
- `2025-08-25T22:02:52Z` `inline` by `JartX` `vllm/model_executor/layers/quantization/moe_wna16.py`:310; signals: moe; excerpt: "Readded" (https://github.com/vllm-project/vllm/pull/22797#discussion_r2299238701)
- `2025-08-25T22:04:24Z` `inline` by `JartX` `vllm/model_executor/layers/quantization/moe_wna16.py`:329; signals: moe; excerpt: "Readded" (https://github.com/vllm-project/vllm/pull/22797#discussion_r2299240590)
- `2025-08-26T03:17:35Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/moe_wna16.py`:163; signals: moe; excerpt: "I think this still isn't right, layer is not FusedMoEConfig" (https://github.com/vllm-project/vllm/pull/22797#discussion_r2299633633)
- `2025-08-26T07:47:41Z` `inline` by `JartX` `vllm/model_executor/layers/quantization/moe_wna16.py`:163; signals: moe; excerpt: "yep,kill me, many thanks!" (https://github.com/vllm-project/vllm/pull/22797#discussion_r2300112147)
- `2025-08-26T08:01:37Z` `inline` by `JartX` `vllm/model_executor/layers/quantization/moe_wna16.py`:163; signals: moe; excerpt: "solved here" (https://github.com/vllm-project/vllm/pull/22797#discussion_r2300155426)
- `2025-08-20T11:11:19Z` `issue` by `JartX`; signals: moe; excerpt: "@DarkLight1337 @tjtanaa Would you be so kind as to review the following PR? It prevents MOE from loading in ROCM with GPTQ, for example. ..." (https://github.com/vllm-project/vllm/pull/22797#issuecomment-3205689591)
- `2025-08-15T17:59:47Z` `issue` by `russellb`; signals: general review; excerpt: "Hi @russellb would you be so kind as to review this PR? Thank you very much for your time you've got some bot feedback ..." (https://github.com/vllm-project/vllm/pull/22797#issuecomment-3192320252)
