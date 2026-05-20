# PR Discussion Digest

- Source PR: [vllm-project/vllm#13167](https://github.com/vllm-project/vllm/pull/13167)
- Source page: `sources/prs/vllm/PR-13167.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-13167`
- Generated at: `2026-05-20T15:33:58.479678+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete via REST overflow fallback`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-12T16:49:18Z`
- Merged: `2025-02-27T10:08:35Z`

## Discussion Counts

- Issue comments: 106
- Review submissions: 19 (approved=2, commented=17)
- Inline review comments: 22
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=6, outdated=10
- Human participants with discussion text: ChuanhongLi, Isotr0py, SzymonOzog, ZinonDynn, boywuxu, chuangzhidan, cjackal, davidsyoung, fclearner, hahmad2008, huang-junhong, hyunwen, iehgit, irdbl, joshuakoh1, junuMoon, justinjja, kechengcode, leolmj, lv03
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 58

## Review Decisions

- `2025-02-13T03:42:22Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2613735936)
- `2025-02-13T09:41:28Z` `COMMENTED` by `SzymonOzog` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2614425764)
- `2025-02-13T09:50:09Z` `COMMENTED` by `SzymonOzog` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2614448772)
- `2025-02-13T10:21:39Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2614532886)
- `2025-02-13T12:54:32Z` `COMMENTED` by `SzymonOzog` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2614896444)
- `2025-02-18T05:33:58Z` `APPROVED` by `huang-junhong` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2622488346)
- `2025-02-20T06:44:10Z` `COMMENTED` by `Isotr0py` - @SzymonOzog Sorry for the delay! R1 is too large for me to evaluate the model perplexity. 😓 Since ... (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2628818847)
- `2025-02-20T06:54:04Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2628862028)
- `2025-02-21T14:43:16Z` `COMMENTED` by `SzymonOzog` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2633255330)
- `2025-02-21T14:43:24Z` `COMMENTED` by `SzymonOzog` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2633255703)
- `2025-02-24T16:13:04Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2637681633)
- `2025-02-25T13:57:10Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2641158249)
- `2025-02-25T14:30:45Z` `COMMENTED` by `SzymonOzog` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2641299304)
- `2025-02-25T14:55:03Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2641393898)
- `2025-02-25T15:35:23Z` `APPROVED` by `Isotr0py` - The model evaluation results look reasonable to me. We can merge it once the cleanup for dtype check ... (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2641535389)
- `2025-02-26T09:45:05Z` `COMMENTED` by `SzymonOzog` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2643820540)
- `2025-02-26T09:45:20Z` `COMMENTED` by `SzymonOzog` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2643821182)
- `2025-02-26T14:42:33Z` `COMMENTED` by `cjackal` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2644758874)
- `2025-02-26T18:01:42Z` `COMMENTED` by `SzymonOzog` (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2645382200)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/gguf.py`: 9 inline comment(s)
- `vllm/config.py`: 5 inline comment(s)
- `vllm/model_executor/model_loader/loader.py`: 4 inline comment(s)
- `vllm/engine/arg_utils.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-02-19T09:32:58Z` `issue` by `davidsyoung`; signals: benchmark, cute, perf, performance; excerpt: "@SzymonOzog thanks for your valuable suggestions. I install the vllm from deepseek-gguf branch from [your vllm repo]( And successfully execute DeepSeek-R1-UD-IQ1 S in 4 ..." (https://github.com/vllm-project/vllm/pull/13167#issuecomment-2668051423)
- `2025-02-19T13:10:28Z` `issue` by `junuMoon`; signals: cache, kv cache, memory, throughput; excerpt: "@zh-jp Did you test the speed compared with the llama.cpp? And how much memory does it need at least? INFO 02-19 22:08:59 metrics.py:455] Avg ..." (https://github.com/vllm-project/vllm/pull/13167#issuecomment-2668612296)
- `2025-02-24T15:02:05Z` `issue` by `SzymonOzog`; signals: compile, kernel, moe; excerpt: "@fclearner Hey Alan, if you're eager to try to get it to run fast you could try checking out the branch where I'm working ..." (https://github.com/vllm-project/vllm/pull/13167#issuecomment-2678725578)
- `2025-02-25T05:46:46Z` `issue` by `fclearner`; signals: compile, kernel, moe; excerpt: "@fclearner Hey Alan, if you're eager to try to get it to run fast you could try checking out the branch where I'm working ..." (https://github.com/vllm-project/vllm/pull/13167#issuecomment-2680663962)
- `2025-02-25T13:56:45Z` `inline` by `Isotr0py` `vllm/model_executor/layers/quantization/gguf.py`:209; signals: block, kernel; excerpt: "Any reason to add this strict assertion here? I think there should be no block size limitation here since we will do padding in ..." (https://github.com/vllm-project/vllm/pull/13167#discussion_r1969834991)
- `2025-02-26T09:45:05Z` `inline` by `SzymonOzog` `vllm/model_executor/layers/quantization/gguf.py`:209; signals: block, kernel; excerpt: "Removed the assertion for now, can confirm that I get reasonable outputs for block size of 256, might have ran the code against my ..." (https://github.com/vllm-project/vllm/pull/13167#discussion_r1971266513)
- `2025-02-20T06:44:10Z` `review` `COMMENTED` by `Isotr0py`; signals: accuracy; excerpt: "@SzymonOzog Sorry for the delay! R1 is too large for me to evaluate the model perplexity. 😓 Since deepseek-v2 and v3 using same architecture ..." (https://github.com/vllm-project/vllm/pull/13167#pullrequestreview-2628818847)
- `2025-02-14T02:51:43Z` `issue` by `chuangzhidan`; signals: cuda, race; excerpt: "met an error： (base) ubuntu@localhost:/media/data/scripts$ python start gguf.py INFO 02-14 10:44:20 init .py:190] Automatically detected platform cuda. Traceback (most recent call last): File "/media/data/xgp/scripts/start ..." (https://github.com/vllm-project/vllm/pull/13167#issuecomment-2658147275)
- `2025-02-18T16:27:26Z` `issue` by `SzymonOzog`; signals: dtype, hang; excerpt: "@zh-jp You also need to change your dtype in config from bfloat16 to float16. Also could you check out this PR and run it ..." (https://github.com/vllm-project/vllm/pull/13167#issuecomment-2666221477)
- `2025-02-19T16:30:10Z` `issue` by `SzymonOzog`; signals: compile, hang; excerpt: "@leolmj There were no changes to compiled files so you shoud be able to run with the wheel from the main branch VLLM USE ..." (https://github.com/vllm-project/vllm/pull/13167#issuecomment-2669157115)
- `2025-02-21T14:45:31Z` `issue` by `SzymonOzog`; signals: dtype, hang; excerpt: "@Isotr0py No worries, just incorporated the feedback and also added some asserts and removed the need to change dtype manually. I tried running lm ..." (https://github.com/vllm-project/vllm/pull/13167#issuecomment-2674741558)
- `2025-02-21T14:48:11Z` `issue` by `SzymonOzog`; signals: kernel, moe; excerpt: "Also FYI got a working version of fused moe kernel for gguf. I'll write necessary test and clean this up so expect an PR ..." (https://github.com/vllm-project/vllm/pull/13167#issuecomment-2674747962)
