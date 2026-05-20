# PR Discussion Digest

- Source PR: [vllm-project/vllm#29642](https://github.com/vllm-project/vllm/pull/29642)
- Source page: `sources/prs/vllm/PR-29642.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29642`
- Generated at: `2026-05-20T15:38:45.728301+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-28T04:26:06Z`
- Merged: `2025-12-07T09:58:47Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 15 (approved=1, commented=14)
- Inline review comments: 19
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: ElizaWszola, alexm-redhat, chatgpt-codex-connector, jeejeelee, jinzhen-lin, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-28T04:27:59Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces several well-implemented optimizations to moe align block size, resulting in significant performance ... (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3517442635)
- `2025-11-28T04:33:10Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3517448306)
- `2025-11-28T08:16:12Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3517884887)
- `2025-11-28T08:23:56Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3517906440)
- `2025-11-28T08:25:08Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3517909648)
- `2025-11-28T08:29:06Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3517924221)
- `2025-12-05T16:48:43Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3545562661)
- `2025-12-05T17:00:27Z` `COMMENTED` by `alexm-redhat` - @jinzhen-lin thanks for the PR, these are nice ideas and provide good speedups. Left some review comments - ... (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3545591170)
- `2025-12-05T17:01:00Z` `APPROVED` by `alexm-redhat` (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3545613924)
- `2025-12-06T00:03:14Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3546759949)
- `2025-12-06T00:06:33Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3546763620)
- `2025-12-06T00:09:53Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3546766541)
- `2025-12-06T00:15:00Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3546770886)
- `2025-12-06T00:15:42Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3546771455)
- `2025-12-06T00:17:09Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/29642#pullrequestreview-3546772610)

## Inline Comment Hotspots

- `csrc/moe/moe_align_sum_kernels.cu`: 11 inline comment(s)
- `vllm/model_executor/layers/fused_moe/moe_align_block_size.py`: 6 inline comment(s)
- `csrc/moe/torch_bindings.cpp`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-05T16:48:43Z` `inline` by `jeejeelee` `csrc/moe/moe_align_sum_kernels.cu`:95; signals: block, kernel, moe, perf, performance; excerpt: "Just curious, can we get better performance by using more blocks (e.g., 4, 8)?" (https://github.com/vllm-project/vllm/pull/29642#discussion_r2593321626)
- `2025-12-06T00:03:14Z` `inline` by `jinzhen-lin` `csrc/moe/moe_align_sum_kernels.cu`:95; signals: block, kernel, moe, perf, performance; excerpt: "In my local test, one additional threadblock is enough to get best performance." (https://github.com/vllm-project/vllm/pull/29642#discussion_r2594256333)
- `2025-12-05T16:56:49Z` `inline` by `alexm-redhat` `csrc/moe/moe_align_sum_kernels.cu`:215; signals: kernel, moe, perf, performance; excerpt: "what is the performance benefit of the small batch kernel vs the standard one (above)? Just to get a feeling..." (https://github.com/vllm-project/vllm/pull/29642#discussion_r2593344744)
- `2025-12-05T16:58:06Z` `inline` by `alexm-redhat` `csrc/moe/moe_align_sum_kernels.cu`:295; signals: block, kernel, moe; excerpt: "why not use the same idea of a separate threadblock to prefill expert ids all with 0s, and then you don't need to do ..." (https://github.com/vllm-project/vllm/pull/29642#discussion_r2593348256)
- `2025-12-06T00:15:00Z` `inline` by `jinzhen-lin` `csrc/moe/moe_align_sum_kernels.cu`:295; signals: block, kernel, moe; excerpt: "The size of expert ids is only 1/block size the size of sorted token ids, so this might not offer much improvement, but I ..." (https://github.com/vllm-project/vllm/pull/29642#discussion_r2594266236)
- `2025-12-05T16:58:48Z` `inline` by `alexm-redhat` `csrc/moe/moe_align_sum_kernels.cu`:357; signals: kernel, moe, perf; excerpt: "any reason for 256? does it provide best perf?" (https://github.com/vllm-project/vllm/pull/29642#discussion_r2593350280)
- `2025-11-28T04:33:10Z` `inline` by `chatgpt-codex-connector` `csrc/moe/torch_bindings.cpp`:23; signals: failing, moe; excerpt: ". Please supply a default of None in the schema or update callers to pass the extra argument to keep tests from failing immediately. ..." (https://github.com/vllm-project/vllm/pull/29642#discussion_r2570448538)
- `2025-12-06T00:06:33Z` `inline` by `jinzhen-lin` `csrc/moe/moe_align_sum_kernels.cu`:215; signals: kernel, moe; excerpt: "I'm not sure, maybe it's because it can be completed within a single kernel, instead of splitting it into align kernel and sort kernel ..." (https://github.com/vllm-project/vllm/pull/29642#discussion_r2594259554)
- `2025-12-06T00:09:53Z` `inline` by `jinzhen-lin` `csrc/moe/moe_align_sum_kernels.cu`:233; signals: kernel, moe; excerpt: "We need syncthreads() to prevent other threads from writing before the fill operation is completed. The reason for using three is that there are ..." (https://github.com/vllm-project/vllm/pull/29642#discussion_r2594262090)
- `2025-12-06T00:17:09Z` `inline` by `jinzhen-lin` `vllm/model_executor/layers/fused_moe/moe_align_block_size.py`:40; signals: block, moe; excerpt: "I'm not sure if there are other places that rely on the original EP logic, so I added this parameter and set its default ..." (https://github.com/vllm-project/vllm/pull/29642#discussion_r2594267949)
- `2025-11-28T08:16:11Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/fused_moe/moe_align_block_size.py`:80; signals: block, moe; excerpt: "redundant min" (https://github.com/vllm-project/vllm/pull/29642#discussion_r2570777234)
- `2025-11-28T08:23:56Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/fused_moe/moe_align_block_size.py`:17; signals: block, moe; excerpt: "nit: maybe rename to ignore invalid experts?" (https://github.com/vllm-project/vllm/pull/29642#discussion_r2570795808)
