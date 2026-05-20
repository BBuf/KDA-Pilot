# PR Discussion Digest

- Source PR: [vllm-project/vllm#12721](https://github.com/vllm-project/vllm/pull/12721)
- Source page: `sources/prs/vllm/PR-12721.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-12721`
- Generated at: `2026-05-20T15:33:51.869523+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-04T01:44:29Z`
- Merged: `2025-03-14T20:58:30Z`

## Discussion Counts

- Issue comments: 44
- Review submissions: 6 (approved=3, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: DarkLight1337, LouisCastricato, ProExpertProg, SinanTokmak, bigPYJ1151, bnellnm, fialhocoelho, hmellor, houseroad, jamesbraza, jeejeelee, jiangshaoping, mergify, mgoin, simon-mo, tiran, tlrmchlsmth, xihuai18, youkaichao, zhouyuan
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 6

## Review Decisions

- `2025-02-04T03:20:16Z` `APPROVED` by `zhuohan123` (https://github.com/vllm-project/vllm/pull/12721#pullrequestreview-2591623186)
- `2025-02-04T03:44:16Z` `APPROVED` by `tlrmchlsmth` - Nice, CI looks green (https://github.com/vllm-project/vllm/pull/12721#pullrequestreview-2591645055)
- `2025-02-04T05:03:53Z` `APPROVED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/12721#pullrequestreview-2591745571)
- `2025-02-04T14:28:34Z` `COMMENTED` by `fialhocoelho` - LGTM. I built vLLM by merging this PR, and it worked perfectly 🚀 (https://github.com/vllm-project/vllm/pull/12721#pullrequestreview-2593039859)
- `2025-02-25T22:53:49Z` `COMMENTED` by `jamesbraza` (https://github.com/vllm-project/vllm/pull/12721#pullrequestreview-2642645634)
- `2025-02-28T11:40:47Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/12721#pullrequestreview-2650508344)

## Inline Comment Hotspots

- `requirements-build.txt`: 2 inline comment(s)

## High-Signal Discussion

- `2025-02-17T23:22:58Z` `issue` by `mgoin`; signals: compile, correctness, flashinfer, kernel, oom; excerpt: "I kicked off a manual build here There are a lot of test failures that seem real and worth looking into. I am rebuilding ..." (https://github.com/vllm-project/vllm/pull/12721#issuecomment-2664219656)
- `2025-02-26T03:40:02Z` `issue` by `zou3519`; signals: compile, failing, perf; excerpt: "Some kind of failure due to marlin view code I know what the bug here is ( trying to figure out what the best ..." (https://github.com/vllm-project/vllm/pull/12721#issuecomment-2683815292)
- `2025-02-04T14:28:34Z` `review` `COMMENTED` by `fialhocoelho`; signals: perf; excerpt: "LGTM. I built vLLM by merging this PR, and it worked perfectly 🚀" (https://github.com/vllm-project/vllm/pull/12721#pullrequestreview-2593039859)
- `2025-02-18T16:03:27Z` `issue` by `tlrmchlsmth`; signals: compile, cutlass; excerpt: "[2025-02-17T21:45:47Z] torch.ops. C.cutlass scaled mm.default(buf5, buf1, buf6, arg4 1, arg6 1, None) [2025-02-17T21:45:47Z] File "/usr/local/lib/python3.12/dist-packages/torch/ ops.py", line 723, in call [2025-02-17T21:45:47Z] return self. op( ..." (https://github.com/vllm-project/vllm/pull/12721#issuecomment-2666157427)
- `2025-02-25T19:13:55Z` `issue` by `zou3519`; signals: cutlass, hang; excerpt: "If cutlass scaled mm is a custom op then it's possible inductor changed the strides to the input for it. Is it possible to ..." (https://github.com/vllm-project/vllm/pull/12721#issuecomment-2683025328)
- `2025-02-18T05:05:27Z` `issue` by `youkaichao`; signals: cutlass; excerpt: "PyTorch Fullgraph Test fails with a few unhelpful messages RuntimeError: Expected b.stride(0) == 1 to be true, but got false. (Could this error message ..." (https://github.com/vllm-project/vllm/pull/12721#issuecomment-2664618203)
- `2025-02-23T17:29:24Z` `issue` by `LouisCastricato`; signals: cutlass; excerpt: "Hey! I wanted to know the process here for building locally @mgoin -- when I attempt to do so I get a bunch of ..." (https://github.com/vllm-project/vllm/pull/12721#issuecomment-2676999545)
- `2025-02-24T19:28:52Z` `issue` by `ProExpertProg`; signals: hang; excerpt: "Btw, Pytorch [updated the auto-functionalization]( which I think will break our custom fusion passes. So we should disable it, there's an inductor config field ..." (https://github.com/vllm-project/vllm/pull/12721#issuecomment-2679449916)
- `2025-02-24T20:13:29Z` `issue` by `bnellnm`; signals: hang; excerpt: "Btw, Pytorch [updated the auto-functionalization]( which I think will break our custom fusion passes. So we should disable it, there's an inductor config field ..." (https://github.com/vllm-project/vllm/pull/12721#issuecomment-2679541075)
- `2025-02-25T20:47:53Z` `issue` by `tlrmchlsmth`; signals: hang; excerpt: "@zou3519 yes and thanks for taking a look! Here is one setting TORCH LOGS=+inductor [scaled mm torch 2.6.log]( This is the repro: Is there ..." (https://github.com/vllm-project/vllm/pull/12721#issuecomment-2683249694)
- `2025-02-26T02:08:51Z` `issue` by `zou3519`; signals: hang; excerpt: "@zou3519 yes and thanks for taking a look! Here is one setting TORCH LOGS=+inductor [scaled mm torch 2.6.log]( This is the repro: Is there ..." (https://github.com/vllm-project/vllm/pull/12721#issuecomment-2683711678)
- `2025-02-26T04:06:40Z` `issue` by `ProExpertProg`; signals: compile; excerpt: "In terms of tests, once we disable V2 like mentioned [here]( all tests in tests/compile/ are torch.compile related." (https://github.com/vllm-project/vllm/pull/12721#issuecomment-2683841919)
