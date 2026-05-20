# PR Discussion Digest

- Source PR: [vllm-project/vllm#28816](https://github.com/vllm-project/vllm/pull/28816)
- Source page: `sources/prs/vllm/PR-28816.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28816`
- Generated at: `2026-05-20T15:38:33.740405+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-16T20:32:12Z`
- Merged: `2025-11-17T18:15:26Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: chatgpt-codex-connector, gshtras, houseroad, liuzijing2014, tjtanaa, zhewenl
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-16T20:34:25Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28816#pullrequestreview-3470480554)
- `2025-11-16T23:55:02Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/28816#pullrequestreview-3470584308)
- `2025-11-16T23:56:26Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/28816#pullrequestreview-3470585028)
- `2025-11-16T23:57:10Z` `COMMENTED` by `zhewenl` (https://github.com/vllm-project/vllm/pull/28816#pullrequestreview-3470585392)
- `2025-11-16T23:57:51Z` `COMMENTED` by `zhewenl` (https://github.com/vllm-project/vllm/pull/28816#pullrequestreview-3470585723)
- `2025-11-17T00:37:24Z` `COMMENTED` by `zhewenl` (https://github.com/vllm-project/vllm/pull/28816#pullrequestreview-3470611692)
- `2025-11-17T02:02:05Z` `APPROVED` by `tjtanaa` - LGTM. Since @zhewenl has also verified that it works on CUDA. However, let's see if @houseroad , @liuzijing2014 ... (https://github.com/vllm-project/vllm/pull/28816#pullrequestreview-3470692735)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/mxfp4.py`: 4 inline comment(s)
- `.buildkite/test-amd.yaml`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-17T18:14:50Z` `issue` by `gshtras`; signals: block, hang, kernel, perf, performance, regression, triton; excerpt: "Hi @zhewenl, i wonder can we upgrade the pin for AMD CI to use a newer triton package? Is there anything blocking it? @liuzijing2014 ..." (https://github.com/vllm-project/vllm/pull/28816#issuecomment-3543266723)
- `2025-11-17T00:37:24Z` `inline` by `zhewenl` `vllm/model_executor/layers/quantization/mxfp4.py`:758; signals: blackwell, block, fp4, h100, mxfp4; excerpt: "@houseroad verified it's working on H100 and updated test plan, also unblocked CI to verify it on Blackwell" (https://github.com/vllm-project/vllm/pull/28816#discussion_r2532362113)
- `2025-11-17T01:42:13Z` `issue` by `tjtanaa`; signals: block, regression, triton; excerpt: "Hi @zhewenl, i wonder can we upgrade the pin for AMD CI to use a newer triton package? Is there anything blocking it? @liuzijing2014 ..." (https://github.com/vllm-project/vllm/pull/28816#issuecomment-3539633409)
- `2025-11-16T20:34:25Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/quantization/mxfp4.py`:759; signals: fp4, mxfp4; excerpt: "![P1 Badge]( Assign correct tensor to w2 weight Parameter The new AMD fallback sets both layer.w13 weight and layer.w2 weight from w13 weight.storage.data. As ..." (https://github.com/vllm-project/vllm/pull/28816#discussion_r2532216236)
- `2025-11-16T23:56:26Z` `inline` by `houseroad` `vllm/model_executor/layers/quantization/mxfp4.py`:758; signals: fp4, mxfp4; excerpt: "does this work for nvidia?" (https://github.com/vllm-project/vllm/pull/28816#discussion_r2532334841)
- `2025-11-16T23:57:51Z` `inline` by `zhewenl` `vllm/model_executor/layers/quantization/mxfp4.py`:758; signals: fp4, mxfp4; excerpt: "since it's using an older version, it should be be compatible, let me also verify it" (https://github.com/vllm-project/vllm/pull/28816#discussion_r2532335607)
- `2025-11-17T01:02:04Z` `issue` by `liuzijing2014`; signals: block, triton; excerpt: "Hi @zhewenl, i wonder can we upgrade the pin for AMD CI to use a newer triton package? Is there anything blocking it?" (https://github.com/vllm-project/vllm/pull/28816#issuecomment-3539575597)
- `2025-11-17T02:02:05Z` `review` `APPROVED` by `tjtanaa`; signals: cuda, hang; excerpt: "LGTM. Since @zhewenl has also verified that it works on CUDA. However, let's see if @houseroad , @liuzijing2014 think this is changes is fine." (https://github.com/vllm-project/vllm/pull/28816#pullrequestreview-3470692735)
- `2025-11-16T20:34:25Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/28816#pullrequestreview-3470480554)
- `2025-11-16T23:55:01Z` `inline` by `houseroad` `.buildkite/test-amd.yaml`:1098; signals: b200; excerpt: "why remove the b200 checks?" (https://github.com/vllm-project/vllm/pull/28816#discussion_r2532333952)
- `2025-11-17T01:13:52Z` `issue` by `zhewenl`; signals: regression; excerpt: "@liuzijing2014 for this I am not sure, we might need to confirm with amd folks whether there is any reason pinning the version and ..." (https://github.com/vllm-project/vllm/pull/28816#issuecomment-3539594136)
- `2025-11-16T23:57:10Z` `inline` by `zhewenl` `.buildkite/test-amd.yaml`:1098; signals: general review; excerpt: "because it's been added&enabled to AMD CI, we should update the naming" (https://github.com/vllm-project/vllm/pull/28816#discussion_r2532335221)
