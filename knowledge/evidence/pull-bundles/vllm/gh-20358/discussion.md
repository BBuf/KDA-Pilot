# PR Discussion Digest

- Source PR: [vllm-project/vllm#20358](https://github.com/vllm-project/vllm/pull/20358)
- Source page: `sources/prs/vllm/PR-20358.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-20358`
- Generated at: `2026-05-20T15:36:06.797394+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-02T07:18:42Z`
- Merged: `2025-08-29T10:57:35Z`

## Discussion Counts

- Issue comments: 58
- Review submissions: 30 (approved=1, commented=29)
- Inline review comments: 29
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=6, outdated=7
- Human participants with discussion text: DarkLight1337, ProExpertProg, cjackal, drdown33, elvischenv, hmellor, huydhn, jeejeelee, learning4life, lgeiger, mergify, mgoin, nWEIdia, simon-mo, tlrmchlsmth, vadimkantorov, youkaichao, zifeitong, zou3519
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 30

## Review Decisions

- `2025-07-02T07:19:14Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @huydhn, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-2978027458)
- `2025-07-02T07:20:17Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates PyTorch to version 2.8.0 and its related dependencies like torchvision, torchaudio, and ... (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-2978030278)
- `2025-07-15T19:27:00Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3022012532)
- `2025-07-16T00:20:40Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3022682091)
- `2025-07-16T00:59:26Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3022752150)
- `2025-07-16T15:09:08Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3025489474)
- `2025-07-16T18:31:14Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3026355124)
- `2025-07-16T18:35:05Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3026364905)
- `2025-07-16T21:58:19Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3027024439)
- `2025-07-17T20:45:57Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3030968336)
- `2025-08-06T17:57:34Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3093671205)
- `2025-08-06T18:45:14Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3093801297)
- `2025-08-06T18:46:41Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3093806317)
- `2025-08-06T23:06:54Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3094566375)
- `2025-08-06T23:56:21Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3094658484)
- `2025-08-07T01:07:31Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3094745665)
- `2025-08-10T19:48:58Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3103729213)
- `2025-08-10T20:06:22Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3103732424)
- `2025-08-11T21:17:52Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3107807432)
- `2025-08-13T01:20:44Z` `COMMENTED` by `zifeitong` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3113687828)
- `2025-08-13T01:59:35Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3113729547)
- `2025-08-13T02:16:23Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3113747046)
- `2025-08-26T22:33:54Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3157512162)
- `2025-08-27T00:02:16Z` `COMMENTED` by `huydhn` (https://github.com/vllm-project/vllm/pull/20358#pullrequestreview-3157700917)
- ... 6 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `docker/Dockerfile`: 11 inline comment(s)
- `tests/models/test_transformers.py`: 7 inline comment(s)
- `tests/distributed/test_sequence_parallel.py`: 5 inline comment(s)
- `tests/lora/test_chatglm3_tp.py`: 3 inline comment(s)
- `requirements/cuda.txt`: 2 inline comment(s)
- `.pre-commit-config.yaml`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-28T10:01:34Z` `inline` by `huydhn` `tests/models/test_transformers.py`:190; signals: attention, failing, oom, pipeline; excerpt: "@zou3519 @drisspg I'm pretty sure that the increase is either coming from or is partly due to it. Here is what I have been ..." (https://github.com/vllm-project/vllm/pull/20358#discussion_r2306907125)
- `2025-08-13T02:16:23Z` `inline` by `huydhn` `requirements/cuda.txt`:15; signals: block, cuda, hang; excerpt: "Keep this here would effectively block this change until xformers release a new package working with 2.8.0. I'm asking for the release timeline of ..." (https://github.com/vllm-project/vllm/pull/20358#discussion_r2271911807)
- `2025-08-26T22:33:53Z` `inline` by `huydhn` `tests/models/test_transformers.py`:190; signals: compile, hang, memory; excerpt: "I start to see a slight memory increase for jason9693/Qwen2.5-1.5B-apeach in 2.8 torch.compile, i.e. This must have come from a change(s) in the past ..." (https://github.com/vllm-project/vllm/pull/20358#discussion_r2302291962)
- `2025-08-26T02:07:37Z` `issue` by `huydhn`; signals: hang, kernel, moe; excerpt: "[Kernels MoE]( failures seem to come from @mgoin @simon-mo Should we force merge this change now or continue to wait for fixes and do ..." (https://github.com/vllm-project/vllm/pull/20358#issuecomment-3222315211)
- `2025-07-15T19:27:00Z` `inline` by `zou3519` `tests/distributed/test_sequence_parallel.py`:299; signals: fp8, sm90; excerpt: "@tlrmchlsmth @cascade812 @ProExpertProg upgrading to PyTorch 2.8 causes this test to fail with "FP8 reduction requires sm90 or higher". Is this expected?" (https://github.com/vllm-project/vllm/pull/20358#discussion_r2208473696)
- `2025-08-11T21:17:52Z` `inline` by `huydhn` `docker/Dockerfile`:387; signals: attention, cuda; excerpt: "Well, I'm encountering a build issue with xformers v0.0.31 or later and have cut an issue for the team at As the build failure ..." (https://github.com/vllm-project/vllm/pull/20358#discussion_r2268035970)
- `2025-08-13T01:20:44Z` `inline` by `zifeitong` `docker/Dockerfile`:387; signals: cuda, ptx; excerpt: "Limiting TORCH CUDA ARCH LIST for xformers build worked for me: xformers official wheel is built with TORCH CUDA ARCH LIST: 7.5 8.0+PTX 9.0a" (https://github.com/vllm-project/vllm/pull/20358#discussion_r2271859359)
- `2025-08-27T20:50:18Z` `inline` by `zou3519` `tests/models/test_transformers.py`:190; signals: kernel, triton; excerpt: "cc @BoyuanFeng it sounds like Inductor generated a triton kernel that doesn't work on L4 gpus because the machine type doesn't have enough sram" (https://github.com/vllm-project/vllm/pull/20358#discussion_r2305266528)
- `2025-07-16T00:20:40Z` `inline` by `ProExpertProg` `tests/distributed/test_sequence_parallel.py`:299; signals: fp8, hang; excerpt: "Huh, did something change in PyTorch around fp8 on sm89?" (https://github.com/vllm-project/vllm/pull/20358#discussion_r2208941940)
- `2025-08-13T06:59:51Z` `issue` by `huydhn`; signals: block, hang; excerpt: "What's the status of this PR? The change itself is ready to land with one condition that we need to build xformers from source ..." (https://github.com/vllm-project/vllm/pull/20358#issuecomment-3182426583)
- `2025-08-25T19:40:31Z` `issue` by `huydhn`; signals: hang, kernel; excerpt: "@zhewenl I'm seeing this new failure showing up where a bunch of libraries used by EP kernel needs to be uploaded to Ray pushing ..." (https://github.com/vllm-project/vllm/pull/20358#issuecomment-3221515897)
- `2025-07-16T18:31:14Z` `inline` by `huydhn` `tests/lora/test_chatglm3_tp.py`:100; signals: oom; excerpt: "I'm getting OOM when running this test on CI. It's unclear if it's related to 2.8 upgrade" (https://github.com/vllm-project/vllm/pull/20358#discussion_r2211262822)
