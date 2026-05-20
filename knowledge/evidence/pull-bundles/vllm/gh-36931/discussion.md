# PR Discussion Digest

- Source PR: [vllm-project/vllm#36931](https://github.com/vllm-project/vllm/pull/36931)
- Source page: `sources/prs/vllm/PR-36931.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36931`
- Generated at: `2026-05-20T15:40:16.132365+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-12T21:56:20Z`
- Merged: `2026-03-13T23:41:16Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: dbari, pavanimajety, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-12T21:57:31Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces three main changes: it enables an additional dimension (qk nope head dim=64) ... (https://github.com/vllm-project/vllm/pull/36931#pullrequestreview-3939991299)
- `2026-03-13T20:36:23Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/36931#pullrequestreview-3946840389)
- `2026-03-13T20:43:54Z` `APPROVED` by `pavanimajety` - LGTM, @dbari, Thanks for the PR. (https://github.com/vllm-project/vllm/pull/36931#pullrequestreview-3946843326)
- `2026-03-13T20:47:19Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36931#pullrequestreview-3946879132)
- `2026-03-13T20:48:45Z` `COMMENTED` by `dbari` (https://github.com/vllm-project/vllm/pull/36931#pullrequestreview-3946884201)

## Inline Comment Hotspots

- `vllm/model_executor/models/deepseek_v2.py`: 5 inline comment(s)

## High-Signal Discussion

- `2026-03-13T20:43:06Z` `inline` by `pavanimajety` `vllm/model_executor/models/deepseek_v2.py`:345; signals: dtype, flashinfer, kernel; excerpt: "@robertgshaw2-redhat shouldn't torch.float32 be default for all Deepseek Architectures (i.e. when RoutingMethodType==DeepseekV3) and not just flashinfer trtllm / monolithic kernels?" (https://github.com/vllm-project/vllm/pull/36931#discussion_r2933679134)
- `2026-03-13T20:47:19Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/models/deepseek_v2.py`:345; signals: kernel; excerpt: "I don’t think the grouped took kernels in vLLM support fp32. Ideally we could add this support. Need to double checj" (https://github.com/vllm-project/vllm/pull/36931#discussion_r2933694224)
- `2026-03-13T20:48:45Z` `inline` by `dbari` `vllm/model_executor/models/deepseek_v2.py`:1212; signals: compile; excerpt: "I ran into an error of the compilation, where the function was called with both arguments None and the compilation failed due to a ..." (https://github.com/vllm-project/vllm/pull/36931#discussion_r2933699344)
- `2026-03-13T20:36:23Z` `inline` by `pavanimajety` `vllm/model_executor/models/deepseek_v2.py`:340; signals: general review; excerpt: "@robertgshaw2-redhat for viz & review" (https://github.com/vllm-project/vllm/pull/36931#discussion_r2933654589)
- `2026-03-13T20:37:13Z` `inline` by `pavanimajety` `vllm/model_executor/models/deepseek_v2.py`:1212; signals: general review; excerpt: "when would we run into this?" (https://github.com/vllm-project/vllm/pull/36931#discussion_r2933657639)
