# PR Discussion Digest

- Source PR: [vllm-project/vllm#32614](https://github.com/vllm-project/vllm/pull/32614)
- Source page: `sources/prs/vllm/PR-32614.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-32614`
- Generated at: `2026-05-20T15:39:30.722125+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-19T20:00:25Z`
- Merged: `2026-01-23T20:38:57Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 9 (approved=4, changes_requested=1, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: LucasWilkinson, MatthewBonanni, Xiaojinhua, esmeetu, gaby, marksverdhei, mdierolf, mgoin, zRzRzRzRzRzRzR
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 10

## Review Decisions

- `2026-01-19T20:01:49Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to enable Multi-head Latent Attention (MLA) for GLM-4 MoE models. The change ... (https://github.com/vllm-project/vllm/pull/32614#pullrequestreview-3679446399)
- `2026-01-19T20:04:19Z` `COMMENTED` by `marksverdhei` (https://github.com/vllm-project/vllm/pull/32614#pullrequestreview-3679453506)
- `2026-01-20T12:50:25Z` `APPROVED` by `MatthewBonanni` - LGTM, thanks for catching this! (https://github.com/vllm-project/vllm/pull/32614#pullrequestreview-3682035856)
- `2026-01-20T15:48:46Z` `APPROVED` by `LucasWilkinson` - LGTM (https://github.com/vllm-project/vllm/pull/32614#pullrequestreview-3682910233)
- `2026-01-20T16:48:33Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/32614#pullrequestreview-3683205947)
- `2026-01-20T18:43:11Z` `CHANGES_REQUESTED` by `mgoin` - Blocking merge while we investigate which MLA backends are/can be supported for this model. For instance forcing TRITON ... (https://github.com/vllm-project/vllm/pull/32614#pullrequestreview-3683758881)
- `2026-01-21T13:40:10Z` `COMMENTED` by `zRzRzRzRzRzRzR` (https://github.com/vllm-project/vllm/pull/32614#pullrequestreview-3685649481)
- `2026-01-21T15:18:03Z` `COMMENTED` by `marksverdhei` (https://github.com/vllm-project/vllm/pull/32614#pullrequestreview-3687797671)
- `2026-01-23T17:57:31Z` `APPROVED` by `mgoin` - Should be good to go now with the Blackwell fixes, thanks for kicking this off @marksverdhei ! (https://github.com/vllm-project/vllm/pull/32614#pullrequestreview-3698845224)

## Inline Comment Hotspots

- `vllm/transformers_utils/model_arch_config_convertor.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-01-20T18:43:11Z` `review` `CHANGES_REQUESTED` by `mgoin`; signals: b200, block, mla, triton; excerpt: "Blocking merge while we investigate which MLA backends are/can be supported for this model. For instance forcing TRITON MLA on B200 results in 0% ..." (https://github.com/vllm-project/vllm/pull/32614#pullrequestreview-3683758881)
- `2026-01-20T17:02:08Z` `issue` by `mgoin`; signals: b200, hang, kernel, nan; excerpt: "@LucasWilkinson @MatthewBonanni When I run with this PR on B200, I get this error. I think we need to change the kernel support registration" (https://github.com/vllm-project/vllm/pull/32614#issuecomment-3773974742)
- `2026-01-22T14:02:53Z` `issue` by `marksverdhei`; signals: b200, block, mla, triton; excerpt: "Blocking merge while we investigate which MLA backends are/can be supported for this model. For instance forcing TRITON MLA on B200 results in 0% ..." (https://github.com/vllm-project/vllm/pull/32614#issuecomment-3784587984)
- `2026-01-19T20:04:19Z` `inline` by `marksverdhei` `vllm/transformers_utils/model_arch_config_convertor.py`:193; signals: attention, mla, moe; excerpt: "Good catch\! You're right - glm4 moe uses standard attention while only glm4 moe lite has MLA support via Glm4MoeLiteMLAAttention. I've updated the PR ..." (https://github.com/vllm-project/vllm/pull/32614#discussion_r2705951931)
- `2026-01-23T17:04:38Z` `issue` by `mdierolf`; signals: b200, blackwell; excerpt: "LGTM! Works well on RTX 6000 Blackwell, model is unusable without this. Nobody is going to run this small model on B200 anyway, merge ..." (https://github.com/vllm-project/vllm/pull/32614#issuecomment-3791291969)
- `2026-01-21T07:02:38Z` `inline` by `zRzRzRzRzRzRzR` `vllm/transformers_utils/model_arch_config_convertor.py`; signals: moe; excerpt: "Should "glm4 moe lite mtp" be added as well?" (https://github.com/vllm-project/vllm/pull/32614#discussion_r2711235283)
- `2026-01-23T17:57:31Z` `review` `APPROVED` by `mgoin`; signals: blackwell; excerpt: "Should be good to go now with the Blackwell fixes, thanks for kicking this off @marksverdhei !" (https://github.com/vllm-project/vllm/pull/32614#pullrequestreview-3698845224)
- `2026-01-21T15:18:03Z` `inline` by `marksverdhei` `vllm/transformers_utils/model_arch_config_convertor.py`; signals: general review; excerpt: "You're right, ty for catching" (https://github.com/vllm-project/vllm/pull/32614#discussion_r2713041150)
