# PR Discussion Digest

- Source PR: [sgl-project/sglang#5587](https://github.com/sgl-project/sglang/pull/5587)
- Source page: `sources/prs/sglang/PR-5587.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-5587`
- Generated at: `2026-05-20T15:30:28.036942+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-20T23:28:25Z`
- Merged: `2025-05-05T17:32:02Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 19 (approved=1, changes_requested=1, commented=17)
- Inline review comments: 19
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=4
- Human participants with discussion text: Fridge003, PopSoda2002, merrymercy
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-24T17:55:42Z` `APPROVED` by `Fridge003` - LGTM (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2792056314)
- `2025-04-27T02:01:42Z` `COMMENTED` by `merrymercy` - Can you add your test case here so it can run on CI? (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2796843053)
- `2025-04-27T02:02:44Z` `CHANGES_REQUESTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2796847721)
- `2025-04-30T03:45:02Z` `COMMENTED` by `PopSoda2002` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2805631960)
- `2025-04-30T03:45:34Z` `COMMENTED` by `PopSoda2002` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2805632798)
- `2025-04-30T03:45:40Z` `COMMENTED` by `PopSoda2002` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2805632895)
- `2025-04-30T07:21:03Z` `COMMENTED` by `PopSoda2002` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2806042560)
- `2025-05-03T02:22:56Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2813118746)
- `2025-05-03T02:28:43Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2813119700)
- `2025-05-03T02:36:31Z` `COMMENTED` by `PopSoda2002` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2813121969)
- `2025-05-03T02:37:15Z` `COMMENTED` by `PopSoda2002` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2813122100)
- `2025-05-03T02:40:38Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2813122707)
- `2025-05-03T06:25:02Z` `COMMENTED` by `PopSoda2002` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2813168806)
- `2025-05-03T06:28:35Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2813169304)
- `2025-05-03T06:29:31Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2813169424)
- `2025-05-03T06:31:08Z` `COMMENTED` by `PopSoda2002` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2813169623)
- `2025-05-03T06:32:43Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2813169810)
- `2025-05-03T06:39:46Z` `COMMENTED` by `PopSoda2002` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2813170787)
- `2025-05-03T06:39:59Z` `COMMENTED` by `PopSoda2002` (https://github.com/sgl-project/sglang/pull/5587#pullrequestreview-2813170837)

## Inline Comment Hotspots

- `sgl-kernel/CMakeLists.txt`: 8 inline comment(s)
- `test/srt/test_flash_mla_attention_backend.py`: 7 inline comment(s)
- `scripts/ci_install_dependency.sh`: 4 inline comment(s)

## High-Signal Discussion

- `2025-05-03T06:25:02Z` `inline` by `PopSoda2002` `sgl-kernel/CMakeLists.txt`:100; signals: block, hang, kernel; excerpt: "Yes, I will move this change to another PR. But It seems this PR would be blocked before that one merged" (https://github.com/sgl-project/sglang/pull/5587#discussion_r2072332012)
- `2025-04-30T07:21:03Z` `inline` by `PopSoda2002` `test/srt/test_flash_mla_attention_backend.py`:85; signals: attention, mla, triton; excerpt: "sry, just deleted the gsm8k metrics which aligns with test/srt/test triton attention backend.py" (https://github.com/sgl-project/sglang/pull/5587#discussion_r2068040058)
- `2025-05-03T02:22:56Z` `inline` by `Fridge003` `sgl-kernel/CMakeLists.txt`:100; signals: kernel, mla; excerpt: "I feel the work of integrating flashmla into sgl-kernel can be moved to another PR. Just opened an issue for this task ( 5989)" (https://github.com/sgl-project/sglang/pull/5587#discussion_r2072290869)
- `2025-05-03T02:28:43Z` `inline` by `Fridge003` `scripts/ci_install_dependency.sh`:36; signals: kernel, mla; excerpt: "For now this line is for passing flashmla tests in CI. After integrating flashmla into sgl-kernel, this line should be removed." (https://github.com/sgl-project/sglang/pull/5587#discussion_r2072291927)
- `2025-04-27T02:00:25Z` `inline` by `merrymercy` `test/srt/test_flash_mla_attention_backend.py`:29; signals: attention, mla; excerpt: "remove this?" (https://github.com/sgl-project/sglang/pull/5587#discussion_r2061940905)
- `2025-04-27T02:01:03Z` `inline` by `merrymercy` `test/srt/test_flash_mla_attention_backend.py`:85; signals: attention, mla; excerpt: "can it be this high?" (https://github.com/sgl-project/sglang/pull/5587#discussion_r2061941761)
- `2025-04-27T02:02:40Z` `inline` by `merrymercy` `test/srt/test_flash_mla_attention_backend.py`:20; signals: attention, mla; excerpt: "please use from sglang.test.test utils import DEFAULT MLA MODEL NAME FOR TEST" (https://github.com/sgl-project/sglang/pull/5587#discussion_r2061943287)
- `2025-04-30T03:45:02Z` `inline` by `PopSoda2002` `test/srt/test_flash_mla_attention_backend.py`:29; signals: attention, mla; excerpt: "has updated into flashmla" (https://github.com/sgl-project/sglang/pull/5587#discussion_r2067805951)
- `2025-04-30T03:45:34Z` `inline` by `PopSoda2002` `test/srt/test_flash_mla_attention_backend.py`:85; signals: attention, mla; excerpt: "I tested by myself, it can pass, let me double check" (https://github.com/sgl-project/sglang/pull/5587#discussion_r2067806295)
- `2025-04-30T03:45:40Z` `inline` by `PopSoda2002` `test/srt/test_flash_mla_attention_backend.py`:20; signals: attention, mla; excerpt: "Done!" (https://github.com/sgl-project/sglang/pull/5587#discussion_r2067806360)
- `2025-05-03T02:40:38Z` `inline` by `Fridge003` `sgl-kernel/CMakeLists.txt`:100; signals: hang, kernel; excerpt: "Can you please restore the changes in this file?" (https://github.com/sgl-project/sglang/pull/5587#discussion_r2072294059)
- `2025-05-03T02:36:31Z` `inline` by `PopSoda2002` `sgl-kernel/CMakeLists.txt`:100; signals: kernel; excerpt: "Yeah sure, I will take it! Thanks a lot" (https://github.com/sgl-project/sglang/pull/5587#discussion_r2072293336)
