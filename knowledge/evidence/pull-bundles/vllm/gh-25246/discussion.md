# PR Discussion Digest

- Source PR: [vllm-project/vllm#25246](https://github.com/vllm-project/vllm/pull/25246)
- Source page: `sources/prs/vllm/PR-25246.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-25246`
- Generated at: `2026-05-20T15:37:54.715101+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-19T10:21:20Z`
- Merged: `2025-09-22T08:50:40Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 9
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: NickLucche, benchislett, eldarkurtic, jiahanc, mgoin, rahul-tuli
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-19T10:23:17Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables Eagle3 speculative decoding for the GPT-OSS model. The changes are generally well-implemented, ... (https://github.com/vllm-project/vllm/pull/25246#pullrequestreview-3244242538)
- `2025-09-19T12:53:26Z` `APPROVED` by `rahul-tuli` - Looks good to me! (https://github.com/vllm-project/vllm/pull/25246#pullrequestreview-3244724175)
- `2025-09-19T13:30:25Z` `APPROVED` by `NickLucche` - LGTM but let's wait for someone more familiar with eagle perhaps. Would be great to have smoke tests ... (https://github.com/vllm-project/vllm/pull/25246#pullrequestreview-3244834605)
- `2025-09-19T16:26:31Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/25246#pullrequestreview-3245765104)
- `2025-09-19T16:41:36Z` `COMMENTED` by `eldarkurtic` (https://github.com/vllm-project/vllm/pull/25246#pullrequestreview-3245833984)
- `2025-09-19T16:42:40Z` `COMMENTED` by `eldarkurtic` (https://github.com/vllm-project/vllm/pull/25246#pullrequestreview-3245839393)
- `2025-09-20T10:51:16Z` `COMMENTED` by `eldarkurtic` (https://github.com/vllm-project/vllm/pull/25246#pullrequestreview-3248987915)

## Inline Comment Hotspots

- `vllm/model_executor/models/gpt_oss.py`: 5 inline comment(s)
- `vllm/config/speculative.py`: 2 inline comment(s)
- `vllm/v1/spec_decode/eagle.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-19T14:30:02Z` `issue` by `benchislett`; signals: blackwell, flashinfer; excerpt: "Noting 23596, which implements similarly but includes blackwell support via FlashInfer. Should be fine to merge this one first, but we should make sure ..." (https://github.com/vllm-project/vllm/pull/25246#issuecomment-3312435488)
- `2025-09-19T15:51:28Z` `issue` by `jiahanc`; signals: accuracy, attention; excerpt: "I think for models with alternative attentions like gpt-oss, you need to find correct attention builders for draft model (draft model is full attention) ..." (https://github.com/vllm-project/vllm/pull/25246#issuecomment-3312723582)
- `2025-09-20T11:02:15Z` `issue` by `eldarkurtic`; signals: block; excerpt: "The goal of this one was to first add support for the simplest Llama-like-speculator from Eagle3. And then we can build on top of ..." (https://github.com/vllm-project/vllm/pull/25246#issuecomment-3314897259)
- `2025-09-19T13:21:00Z` `inline` by `NickLucche` `vllm/config/speculative.py`:530; signals: general review; excerpt: "unrelated to this PR, but I wonder why do we have to list models here instead of relying on SupportsEagle3 dispatching" (https://github.com/vllm-project/vllm/pull/25246#discussion_r2362876457)
- `2025-09-19T12:50:54Z` `inline` by `rahul-tuli` `vllm/model_executor/models/gpt_oss.py`:242; signals: general review; excerpt: "Should this be:" (https://github.com/vllm-project/vllm/pull/25246#discussion_r2362784879)
- `2025-09-19T13:18:16Z` `inline` by `NickLucche` `vllm/model_executor/models/gpt_oss.py`:242; signals: general review; excerpt: "it's a newer syntax, it's still consistent" (https://github.com/vllm-project/vllm/pull/25246#discussion_r2362869546)
- `2025-09-19T13:29:13Z` `inline` by `NickLucche` `vllm/v1/spec_decode/eagle.py`:846; signals: general review; excerpt: "should be picked up by gc" (https://github.com/vllm-project/vllm/pull/25246#discussion_r2362897038)
- `2025-09-19T16:26:31Z` `inline` by `mgoin` `vllm/model_executor/models/gpt_oss.py`:242; signals: general review; excerpt: "Is it valid for python 3.9? That is still our minimum" (https://github.com/vllm-project/vllm/pull/25246#discussion_r2363534743)
- `2025-09-19T16:41:36Z` `inline` by `eldarkurtic` `vllm/model_executor/models/gpt_oss.py`:242; signals: general review; excerpt: "It is copy-pasted from llama.py and qwen.py in vllm main" (https://github.com/vllm-project/vllm/pull/25246#discussion_r2363586503)
- `2025-09-19T16:42:39Z` `inline` by `eldarkurtic` `vllm/config/speculative.py`:530; signals: general review; excerpt: "To be honest not sure, I just followed llama.py / qwen.py to see how eagle is enabled there" (https://github.com/vllm-project/vllm/pull/25246#discussion_r2363590727)
- `2025-09-20T10:51:16Z` `inline` by `eldarkurtic` `vllm/v1/spec_decode/eagle.py`:846; signals: general review; excerpt: "I took this from llama.py and qwen.py. Should I remove it here or leave it for consistency?" (https://github.com/vllm-project/vllm/pull/25246#discussion_r2365582423)
- `2025-09-19T13:30:25Z` `review` `APPROVED` by `NickLucche`; signals: general review; excerpt: "LGTM but let's wait for someone more familiar with eagle perhaps. Would be great to have smoke tests for model init at least with ..." (https://github.com/vllm-project/vllm/pull/25246#pullrequestreview-3244834605)
