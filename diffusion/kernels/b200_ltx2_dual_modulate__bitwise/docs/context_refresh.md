# RLCR Context Refresh

Per-round record of the kernel-optimization context consulted before choosing edits,
profiling, and benchmark/no-go decisions (source prompt, diffusion rules, current
evidence, KernelWiki, ncu-report-skill).

## Round 0

| Source consulted | How it shaped the decision |
|---|---|
| `prompt.md` (K/R/W) | K: rms_norm + dual `(1+scale)·normed+shift`; CA from `table+temb`. R: independent oracle + eager baseline. W: 12 frozen rows. → fixed the ABI/semantics the candidate must match. |
| `docs/baseline_source.md` + upstream re-check (`bb74ed4`) | Production norm is `RMSNormNoWeight → F.rms_norm` (unchanged on latest `main`). → chose **Strategy A** (reuse ATen `rms_norm`) for guaranteed bit-identical `normed`. |
| `docs/rms_norm_numerics.md` | Pinned the three bf16 affine rounding points, fp32-table→bf16-before-add, `unbind` order, and the "custom RMS is gated" rule. → affine implemented with `__fadd_rn`/`__fmul_rn`/`__float2bfloat16_rn` (no FMA/native bf16); Strategy B kept behind an RMS-only `torch.equal` + `rstd` ULP gate. |
| `../../docs/diffusion_kernel_rules.md`, `diffusion_correctness_contract.md`, `standalone_diffusion_benchmark.md` | Symmetric build/flags, no `--use_fast_math`, `torch.equal` (no tolerance), frozen workloads, idle-GPU rule, completion bar (per-shape stats + roofline/NCU + provenance + PR hygiene). → drove the build mirror, the correctness-coverage extension, the benchmark protocol, and the docs set. |
| `external/KernelWiki/SKILL.md` | Memory-bound elementwise pattern guidance (coalesced/vectorized access, occupancy). → after profiling showed the affine at 14% peak BW, vectorized the dominant `normed`/`y0`/`y1` traffic to 16-byte `int4` (memory only; math unchanged), lifting geomean 2.28×→3.54×. |
| `external/ncu-report-skill/SKILL.md` | Profile→diagnose→plan; one run dir; B200 metric-name caveats; cite specific metrics. → ran NCU `--set basic` on a small audio row and the huge video row; cited Memory(L1TEX)/DRAM/Compute/Occupancy. Diagnosis: video affine **L1TEX-bound** (DRAM 22.6%), audio launch-bound. |
| Current benchmark/profile evidence (`bench/results.jsonl`, event-split diagnostic) | rms_norm already ~81% of peak (shared, not improvable in Strategy A); affine dominates and had headroom. → optimization targeted the affine; Strategy B **rejected** by gate (every row already wins ≥2.42×, geomean 3.54×, no regression). |

## Round 1

| Source consulted | How it shaped the decision |
|---|---|
| Round-0 Codex review | Identified evidence/doc completion gaps (a stale correctness count, an NCU command not reproducible from the repo, and a missing context-refresh record). → this round reconciles every count to the actual `1819/0` run, adds the checked-in `bench/ncu_run.py` replay harness + workload-id NCU commands, and adds this record. No kernel/perf change. |
| `.humanize/bitlesson.md` (BL-20260629-ltx2-dualmod-bitexact) | Confirms the `1819/0` count and the frozen-`workloads.json` construction approach. → `bench/ncu_run.py` builds the profiled workload through `bench/adapter.py` (same frozen shapes/strides) and runs only the candidate. |
| `external/KernelWiki`, `external/ncu-report-skill` | No new query needed this round — it is documentation/provenance reconciliation only; the kernel and its diagnosed bound are unchanged from Round 0. |
