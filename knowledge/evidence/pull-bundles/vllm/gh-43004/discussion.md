# PR Discussion Digest

- Source PR: [vllm-project/vllm#43004](https://github.com/vllm-project/vllm/pull/43004)
- Source page: `sources/prs/vllm/PR-43004.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-43004`
- Generated at: `2026-05-20T15:41:02.254488+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-18T17:09:00Z`
- Merged: `2026-05-19T02:50:03Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 5 (commented=5)
- Inline review comments: 7
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: WoosukKwon, zyongye
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-18T17:13:08Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the DeepSeek V4 model implementation by moving it to a new hardware-isolated ... (https://github.com/vllm-project/vllm/pull/43004#pullrequestreview-4312208401)
- `2026-05-18T18:45:45Z` `COMMENTED` by `zyongye` - Have we decide the name nvidia and amd? Or we want to say them cuda and rocm to ... (https://github.com/vllm-project/vllm/pull/43004#pullrequestreview-4312790542)
- `2026-05-19T02:06:01Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/43004#pullrequestreview-4315195456)
- `2026-05-19T02:07:44Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/43004#pullrequestreview-4315201710)
- `2026-05-19T02:08:24Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/43004#pullrequestreview-4315204286)

## Inline Comment Hotspots

- `vllm/models/deepseek_v4/nvidia/deepseek_v4.py`: 2 inline comment(s)
- `vllm/models/deepseek_v4/__init__.py`: 2 inline comment(s)
- `vllm/models/deepseek_v4/amd/deepseek_v4.py`: 2 inline comment(s)
- `vllm/models/deepseek_v4/nvidia/deepseek_v4_mtp.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-19T02:08:24Z` `inline` by `WoosukKwon` `vllm/models/deepseek_v4/amd/deepseek_v4.py`:1; signals: attention, hang, moe; excerpt: "Yes for attention, but not sure about MoE. For this PR, I didn't include the changes to keep it small." (https://github.com/vllm-project/vllm/pull/43004#discussion_r3263250025)
- `2026-05-18T18:44:27Z` `inline` by `zyongye` `vllm/models/deepseek_v4/amd/deepseek_v4.py`:1; signals: attention, moe; excerpt: "We would want to have amd specific version of fused moe and attention class right?" (https://github.com/vllm-project/vllm/pull/43004#discussion_r3261231588)
- `2026-05-18T18:45:45Z` `review` `COMMENTED` by `zyongye`; signals: cuda; excerpt: "Have we decide the name nvidia and amd? Or we want to say them cuda and rocm to match the name on current platform?" (https://github.com/vllm-project/vllm/pull/43004#pullrequestreview-4312790542)
- `2026-05-19T02:07:44Z` `inline` by `WoosukKwon` `vllm/models/deepseek_v4/nvidia/deepseek_v4.py`:1537; signals: general review; excerpt: "It's because vllm/model executor/models is excluded from the mypy check historically. Now we apply mypy to vllm/models, which is a nice improvement" (https://github.com/vllm-project/vllm/pull/43004#discussion_r3263247800)
- `2026-05-18T18:41:52Z` `inline` by `zyongye` `vllm/models/deepseek_v4/nvidia/deepseek_v4.py`:1537; signals: general review; excerpt: "type: ignore[assignment] is this flagged by pre-commit? why don't we have this before?" (https://github.com/vllm-project/vllm/pull/43004#discussion_r3261212998)
- `2026-05-18T18:42:42Z` `inline` by `zyongye` `vllm/models/deepseek_v4/__init__.py`:24; signals: general review; excerpt: "We can extract this away once we have more and more models written in this way right?" (https://github.com/vllm-project/vllm/pull/43004#discussion_r3261218462)
- `2026-05-19T02:06:00Z` `inline` by `WoosukKwon` `vllm/models/deepseek_v4/__init__.py`:24; signals: general review; excerpt: "Good point. Will do it later." (https://github.com/vllm-project/vllm/pull/43004#discussion_r3263242331)
