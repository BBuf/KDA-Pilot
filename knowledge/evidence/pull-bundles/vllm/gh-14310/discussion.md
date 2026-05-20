# PR Discussion Digest

- Source PR: [vllm-project/vllm#14310](https://github.com/vllm-project/vllm/pull/14310)
- Source page: `sources/prs/vllm/PR-14310.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14310`
- Generated at: `2026-05-20T15:34:21.321830+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-05T20:50:15Z`
- Merged: `2025-03-06T23:31:05Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 9 (approved=2, commented=7)
- Inline review comments: 13
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=2
- Human participants with discussion text: alexm-redhat, mergify, mgoin, yaochengji
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-05T21:38:59Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/14310#pullrequestreview-2662550584)
- `2025-03-05T21:40:08Z` `COMMENTED` by `yaochengji` (https://github.com/vllm-project/vllm/pull/14310#pullrequestreview-2662556437)
- `2025-03-06T14:49:02Z` `COMMENTED` by `alexm-redhat` - @yaochengji thanks for the PR! I did a first review pass and have some questions about parameters that ... (https://github.com/vllm-project/vllm/pull/14310#pullrequestreview-2664663545)
- `2025-03-06T19:47:02Z` `COMMENTED` by `yaochengji` (https://github.com/vllm-project/vllm/pull/14310#pullrequestreview-2665465513)
- `2025-03-06T19:52:17Z` `COMMENTED` by `yaochengji` (https://github.com/vllm-project/vllm/pull/14310#pullrequestreview-2665475725)
- `2025-03-06T19:53:06Z` `COMMENTED` by `yaochengji` (https://github.com/vllm-project/vllm/pull/14310#pullrequestreview-2665477307)
- `2025-03-06T21:46:30Z` `COMMENTED` by `yaochengji` (https://github.com/vllm-project/vllm/pull/14310#pullrequestreview-2665709536)
- `2025-03-06T21:52:24Z` `APPROVED` by `alexm-redhat` - @yaochengji LGTM! ready to merge when green. (https://github.com/vllm-project/vllm/pull/14310#pullrequestreview-2665717666)
- `2025-03-06T23:10:00Z` `APPROVED` by `mgoin` - i was able to run gsm8k on qwen2, great work! (https://github.com/vllm-project/vllm/pull/14310#pullrequestreview-2665828670)

## Inline Comment Hotspots

- `vllm/v1/worker/tpu_model_runner.py`: 10 inline comment(s)
- `vllm/v1/attention/backends/pallas.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-03-06T19:53:06Z` `inline` by `yaochengji` `vllm/v1/worker/tpu_model_runner.py`:722; signals: compile, hang; excerpt: "actual num reqs is int and num seqs is Tensor. torch dynamo will always recompile if the value of an int variable changes." (https://github.com/vllm-project/vllm/pull/14310#discussion_r1983967472)
- `2025-03-05T21:40:08Z` `inline` by `yaochengji` `vllm/v1/attention/backends/pallas.py`:167; signals: attention, kernel; excerpt: "Yes, @vanbasten23 is tuning the kernel parameter, will update it later." (https://github.com/vllm-project/vllm/pull/14310#discussion_r1982223053)
- `2025-03-06T14:42:09Z` `inline` by `alexm-redhat` `vllm/v1/worker/tpu_model_runner.py`:435; signals: block; excerpt: "I see that padding is applied to inputs ids, position ids and slot mapping. Why it is not necessary to apply padding to block ..." (https://github.com/vllm-project/vllm/pull/14310#discussion_r1983483591)
- `2025-03-06T19:47:02Z` `inline` by `yaochengji` `vllm/v1/worker/tpu_model_runner.py`:435; signals: block; excerpt: "Because the first dimension of block table, query start loc and seq lens are at most max num reqs. Padding them based on token ..." (https://github.com/vllm-project/vllm/pull/14310#discussion_r1983960427)
- `2025-03-05T21:36:54Z` `inline` by `mgoin` `vllm/v1/attention/backends/pallas.py`:167; signals: attention; excerpt: "Should this shift depending on device?" (https://github.com/vllm-project/vllm/pull/14310#discussion_r1982219316)
- `2025-03-06T14:42:21Z` `inline` by `alexm-redhat` `vllm/v1/worker/tpu_model_runner.py`:431; signals: block; excerpt: "rename padded block table = block table" (https://github.com/vllm-project/vllm/pull/14310#discussion_r1983483950)
- `2025-03-06T14:49:02Z` `review` `COMMENTED` by `alexm-redhat`; signals: general review; excerpt: "@yaochengji thanks for the PR! I did a first review pass and have some questions about parameters that would be good to understand." (https://github.com/vllm-project/vllm/pull/14310#pullrequestreview-2664663545)
- `2025-03-06T21:46:30Z` `inline` by `yaochengji` `vllm/v1/attention/backends/pallas.py`:167; signals: attention; excerpt: "The parameter is updated, thanks!" (https://github.com/vllm-project/vllm/pull/14310#discussion_r1984096656)
- `2025-03-06T14:47:06Z` `inline` by `alexm-redhat` `vllm/v1/worker/tpu_model_runner.py`:703; signals: general review; excerpt: "Why not use "actual num reqs" here? I.e why do we need to max the num of sequences for the dummy run?" (https://github.com/vllm-project/vllm/pull/14310#discussion_r1983492533)
- `2025-03-06T14:47:51Z` `inline` by `alexm-redhat` `vllm/v1/worker/tpu_model_runner.py`:722; signals: general review; excerpt: "why not actual num reqs?" (https://github.com/vllm-project/vllm/pull/14310#discussion_r1983493852)
- `2025-03-06T19:52:17Z` `inline` by `yaochengji` `vllm/v1/worker/tpu_model_runner.py`:703; signals: general review; excerpt: "To avoid recompilation, then only dimension that can vary is the token num." (https://github.com/vllm-project/vllm/pull/14310#discussion_r1983966494)
- `2025-03-06T21:51:23Z` `inline` by `alexm-redhat` `vllm/v1/worker/tpu_model_runner.py`:435; signals: general review; excerpt: "oh I see, this is already maxed, ok makes sense." (https://github.com/vllm-project/vllm/pull/14310#discussion_r1984101576)
