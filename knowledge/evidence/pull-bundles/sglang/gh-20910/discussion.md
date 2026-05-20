# PR Discussion Digest

- Source PR: [sgl-project/sglang#20910](https://github.com/sgl-project/sglang/pull/20910)
- Source page: `sources/prs/sglang/PR-20910.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-20910`
- Generated at: `2026-05-20T15:29:08.004849+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-19T05:39:12Z`
- Merged: `2026-03-22T08:39:40Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 14 (approved=1, changes_requested=2, commented=11)
- Inline review comments: 20
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=6, outdated=10
- Human participants with discussion text: BBuf, DarkSharpness, merrymercy
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-19T08:56:02Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3973668412)
- `2026-03-19T09:33:06Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3973864775)
- `2026-03-20T02:18:31Z` `CHANGES_REQUESTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3978958701)
- `2026-03-20T04:19:16Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3979296411)
- `2026-03-20T04:19:22Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3979297007)
- `2026-03-20T04:19:28Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3979297732)
- `2026-03-20T04:19:34Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3979298354)
- `2026-03-20T04:19:39Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3979298869)
- `2026-03-20T07:34:14Z` `CHANGES_REQUESTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3979938085)
- `2026-03-20T08:38:59Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3980224269)
- `2026-03-20T08:39:06Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3980224698)
- `2026-03-20T08:39:12Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3980225046)
- `2026-03-20T08:39:19Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3980225548)
- `2026-03-22T08:33:29Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/20910#pullrequestreview-3987903700)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/debug_utils.py`: 2 inline comment(s)
- `docs/references/environment_variables.md`: 2 inline comment(s)
- `python/sglang/api_logging.py`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/bitsandbytes.py`: 2 inline comment(s)
- `python/sglang/srt/models/kimi_vl_moonvit.py`: 2 inline comment(s)
- `sgl-kernel/python/sgl_kernel/flash_attn.py`: 2 inline comment(s)
- `.claude/skills/debug-cuda-crash/SKILL.md`: 2 inline comment(s)
- `python/sglang/jit_kernel/diffusion/triton/norm.py`: 2 inline comment(s)
- `python/sglang/jit_kernel/diffusion/triton/scale_shift.py`: 2 inline comment(s)
- `python/sglang/srt/models/minimax_m2.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-19T06:10:27Z` `issue` by `BBuf`; signals: cuda, failing, kernel, nan; excerpt: "Validated the CUDA crash debugging flow on a real 7B model: Qwen/Qwen2.5-7B-Instruct. For validation, I used a temporary fault-injection script that monkey-patches the model's ..." (https://github.com/sgl-project/sglang/pull/20910#issuecomment-4088048145)
- `2026-03-19T08:54:36Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/debug_utils.py`:5; signals: kernel, register; excerpt: "Could we make it a typing-friendly decorator (like register custom op)? Also, when used with custom op registration, we need to keep the signature ..." (https://github.com/sgl-project/sglang/pull/20910#discussion_r2958658704)
- `2026-03-20T02:14:02Z` `inline` by `merrymercy` `docs/references/environment_variables.md`:154; signals: cuda, kernel; excerpt: "SGLANG API is too broad. Can you rename all env vars to SGLANG CUDA API LOGLEVEL or SGLANG KERNEL API LOGLEVEL?" (https://github.com/sgl-project/sglang/pull/20910#discussion_r2963621125)
- `2026-03-20T02:16:32Z` `inline` by `merrymercy` `python/sglang/api_logging.py`:1; signals: flashinfer, kernel; excerpt: "It is okay to call it "api logging" for flashinfer because the api of flashinfer is all kernels. It is not very precise to ..." (https://github.com/sgl-project/sglang/pull/20910#discussion_r2963626256)
- `2026-03-20T07:31:37Z` `inline` by `merrymercy` `python/sglang/jit_kernel/diffusion/triton/norm.py`:644; signals: kernel, triton; excerpt: "why do we need to manually give it a name? It should be able to auto infer the op name" (https://github.com/sgl-project/sglang/pull/20910#discussion_r2964367038)
- `2026-03-20T07:31:59Z` `inline` by `merrymercy` `python/sglang/jit_kernel/diffusion/triton/scale_shift.py`:738; signals: kernel, triton; excerpt: "this is too tedious. The decorator should auto infer the name" (https://github.com/sgl-project/sglang/pull/20910#discussion_r2964367951)
- `2026-03-20T08:39:06Z` `inline` by `BBuf` `python/sglang/jit_kernel/diffusion/triton/norm.py`:644; signals: kernel, triton; excerpt: "Done" (https://github.com/sgl-project/sglang/pull/20910#discussion_r2964583110)
- `2026-03-20T08:39:12Z` `inline` by `BBuf` `python/sglang/jit_kernel/diffusion/triton/scale_shift.py`:738; signals: kernel, triton; excerpt: "Done" (https://github.com/sgl-project/sglang/pull/20910#discussion_r2964583454)
- `2026-03-19T09:33:06Z` `inline` by `BBuf` `python/sglang/jit_kernel/debug_utils.py`:5; signals: kernel; excerpt: "Done in" (https://github.com/sgl-project/sglang/pull/20910#discussion_r2958845981)
- `2026-03-20T02:17:51Z` `inline` by `merrymercy` `python/sglang/srt/models/kimi_vl_moonvit.py`:70; signals: kernel; excerpt: "debug kernel api?" (https://github.com/sgl-project/sglang/pull/20910#discussion_r2963628775)
- `2026-03-20T02:18:26Z` `inline` by `merrymercy` `sgl-kernel/python/sgl_kernel/flash_attn.py`:5; signals: kernel; excerpt: "maybe wrap debug kernel" (https://github.com/sgl-project/sglang/pull/20910#discussion_r2963630008)
- `2026-03-20T04:19:39Z` `inline` by `BBuf` `sgl-kernel/python/sgl_kernel/flash_attn.py`:5; signals: kernel; excerpt: "done" (https://github.com/sgl-project/sglang/pull/20910#discussion_r2963877604)
