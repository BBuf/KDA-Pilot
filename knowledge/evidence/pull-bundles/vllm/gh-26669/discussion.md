# PR Discussion Digest

- Source PR: [vllm-project/vllm#26669](https://github.com/vllm-project/vllm/pull/26669)
- Source page: `sources/prs/vllm/PR-26669.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-26669`
- Generated at: `2026-05-20T15:38:08.233274+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-13T02:46:01Z`
- Merged: `2025-10-15T19:06:47Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 6 (approved=3, commented=3)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: BenasdTW, ReinForce-II, XiaobingSuper, jasl, mgoin, unknown, voipmonitor, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-13T02:47:52Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for flashinfer fp4 MoE on 5090 GPUs by enabling it for ... (https://github.com/vllm-project/vllm/pull/26669#pullrequestreview-3329855169)
- `2025-10-13T15:13:24Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! (https://github.com/vllm-project/vllm/pull/26669#pullrequestreview-3332024943)
- `2025-10-14T21:42:19Z` `COMMENTED` by `jasl` (https://github.com/vllm-project/vllm/pull/26669#pullrequestreview-3337608161)
- `2025-10-15T02:01:26Z` `COMMENTED` by `XiaobingSuper` (https://github.com/vllm-project/vllm/pull/26669#pullrequestreview-3338106489)
- `2025-10-15T02:38:12Z` `APPROVED` by `jasl` - Thank you! cc @johnnynunez (https://github.com/vllm-project/vllm/pull/26669#pullrequestreview-3338151128)
- `2025-10-15T16:54:57Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/26669#pullrequestreview-3341440673)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-10-15T02:02:39Z` `issue` by `unknown`; signals: fp4, fp8, nvfp4, perf, performance, tensorrt; excerpt: "the problem is that I got exactly the same speed in FP4 as FP8 which means native NVFP4 is not used. It must be ..." (https://github.com/vllm-project/vllm/pull/26669#issuecomment-3404243499)
- `2025-10-14T12:02:27Z` `issue` by `unknown`; signals: compile, cuda, cutlass, kernel, moe; excerpt: "Do you meet any errors? I get NotImplementedError: No compiled get cutlass moe mm data: no cutlass scaled mm kernel for CUDA device capability: ..." (https://github.com/vllm-project/vllm/pull/26669#issuecomment-3401447060)
- `2025-10-14T15:08:34Z` `issue` by `unknown`; signals: fp4, fp8, nvfp4, throughput; excerpt: "the biggest problem is that while it works for me, the speed is only 100 tokens/sec while the FP8 variant is 122 tokens/sec. This ..." (https://github.com/vllm-project/vllm/pull/26669#issuecomment-3402339218)
- `2025-10-14T16:43:08Z` `issue` by `voipmonitor`; signals: fp4, fp8, nvfp4, throughput; excerpt: "the biggest problem is that while it works for me, the speed is only 100 tokens/sec while the FP8 variant is 122 tokens/sec. This ..." (https://github.com/vllm-project/vllm/pull/26669#issuecomment-3402769201)
- `2025-10-14T21:42:19Z` `inline` by `jasl` `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`:35; signals: flashinfer, fp4, moe; excerpt: "Can you add 110 (Thor) and 121 (Spark)?" (https://github.com/vllm-project/vllm/pull/26669#discussion_r2430553357)
- `2025-10-15T02:01:26Z` `inline` by `XiaobingSuper` `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`:35; signals: flashinfer, fp4, moe; excerpt: "added." (https://github.com/vllm-project/vllm/pull/26669#discussion_r2430920816)
- `2025-10-15T16:54:53Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`:37; signals: flashinfer, fp4, moe; excerpt: "switching to has is sufficient here for greater than or equal" (https://github.com/vllm-project/vllm/pull/26669#discussion_r2433336817)
- `2025-10-14T15:05:54Z` `issue` by `voipmonitor`; signals: fp4, fp8, nvfp4; excerpt: "the biggest problem is that while it works for me, the speed is only 100 tokens/sec while the FP8 variant is 122 tokens/sec. This ..." (https://github.com/vllm-project/vllm/pull/26669#issuecomment-3402326529)
- `2025-10-14T15:06:52Z` `issue` by `unknown`; signals: compile, fp4, nvfp4; excerpt: "It is so strange, I also tested huggingface.co/NVFP4/Qwen3-30B-A3B-Instruct-2507-FP4, it works well in my side. Alright, I deleted my vllm folder and completely recompiled it. ..." (https://github.com/vllm-project/vllm/pull/26669#issuecomment-3402330823)
- `2025-10-14T15:12:26Z` `issue` by `BenasdTW`; signals: fp4, fp8, nvfp4; excerpt: "It is so strange, I also tested huggingface.co/NVFP4/Qwen3-30B-A3B-Instruct-2507-FP4, it works well in my side. It worked for me as well. I've tested the following ..." (https://github.com/vllm-project/vllm/pull/26669#issuecomment-3402359774)
- `2025-10-15T02:48:46Z` `issue` by `unknown`; signals: fp4, nvfp4, tensorrt; excerpt: "I tested it again and this time I looked at the response content. It responses nonsense sometimes, and sometimes it loops forever. It's prompt ..." (https://github.com/vllm-project/vllm/pull/26669#issuecomment-3404314623)
- `2025-10-15T03:09:55Z` `issue` by `ReinForce-II`; signals: fp4, fp8, nvfp4; excerpt: "the problem is that I got exactly the same speed in FP4 as FP8 which means native NVFP4 is not used. It must be ..." (https://github.com/vllm-project/vllm/pull/26669#issuecomment-3404345218)
