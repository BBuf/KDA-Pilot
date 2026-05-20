# PR Discussion Digest

- Source PR: [sgl-project/sglang#8638](https://github.com/sgl-project/sglang/pull/8638)
- Source page: `sources/prs/sglang/PR-8638.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-8638`
- Generated at: `2026-05-20T15:31:25.930424+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-31T23:06:08Z`
- Merged: `2025-08-11T21:02:13Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 22 (approved=3, commented=19)
- Inline review comments: 26
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=14, outdated=11
- Human participants with discussion text: elfiegg, farazkh80, fzyzcjy, kaixih, kushanam, merrymercy, pavanimajety, zhyncs
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-07-31T23:06:38Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @farazkh80, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3077124704)
- `2025-07-31T23:07:44Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for the TRTLLM MLA attention backend, which is optimized for NVIDIA's ... (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3077125994)
- `2025-08-01T03:31:30Z` `COMMENTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3077540864)
- `2025-08-01T03:32:01Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3077541631)
- `2025-08-04T04:51:48Z` `APPROVED` by `kushanam` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3082680061)
- `2025-08-07T15:28:58Z` `COMMENTED` by `pavanimajety` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3097684164)
- `2025-08-07T15:33:09Z` `COMMENTED` by `pavanimajety` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3097708133)
- `2025-08-07T15:40:40Z` `COMMENTED` by `farazkh80` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3097739165)
- `2025-08-07T20:16:24Z` `COMMENTED` by `elfiegg` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3098601561)
- `2025-08-08T03:49:28Z` `COMMENTED` by `farazkh80` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3099371477)
- `2025-08-08T03:49:47Z` `COMMENTED` by `farazkh80` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3099371773)
- `2025-08-09T00:44:23Z` `COMMENTED` by `fzyzcjy` - LGTM, some nits (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3102353463)
- `2025-08-09T00:49:31Z` `COMMENTED` by `farazkh80` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3102357055)
- `2025-08-09T01:35:25Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3102374087)
- `2025-08-10T02:08:32Z` `COMMENTED` by `farazkh80` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3103441311)
- `2025-08-10T02:08:39Z` `COMMENTED` by `farazkh80` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3103441326)
- `2025-08-10T02:08:45Z` `COMMENTED` by `farazkh80` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3103441335)
- `2025-08-10T02:08:50Z` `COMMENTED` by `farazkh80` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3103441342)
- `2025-08-10T03:24:32Z` `COMMENTED` by `farazkh80` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3103451616)
- `2025-08-11T11:37:05Z` `APPROVED` by `fzyzcjy` - LGTM, only two nits (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3105422707)
- `2025-08-11T15:39:44Z` `COMMENTED` by `farazkh80` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3106466865)
- `2025-08-11T15:53:43Z` `COMMENTED` by `farazkh80` (https://github.com/sgl-project/sglang/pull/8638#pullrequestreview-3106541795)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/trtllm_mla_backend.py`: 10 inline comment(s)
- `python/sglang/srt/models/deepseek_v2.py`: 6 inline comment(s)
- `python/sglang/srt/server_args.py`: 5 inline comment(s)
- `python/sglang/test/attention/test_trtllm_mla_backend.py`: 3 inline comment(s)
- `docs/backend/attention_backend.md`: 1 inline comment(s)
- `python/pyproject.toml`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-07T20:06:15Z` `issue` by `elfiegg`; signals: attention, blackwell, cache, cuda, fp8, kernel, kv cache, mla; excerpt: "@fzyzcjy – I agree with your intuition. The caveat is that our performance analysis currently shows MLA prefill accounts for only about 5% of ..." (https://github.com/sgl-project/sglang/pull/8638#issuecomment-3165560173)
- `2025-08-08T04:08:14Z` `issue` by `farazkh80`; signals: accuracy, benchmark, flashinfer, fp8, mla, oom, throughput; excerpt: "This PR is ready for review @fzyzcjy @merrymercy Ran latest benchmarking and hightlights include - With TRTLLM MLA fp8 We can get up to ..." (https://github.com/sgl-project/sglang/pull/8638#issuecomment-3166497674)
- `2025-08-07T15:40:40Z` `inline` by `farazkh80` `python/sglang/test/attention/test_trtllm_mla_backend.py`:73; signals: accuracy, attention, bf16, failing, flashinfer, mla; excerpt: "they are currently failing when comparing accuracy against flashinfer MLA that happens in BF16, I need to fix them." (https://github.com/sgl-project/sglang/pull/8638#discussion_r2260720325)
- `2025-08-11T15:39:44Z` `inline` by `farazkh80` `python/sglang/srt/server_args.py`:444; signals: bf16, cache, dtype, fp8, kernel, mla; excerpt: "I removed the fp16/bf16 since it is not supported in the server args for kv-cache-dtype anyways. Valid options are fp8 e4m3 for fp8 path ..." (https://github.com/sgl-project/sglang/pull/8638#discussion_r2267165675)
- `2025-08-09T00:49:30Z` `inline` by `farazkh80` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:416; signals: accuracy, attention, fp8, mla; excerpt: "yes only used when in fp16. But since fp8 is faster and no accuracy degradation, fp8 should be default if possible" (https://github.com/sgl-project/sglang/pull/8638#discussion_r2264167605)
- `2025-08-06T23:22:16Z` `issue` by `fzyzcjy`; signals: bf16, cache, fp8, kv cache; excerpt: "@elfiegg No, but from my naive understanding, fp8 computation may be faster than bf16 since we have more theoretical flops, and it would be ..." (https://github.com/sgl-project/sglang/pull/8638#issuecomment-3161900897)
- `2025-08-07T21:01:08Z` `issue` by `elfiegg`; signals: attention, flashinfer, kernel, mla; excerpt: "@fzyzcjy as we speak we have received strong signal to optimize flashinfer::mla::BatchMLAPagedAttentionKernel. will update you in" (https://github.com/sgl-project/sglang/pull/8638#issuecomment-3165690774)
- `2025-08-07T15:28:57Z` `inline` by `pavanimajety` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:307; signals: attention, dtype, mla; excerpt: "small suggestion: add the expected dtype for each of query and k inputs and the expected outputs for clarity" (https://github.com/sgl-project/sglang/pull/8638#discussion_r2260684984)
- `2025-08-09T00:43:47Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:416; signals: attention, fp8, mla; excerpt: "btw I see this branch is not used when in fp8, thus agree the cat may not be of high priority to be optimized ..." (https://github.com/sgl-project/sglang/pull/8638#discussion_r2264165753)
- `2025-08-07T15:33:09Z` `inline` by `pavanimajety` `python/sglang/test/attention/test_trtllm_mla_backend.py`:73; signals: attention, fp8, mla; excerpt: "Do we need to uncomment these for fp8 tests?" (https://github.com/sgl-project/sglang/pull/8638#discussion_r2260699991)
- `2025-08-07T20:16:24Z` `inline` by `elfiegg` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:378; signals: attention, mla; excerpt: "do me a favor to throw something meaningful after this assertion? e.g. what's wrong / alternative solution?" (https://github.com/sgl-project/sglang/pull/8638#discussion_r2261313108)
- `2025-08-10T03:24:31Z` `inline` by `farazkh80` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:405; signals: attention, mla; excerpt: "I actually remove the assert since I realized in forward absorb core in deepseek v2.py I use the same attention call where v is ..." (https://github.com/sgl-project/sglang/pull/8638#discussion_r2265096675)
