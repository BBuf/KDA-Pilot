# PR Discussion Digest

- Source PR: [vllm-project/vllm#34580](https://github.com/vllm-project/vllm/pull/34580)
- Source page: `sources/prs/vllm/PR-34580.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-34580`
- Generated at: `2026-05-20T15:39:51.748874+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-15T11:36:07Z`
- Merged: `2026-02-27T12:20:23Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 14 (approved=3, commented=11)
- Inline review comments: 15
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=6
- Human participants with discussion text: Isotr0py, maxyanghu, mergify, wangshangsam, ywang96
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-15T11:37:55Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for the Flashinfer cuDNN backend for Qwen3 VL ViT attention, which ... (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3804522773)
- `2026-02-17T21:19:46Z` `APPROVED` by `wangshangsam` (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3816360100)
- `2026-02-17T21:23:00Z` `COMMENTED` by `wangshangsam` (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3816378030)
- `2026-02-18T01:43:09Z` `COMMENTED` by `maxyanghu` (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3817227872)
- `2026-02-18T08:58:38Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3818510992)
- `2026-02-18T10:52:12Z` `COMMENTED` by `ywang96` - Thanks for the contribution and the idea makes sense to me! I have a high-level suggestion - I ... (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3818937348)
- `2026-02-18T12:48:40Z` `COMMENTED` by `maxyanghu` (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3819730897)
- `2026-02-18T13:57:30Z` `COMMENTED` by `maxyanghu` (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3820061972)
- `2026-02-18T15:00:16Z` `COMMENTED` by `maxyanghu` (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3820400010)
- `2026-02-18T15:00:51Z` `COMMENTED` by `maxyanghu` (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3820403781)
- `2026-02-18T23:41:52Z` `COMMENTED` by `maxyanghu` (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3822748675)
- `2026-02-23T02:53:55Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3838878889)
- `2026-02-27T07:05:42Z` `APPROVED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3865338555)
- `2026-02-27T07:40:57Z` `APPROVED` by `ywang96` - Let's get this in! (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3865486181)

## Inline Comment Hotspots

- `vllm/model_executor/models/qwen3_vl.py`: 11 inline comment(s)
- `vllm/v1/attention/ops/vit_attn_wrappers.py`: 2 inline comment(s)
- `vllm/model_executor/models/qwen2_5_vl.py`: 1 inline comment(s)
- `requirements/test.txt`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-21T10:09:05Z` `issue` by `Isotr0py`; signals: attention, failing, kernel; excerpt: "PTAL the failing attention kernels tests." (https://github.com/vllm-project/vllm/pull/34580#issuecomment-3938550248)
- `2026-02-18T08:57:45Z` `inline` by `Isotr0py` `vllm/v1/attention/ops/vit_attn_wrappers.py`:358; signals: attention, kernel; excerpt: "Can you update tests under tests/kernels/attention/test mha attn.py?" (https://github.com/vllm-project/vllm/pull/34580#discussion_r2821135611)
- `2026-02-18T10:52:12Z` `review` `COMMENTED` by `ywang96`; signals: flashinfer; excerpt: "Thanks for the contribution and the idea makes sense to me! I have a high-level suggestion - I think currently there are quite a ..." (https://github.com/vllm-project/vllm/pull/34580#pullrequestreview-3818937348)
- `2026-02-21T16:58:37Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @maxyanghu, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/34580#issuecomment-3939090903)
- `2026-02-17T21:23:00Z` `inline` by `wangshangsam` `vllm/model_executor/models/qwen3_vl.py`:160; signals: cuda; excerpt: "For these two TODO items, I wondering if we should create issues to track them. The full CUDA graph support, I presume would come ..." (https://github.com/vllm-project/vllm/pull/34580#discussion_r2819150748)
- `2026-02-18T01:43:08Z` `inline` by `maxyanghu` `vllm/model_executor/models/qwen3_vl.py`:160; signals: cuda; excerpt: "I created an issue to track cuDNN upgrade. For full CUDA graph support, since we're already working on it i don't think we need ..." (https://github.com/vllm-project/vllm/pull/34580#discussion_r2819910886)
- `2026-02-18T08:44:18Z` `inline` by `Isotr0py` `vllm/model_executor/models/qwen3_vl.py`:648; signals: attention; excerpt: "I prefer to move these methods inside MMEncoderAttention as classmethod somehow, then we can reuse it for other similar models:" (https://github.com/vllm-project/vllm/pull/34580#discussion_r2821059163)
- `2026-02-18T10:19:39Z` `inline` by `ywang96` `vllm/model_executor/models/qwen3_vl.py`:172; signals: attention; excerpt: "Can we move this to mm encoder attention.py? Also might be dumb question - how did we derive to the 128 MiB workspace size?" (https://github.com/vllm-project/vllm/pull/34580#discussion_r2821505420)
- `2026-02-18T23:41:52Z` `inline` by `maxyanghu` `vllm/model_executor/models/qwen3_vl.py`:172; signals: tma; excerpt: "From cuDNN team - For Prefill 128MB should be good. Lets keep it as a magic number. Ideally it would be batch size size ..." (https://github.com/vllm-project/vllm/pull/34580#discussion_r2824962773)
- `2026-02-18T12:48:40Z` `inline` by `maxyanghu` `vllm/v1/attention/ops/vit_attn_wrappers.py`:358; signals: attention; excerpt: "Added test" (https://github.com/vllm-project/vllm/pull/34580#discussion_r2822169188)
- `2026-02-18T13:57:30Z` `inline` by `maxyanghu` `vllm/model_executor/models/qwen3_vl.py`:160; signals: attention; excerpt: "I'm moved these comments to mm encoder attention.py" (https://github.com/vllm-project/vllm/pull/34580#discussion_r2822493490)
- `2026-02-18T15:00:16Z` `inline` by `maxyanghu` `vllm/model_executor/models/qwen3_vl.py`:172; signals: attention; excerpt: "moved workspace buffer inside MMEncoderAttention" (https://github.com/vllm-project/vllm/pull/34580#discussion_r2822780757)
