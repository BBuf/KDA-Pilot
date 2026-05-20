# PR Discussion Digest

- Source PR: [sgl-project/sglang#17627](https://github.com/sgl-project/sglang/pull/17627)
- Source page: `sources/prs/sglang/PR-17627.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-17627`
- Generated at: `2026-05-20T15:28:31.266770+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-23T05:32:01Z`
- Merged: `2026-02-28T02:28:47Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 6 (approved=2, changes_requested=2, commented=2)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Fridge003, hlu1, samuellees, zhengd-nv
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-03T12:26:05Z` `CHANGES_REQUESTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/17627#pullrequestreview-3744970144)
- `2026-02-05T07:06:47Z` `COMMENTED` by `zhengd-nv` (https://github.com/sgl-project/sglang/pull/17627#pullrequestreview-3754911785)
- `2026-02-05T16:00:42Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/17627#pullrequestreview-3758009003)
- `2026-02-06T02:01:39Z` `CHANGES_REQUESTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/17627#pullrequestreview-3760344553)
- `2026-02-06T09:30:16Z` `COMMENTED` by `zhengd-nv` (https://github.com/sgl-project/sglang/pull/17627#pullrequestreview-3761802475)
- `2026-02-27T18:31:15Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/17627#pullrequestreview-3868416752)

## Inline Comment Hotspots

- `test/registered/models/test_qwen3_next_models_fp4.py`: 4 inline comment(s)
- `test/run_suite_nightly.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-05T07:06:47Z` `inline` by `zhengd-nv` `test/registered/models/test_qwen3_next_models_fp4.py`:122; signals: fp4, hang, register; excerpt: "Thanks for your comment. The accept length test indicates some problems in the MTP integration. I reverted all the changes about MTP and make ..." (https://github.com/sgl-project/sglang/pull/17627#discussion_r2767447716)
- `2026-02-06T02:01:35Z` `inline` by `Fridge003` `test/registered/models/test_qwen3_next_models_fp4.py`:13; signals: cuda, fp4, register; excerpt: "Please also register this CI with register cuda ci" (https://github.com/sgl-project/sglang/pull/17627#discussion_r2771904328)
- `2026-02-03T12:25:55Z` `inline` by `Fridge003` `test/registered/models/test_qwen3_next_models_fp4.py`:122; signals: fp4, register; excerpt: "Add a send one test for detecting accept length? Like this one" (https://github.com/sgl-project/sglang/pull/17627#discussion_r2758820902)
- `2026-02-06T09:30:15Z` `inline` by `zhengd-nv` `test/registered/models/test_qwen3_next_models_fp4.py`:13; signals: fp4, register; excerpt: "Updated." (https://github.com/sgl-project/sglang/pull/17627#discussion_r2773139223)
- `2026-02-10T06:28:51Z` `issue` by `samuellees`; signals: hang; excerpt: "It always falls, but seems not relative with this PR. Do you have any insight, please? cc @Fridge003 @yizhang2077 [PR Test / stage-b-test-large-1-gpu (4) ..." (https://github.com/sgl-project/sglang/pull/17627#issuecomment-3875607726)
- `2026-01-23T05:38:54Z` `issue` by `samuellees`; signals: hang; excerpt: "cc @yizhang2077" (https://github.com/sgl-project/sglang/pull/17627#issuecomment-3788402361)
