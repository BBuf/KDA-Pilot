# PR Discussion Digest

- Source PR: [vllm-project/vllm#14967](https://github.com/vllm-project/vllm/pull/14967)
- Source page: `sources/prs/vllm/PR-14967.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14967`
- Generated at: `2026-05-20T15:34:33.201781+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-17T15:15:42Z`
- Merged: `2025-03-26T08:30:30Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 12 (approved=2, changes_requested=1, commented=9)
- Inline review comments: 15
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=1, outdated=5
- Human participants with discussion text: DarkLight1337, SageMoore, hongxiayang, mergify, tjtanaa, vllmellm
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-18T14:32:56Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/14967#pullrequestreview-2694826082)
- `2025-03-18T16:21:00Z` `CHANGES_REQUESTED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/14967#pullrequestreview-2695168955)
- `2025-03-18T23:01:44Z` `COMMENTED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/14967#pullrequestreview-2696058963)
- `2025-03-19T03:58:17Z` `COMMENTED` by `vllmellm` (https://github.com/vllm-project/vllm/pull/14967#pullrequestreview-2696834193)
- `2025-03-19T04:03:29Z` `COMMENTED` by `vllmellm` (https://github.com/vllm-project/vllm/pull/14967#pullrequestreview-2696838923)
- `2025-03-19T09:05:14Z` `COMMENTED` by `vllmellm` (https://github.com/vllm-project/vllm/pull/14967#pullrequestreview-2697542499)
- `2025-03-19T09:08:54Z` `COMMENTED` by `vllmellm` (https://github.com/vllm-project/vllm/pull/14967#pullrequestreview-2697562439)
- `2025-03-19T09:14:23Z` `COMMENTED` by `vllmellm` (https://github.com/vllm-project/vllm/pull/14967#pullrequestreview-2697580712)
- `2025-03-19T15:23:16Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/14967#pullrequestreview-2698959349)
- `2025-03-19T15:34:42Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/14967#pullrequestreview-2699010780)
- `2025-03-24T17:31:42Z` `APPROVED` by `SageMoore` - This looks reasonable to me. Thanks for cleaning up the tests and running lm eval. (https://github.com/vllm-project/vllm/pull/14967#pullrequestreview-2711186777)
- `2025-03-26T08:30:23Z` `APPROVED` by `DarkLight1337` - Stamp (https://github.com/vllm-project/vllm/pull/14967#pullrequestreview-2716270590)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`: 4 inline comment(s)
- `vllm/envs.py`: 3 inline comment(s)
- `tests/kernels/test_moe.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/fp8.py`: 2 inline comment(s)
- `tests/models/decoder_only/language/test_mistral.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-19T09:14:23Z` `inline` by `vllmellm` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1283; signals: kernel, moe, perf, performance; excerpt: "@SageMoore our team has decided to not check for aiter installation and add a fallback for the reasons below: 1. having a fallback makes ..." (https://github.com/vllm-project/vllm/pull/14967#discussion_r2002839317)
- `2025-03-19T17:04:45Z` `issue` by `SageMoore`; signals: accuracy, kernel, perf, performance; excerpt: "I have two high level requests for this PR. The first is that we remove AITER enablement in any unit test that does not ..." (https://github.com/vllm-project/vllm/pull/14967#issuecomment-2737418872)
- `2025-03-18T16:03:44Z` `inline` by `SageMoore` `tests/kernels/test_moe.py`:215; signals: hang, kernel, moe; excerpt: "I actually like @DarkLight1337's feedback on 14959 to use pytest custom markers, instead of an environment variable, to selectively enable/disable these tests. I assume ..." (https://github.com/vllm-project/vllm/pull/14967#discussion_r2001405896)
- `2025-03-19T15:23:15Z` `inline` by `tjtanaa` `tests/kernels/test_moe.py`:215; signals: hang, kernel, moe; excerpt: "We have tried to introduce the pytest.marker for use rocm aiter, in a minimal way. Without changing the buildkite command: e.g. pytest -v -s ..." (https://github.com/vllm-project/vllm/pull/14967#discussion_r2003621235)
- `2025-03-18T15:56:10Z` `inline` by `SageMoore` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:2; signals: moe, tma; excerpt: "Thanks for factoring this out! It really cleans up the fused moe.py file. How do you feel about putting the softmax function in here ..." (https://github.com/vllm-project/vllm/pull/14967#discussion_r2001390341)
- `2025-03-18T20:13:48Z` `inline` by `SageMoore` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:38; signals: kernel, moe; excerpt: "I put an assert False here and ran the various tests that are included in this PR. test mistral.py doesn't look like it exercises ..." (https://github.com/vllm-project/vllm/pull/14967#discussion_r2001914470)
- `2025-03-19T03:58:17Z` `inline` by `vllmellm` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:38; signals: kernel, moe; excerpt: "@SageMoore the error is due to transformer version have to install version 4.46 lower versions. test mistral.py is not an MoE model thus it ..." (https://github.com/vllm-project/vllm/pull/14967#discussion_r2002369128)
- `2025-03-19T09:08:54Z` `inline` by `vllmellm` `vllm/model_executor/layers/quantization/fp8.py`:564; signals: fp8, moe; excerpt: "@SageMoore have been addressed in [this commit]( although that it didn't really help out in clearing process weights after loading nested if/else logics. I ..." (https://github.com/vllm-project/vllm/pull/14967#discussion_r2002829558)
- `2025-03-19T15:34:42Z` `inline` by `tjtanaa` `tests/kernels/test_moe.py`:215; signals: kernel, moe; excerpt: "@SageMoore @DarkLight1337 Since we have been ensuring the unit tests passing on a particular AITER commit, we will enable the AITER kernel tests by ..." (https://github.com/vllm-project/vllm/pull/14967#discussion_r2003648386)
- `2025-03-18T15:54:38Z` `inline` by `SageMoore` `vllm/envs.py`:547; signals: kernel; excerpt: "I agree that the cascading logic is a bit much for the vllm.envs, but I don't think that the platforms class is really the ..." (https://github.com/vllm-project/vllm/pull/14967#discussion_r2001387090)
- `2025-03-18T15:59:56Z` `inline` by `SageMoore` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1283; signals: moe; excerpt: "I said this on my 14959 review, but I'll paste it here as well. Let me know what you think Given that AITER isn't ..." (https://github.com/vllm-project/vllm/pull/14967#discussion_r2001398627)
- `2025-03-18T16:09:36Z` `inline` by `SageMoore` `vllm/model_executor/layers/quantization/fp8.py`:564; signals: fp8; excerpt: "Let's move these AITER specific sections to their own functions." (https://github.com/vllm-project/vllm/pull/14967#discussion_r2001418814)
