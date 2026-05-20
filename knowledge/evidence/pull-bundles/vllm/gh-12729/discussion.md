# PR Discussion Digest

- Source PR: [vllm-project/vllm#12729](https://github.com/vllm-project/vllm/pull/12729)
- Source page: `sources/prs/vllm/PR-12729.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-12729`
- Generated at: `2026-05-20T15:33:51.873603+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-04T13:30:28Z`
- Merged: `2025-02-05T04:44:27Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 5
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: Isotr0py, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-02-04T16:46:36Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/12729#pullrequestreview-2593467155)
- `2025-02-05T02:36:10Z` `APPROVED` by `tlrmchlsmth` - Thanks for the fix! I had one comment from earlier today asking if the implementation could be cleaned ... (https://github.com/vllm-project/vllm/pull/12729#pullrequestreview-2594488989)
- `2025-02-05T03:17:43Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/12729#pullrequestreview-2594525135)
- `2025-02-05T03:40:50Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/12729#pullrequestreview-2594546890)
- `2025-02-05T03:43:37Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/12729#pullrequestreview-2594550600)
- `2025-02-05T04:12:31Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/12729#pullrequestreview-2594578372)

## Inline Comment Hotspots

- `vllm/attention/backends/mla/utils.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-02-05T03:17:43Z` `inline` by `Isotr0py` `vllm/attention/backends/mla/utils.py`:442; signals: attention, cuda, flash attention, memory, mla; excerpt: "I wrapped the rotary embedding to reshape with pure rope because if q pe and k pe have shape of [seq len, num heads, ..." (https://github.com/vllm-project/vllm/pull/12729#discussion_r1942191221)
- `2025-02-05T03:40:49Z` `inline` by `Isotr0py` `vllm/attention/backends/mla/utils.py`:442; signals: attention, block, cuda, kernel, mla; excerpt: "Oh, seems that it's because the calculation for num heads in rotary embedding cuda ops is unsuitable for tensor with shape [seq len, num ..." (https://github.com/vllm-project/vllm/pull/12729#discussion_r1942203266)
- `2025-02-05T03:43:37Z` `inline` by `tlrmchlsmth` `vllm/attention/backends/mla/utils.py`:442; signals: attention, cuda, kernel, mla; excerpt: "Sounds like a bug in the kernel -- I'll look into it tomorrow. In the meantime I like adding a shape check in forward ..." (https://github.com/vllm-project/vllm/pull/12729#discussion_r1942205093)
- `2025-02-05T04:12:31Z` `inline` by `tlrmchlsmth` `vllm/attention/backends/mla/utils.py`:442; signals: attention, block, kernel, mla; excerpt: "Let's fix it in a separate PR to avoid blocking v0.7.2 release, especially it's on the kernel side and I need some time to ..." (https://github.com/vllm-project/vllm/pull/12729#discussion_r1942220389)
- `2025-02-04T16:46:36Z` `inline` by `tlrmchlsmth` `vllm/attention/backends/mla/utils.py`:442; signals: attention, mla; excerpt: "Could you say a bit about why you needed to wrap rotary embedding when using pure rope? Wondering if we could clean things up ..." (https://github.com/vllm-project/vllm/pull/12729#discussion_r1941538656)
- `2025-02-04T15:08:55Z` `issue` by `Isotr0py`; signals: mla; excerpt: "deepseek-vl2-small with deepseek-v2 backbone should work with MLA backend now:" (https://github.com/vllm-project/vllm/pull/12729#issuecomment-2634262268)
- `2025-02-05T02:36:10Z` `review` `APPROVED` by `tlrmchlsmth`; signals: general review; excerpt: "Thanks for the fix! I had one comment from earlier today asking if the implementation could be cleaned up a bit - I still ..." (https://github.com/vllm-project/vllm/pull/12729#pullrequestreview-2594488989)
