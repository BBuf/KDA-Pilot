# PR Discussion Digest

- Source PR: [vllm-project/vllm#39391](https://github.com/vllm-project/vllm/pull/39391)
- Source page: `sources/prs/vllm/PR-39391.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-39391`
- Generated at: `2026-05-20T15:40:44.971314+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-09T06:33:42Z`
- Merged: `2026-04-21T11:04:41Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 12 (approved=2, commented=10)
- Inline review comments: 8
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: ZJY0516, jhaotingc, mergify, tlrmchlsmth, vadiklyutiy
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-09T06:35:57Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request implements NaN and Inf clamping within the optimized topkGating kernel to prevent duplicate ... (https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4080156611)
- `2026-04-16T16:50:06Z` `COMMENTED` by `ZJY0516` - please add a test for this (https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4122774686)
- `2026-04-16T20:12:33Z` `COMMENTED` by `jhaotingc` (https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4124116471)
- `2026-04-16T20:19:40Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4124164432)
- `2026-04-16T20:57:32Z` `COMMENTED` by `jhaotingc` (https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4124393446)
- `2026-04-17T15:04:10Z` `COMMENTED` by `ZJY0516` (https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4129889672)
- `2026-04-17T17:29:09Z` `COMMENTED` by `jhaotingc` (https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4130819917)
- `2026-04-20T13:44:18Z` `COMMENTED` by `tlrmchlsmth` - This seems like a reasonable approach. My concern would be around fragility in case some other topk softmax ... (https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4140535706)
- `2026-04-20T13:54:12Z` `APPROVED` by `ZJY0516` (https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4140609344)
- `2026-04-21T00:53:23Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4144370382)
- `2026-04-21T00:55:37Z` `COMMENTED` by `vadiklyutiy` - After fixing - add to CI - add fused topk bias - will look good to me (https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4144377845)
- `2026-04-21T11:04:26Z` `APPROVED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4147147496)

## Inline Comment Hotspots

- `csrc/moe/topk_softmax_kernels.cu`: 7 inline comment(s)
- `tests/kernels/moe/test_fused_topk.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-20T17:28:51Z` `issue` by `jhaotingc`; signals: kernel, nan, perf, performance, tma; excerpt: "My only concern is whether the overhead from these additional check is acceptable. My concern would be around fragility in case some other topk ..." (https://github.com/vllm-project/vllm/pull/39391#issuecomment-4282940613)
- `2026-04-16T20:57:32Z` `inline` by `jhaotingc` `csrc/moe/topk_softmax_kernels.cu`:451; signals: kernel, moe, nan, tma; excerpt: "for padded tokens, seems that qwen3.5 processes zero hidden states - some how after some layer they all become nan, which lead to this ..." (https://github.com/vllm-project/vllm/pull/39391#discussion_r3096324841)
- `2026-04-16T20:19:40Z` `inline` by `vadiklyutiy` `csrc/moe/topk_softmax_kernels.cu`:451; signals: kernel, moe, nan, tma; excerpt: "Does "all-NaN" mean NaN for padded tokens or NaN for all tokens (padded and regular)?" (https://github.com/vllm-project/vllm/pull/39391#discussion_r3096134683)
- `2026-04-17T15:03:58Z` `inline` by `ZJY0516` `csrc/moe/topk_softmax_kernels.cu`:129; signals: hang, kernel, moe, tma; excerpt: "Do we really need to change this?" (https://github.com/vllm-project/vllm/pull/39391#discussion_r3101266903)
- `2026-04-20T13:44:18Z` `review` `COMMENTED` by `tlrmchlsmth`; signals: kernel, nan, tma; excerpt: "This seems like a reasonable approach. My concern would be around fragility in case some other topk softmax kernel is used that doesn't suppress ..." (https://github.com/vllm-project/vllm/pull/39391#pullrequestreview-4140535706)
- `2026-04-17T17:29:09Z` `inline` by `jhaotingc` `csrc/moe/topk_softmax_kernels.cu`:129; signals: kernel, moe, tma; excerpt: "Here's the logics to choose either (1) topkGatingSoftmax kernel or (2) moeSoftmax/moeSigmoid kernel when calculating topk. If the expert num is not what's listed ..." (https://github.com/vllm-project/vllm/pull/39391#discussion_r3102122329)
- `2026-04-16T20:12:33Z` `inline` by `jhaotingc` `csrc/moe/topk_softmax_kernels.cu`:460; signals: kernel, moe, tma; excerpt: "Also included" (https://github.com/vllm-project/vllm/pull/39391#discussion_r3096090005)
- `2026-04-17T15:04:05Z` `inline` by `ZJY0516` `csrc/moe/topk_softmax_kernels.cu`:152; signals: kernel, moe, tma; excerpt: "same" (https://github.com/vllm-project/vllm/pull/39391#discussion_r3101267538)
- `2026-04-20T13:53:16Z` `issue` by `ZJY0516`; signals: kernel, nan, tma; excerpt: "My only concern is whether the overhead from these additional check is acceptable. My concern would be around fragility in case some other topk ..." (https://github.com/vllm-project/vllm/pull/39391#issuecomment-4281345250)
- `2026-04-21T00:53:23Z` `inline` by `vadiklyutiy` `tests/kernels/moe/test_fused_topk.py`:173; signals: kernel, moe; excerpt: "Could you add test for fused topk bias as well." (https://github.com/vllm-project/vllm/pull/39391#discussion_r3114432434)
- `2026-04-16T18:48:58Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @jhaotingc, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/39391#issuecomment-4262611070)
- `2026-04-16T19:03:31Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @jhaotingc, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/39391#issuecomment-4262695500)
