# PR Discussion Digest

- Source PR: [vllm-project/vllm#14323](https://github.com/vllm-project/vllm/pull/14323)
- Source page: `sources/prs/vllm/PR-14323.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14323`
- Generated at: `2026-05-20T15:34:23.985084+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-06T03:10:33Z`
- Merged: `2025-04-16T02:31:30Z`

## Discussion Counts

- Issue comments: 22
- Review submissions: 26 (approved=1, commented=25)
- Inline review comments: 33
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=8, outdated=11
- Human participants with discussion text: Alnusjaponica, DarkLight1337, mergify, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-03-19T15:09:26Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2698898437)
- `2025-03-19T15:10:11Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2698901000)
- `2025-03-19T15:10:51Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2698903154)
- `2025-03-19T17:58:05Z` `COMMENTED` by `tlrmchlsmth` - Thanks for the contribution! I left some comments - Ideally we should directly use MambaMixer2 to avoid code ... (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2699496642)
- `2025-03-20T03:38:05Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2701092773)
- `2025-03-20T03:40:32Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2701094952)
- `2025-03-21T05:46:04Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2704794217)
- `2025-03-21T06:02:45Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2704818997)
- `2025-03-21T06:06:36Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2704829190)
- `2025-03-24T01:59:55Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2708946360)
- `2025-03-24T02:24:28Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2708974189)
- `2025-03-24T02:25:08Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2708974717)
- `2025-03-24T02:27:16Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2708976373)
- `2025-03-24T18:12:37Z` `COMMENTED` by `tlrmchlsmth` - I'm not getting any output generated from following simple script (on an H100). Could you take a look? (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2711286347)
- `2025-03-24T18:14:36Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2711314140)
- `2025-03-25T05:41:13Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2712440232)
- `2025-03-25T05:57:57Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2712466890)
- `2025-03-25T06:15:07Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2712496732)
- `2025-03-27T07:55:13Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2720184540)
- `2025-03-31T13:57:32Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2729399303)
- `2025-04-01T11:03:22Z` `COMMENTED` by `Alnusjaponica` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2732320530)
- `2025-04-02T15:43:34Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2736765642)
- `2025-04-07T11:00:38Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2746417467)
- `2025-04-07T11:01:10Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2746418752)
- ... 2 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/models/plamo2.py`: 19 inline comment(s)
- `tests/models/decoder_only/language/test_hybrid.py`: 5 inline comment(s)
- `docs/source/models/supported_models.md`: 4 inline comment(s)
- `tests/models/registry.py`: 2 inline comment(s)
- `vllm/model_executor/models/registry.py`: 2 inline comment(s)
- `vllm/config.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-31T14:41:59Z` `issue` by `tlrmchlsmth`; signals: bf16, dtype, gemm, h100; excerpt: "I'm not getting any output generated from following simple script (on an H100). Could you take a look? Somehow float16 is used by default ..." (https://github.com/vllm-project/vllm/pull/14323#issuecomment-2766462486)
- `2025-03-21T06:06:35Z` `inline` by `Alnusjaponica` `vllm/model_executor/models/plamo2.py`:119; signals: hang, perf, performance; excerpt: "It is possible to replace the selective scan fn with the mamba chunk scan combined function, as in MambaMixer2, to improve performance. This is ..." (https://github.com/vllm-project/vllm/pull/14323#discussion_r2006908999)
- `2025-03-24T02:24:28Z` `inline` by `Alnusjaponica` `tests/models/decoder_only/language/test_hybrid.py`:17; signals: block, kernel, pipeline; excerpt: "Let's instead add this step to .buildkite/test-pipeline.yaml under the Language Models Test (both) Thank you for the suggestion. I've moved pip install step to ..." (https://github.com/vllm-project/vllm/pull/14323#discussion_r2009371943)
- `2025-04-01T11:01:15Z` `issue` by `Alnusjaponica`; signals: attention, dtype, hang; excerpt: "Thanks for your suggestions. It seems the weight's dtype is downcasted here: So, I am decided to edit vllm/vllm/config.py to use bfloat16 by default. ..." (https://github.com/vllm-project/vllm/pull/14323#issuecomment-2768985807)
- `2025-04-02T11:44:12Z` `issue` by `Alnusjaponica`; signals: block, compile, hang; excerpt: "Does this still happen even after recompiling? It resolved after I recompiled. Thanks a lot. We're going to fix PlamoConfig.model type in modeling plamo.py ..." (https://github.com/vllm-project/vllm/pull/14323#issuecomment-2772301509)
- `2025-04-02T15:47:11Z` `issue` by `tlrmchlsmth`; signals: hang, perf, performance; excerpt: "@Alnusjaponica thanks, let me know when those changes are in! I'll update this PR after those public model changes. Is there anything else that ..." (https://github.com/vllm-project/vllm/pull/14323#issuecomment-2773012714)
- `2025-03-19T17:43:36Z` `inline` by `tlrmchlsmth` `tests/models/decoder_only/language/test_hybrid.py`:17; signals: block, kernel; excerpt: "Do we need this for the test to work, or just for speed up? If we are installing the mamba kernels, can we delete ..." (https://github.com/vllm-project/vllm/pull/14323#discussion_r2003913335)
- `2025-03-24T18:12:37Z` `review` `COMMENTED` by `tlrmchlsmth`; signals: h100; excerpt: "I'm not getting any output generated from following simple script (on an H100). Could you take a look?" (https://github.com/vllm-project/vllm/pull/14323#pullrequestreview-2711286347)
- `2025-03-25T05:46:32Z` `issue` by `Alnusjaponica`; signals: dtype, h100; excerpt: "I'm not getting any output generated from following simple script (on an H100). Could you take a look? Somehow float16 is used by default ..." (https://github.com/vllm-project/vllm/pull/14323#issuecomment-2750155782)
- `2025-03-31T14:46:45Z` `issue` by `DarkLight1337`; signals: bf16, dtype; excerpt: "@DarkLight1337 do you have any better ideas? (Also do you know why that snippet got removed in The proper way to do it would ..." (https://github.com/vllm-project/vllm/pull/14323#issuecomment-2766476775)
- `2025-03-31T16:17:17Z` `issue` by `tlrmchlsmth`; signals: bf16, dtype; excerpt: "@DarkLight1337 do you have any better ideas? (Also do you know why that snippet got removed in 14858?) The proper way to do it ..." (https://github.com/vllm-project/vllm/pull/14323#issuecomment-2766735308)
- `2025-04-01T20:56:19Z` `issue` by `tlrmchlsmth`; signals: attention, hang; excerpt: "I also noticed that this PR is affected by 15238 after I merge the latest changes from the main branch, so I need to ..." (https://github.com/vllm-project/vllm/pull/14323#issuecomment-2770665617)
