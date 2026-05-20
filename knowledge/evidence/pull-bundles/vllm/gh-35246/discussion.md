# PR Discussion Digest

- Source PR: [vllm-project/vllm#35246](https://github.com/vllm-project/vllm/pull/35246)
- Source page: `sources/prs/vllm/PR-35246.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-35246`
- Generated at: `2026-05-20T15:39:59.978019+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-25T00:25:26Z`
- Merged: `2026-03-05T16:51:27Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 13 (approved=2, commented=11)
- Inline review comments: 12
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=2, outdated=3
- Human participants with discussion text: MatthewBonanni, SageMoore, gshtras, jennyyyyzhen, mergify, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-02-25T00:27:58Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the attention backend selection logic for the ROCm platform by centralizing priority ... (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3851204885)
- `2026-02-25T02:12:25Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3851452495)
- `2026-02-25T17:09:24Z` `COMMENTED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3855601045)
- `2026-02-26T18:39:34Z` `COMMENTED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3862899736)
- `2026-02-26T18:54:08Z` `COMMENTED` by `MatthewBonanni` (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3862965008)
- `2026-02-26T19:38:21Z` `COMMENTED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3863165022)
- `2026-02-26T19:55:55Z` `APPROVED` by `MatthewBonanni` - LGTM, would like to get a stamp from someone from AMD before merging though. Is there a selector ... (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3863251862)
- `2026-02-26T22:24:49Z` `APPROVED` by `gshtras` - Overall looks that the logic was ported correctly, while exposing a few inaccuracies that were present in the ... (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3863861755)
- `2026-02-27T14:22:12Z` `COMMENTED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3867200969)
- `2026-02-27T15:09:55Z` `COMMENTED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3867449851)
- `2026-02-27T16:43:01Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3867935246)
- `2026-02-27T17:23:04Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3868127323)
- `2026-02-27T17:24:59Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3868139104)

## Inline Comment Hotspots

- `vllm/platforms/rocm.py`: 7 inline comment(s)
- `vllm/v1/attention/backends/rocm_aiter_fa.py`: 5 inline comment(s)

## High-Signal Discussion

- `2026-02-26T18:39:34Z` `inline` by `SageMoore` `vllm/platforms/rocm.py`:379; signals: attention, block, hang, mla, triton; excerpt: "@tjtanaa @dllehr-amd @gshtras This PR shouldn't change attention backend selection at all with one minor exception. Right here we will "fall-back" the ROCM AITER ..." (https://github.com/vllm-project/vllm/pull/35246#discussion_r2860704696)
- `2026-02-27T17:24:59Z` `inline` by `tjtanaa` `vllm/platforms/rocm.py`:379; signals: block, hang, mla, triton; excerpt: "Yes. TRITON MLA does not support block size 1. I am fine with changing the behaviour to error out if user uses the combination ..." (https://github.com/vllm-project/vllm/pull/35246#discussion_r2865397338)
- `2026-02-25T02:12:25Z` `inline` by `tjtanaa` `vllm/platforms/rocm.py`:309; signals: mla, perf; excerpt: "I wonder if it is easier if we just hardcode the list of backends irregardless of whether we enable mla or aiter. Because the ..." (https://github.com/vllm-project/vllm/pull/35246#discussion_r2850445999)
- `2026-02-27T14:22:11Z` `inline` by `SageMoore` `vllm/v1/attention/backends/rocm_aiter_fa.py`:772; signals: attention, cuda; excerpt: "I see. I've updated the check to only support gfx942 and gfx950, which is what on mi3xx() does. Or are you saying that we ..." (https://github.com/vllm-project/vllm/pull/35246#discussion_r2864572989)
- `2026-02-27T15:09:54Z` `inline` by `SageMoore` `vllm/v1/attention/backends/rocm_aiter_fa.py`:772; signals: attention, cuda; excerpt: "I decided that the safest thing is to just add a on mi3xx() check to supports compute capability. This isn't great because it completely ..." (https://github.com/vllm-project/vllm/pull/35246#discussion_r2864800428)
- `2026-02-26T18:54:09Z` `inline` by `MatthewBonanni` `vllm/platforms/rocm.py`:333; signals: attention; excerpt: "Out of scope for this PR, but would it be possible to move towards deprecating envs.VLLM ROCM USE AITER UNIFIED ATTENTION and envs.VLLM ROCM ..." (https://github.com/vllm-project/vllm/pull/35246#discussion_r2860764657)
- `2026-02-26T19:38:21Z` `inline` by `SageMoore` `vllm/platforms/rocm.py`:333; signals: attention; excerpt: "Yeah, it would be great to get rid of all of these environment variables. I suspect for the attention ones we can start to ..." (https://github.com/vllm-project/vllm/pull/35246#discussion_r2860944504)
- `2026-02-26T22:24:00Z` `inline` by `gshtras` `vllm/v1/attention/backends/rocm_aiter_fa.py`:772; signals: attention; excerpt: "One small nit. While this matches the semantics of the current check, it also exposes a bug, and misses the purpose. Reason being, on ..." (https://github.com/vllm-project/vllm/pull/35246#discussion_r2861575202)
- `2026-02-27T16:43:01Z` `inline` by `gshtras` `vllm/v1/attention/backends/rocm_aiter_fa.py`:772; signals: attention; excerpt: "Just to clarify things, the reason to not use device capability on ROCm is not because it's unreliable, but because it's inherently broken through ..." (https://github.com/vllm-project/vllm/pull/35246#discussion_r2865220295)
- `2026-02-27T17:23:04Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/rocm_aiter_fa.py`:16; signals: attention; excerpt: "@SageMoore We should try to keep any import from vllm.platforms.rocm local. In this case, import in supports compute capability instead. This can help to ..." (https://github.com/vllm-project/vllm/pull/35246#discussion_r2865389068)
- `2026-02-26T19:55:55Z` `review` `APPROVED` by `MatthewBonanni`; signals: cuda; excerpt: "LGTM, would like to get a stamp from someone from AMD before merging though. Is there a selector test on the AMD side to ..." (https://github.com/vllm-project/vllm/pull/35246#pullrequestreview-3863251862)
- `2026-02-25T17:09:24Z` `inline` by `SageMoore` `vllm/platforms/rocm.py`:309; signals: general review; excerpt: "I think that it's better to start with a straight port of the existing logic and work on refining it in future PRs." (https://github.com/vllm-project/vllm/pull/35246#discussion_r2854288251)
