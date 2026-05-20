# PR Discussion Digest

- Source PR: [vllm-project/vllm#28718](https://github.com/vllm-project/vllm/pull/28718)
- Source page: `sources/prs/vllm/PR-28718.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28718`
- Generated at: `2026-05-20T15:38:32.013253+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-14T09:02:56Z`
- Merged: `2025-11-19T20:52:44Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 17 (approved=1, commented=16)
- Inline review comments: 20
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=8, outdated=5
- Human participants with discussion text: FENP, LucasWilkinson, chatgpt-codex-connector, heroes999, luccafong, mergify, pisceskkk
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-11-14T09:07:09Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces basic support for Prefill Context Parallelism (PCP), aligning with the RFC. The ... (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3463795948)
- `2025-11-14T18:09:43Z` `COMMENTED` by `luccafong` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3466140674)
- `2025-11-15T03:39:40Z` `COMMENTED` by `pisceskkk` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3467587877)
- `2025-11-17T06:02:46Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3471093462)
- `2025-11-17T06:50:07Z` `COMMENTED` by `pisceskkk` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3471239057)
- `2025-11-17T06:50:09Z` `COMMENTED` by `pisceskkk` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3471239130)
- `2025-11-17T07:06:22Z` `COMMENTED` by `pisceskkk` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3471276650)
- `2025-11-17T07:29:09Z` `COMMENTED` by `FENP` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3471340659)
- `2025-11-18T05:44:30Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3475570757)
- `2025-11-18T05:49:23Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3475585936)
- `2025-11-18T06:42:44Z` `COMMENTED` by `FENP` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3475759712)
- `2025-11-18T06:48:49Z` `COMMENTED` by `pisceskkk` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3475776265)
- `2025-11-19T04:50:09Z` `COMMENTED` by `LucasWilkinson` - Overall looks pretty good to me; running the CI, left a couple of final nits/comments (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3480811615)
- `2025-11-19T05:41:03Z` `COMMENTED` by `pisceskkk` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3480903494)
- `2025-11-19T05:42:45Z` `COMMENTED` by `pisceskkk` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3480906664)
- `2025-11-19T05:43:24Z` `COMMENTED` by `pisceskkk` (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3480907786)
- `2025-11-19T20:52:37Z` `APPROVED` by `LucasWilkinson` - LGTM (https://github.com/vllm-project/vllm/pull/28718#pullrequestreview-3484704414)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 6 inline comment(s)
- `vllm/v1/core/kv_cache_utils.py`: 4 inline comment(s)
- `vllm/v1/attention/backends/utils.py`: 4 inline comment(s)
- `vllm/engine/arg_utils.py`: 2 inline comment(s)
- `vllm/v1/core/kv_cache_manager.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/config.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-17T06:50:09Z` `inline` by `pisceskkk` `vllm/v1/attention/backends/utils.py`:1083; signals: attention, cache, hang; excerpt: "no, we will split KVCache among PCP devices too, so this local seq len func will be used as following: but, maybe we could ..." (https://github.com/vllm-project/vllm/pull/28718#discussion_r2532905308)
- `2025-11-17T07:29:09Z` `inline` by `FENP` `vllm/model_executor/layers/fused_moe/layer.py`:1779; signals: cute, hang, moe; excerpt: "can you explain why this all gather is needed? Why can't we just dispatch tokens directly from there existing PCP ranks? Yes, indeed, the ..." (https://github.com/vllm-project/vllm/pull/28718#discussion_r2532989642)
- `2025-11-18T06:48:48Z` `inline` by `pisceskkk` `vllm/v1/attention/backends/utils.py`:1083; signals: attention, hang; excerpt: "lets not rename the variables in this function yet since it will cause confusion with the function name get dcp local seq lens; we ..." (https://github.com/vllm-project/vllm/pull/28718#discussion_r2536536795)
- `2025-11-17T05:56:48Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/fused_moe/layer.py`:1849; signals: hang, moe; excerpt: "what is this change for?" (https://github.com/vllm-project/vllm/pull/28718#discussion_r2532794511)
- `2025-11-17T06:50:07Z` `inline` by `pisceskkk` `vllm/v1/core/kv_cache_utils.py`:1231; signals: cache, hang; excerpt: "sure, we will change this" (https://github.com/vllm-project/vllm/pull/28718#discussion_r2532905252)
- `2025-11-19T05:42:45Z` `inline` by `pisceskkk` `vllm/v1/core/kv_cache_utils.py`:1231; signals: cache, hang; excerpt: "sure, changed this" (https://github.com/vllm-project/vllm/pull/28718#discussion_r2540617472)
- `2025-11-15T03:39:26Z` `issue` by `pisceskkk`; signals: cache, mla; excerpt: "can you share a few combinations of PCP x DCP x TP in your summary? We usually set PCP=2, and TP=num devices/PCP. For the ..." (https://github.com/vllm-project/vllm/pull/28718#issuecomment-3535516211)
- `2025-11-14T18:09:43Z` `inline` by `luccafong` `vllm/engine/arg_utils.py`:772; signals: cache; excerpt: "we may need to add both --dcp-kv-cache-interleave-size and --cp-kv-cache-interleave-size to align the interface and deprecate --dcp-xx later" (https://github.com/vllm-project/vllm/pull/28718#discussion_r2528459629)
- `2025-11-17T06:02:40Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/fused_moe/layer.py`:1779; signals: moe; excerpt: "can you explain why this all gather is needed? Why can't we just dispatch tokens directly from there existing PCP ranks?" (https://github.com/vllm-project/vllm/pull/28718#discussion_r2532812515)
- `2025-11-17T07:06:21Z` `inline` by `pisceskkk` `vllm/model_executor/layers/fused_moe/layer.py`:1849; signals: moe; excerpt: "Apologies, this code was mistakenly included due to my error. It existed in a previous PR but was optimized out in a later commit. ..." (https://github.com/vllm-project/vllm/pull/28718#discussion_r2532937680)
- `2025-11-18T05:44:30Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/fused_moe/layer.py`:1779; signals: moe; excerpt: "got it, thanks!; yes this is fine for now; what test setup are you using (like vllm serve ... I'd love to poke around ..." (https://github.com/vllm-project/vllm/pull/28718#discussion_r2536389507)
- `2025-11-18T05:49:23Z` `inline` by `LucasWilkinson` `vllm/v1/attention/backends/utils.py`:1083; signals: attention; excerpt: "lets not rename the variables in this function yet since it will cause confusion with the function name get dcp local seq lens; we ..." (https://github.com/vllm-project/vllm/pull/28718#discussion_r2536399585)
