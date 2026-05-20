# PR Discussion Digest

- Source PR: [vllm-project/vllm#17751](https://github.com/vllm-project/vllm/pull/17751)
- Source page: `sources/prs/vllm/PR-17751.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-17751`
- Generated at: `2026-05-20T15:35:12.615837+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-06T23:17:37Z`
- Merged: `2025-05-12T16:46:16Z`

## Discussion Counts

- Issue comments: 20
- Review submissions: 22 (approved=1, commented=21)
- Inline review comments: 27
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=11, outdated=9
- Human participants with discussion text: ApostaC, AsicDyc, LCAIZJ, WoosukKwon, axxx03, david6666666, heheda12345, khuonglm, kouroshHakha, mergify, new-TonyWang, njhill, ptarasiewiczNV, robertgshaw2-redhat, tlrmchlsmth, zhaohaidao, zzh142857
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 12

## Review Decisions

- `2025-05-07T01:13:42Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2820080498)
- `2025-05-08T14:30:16Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2825345991)
- `2025-05-08T16:20:36Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2825702924)
- `2025-05-08T17:37:51Z` `COMMENTED` by `ApostaC` - Thanks @robertgshaw2-redhat Seems we have a lot of changes here. Just wanted to make sure it does not ... (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2825892307)
- `2025-05-09T14:17:49Z` `COMMENTED` by `ptarasiewiczNV` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2828532866)
- `2025-05-09T14:37:19Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2828596559)
- `2025-05-09T14:41:43Z` `COMMENTED` by `ptarasiewiczNV` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2828614216)
- `2025-05-09T14:42:42Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2828618347)
- `2025-05-09T14:47:58Z` `COMMENTED` by `njhill` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2828637119)
- `2025-05-09T14:49:16Z` `COMMENTED` by `njhill` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2828640442)
- `2025-05-09T16:41:45Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2829032990)
- `2025-05-09T20:02:14Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2823715508)
- `2025-05-09T20:11:06Z` `COMMENTED` by `WoosukKwon` - Overall, I'm happy with the PR. Thanks for iterating over for the clean design. My two cents: 1. ... (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2829555671)
- `2025-05-09T20:13:43Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2829559704)
- `2025-05-09T21:19:30Z` `COMMENTED` by `njhill` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2829695827)
- `2025-05-09T21:21:26Z` `COMMENTED` by `njhill` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2829699160)
- `2025-05-09T21:22:53Z` `COMMENTED` by `njhill` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2829701340)
- `2025-05-09T21:25:53Z` `COMMENTED` by `njhill` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2829707022)
- `2025-05-10T14:29:49Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2830844552)
- `2025-05-10T18:35:10Z` `APPROVED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2831030027)
- `2025-05-12T16:20:46Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2833809667)

## Inline Comment Hotspots

- `vllm/v1/core/sched/scheduler.py`: 5 inline comment(s)
- `tests/v1/kv_connector/nixl_integration/toy_proxy_server.py`: 4 inline comment(s)
- `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`: 3 inline comment(s)
- `vllm/distributed/kv_transfer/kv_connector/v1/base.py`: 3 inline comment(s)
- `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_connector.py`: 3 inline comment(s)
- `vllm/v1/core/kv_cache_manager.py`: 3 inline comment(s)
- `vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py`: 3 inline comment(s)
- `vllm/envs.py`: 2 inline comment(s)
- `vllm/v1/request.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-05-08T17:37:51Z` `review` `COMMENTED` by `ApostaC`; signals: cache, hang, perf, performance; excerpt: "Thanks @robertgshaw2-redhat Seems we have a lot of changes here. Just wanted to make sure it does not break the old connector logic. Would ..." (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2825892307)
- `2025-05-09T20:11:06Z` `review` `COMMENTED` by `WoosukKwon`; signals: aligned, block, cache, kv cache; excerpt: "Overall, I'm happy with the PR. Thanks for iterating over for the clean design. My two cents: 1. I think we need a way ..." (https://github.com/vllm-project/vllm/pull/17751#pullrequestreview-2829555671)
- `2025-05-08T21:49:19Z` `issue` by `robertgshaw2-redhat`; signals: cache, hang, perf, performance; excerpt: "Thanks @robertgshaw2-redhat Seems we have a lot of changes here. Just wanted to make sure it does not break the old connector logic. Would ..." (https://github.com/vllm-project/vllm/pull/17751#issuecomment-2864411389)
- `2025-05-08T22:01:34Z` `issue` by `robertgshaw2-redhat`; signals: cache, hang, perf, performance; excerpt: "Thanks @robertgshaw2-redhat Seems we have a lot of changes here. Just wanted to make sure it does not break the old connector logic. Would ..." (https://github.com/vllm-project/vllm/pull/17751#issuecomment-2864530017)
- `2025-05-09T21:49:25Z` `issue` by `njhill`; signals: aligned, block, cache, kv cache; excerpt: "Thanks @WoosukKwon 1. I think we need a way to asynchronously load the KV cache across multiple scheduling step, which will be a followup ..." (https://github.com/vllm-project/vllm/pull/17751#issuecomment-2867943752)
- `2025-05-08T14:30:16Z` `inline` by `tlrmchlsmth` `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`:7; signals: accuracy, fp8, mla; excerpt: "This turns out to not actually have MLA very unfortunately -- maybe we go with mgoin/DeepSeek-Coder-V2-Lite-Instruct-FP8?" (https://github.com/vllm-project/vllm/pull/17751#discussion_r2079839524)
- `2025-05-10T01:12:40Z` `issue` by `WoosukKwon`; signals: cache, hang, kv cache; excerpt: "@njhill Isn't this already covered? The connector's get num new matched tokens now also returns a bool indicating whether the load is async or ..." (https://github.com/vllm-project/vllm/pull/17751#issuecomment-2868178676)
- `2025-05-10T14:48:27Z` `issue` by `robertgshaw2-redhat`; signals: cache, hang, kv cache; excerpt: "We'll probably need such a queue anyhow to keep track of requests for which take too long to finish (likely a set/dict rather than ..." (https://github.com/vllm-project/vllm/pull/17751#issuecomment-2868941257)
- `2025-05-07T01:13:41Z` `inline` by `tlrmchlsmth` `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`:6; signals: accuracy; excerpt: "Could you uncomment this? This one is my b" (https://github.com/vllm-project/vllm/pull/17751#discussion_r2076611077)
- `2025-05-08T16:20:36Z` `inline` by `robertgshaw2-redhat` `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`:7; signals: accuracy; excerpt: "in fup" (https://github.com/vllm-project/vllm/pull/17751#discussion_r2080053981)
- `2025-05-09T01:44:05Z` `inline` by `WoosukKwon` `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_connector.py`:108; signals: cache; excerpt: "Please add a comment on load kv async?" (https://github.com/vllm-project/vllm/pull/17751#discussion_r2080747366)
- `2025-05-09T02:21:52Z` `inline` by `WoosukKwon` `vllm/v1/core/sched/scheduler.py`:362; signals: hang; excerpt: "Why this change?" (https://github.com/vllm-project/vllm/pull/17751#discussion_r2080776740)
