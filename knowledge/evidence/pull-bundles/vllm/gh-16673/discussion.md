# PR Discussion Digest

- Source PR: [vllm-project/vllm#16673](https://github.com/vllm-project/vllm/pull/16673)
- Source page: `sources/prs/vllm/PR-16673.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16673`
- Generated at: `2026-05-20T15:34:56.457155+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-15T16:22:59Z`
- Merged: `2025-04-17T20:12:09Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 6
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: LucasWilkinson, njhill
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-15T16:31:33Z` `COMMENTED` by `njhill` (https://github.com/vllm-project/vllm/pull/16673#pullrequestreview-2769082325)
- `2025-04-15T16:33:57Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/16673#pullrequestreview-2769090938)
- `2025-04-15T16:35:20Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/16673#pullrequestreview-2769096099)
- `2025-04-15T17:15:04Z` `COMMENTED` by `njhill` (https://github.com/vllm-project/vllm/pull/16673#pullrequestreview-2769201311)
- `2025-04-15T17:15:14Z` `COMMENTED` by `njhill` (https://github.com/vllm-project/vllm/pull/16673#pullrequestreview-2769201681)
- `2025-04-15T19:39:44Z` `COMMENTED` by `LucasWilkinson` - LGTM, do you mind just checking correctness? (https://github.com/vllm-project/vllm/pull/16673#pullrequestreview-2769582027)
- `2025-04-15T20:15:11Z` `COMMENTED` by `njhill` (https://github.com/vllm-project/vllm/pull/16673#pullrequestreview-2769691558)
- `2025-04-17T20:12:03Z` `APPROVED` by `LucasWilkinson` - LGTM, thanks for the accuracy checks! (https://github.com/vllm-project/vllm/pull/16673#pullrequestreview-2776809208)

## Inline Comment Hotspots

- `vllm/v1/worker/gpu_model_runner.py`: 6 inline comment(s)

## High-Signal Discussion

- `2025-04-15T16:33:57Z` `inline` by `LucasWilkinson` `vllm/v1/worker/gpu_model_runner.py`:466; signals: correctness, hang; excerpt: "the reorder batch is dependent on the scheduler output so we should call this regardless of batch changed, I think if we want to ..." (https://github.com/vllm-project/vllm/pull/16673#discussion_r2045038994)
- `2025-04-15T19:39:44Z` `review` `COMMENTED` by `LucasWilkinson`; signals: correctness; excerpt: "LGTM, do you mind just checking correctness?" (https://github.com/vllm-project/vllm/pull/16673#pullrequestreview-2769582027)
- `2025-04-15T16:31:33Z` `inline` by `njhill` `vllm/v1/worker/gpu_model_runner.py`:466; signals: hang; excerpt: "The only time we might need to reorder should be after the batch contents already changed right?" (https://github.com/vllm-project/vllm/pull/16673#discussion_r2045035429)
- `2025-04-17T20:12:03Z` `review` `APPROVED` by `LucasWilkinson`; signals: accuracy; excerpt: "LGTM, thanks for the accuracy checks!" (https://github.com/vllm-project/vllm/pull/16673#pullrequestreview-2776809208)
- `2025-04-15T16:35:20Z` `inline` by `LucasWilkinson` `vllm/v1/worker/gpu_model_runner.py`:466; signals: general review; excerpt: "unfortunately no, reordering happens when requests transition from prefill to decode" (https://github.com/vllm-project/vllm/pull/16673#discussion_r2045041232)
- `2025-04-15T17:15:04Z` `inline` by `njhill` `vllm/v1/worker/gpu_model_runner.py`:466; signals: general review; excerpt: "Thanks @LucasWilkinson, good point! Now fixed." (https://github.com/vllm-project/vllm/pull/16673#discussion_r2045107334)
- `2025-04-15T17:15:14Z` `inline` by `njhill` `vllm/v1/worker/gpu_model_runner.py`:466; signals: general review; excerpt: "Wrong." (https://github.com/vllm-project/vllm/pull/16673#discussion_r2045107565)
- `2025-04-15T20:15:11Z` `inline` by `njhill` `vllm/v1/worker/gpu_model_runner.py`:466; signals: general review; excerpt: "(that "Wrong" was in response to my own question lol)" (https://github.com/vllm-project/vllm/pull/16673#discussion_r2045405649)
