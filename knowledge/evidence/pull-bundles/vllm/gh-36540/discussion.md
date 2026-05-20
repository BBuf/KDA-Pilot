# PR Discussion Digest

- Source PR: [vllm-project/vllm#36540](https://github.com/vllm-project/vllm/pull/36540)
- Source page: `sources/prs/vllm/PR-36540.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36540`
- Generated at: `2026-05-20T15:40:13.282726+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-09T20:42:56Z`
- Merged: `2026-03-31T19:30:27Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 9
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=1
- Human participants with discussion text: LucasWilkinson, evezhier, mergify, pavanimajety
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-09T20:53:29Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to remove buffer prefills for run prefill context chunk trtllm ragged and ... (https://github.com/vllm-project/vllm/pull/36540#pullrequestreview-3918153691)
- `2026-03-10T08:31:29Z` `COMMENTED` by `evezhier` (https://github.com/vllm-project/vllm/pull/36540#pullrequestreview-3920649797)
- `2026-03-11T20:26:55Z` `COMMENTED` by `pavanimajety` - Thanks for the PR, do we see any reduced perf due to the additional logic for batches of ... (https://github.com/vllm-project/vllm/pull/36540#pullrequestreview-3932341428)
- `2026-03-16T22:06:36Z` `COMMENTED` by `evezhier` (https://github.com/vllm-project/vllm/pull/36540#pullrequestreview-3956937842)
- `2026-03-24T02:20:53Z` `APPROVED` by `LucasWilkinson` - Overall LGTM; thanks for doing this! left one comment thats worth addressing (https://github.com/vllm-project/vllm/pull/36540#pullrequestreview-3995829395)
- `2026-03-31T15:10:01Z` `COMMENTED` by `evezhier` (https://github.com/vllm-project/vllm/pull/36540#pullrequestreview-4038134872)

## Inline Comment Hotspots

- `vllm/model_executor/layers/attention/mla_attention.py`: 6 inline comment(s)
- `vllm/v1/attention/ops/merge_attn_states.py`: 2 inline comment(s)
- `vllm/v1/attention/ops/triton_merge_attn_states.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-31T15:10:01Z` `inline` by `evezhier` `vllm/model_executor/layers/attention/mla_attention.py`:1875; signals: attention, mla, perf; excerpt: "There is no prefill query start loc cpu, to create it I had to duplicate the operation in the MLACommonMetadataBuilder: It's awkward but it ..." (https://github.com/vllm-project/vllm/pull/36540#discussion_r3016558174)
- `2026-03-10T08:31:29Z` `inline` by `evezhier` `vllm/model_executor/layers/attention/mla_attention.py`:2396; signals: attention, mla; excerpt: "This is a precise description of why this task appeared, thanks, Gemini :) merge attn states has been modified to handle this." (https://github.com/vllm-project/vllm/pull/36540#discussion_r2910155714)
- `2026-03-24T02:16:32Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/attention/mla_attention.py`:1875; signals: attention, mla; excerpt: "we should prefer prefill query start loc cpu over the device side tensor if doing .item() to avoid D- H sync" (https://github.com/vllm-project/vllm/pull/36540#discussion_r2978601342)
- `2026-03-24T02:19:36Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/attention/mla_attention.py`:1875; signals: attention, mla; excerpt: "I think you may actually want to consider using split decodes prefills and extends instead of split decodes and prefills to achieve this" (https://github.com/vllm-project/vllm/pull/36540#discussion_r2978608494)
- `2026-03-11T20:26:55Z` `review` `COMMENTED` by `pavanimajety`; signals: perf; excerpt: "Thanks for the PR, do we see any reduced perf due to the additional logic for batches of requests with no history context?" (https://github.com/vllm-project/vllm/pull/36540#pullrequestreview-3932341428)
- `2026-03-09T20:47:33Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @evezhier, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/36540#issuecomment-4026813436)
- `2026-03-16T22:10:03Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @evezhier, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/36540#issuecomment-4070948785)
- `2026-03-11T20:23:52Z` `inline` by `pavanimajety` `vllm/v1/attention/ops/merge_attn_states.py`:46; signals: attention; excerpt: "Nit: Could we add a doc string here explaining all the arguments, including the new one? Especially that what it means when it is ..." (https://github.com/vllm-project/vllm/pull/36540#discussion_r2920810341)
- `2026-03-16T22:06:36Z` `inline` by `evezhier` `vllm/v1/attention/ops/merge_attn_states.py`:46; signals: attention; excerpt: "Done" (https://github.com/vllm-project/vllm/pull/36540#discussion_r2943221930)
- `2026-03-17T21:21:01Z` `issue` by `evezhier`; signals: general review; excerpt: "@pavanimajety I clarified in the docstring that for cases when prefill tokens with context is not set the whole batch is treated as having ..." (https://github.com/vllm-project/vllm/pull/36540#issuecomment-4078075344)
