# PR Discussion Digest

- Source PR: [vllm-project/vllm#35047](https://github.com/vllm-project/vllm/pull/35047)
- Source page: `sources/prs/vllm/PR-35047.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-35047`
- Generated at: `2026-05-20T15:39:56.648302+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-22T05:32:01Z`
- Merged: `2026-02-26T21:56:24Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 15 (approved=2, commented=13)
- Inline review comments: 18
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=2, outdated=4
- Human participants with discussion text: Edwardf0t1, mgoin, pavanimajety, sychen52
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-02-22T05:41:23Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request introduces support for 'modelopt mixed' precision in vLLM, allowing different quantization algorithms for ... (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3836781760)
- `2026-02-23T23:32:48Z` `COMMENTED` by `pavanimajety` - @sychen52 If we are going to see more mixed precision formats like INT4 + FP8, the config "modelopt ... (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3844059307)
- `2026-02-24T05:11:24Z` `COMMENTED` by `Edwardf0t1` (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3845000018)
- `2026-02-24T17:34:19Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3844204166)
- `2026-02-24T19:54:56Z` `COMMENTED` by `sychen52` (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3850210219)
- `2026-02-24T19:55:06Z` `COMMENTED` by `sychen52` (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3850211016)
- `2026-02-24T19:56:50Z` `COMMENTED` by `sychen52` (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3850218265)
- `2026-02-24T22:52:20Z` `COMMENTED` by `sychen52` (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3850939962)
- `2026-02-25T01:31:58Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3851331863)
- `2026-02-25T05:48:17Z` `COMMENTED` by `sychen52` (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3852037774)
- `2026-02-25T05:50:17Z` `COMMENTED` by `sychen52` (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3852042863)
- `2026-02-25T06:30:04Z` `COMMENTED` by `sychen52` (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3852190471)
- `2026-02-25T07:42:05Z` `APPROVED` by `Edwardf0t1` - LGTM. Could we run tests on a ModelOpt FP8 and a NVFP4 checkpoints since I think they’re not ... (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3852454964)
- `2026-02-25T20:59:10Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3856933297)
- `2026-02-26T17:45:07Z` `APPROVED` by `pavanimajety` - LGTM, please add a test to exercise this path when the model is out. (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3862602631)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/modelopt.py`: 13 inline comment(s)
- `vllm/model_executor/model_loader/weight_utils.py`: 5 inline comment(s)

## High-Signal Discussion

- `2026-02-23T23:32:48Z` `review` `COMMENTED` by `pavanimajety`; signals: fp4, fp8, nvfp4; excerpt: "@sychen52 If we are going to see more mixed precision formats like INT4 + FP8, the config "modelopt mixed" would be confusing looking at ..." (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3844059307)
- `2026-02-25T07:42:05Z` `review` `APPROVED` by `Edwardf0t1`; signals: fp4, fp8, nvfp4; excerpt: "LGTM. Could we run tests on a ModelOpt FP8 and a NVFP4 checkpoints since I think they’re not already covered by CI as [this ..." (https://github.com/vllm-project/vllm/pull/35047#pullrequestreview-3852454964)
- `2026-02-24T19:56:50Z` `inline` by `sychen52` `vllm/model_executor/layers/quantization/modelopt.py`:1884; signals: fp4, nvfp4; excerpt: "If the checkpoint always has NVFP4 layers, it will not be hit. If the checkpoint does not have any NVFP4 Layers, it will be ..." (https://github.com/vllm-project/vllm/pull/35047#discussion_r2849257577)
- `2026-02-25T06:30:04Z` `inline` by `sychen52` `vllm/model_executor/layers/quantization/modelopt.py`:1962; signals: attention, moe; excerpt: "I just checked. It is okay to return None for MOE and attention. However, it is not okay to return None for dense linear. ..." (https://github.com/vllm-project/vllm/pull/35047#discussion_r2851136336)
- `2026-02-25T01:21:56Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/modelopt.py`:306; signals: cache, kv cache; excerpt: "Should you still check for "kv cache quant algo" to older checkpoints?" (https://github.com/vllm-project/vllm/pull/35047#discussion_r2850322014)
- `2026-02-26T01:17:37Z` `issue` by `mgoin`; signals: b200, h100; excerpt: "@Edwardf0t1 I wasn't aware of that PR, but also it is unnecessary as we already have robust gsm8k testing through the tests/evals/gsm8k/ directory. We ..." (https://github.com/vllm-project/vllm/pull/35047#issuecomment-3963279151)
- `2026-02-25T01:30:37Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/modelopt.py`:1962; signals: moe; excerpt: "If you are just going to return None for the non-linear case, where you could return UnquantizedFusedMoEMethod/etc, you could just return None for all ..." (https://github.com/vllm-project/vllm/pull/35047#discussion_r2850341853)
- `2026-02-23T23:19:53Z` `inline` by `pavanimajety` `vllm/model_executor/model_loader/weight_utils.py`:280; signals: general review; excerpt: "Is this the plan for future too? I was of the opinion that Modelopt would switch out of using hf quant config.json?" (https://github.com/vllm-project/vllm/pull/35047#discussion_r2843575566)
- `2026-02-24T04:35:00Z` `inline` by `Edwardf0t1` `vllm/model_executor/model_loader/weight_utils.py`:280; signals: general review; excerpt: "@sychen52 Could we ensure that the per-layer quantization config is included in config.json as well? vLLM will look at config.json for quantization configs first, ..." (https://github.com/vllm-project/vllm/pull/35047#discussion_r2844450158)
- `2026-02-24T05:05:05Z` `inline` by `Edwardf0t1` `vllm/model_executor/layers/quantization/modelopt.py`:1845; signals: general review; excerpt: "In this function we can extract the shared logic among all Config class into a helper on the base class." (https://github.com/vllm-project/vllm/pull/35047#discussion_r2844525281)
- `2026-02-25T01:31:56Z` `inline` by `mgoin` `vllm/model_executor/model_loader/weight_utils.py`:379; signals: general review; excerpt: "It is a shame you have to introduce a new quantization string just to represent mixed checkpoints, since this should be information you can ..." (https://github.com/vllm-project/vllm/pull/35047#discussion_r2850344777)
- `2026-02-25T05:50:17Z` `inline` by `sychen52` `vllm/model_executor/layers/quantization/modelopt.py`:306; signals: general review; excerpt: "I think it makes sense to assume that there is no old mixed precision checkpoint. For this reason, I remove the legacy vision support ..." (https://github.com/vllm-project/vllm/pull/35047#discussion_r2851000970)
