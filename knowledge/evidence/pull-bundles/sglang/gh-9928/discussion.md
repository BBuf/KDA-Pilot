# PR Discussion Digest

- Source PR: [sgl-project/sglang#9928](https://github.com/sgl-project/sglang/pull/9928)
- Source page: `sources/prs/sglang/PR-9928.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-9928`
- Generated at: `2026-05-20T15:31:39.828047+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-02T12:19:12Z`
- Merged: `2025-09-16T23:16:06Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: cicirori, fzyzcjy, yuho8818, zhyncs
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-09-02T17:10:27Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for FlashAttention v4, a significant enhancement for models running on newer ... (https://github.com/sgl-project/sglang/pull/9928#pullrequestreview-3177450811)
- `2025-09-02T21:14:12Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/9928#pullrequestreview-3178151100)
- `2025-09-02T21:15:01Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/9928#pullrequestreview-3178152626)
- `2025-09-02T22:55:00Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/9928#pullrequestreview-3178390333)
- `2025-09-02T22:56:25Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/9928#pullrequestreview-3178391966)
- `2025-09-16T18:49:41Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/9928#pullrequestreview-3231264435)

## Inline Comment Hotspots

- `sgl-kernel/pyproject.toml`: 2 inline comment(s)
- `python/sglang/srt/models/deepseek_v2.py`: 2 inline comment(s)
- `sgl-kernel/tests/test_flash_attention_4.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-02T17:01:09Z` `issue` by `cicirori`; signals: attention, cute, flash attention, kernel, sm100, tile; excerpt: "unit test ``` python sgl-kernel/tests/test flash attention 4.py ====================================== test session starts ======================================= platform linux -- Python 3.12.11, pytest-8.4.1, pluggy-1.6.0 rootdir: configfile: pyproject.toml plugins: ..." (https://github.com/sgl-project/sglang/pull/9928#issuecomment-3246121060)
- `2025-09-16T10:46:55Z` `issue` by `cicirori`; signals: cache, compile, correctness, cute, hang, kernel; excerpt: "I disabled the Cute DSL logs and added a more concise log for compile triggers. On the first call, I also added some known ..." (https://github.com/sgl-project/sglang/pull/9928#issuecomment-3297684067)
- `2025-09-02T16:55:22Z` `issue` by `cicirori`; signals: attention, benchmark, cache, flashinfer, fp4; excerpt: "Launch Command python3 -m sglang.launch server \ --model-path deepseek-v3-FP4 \ --trust-remote-code \ --quantization modelopt fp4 \ --tp-size 4 \ --ep-size 1 \ --model-loader-extra-config '{"enable ..." (https://github.com/sgl-project/sglang/pull/9928#issuecomment-3246105009)
- `2025-09-14T07:25:38Z` `issue` by `cicirori`; signals: attention, flashinfer, mla, moe; excerpt: "basline + --moe-runner-backend flashinfer trtllm + --moe-runner-backend flashinfer trtllm --attention-backend trtllm mla + --moe-runner-backend flashinfer trtllm --attention-backend trtllm mla when using hybrid attention backend ..." (https://github.com/sgl-project/sglang/pull/9928#issuecomment-3289306098)
- `2025-09-02T21:14:12Z` `inline` by `zhyncs` `sgl-kernel/pyproject.toml`:24; signals: blackwell, kernel; excerpt: "we don't want to introduce pip install sgl-kernel[blackwell]" (https://github.com/sgl-project/sglang/pull/9928#discussion_r2317189044)
- `2025-09-02T21:15:01Z` `inline` by `zhyncs` `sgl-kernel/pyproject.toml`:24; signals: kernel; excerpt: "how about add the dependency in" (https://github.com/sgl-project/sglang/pull/9928#discussion_r2317190257)
- `2025-09-02T22:56:25Z` `inline` by `zhyncs` `python/sglang/srt/models/deepseek_v2.py`:1738; signals: general review; excerpt: "ref" (https://github.com/sgl-project/sglang/pull/9928#discussion_r2317355160)
