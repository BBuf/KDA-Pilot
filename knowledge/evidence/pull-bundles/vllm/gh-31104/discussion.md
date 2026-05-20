# PR Discussion Digest

- Source PR: [vllm-project/vllm#31104](https://github.com/vllm-project/vllm/pull/31104)
- Source page: `sources/prs/vllm/PR-31104.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-31104`
- Generated at: `2026-05-20T15:39:14.219192+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-22T00:44:31Z`
- Merged: `2026-01-07T06:49:40Z`

## Discussion Counts

- Issue comments: 17
- Review submissions: 19 (approved=1, commented=17, dismissed=1)
- Inline review comments: 12
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=2
- Human participants with discussion text: HollowMan6, chatgpt-codex-connector, copilot-pull-request-reviewer, hmellor, jeejeelee
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-12-22T00:52:42Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a bug in weight loading for FusedMoE layers when LoRA is enabled. ... (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3602188440)
- `2025-12-22T00:55:32Z` `COMMENTED` by `HollowMan6` (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3602191110)
- `2025-12-22T01:26:28Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3602219514)
- `2025-12-22T12:46:52Z` `COMMENTED` by `HollowMan6` (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3603964013)
- `2025-12-23T10:30:58Z` `DISMISSED` by `hmellor` - We should not be duplicating this code in every model. It should be abstracted to a util. Also, ... (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3607498298)
- `2025-12-24T02:15:43Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3609747961)
- `2025-12-24T09:04:16Z` `COMMENTED` by `HollowMan6` (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3610383492)
- `2025-12-24T15:29:07Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3611248337)
- `2025-12-24T18:08:27Z` `COMMENTED` by `HollowMan6` (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3611431397)
- `2025-12-25T01:00:27Z` `APPROVED` by `jeejeelee` - LGTM once CI is green (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3611704695)
- `2025-12-30T01:52:34Z` `COMMENTED` by `copilot-pull-request-reviewer` - Copilot encountered an error and was unable to review this pull request. You can try again by re-requesting ... (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3617098188)
- `2025-12-30T11:41:30Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a fix for loading LoRA weights for experts in MoE models. The ... (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3617969249)
- `2025-12-30T13:54:16Z` `COMMENTED` by `copilot-pull-request-reviewer` - Copilot encountered an error and was unable to review this pull request. You can try again by re-requesting ... (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3618313203)
- `2026-01-02T14:55:57Z` `COMMENTED` by `hmellor` - My original concerns have been addressed so I'll dismiss my blocking review. I have had a thought though. ... (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3623294444)
- `2026-01-03T22:05:16Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request fixes an issue with loading LoRA weights for experts by correctly handling the ... (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3624576707)
- `2026-01-03T22:06:24Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview Copilot reviewed 35 out of 35 changed files in this pull request and generated no ... (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3624577014)
- `2026-01-03T22:08:01Z` `COMMENTED` by `HollowMan6` (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3624577479)
- `2026-01-03T22:08:42Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. Reviewed commit: 0b4bd65a4b ℹ️ About ... (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3624577646)
- `2026-01-03T22:11:09Z` `COMMENTED` by `HollowMan6` (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3624578215)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 12 inline comment(s)

## High-Signal Discussion

- `2026-01-03T22:08:42Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/fused_moe/layer.py`:2041; signals: attention, moe, regression; excerpt: ", and appends that suffix to every checkpoint key (weight name). For LoRA configurations that patch other modules (e.g., attention/embeddings) but do not wrap ..." (https://github.com/vllm-project/vllm/pull/31104#discussion_r2659177277)
- `2026-01-02T14:55:57Z` `review` `COMMENTED` by `hmellor`; signals: block, moe; excerpt: "My original concerns have been addressed so I'll dismiss my blocking review. I have had a thought though. It seems like this logic should ..." (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3623294444)
- `2025-12-22T01:26:28Z` `inline` by `jeejeelee` `vllm/model_executor/layers/fused_moe/layer.py`:2038; signals: hang, moe; excerpt: "Can you test [test qwen3moe tp]( locally? Generally, enabling LoRA doesn't require changing the base model's layer names" (https://github.com/vllm-project/vllm/pull/31104#discussion_r2638311196)
- `2025-12-24T18:08:27Z` `inline` by `HollowMan6` `vllm/model_executor/layers/fused_moe/layer.py`:2038; signals: hang, moe; excerpt: "Thank you for pointing this out, @jeejeelee ! I didn't notice that importing vllm.model executor.model loader.weight utils directly in vllm/model executor/layers/fused moe/layer.py will cause ..." (https://github.com/vllm-project/vllm/pull/31104#discussion_r2646121444)
- `2026-01-03T22:06:24Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: hang; excerpt: "Pull request overview Copilot reviewed 35 out of 35 changed files in this pull request and generated no new comments. --- 💡 Add Copilot ..." (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3624577014)
- `2025-12-22T12:46:52Z` `inline` by `HollowMan6` `vllm/model_executor/layers/fused_moe/layer.py`:2038; signals: moe; excerpt: "Hi @jeejeelee, thank you for reviewing and pointing this out, originally I was intended for solutions like but later I though this is not ..." (https://github.com/vllm-project/vllm/pull/31104#discussion_r2639778413)
- `2025-12-24T02:15:42Z` `inline` by `jeejeelee` `vllm/model_executor/layers/fused_moe/layer.py`:2038; signals: moe; excerpt: "The issue here is that, for during the weight update (refit), with lora, when the weight has already loaded and we want to update ..." (https://github.com/vllm-project/vllm/pull/31104#discussion_r2644628451)
- `2025-12-24T09:04:16Z` `inline` by `HollowMan6` `vllm/model_executor/layers/fused_moe/layer.py`:2038; signals: moe; excerpt: "Non-experts linear layers also have .base layer in weight names, and they don't have any issue. The actual bug is not related to the ..." (https://github.com/vllm-project/vllm/pull/31104#discussion_r2645192438)
- `2025-12-24T15:29:07Z` `inline` by `jeejeelee` `vllm/model_executor/layers/fused_moe/layer.py`:2038; signals: moe; excerpt: "Thank you very much for your patient explanation. I misunderstood before, and now I think these modifications are ok, but could you test it ..." (https://github.com/vllm-project/vllm/pull/31104#discussion_r2645934948)
- `2026-01-03T22:11:09Z` `inline` by `HollowMan6` `vllm/model_executor/layers/fused_moe/layer.py`:2041; signals: moe; excerpt: "In vLLM, all-linear will be used for base models so that LoRA request can work, so this should be fine." (https://github.com/vllm-project/vllm/pull/31104#discussion_r2659178202)
- `2025-12-22T00:55:31Z` `inline` by `HollowMan6` `vllm/model_executor/layers/fused_moe/layer.py`:2041; signals: moe; excerpt: "This is not correct" (https://github.com/vllm-project/vllm/pull/31104#discussion_r2638283219)
- `2025-12-30T01:52:34Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: general review; excerpt: "Copilot encountered an error and was unable to review this pull request. You can try again by re-requesting a review." (https://github.com/vllm-project/vllm/pull/31104#pullrequestreview-3617098188)
