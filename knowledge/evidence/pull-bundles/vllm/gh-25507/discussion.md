# PR Discussion Digest

- Source PR: [vllm-project/vllm#25507](https://github.com/vllm-project/vllm/pull/25507)
- Source page: `sources/prs/vllm/PR-25507.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-25507`
- Generated at: `2026-05-20T15:37:56.210231+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-23T19:33:00Z`
- Merged: `2025-10-06T22:49:24Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 15
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=5, outdated=6
- Human participants with discussion text: ProExpertProg, gshtras, mergify
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-23T19:35:07Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the ROCm attention backend selection by splitting the AITER unified attention into ... (https://github.com/vllm-project/vllm/pull/25507#pullrequestreview-3259351023)
- `2025-09-23T21:04:06Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/25507#pullrequestreview-3259583488)
- `2025-09-26T11:59:23Z` `COMMENTED` by `ProExpertProg` - Just a few comments on attention+fusion test, looks good otherwise (https://github.com/vllm-project/vllm/pull/25507#pullrequestreview-3271817885)
- `2025-09-26T15:22:08Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/25507#pullrequestreview-3272733269)
- `2025-09-26T15:28:01Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/25507#pullrequestreview-3272753252)
- `2025-10-06T18:58:36Z` `COMMENTED` by `ProExpertProg` - Just a few nits and a qq about FI (https://github.com/vllm-project/vllm/pull/25507#pullrequestreview-3306621127)
- `2025-10-06T18:59:50Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/25507#pullrequestreview-3306674102)
- `2025-10-06T20:40:55Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/25507#pullrequestreview-3307229101)
- `2025-10-06T20:56:32Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/25507#pullrequestreview-3307323052)
- `2025-10-06T20:57:32Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/25507#pullrequestreview-3307327672)
- `2025-10-06T21:20:59Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/25507#pullrequestreview-3307457891)

## Inline Comment Hotspots

- `tests/compile/test_fusion_attn.py`: 11 inline comment(s)
- `vllm/v1/attention/backends/rocm_attn.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-09-26T15:22:08Z` `inline` by `gshtras` `tests/compile/test_fusion_attn.py`:122; signals: cache, compile, kernel, triton; excerpt: "Permute didn't sit well with the new triton reshape and cache kernel in the triton backend" (https://github.com/vllm-project/vllm/pull/25507#discussion_r2382738135)
- `2025-10-06T18:53:02Z` `inline` by `ProExpertProg` `tests/compile/test_fusion_attn.py`:136; signals: cache, compile, flashinfer; excerpt: "This looks like the original kvcache (lines 239-248) but without the permute following it. Did you test this with FlashInfer?" (https://github.com/vllm-project/vllm/pull/25507#discussion_r2407982464)
- `2025-09-26T15:28:01Z` `inline` by `gshtras` `tests/compile/test_fusion_attn.py`:262; signals: cache, compile, hang; excerpt: "Until the clear cache change gets merged it can't be used here" (https://github.com/vllm-project/vllm/pull/25507#discussion_r2382751984)
- `2025-10-06T18:59:50Z` `inline` by `ProExpertProg` `tests/compile/test_fusion_attn.py`:136; signals: blackwell, block, compile; excerpt: "(I unblocked the Blackwell test to check FI fusion)" (https://github.com/vllm-project/vllm/pull/25507#discussion_r2408015079)
- `2025-09-23T21:04:06Z` `inline` by `gshtras` `vllm/v1/attention/backends/rocm_attn.py`:295; signals: attention, hang; excerpt: "Nothing changed here" (https://github.com/vllm-project/vllm/pull/25507#discussion_r2373447911)
- `2025-10-06T18:56:46Z` `inline` by `ProExpertProg` `vllm/v1/attention/backends/rocm_attn.py`:343; signals: attention, cuda; excerpt: "Why is there a CUDA check inside a ROCm backend?" (https://github.com/vllm-project/vllm/pull/25507#discussion_r2407999953)
- `2025-10-06T20:40:55Z` `inline` by `ProExpertProg` `tests/compile/test_fusion_attn.py`:136; signals: compile, failing; excerpt: "The test is failing in CI so I think this is incorrect" (https://github.com/vllm-project/vllm/pull/25507#discussion_r2408461434)
- `2025-09-26T11:59:23Z` `review` `COMMENTED` by `ProExpertProg`; signals: attention; excerpt: "Just a few comments on attention+fusion test, looks good otherwise" (https://github.com/vllm-project/vllm/pull/25507#pullrequestreview-3271817885)
- `2025-09-26T11:35:50Z` `inline` by `ProExpertProg` `tests/compile/test_fusion_attn.py`:101; signals: compile; excerpt: "We only test one of these options per-backend, can we just check the backend here (self.attn.backend) to decide which one we're doing, instead of ..." (https://github.com/vllm-project/vllm/pull/25507#discussion_r2382107477)
- `2025-09-26T11:35:37Z` `inline` by `ProExpertProg` `tests/compile/test_fusion_attn.py`:122; signals: compile; excerpt: "This is the same as before but without the permute" (https://github.com/vllm-project/vllm/pull/25507#discussion_r2382106789)
- `2025-09-26T11:37:05Z` `inline` by `ProExpertProg` `tests/compile/test_fusion_attn.py`:262; signals: compile; excerpt: "See 24604: we should fix global force attn backend context manager instead of monkeypatching" (https://github.com/vllm-project/vllm/pull/25507#discussion_r2382111184)
- `2025-10-06T20:56:32Z` `inline` by `gshtras` `vllm/v1/attention/backends/rocm_attn.py`:343; signals: attention; excerpt: "Missed copy paste issue from the previous PR I guess, but good catch, it's worth a cleanup" (https://github.com/vllm-project/vllm/pull/25507#discussion_r2408532062)
