# PR Discussion Digest

- Source PR: [sgl-project/sglang#10263](https://github.com/sgl-project/sglang/pull/10263)
- Source page: `sources/prs/sglang/PR-10263.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-10263`
- Generated at: `2026-05-20T15:27:16.567083+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-10T07:47:57Z`
- Merged: `2025-10-02T10:02:19Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 0 (no states)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: fzyzcjy, kaixih, shifangx
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- No review submissions were returned by GitHub.

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-09-20T01:53:05Z` `issue` by `kaixih`; signals: accuracy, block, fp4; excerpt: "Following @shifangx 's question: so the prefill side command in doesn't seem to use the fp4. I recall that we had an accuracy issue ..." (https://github.com/sgl-project/sglang/pull/10263#issuecomment-3314389737)
- `2025-09-16T07:59:00Z` `issue` by `shifangx`; signals: fp4, nvfp4; excerpt: "Hi, @fzyzcjy, @kaixih and I noticed that --quantization modelopt fp4 is only used for decoding disaggregation-mode. Dose prefill disaggregation-mode will also support nvfp4 in ..." (https://github.com/sgl-project/sglang/pull/10263#issuecomment-3296404466)
- `2025-09-23T02:24:24Z` `issue` by `fzyzcjy`; signals: b200, cuda; excerpt: "excluding the b200 which is known to have issues, cuda ci is green now" (https://github.com/sgl-project/sglang/pull/10263#issuecomment-3322140093)
- `2025-09-20T03:32:03Z` `issue` by `fzyzcjy`; signals: fp4; excerpt: "yes I use fp4 for P as well now, but not using deepep yet indeed" (https://github.com/sgl-project/sglang/pull/10263#issuecomment-3314479013)
- `2025-09-12T03:59:43Z` `issue` by `fzyzcjy`; signals: general review; excerpt: "gives gsm: mean=96.0, std=0.3, min=95.5, max=96.4, repeat=48 math500: 980,986,984 gpqa: mean=80.7, std=1.7, min=76.8, max=84.3, repeat=48" (https://github.com/sgl-project/sglang/pull/10263#issuecomment-3283563891)
