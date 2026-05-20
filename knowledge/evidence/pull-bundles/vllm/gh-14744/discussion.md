# PR Discussion Digest

- Source PR: [vllm-project/vllm#14744](https://github.com/vllm-project/vllm/pull/14744)
- Source page: `sources/prs/vllm/PR-14744.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14744`
- Generated at: `2026-05-20T15:34:31.235483+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-13T09:23:10Z`
- Merged: `2025-03-25T09:35:00Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 13
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=5, outdated=4
- Human participants with discussion text: LucasWilkinson, gau-nernst, mergify
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-18T03:40:07Z` `COMMENTED` by `LucasWilkinson` - on first pass this looks good to me, left a few nits, will do a second pass in ... (https://github.com/vllm-project/vllm/pull/14744#pullrequestreview-2692810719)
- `2025-03-18T03:44:53Z` `COMMENTED` by `gau-nernst` (https://github.com/vllm-project/vllm/pull/14744#pullrequestreview-2692826360)
- `2025-03-21T04:47:49Z` `COMMENTED` by `gau-nernst` (https://github.com/vllm-project/vllm/pull/14744#pullrequestreview-2704723570)
- `2025-03-21T04:48:53Z` `COMMENTED` by `gau-nernst` (https://github.com/vllm-project/vllm/pull/14744#pullrequestreview-2704724553)
- `2025-03-22T00:16:47Z` `COMMENTED` by `LucasWilkinson` - Apologies for the delay! Overall I think this is quite close to mergable, just left a few comments (https://github.com/vllm-project/vllm/pull/14744#pullrequestreview-2706576392)
- `2025-03-22T00:49:26Z` `COMMENTED` by `gau-nernst` (https://github.com/vllm-project/vllm/pull/14744#pullrequestreview-2707624132)
- `2025-03-22T00:52:55Z` `COMMENTED` by `gau-nernst` (https://github.com/vllm-project/vllm/pull/14744#pullrequestreview-2707625910)
- `2025-03-22T00:53:31Z` `COMMENTED` by `gau-nernst` (https://github.com/vllm-project/vllm/pull/14744#pullrequestreview-2707626201)
- `2025-03-25T01:25:00Z` `APPROVED` by `LucasWilkinson` - LGTM, thanks for the contribution! (https://github.com/vllm-project/vllm/pull/14744#pullrequestreview-2712037755)

## Inline Comment Hotspots

- `vllm/attention/backends/cpu_mla.py`: 4 inline comment(s)
- `tests/kernels/test_cache.py`: 3 inline comment(s)
- `vllm/attention/backends/mla/common.py`: 2 inline comment(s)
- `csrc/cpu/mla_decode.cpp`: 2 inline comment(s)
- `vllm/platforms/cpu.py`: 1 inline comment(s)
- `.buildkite/run-cpu-test.sh`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-22T00:52:55Z` `inline` by `gau-nernst` `csrc/cpu/mla_decode.cpp`:223; signals: cache, hang, mla, register; excerpt: "When testing on my machine, 4 was worse than 2. I can try 3. It's likely depends on the CPU too (no. of registers ..." (https://github.com/vllm-project/vllm/pull/14744#discussion_r2008515801)
- `2025-03-22T00:53:31Z` `inline` by `gau-nernst` `tests/kernels/test_cache.py`:821; signals: cache, fp8, kernel, kv cache; excerpt: "Sure, I will remove it. I copied it from the GPU test. Was thinking it would still be useful once we add support for ..." (https://github.com/vllm-project/vllm/pull/14744#discussion_r2008515942)
- `2025-03-21T04:48:52Z` `inline` by `gau-nernst` `tests/kernels/test_cache.py`:764; signals: cache, cuda, kernel; excerpt: "In the future, we can merge this with the CUDA test of the same op (i.e. select correct device at runtime)" (https://github.com/vllm-project/vllm/pull/14744#discussion_r2006843660)
- `2025-03-22T00:16:08Z` `inline` by `LucasWilkinson` `tests/kernels/test_cache.py`:821; signals: cache, fp8, kernel; excerpt: "it doesnt look like fp8 is supported, I think we should remove this code if its not supported yet" (https://github.com/vllm-project/vllm/pull/14744#discussion_r2008498083)
- `2025-03-18T03:37:18Z` `inline` by `LucasWilkinson` `vllm/attention/backends/mla/common.py`:1351; signals: attention, mla; excerpt: "nit: I think . can be faster than getattr, is there a reason is profile run can't be in the attn metadata?" (https://github.com/vllm-project/vllm/pull/14744#discussion_r2000132754)
- `2025-03-18T03:44:53Z` `inline` by `gau-nernst` `vllm/attention/backends/mla/common.py`:1351; signals: attention, mla; excerpt: "CPUMLAMetadata (and TorchSDPAMetadata) doesn't have .is profile run. I can add that attribute and don't do anything with it." (https://github.com/vllm-project/vllm/pull/14744#discussion_r2000139670)
- `2025-03-21T04:47:49Z` `inline` by `gau-nernst` `.buildkite/run-cpu-test.sh`:42; signals: kernel, triton; excerpt: "pytest -v -s tests/kernels -m cpu model doesn't work due to Triton imports (there are probably other issues as well). We can have a ..." (https://github.com/vllm-project/vllm/pull/14744#discussion_r2006842894)
- `2025-03-21T16:40:17Z` `inline` by `LucasWilkinson` `vllm/attention/backends/cpu_mla.py`:122; signals: attention, mla; excerpt: "I think all of the above this is fine for now but we should see what we need to do to reuse more from ..." (https://github.com/vllm-project/vllm/pull/14744#discussion_r2007949706)
- `2025-03-22T00:09:12Z` `inline` by `LucasWilkinson` `csrc/cpu/mla_decode.cpp`:223; signals: mla, perf; excerpt: "nit: using a constexpr for the number of heads to compute (may be useful since I suspect it will perform better if this is ..." (https://github.com/vllm-project/vllm/pull/14744#discussion_r2008495458)
- `2025-03-18T03:38:48Z` `inline` by `LucasWilkinson` `vllm/attention/backends/cpu_mla.py`:235; signals: attention, mla; excerpt: "thanks for putting this in the subclass!" (https://github.com/vllm-project/vllm/pull/14744#discussion_r2000134418)
- `2025-03-21T16:36:50Z` `inline` by `LucasWilkinson` `vllm/attention/backends/cpu_mla.py`:128; signals: attention, mla; excerpt: "should we assert here since chunked prefill is not supported?" (https://github.com/vllm-project/vllm/pull/14744#discussion_r2007943950)
- `2025-03-22T00:49:26Z` `inline` by `gau-nernst` `vllm/attention/backends/cpu_mla.py`:128; signals: attention, mla; excerpt: "I have an assert in init (). That should be sufficient?" (https://github.com/vllm-project/vllm/pull/14744#discussion_r2008514976)
