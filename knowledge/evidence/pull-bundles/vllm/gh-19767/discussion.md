# PR Discussion Digest

- Source PR: [vllm-project/vllm#19767](https://github.com/vllm-project/vllm/pull/19767)
- Source page: `sources/prs/vllm/PR-19767.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-19767`
- Generated at: `2026-05-20T15:35:33.390844+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-17T20:17:16Z`
- Merged: `2025-09-10T20:59:55Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 28 (approved=1, commented=27)
- Inline review comments: 51
- Review threads observed: 28
- Resolved/outdated thread markers: resolved=21, outdated=23
- Human participants with discussion text: ProExpertProg, gshtras, mergify
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-17T20:17:42Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @gshtras, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-2936981965)
- `2025-06-17T20:18:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces FP8 output fusion for V1 attention backends, which is a valuable feature ... (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-2936984169)
- `2025-06-18T14:45:50Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-2939553092)
- `2025-06-30T18:40:53Z` `COMMENTED` by `ProExpertProg` - I don't think non-LLM tests (with custom TestModels) need to use the check function, this is only for ... (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-2972162509)
- `2025-06-30T21:46:46Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-2972844298)
- `2025-06-30T21:56:59Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-2972858791)
- `2025-06-30T22:43:00Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-2972973510)
- `2025-06-30T22:43:08Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-2972973758)
- `2025-06-30T23:24:38Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-2973055067)
- `2025-06-30T23:25:50Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-2973056343)
- `2025-07-09T18:55:08Z` `COMMENTED` by `ProExpertProg` - There were a few comments still unaddressed from last time, let me know once those are all addressed ... (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3002710395)
- `2025-07-10T04:38:16Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3003866818)
- `2025-07-10T04:39:41Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3003868894)
- `2025-07-10T20:49:23Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3007315424)
- `2025-07-10T20:49:47Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3007317678)
- `2025-07-14T09:56:24Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3015628599)
- `2025-07-14T10:16:44Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3015715199)
- `2025-07-14T13:59:05Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3016497810)
- `2025-09-04T23:26:08Z` `COMMENTED` by `ProExpertProg` - A couple of minor notes! Glad we don't have to do the complicated model loading anymore & great ... (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3187509632)
- `2025-09-05T14:30:50Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3189617067)
- `2025-09-05T14:31:17Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3189619194)
- `2025-09-05T14:34:07Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3189630652)
- `2025-09-05T20:41:41Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3190738290)
- `2025-09-05T20:51:37Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/19767#pullrequestreview-3190759618)
- ... 4 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tests/compile/test_fusion_attn.py`: 25 inline comment(s)
- `vllm/compilation/fusion_attn.py`: 8 inline comment(s)
- `vllm/attention/ops/chunked_prefill_paged_decode.py`: 5 inline comment(s)
- `tests/compile/test_async_tp.py`: 4 inline comment(s)
- `vllm/attention/ops/triton_unified_attention.py`: 3 inline comment(s)
- `vllm/v1/attention/backends/triton_attn.py`: 2 inline comment(s)
- `vllm/attention/ops/prefix_prefill.py`: 2 inline comment(s)
- `tests/compile/backend.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-05T14:30:50Z` `inline` by `gshtras` `tests/compile/test_fusion_attn.py`:182; signals: cache, compile, cuda, kernel; excerpt: "Using on-cpu tensors in the reshape and cache kernel causes a crash. In production the default device is set to CUDA before the tensors ..." (https://github.com/vllm-project/vllm/pull/19767#discussion_r2325265362)
- `2025-06-30T18:06:08Z` `inline` by `ProExpertProg` `tests/compile/test_fusion_attn.py`:194; signals: compile, hang, register; excerpt: "It's currently not clear that this registers the custom pass into current vllm config, could you change it so that it is?" (https://github.com/vllm-project/vllm/pull/19767#discussion_r2175625031)
- `2025-07-14T13:59:05Z` `inline` by `gshtras` `tests/compile/test_fusion_attn.py`:26; signals: compile, memory, oom; excerpt: "Did you figure out the OOM issue? Not really. At least on ROCm currently no manual deletion seems to free the memory" (https://github.com/vllm-project/vllm/pull/19767#discussion_r2205021517)
- `2025-09-05T14:34:06Z` `inline` by `gshtras` `tests/compile/test_fusion_attn.py`:325; signals: compile, cuda, hang; excerpt: "I considered this approach, but this implies that if it is not cuda, it's automatically rocm without clarification, which may not always remain true. ..." (https://github.com/vllm-project/vllm/pull/19767#discussion_r2325274074)
- `2025-09-05T21:22:00Z` `inline` by `ProExpertProg` `tests/compile/test_fusion_attn.py`:338; signals: attention, compile, triton; excerpt: "I see, this actually dispatches to the triton backend. We should cleanup the attention backend selection logic on rocm" (https://github.com/vllm-project/vllm/pull/19767#discussion_r2326072995)
- `2025-09-05T21:25:44Z` `inline` by `ProExpertProg` `tests/compile/test_fusion_attn.py`:338; signals: compile, cuda, triton; excerpt: "Also, I just remembered: we could test the Triton backend on CUDA as well, it would run in CI automatically which would be nice. ..." (https://github.com/vllm-project/vllm/pull/19767#discussion_r2326079879)
- `2025-06-30T17:56:42Z` `inline` by `ProExpertProg` `vllm/attention/ops/triton_unified_attention.py`:250; signals: attention, kernel, triton; excerpt: "Should we invert the scale outside the kernel?" (https://github.com/vllm-project/vllm/pull/19767#discussion_r2175611617)
- `2025-06-30T22:43:00Z` `inline` by `gshtras` `tests/compile/test_fusion_attn.py`:143; signals: compile, oom; excerpt: "Running multiple test parallelizations in a row often causes OOM if the test creates an LLM object, something is not getting cleaned up properly ..." (https://github.com/vllm-project/vllm/pull/19767#discussion_r2176094196)
- `2025-07-09T18:48:13Z` `inline` by `ProExpertProg` `tests/compile/test_async_tp.py`:161; signals: compile, hang; excerpt: "No need to change these, check function only necessary when the checks must happen during compilation" (https://github.com/vllm-project/vllm/pull/19767#discussion_r2195749848)
- `2025-07-10T04:39:41Z` `inline` by `gshtras` `vllm/attention/ops/chunked_prefill_paged_decode.py`:39; signals: attention, kernel; excerpt: "Arguably this name is now more correct after the inversion since now we're multiplying by it inside the kernel" (https://github.com/vllm-project/vllm/pull/19767#discussion_r2196531478)
- `2025-09-04T23:06:33Z` `inline` by `ProExpertProg` `vllm/compilation/fusion_attn.py`:50; signals: cuda, dtype; excerpt: "Apply below: ``` self.dtype = dtype assert self.quant key in QUANT OPS, \ f"unsupported quantization scheme {self.quant key}" self.QUANT OP = QUANT OPS[self.quant key] ..." (https://github.com/vllm-project/vllm/pull/19767#discussion_r2323722576)
- `2025-09-04T23:21:32Z` `inline` by `ProExpertProg` `tests/compile/test_fusion_attn.py`:182; signals: blackwell, compile; excerpt: "Why is this necessary? Where would ROCm actually do this? Because I think it might break the Blackwell FI?" (https://github.com/vllm-project/vllm/pull/19767#discussion_r2323736992)
