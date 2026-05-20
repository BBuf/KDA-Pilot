# PR Discussion Digest

- Source PR: [vllm-project/vllm#23809](https://github.com/vllm-project/vllm/pull/23809)
- Source page: `sources/prs/vllm/PR-23809.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23809`
- Generated at: `2026-05-20T15:37:42.310682+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-28T08:01:57Z`
- Merged: `2025-09-24T01:32:23Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 13 (approved=1, commented=12)
- Inline review comments: 12
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=5, outdated=4
- Human participants with discussion text: aditew01, mergify, mgoin, nikhil-arm, xiangze-arm
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-28T08:06:32Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for 4-bit fused Mixture-of-Experts (MoE) on ARM CPU platforms. The changes ... (https://github.com/vllm-project/vllm/pull/23809#pullrequestreview-3163718793)
- `2025-08-28T13:54:07Z` `COMMENTED` by `nikhil-arm` (https://github.com/vllm-project/vllm/pull/23809#pullrequestreview-3164973427)
- `2025-08-28T13:54:43Z` `COMMENTED` by `nikhil-arm` (https://github.com/vllm-project/vllm/pull/23809#pullrequestreview-3164975835)
- `2025-09-11T13:45:28Z` `COMMENTED` by `nikhil-arm` (https://github.com/vllm-project/vllm/pull/23809#pullrequestreview-3211692085)
- `2025-09-11T13:57:30Z` `COMMENTED` by `aditew01` (https://github.com/vllm-project/vllm/pull/23809#pullrequestreview-3211780324)
- `2025-09-11T14:24:21Z` `COMMENTED` by `nikhil-arm` (https://github.com/vllm-project/vllm/pull/23809#pullrequestreview-3211952095)
- `2025-09-11T14:24:37Z` `COMMENTED` by `nikhil-arm` (https://github.com/vllm-project/vllm/pull/23809#pullrequestreview-3211953737)
- `2025-09-15T11:10:41Z` `COMMENTED` by `nikhil-arm` (https://github.com/vllm-project/vllm/pull/23809#pullrequestreview-3224093366)
- `2025-09-16T10:13:10Z` `COMMENTED` by `xiangze-arm` (https://github.com/vllm-project/vllm/pull/23809#pullrequestreview-3228955598)
- `2025-09-17T11:16:23Z` `COMMENTED` by `nikhil-arm` (https://github.com/vllm-project/vllm/pull/23809#pullrequestreview-3233933524)
- `2025-09-17T13:12:44Z` `COMMENTED` by `nikhil-arm` (https://github.com/vllm-project/vllm/pull/23809#pullrequestreview-3234405702)
- `2025-09-17T14:41:45Z` `COMMENTED` by `nikhil-arm` (https://github.com/vllm-project/vllm/pull/23809#pullrequestreview-3234835239)
- `2025-09-19T15:48:04Z` `APPROVED` by `mgoin` - LGTM, nice work! (https://github.com/vllm-project/vllm/pull/23809#pullrequestreview-3245570256)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 6 inline comment(s)
- `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py`: 4 inline comment(s)
- `csrc/moe/dynamic_4bit_int_moe_cpu.cpp`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-17T11:16:23Z` `inline` by `nikhil-arm` `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py`:109; signals: moe, tma, vector; excerpt: "for primitive ops, pytorch uses vectorizer classes internally. These vectoriser classes are highly optimised. My idea was to use combination of ops instead of ..." (https://github.com/vllm-project/vllm/pull/23809#discussion_r2355170871)
- `2025-08-28T13:54:06Z` `inline` by `nikhil-arm` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:1813; signals: dtype, moe; excerpt: "fix scale & bias dtype hardcoding" (https://github.com/vllm-project/vllm/pull/23809#discussion_r2307494720)
- `2025-09-11T13:57:30Z` `inline` by `aditew01` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:1945; signals: hang, moe; excerpt: "Note: add routed scaling factor param to be in sync with latest changes: ref:" (https://github.com/vllm-project/vllm/pull/23809#discussion_r2341010144)
- `2025-09-16T10:13:10Z` `inline` by `xiangze-arm` `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py`:109; signals: moe, tma; excerpt: "I think these 4 lines are equivalent to a Softmax?" (https://github.com/vllm-project/vllm/pull/23809#discussion_r2351820809)
- `2025-09-17T13:12:44Z` `inline` by `nikhil-arm` `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py`:109; signals: moe, tma; excerpt: "torch.softmax() is faster" (https://github.com/vllm-project/vllm/pull/23809#discussion_r2355482660)
- `2025-09-23T15:15:17Z` `issue` by `nikhil-arm`; signals: compile, hang; excerpt: "Looks like it failed to compile Thanks, I have fixed it and pushed the changes" (https://github.com/vllm-project/vllm/pull/23809#issuecomment-3324462654)
- `2025-08-28T13:54:43Z` `inline` by `nikhil-arm` `csrc/moe/dynamic_4bit_int_moe_cpu.cpp`:5; signals: moe; excerpt: "remove unused headers" (https://github.com/vllm-project/vllm/pull/23809#discussion_r2307496552)
- `2025-09-11T13:45:28Z` `inline` by `nikhil-arm` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:1970; signals: moe; excerpt: "vLLM treats silu as siluandmul for moe. swiglu gu is correct implementation for silu or swiglu" (https://github.com/vllm-project/vllm/pull/23809#discussion_r2340944599)
- `2025-09-11T14:24:21Z` `inline` by `nikhil-arm` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:1945; signals: moe; excerpt: "done" (https://github.com/vllm-project/vllm/pull/23809#discussion_r2341138049)
- `2025-09-11T14:24:37Z` `inline` by `nikhil-arm` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:1813; signals: moe; excerpt: "done" (https://github.com/vllm-project/vllm/pull/23809#discussion_r2341139284)
- `2025-09-15T11:10:40Z` `inline` by `nikhil-arm` `csrc/moe/dynamic_4bit_int_moe_cpu.cpp`:118; signals: moe; excerpt: "use openai specific limits and alpha with sigmoid" (https://github.com/vllm-project/vllm/pull/23809#discussion_r2348653647)
- `2025-09-17T14:41:44Z` `inline` by `nikhil-arm` `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py`:109; signals: moe; excerpt: "done" (https://github.com/vllm-project/vllm/pull/23809#discussion_r2355771213)
