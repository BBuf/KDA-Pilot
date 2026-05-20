# PR Discussion Digest

- Source PR: [vllm-project/vllm#13111](https://github.com/vllm-project/vllm/pull/13111)
- Source page: `sources/prs/vllm/PR-13111.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-13111`
- Generated at: `2026-05-20T15:33:56.880589+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-11T19:42:16Z`
- Merged: `2025-04-17T22:14:07Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 15 (approved=2, commented=13)
- Inline review comments: 13
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=5, outdated=6
- Human participants with discussion text: LucasWilkinson, chaunceyjiang, mergify, nnding, qli88, simon-mo, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-02-27T02:02:33Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2646360607)
- `2025-02-27T02:04:53Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2646362712)
- `2025-02-27T02:05:25Z` `APPROVED` by `tlrmchlsmth` - LGTM (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2646363254)
- `2025-02-28T07:47:54Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2649997793)
- `2025-02-28T07:48:52Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2649999345)
- `2025-02-28T17:41:13Z` `COMMENTED` by `qli88` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2651424352)
- `2025-02-28T17:50:31Z` `COMMENTED` by `qli88` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2651441913)
- `2025-02-28T18:03:46Z` `COMMENTED` by `qli88` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2651469430)
- `2025-02-28T18:04:47Z` `COMMENTED` by `qli88` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2651472600)
- `2025-02-28T18:05:15Z` `COMMENTED` by `qli88` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2651473415)
- `2025-03-04T01:42:27Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2655720206)
- `2025-03-05T03:39:52Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2659785457)
- `2025-03-05T03:40:01Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2659785580)
- `2025-03-05T03:40:12Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2659785741)
- `2025-04-17T22:13:57Z` `APPROVED` by `simon-mo` (https://github.com/vllm-project/vllm/pull/13111#pullrequestreview-2777044644)

## Inline Comment Hotspots

- `vllm/attention/backends/mla/common.py`: 9 inline comment(s)
- `vllm/v1/attention/backends/mla/common.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-02-28T17:41:13Z` `inline` by `qli88` `vllm/attention/backends/mla/common.py`:1088; signals: attention, mla, tma, triton; excerpt: "triton flash always returns (output, softmax lse), so return softmax lse could be True. We just need to unpack the attn out if return ..." (https://github.com/vllm-project/vllm/pull/13111#discussion_r1975800650)
- `2025-02-28T17:50:31Z` `inline` by `qli88` `vllm/attention/backends/mla/common.py`:1108; signals: attention, mla, tma, triton; excerpt: "I think we should adjust attn out based on the value of return softmax lse. If it is True, both triton attn and vllm.flash ..." (https://github.com/vllm-project/vllm/pull/13111#discussion_r1975811305)
- `2025-03-04T01:42:26Z` `inline` by `LucasWilkinson` `vllm/attention/backends/mla/common.py`:1435; signals: attention, mla, tma; excerpt: "sorry this was cruft from an earlier slack discussion that cast doubts on if return softmax lse was supported on RoCM" (https://github.com/vllm-project/vllm/pull/13111#discussion_r1978477599)
- `2025-02-27T02:02:32Z` `inline` by `tlrmchlsmth` `vllm/attention/backends/mla/common.py`:1261; signals: attention, mla, tma; excerpt: "while we're at it, can we handle the lack of the softmax lse arg on RoCM here as well?" (https://github.com/vllm-project/vllm/pull/13111#discussion_r1972690003)
- `2025-02-11T20:57:20Z` `issue` by `LucasWilkinson`; signals: hang, perf, regression; excerpt: "@khluu can we run the perf CI on this? would be nice to check for regressions since theres alot of FA changes" (https://github.com/vllm-project/vllm/pull/13111#issuecomment-2652050738)
- `2025-02-27T02:04:53Z` `inline` by `tlrmchlsmth` `vllm/attention/backends/mla/common.py`:1390; signals: attention, mla; excerpt: "do we need to handle the fact that flash attn varlen diff headdims returns both output and rest in this case?" (https://github.com/vllm-project/vllm/pull/13111#discussion_r1972691355)
- `2025-02-28T07:47:54Z` `inline` by `LucasWilkinson` `vllm/attention/backends/mla/common.py`:1261; signals: attention, mla; excerpt: "done" (https://github.com/vllm-project/vllm/pull/13111#discussion_r1974955388)
- `2025-02-28T07:48:52Z` `inline` by `LucasWilkinson` `vllm/attention/backends/mla/common.py`:1390; signals: attention, mla; excerpt: "we did, but the return was slicing a tensor" (https://github.com/vllm-project/vllm/pull/13111#discussion_r1974956788)
- `2025-02-28T18:03:46Z` `inline` by `qli88` `vllm/attention/backends/mla/common.py`:1435; signals: attention, mla; excerpt: "Why does this not work for ROCm?" (https://github.com/vllm-project/vllm/pull/13111#discussion_r1975827996)
- `2025-02-28T18:04:47Z` `inline` by `qli88` `vllm/v1/attention/backends/mla/common.py`:621; signals: attention, mla; excerpt: "The same as in another common.py" (https://github.com/vllm-project/vllm/pull/13111#discussion_r1975830290)
- `2025-02-28T18:05:15Z` `inline` by `qli88` `vllm/v1/attention/backends/mla/common.py`:652; signals: attention, mla; excerpt: "the same as above." (https://github.com/vllm-project/vllm/pull/13111#discussion_r1975830751)
- `2025-03-05T03:39:52Z` `inline` by `LucasWilkinson` `vllm/attention/backends/mla/common.py`:1088; signals: attention, mla; excerpt: "Fixed" (https://github.com/vllm-project/vllm/pull/13111#discussion_r1980638658)
