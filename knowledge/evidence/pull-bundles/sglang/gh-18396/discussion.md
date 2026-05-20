# PR Discussion Digest

- Source PR: [sgl-project/sglang#18396](https://github.com/sgl-project/sglang/pull/18396)
- Source page: `sources/prs/sglang/PR-18396.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18396`
- Generated at: `2026-05-20T15:28:38.519908+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-07T06:13:21Z`
- Merged: `2026-02-08T15:11:16Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: Fridge003, debo3
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-08T03:30:38Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/18396#pullrequestreview-3768757570)
- `2026-02-08T08:58:06Z` `COMMENTED` by `debo3` (https://github.com/sgl-project/sglang/pull/18396#pullrequestreview-3769263393)
- `2026-02-08T09:06:39Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/18396#pullrequestreview-3769304317)
- `2026-02-08T09:34:53Z` `COMMENTED` by `debo3` (https://github.com/sgl-project/sglang/pull/18396#pullrequestreview-3769403830)
- `2026-02-08T09:39:29Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/18396#pullrequestreview-3769419426)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/trtllm_mla_backend.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-02-08T08:58:06Z` `inline` by `debo3` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:915; signals: attention, bf16, cache, fp8, kv cache, mla, pipeline; excerpt: "An assertion would cause the server to crash for checkpoints that legitimately contain k scale/v scale (e.g., from FP8 KV cache calibration pipelines like ..." (https://github.com/sgl-project/sglang/pull/18396#discussion_r2778929470)
- `2026-02-08T09:34:53Z` `inline` by `debo3` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:915; signals: attention, cache, dtype, fp8, kv cache, mla; excerpt: "Added a logger.warning once in both code paths that logs when k scale is present in the checkpoint but being ignored due to non-FP8 ..." (https://github.com/sgl-project/sglang/pull/18396#discussion_r2779008884)
- `2026-02-08T03:30:35Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:915; signals: attention, bf16, cache, kv cache, mla; excerpt: "Why not add an assertion on k scale being None when bf16 kv cache is used?" (https://github.com/sgl-project/sglang/pull/18396#discussion_r2778445772)
- `2026-02-08T09:06:39Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:915; signals: attention, hang, mla; excerpt: "I see... Can we throw a warning on changing the passed in k scale/v scale value?" (https://github.com/sgl-project/sglang/pull/18396#discussion_r2778953210)
