# PR Discussion Digest

- Source PR: [vllm-project/vllm#22637](https://github.com/vllm-project/vllm/pull/22637)
- Source page: `sources/prs/vllm/PR-22637.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-22637`
- Generated at: `2026-05-20T15:37:06.512470+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-11T09:49:55Z`
- Merged: `2025-08-12T07:23:18Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 15 (approved=1, commented=14)
- Inline review comments: 13
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: DarkLight1337, maxdebayser, mergify, noooop
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-11T09:51:24Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request provides a set of crucial bug fixes for the ModernBert model implementation, ensuring ... (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3104954020)
- `2025-08-11T09:53:14Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3104967423)
- `2025-08-11T09:56:44Z` `COMMENTED` by `noooop` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3104986775)
- `2025-08-11T10:03:02Z` `COMMENTED` by `noooop` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3105040364)
- `2025-08-11T10:11:20Z` `COMMENTED` by `noooop` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3105095031)
- `2025-08-11T10:18:23Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3105127180)
- `2025-08-11T10:18:42Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3105128607)
- `2025-08-11T10:24:03Z` `COMMENTED` by `noooop` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3105153853)
- `2025-08-11T14:34:43Z` `COMMENTED` by `maxdebayser` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3106209584)
- `2025-08-11T14:59:06Z` `COMMENTED` by `maxdebayser` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3106306959)
- `2025-08-11T17:22:47Z` `COMMENTED` by `maxdebayser` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3106936190)
- `2025-08-11T20:10:54Z` `COMMENTED` by `maxdebayser` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3107635365)
- `2025-08-11T23:24:49Z` `COMMENTED` by `noooop` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3108051251)
- `2025-08-11T23:26:44Z` `COMMENTED` by `noooop` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3108053968)
- `2025-08-12T02:51:39Z` `APPROVED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/22637#pullrequestreview-3108375537)

## Inline Comment Hotspots

- `vllm/model_executor/models/modernbert.py`: 13 inline comment(s)

## High-Signal Discussion

- `2025-08-11T14:34:43Z` `inline` by `maxdebayser` `vllm/model_executor/models/modernbert.py`:298; signals: attention; excerpt: "I think it's because of the sliding window attention that is used in some layers. When I disable it in transformers I get the ..." (https://github.com/vllm-project/vllm/pull/22637#discussion_r2266980119)
- `2025-08-11T14:59:06Z` `inline` by `maxdebayser` `vllm/model_executor/models/modernbert.py`:298; signals: attention; excerpt: "I got it working locally by hacking flash attn. Let me see now what's the right way to do it and also apply it ..." (https://github.com/vllm-project/vllm/pull/22637#discussion_r2267052459)
- `2025-08-11T17:22:47Z` `inline` by `maxdebayser` `vllm/model_executor/models/modernbert.py`:298; signals: hang; excerpt: "@noooop here are the changes required to run with sliding attn: . Feel free to cherry-pick the commit." (https://github.com/vllm-project/vllm/pull/22637#discussion_r2267496668)
- `2025-08-11T20:10:54Z` `inline` by `maxdebayser` `vllm/model_executor/models/modernbert.py`:298; signals: attention; excerpt: "Actually, there was a missing detail to the commit above. Since the attention spec is not uniform, I had to map it to the ..." (https://github.com/vllm-project/vllm/pull/22637#discussion_r2267914218)
- `2025-08-12T00:43:30Z` `issue` by `noooop`; signals: hang; excerpt: "I've pushed the sliding attn changes directly on your PR, I hope that's OK. The local test runs successfully on my machine. Looking forward ..." (https://github.com/vllm-project/vllm/pull/22637#issuecomment-3177320387)
- `2025-08-11T09:56:44Z` `inline` by `noooop` `vllm/model_executor/models/modernbert.py`:298; signals: general review; excerpt: "Well, I think there is a problem with this ModernBERT implementation, but I don't know how to fix it, so I try to leave ..." (https://github.com/vllm-project/vllm/pull/22637#discussion_r2266203831)
- `2025-08-11T23:24:49Z` `inline` by `noooop` `vllm/model_executor/models/modernbert.py`:298; signals: general review; excerpt: "@maxdebayser I hope to collaborate with you on this. I have done some clean up, please submit directly to this branch" (https://github.com/vllm-project/vllm/pull/22637#discussion_r2268219561)
- `2025-08-11T23:26:44Z` `inline` by `noooop` `vllm/model_executor/models/modernbert.py`:298; signals: general review; excerpt: "I only kept the Alibaba-NLP/gte-reranker-modernbert-base test pytest -s -vvv tests/models/language/pooling/test gte.py::test rerank models mteb" (https://github.com/vllm-project/vllm/pull/22637#discussion_r2268221548)
- `2025-08-12T00:36:25Z` `issue` by `maxdebayser`; signals: hang; excerpt: "I've pushed the sliding attn changes directly on your PR, I hope that's OK." (https://github.com/vllm-project/vllm/pull/22637#issuecomment-3177308248)
- `2025-08-11T09:53:14Z` `inline` by `DarkLight1337` `vllm/model_executor/models/modernbert.py`:298; signals: general review; excerpt: "Was this missed in a previous PR? The weight loading has nothing to do with V1 right?" (https://github.com/vllm-project/vllm/pull/22637#discussion_r2266195613)
- `2025-08-11T10:03:01Z` `inline` by `noooop` `vllm/model_executor/models/modernbert.py`:298; signals: general review; excerpt: "The difference becomes significant when the input is around 48." (https://github.com/vllm-project/vllm/pull/22637#discussion_r2266219301)
- `2025-08-11T10:11:19Z` `inline` by `noooop` `vllm/model_executor/models/modernbert.py`:298; signals: general review; excerpt: "But now almost all pooling models support v1, I don't want it to hold V0 Deprecation." (https://github.com/vllm-project/vllm/pull/22637#discussion_r2266238527)
