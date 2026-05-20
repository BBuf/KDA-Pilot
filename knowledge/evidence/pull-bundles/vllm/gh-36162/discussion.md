# PR Discussion Digest

- Source PR: [vllm-project/vllm#36162](https://github.com/vllm-project/vllm/pull/36162)
- Source page: `sources/prs/vllm/PR-36162.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36162`
- Generated at: `2026-05-20T15:40:09.061442+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-05T17:45:28Z`
- Merged: `2026-04-14T19:10:59Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 18 (approved=4, commented=14)
- Inline review comments: 13
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=7, outdated=5
- Human participants with discussion text: amirkl94, hmellor, mergify, mgoin, roikoren755, tdoublep, tomeras91
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2026-03-05T17:48:29Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for the Flashinfer selective state update kernel as an alternative to ... (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-3898505137)
- `2026-03-16T09:10:14Z` `COMMENTED` by `hmellor` - Could we not introduce an enum to vllm.config, we we have been reserving this namespace for config classes ... (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-3952381167)
- `2026-04-05T19:54:52Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4059787880)
- `2026-04-05T19:56:46Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4059789148)
- `2026-04-05T19:59:48Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4059792024)
- `2026-04-05T20:04:55Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4059795812)
- `2026-04-05T20:10:09Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4059799693)
- `2026-04-05T20:11:38Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4059800652)
- `2026-04-06T09:02:22Z` `COMMENTED` by `roikoren755` (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4061162618)
- `2026-04-06T09:05:32Z` `COMMENTED` by `roikoren755` (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4061173687)
- `2026-04-06T09:06:19Z` `COMMENTED` by `roikoren755` (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4061176180)
- `2026-04-06T09:07:07Z` `COMMENTED` by `roikoren755` (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4061178868)
- `2026-04-06T13:45:52Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4062310900)
- `2026-04-06T13:46:35Z` `APPROVED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4062314101)
- `2026-04-06T13:46:52Z` `APPROVED` by `amirkl94` - LGTM (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4062315314)
- `2026-04-12T16:17:14Z` `COMMENTED` by `tomeras91` - Overall looks good! I do have some comments though: 1. I agree with @amirkl94 we should have the ... (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4095244969)
- `2026-04-14T18:58:19Z` `APPROVED` by `tdoublep` - LGTM We might want to revisit whether the dispatch could be better handled by vLLM IR at a ... (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4108416448)
- `2026-04-14T19:09:46Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4108482959)

## Inline Comment Hotspots

- `vllm/config/mamba.py`: 5 inline comment(s)
- `tests/kernels/mamba/test_ssu_dispatch.py`: 3 inline comment(s)
- `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`: 3 inline comment(s)
- `vllm/config/__init__.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-12T16:17:14Z` `review` `COMMENTED` by `tomeras91`; signals: flashinfer, triton; excerpt: "Overall looks good! I do have some comments though: 1. I agree with @amirkl94 we should have the triton backend as default so we ..." (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-4095244969)
- `2026-04-13T10:03:53Z` `issue` by `roikoren755`; signals: flashinfer, kernel, triton; excerpt: "Overall looks good! I do have some comments though: 1. I agree with @amirkl94 we should have the triton backend as default so we ..." (https://github.com/vllm-project/vllm/pull/36162#issuecomment-4235544017)
- `2026-04-05T20:04:55Z` `inline` by `amirkl94` `vllm/config/mamba.py`:33; signals: cache, dtype; excerpt: "Does moving the cache dtype here make sense?" (https://github.com/vllm-project/vllm/pull/36162#discussion_r3037294175)
- `2026-04-06T09:07:06Z` `inline` by `roikoren755` `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`:113; signals: flashinfer, kernel; excerpt: "No, the flashinfer kernel should work on all SMs" (https://github.com/vllm-project/vllm/pull/36162#discussion_r3038708637)
- `2026-04-05T19:59:48Z` `inline` by `amirkl94` `vllm/config/mamba.py`:66; signals: triton; excerpt: "The comment above says that self.backend defaults to triton so I may be wrong, but it looks like self.backend can be None here, and ..." (https://github.com/vllm-project/vllm/pull/36162#discussion_r3037289033)
- `2026-03-16T09:10:14Z` `review` `COMMENTED` by `hmellor`; signals: general review; excerpt: "Could we not introduce an enum to vllm.config, we we have been reserving this namespace for config classes only" (https://github.com/vllm-project/vllm/pull/36162#pullrequestreview-3952381167)
- `2026-04-05T19:54:52Z` `inline` by `amirkl94` `tests/kernels/mamba/test_ssu_dispatch.py`:70; signals: kernel; excerpt: "Maybe add a seed so that the test is deterministic?" (https://github.com/vllm-project/vllm/pull/36162#discussion_r3037283772)
- `2026-04-05T19:56:46Z` `inline` by `amirkl94` `tests/kernels/mamba/test_ssu_dispatch.py`:62; signals: kernel; excerpt: "What's the purpose of this test?" (https://github.com/vllm-project/vllm/pull/36162#discussion_r3037285699)
- `2026-04-05T20:11:39Z` `inline` by `amirkl94` `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`:113; signals: kernel; excerpt: "Is there an sm requirement for this kernel as well?" (https://github.com/vllm-project/vllm/pull/36162#discussion_r3037300814)
- `2026-04-06T09:02:22Z` `inline` by `roikoren755` `tests/kernels/mamba/test_ssu_dispatch.py`:62; signals: kernel; excerpt: "It's a sanity check that calling the wrapper function doesn't fail" (https://github.com/vllm-project/vllm/pull/36162#discussion_r3038692915)
- `2026-04-06T13:45:52Z` `inline` by `amirkl94` `vllm/config/mamba.py`:58; signals: triton; excerpt: "If the default is TRITON maybe we can just remove the None option and set:" (https://github.com/vllm-project/vllm/pull/36162#discussion_r3039742039)
- `2026-04-06T09:06:19Z` `inline` by `roikoren755` `vllm/config/mamba.py`:33; signals: general review; excerpt: "Thought about that, but that's a much bigger refactor than moving the stochastic rounding fields, so I decided against it. We can do that ..." (https://github.com/vllm-project/vllm/pull/36162#discussion_r3038705632)
