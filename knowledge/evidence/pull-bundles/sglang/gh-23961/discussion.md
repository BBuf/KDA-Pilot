# PR Discussion Digest

- Source PR: [sgl-project/sglang#23961](https://github.com/sgl-project/sglang/pull/23961)
- Source page: `sources/prs/sglang/PR-23961.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-23961`
- Generated at: `2026-05-20T15:29:41.827463+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-28T20:35:47Z`
- Merged: `2026-05-18T06:20:42Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 17
- Review threads observed: 15
- Resolved/outdated thread markers: resolved=0, outdated=12
- Human participants with discussion text: ch-wan, maocheng23
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-08T00:45:45Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/23961#pullrequestreview-4248089294)
- `2026-05-13T22:47:23Z` `COMMENTED` by `maocheng23` (https://github.com/sgl-project/sglang/pull/23961#pullrequestreview-4285867070)
- `2026-05-14T00:59:14Z` `COMMENTED` by `maocheng23` (https://github.com/sgl-project/sglang/pull/23961#pullrequestreview-4286422371)
- `2026-05-14T22:57:37Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/23961#pullrequestreview-4294062990)

## Inline Comment Hotspots

- `python/sglang/srt/tp_invariant_ops/tp_invariant_ops.py`: 4 inline comment(s)
- `python/sglang/srt/distributed/communication_op.py`: 3 inline comment(s)
- `python/sglang/srt/layers/linear.py`: 3 inline comment(s)
- `python/sglang/srt/true_on_policy/config.py`: 2 inline comment(s)
- `python/sglang/srt/models/qwen2.py`: 2 inline comment(s)
- `python/sglang/srt/layers/layernorm.py`: 1 inline comment(s)
- `python/sglang/srt/layers/logits_processor.py`: 1 inline comment(s)
- `python/sglang/srt/model_executor/cuda_graph_runner.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-07T23:07:04Z` `inline` by `ch-wan` `python/sglang/srt/model_executor/cuda_graph_runner.py`:810; signals: cuda; excerpt: "How can this incur ValueError?" (https://github.com/sgl-project/sglang/pull/23961#discussion_r3205179680)
- `2026-05-07T22:25:08Z` `inline` by `ch-wan` `python/sglang/srt/distributed/communication_op.py`:21; signals: general review; excerpt: "A refactor is needed. Tree allreduce should be called within allreduce. Try decoupling model definition and system execution." (https://github.com/sgl-project/sglang/pull/23961#discussion_r3205043355)
- `2026-05-07T23:04:59Z` `inline` by `ch-wan` `python/sglang/srt/layers/logits_processor.py`:939; signals: general review; excerpt: "Is this more efficient? It has two reshape + one movedim. Previously, we have 1 reshape plus one permute" (https://github.com/sgl-project/sglang/pull/23961#discussion_r3205172556)
- `2026-05-07T23:09:18Z` `inline` by `ch-wan` `python/sglang/srt/true_on_policy/config.py`:125; signals: general review; excerpt: "What's the difference between server args and global server args? Also, we can directly call global server args anywhere. Passing server args to a ..." (https://github.com/sgl-project/sglang/pull/23961#discussion_r3205186845)
- `2026-05-13T22:47:23Z` `inline` by `maocheng23` `python/sglang/srt/layers/linear.py`:1510; signals: general review; excerpt: "Yes, this is expected. ColumnParallelLinear and QKVParallelLinear are independent per-rank matmuls — each rank computes its shard without a subsequent reduction, so there's no ..." (https://github.com/sgl-project/sglang/pull/23961#discussion_r3237879357)
- `2026-05-14T00:59:13Z` `inline` by `maocheng23` `python/sglang/srt/models/qwen2.py`:310; signals: general review; excerpt: "Just to confirm, norm kwargs with the new function follows the same logic as before, right? Could you explain your idea a bit more?" (https://github.com/sgl-project/sglang/pull/23961#discussion_r3238349839)
- `2026-05-07T22:21:34Z` `inline` by `ch-wan` `python/sglang/srt/distributed/communication_op.py`:23; signals: general review; excerpt: "move import to the beginning of this file" (https://github.com/sgl-project/sglang/pull/23961#discussion_r3205029768)
- `2026-05-07T22:21:42Z` `inline` by `ch-wan` `python/sglang/srt/distributed/communication_op.py`:30; signals: general review; excerpt: "same here" (https://github.com/sgl-project/sglang/pull/23961#discussion_r3205030228)
- `2026-05-07T22:56:42Z` `inline` by `ch-wan` `python/sglang/srt/layers/linear.py`:1510; signals: general review; excerpt: "You only modified RowParallelLinear but did not touch other linear classes. Is this expected?" (https://github.com/sgl-project/sglang/pull/23961#discussion_r3205147039)
- `2026-05-07T22:57:09Z` `inline` by `ch-wan` `python/sglang/srt/layers/linear.py`:1524; signals: general review; excerpt: "incorrect under dp attn" (https://github.com/sgl-project/sglang/pull/23961#discussion_r3205148436)
- `2026-05-07T23:18:25Z` `inline` by `ch-wan` `python/sglang/srt/true_on_policy/config.py`:13; signals: general review; excerpt: "how can server args be different with get global server args?" (https://github.com/sgl-project/sglang/pull/23961#discussion_r3205218746)
- `2026-05-07T23:22:17Z` `inline` by `ch-wan` `python/sglang/srt/models/qwen2.py`:310; signals: general review; excerpt: "we don't need to unwrap norm kwargs right? this would make code simpler" (https://github.com/sgl-project/sglang/pull/23961#discussion_r3205230131)
