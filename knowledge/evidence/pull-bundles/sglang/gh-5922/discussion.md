# PR Discussion Digest

- Source PR: [sgl-project/sglang#5922](https://github.com/sgl-project/sglang/pull/5922)
- Source page: `sources/prs/sglang/PR-5922.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-5922`
- Generated at: `2026-05-20T15:30:33.657668+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-30T16:20:32Z`
- Merged: `2025-05-12T20:55:42Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: ByronHsu, Hongbosherlock, ShangmingCai, ZhengWG, jokerwyt, whybeyoung
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-04-30T16:54:32Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/5922#pullrequestreview-2807786284)
- `2025-04-30T17:43:42Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/5922#pullrequestreview-2807949097)
- `2025-05-01T09:46:01Z` `COMMENTED` by `ZhengWG` (https://github.com/sgl-project/sglang/pull/5922#pullrequestreview-2809538133)
- `2025-05-01T12:36:38Z` `COMMENTED` by `ZhengWG` (https://github.com/sgl-project/sglang/pull/5922#pullrequestreview-2809708436)
- `2025-05-11T04:09:35Z` `APPROVED` by `ByronHsu` - LGTM! can you add a unit test? (https://github.com/sgl-project/sglang/pull/5922#pullrequestreview-2831221357)

## Inline Comment Hotspots

- `python/sglang/srt/disaggregation/mooncake/conn.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-05-07T07:48:19Z` `issue` by `Hongbosherlock`; signals: cache, hang, kv cache, mla; excerpt: "when decode tp size per dp rank prefill tp size per dp rank, the result repeats one word. ![image]( command: @ShangmingCai For non-MLA models, ..." (https://github.com/sgl-project/sglang/pull/5922#issuecomment-2857468761)
- `2025-05-01T13:00:06Z` `issue` by `ZhengWG`; signals: hang, mla; excerpt: "@ShangmingCai I’ve implemented the logic for the MLA model in [PR 5887]( For non-MLA models, however, I think further design work may still be ..." (https://github.com/sgl-project/sglang/pull/5922#issuecomment-2844805914)
- `2025-05-01T12:36:37Z` `inline` by `ZhengWG` `python/sglang/srt/disaggregation/mooncake/conn.py`:340; signals: oom; excerpt: "Should 'self.transfer infos.pop(req.room)' be moved inside the loop when 'kv chunk.is last == True'?" (https://github.com/sgl-project/sglang/pull/5922#discussion_r2070220705)
- `2025-04-30T16:40:03Z` `issue` by `ShangmingCai`; signals: mla; excerpt: "@ZhengWG I think dummy req might be needed for decode tp size per dp rank prefill tp size per dp rank, this PR will ..." (https://github.com/sgl-project/sglang/pull/5922#issuecomment-2842602724)
- `2025-05-02T03:23:49Z` `issue` by `jokerwyt`; signals: hang; excerpt: "@ShangmingCai @ZhengWG In most cases Prefill TP size will be larger than the Decode TP size. Supporting merging cases such as Prefill TP size=16 ..." (https://github.com/sgl-project/sglang/pull/5922#issuecomment-2846229285)
- `2025-04-30T16:54:32Z` `inline` by `ShangmingCai` `python/sglang/srt/disaggregation/mooncake/conn.py`:531; signals: general review; excerpt: "@ZhengWG I think you can calculate self.target tp ranks here, and only retrieve from the self.target tp ranks[0] while sending dummy requests to self.target ..." (https://github.com/sgl-project/sglang/pull/5922#discussion_r2069103833)
- `2025-05-01T09:46:01Z` `inline` by `ZhengWG` `python/sglang/srt/disaggregation/mooncake/conn.py`:544; signals: general review; excerpt: "@ZhengWG Can you check whether this logic is correct, then add your implementation based on this? Got it, I will add my implementation on ..." (https://github.com/sgl-project/sglang/pull/5922#discussion_r2070104191)
- `2025-05-07T12:49:05Z` `issue` by `ShangmingCai`; signals: mla; excerpt: "@Hongbosherlock Only MLA is supported for now." (https://github.com/sgl-project/sglang/pull/5922#issuecomment-2858464427)
- `2025-04-30T17:43:42Z` `inline` by `ShangmingCai` `python/sglang/srt/disaggregation/mooncake/conn.py`:544; signals: general review; excerpt: "@ZhengWG Can you check whether this logic is correct, then add your implementation based on this?" (https://github.com/sgl-project/sglang/pull/5922#discussion_r2069176405)
- `2025-04-30T16:48:25Z` `issue` by `whybeyoung`; signals: general review; excerpt: "Test Result: - case1: tp16 dp1 in prefill, tp32 dp 4 in decode , not work. raise Error: - case2: tp16 dp4 in prefill ..." (https://github.com/sgl-project/sglang/pull/5922#issuecomment-2842622998)
- `2025-04-30T17:03:43Z` `issue` by `ShangmingCai`; signals: general review; excerpt: "Test Result: case1: tp16 dp1 in prefill, tp32 dp 4 in decode , not work. raise Error: <img alt="image" width="948" src=" This case will ..." (https://github.com/sgl-project/sglang/pull/5922#issuecomment-2842662918)
- `2025-05-07T12:55:54Z` `issue` by `ShangmingCai`; signals: general review; excerpt: "@ZhengWG I added your impl in this PR and made a commit with you as the author since it would be better to combine ..." (https://github.com/sgl-project/sglang/pull/5922#issuecomment-2858490969)
