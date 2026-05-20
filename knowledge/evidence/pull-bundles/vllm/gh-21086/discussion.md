# PR Discussion Digest

- Source PR: [vllm-project/vllm#21086](https://github.com/vllm-project/vllm/pull/21086)
- Source page: `sources/prs/vllm/PR-21086.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21086`
- Generated at: `2026-05-20T15:36:24.638914+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-17T01:57:00Z`
- Merged: `2025-08-20T11:01:31Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 12 (approved=2, commented=10)
- Inline review comments: 11
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=2, outdated=3
- Human participants with discussion text: Ja1Zhou, aarnphm, benchislett, gyou2021, simon-mo, xyang16
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-07-17T01:58:52Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for Eagle speculative decoding with Deepseek models. I've found a few ... (https://github.com/vllm-project/vllm/pull/21086#pullrequestreview-3027458451)
- `2025-07-29T17:12:46Z` `COMMENTED` by `aarnphm` - Do you have a eagle checkpoint to test with this? If you have some numbers that would be ... (https://github.com/vllm-project/vllm/pull/21086#pullrequestreview-3068478027)
- `2025-08-14T22:40:15Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/21086#pullrequestreview-3122293848)
- `2025-08-14T22:42:52Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/21086#pullrequestreview-3122298175)
- `2025-08-14T22:45:52Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/21086#pullrequestreview-3122301897)
- `2025-08-14T23:26:20Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/21086#pullrequestreview-3122423546)
- `2025-08-14T23:53:01Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/21086#pullrequestreview-3122458789)
- `2025-08-14T23:57:55Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/21086#pullrequestreview-3122465387)
- `2025-08-15T00:00:24Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/21086#pullrequestreview-3122469284)
- `2025-08-18T21:42:45Z` `APPROVED` by `benchislett` - The implementation now seems more in-line with the MTP implementation. There are still differences between how we handle ... (https://github.com/vllm-project/vllm/pull/21086#pullrequestreview-3130062629)
- `2025-08-18T21:43:57Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/21086#pullrequestreview-3130065296)
- `2025-08-19T22:06:17Z` `APPROVED` by `simon-mo` - Stamping given Benjamin approved. (https://github.com/vllm-project/vllm/pull/21086#pullrequestreview-3133979938)

## Inline Comment Hotspots

- `vllm/model_executor/models/deepseek_eagle.py`: 10 inline comment(s)
- `vllm/model_executor/models/registry.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-14T22:42:51Z` `inline` by `benchislett` `vllm/model_executor/models/deepseek_eagle.py`:89; signals: attention; excerpt: "There have been many discussions in the community about how to properly handle the rotated input slot, but this does not seem in line ..." (https://github.com/vllm-project/vllm/pull/21086#discussion_r2277863258)
- `2025-08-14T22:45:52Z` `inline` by `benchislett` `vllm/model_executor/models/deepseek_eagle.py`:85; signals: attention; excerpt: "This looks like too many norms being applied. In the Llama Eagle reference code, the input layernorm to each layer is disabled, and IIRC ..." (https://github.com/vllm-project/vllm/pull/21086#discussion_r2277866407)
- `2025-08-14T23:53:00Z` `inline` by `xyang16` `vllm/model_executor/models/deepseek_eagle.py`:85; signals: benchmark; excerpt: "I have taken a look at the deepseek mtp.py at The only difference is output self.norm. But in our benchmarking, we found that including ..." (https://github.com/vllm-project/vllm/pull/21086#discussion_r2277963506)
- `2025-08-14T23:57:55Z` `inline` by `xyang16` `vllm/model_executor/models/deepseek_eagle.py`:89; signals: attention; excerpt: "Yes, there's discussion this will mess up the attention normalization. I have removed this. Please review. Thanks." (https://github.com/vllm-project/vllm/pull/21086#discussion_r2277970026)
- `2025-07-29T17:12:46Z` `review` `COMMENTED` by `aarnphm`; signals: general review; excerpt: "Do you have a eagle checkpoint to test with this? If you have some numbers that would be great. Llama 4 EAGLE was landed ..." (https://github.com/vllm-project/vllm/pull/21086#pullrequestreview-3068478027)
- `2025-08-14T22:40:14Z` `inline` by `benchislett` `vllm/model_executor/models/deepseek_eagle.py`:102; signals: general review; excerpt: "Does this need to be made compatible with the fused qkv a proj optimization from 21116? I have observed multiple issues with weight loading ..." (https://github.com/vllm-project/vllm/pull/21086#discussion_r2277859980)
- `2025-08-15T00:00:24Z` `inline` by `xyang16` `vllm/model_executor/models/deepseek_eagle.py`:89; signals: general review; excerpt: "I see deepseek mtp.py has also masked the hidden states to 0: I can remove the line in deepseek mtp.py together in this PR. ..." (https://github.com/vllm-project/vllm/pull/21086#discussion_r2277973995)
- `2025-08-18T21:43:57Z` `inline` by `benchislett` `vllm/model_executor/models/deepseek_eagle.py`:89; signals: general review; excerpt: "Perhaps best to leave it pending a complete study of impact on AL for MTP. If there isn't a github issue for this task, ..." (https://github.com/vllm-project/vllm/pull/21086#discussion_r2283563296)
- `2025-08-14T23:26:20Z` `inline` by `xyang16` `vllm/model_executor/models/deepseek_eagle.py`:102; signals: general review; excerpt: "I have updated the stacked params mapping. Thanks!" (https://github.com/vllm-project/vllm/pull/21086#discussion_r2277937642)
- `2025-07-17T05:03:55Z` `issue` by `Ja1Zhou`; signals: general review; excerpt: "Hi! I tried installing this pr from source. But got Should the auto map field of [config.json]( be fixed?" (https://github.com/vllm-project/vllm/pull/21086#issuecomment-3082520646)
- `2025-07-17T05:23:56Z` `issue` by `xyang16`; signals: general review; excerpt: "Hi! I tried installing this pr from source. But got Should the auto map field of [config.json]( be fixed? Thanks for your comment, fixed ..." (https://github.com/vllm-project/vllm/pull/21086#issuecomment-3082575172)
- `2025-07-17T16:58:41Z` `issue` by `Ja1Zhou`; signals: general review; excerpt: "Hi! I tried installing this pr from source. But got Should the auto map field of [config.json]( be fixed? Thanks for your comment, fixed ..." (https://github.com/vllm-project/vllm/pull/21086#issuecomment-3084771847)
