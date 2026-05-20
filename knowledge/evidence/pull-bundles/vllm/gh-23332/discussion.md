# PR Discussion Digest

- Source PR: [vllm-project/vllm#23332](https://github.com/vllm-project/vllm/pull/23332)
- Source page: `sources/prs/vllm/PR-23332.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23332`
- Generated at: `2026-05-20T15:37:31.582968+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-21T10:08:46Z`
- Merged: `2025-09-04T09:46:37Z`

## Discussion Counts

- Issue comments: 26
- Review submissions: 17 (approved=3, changes_requested=1, commented=13)
- Inline review comments: 17
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=5, outdated=6
- Human participants with discussion text: LucasWilkinson, ProExpertProg, Yikun, jgong5, whx-sjtu, youkaichao
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-21T10:20:03Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the Multi-Head Latent Attention (MLA) into a CustomOp to improve extensibility for ... (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3140022790)
- `2025-08-21T10:34:35Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the Multi-Head Latent Attention (MLA) implementation into a CustomOp to better support ... (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3140064690)
- `2025-08-21T10:36:50Z` `COMMENTED` by `whx-sjtu` (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3140070558)
- `2025-08-21T17:18:59Z` `CHANGES_REQUESTED` by `ProExpertProg` - I'm not sure if this is the best approach. The CustomOp abstraction is meant as a simple abstraction ... (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3141646251)
- `2025-08-24T05:50:09Z` `COMMENTED` by `LucasWilkinson` - I am not up to date on the intentions behind CustomOp or the HW plugins; so I will ... (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3141523380)
- `2025-08-25T01:41:42Z` `COMMENTED` by `whx-sjtu` (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3149629801)
- `2025-08-26T02:03:02Z` `COMMENTED` by `Yikun` - @ProExpertProg @LucasWilkinson Thanks for your comments, looks like that we have reached a preliminary consensus. - In short ... (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3147020816)
- `2025-08-26T02:57:07Z` `COMMENTED` by `whx-sjtu` (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3153681067)
- `2025-08-26T09:53:34Z` `COMMENTED` by `Yikun` (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3154881988)
- `2025-08-26T10:07:00Z` `COMMENTED` by `whx-sjtu` (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3154927090)
- `2025-08-26T21:12:52Z` `APPROVED` by `ProExpertProg` - Good with me once @LucasWilkinson approves the MLA piece (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3157324890)
- `2025-08-27T01:33:53Z` `COMMENTED` by `whx-sjtu` (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3157948538)
- `2025-08-28T18:26:44Z` `APPROVED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3166056637)
- `2025-08-29T09:21:47Z` `COMMENTED` by `youkaichao` (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3168027743)
- `2025-08-29T09:24:19Z` `APPROVED` by `youkaichao` - the idea looks good to me. we can use this to unblock hardware optimizations. but please make sure ... (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3168038163)
- `2025-08-29T09:44:25Z` `COMMENTED` by `Yikun` (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3168098405)
- `2025-08-29T13:25:15Z` `COMMENTED` by `whx-sjtu` (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3168731803)

## Inline Comment Hotspots

- `vllm/model_executor/layers/mla.py`: 13 inline comment(s)
- `vllm/model_executor/models/deepseek_v2.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-08-21T17:18:59Z` `review` `CHANGES_REQUESTED` by `ProExpertProg`; signals: compile, cuda, kernel, mla, perf; excerpt: "I'm not sure if this is the best approach. The CustomOp abstraction is meant as a simple abstraction to dispatch between torch implementations and ..." (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3141646251)
- `2025-08-22T01:53:42Z` `issue` by `whx-sjtu`; signals: compile, cuda, kernel, mla, perf; excerpt: "I'm not sure if this is the best approach. The CustomOp abstraction is meant as a simple abstraction to dispatch between torch implementations and ..." (https://github.com/vllm-project/vllm/pull/23332#issuecomment-3212746038)
- `2025-08-22T02:16:22Z` `issue` by `ProExpertProg`; signals: attention, compile, cuda, fp8; excerpt: "Thank you for the picture. Honestly this is a common issue with attention, there can be a lot of ops hidden from torch.compile. There ..." (https://github.com/vllm-project/vllm/pull/23332#issuecomment-3212804798)
- `2025-08-22T02:35:05Z` `issue` by `whx-sjtu`; signals: attention, cuda, kernel, perf; excerpt: "Before we go down this rabbit hole, is Inductor supported on vllm-ascend? What about cuda graphs? Thanks for your attention. Currently, vLLM-Ascend does not ..." (https://github.com/vllm-project/vllm/pull/23332#issuecomment-3212832856)
- `2025-08-23T22:27:19Z` `issue` by `jgong5`; signals: compile, mla, moe, perf; excerpt: "Yeah, to elaborate, I think a custom pass mechanism to perform fusion would be good in vllm-ascend because plugging layers and fusing manually inside ..." (https://github.com/vllm-project/vllm/pull/23332#issuecomment-3217450860)
- `2025-08-26T02:57:07Z` `inline` by `whx-sjtu` `vllm/model_executor/layers/mla.py`:29; signals: attention, mla, moe; excerpt: "In history names there are also abbreviations like 'moe', 'silu' and 'rms norm' etc. Using 'mla' is simple and clear while using 'multi head ..." (https://github.com/vllm-project/vllm/pull/23332#discussion_r2299610450)
- `2025-08-24T05:50:09Z` `review` `COMMENTED` by `LucasWilkinson`; signals: hang, mla; excerpt: "I am not up to date on the intentions behind CustomOp or the HW plugins; so I will defer to the experts for final ..." (https://github.com/vllm-project/vllm/pull/23332#pullrequestreview-3141523380)
- `2025-08-22T03:19:38Z` `issue` by `whx-sjtu`; signals: attention, mla, register; excerpt: "2. Add an extra forward layer to AttentionImpl where instead of calling the custom op directly, forward outer is called on the impl. forward ..." (https://github.com/vllm-project/vllm/pull/23332#issuecomment-3212894590)
- `2025-08-23T05:57:50Z` `inline` by `Yikun` `vllm/model_executor/layers/mla.py`:29; signals: attention, mla; excerpt: "super tiny nit: according to history naming rule: Maybe this should be multi head latent attention" (https://github.com/vllm-project/vllm/pull/23332#discussion_r2295225772)
- `2025-08-26T09:53:33Z` `inline` by `Yikun` `vllm/model_executor/layers/mla.py`:29; signals: mla, register; excerpt: "My mean was we should keep class name same with register name." (https://github.com/vllm-project/vllm/pull/23332#discussion_r2300462441)
- `2025-08-22T03:33:24Z` `issue` by `ProExpertProg`; signals: cuda, cudagraph; excerpt: "Not exactly, but it would still require Inductor fusions anyway. Does vllm-ascend support (or use) Dynamo at all? What about AotDispatcher? Because we could ..." (https://github.com/vllm-project/vllm/pull/23332#issuecomment-3212914560)
- `2025-08-22T04:06:09Z` `issue` by `whx-sjtu`; signals: cuda, cudagraph; excerpt: "Not exactly, but it would still require Inductor fusions anyway. Does vllm-ascend support (or use) Dynamo at all? What about AotDispatcher? Because we could ..." (https://github.com/vllm-project/vllm/pull/23332#issuecomment-3212960648)
