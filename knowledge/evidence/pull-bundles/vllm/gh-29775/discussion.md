# PR Discussion Digest

- Source PR: [vllm-project/vllm#29775](https://github.com/vllm-project/vllm/pull/29775)
- Source page: `sources/prs/vllm/PR-29775.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29775`
- Generated at: `2026-05-20T15:38:49.159954+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-01T08:10:00Z`
- Merged: `2025-12-05T11:01:17Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 4 (approved=2, changes_requested=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: BowenBao, ZhiweiYan-96, chatgpt-codex-connector, heheda12345, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-01T08:12:36Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request makes the w4a16 quantization recipe the default for Quark MoE on ROCm, which ... (https://github.com/vllm-project/vllm/pull/29775#pullrequestreview-3523706169)
- `2025-12-02T22:17:01Z` `CHANGES_REQUESTED` by `BowenBao` - Please consider above recommendation. (https://github.com/vllm-project/vllm/pull/29775#pullrequestreview-3532317782)
- `2025-12-05T08:03:11Z` `APPROVED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/29775#pullrequestreview-3543528567)
- `2025-12-05T08:38:40Z` `APPROVED` by `tjtanaa` - LGTM. @ZhiweiYan-96 can you also sync your branch with upstream main? (https://github.com/vllm-project/vllm/pull/29775#pullrequestreview-3543634604)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-12-02T17:38:49Z` `issue` by `BowenBao`; signals: bf16, fp4, mxfp4, regression; excerpt: "Hi @ZhiweiYan-96, the existing code flow w mxfp4 a mxfp4 refers to the same concept. What was the issue w/o this PR? looks like ..." (https://github.com/vllm-project/vllm/pull/29775#issuecomment-3603233447)
- `2025-12-02T22:12:54Z` `issue` by `BowenBao`; signals: kernel, moe, triton; excerpt: "After offline discussion with @dllehr-amd, here is our recommended fix. As pointed out from my previous comment, w4a16 is 4bit weight only static quantization ..." (https://github.com/vllm-project/vllm/pull/29775#issuecomment-3604179969)
- `2025-12-05T08:00:15Z` `issue` by `ZhiweiYan-96`; signals: fp4, kernel, mxfp4; excerpt: "@BowenBao @tjtanaa @dllehr-amd Thanks for the suggestion, it is the exact thing we want and it can fix the kernel jitting issue. Following is ..." (https://github.com/vllm-project/vllm/pull/29775#issuecomment-3615710003)
- `2025-12-02T22:17:01Z` `review` `CHANGES_REQUESTED` by `BowenBao`; signals: general review; excerpt: "Please consider above recommendation." (https://github.com/vllm-project/vllm/pull/29775#pullrequestreview-3532317782)
- `2025-12-01T08:10:05Z` `issue` by `chatgpt-codex-connector`; signals: general review; excerpt: "Codex usage limits have been reached for code reviews. Please check with the admins of this repo to increase the limits by adding credits." (https://github.com/vllm-project/vllm/pull/29775#issuecomment-3595171022)
- `2025-12-01T08:11:03Z` `issue` by `ZhiweiYan-96`; signals: general review; excerpt: "@gshtras @wuhuikx @zejunchen-zejun @tjtanaa Could you please help review the PR？Appreciation for your suggestions." (https://github.com/vllm-project/vllm/pull/29775#issuecomment-3595175782)
