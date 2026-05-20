# PR Discussion Digest

- Source PR: [vllm-project/vllm#34871](https://github.com/vllm-project/vllm/pull/34871)
- Source page: `sources/prs/vllm/PR-34871.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-34871`
- Generated at: `2026-05-20T15:39:55.007803+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-19T04:22:32Z`
- Merged: `2026-03-16T09:30:24Z`

## Discussion Counts

- Issue comments: 23
- Review submissions: 4 (approved=3, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: DarkLight1337, LucasWilkinson, ZJY0516, blancsw, cjackal, haosdent, open17777, peakcrosser7, tdoublep, vadiklyutiy
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-02-19T04:24:00Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request effectively addresses the crash in the GDN attention backend by reclassifying regular decodes ... (https://github.com/vllm-project/vllm/pull/34871#pullrequestreview-3823442648)
- `2026-02-23T17:10:28Z` `APPROVED` by `LucasWilkinson` - LGTM, thanks for the fix :+1: (https://github.com/vllm-project/vllm/pull/34871#pullrequestreview-3842382411)
- `2026-02-26T19:25:32Z` `APPROVED` by `vadiklyutiy` - Second the motion! (https://github.com/vllm-project/vllm/pull/34871#pullrequestreview-3863111423)
- `2026-03-16T09:29:45Z` `APPROVED` by `tdoublep` - LGTM (https://github.com/vllm-project/vllm/pull/34871#pullrequestreview-3952500649)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-02-23T17:21:31Z` `issue` by `LucasWilkinson`; signals: blackwell, correctness, fp4, nvfp4; excerpt: "can you please ensure pytest -s -v tests/evals/gsm8k/test gsm8k correctness.py -k "Qwen3-Next-80B-A3B-NVFP4-EP2" --config-list-file=tests/evals/gsm8k/configs/models-blackwell.txt passes?" (https://github.com/vllm-project/vllm/pull/34871#issuecomment-3946142013)
- `2026-02-24T02:19:07Z` `issue` by `haosdent`; signals: blackwell, correctness, fp4, nvfp4; excerpt: "can you please ensure pytest -s -v tests/evals/gsm8k/test gsm8k correctness.py -k "Qwen3-Next-80B-A3B-NVFP4-EP2" --config-list-file=tests/evals/gsm8k/configs/models-blackwell.txt passes? Let me try it" (https://github.com/vllm-project/vllm/pull/34871#issuecomment-3948502121)
- `2026-03-14T10:02:54Z` `issue` by `blancsw`; signals: fp8, h200, perf; excerpt: "Thanks, @haosdent , for the fix. Your support has been invaluable to us at Infomaniak during our deployment of Qwen/Qwen3.5-397B-A17B-FP8. I can confirm that ..." (https://github.com/vllm-project/vllm/pull/34871#issuecomment-4060200711)
- `2026-02-20T09:39:04Z` `issue` by `haosdent`; signals: cute; excerpt: "I checked this call chain schedule() - update after schedule() - execute model () - post step() - update draft token ids(), and try ..." (https://github.com/vllm-project/vllm/pull/34871#issuecomment-3932691125)
- `2026-02-20T16:19:32Z` `issue` by `peakcrosser7`; signals: correctness; excerpt: "Hi @haosdent . Thanks for the explanation! I’m not particularly familiar with GDNMetadata and I believe your fix can resolve the issue. I’m just ..." (https://github.com/vllm-project/vllm/pull/34871#issuecomment-3935842968)
- `2026-03-14T11:14:48Z` `issue` by `haosdent`; signals: nan; excerpt: "@vadiklyutiy @MatthewBonanni May you help to review again when you are available? Thank you in advance!" (https://github.com/vllm-project/vllm/pull/34871#issuecomment-4060302857)
- `2026-02-24T12:19:23Z` `issue` by `DarkLight1337`; signals: block; excerpt: "Unblocking the test" (https://github.com/vllm-project/vllm/pull/34871#issuecomment-3951366695)
- `2026-02-20T08:24:24Z` `issue` by `peakcrosser7`; signals: general review; excerpt: "Hi @haosdent . Just a bit confused about the decode phase. When MTP is enabled, is the first decode step a regular one (query ..." (https://github.com/vllm-project/vllm/pull/34871#issuecomment-3932375339)
- `2026-02-20T09:40:24Z` `issue` by `haosdent`; signals: general review; excerpt: "But I agree this patch is a bit hacky, let me think if there is a better way to address this. Also any suggestions ..." (https://github.com/vllm-project/vllm/pull/34871#issuecomment-3932698762)
- `2026-02-20T12:32:30Z` `issue` by `haosdent`; signals: general review; excerpt: "Hi, @peakcrosser7, Thanks for your comment. I have simplified the patch. Could you help review it again when you are available? Thank you in ..." (https://github.com/vllm-project/vllm/pull/34871#issuecomment-3933997851)
- `2026-02-21T10:52:23Z` `issue` by `cjackal`; signals: general review; excerpt: "Seems like 34999 is fixing the same issue (except the new unit tests) by just removing the assertion, FYI" (https://github.com/vllm-project/vllm/pull/34871#issuecomment-3938600101)
- `2026-02-23T02:29:18Z` `issue` by `haosdent`; signals: general review; excerpt: "why the first decode step behaves differently. @peakcrosser7 Thanks for your comment. As I saw in the code, the first decode step doesn't have ..." (https://github.com/vllm-project/vllm/pull/34871#issuecomment-3942202967)
