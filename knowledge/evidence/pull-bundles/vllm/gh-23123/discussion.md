# PR Discussion Digest

- Source PR: [vllm-project/vllm#23123](https://github.com/vllm-project/vllm/pull/23123)
- Source page: `sources/prs/vllm/PR-23123.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23123`
- Generated at: `2026-05-20T15:37:18.728286+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-18T17:40:08Z`
- Merged: `2025-08-30T04:36:48Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: josephrocca, mgoin, xyang16, yewentao256
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-08-18T17:45:03Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces the routed scaling factor to the MoE grouped top-k logic, which is ... (https://github.com/vllm-project/vllm/pull/23123#pullrequestreview-3129328895)
- `2025-08-25T20:14:54Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/23123#pullrequestreview-3152883392)
- `2025-08-25T20:18:24Z` `COMMENTED` by `mgoin` - LGTM overall, just would like some assertions or implementations added where the arg is ignored at the moment. ... (https://github.com/vllm-project/vllm/pull/23123#pullrequestreview-3152887482)
- `2025-08-25T20:26:16Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23123#pullrequestreview-3152912628)
- `2025-08-25T20:30:16Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/23123#pullrequestreview-3152931040)
- `2025-08-29T16:49:01Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/23123#pullrequestreview-3169412887)
- `2025-08-29T18:28:21Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! (https://github.com/vllm-project/vllm/pull/23123#pullrequestreview-3169675401)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-25T20:14:54Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py`:142; signals: moe; excerpt: "Maybe we could assert 1.0 here?" (https://github.com/vllm-project/vllm/pull/23123#discussion_r2299028242)
- `2025-08-25T20:15:54Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/layer.py`:628; signals: moe; excerpt: "Ditto" (https://github.com/vllm-project/vllm/pull/23123#discussion_r2299030225)
- `2025-08-25T20:18:24Z` `review` `COMMENTED` by `mgoin`; signals: general review; excerpt: "LGTM overall, just would like some assertions or implementations added where the arg is ignored at the moment. I think this would be helped ..." (https://github.com/vllm-project/vllm/pull/23123#pullrequestreview-3152887482)
- `2025-08-25T20:26:16Z` `inline` by `xyang16` `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py`:142; signals: moe; excerpt: "Yes that makes sense. Added assert." (https://github.com/vllm-project/vllm/pull/23123#discussion_r2299049789)
- `2025-08-25T20:30:16Z` `inline` by `xyang16` `vllm/model_executor/layers/fused_moe/layer.py`:628; signals: moe; excerpt: "Added assert. Thanks." (https://github.com/vllm-project/vllm/pull/23123#discussion_r2299063748)
- `2025-08-29T16:53:22Z` `issue` by `mgoin`; signals: moe; excerpt: "Could you run an eval on deepseek? A bit worried of leaving something behind here since we don't have great quantized moe tests at ..." (https://github.com/vllm-project/vllm/pull/23123#issuecomment-3237654442)
- `2025-08-26T17:28:11Z` `issue` by `xyang16`; signals: general review; excerpt: "@mgoin Since the routed scaling factor doesn't default to None in model config, see [here]( I still keep routed scaling factor default to 1.0, ..." (https://github.com/vllm-project/vllm/pull/23123#issuecomment-3225086662)
- `2025-08-29T16:56:25Z` `issue` by `xyang16`; signals: general review; excerpt: "Thanks for your review! I have run the eval based on this PR and combined. Eval result posted in Pasting result here as well: ..." (https://github.com/vllm-project/vllm/pull/23123#issuecomment-3237661042)
