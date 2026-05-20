# PR Discussion Digest

- Source PR: [vllm-project/vllm#16032](https://github.com/vllm-project/vllm/pull/16032)
- Source page: `sources/prs/vllm/PR-16032.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16032`
- Generated at: `2026-05-20T15:34:48.679474+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-03T19:38:20Z`
- Merged: `2025-04-27T13:29:22Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 13
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=3, outdated=7
- Human participants with discussion text: LucasWilkinson, kaixih
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-25T18:33:09Z` `COMMENTED` by `LucasWilkinson` - Overall looks pretty good, left a couple nits (https://github.com/vllm-project/vllm/pull/16032#pullrequestreview-2794953253)
- `2025-04-25T22:40:35Z` `APPROVED` by `LucasWilkinson` - Thanks for the updates, left a few more nits (they can be punted to a future PR if ... (https://github.com/vllm-project/vllm/pull/16032#pullrequestreview-2795432002)
- `2025-04-26T09:27:20Z` `COMMENTED` by `kaixih` (https://github.com/vllm-project/vllm/pull/16032#pullrequestreview-2795861373)
- `2025-04-26T09:27:28Z` `COMMENTED` by `kaixih` (https://github.com/vllm-project/vllm/pull/16032#pullrequestreview-2795861395)
- `2025-04-26T09:27:34Z` `COMMENTED` by `kaixih` (https://github.com/vllm-project/vllm/pull/16032#pullrequestreview-2795861408)
- `2025-04-26T09:29:05Z` `COMMENTED` by `kaixih` (https://github.com/vllm-project/vllm/pull/16032#pullrequestreview-2795861640)
- `2025-04-26T20:37:23Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/16032#pullrequestreview-2796425737)
- `2025-04-26T23:21:43Z` `COMMENTED` by `kaixih` (https://github.com/vllm-project/vllm/pull/16032#pullrequestreview-2796649570)

## Inline Comment Hotspots

- `csrc/attention/mla/cutlass_mla_kernels.cu`: 10 inline comment(s)
- `vllm/_custom_ops.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-04-25T18:29:00Z` `inline` by `LucasWilkinson` `vllm/_custom_ops.py`:1475; signals: attention, block, cuda, perf; excerpt: "nit: I think alot of these assets/checks are better moved into the C++, that way they are performed even if the someone calls the ..." (https://github.com/vllm-project/vllm/pull/16032#discussion_r2060707489)
- `2025-04-25T22:39:25Z` `inline` by `LucasWilkinson` `csrc/attention/mla/cutlass_mla_kernels.cu`:121; signals: attention, cutlass, kernel, mla; excerpt: "nit: maybe for a future PR, if Q ptr (q nope) and Q ptr + D latent (q pe) as seperate tensor (assuming the ..." (https://github.com/vllm-project/vllm/pull/16032#discussion_r2060969946)
- `2025-04-26T09:29:05Z` `inline` by `kaixih` `csrc/attention/mla/cutlass_mla_kernels.cu`:121; signals: attention, cutlass, kernel, mla; excerpt: "Right, currently we follow the cutlass example, which only supports the single query tensor. If needed or this is a common practice, we can ..." (https://github.com/vllm-project/vllm/pull/16032#discussion_r2061241224)
- `2025-04-25T18:27:22Z` `inline` by `LucasWilkinson` `csrc/attention/mla/cutlass_mla_kernels.cu`:117; signals: attention, cutlass, kernel, mla; excerpt: "nit: why 0 + ... everywhere?" (https://github.com/vllm-project/vllm/pull/16032#discussion_r2060705125)
- `2025-04-25T18:30:13Z` `inline` by `LucasWilkinson` `csrc/attention/mla/cutlass_mla_kernels.cu`:30; signals: attention, cutlass, kernel, mla; excerpt: "nit: we can get this from csrc/cutlass extensions/common.hpp" (https://github.com/vllm-project/vllm/pull/16032#discussion_r2060708781)
- `2025-04-25T22:33:15Z` `inline` by `LucasWilkinson` `csrc/attention/mla/cutlass_mla_kernels.cu`:38; signals: attention, cutlass, kernel, mla; excerpt: "nit: is this wrapper required? can we just do:" (https://github.com/vllm-project/vllm/pull/16032#discussion_r2060966265)
- `2025-04-25T22:34:25Z` `inline` by `LucasWilkinson` `csrc/attention/mla/cutlass_mla_kernels.cu`:96; signals: attention, cutlass, kernel, mla; excerpt: "nit: we should pass in the scale (from Python) to avoid having to har code D non latent" (https://github.com/vllm-project/vllm/pull/16032#discussion_r2060966948)
- `2025-04-26T09:27:20Z` `inline` by `kaixih` `csrc/attention/mla/cutlass_mla_kernels.cu`:38; signals: attention, cutlass, kernel, mla; excerpt: "Done." (https://github.com/vllm-project/vllm/pull/16032#discussion_r2061241000)
- `2025-04-26T09:27:34Z` `inline` by `kaixih` `csrc/attention/mla/cutlass_mla_kernels.cu`:96; signals: attention, cutlass, kernel, mla; excerpt: "Done." (https://github.com/vllm-project/vllm/pull/16032#discussion_r2061241039)
- `2025-04-26T20:37:23Z` `inline` by `LucasWilkinson` `csrc/attention/mla/cutlass_mla_kernels.cu`:121; signals: attention, cutlass, kernel, mla; excerpt: "im confused, it appears to support multiple: am I missing something here?" (https://github.com/vllm-project/vllm/pull/16032#discussion_r2061603794)
- `2025-04-26T23:21:43Z` `inline` by `kaixih` `csrc/attention/mla/cutlass_mla_kernels.cu`:121; signals: attention, cutlass, kernel, mla; excerpt: "Tried the separate tensors and it works. Updated the PR. PTAL." (https://github.com/vllm-project/vllm/pull/16032#discussion_r2061809853)
- `2025-04-25T22:33:23Z` `inline` by `LucasWilkinson` `vllm/_custom_ops.py`:1536; signals: tma; excerpt: "nit: this probably shouldn't be hard coded to 512, we should pass in latent size, also we should pass in the softmax scale so ..." (https://github.com/vllm-project/vllm/pull/16032#discussion_r2060966335)
