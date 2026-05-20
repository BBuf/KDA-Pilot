# PR Discussion Digest

- Source PR: [vllm-project/vllm#35075](https://github.com/vllm-project/vllm/pull/35075)
- Source page: `sources/prs/vllm/PR-35075.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-35075`
- Generated at: `2026-05-20T15:39:58.116585+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-23T04:10:54Z`
- Merged: `2026-02-24T22:55:22Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 5 (approved=4, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: LopezCastroRoberto, LucasWilkinson, MatthewBonanni, benchislett, mgoin, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-23T04:12:15Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request correctly addresses a crash in DeepSeek V3.2 when VLLM USE DEEP GEMM=0 is ... (https://github.com/vllm-project/vllm/pull/35075#pullrequestreview-3839071712)
- `2026-02-23T10:01:07Z` `APPROVED` by `LopezCastroRoberto` - LGTM, thanks for the fix! (https://github.com/vllm-project/vllm/pull/35075#pullrequestreview-3840102345)
- `2026-02-23T15:43:24Z` `APPROVED` by `LucasWilkinson` - LGTM, thanks for the fix! (https://github.com/vllm-project/vllm/pull/35075#pullrequestreview-3841853161)
- `2026-02-23T16:03:43Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/35075#pullrequestreview-3841983800)
- `2026-02-24T22:55:03Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/35075#pullrequestreview-3850947885)

## Inline Comment Hotspots

- `vllm/utils/deep_gemm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-23T15:44:51Z` `issue` by `LucasWilkinson`; signals: deepgemm, gemm, moe; excerpt: "If DeepGEMM is truly required, shouldn't we just have a better assertion during startup rather than ignoring the environment variable setting? I think the ..." (https://github.com/vllm-project/vllm/pull/35075#issuecomment-3945567737)
- `2026-02-23T15:49:10Z` `issue` by `mgoin`; signals: attention, gemm, kernel; excerpt: "Could we just not use this utility for the attention kernel and just check for has deep gemm()? We already do this as an ..." (https://github.com/vllm-project/vllm/pull/35075#issuecomment-3945607729)
- `2026-02-23T15:43:03Z` `inline` by `LucasWilkinson` `vllm/utils/deep_gemm.py`:75; signals: gemm, hopper; excerpt: "nit: it think its the only choice on hopper too" (https://github.com/vllm-project/vllm/pull/35075#discussion_r2841570484)
- `2026-02-23T14:36:31Z` `issue` by `MatthewBonanni`; signals: deepgemm, gemm; excerpt: "If DeepGEMM is truly required, shouldn't we just have a better assertion during startup rather than ignoring the environment variable setting?" (https://github.com/vllm-project/vllm/pull/35075#issuecomment-3945134783)
- `2026-02-23T16:39:43Z` `issue` by `benchislett`; signals: attention; excerpt: "Ah, I missed that check in the attention init. That should be sufficient, I'll use that instead" (https://github.com/vllm-project/vllm/pull/35075#issuecomment-3945905276)
