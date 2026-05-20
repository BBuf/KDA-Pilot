# PR Discussion Digest

- Source PR: [vllm-project/vllm#15961](https://github.com/vllm-project/vllm/pull/15961)
- Source page: `sources/prs/vllm/PR-15961.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-15961`
- Generated at: `2026-05-20T15:34:46.129616+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-02T18:50:49Z`
- Merged: `2025-04-09T01:53:31Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: mgoin, pavanimajety, yueshen2016
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-03T10:06:17Z` `COMMENTED` by `mgoin` - This seems to add support for kv cache quantization to mixtral. However there is no MoE layer registered ... (https://github.com/vllm-project/vllm/pull/15961#pullrequestreview-2739242328)
- `2025-04-03T18:55:02Z` `APPROVED` by `pavanimajety` - LGTM. @mgoin This is a python change, don't see why the docker is failing. Can we restart the ... (https://github.com/vllm-project/vllm/pull/15961#pullrequestreview-2740862492)
- `2025-04-08T22:30:40Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/15961#pullrequestreview-2751544997)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-04-03T10:06:17Z` `review` `COMMENTED` by `mgoin`; signals: cache, kv cache, moe, register; excerpt: "This seems to add support for kv cache quantization to mixtral. However there is no MoE layer registered for modelopt to use, so what ..." (https://github.com/vllm-project/vllm/pull/15961#pullrequestreview-2739242328)
- `2025-04-03T18:18:29Z` `issue` by `yueshen2016`; signals: cache, kv cache, moe, register; excerpt: "This seems to add support for kv cache quantization to mixtral. However there is no MoE layer registered for modelopt to use, so what ..." (https://github.com/vllm-project/vllm/pull/15961#issuecomment-2776587462)
- `2025-04-03T18:55:02Z` `review` `APPROVED` by `pavanimajety`; signals: failing, hang; excerpt: "LGTM. @mgoin This is a python change, don't see why the docker is failing. Can we restart the CI?" (https://github.com/vllm-project/vllm/pull/15961#pullrequestreview-2740862492)
- `2025-04-03T18:39:54Z` `issue` by `pavanimajety`; signals: moe; excerpt: "@mgoin This is mixtral quant.py which doesn't use FusedMoE layer. It is simply an MLP layer: [here ]( And the switch between architectures happens ..." (https://github.com/vllm-project/vllm/pull/15961#issuecomment-2776630798)
- `2025-04-08T22:30:09Z` `issue` by `mgoin`; signals: hang; excerpt: "I think this PR was made before we made changes to the docker image. Can you please merge with main?" (https://github.com/vllm-project/vllm/pull/15961#issuecomment-2787795493)
