# PR Discussion Digest

- Source PR: [vllm-project/vllm#23035](https://github.com/vllm-project/vllm/pull/23035)
- Source page: `sources/prs/vllm/PR-23035.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23035`
- Generated at: `2026-05-20T15:37:16.401660+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-16T21:00:00Z`
- Merged: `2025-08-21T03:08:51Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 18 (approved=1, commented=17)
- Inline review comments: 19
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=3, outdated=4
- Human participants with discussion text: DarkLight1337, Josephasafg, ProExpertProg, tdoublep, zou3519
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-08-16T21:01:09Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for Full and Piecewise CUDA Graphs for Mamba-1 models, which is ... (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3126053500)
- `2025-08-19T15:13:45Z` `COMMENTED` by `tdoublep` - In general, this change looks clean - just have a couple questions (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3132745793)
- `2025-08-19T17:16:18Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3126069896)
- `2025-08-19T20:08:14Z` `COMMENTED` by `tdoublep` (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3133674589)
- `2025-08-20T06:47:37Z` `COMMENTED` by `tdoublep` (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3135014614)
- `2025-08-20T06:48:48Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3135019568)
- `2025-08-20T12:36:05Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3136399108)
- `2025-08-20T14:48:29Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3136998054)
- `2025-08-20T18:09:42Z` `COMMENTED` by `tdoublep` (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3137730742)
- `2025-08-20T18:12:29Z` `COMMENTED` by `tdoublep` (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3137738627)
- `2025-08-20T18:18:50Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3137755055)
- `2025-08-20T18:25:03Z` `COMMENTED` by `tdoublep` (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3137770810)
- `2025-08-20T19:09:14Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3137897911)
- `2025-08-20T19:14:21Z` `COMMENTED` by `tdoublep` (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3137915870)
- `2025-08-20T19:30:41Z` `APPROVED` by `tdoublep` - LGTM (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3137972622)
- `2025-08-20T19:30:59Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3137973369)

## Inline Comment Hotspots

- `vllm/model_executor/layers/mamba/mamba_mixer.py`: 16 inline comment(s)
- `vllm/model_executor/models/mamba.py`: 2 inline comment(s)
- `vllm/v1/attention/backends/mamba1_attn.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-19T17:15:51Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/mamba/mamba_mixer.py`:196; signals: cuda, cudagraph; excerpt: "While I'm all for custom ops without mutating inputs, this one might be better by taking in output as an arg. IIRC this is ..." (https://github.com/vllm-project/vllm/pull/23035#discussion_r2285867293)
- `2025-08-19T20:08:14Z` `inline` by `tdoublep` `vllm/model_executor/layers/mamba/mamba_mixer.py`:196; signals: attention, cuda; excerpt: "Right, it makes sense that the output tensor needs to live in the CUDA graph. Just wasn't sure if torch can figure that out ..." (https://github.com/vllm-project/vllm/pull/23035#discussion_r2286219550)
- `2025-08-20T19:09:14Z` `inline` by `Josephasafg` `vllm/model_executor/layers/mamba/mamba_mixer.py`:436; signals: cache, cuda; excerpt: "Its a good question. I think that in V0 in the mamba cache - padding is applied for CUDA Graph capture. It would make ..." (https://github.com/vllm-project/vllm/pull/23035#discussion_r2289051781)
- `2025-08-19T15:13:45Z` `review` `COMMENTED` by `tdoublep`; signals: hang; excerpt: "In general, this change looks clean - just have a couple questions" (https://github.com/vllm-project/vllm/pull/23035#pullrequestreview-3132745793)
- `2025-08-19T15:01:56Z` `inline` by `tdoublep` `vllm/model_executor/layers/mamba/mamba_mixer.py`:196; signals: hang; excerpt: "Did you happen to check if it worked if you return the output instead of mutating? I know I made similar changes in Mamba2, ..." (https://github.com/vllm-project/vllm/pull/23035#discussion_r2285555341)
- `2025-08-19T15:08:59Z` `inline` by `tdoublep` `vllm/model_executor/layers/mamba/mamba_mixer.py`:444; signals: cuda; excerpt: "I think this might be a bug inherited from the mamba2 implementation that was caught by the AI on another PR. state indices tensor ..." (https://github.com/vllm-project/vllm/pull/23035#discussion_r2285572703)
- `2025-08-20T06:47:37Z` `inline` by `tdoublep` `vllm/model_executor/layers/mamba/mamba_mixer.py`:196; signals: block; excerpt: "to be clear: this doesn't need to block merging this PR. Mutating the output is the way it is implemented for mamba2 right now, ..." (https://github.com/vllm-project/vllm/pull/23035#discussion_r2287154548)
- `2025-08-20T12:36:04Z` `inline` by `Josephasafg` `vllm/model_executor/layers/mamba/mamba_mixer.py`:444; signals: cuda; excerpt: "@tdoublep Thanks I added a two things - - In mamba1 attn Im doing the padding for full cuda graphs only as for piecewise ..." (https://github.com/vllm-project/vllm/pull/23035#discussion_r2288028824)
- `2025-08-20T18:25:03Z` `inline` by `tdoublep` `vllm/model_executor/layers/mamba/mamba_mixer.py`:436; signals: cuda; excerpt: "Just thinking this through: if FCG is enabled then num prefill tokens=0, but wouldn't we also want to use num decode tokens in this ..." (https://github.com/vllm-project/vllm/pull/23035#discussion_r2288958271)
- `2025-08-16T21:40:29Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/mamba/mamba_mixer.py`:193; signals: cuda; excerpt: "@tdoublep do you know why we forced the CUDA op in V1?" (https://github.com/vllm-project/vllm/pull/23035#discussion_r2280612944)
- `2025-08-20T18:09:42Z` `inline` by `tdoublep` `vllm/model_executor/layers/mamba/mamba_mixer.py`:193; signals: cuda; excerpt: "I think forward cuda is the only implementation rn." (https://github.com/vllm-project/vllm/pull/23035#discussion_r2288928971)
- `2025-08-20T18:18:50Z` `inline` by `Josephasafg` `vllm/model_executor/layers/mamba/mamba_mixer.py`:451; signals: hang; excerpt: "Apologies it was meant to be num padded decodes. I hadn’t pushed the change earlier" (https://github.com/vllm-project/vllm/pull/23035#discussion_r2288946202)
