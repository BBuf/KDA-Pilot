# PR Discussion Digest

- Source PR: [vllm-project/vllm#26534](https://github.com/vllm-project/vllm/pull/26534)
- Source page: `sources/prs/vllm/PR-26534.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-26534`
- Generated at: `2026-05-20T15:38:08.226254+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-09T21:10:40Z`
- Merged: `2025-10-15T23:01:38Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 22 (approved=3, changes_requested=1, commented=18)
- Inline review comments: 24
- Review threads observed: 18
- Resolved/outdated thread markers: resolved=6, outdated=14
- Human participants with discussion text: ProExpertProg, adabeyta, chatgpt-codex-connector, elvischenv, mergify, pavanimajety
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-10-09T21:12:07Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the query quantization logic for the Flashinfer and Triton attention backends, moving ... (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3320658046)
- `2025-10-09T21:15:45Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3320665741)
- `2025-10-10T00:48:18Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3321022385)
- `2025-10-10T00:48:54Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3321022939)
- `2025-10-10T01:06:56Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3321050726)
- `2025-10-10T01:13:24Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3321065154)
- `2025-10-10T01:27:50Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3321092510)
- `2025-10-11T13:34:46Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3327185813)
- `2025-10-13T12:54:38Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3331525354)
- `2025-10-13T12:59:14Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3331545401)
- `2025-10-13T13:00:42Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3331550266)
- `2025-10-13T13:01:34Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3331553129)
- `2025-10-13T19:32:30Z` `COMMENTED` by `ProExpertProg` - I'm still confused why the diff doesn't show your changes from your PR (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3332697360)
- `2025-10-13T19:44:01Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3332849315)
- `2025-10-13T23:40:20Z` `COMMENTED` by `ProExpertProg` - Mostly cleanup! (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3333382458)
- `2025-10-14T02:37:52Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3333699730)
- `2025-10-14T15:41:46Z` `COMMENTED` by `ProExpertProg` - One more note about supports quant query input (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3336324737)
- `2025-10-14T17:43:57Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3336811596)
- `2025-10-14T17:49:39Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3336828337)
- `2025-10-15T17:23:24Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3341540062)
- `2025-10-15T17:25:43Z` `CHANGES_REQUESTED` by `ProExpertProg` - I see now we actually lost performance with this; we should make sure we gain and not lose ... (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3341547420)
- `2025-10-15T23:01:30Z` `APPROVED` by `ProExpertProg` - Wow, those are some insane numbers... good work! (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3342599025)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/flashinfer.py`: 11 inline comment(s)
- `vllm/attention/layer.py`: 9 inline comment(s)
- `vllm/v1/attention/backends/triton_attn.py`: 2 inline comment(s)
- `vllm/attention/backends/abstract.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-09T21:15:45Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/flashinfer.py`:914; signals: attention, bf16, cache, dtype, flashinfer, fp8, hang, kv cache; excerpt: "![P1 Badge]( Gate query quantization on q data type Setting supports quant query input = True and removing the in-backend check means FlashInfer queries ..." (https://github.com/vllm-project/vllm/pull/26534#discussion_r2417976308)
- `2025-10-10T01:06:56Z` `inline` by `pavanimajety` `vllm/v1/attention/backends/flashinfer.py`:914; signals: attention, cache, dtype, flashinfer, fp8, sm90; excerpt: "Algorithmically, it is the same as FlashAttention. When KV-Cache dtype is set to FP8, we should also use query quantization and Attention in FP8. ..." (https://github.com/vllm-project/vllm/pull/26534#discussion_r2418279686)
- `2025-10-10T00:48:17Z` `inline` by `ProExpertProg` `vllm/v1/attention/backends/flashinfer.py`:914; signals: attention, cache, flashinfer, fp8, kv cache; excerpt: "I hate to say it but this comment is correct. Note that other backends always quantize query if kv cache scale.startswith("fp8"). This one has ..." (https://github.com/vllm-project/vllm/pull/26534#discussion_r2418260528)
- `2025-10-10T01:27:50Z` `inline` by `elvischenv` `vllm/v1/attention/backends/flashinfer.py`:914; signals: attention, flashinfer, sm100; excerpt: "@ProExpertProg That's correct, agree that it needs to be a dynamic prop. Currently only trtllm attn supports query quantization, and trtllm attn only supports ..." (https://github.com/vllm-project/vllm/pull/26534#discussion_r2418304861)
- `2025-10-13T23:39:55Z` `inline` by `ProExpertProg` `vllm/v1/attention/backends/flashinfer.py`:912; signals: attention, dtype, flashinfer; excerpt: "No matter what branch we're in, we should assert that attn metadata.q data type matches query.dtype()" (https://github.com/vllm-project/vllm/pull/26534#discussion_r2427556735)
- `2025-10-10T00:48:54Z` `inline` by `ProExpertProg` `vllm/v1/attention/backends/flashinfer.py`:914; signals: attention, flashinfer, fp8; excerpt: "cc @nvpohanh is there an easy way to know when q data type will be FP8 and when it won't?" (https://github.com/vllm-project/vllm/pull/26534#discussion_r2418261023)
- `2025-10-15T17:25:43Z` `review` `CHANGES_REQUESTED` by `ProExpertProg`; signals: perf, performance; excerpt: "I see now we actually lost performance with this; we should make sure we gain and not lose performance." (https://github.com/vllm-project/vllm/pull/26534#pullrequestreview-3341547420)
- `2025-10-14T20:50:52Z` `issue` by `pavanimajety`; signals: kernel, perf, triton; excerpt: "@adabeyta Any analysis on why we are seeing lower toks/sec with enhanced fusion? Even without a custom kernel, the fact that rope + Quant ..." (https://github.com/vllm-project/vllm/pull/26534#issuecomment-3403573966)
- `2025-10-10T01:13:24Z` `inline` by `ProExpertProg` `vllm/v1/attention/backends/flashinfer.py`:914; signals: attention, flashinfer; excerpt: "when TRTLLM attention is unavailable or VLLM FLASHINFER DISABLE Q QUANTIZATION=1 What about these cases, I assume we should handle them as well? Maybe ..." (https://github.com/vllm-project/vllm/pull/26534#discussion_r2418285483)
- `2025-10-13T12:59:15Z` `inline` by `ProExpertProg` `vllm/v1/attention/backends/flashinfer.py`:354; signals: attention, flashinfer; excerpt: "Somehow we need to move this logic into the supports query quant input. We might need to make it a function on the impl ..." (https://github.com/vllm-project/vllm/pull/26534#discussion_r2426283941)
- `2025-10-13T13:00:43Z` `inline` by `ProExpertProg` `vllm/attention/layer.py`:349; signals: attention, compile; excerpt: "I don't think this will work; attention metadata is not set during the profile run when we compile. Instead, we should have a more ..." (https://github.com/vllm-project/vllm/pull/26534#discussion_r2426287399)
- `2025-10-11T13:34:37Z` `inline` by `elvischenv` `vllm/v1/attention/backends/flashinfer.py`:149; signals: attention, flashinfer; excerpt: "You may need to rebase or merge main and resolve the import issue" (https://github.com/vllm-project/vllm/pull/26534#discussion_r2422849483)
