# PR Discussion Digest

- Source PR: [vllm-project/vllm#28687](https://github.com/vllm-project/vllm/pull/28687)
- Source page: `sources/prs/vllm/PR-28687.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28687`
- Generated at: `2026-05-20T15:38:32.006623+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-13T22:48:09Z`
- Merged: `2025-11-19T23:47:13Z`

## Discussion Counts

- Issue comments: 17
- Review submissions: 8 (approved=2, changes_requested=1, commented=5)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=3
- Human participants with discussion text: ElizaWszola, alexm-redhat, chatgpt-codex-connector, heheda12345, mergify, mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-13T22:50:43Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28687#pullrequestreview-3462018586)
- `2025-11-13T22:56:10Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to improve performance by removing a dimension restriction in the should use ... (https://github.com/vllm-project/vllm/pull/28687#pullrequestreview-3462032595)
- `2025-11-16T07:29:15Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/28687#pullrequestreview-3469819752)
- `2025-11-17T19:47:28Z` `COMMENTED` by `yewentao256` - We should be more careful about removing this. I tried to remove before, and got a lot performance ... (https://github.com/vllm-project/vllm/pull/28687#pullrequestreview-3474327296)
- `2025-11-17T22:21:44Z` `COMMENTED` by `alexm-redhat` (https://github.com/vllm-project/vllm/pull/28687#pullrequestreview-3474773402)
- `2025-11-18T17:25:51Z` `APPROVED` by `yewentao256` - vllm bench serve --model deepseek-ai/DeepSeek-R1 --dataset-name random --host 127.0.0.1 --random-input-len 4 --random-output-len 1024 --request-rate inf --num-prompts 1024 --port ... (https://github.com/vllm-project/vllm/pull/28687#pullrequestreview-3478955772)
- `2025-11-18T19:38:39Z` `CHANGES_REQUESTED` by `mgoin` - @alexm-redhat Can we please add unit test cases before landing? See where we currently skip many shapes And ... (https://github.com/vllm-project/vllm/pull/28687#pullrequestreview-3479464225)
- `2025-11-19T19:47:33Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28687#pullrequestreview-3484461086)

## Inline Comment Hotspots

- `vllm/utils/deep_gemm.py`: 2 inline comment(s)
- `examples/offline_inference/basic/basic.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-13T22:50:43Z` `inline` by `chatgpt-codex-connector` `vllm/utils/deep_gemm.py`:351; signals: aligned, alignment, block, deepgemm, fp8, gemm, hang, kernel; excerpt: "[0] (currently 128), and the DeepGEMM kernels require that block alignment to operate correctly. With this change, layers whose weight shapes are not aligned ..." (https://github.com/vllm-project/vllm/pull/28687#discussion_r2525183599)
- `2025-11-17T22:13:56Z` `issue` by `alexm-redhat`; signals: b200, deepgemm, gemm, perf, performance; excerpt: "@yewentao256 @robertgshaw2-redhat Verified performance for DSR1 on 8xB200 system that has DeepGEMM installed. For TP==8 and DP==8 (+EP), performance with the PR or without ..." (https://github.com/vllm-project/vllm/pull/28687#issuecomment-3544062898)
- `2025-11-17T23:06:04Z` `issue` by `yewentao256`; signals: b200, deepgemm, gemm, perf, performance; excerpt: "@yewentao256 @robertgshaw2-redhat Verified performance for DSR1 on 8xB200 system that has DeepGEMM installed. For TP==8 and DP==8 (+EP), performance with the PR or without ..." (https://github.com/vllm-project/vllm/pull/28687#issuecomment-3544220344)
- `2025-11-14T06:37:45Z` `issue` by `ElizaWszola`; signals: block, deepgemm, fp8, gemm; excerpt: "If we successfully remove the size restriction, it would be good if we could also remove the should use deepgemm for fp8 linear condition ..." (https://github.com/vllm-project/vllm/pull/28687#issuecomment-3531127400)
- `2025-11-18T19:42:03Z` `issue` by `mgoin`; signals: block, deepgemm, fp8, gemm; excerpt: "If we successfully remove the size restriction, it would be good if we could also remove the should use deepgemm for fp8 linear condition ..." (https://github.com/vllm-project/vllm/pull/28687#issuecomment-3549299942)
- `2025-11-17T19:47:28Z` `review` `COMMENTED` by `yewentao256`; signals: perf, performance; excerpt: "We should be more careful about removing this. I tried to remove before, and got a lot performance loss. Seems to be like dp=8 ..." (https://github.com/vllm-project/vllm/pull/28687#pullrequestreview-3474327296)
- `2025-11-18T19:38:39Z` `review` `CHANGES_REQUESTED` by `mgoin`; signals: blackwell, hopper; excerpt: "@alexm-redhat Can we please add unit test cases before landing? See where we currently skip many shapes And I think the current N and ..." (https://github.com/vllm-project/vllm/pull/28687#pullrequestreview-3479464225)
- `2025-11-13T23:59:56Z` `issue` by `mgoin`; signals: blackwell, hopper, kernel; excerpt: "We should check this on Hopper and Blackwell, and make sure to expand the kernel unit test to check for edge cases" (https://github.com/vllm-project/vllm/pull/28687#issuecomment-3530234472)
- `2025-11-17T21:02:24Z` `issue` by `alexm-redhat`; signals: h200, perf, performance; excerpt: "@yewentao256 I have verified dp==8 DSR1 (on H200) and the performance is actually better with this PR, about 1.5% for TPOT." (https://github.com/vllm-project/vllm/pull/28687#issuecomment-3543828860)
- `2025-11-17T21:10:35Z` `issue` by `alexm-redhat`; signals: deepgemm, fp8, gemm; excerpt: "Also, I did a manual inspection of the deepgemm code and did not found any 128 division restriction for the gemm we use (fp8 ..." (https://github.com/vllm-project/vllm/pull/28687#issuecomment-3543859096)
- `2025-11-18T17:25:51Z` `review` `APPROVED` by `yewentao256`; signals: perf, performance; excerpt: "vllm bench serve --model deepseek-ai/DeepSeek-R1 --dataset-name random --host 127.0.0.1 --random-input-len 4 --random-output-len 1024 --request-rate inf --num-prompts 1024 --port 9256 For larger batch size, seems ..." (https://github.com/vllm-project/vllm/pull/28687#pullrequestreview-3478955772)
- `2025-11-13T22:50:43Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/28687#pullrequestreview-3462018586)
