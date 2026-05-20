# PR Discussion Digest

- Source PR: [vllm-project/vllm#22387](https://github.com/vllm-project/vllm/pull/22387)
- Source page: `sources/prs/vllm/PR-22387.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-22387`
- Generated at: `2026-05-20T15:37:03.245017+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-06T19:54:45Z`
- Merged: `2025-08-21T04:28:32Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 24 (approved=1, commented=23)
- Inline review comments: 30
- Review threads observed: 15
- Resolved/outdated thread markers: resolved=10, outdated=13
- Human participants with discussion text: 22quinn, WoosukKwon, hijkzzz, houseroad, mergify, njhill, simon-mo, youkaichao
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-06T19:56:36Z` `COMMENTED` by `gemini-code-assist` - Code Review This PR introduces a new sampled logprobs mode. I've identified a critical issue in vllm/v1/sample/sampler.py where ... (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3094033701)
- `2025-08-06T22:48:31Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for a new logprobs mode, final logprobs, which allows retrieving log ... (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3094531147)
- `2025-08-11T06:32:14Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3104192578)
- `2025-08-13T15:35:15Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3116576932)
- `2025-08-13T17:17:02Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3117010186)
- `2025-08-13T17:48:48Z` `COMMENTED` by `22quinn` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3117102098)
- `2025-08-15T00:39:39Z` `COMMENTED` by `simon-mo` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3122519330)
- `2025-08-15T03:00:37Z` `COMMENTED` by `22quinn` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3122696546)
- `2025-08-15T16:01:02Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3124376052)
- `2025-08-15T16:01:37Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3124377326)
- `2025-08-15T16:05:31Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3124388866)
- `2025-08-15T16:08:14Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3124399956)
- `2025-08-15T16:35:39Z` `COMMENTED` by `njhill` - Sorry I wrote this review yesterday but somehow didn't submit it :sweat: (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3122545358)
- `2025-08-15T16:39:12Z` `COMMENTED` by `njhill` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3124499387)
- `2025-08-15T23:55:20Z` `COMMENTED` by `22quinn` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3125366893)
- `2025-08-15T23:56:31Z` `COMMENTED` by `22quinn` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3125367500)
- `2025-08-18T07:34:42Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3127144072)
- `2025-08-18T20:03:36Z` `COMMENTED` by `22quinn` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3129729378)
- `2025-08-20T00:21:10Z` `COMMENTED` by `njhill` - Thanks @22quinn, just have a couple of remaining comments (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3134340105)
- `2025-08-20T05:31:50Z` `COMMENTED` by `22quinn` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3134836058)
- `2025-08-20T05:32:10Z` `COMMENTED` by `22quinn` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3134836647)
- `2025-08-20T16:42:23Z` `COMMENTED` by `njhill` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3137452839)
- `2025-08-20T18:56:41Z` `COMMENTED` by `22quinn` (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3137857244)
- `2025-08-21T00:11:14Z` `APPROVED` by `njhill` - Thanks @22quinn! (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3138631544)

## Inline Comment Hotspots

- `vllm/v1/sample/sampler.py`: 22 inline comment(s)
- `vllm/v1/sample/ops/topk_topp_sampler.py`: 5 inline comment(s)
- `vllm/config.py`: 1 inline comment(s)
- `docs/usage/v1_guide.md`: 1 inline comment(s)
- `vllm/config/__init__.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-13T17:48:47Z` `inline` by `22quinn` `vllm/v1/sample/sampler.py`:191; signals: flashinfer, tma; excerpt: "topk topp sampler computes softmax not logsoftmax as an intermediate step. I worry the numerics could be different if we simply add log after ..." (https://github.com/vllm-project/vllm/pull/22387#discussion_r2274207827)
- `2025-08-15T01:37:58Z` `inline` by `njhill` `vllm/v1/sample/sampler.py`:191; signals: flashinfer, tma; excerpt: "The numerics might not be too much of a problem since the logits are fp32 here. Whether or not we reuse the softmax (we ..." (https://github.com/vllm-project/vllm/pull/22387#discussion_r2278057243)
- `2025-08-15T03:00:37Z` `inline` by `22quinn` `vllm/v1/sample/sampler.py`:191; signals: flashinfer, tma; excerpt: "Edit: let me organize it more clearly. Let me know any opinion/preference here. There are two re-computations involved here: apply top k top p ..." (https://github.com/vllm-project/vllm/pull/22387#discussion_r2278129353)
- `2025-08-15T16:05:31Z` `inline` by `WoosukKwon` `vllm/v1/sample/sampler.py`:191; signals: flashinfer, kernel; excerpt: "I think we should use apply top k top p (instead of flashinfer) if the logprobs are required. If we already applied top-p and ..." (https://github.com/vllm-project/vllm/pull/22387#discussion_r2279386212)
- `2025-08-18T20:03:36Z` `inline` by `22quinn` `vllm/v1/sample/sampler.py`:174; signals: hang, tma; excerpt: "I looked into transformers: it [supports]( returning pre-logit-processor logits as logits and post-logit-processor but pre-softmax logits as scores. There's no support for something in ..." (https://github.com/vllm-project/vllm/pull/22387#discussion_r2283335623)
- `2025-08-15T16:08:14Z` `inline` by `WoosukKwon` `vllm/v1/sample/sampler.py`:191; signals: flashinfer; excerpt: "My suggestion is to restructure the code so that when processed logprobs are required, compute top-p/top-k mask only once and use it for both ..." (https://github.com/vllm-project/vllm/pull/22387#discussion_r2279391101)
- `2025-08-20T16:42:23Z` `inline` by `njhill` `vllm/v1/sample/ops/topk_topp_sampler.py`:36; signals: hang; excerpt: "Thanks @22quinn. I was actually thinking the enum could just be internal to the sampler. Because this would technically be a breaking change if ..." (https://github.com/vllm-project/vllm/pull/22387#discussion_r2288742257)
- `2025-08-20T18:56:41Z` `inline` by `22quinn` `vllm/v1/sample/ops/topk_topp_sampler.py`:36; signals: hang; excerpt: "It's fine. We confirmed with major RL frameworks they are not really using this flag yet. And yes vllm serve flag remains unchanged." (https://github.com/vllm-project/vllm/pull/22387#discussion_r2289022480)
- `2025-08-15T16:35:39Z` `review` `COMMENTED` by `njhill`; signals: general review; excerpt: "Sorry I wrote this review yesterday but somehow didn't submit it :sweat:" (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3122545358)
- `2025-08-18T23:16:38Z` `issue` by `njhill`; signals: hang; excerpt: "@22quinn I have some more comments based on the current state. Are you still making changes? I'll hold off making my comments until it's ..." (https://github.com/vllm-project/vllm/pull/22387#issuecomment-3198693711)
- `2025-08-19T00:02:04Z` `issue` by `22quinn`; signals: hang; excerpt: "@22quinn I have some more comments based on the current state. Are you still making changes? I'll hold off making my comments until it's ..." (https://github.com/vllm-project/vllm/pull/22387#issuecomment-3198766114)
- `2025-08-20T00:21:10Z` `review` `COMMENTED` by `njhill`; signals: general review; excerpt: "Thanks @22quinn, just have a couple of remaining comments" (https://github.com/vllm-project/vllm/pull/22387#pullrequestreview-3134340105)
