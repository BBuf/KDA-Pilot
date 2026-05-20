# PR Discussion Digest

- Source PR: [vllm-project/vllm#22378](https://github.com/vllm-project/vllm/pull/22378)
- Source page: `sources/prs/vllm/PR-22378.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-22378`
- Generated at: `2026-05-20T15:37:03.242292+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-06T17:50:01Z`
- Merged: `2025-08-07T01:07:41Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 17 (approved=1, commented=16)
- Inline review comments: 18
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=6, outdated=3
- Human participants with discussion text: IwakuraRein, WoosukKwon, elvischenv, mergify, mgoin, pavanimajety, yewentao256, zyongye
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-08-06T17:51:56Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the environment variables for enabling TRT-LLM attention and adds support for attention ... (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3093656018)
- `2025-08-06T18:21:44Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3093736691)
- `2025-08-06T18:51:32Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3093821731)
- `2025-08-06T18:52:27Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3093824597)
- `2025-08-06T20:04:50Z` `COMMENTED` by `IwakuraRein` (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3094060212)
- `2025-08-06T20:44:40Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3094212875)
- `2025-08-06T21:06:44Z` `COMMENTED` by `yewentao256` - Do we need to have a quick fix for this bug? @mgoin , now triggers everywhere (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3094286432)
- `2025-08-06T21:31:22Z` `COMMENTED` by `IwakuraRein` (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3094376406)
- `2025-08-06T23:44:28Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3094633699)
- `2025-08-06T23:51:55Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3094652859)
- `2025-08-06T23:58:22Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3094660758)
- `2025-08-07T00:07:26Z` `COMMENTED` by `IwakuraRein` (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3094674454)
- `2025-08-07T00:24:23Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3094694789)
- `2025-08-07T00:29:25Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3094701588)
- `2025-08-07T00:48:10Z` `COMMENTED` by `IwakuraRein` (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3094721268)
- `2025-08-07T01:07:31Z` `APPROVED` by `WoosukKwon` - thanks so much! (https://github.com/vllm-project/vllm/pull/22378#pullrequestreview-3094745674)

## Inline Comment Hotspots

- `vllm/envs.py`: 10 inline comment(s)
- `vllm/v1/attention/backends/flashinfer.py`: 5 inline comment(s)
- `vllm/utils/flashinfer.py`: 2 inline comment(s)
- `vllm/model_executor/models/gpt_oss.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-06T23:51:55Z` `inline` by `elvischenv` `vllm/v1/attention/backends/flashinfer.py`:528; signals: attention, cache, flashinfer, fp8, kernel, kv cache; excerpt: "Prefill kernel is not supported for fp8 kv cache so I added this line. Could you double check?" (https://github.com/vllm-project/vllm/pull/22378#discussion_r2258556817)
- `2025-08-06T23:58:22Z` `inline` by `elvischenv` `vllm/envs.py`:1047; signals: attention, hang; excerpt: "Since envs.VLLM USE TRTLLM ATTENTION is always set to true or false, the else part will never go into. But for other changes in ..." (https://github.com/vllm-project/vllm/pull/22378#discussion_r2258563324)
- `2025-08-06T20:44:30Z` `inline` by `mgoin` `vllm/v1/attention/backends/flashinfer.py`:842; signals: attention, flashinfer; excerpt: "Does this require a flashinfer version upgrade? For instance 0.2.10?" (https://github.com/vllm-project/vllm/pull/22378#discussion_r2258256002)
- `2025-08-06T21:31:22Z` `inline` by `IwakuraRein` `vllm/v1/attention/backends/flashinfer.py`:842; signals: attention, flashinfer; excerpt: "Yes. 0.2.10" (https://github.com/vllm-project/vllm/pull/22378#discussion_r2258357328)
- `2025-08-07T00:48:10Z` `inline` by `IwakuraRein` `vllm/v1/attention/backends/flashinfer.py`:528; signals: attention, flashinfer; excerpt: "It's in flashinfer's [unit test]( so it should be supported" (https://github.com/vllm-project/vllm/pull/22378#discussion_r2258609264)
- `2025-08-06T18:51:32Z` `inline` by `pavanimajety` `vllm/envs.py`:155; signals: attention; excerpt: "What is the default behavior for the environment variable now? Do we automatically opt into TRTLLM attention when possible? If we need to set ..." (https://github.com/vllm-project/vllm/pull/22378#discussion_r2258004993)
- `2025-08-06T18:52:27Z` `inline` by `pavanimajety` `vllm/utils/flashinfer.py`:162; signals: flashinfer; excerpt: "Is this safe to do? Are decode cubins updated to remove the head size restrictions and head group ratios?" (https://github.com/vllm-project/vllm/pull/22378#discussion_r2258006770)
- `2025-08-06T23:44:28Z` `inline` by `elvischenv` `vllm/envs.py`:1047; signals: attention; excerpt: "If we want to recover to the original behavior, we should use lambda: os.getenv("VLLM USE TRTLLM ATTENTION", None), cc @pavanimajety" (https://github.com/vllm-project/vllm/pull/22378#discussion_r2258543144)
- `2025-08-07T00:07:26Z` `inline` by `IwakuraRein` `vllm/envs.py`:1047; signals: attention; excerpt: "Thanks for catching this. Shouldn't we update if env value is not None: to if envs.VLLM USE TRTLLM ATTENTION then?" (https://github.com/vllm-project/vllm/pull/22378#discussion_r2258572556)
- `2025-08-07T00:29:25Z` `inline` by `elvischenv` `vllm/envs.py`:1047; signals: attention; excerpt: "This may require re-design for the number of states for the env. If we want to keep ternary states for the env, then we ..." (https://github.com/vllm-project/vllm/pull/22378#discussion_r2258593715)
- `2025-08-06T20:04:48Z` `inline` by `IwakuraRein` `vllm/utils/flashinfer.py`:162; signals: flashinfer; excerpt: "I think so as our e2e test passed." (https://github.com/vllm-project/vllm/pull/22378#discussion_r2258163769)
- `2025-08-06T20:43:16Z` `inline` by `mgoin` `vllm/envs.py`:155; signals: hang; excerpt: "We should fix the env var def to be boolean, I commented the change" (https://github.com/vllm-project/vllm/pull/22378#discussion_r2258252869)
