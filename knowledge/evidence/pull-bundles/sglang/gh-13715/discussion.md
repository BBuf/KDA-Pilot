# PR Discussion Digest

- Source PR: [sgl-project/sglang#13715](https://github.com/sgl-project/sglang/pull/13715)
- Source page: `sources/prs/sglang/PR-13715.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13715`
- Generated at: `2026-05-20T15:27:49.573117+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-21T08:24:37Z`
- Merged: `2026-01-10T05:38:19Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: Fridge003, kaixih, shifangx, wenscarl
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-21T08:34:57Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses an issue related to --enable-eplb and fp4 by correctly filtering parameters in ... (https://github.com/sgl-project/sglang/pull/13715#pullrequestreview-3491699892)
- `2025-11-21T08:57:55Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13715#pullrequestreview-3491770481)
- `2026-01-10T05:27:27Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13715#pullrequestreview-3646452724)

## Inline Comment Hotspots

- `python/sglang/srt/models/bailing_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-23T07:58:16Z` `issue` by `Fridge003`; signals: fp4, moe, nvfp4; excerpt: "Setting SGLANG MOE NVFP4 DISPATCH=1 for prefill node should solve this. There has been some refactors on MoE recently." (https://github.com/sgl-project/sglang/pull/13715#issuecomment-3567596175)
- `2025-11-21T08:57:52Z` `inline` by `Fridge003` `python/sglang/srt/models/bailing_moe.py`:316; signals: moe; excerpt: "Can we wrap them into a util function and reuse?" (https://github.com/sgl-project/sglang/pull/13715#discussion_r2549008071)
- `2025-11-24T03:25:06Z` `issue` by `shifangx`; signals: fp4; excerpt: "Perhaps it would be better for a colleague who is familiar with the fp4 weight format to handle this issue. So I just close ..." (https://github.com/sgl-project/sglang/pull/13715#issuecomment-3568796395)
- `2025-11-21T18:50:45Z` `issue` by `kaixih`; signals: general review; excerpt: "Original w13 weight scale shape: [num local experts, M, K] After swizzling shape: [M padded, K padded] - missing expert dimension EPLB cannot handle ..." (https://github.com/sgl-project/sglang/pull/13715#issuecomment-3564231537)
- `2025-11-24T03:26:48Z` `issue` by `shifangx`; signals: general review; excerpt: "Original w13 weight scale shape: [num local experts, M, K] After swizzling shape: [M padded, K padded] - missing expert dimension EPLB cannot handle ..." (https://github.com/sgl-project/sglang/pull/13715#issuecomment-3568798605)
- `2025-12-09T23:45:17Z` `issue` by `wenscarl`; signals: general review; excerpt: "Just tried this fix in 0.5.5.post.2 container with script [here]( except I have to manually start router and client. I didn't obverse any issue ..." (https://github.com/sgl-project/sglang/pull/13715#issuecomment-3634750034)
