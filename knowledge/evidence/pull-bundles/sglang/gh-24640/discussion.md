# PR Discussion Digest

- Source PR: [sgl-project/sglang#24640](https://github.com/sgl-project/sglang/pull/24640)
- Source page: `sources/prs/sglang/PR-24640.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-24640`
- Generated at: `2026-05-20T15:29:43.971950+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-08T01:20:00Z`
- Merged: `2026-05-19T22:23:18Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: Qiaolin-Yu, nagisa-kunhah, zhendonghua
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-08T01:31:29Z` `COMMENTED` by `Qiaolin-Yu` - Could you share the profiling result to prove it's overlapped correctly? Thanks! (https://github.com/sgl-project/sglang/pull/24640#pullrequestreview-4248790661)
- `2026-05-15T23:10:19Z` `COMMENTED` by `zhendonghua` (https://github.com/sgl-project/sglang/pull/24640#pullrequestreview-4301908395)
- `2026-05-15T23:59:54Z` `APPROVED` by `Qiaolin-Yu` - verified by @zhendonghua (https://github.com/sgl-project/sglang/pull/24640#pullrequestreview-4302079557)

## Inline Comment Hotspots

- `test/registered/mla/test_flashmla.py`: 1 inline comment(s)
- `python/sglang/srt/layers/attention/flashmla_backend.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-15T23:10:19Z` `inline` by `zhendonghua` `python/sglang/srt/layers/attention/flashmla_backend.py`:483; signals: attention, flashinfer, mla; excerpt: "@Qiaolin-Yu This line enforces to use the base flashinfer mla attn backend in spec v2 draft extend stage" (https://github.com/sgl-project/sglang/pull/24640#discussion_r3251440587)
- `2026-05-08T05:05:14Z` `issue` by `nagisa-kunhah`; signals: h100, mla, race; excerpt: "Could you share the profiling result to prove it's overlapped correctly? Thanks! @Qiaolin-Yu Sorry, I don't have local access to an H100/FlashMLA-capable GPU right ..." (https://github.com/sgl-project/sglang/pull/24640#issuecomment-4403494024)
- `2026-05-08T01:31:03Z` `inline` by `Qiaolin-Yu` `test/registered/mla/test_flashmla.py`:57; signals: mla, register; excerpt: "we can simply remove this line since we already use v2 by default" (https://github.com/sgl-project/sglang/pull/24640#discussion_r3205675240)
- `2026-05-08T16:22:37Z` `issue` by `nagisa-kunhah`; signals: h100, mla; excerpt: "@Qiaolin-Yu hi，I tried to set up an external H100 environment for profiling, but I couldn't find lmsys/sglang-ci-dsv3-test or lmsys/sglang-ci-dsv3-test-NextN on Hugging Face. Could you ..." (https://github.com/sgl-project/sglang/pull/24640#issuecomment-4407993017)
- `2026-05-08T18:14:44Z` `issue` by `Qiaolin-Yu`; signals: h100, mla; excerpt: "@Qiaolin-Yu hi，I tried to set up an external H100 environment for profiling, but I couldn't find lmsys/sglang-ci-dsv3-test or lmsys/sglang-ci-dsv3-test-NextN on Hugging Face. Could you ..." (https://github.com/sgl-project/sglang/pull/24640#issuecomment-4408815293)
- `2026-05-08T18:43:01Z` `issue` by `nagisa-kunhah`; signals: h100, mla; excerpt: "@Qiaolin-Yu hi，I tried to set up an external H100 environment for profiling, but I couldn't find lmsys/sglang-ci-dsv3-test or lmsys/sglang-ci-dsv3-test-NextN on Hugging Face. Could you ..." (https://github.com/sgl-project/sglang/pull/24640#issuecomment-4408984459)
- `2026-05-08T01:31:29Z` `review` `COMMENTED` by `Qiaolin-Yu`; signals: general review; excerpt: "Could you share the profiling result to prove it's overlapped correctly? Thanks!" (https://github.com/sgl-project/sglang/pull/24640#pullrequestreview-4248790661)
- `2026-05-15T23:58:36Z` `issue` by `Qiaolin-Yu`; signals: mla, register; excerpt: "/rerun-test test/registered/mla/test flashmla.py" (https://github.com/sgl-project/sglang/pull/24640#issuecomment-4464610548)
- `2026-05-14T23:51:35Z` `issue` by `Qiaolin-Yu`; signals: general review; excerpt: "lmsys/sglang-ci-dsv3-test and lmsys/sglang-ci-dsv3-test-NextN theses are private models. seems very hard to provide. Could @zhendonghua help to capture profiling of this?" (https://github.com/sgl-project/sglang/pull/24640#issuecomment-4455656093)
