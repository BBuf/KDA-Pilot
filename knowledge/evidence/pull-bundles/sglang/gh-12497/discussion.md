# PR Discussion Digest

- Source PR: [sgl-project/sglang#12497](https://github.com/sgl-project/sglang/pull/12497)
- Source page: `sources/prs/sglang/PR-12497.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-12497`
- Generated at: `2026-05-20T15:27:39.741005+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-01T17:13:32Z`
- Merged: `2026-01-15T00:57:15Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: JustinTong0323, LorrinWWW, b8zhong, copilot-pull-request-reviewer
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-01T17:15:30Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses an issue where an overly strict assertion on weight scale padding for ... (https://github.com/sgl-project/sglang/pull/12497#pullrequestreview-3407605046)
- `2025-11-01T17:19:07Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull Request Overview This PR relaxes the validation constraint for NVFP4 weight scale dimensions in MoE (Mixture of ... (https://github.com/sgl-project/sglang/pull/12497#pullrequestreview-3407606112)
- `2026-01-08T04:40:57Z` `APPROVED` by `JustinTong0323` (https://github.com/sgl-project/sglang/pull/12497#pullrequestreview-3637621459)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-01T17:19:07Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: fp4, hang, moe, nvfp4; excerpt: "Pull Request Overview This PR relaxes the validation constraint for NVFP4 weight scale dimensions in MoE (Mixture of Experts) processing. The change replaces a ..." (https://github.com/sgl-project/sglang/pull/12497#pullrequestreview-3407606112)
- `2026-01-06T19:27:56Z` `issue` by `b8zhong`; signals: accuracy; excerpt: "Hi @LorrinWWW , thanks for the reminder for this PR, I rebased it onto main and after the assertion fix, it seems the accuracy ..." (https://github.com/sgl-project/sglang/pull/12497#issuecomment-3716014677)
