# PR Discussion Digest

- Source PR: [sgl-project/sglang#17235](https://github.com/sgl-project/sglang/pull/17235)
- Source page: `sources/prs/sglang/PR-17235.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-17235`
- Generated at: `2026-05-20T15:28:27.009058+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-16T22:03:33Z`
- Merged: `2026-01-18T21:33:20Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: b8zhong, koush
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-16T22:05:30Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds Triton MoE kernel configurations for the NVIDIA RTX PRO 6000 Blackwell GPU ... (https://github.com/sgl-project/sglang/pull/17235#pullrequestreview-3672917305)
- `2026-01-16T22:06:11Z` `COMMENTED` by `koush` (https://github.com/sgl-project/sglang/pull/17235#pullrequestreview-3672918729)
- `2026-01-16T22:47:13Z` `APPROVED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/17235#pullrequestreview-3673052678)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=161,N=192,device_name=NVIDIA_RTX_PRO_6000_Blackwell_Max-Q_Workstation_Edition.json`: 2 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=161,N=192,device_name=NVIDIA_RTX_PRO_6000_Blackwell_Max-Q_Workstation_Edition,dtype=fp8_w8a8,per_channel_quant=True.json`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-16T22:06:10Z` `inline` by `koush` `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_5_1/E=161,N=192,device_name=NVIDIA_RTX_PRO_6000_Blackwell_Max-Q_Workstation_Edition.json`:1; signals: blackwell, moe, triton; excerpt: "This is exactly what sglang uses/generates for the device fingerprint. It is correct. Similar files also exist in the other triton version config directories." (https://github.com/sgl-project/sglang/pull/17235#discussion_r2700123762)
