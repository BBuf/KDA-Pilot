# PR Discussion Digest

- Source PR: [triton-lang/triton#10127](https://github.com/triton-lang/triton/pull/10127)
- Source page: `sources/prs/triton/PR-10127.md`
- Evidence bundle: `evidence/pull-bundles/triton/gh-10127`
- Generated at: `2026-05-20T15:33:21.547867+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-24T17:36:52Z`
- Merged: `2026-05-15T19:59:07Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 9 (approved=2, changes_requested=1, commented=6)
- Inline review comments: 6
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: ThomasRaoux, mooskagh, mydatascience, peterbell10
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-24T18:27:05Z` `CHANGES_REQUESTED` by `ThomasRaoux` - Can this happen in current flow? If so please make a lit test that expose the problem otherwise ... (https://github.com/triton-lang/triton/pull/10127#pullrequestreview-4172611197)
- `2026-04-27T17:13:34Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10127#pullrequestreview-4182854894)
- `2026-04-27T17:22:33Z` `COMMENTED` by `mydatascience` (https://github.com/triton-lang/triton/pull/10127#pullrequestreview-4182910255)
- `2026-04-27T17:24:41Z` `COMMENTED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10127#pullrequestreview-4182924693)
- `2026-04-27T18:04:37Z` `COMMENTED` by `mydatascience` (https://github.com/triton-lang/triton/pull/10127#pullrequestreview-4183173361)
- `2026-04-30T09:55:34Z` `COMMENTED` by `peterbell10` (https://github.com/triton-lang/triton/pull/10127#pullrequestreview-4204167626)
- `2026-05-04T16:57:44Z` `COMMENTED` by `mydatascience` (https://github.com/triton-lang/triton/pull/10127#pullrequestreview-4221863019)
- `2026-05-15T16:23:22Z` `APPROVED` by `peterbell10` (https://github.com/triton-lang/triton/pull/10127#pullrequestreview-4299686956)
- `2026-05-15T19:59:01Z` `APPROVED` by `ThomasRaoux` (https://github.com/triton-lang/triton/pull/10127#pullrequestreview-4301014989)

## Inline Comment Hotspots

- `test/TritonGPU/pipeline-split-cluster-unscheduled-op.mlir`: 6 inline comment(s)

## High-Signal Discussion

- `2026-04-27T17:22:32Z` `inline` by `mydatascience` `test/TritonGPU/pipeline-split-cluster-unscheduled-op.mlir`:19; signals: pipeline, triton; excerpt: "It wouldn’t assert at find. The bug was from using operator[], which inserted a default (invalid) entry for missing ops. That bogus entry later ..." (https://github.com/triton-lang/triton/pull/10127#discussion_r3149059306)
- `2026-04-27T18:04:37Z` `inline` by `mydatascience` `test/TritonGPU/pipeline-split-cluster-unscheduled-op.mlir`:19; signals: pipeline, triton; excerpt: "It won’t trigger in this case. Before the fix, the code used operator[], which silently inserted a missing op into the map with an ..." (https://github.com/triton-lang/triton/pull/10127#discussion_r3149281787)
- `2026-05-04T16:57:44Z` `inline` by `mydatascience` `test/TritonGPU/pipeline-split-cluster-unscheduled-op.mlir`:49; signals: pipeline, triton; excerpt: "That's a synthetic test. Still this can happen in a real life, you can check the mlir above. Should I replace this one with ..." (https://github.com/triton-lang/triton/pull/10127#discussion_r3183106415)
- `2026-04-27T17:13:34Z` `inline` by `ThomasRaoux` `test/TritonGPU/pipeline-split-cluster-unscheduled-op.mlir`:19; signals: pipeline, triton; excerpt: "I don't get it, if the op is not find then the function would assert?" (https://github.com/triton-lang/triton/pull/10127#discussion_r3149011706)
- `2026-04-27T17:24:41Z` `inline` by `ThomasRaoux` `test/TritonGPU/pipeline-split-cluster-unscheduled-op.mlir`:19; signals: pipeline, triton; excerpt: "but this one would trigger?" (https://github.com/triton-lang/triton/pull/10127#discussion_r3149070752)
- `2026-04-30T09:55:34Z` `inline` by `peterbell10` `test/TritonGPU/pipeline-split-cluster-unscheduled-op.mlir`:49; signals: pipeline, triton; excerpt: "Is this something that comes up in practice, or is it purely synthetic?" (https://github.com/triton-lang/triton/pull/10127#discussion_r3167091341)
- `2026-04-24T18:27:05Z` `review` `CHANGES_REQUESTED` by `ThomasRaoux`; signals: general review; excerpt: "Can this happen in current flow? If so please make a lit test that expose the problem otherwise I don't think it makes sense ..." (https://github.com/triton-lang/triton/pull/10127#pullrequestreview-4172611197)
- `2026-04-25T08:38:58Z` `issue` by `mydatascience`; signals: gemm; excerpt: "Can this happen in current flow? If so please make a lit test that expose the problem otherwise I don't think it makes sense ..." (https://github.com/triton-lang/triton/pull/10127#issuecomment-4318564667)
- `2026-05-15T12:02:52Z` `issue` by `mooskagh`; signals: general review; excerpt: "Regarding whether this issue could be encountered vs purely theoretical, it was discovered when debugging one of XLA crashes, so that's the IR that ..." (https://github.com/triton-lang/triton/pull/10127#issuecomment-4459574541)
