# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#14344](https://github.com/NVIDIA/TensorRT-LLM/pull/14344)
- Source page: `sources/prs/tensorrt-llm/PR-14344.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-14344`
- Generated at: `2026-05-20T15:19:11.419239+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-20T07:16:12Z`
- Merged: `2026-05-20T07:35:19Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 7
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=0
- Human participants with discussion text: QiJune, coderabbitai, kaiyux, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-20T07:20:11Z` `APPROVED` by `QiJune` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/14344#pullrequestreview-4326056893)
- `2026-05-20T07:23:24Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 7 🧹 Nitpick comments (9) .claude/skills/perf-host-optimization/references/patterns/gpu-graph.md (2) 122-130: ⚡ Quick win Add language specifier to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/14344#pullrequestreview-4326080193)

## Inline Comment Hotspots

- `.claude/skills/perf-host-analysis/scripts/detect_host_overhead.py`: 3 inline comment(s)
- `.claude/skills/ad-layer-visualizer/scripts/extract_trace_kernels.py`: 1 inline comment(s)
- `.claude/skills/ad-layer-visualizer/scripts/render_layer.py`: 1 inline comment(s)
- `.claude/skills/perf-host-analysis/SKILL.md`: 1 inline comment(s)
- `.claude/skills/perf-host-optimization/references/patterns/compound-pitfalls.md`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-20T07:23:24Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, attention, benchmark, block, cuda, cute, hang, kernel; excerpt: "Actionable comments posted: 7 🧹 Nitpick comments (9) .claude/skills/perf-host-optimization/references/patterns/gpu-graph.md (2) 122-130: ⚡ Quick win Add language specifier to fenced code block. The code block ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14344#pullrequestreview-4326080193)
- `2026-05-20T07:23:18Z` `issue` by `coderabbitai`; signals: accuracy, alignment, attention, cache, cuda, cute, hang, kernel; excerpt: "📝 Walkthrough Walkthrough This PR adds comprehensive documentation and tooling for AutoDeploy, performance analysis, and TensorRT-LLM MoE development. Key changes include CPU-based testing alignment, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14344#issuecomment-4495658378)
- `2026-05-20T07:23:22Z` `inline` by `coderabbitai` `.claude/skills/perf-host-analysis/SKILL.md`:233; signals: block, hang, kernel, perf; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win Add a language identifier to the fenced code block. The example block is missing a fence ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14344#discussion_r3271969223)
- `2026-05-20T07:23:21Z` `inline` by `coderabbitai` `.claude/skills/ad-layer-visualizer/scripts/extract_trace_kernels.py`:109; signals: benchmark, kernel, race; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Harden external command execution for nsys resolution. Line 106 starts nsys via PATH lookup. In shared ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14344#discussion_r3271969176)
- `2026-05-20T07:23:22Z` `inline` by `coderabbitai` `.claude/skills/perf-host-analysis/scripts/detect_host_overhead.py`:196; signals: kernel, perf; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win M3 exposed-time calculation misses boundary idle gaps. Idle gaps are only computed between kernels. If host ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14344#discussion_r3271969208)
- `2026-05-20T07:23:22Z` `inline` by `coderabbitai` `.claude/skills/perf-host-analysis/scripts/detect_host_overhead.py`:367; signals: kernel, perf; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Error payload from detect() can crash report rendering. When no kernels are found, detect() returns an ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14344#discussion_r3271969218)
- `2026-05-20T07:23:22Z` `inline` by `coderabbitai` `.claude/skills/perf-host-optimization/references/patterns/compound-pitfalls.md`:94; signals: perf, performance; excerpt: "⚠️ Potential issue 🟡 Minor ⚡ Quick win The ternary vs attribute access comparison is misleading. The "SEEMS FASTER" and "ACTUALLY FASTER" examples are ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14344#discussion_r3271969226)
- `2026-05-20T07:23:22Z` `inline` by `coderabbitai` `.claude/skills/perf-host-analysis/scripts/detect_host_overhead.py`:119; signals: perf; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Phase-window queries are not overlap-safe, which skews per-phase metrics. Windowed queries currently filter by interval start ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14344#discussion_r3271969203)
- `2026-05-20T07:23:22Z` `inline` by `coderabbitai` `.claude/skills/ad-layer-visualizer/scripts/render_layer.py`:540; signals: general review; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Resolve dot to an absolute executable path before spawn. Line 535 launches dot via PATH lookup. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14344#discussion_r3271969197)
- `2026-05-20T07:35:15Z` `issue` by `tensorrt-cicd`; signals: general review; excerpt: "[PR Github 49390]( [ skip ] completed with state SUCCESS. Commit: 03d8c76 Skipping testing for commit 03d8c76 [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/14344#issuecomment-4495767476)
