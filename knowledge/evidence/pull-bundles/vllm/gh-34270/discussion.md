# PR Discussion Digest

- Source PR: [vllm-project/vllm#34270](https://github.com/vllm-project/vllm/pull/34270)
- Source page: `sources/prs/vllm/PR-34270.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-34270`
- Generated at: `2026-05-20T15:39:47.260183+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-10T19:14:54Z`
- Merged: `2026-02-25T21:33:42Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 13 (approved=2, commented=11)
- Inline review comments: 9
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: elizabetht, mgoin, tlrmchlsmth, varun-sundar-rabindranath
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2026-02-10T19:17:29Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a critical bug where the monolithic TRITON backend for MXFP4 MoE would ... (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3781021117)
- `2026-02-13T01:40:45Z` `COMMENTED` by `tlrmchlsmth` - When I tried this out on an MI300X machine I hit the following: vllm serve --data-parallel-size 2 --enable-expert-parallel ... (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3794620153)
- `2026-02-13T18:43:23Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3798872151)
- `2026-02-13T19:11:26Z` `COMMENTED` by `elizabetht` (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3799012529)
- `2026-02-17T17:08:36Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3815184396)
- `2026-02-21T04:34:03Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3835037331)
- `2026-02-23T19:00:28Z` `COMMENTED` by `elizabetht` (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3842948501)
- `2026-02-23T19:38:32Z` `COMMENTED` by `elizabetht` (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3843130028)
- `2026-02-23T19:40:31Z` `COMMENTED` by `elizabetht` (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3843139426)
- `2026-02-25T04:39:38Z` `APPROVED` by `varun-sundar-rabindranath` - LGTM ! Tested on an H100 that vllm serve openai/gpt-oss-20b -dp=2 -ep --port 9010 and vllm serve openai/gpt-oss-20b ... (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3851800011)
- `2026-02-25T16:11:59Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3855261004)
- `2026-02-25T16:23:55Z` `APPROVED` by `mgoin` - Ran a local eval with EPDP and it works fine, thanks! (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3855345081)

## Inline Comment Hotspots

- `tests/kernels/quantization/test_mxfp4_triton_ep.py`: 7 inline comment(s)
- `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-02-13T18:43:23Z` `inline` by `varun-sundar-rabindranath` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:195; signals: h100, hang, kernel, moe, triton; excerpt: "Hey @elizabetht - I tried this PR on an H100 and I ran into topk ids = expert map[sparse logits.indx.to(torch.long)] fixed it for me. ..." (https://github.com/vllm-project/vllm/pull/34270#discussion_r2805586393)
- `2026-02-25T16:09:05Z` `inline` by `mgoin` `tests/kernels/quantization/test_mxfp4_triton_ep.py`:104; signals: fp4, kernel, moe, mxfp4, triton; excerpt: "Honestly I don't know how useful all this mocked logic is, especially since we are actively refactoring the mxfp4 moe. It would be better ..." (https://github.com/vllm-project/vllm/pull/34270#discussion_r2853960449)
- `2026-02-17T17:08:37Z` `inline` by `varun-sundar-rabindranath` `tests/kernels/quantization/test_mxfp4_triton_ep.py`:104; signals: fp4, h100, kernel, mxfp4, triton; excerpt: "@elizabetht This test doesn't pass for me on H100. Can you fix it by" (https://github.com/vllm-project/vllm/pull/34270#discussion_r2818099924)
- `2026-02-23T19:40:30Z` `inline` by `elizabetht` `tests/kernels/quantization/test_mxfp4_triton_ep.py`:104; signals: cuda, fp4, kernel, mxfp4, triton; excerpt: "Had a minor tweak to conditionally set device as "cuda" if torch.cuda is available." (https://github.com/vllm-project/vllm/pull/34270#discussion_r2842724730)
- `2026-02-21T04:34:03Z` `inline` by `varun-sundar-rabindranath` `tests/kernels/quantization/test_mxfp4_triton_ep.py`:104; signals: fp4, kernel, mxfp4, triton; excerpt: "bump" (https://github.com/vllm-project/vllm/pull/34270#discussion_r2835818615)
- `2026-02-23T19:00:28Z` `inline` by `elizabetht` `tests/kernels/quantization/test_mxfp4_triton_ep.py`:104; signals: fp4, kernel, mxfp4, triton; excerpt: "Working on it now!" (https://github.com/vllm-project/vllm/pull/34270#discussion_r2842546405)
- `2026-02-23T19:38:32Z` `inline` by `elizabetht` `tests/kernels/quantization/test_mxfp4_triton_ep.py`:104; signals: fp4, kernel, mxfp4, triton; excerpt: "@varun-sundar-rabindranath Could you check now?" (https://github.com/vllm-project/vllm/pull/34270#discussion_r2842716306)
- `2026-02-13T19:11:26Z` `inline` by `elizabetht` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:195; signals: kernel, moe, triton; excerpt: "Sure, thanks for the pointer @varun-sundar-rabindranath - will update my PR!" (https://github.com/vllm-project/vllm/pull/34270#discussion_r2805690882)
- `2026-02-13T18:49:01Z` `issue` by `varun-sundar-rabindranath`; signals: h100, h200, triton; excerpt: "Thanks for working on this issue @elizabetht , however this seems to cause an issue since the triton backend doesn't have an impl in ..." (https://github.com/vllm-project/vllm/pull/34270#issuecomment-3898796444)
- `2026-02-10T19:57:00Z` `issue` by `mgoin`; signals: h200, triton; excerpt: "Thanks for working on this issue @elizabetht , however this seems to cause an issue since the triton backend doesn't have an impl in ..." (https://github.com/vllm-project/vllm/pull/34270#issuecomment-3880379452)
- `2026-02-13T01:40:45Z` `review` `COMMENTED` by `tlrmchlsmth`; signals: general review; excerpt: "When I tried this out on an MI300X machine I hit the following: vllm serve --data-parallel-size 2 --enable-expert-parallel openai/gpt-oss-120b" (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3794620153)
- `2026-02-25T04:39:38Z` `review` `APPROVED` by `varun-sundar-rabindranath`; signals: h100; excerpt: "LGTM ! Tested on an H100 that vllm serve openai/gpt-oss-20b -dp=2 -ep --port 9010 and vllm serve openai/gpt-oss-20b -tp=2 -ep --port 9010. Thanks @elizabetht ..." (https://github.com/vllm-project/vllm/pull/34270#pullrequestreview-3851800011)
