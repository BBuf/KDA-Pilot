# PR Discussion Digest

- Source PR: [vllm-project/vllm#16780](https://github.com/vllm-project/vllm/pull/16780)
- Source page: `sources/prs/vllm/PR-16780.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16780`
- Generated at: `2026-05-20T15:35:02.443478+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-17T10:45:38Z`
- Merged: `2025-05-07T06:07:23Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: DarkLight1337, Isotr0py, SzymonOzog, mergify, zhaotyer
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-20T17:11:41Z` `APPROVED` by `Isotr0py` - Sorry for the delay. This looks reasonable to me once we updated the GGUF kernel tests to cover ... (https://github.com/vllm-project/vllm/pull/16780#pullrequestreview-2780293814)
- `2025-04-23T16:03:50Z` `COMMENTED` by `SzymonOzog` (https://github.com/vllm-project/vllm/pull/16780#pullrequestreview-2787889161)

## Inline Comment Hotspots

- `csrc/quantization/gguf/gguf_kernel.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-25T04:52:22Z` `issue` by `SzymonOzog`; signals: compile, failing, kernel, register; excerpt: "@DarkLight1337 So the test seems to use precompiled nightly wheen where the kernel from this PR is not yet present that's why @register fake ..." (https://github.com/vllm-project/vllm/pull/16780#issuecomment-2829369095)
- `2025-04-23T03:05:41Z` `issue` by `zhaotyer`; signals: benchmark, kernel, triton; excerpt: "@zhaotyer Could you try with --enable-chunked-prefill --max-num-batched-tokens 512 I think I know what's causing the issue, it's also present on main, we would need ..." (https://github.com/vllm-project/vllm/pull/16780#issuecomment-2822942112)
- `2025-04-20T17:09:51Z` `inline` by `Isotr0py` `csrc/quantization/gguf/gguf_kernel.cu`:384; signals: kernel, moe; excerpt: "Can we also update the GGUF kernel tests to cover I-Quants with MoeVec kernel?" (https://github.com/vllm-project/vllm/pull/16780#discussion_r2051769817)
- `2025-04-20T17:11:41Z` `review` `APPROVED` by `Isotr0py`; signals: kernel, moe; excerpt: "Sorry for the delay. This looks reasonable to me once we updated the GGUF kernel tests to cover the MoeVec kernel!" (https://github.com/vllm-project/vllm/pull/16780#pullrequestreview-2780293814)
- `2025-04-22T11:22:08Z` `issue` by `zhaotyer`; signals: kernel, moe; excerpt: "When we don't have a high expert utilisation this kernel will work much faster than matmul style moe kernel. Also adds better support for ..." (https://github.com/vllm-project/vllm/pull/16780#issuecomment-2821010338)
- `2025-04-22T13:08:16Z` `issue` by `SzymonOzog`; signals: kernel, triton; excerpt: "@zhaotyer Could you try with --enable-chunked-prefill --max-num-batched-tokens 512 I think I know what's causing the issue, it's also present on main, we would need ..." (https://github.com/vllm-project/vllm/pull/16780#issuecomment-2821278553)
- `2025-04-23T16:03:50Z` `inline` by `SzymonOzog` `csrc/quantization/gguf/gguf_kernel.cu`:384; signals: kernel; excerpt: "Good idea. Updated with I-Quants" (https://github.com/vllm-project/vllm/pull/16780#discussion_r2056396281)
- `2025-04-24T17:47:30Z` `issue` by `DarkLight1337`; signals: failing; excerpt: "PTAL at the failing installation test. It seems related to this PR" (https://github.com/vllm-project/vllm/pull/16780#issuecomment-2828393719)
- `2025-04-23T15:33:56Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @SzymonOzog." (https://github.com/vllm-project/vllm/pull/16780#issuecomment-2824710113)
