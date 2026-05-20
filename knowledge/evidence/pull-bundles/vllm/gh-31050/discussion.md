# PR Discussion Digest

- Source PR: [vllm-project/vllm#31050](https://github.com/vllm-project/vllm/pull/31050)
- Source page: `sources/prs/vllm/PR-31050.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-31050`
- Generated at: `2026-05-20T15:39:11.846196+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-20T00:04:36Z`
- Merged: `2026-01-02T21:47:16Z`

## Discussion Counts

- Issue comments: 18
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: JartX, chatgpt-codex-connector, jinzhen-lin, mergify, mgoin, robertgshaw2-redhat, russellb, zyongye
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 13

## Review Decisions

- `2025-12-20T00:07:44Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/31050#pullrequestreview-3600491596)
- `2025-12-20T00:12:10Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the fused MoE kernel invocation logic by introducing new specialized Triton kernel ... (https://github.com/vllm-project/vllm/pull/31050#pullrequestreview-3600495010)
- `2025-12-26T05:37:22Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/31050#pullrequestreview-3612803632)
- `2025-12-29T18:25:38Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/31050#pullrequestreview-3616474252)
- `2025-12-31T22:13:06Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31050#pullrequestreview-3621478168)
- `2026-01-01T21:30:07Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/31050#pullrequestreview-3622056197)
- `2026-01-02T21:45:45Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31050#pullrequestreview-3623933196)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 5 inline comment(s)
- `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-20T00:07:44Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/fused_moe/fused_moe.py`:856; signals: block, cuda, cute, kernel, moe; excerpt: ". The callee’s signature defined above requires those parameters, so when should moe wna16 use cuda(...) returns true (grouped quantization with block shape set), ..." (https://github.com/vllm-project/vllm/pull/31050#discussion_r2636617662)
- `2025-12-26T05:37:22Z` `inline` by `jinzhen-lin` `vllm/model_executor/layers/fused_moe/fused_moe.py`:541; signals: cuda, kernel, moe, triton; excerpt: "This function runs the cuda kernel, but not the triton kernel. Maybe we can use invoke fused moe wna16 cuda kernel and invoke fused ..." (https://github.com/vllm-project/vllm/pull/31050#discussion_r2647579649)
- `2025-12-20T00:08:41Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @zyongye, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/31050#issuecomment-3677054929)
- `2025-12-20T00:25:50Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @zyongye, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/31050#issuecomment-3677076076)
- `2025-12-20T00:07:44Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub [Your team has set up Codex ..." (https://github.com/vllm-project/vllm/pull/31050#pullrequestreview-3600491596)
- `2025-12-29T18:25:38Z` `inline` by `zyongye` `vllm/model_executor/layers/fused_moe/fused_moe.py`:541; signals: moe; excerpt: "fixed" (https://github.com/vllm-project/vllm/pull/31050#discussion_r2651517523)
- `2025-12-31T22:13:06Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1835; signals: moe; excerpt: "nit" (https://github.com/vllm-project/vllm/pull/31050#discussion_r2655932586)
- `2025-12-31T12:56:01Z` `issue` by `jinzhen-lin`; signals: moe; excerpt: "The rest of the PR LGTM. BTW, I just found the moe wna16 maybe used in SM75+ in some cases, for example, when size ..." (https://github.com/vllm-project/vllm/pull/31050#issuecomment-3702159622)
- `2025-12-23T02:06:01Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @zyongye." (https://github.com/vllm-project/vllm/pull/31050#issuecomment-3684780473)
