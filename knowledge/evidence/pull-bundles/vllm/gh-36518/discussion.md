# PR Discussion Digest

- Source PR: [vllm-project/vllm#36518](https://github.com/vllm-project/vllm/pull/36518)
- Source page: `sources/prs/vllm/PR-36518.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36518`
- Generated at: `2026-05-20T15:40:13.277952+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-09T15:56:59Z`
- Merged: `2026-04-03T01:47:04Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 18 (approved=1, commented=17)
- Inline review comments: 29
- Review threads observed: 19
- Resolved/outdated thread markers: resolved=18, outdated=13
- Human participants with discussion text: ProExpertProg, carlyou, chatgpt-codex-connector, mergify
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-09T16:01:58Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a valuable optimization by fusing FP8 output quantization into the merge attn ... (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3916478319)
- `2026-03-09T16:03:20Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. Reviewed commit: ba229809ff ℹ️ About ... (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3916490239)
- `2026-03-09T16:49:38Z` `COMMENTED` by `carlyou` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3916794470)
- `2026-03-09T16:54:18Z` `COMMENTED` by `carlyou` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3916827366)
- `2026-03-09T17:02:51Z` `COMMENTED` by `carlyou` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3916888096)
- `2026-03-12T18:25:14Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3933170395)
- `2026-03-13T00:19:53Z` `COMMENTED` by `carlyou` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3940736831)
- `2026-03-14T18:24:47Z` `COMMENTED` by `carlyou` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3949123574)
- `2026-03-14T23:19:25Z` `COMMENTED` by `ProExpertProg` - Just a few minor notes again! (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3949401245)
- `2026-03-16T22:55:51Z` `COMMENTED` by `carlyou` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3957206835)
- `2026-03-16T23:00:02Z` `COMMENTED` by `carlyou` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3957233937)
- `2026-03-16T23:04:12Z` `COMMENTED` by `carlyou` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3957253081)
- `2026-03-16T23:04:39Z` `COMMENTED` by `carlyou` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3957255016)
- `2026-03-17T07:16:43Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3958650331)
- `2026-03-18T03:53:51Z` `COMMENTED` by `carlyou` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-3964855764)
- `2026-04-01T21:07:10Z` `APPROVED` by `ProExpertProg` - A few minor notes, otherwise LGTM (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-4047040995)
- `2026-04-02T11:52:58Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-4050157808)
- `2026-04-02T22:11:31Z` `COMMENTED` by `carlyou` (https://github.com/vllm-project/vllm/pull/36518#pullrequestreview-4053459223)

## Inline Comment Hotspots

- `benchmarks/fused_kernels/merge_attn_states_benchmarks.py`: 10 inline comment(s)
- `csrc/attention/merge_attn_states.cu`: 8 inline comment(s)
- `vllm/v1/attention/ops/triton_merge_attn_states.py`: 5 inline comment(s)
- `tests/kernels/attention/test_merge_attn_states.py`: 5 inline comment(s)
- `vllm/v1/attention/ops/merge_attn_states.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-09T16:03:20Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/ops/merge_attn_states.py`:75; signals: attention, cuda, dtype, fp8, kernel, memory; excerpt: ") and writes scalar t-sized values into an FP8 buffer, which can corrupt the output/memory instead of falling back safely. Please keep an output-dtype ..." (https://github.com/vllm-project/vllm/pull/36518#discussion_r2906400045)
- `2026-03-14T23:04:36Z` `inline` by `ProExpertProg` `benchmarks/fused_kernels/merge_attn_states_benchmarks.py`:98; signals: benchmark, cuda, cudagraph, kernel, triton; excerpt: "I think we usually use triton's builtin benchmarking for all of these. That also captures a cudagraph and I believe is generally considered the ..." (https://github.com/vllm-project/vllm/pull/36518#discussion_r2935951558)
- `2026-03-14T23:06:33Z` `inline` by `ProExpertProg` `benchmarks/fused_kernels/merge_attn_states_benchmarks.py`:248; signals: benchmark, compile, cuda, fp8, kernel; excerpt: "Can you look at how quant fp8 is benchmarked? We want to use the torch.compiled kernel here because it's faster than cuda, and that's ..." (https://github.com/vllm-project/vllm/pull/36518#discussion_r2935953971)
- `2026-03-16T23:04:12Z` `inline` by `carlyou` `benchmarks/fused_kernels/merge_attn_states_benchmarks.py`:243; signals: benchmark, kernel, perf, triton; excerpt: "@ProExpertProg , updated benchmark script per comments. The triton fused is now performing worse when token batch is small. Example for 128 heads x ..." (https://github.com/vllm-project/vllm/pull/36518#discussion_r2943474258)
- `2026-03-17T07:16:43Z` `inline` by `ProExpertProg` `benchmarks/fused_kernels/merge_attn_states_benchmarks.py`:243; signals: benchmark, block, cuda, kernel; excerpt: "Huh, that's very weird. Would be good to investigate. But no need to block the CUDA-side improvements if it takes a bit longer to ..." (https://github.com/vllm-project/vllm/pull/36518#discussion_r2944838290)
- `2026-03-18T03:53:51Z` `inline` by `carlyou` `benchmarks/fused_kernels/merge_attn_states_benchmarks.py`:243; signals: benchmark, kernel, triton; excerpt: "it was caused by the 1 / output scale outside of triton kernel 🤦 , [fixed]( Below is the updated benchmark result:" (https://github.com/vllm-project/vllm/pull/36518#discussion_r2950707950)
- `2026-03-09T16:49:38Z` `inline` by `carlyou` `vllm/v1/attention/ops/triton_merge_attn_states.py`:138; signals: attention, fp8, triton; excerpt: "TODO: move to if USE FP8 above." (https://github.com/vllm-project/vllm/pull/36518#discussion_r2906670691)
- `2026-03-14T23:08:19Z` `inline` by `ProExpertProg` `benchmarks/fused_kernels/merge_attn_states_benchmarks.py`:397; signals: benchmark, dtype, kernel; excerpt: "Maybe make a --out-dtypes nargs param?" (https://github.com/vllm-project/vllm/pull/36518#discussion_r2935955839)
- `2026-04-01T21:06:52Z` `inline` by `ProExpertProg` `tests/kernels/attention/test_merge_attn_states.py`:365; signals: attention, fp8, kernel; excerpt: "Instead of a new test, could we add a bool param fp8 output to the existing test above?" (https://github.com/vllm-project/vllm/pull/36518#discussion_r3024666358)
- `2026-03-14T23:07:33Z` `inline` by `ProExpertProg` `benchmarks/fused_kernels/merge_attn_states_benchmarks.py`:346; signals: benchmark, kernel; excerpt: "If not too much trouble, should we use pd or something to print out markdown so we don't have to maintain our own table ..." (https://github.com/vllm-project/vllm/pull/36518#discussion_r2935955099)
- `2026-04-02T11:52:43Z` `inline` by `ProExpertProg` `tests/kernels/attention/test_merge_attn_states.py`:320; signals: attention, kernel; excerpt: "These seem abnormally high, are we sure this is ok? I've never had to use tolerances higher than 1e-1" (https://github.com/vllm-project/vllm/pull/36518#discussion_r3027593002)
- `2026-03-09T16:54:18Z` `inline` by `carlyou` `vllm/v1/attention/ops/triton_merge_attn_states.py`:10; signals: attention, triton; excerpt: "TODO: replace hardcode values" (https://github.com/vllm-project/vllm/pull/36518#discussion_r2906698420)
