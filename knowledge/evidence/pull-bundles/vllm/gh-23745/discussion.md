# PR Discussion Digest

- Source PR: [vllm-project/vllm#23745](https://github.com/vllm-project/vllm/pull/23745)
- Source page: `sources/prs/vllm/PR-23745.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23745`
- Generated at: `2026-05-20T15:37:40.573017+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-27T13:08:12Z`
- Merged: `2025-09-16T10:55:17Z`

## Discussion Counts

- Issue comments: 22
- Review submissions: 16 (approved=2, commented=14)
- Inline review comments: 18
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=9
- Human participants with discussion text: DarkLight1337, Weigaa, abmfy, cboss6, hmellor, luccafong, mergify, roywei
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-08-27T13:10:12Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a novel "Zigzag" static expert placement strategy for MoE models, which is ... (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3159726276)
- `2025-09-02T09:06:58Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3175589151)
- `2025-09-02T09:30:17Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3175619317)
- `2025-09-02T13:10:20Z` `COMMENTED` by `cboss6` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3176499597)
- `2025-09-02T13:10:52Z` `COMMENTED` by `cboss6` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3176501597)
- `2025-09-02T13:14:02Z` `COMMENTED` by `cboss6` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3176515889)
- `2025-09-02T13:14:31Z` `COMMENTED` by `cboss6` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3176519420)
- `2025-09-03T21:00:32Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3182475516)
- `2025-09-03T21:01:43Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3182480208)
- `2025-09-04T06:45:31Z` `COMMENTED` by `cboss6` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3183692941)
- `2025-09-04T06:47:34Z` `COMMENTED` by `cboss6` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3183699081)
- `2025-09-12T20:40:26Z` `APPROVED` by `abmfy` - LGTM. Thanks for the contribution! (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3218755998)
- `2025-09-15T13:50:18Z` `APPROVED` by `hmellor` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3224739447)
- `2025-09-15T16:38:24Z` `COMMENTED` by `luccafong` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3225482841)
- `2025-09-15T16:53:10Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3225529561)
- `2025-09-16T08:35:35Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/23745#pullrequestreview-3228393196)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 10 inline comment(s)
- `tests/distributed/test_zigzag_expert_placement.py`: 6 inline comment(s)
- `vllm/config/parallel.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-05T18:20:48Z` `issue` by `abmfy`; signals: accuracy, alignment, benchmark, hang, kernel, memory; excerpt: "Thanks for your quick response and the contribution! Just curious why the accuracy is good since this PR doesn't seem to be modifying the ..." (https://github.com/vllm-project/vllm/pull/23745#issuecomment-3259344068)
- `2025-09-09T07:52:21Z` `issue` by `cboss6`; signals: accuracy, alignment, benchmark, hang, kernel, memory; excerpt: "Thanks for your quick response and the contribution! Just curious why the accuracy is good since this PR doesn't seem to be modifying the ..." (https://github.com/vllm-project/vllm/pull/23745#issuecomment-3269378055)
- `2025-09-05T12:24:33Z` `issue` by `cboss6`; signals: accuracy, alignment, benchmark, hang, memory; excerpt: "Just curious why the accuracy is good since this PR doesn't seem to be modifying the weight loader; the weights are loaded onto GPUs ..." (https://github.com/vllm-project/vllm/pull/23745#issuecomment-3258170075)
- `2025-09-05T00:55:42Z` `issue` by `abmfy`; signals: accuracy, alignment, benchmark; excerpt: "Just curious why the accuracy is good since this PR doesn't seem to be modifying the weight loader; the weights are loaded onto GPUs ..." (https://github.com/vllm-project/vllm/pull/23745#issuecomment-3256634114)
- `2025-09-02T09:27:47Z` `inline` by `hmellor` `vllm/model_executor/layers/fused_moe/layer.py`:666; signals: moe; excerpt: "Given that this is not a well known technique, I'm hesitant to name it zigzag as it seema a little abstract. Could we instead ..." (https://github.com/vllm-project/vllm/pull/23745#discussion_r2315493794)
- `2025-09-02T13:14:02Z` `inline` by `cboss6` `vllm/model_executor/layers/fused_moe/layer.py`:842; signals: moe; excerpt: "Since this pattern doesn’t benefit from the configuration num expoert group=1 theoretically, I suggest falling back to the default behavior to minimize its impact." (https://github.com/vllm-project/vllm/pull/23745#discussion_r2316058567)
- `2025-09-03T21:00:32Z` `inline` by `hmellor` `vllm/model_executor/layers/fused_moe/layer.py`:842; signals: moe; excerpt: "Yes so we should add ep size 1 to the condition so that we fall back to the default behaviour when there is no ..." (https://github.com/vllm-project/vllm/pull/23745#discussion_r2320201114)
- `2025-09-02T09:15:53Z` `inline` by `hmellor` `tests/distributed/test_zigzag_expert_placement.py`:56; signals: cute; excerpt: "If still needed, could these be imported from .test eplb execute.py instead?" (https://github.com/vllm-project/vllm/pull/23745#discussion_r2315450749)
- `2025-09-02T09:18:04Z` `inline` by `hmellor` `vllm/model_executor/layers/fused_moe/layer.py`:842; signals: moe; excerpt: "Is it also worth conditioning this on ep size 1?" (https://github.com/vllm-project/vllm/pull/23745#discussion_r2315457854)
- `2025-09-02T13:14:31Z` `inline` by `cboss6` `vllm/model_executor/layers/fused_moe/layer.py`:666; signals: moe; excerpt: "Done." (https://github.com/vllm-project/vllm/pull/23745#discussion_r2316060443)
- `2025-09-04T06:45:31Z` `inline` by `cboss6` `vllm/model_executor/layers/fused_moe/layer.py`:842; signals: moe; excerpt: "Done." (https://github.com/vllm-project/vllm/pull/23745#discussion_r2321015514)
- `2025-09-16T08:35:35Z` `inline` by `hmellor` `vllm/model_executor/layers/fused_moe/layer.py`:733; signals: moe; excerpt: "Check linear first" (https://github.com/vllm-project/vllm/pull/23745#discussion_r2351472339)
