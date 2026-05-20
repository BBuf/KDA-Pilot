# PR Discussion Digest

- Source PR: [vllm-project/vllm#33695](https://github.com/vllm-project/vllm/pull/33695)
- Source page: `sources/prs/vllm/PR-33695.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-33695`
- Generated at: `2026-05-20T15:39:43.028542+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-03T12:55:19Z`
- Merged: `2026-03-27T13:25:02Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 11 (approved=3, commented=8)
- Inline review comments: 8
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: MatthewBonanni, hmellor, jmkuebler, mgoin, vkuzo
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-03T12:58:42Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a feature to selectively disable FP8 quantization for sliding window attention layers, ... (https://github.com/vllm-project/vllm/pull/33695#pullrequestreview-3745115436)
- `2026-03-03T14:53:20Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/33695#pullrequestreview-3883128255)
- `2026-03-04T09:43:58Z` `COMMENTED` by `jmkuebler` (https://github.com/vllm-project/vllm/pull/33695#pullrequestreview-3888280752)
- `2026-03-25T15:37:59Z` `APPROVED` by `mgoin` - LGTM! A lot cleaner. I do think we will want to rename this in the future, but I ... (https://github.com/vllm-project/vllm/pull/33695#pullrequestreview-4007715389)
- `2026-03-25T15:40:06Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/33695#pullrequestreview-4007736394)
- `2026-03-25T15:53:21Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/33695#pullrequestreview-4007839471)
- `2026-03-26T13:42:57Z` `COMMENTED` by `jmkuebler` (https://github.com/vllm-project/vllm/pull/33695#pullrequestreview-4014275290)
- `2026-03-26T13:44:25Z` `APPROVED` by `MatthewBonanni` - LGTM (https://github.com/vllm-project/vllm/pull/33695#pullrequestreview-4014288525)
- `2026-03-26T19:45:34Z` `COMMENTED` by `jmkuebler` (https://github.com/vllm-project/vllm/pull/33695#pullrequestreview-4016955321)
- `2026-03-26T19:55:39Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/33695#pullrequestreview-4017007145)
- `2026-03-26T19:56:26Z` `APPROVED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/33695#pullrequestreview-4017011744)

## Inline Comment Hotspots

- `vllm/model_executor/layers/attention/attention.py`: 6 inline comment(s)
- `vllm/engine/arg_utils.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-26T19:45:34Z` `inline` by `jmkuebler` `vllm/model_executor/layers/attention/attention.py`:262; signals: attention, cache, dtype, hang, kv cache, nan; excerpt: "@MatthewBonanni sorry when using vllm config.model config.dtype this results in an error that fails my unit test. the reason is that vllm config.model config.dtype ..." (https://github.com/vllm-project/vllm/pull/33695#discussion_r2997303252)
- `2026-02-04T08:21:15Z` `issue` by `jmkuebler`; signals: cache, fp8, kv cache, memory; excerpt: "@mgoin @vkuzo I reworked the argument a bit: - it is not specific to FP8 anymore, but only supports falling back to 'auto'. In ..." (https://github.com/vllm-project/vllm/pull/33695#issuecomment-3846019844)
- `2026-03-25T15:40:04Z` `inline` by `mgoin` `vllm/model_executor/layers/attention/attention.py`:262; signals: attention, dtype, nan; excerpt: "Actually falling back to "auto" might be an anti-pattern now since @MatthewBonanni is working on removing "auto" internally since we should resolve to a ..." (https://github.com/vllm-project/vllm/pull/33695#discussion_r2989158949)
- `2026-03-26T13:42:57Z` `inline` by `jmkuebler` `vllm/model_executor/layers/attention/attention.py`:262; signals: attention, dtype, nan; excerpt: "Thanks @MatthewBonanni and @mgoin . I updated it to use vllm config.model config.dtype" (https://github.com/vllm-project/vllm/pull/33695#discussion_r2994998230)
- `2026-02-03T16:37:29Z` `issue` by `mgoin`; signals: attention, dtype, fp8; excerpt: "I don't love the overly specific arg --skip-sliding-window-fp8, both wrt specifying sliding window or fp8. Could we have a more general approach for hybrid ..." (https://github.com/vllm-project/vllm/pull/33695#issuecomment-3842381725)
- `2026-02-03T17:26:41Z` `issue` by `jmkuebler`; signals: accuracy, attention, dtype; excerpt: "Thanks @mgoin for the feedback. I do agree its a bit specific. I think dtype map could be a good idea. Another option I ..." (https://github.com/vllm-project/vllm/pull/33695#issuecomment-3842647759)
- `2026-03-25T15:37:59Z` `review` `APPROVED` by `mgoin`; signals: cache, dtype, kv cache; excerpt: "LGTM! A lot cleaner. I do think we will want to rename this in the future, but I think that will be alongside an ..." (https://github.com/vllm-project/vllm/pull/33695#pullrequestreview-4007715389)
- `2026-03-26T19:55:39Z` `inline` by `MatthewBonanni` `vllm/model_executor/layers/attention/attention.py`:262; signals: attention, dtype; excerpt: "Sorry, rather than just vllm config.model config.dtype, it should have been a dtype string as you pointed out. I'm okay with leaving this as ..." (https://github.com/vllm-project/vllm/pull/33695#discussion_r2997350029)
- `2026-03-25T15:53:21Z` `inline` by `MatthewBonanni` `vllm/model_executor/layers/attention/attention.py`:262; signals: attention, dtype; excerpt: "Yeah agreed. Best would be to use model config.dtype" (https://github.com/vllm-project/vllm/pull/33695#discussion_r2989252578)
- `2026-02-03T20:41:22Z` `issue` by `vkuzo`; signals: cache, dtype; excerpt: "how about kvcache dtype skip layers: List[str] = [] for list of layer FQNs to ignore low precision k-v cache from, with direct matching ..." (https://github.com/vllm-project/vllm/pull/33695#issuecomment-3843543699)
- `2026-03-03T14:53:20Z` `inline` by `hmellor` `vllm/engine/arg_utils.py`:1006; signals: cache; excerpt: "Not sure if you plan to update this PR, but if you do the CLI should be added like this: All the information is ..." (https://github.com/vllm-project/vllm/pull/33695#discussion_r2878742426)
- `2026-03-04T09:43:58Z` `inline` by `jmkuebler` `vllm/engine/arg_utils.py`:1006; signals: general review; excerpt: "Thanks, I fixed it! Yes I would still like to merge this PR." (https://github.com/vllm-project/vllm/pull/33695#discussion_r2882799260)
