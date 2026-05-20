# PR Discussion Digest

- Source PR: [vllm-project/vllm#28269](https://github.com/vllm-project/vllm/pull/28269)
- Source page: `sources/prs/vllm/PR-28269.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28269`
- Generated at: `2026-05-20T15:38:27.930578+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-07T05:33:13Z`
- Merged: `2025-11-11T23:32:21Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 14 (approved=2, commented=12)
- Inline review comments: 11
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: benchislett, chatgpt-codex-connector, maxyanghu, mergify, mgoin, mratsim, pavanimajety, wangshangsam
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-11-07T05:34:29Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a configurable workspace size for FlashInfer via the VLLM FLASHINFER WORKSPACE BUFFER ... (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3431736235)
- `2025-11-07T05:34:48Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3431736787)
- `2025-11-07T18:01:27Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3435518614)
- `2025-11-07T18:31:55Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3435660838)
- `2025-11-07T18:33:42Z` `COMMENTED` by `benchislett` - This looks good to me overall. I do think the best approach here is to determine this limit ... (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3435669525)
- `2025-11-07T19:13:58Z` `COMMENTED` by `maxyanghu` (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3435863176)
- `2025-11-07T19:38:21Z` `APPROVED` by `benchislett` - LGTM, Thanks! (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3435990082)
- `2025-11-07T20:06:25Z` `COMMENTED` by `mratsim` (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3436119462)
- `2025-11-07T20:59:59Z` `COMMENTED` by `maxyanghu` (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3436385037)
- `2025-11-08T15:07:44Z` `COMMENTED` by `mratsim` (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3438432777)
- `2025-11-08T20:25:05Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3438589214)
- `2025-11-10T17:20:43Z` `COMMENTED` by `maxyanghu` (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3444340995)
- `2025-11-10T19:17:54Z` `COMMENTED` by `wangshangsam` (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3444770870)

## Inline Comment Hotspots

- `vllm/envs.py`: 7 inline comment(s)
- `vllm/v1/attention/backends/mla/common.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-11-07T05:34:48Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/mla/common.py`:602; signals: attention, cuda, flashinfer, gemm, hang, kernel, mla; excerpt: "for the FlashInfer prefill and TRT-LLM ragged prefill workspaces, sized to avoid CUDA workspace underflows for typical GEMM dimensions. This change routes both allocations ..." (https://github.com/vllm-project/vllm/pull/28269#discussion_r2501747154)
- `2025-11-07T18:01:27Z` `inline` by `pavanimajety` `vllm/v1/attention/backends/mla/common.py`:587; signals: attention, flashinfer, mla; excerpt: "Could we set to the max of env var and the previous value? max(394 1024 1024, envs.VLLM FLASHINFER WORKSPACE BUFFER SIZE) here? Seems like ..." (https://github.com/vllm-project/vllm/pull/28269#discussion_r2504837075)
- `2025-11-07T19:12:49Z` `issue` by `maxyanghu`; signals: cuda, fp4, nvfp4; excerpt: "@maxyanghu Could you please post the evals for a model that would need higher than the default size using the new env var? If ..." (https://github.com/vllm-project/vllm/pull/28269#issuecomment-3504392571)
- `2025-11-07T18:31:55Z` `inline` by `benchislett` `vllm/v1/attention/backends/mla/common.py`:587; signals: attention, mla; excerpt: "I would prefer to just increase the default to 394. I've had to increase this threshold from 256 a few times when locally running ..." (https://github.com/vllm-project/vllm/pull/28269#discussion_r2504938935)
- `2025-11-10T17:20:43Z` `inline` by `maxyanghu` `vllm/envs.py`:162; signals: hang, memory; excerpt: "@mratsim Hi, yeah I saw the link but I'd rather keep it unchanged as I don't know the exact amount of memory it requires." (https://github.com/vllm-project/vllm/pull/28269#discussion_r2511370739)
- `2025-11-07T18:33:42Z` `review` `COMMENTED` by `benchislett`; signals: flashinfer; excerpt: "This looks good to me overall. I do think the best approach here is to determine this limit dynamically based on max batch size ..." (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3435669525)
- `2025-11-07T19:13:58Z` `inline` by `maxyanghu` `vllm/v1/attention/backends/mla/common.py`:587; signals: attention, mla; excerpt: "i increased the default to 394" (https://github.com/vllm-project/vllm/pull/28269#discussion_r2505084646)
- `2025-11-10T19:17:54Z` `inline` by `wangshangsam` `vllm/envs.py`:162; signals: flashinfer; excerpt: "@mratsim The point of this PR is so that you could set the value of VLLM FLASHINFER WORKSPACE BUFFER SIZE for your specific use ..." (https://github.com/vllm-project/vllm/pull/28269#discussion_r2511684484)
- `2025-11-07T05:34:48Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/28269#pullrequestreview-3431736787)
- `2025-11-07T20:06:18Z` `inline` by `mratsim` `vllm/envs.py`:162; signals: general review; excerpt: "394 is a strange default. I assume you meant 384 which is 128+256" (https://github.com/vllm-project/vllm/pull/28269#discussion_r2505296234)
- `2025-11-07T20:59:59Z` `inline` by `maxyanghu` `vllm/envs.py`:162; signals: general review; excerpt: "This is directly copied from [here]( a known use case." (https://github.com/vllm-project/vllm/pull/28269#discussion_r2505504581)
- `2025-11-08T15:07:44Z` `inline` by `mratsim` `vllm/envs.py`:162; signals: general review; excerpt: "And the sglang link mentioned is using 384 not 394" (https://github.com/vllm-project/vllm/pull/28269#discussion_r2506969895)
