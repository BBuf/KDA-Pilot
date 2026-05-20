# PR Discussion Digest

- Source PR: [sgl-project/sglang#19086](https://github.com/sgl-project/sglang/pull/19086)
- Source page: `sources/prs/sglang/PR-19086.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19086`
- Generated at: `2026-05-20T15:28:45.371112+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-20T22:21:26Z`
- Merged: `2026-02-25T08:26:45Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 7
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: ShangmingCai, YAMY1234
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-20T22:28:31Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a critical correctness issue in KV cache slice transfers for GQA models ... (https://github.com/sgl-project/sglang/pull/19086#pullrequestreview-3834477114)
- `2026-02-22T04:15:03Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/19086#pullrequestreview-3836667870)
- `2026-02-22T04:18:04Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/19086#pullrequestreview-3836670783)
- `2026-02-22T04:22:18Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/19086#pullrequestreview-3836674453)
- `2026-02-22T04:23:00Z` `COMMENTED` by `ShangmingCai` - Others LGTM (https://github.com/sgl-project/sglang/pull/19086#pullrequestreview-3836675308)
- `2026-02-22T04:28:35Z` `COMMENTED` by `YAMY1234` (https://github.com/sgl-project/sglang/pull/19086#pullrequestreview-3836678135)
- `2026-02-22T04:45:23Z` `COMMENTED` by `YAMY1234` (https://github.com/sgl-project/sglang/pull/19086#pullrequestreview-3836701649)
- `2026-02-22T06:03:14Z` `APPROVED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/19086#pullrequestreview-3836817753)

## Inline Comment Hotspots

- `python/sglang/srt/disaggregation/mooncake/conn.py`: 7 inline comment(s)

## High-Signal Discussion

- `2026-02-21T06:56:36Z` `issue` by `YAMY1234`; signals: accuracy, attention, cache, kv cache; excerpt: "why the accuracy before this fix is low? I think the original logic should work with dp attention for such setups Do you mean ..." (https://github.com/sgl-project/sglang/pull/19086#issuecomment-3938315337)
- `2026-02-21T07:46:04Z` `issue` by `ShangmingCai`; signals: accuracy, attention, cache, kv cache; excerpt: "why the accuracy before this fix is low? I think the original logic should work with dp attention for such setups Do you mean ..." (https://github.com/sgl-project/sglang/pull/19086#issuecomment-3938396157)
- `2026-02-21T18:27:52Z` `issue` by `YAMY1234`; signals: accuracy, attention, cache, kv cache; excerpt: "why the accuracy before this fix is low? I think the original logic should work with dp attention for such setups Do you mean ..." (https://github.com/sgl-project/sglang/pull/19086#issuecomment-3939210283)
- `2026-02-21T06:33:31Z` `issue` by `ShangmingCai`; signals: accuracy, attention; excerpt: "why the accuracy before this fix is low? I think the original logic should work with dp attention for such setups" (https://github.com/sgl-project/sglang/pull/19086#issuecomment-3938282665)
- `2026-02-22T05:25:34Z` `issue` by `ShangmingCai`; signals: attention, correctness; excerpt: "One last question: if we don't enable dp attention, what is the benefit of duplicating the KV heads? I am still confused about the ..." (https://github.com/sgl-project/sglang/pull/19086#issuecomment-3940208459)
- `2026-02-22T05:56:06Z` `issue` by `YAMY1234`; signals: attention, correctness; excerpt: "One last question: if we don't enable dp attention, what is the benefit of duplicating the KV heads? I am still confused about the ..." (https://github.com/sgl-project/sglang/pull/19086#issuecomment-3940243995)
- `2026-02-22T04:45:23Z` `inline` by `YAMY1234` `python/sglang/srt/disaggregation/mooncake/conn.py`:446; signals: hang; excerpt: "@ShangmingCai I removed it. After thinking twice, the modulo could silently mask offset bugs by wrapping to a wrong-but-valid position. This can led to ..." (https://github.com/sgl-project/sglang/pull/19086#discussion_r2837118087)
- `2026-02-22T04:23:00Z` `review` `COMMENTED` by `ShangmingCai`; signals: general review; excerpt: "Others LGTM" (https://github.com/sgl-project/sglang/pull/19086#pullrequestreview-3836675308)
- `2026-02-22T04:10:39Z` `issue` by `ShangmingCai`; signals: hang; excerpt: "@YAMY1234 Thanks for the clarification. I understand the change now." (https://github.com/sgl-project/sglang/pull/19086#issuecomment-3940101869)
- `2026-02-22T04:15:03Z` `inline` by `ShangmingCai` `python/sglang/srt/disaggregation/mooncake/conn.py`:430; signals: general review; excerpt: "Is it possible that we don't pass total kv head num in, just use self.kv args.kv head num self.attn tp size for all cases?" (https://github.com/sgl-project/sglang/pull/19086#discussion_r2837095902)
- `2026-02-22T04:18:04Z` `inline` by `ShangmingCai` `python/sglang/srt/disaggregation/mooncake/conn.py`:430; signals: general review; excerpt: "OK, I think the problem is that self.kv args.kv head num self.attn tp size won't represent the correct total heads under this case since ..." (https://github.com/sgl-project/sglang/pull/19086#discussion_r2837097976)
- `2026-02-22T04:28:35Z` `inline` by `YAMY1234` `python/sglang/srt/disaggregation/mooncake/conn.py`:446; signals: general review; excerpt: "Yes, this was a suggestion from Gemini code review BTW😂(the third commit). You're right that mathematically it can't exceed dst heads per rank. It ..." (https://github.com/sgl-project/sglang/pull/19086#discussion_r2837105049)
