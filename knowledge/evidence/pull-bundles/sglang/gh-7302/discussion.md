# PR Discussion Digest

- Source PR: [sgl-project/sglang#7302](https://github.com/sgl-project/sglang/pull/7302)
- Source page: `sources/prs/sglang/PR-7302.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7302`
- Generated at: `2026-05-20T15:31:11.547544+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-18T06:36:53Z`
- Merged: `2025-07-19T02:59:39Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 6 (approved=2, changes_requested=2, commented=2)
- Inline review comments: 7
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=6
- Human participants with discussion text: BowenBao, HaiShaw, RioXu, haohui, merrymercy
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-06-18T06:37:20Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @haohui, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7302#pullrequestreview-2937911085)
- `2025-06-18T06:45:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This PR adds support for FP4 quantized models on AMD GPUs, using the Petit library. It ... (https://github.com/sgl-project/sglang/pull/7302#pullrequestreview-2937929453)
- `2025-06-30T00:21:59Z` `CHANGES_REQUESTED` by `HaiShaw` - Can we change petit fp4 to petit nvfp4? (https://github.com/sgl-project/sglang/pull/7302#pullrequestreview-2969607564)
- `2025-07-07T09:07:08Z` `CHANGES_REQUESTED` by `HaiShaw` - Few more name changes? (https://github.com/sgl-project/sglang/pull/7302#pullrequestreview-2992868006)
- `2025-07-16T21:38:52Z` `APPROVED` by `HaiShaw` - LGTM, thanks! (https://github.com/sgl-project/sglang/pull/7302#pullrequestreview-3026981431)
- `2025-07-19T02:59:27Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/7302#pullrequestreview-3035093853)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/petit.py`: 5 inline comment(s)
- `python/sglang/srt/server_args.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/petit_utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-14T00:49:32Z` `issue` by `haohui`; signals: accuracy, b200, bf16, fp4, kernel, perf, performance, throughput; excerpt: "Updated the PR to address the comments. Also pull the petit-kernel 0.0.2 release. The 0.0.2 releases improves both the performance and accuracy. I use ..." (https://github.com/sgl-project/sglang/pull/7302#issuecomment-3067456476)
- `2025-06-30T00:21:59Z` `review` `CHANGES_REQUESTED` by `HaiShaw`; signals: fp4, hang, nvfp4; excerpt: "Can we change petit fp4 to petit nvfp4?" (https://github.com/sgl-project/sglang/pull/7302#pullrequestreview-2969607564)
- `2025-07-01T02:04:51Z` `issue` by `haohui`; signals: benchmark, bf16, fp4, tensorrt; excerpt: "@haohui from MMLU is 83.3 for BF16, 81.1 for FP4. The reported MMLU benchmark scores are BF16: 82.22 and FP4: 78.88, any thought on ..." (https://github.com/sgl-project/sglang/pull/7302#issuecomment-3021447887)
- `2025-06-29T23:42:30Z` `issue` by `HaiShaw`; signals: benchmark, bf16, fp4; excerpt: "@haohui from MMLU is 83.3 for BF16, 81.1 for FP4. The reported MMLU benchmark scores are BF16: 82.22 and FP4: 78.88, any thought on ..." (https://github.com/sgl-project/sglang/pull/7302#issuecomment-3017279602)
- `2025-07-07T09:05:10Z` `inline` by `HaiShaw` `python/sglang/srt/layers/quantization/petit.py`:54; signals: fp4, nvfp4; excerpt: "petit nvfp4?" (https://github.com/sgl-project/sglang/pull/7302#discussion_r2189437153)
- `2025-07-07T09:06:22Z` `inline` by `HaiShaw` `python/sglang/srt/server_args.py`:711; signals: fp4, nvfp4; excerpt: "petit nvfp4?" (https://github.com/sgl-project/sglang/pull/7302#discussion_r2189439862)
- `2025-07-07T09:06:49Z` `inline` by `HaiShaw` `python/sglang/srt/layers/quantization/petit_utils.py`:4; signals: fp4, nvfp4; excerpt: "mul nvfp4 a16?" (https://github.com/sgl-project/sglang/pull/7302#discussion_r2189440894)
- `2025-07-07T09:07:08Z` `review` `CHANGES_REQUESTED` by `HaiShaw`; signals: hang; excerpt: "Few more name changes?" (https://github.com/sgl-project/sglang/pull/7302#pullrequestreview-2992868006)
- `2025-07-07T09:09:57Z` `issue` by `HaiShaw`; signals: accuracy, fp8; excerpt: "@haohui there is 2+ points diff on nvfp8 mmlu accuracy compared with trtllm, do we have a way to triage further? Thanks." (https://github.com/sgl-project/sglang/pull/7302#issuecomment-3044103542)
- `2025-07-14T19:39:52Z` `issue` by `haohui`; signals: perf, performance; excerpt: "For full reproducibility, here are the commands to try out the PR: Command lines to compute the MMLU score on 8x MI300X: Command lines ..." (https://github.com/sgl-project/sglang/pull/7302#issuecomment-3070743998)
- `2025-07-17T18:03:48Z` `issue` by `HaiShaw`; signals: hang, kernel; excerpt: "@haohui petit kernel package works to both AMD and NV? @saienduri there is a change to pyproject, check CI please." (https://github.com/sgl-project/sglang/pull/7302#issuecomment-3084963774)
- `2025-06-18T06:40:14Z` `issue` by `haohui`; signals: fp4; excerpt: "I have tested the PR with MMLU on the AMD MI300x platform. The [Llama-3.3-70B-Instruct]( / [Llama-3.3-70B-Instruct-FP4]( model gets MMLU scores of 82.22 and 78.88 ..." (https://github.com/sgl-project/sglang/pull/7302#issuecomment-2982882621)
