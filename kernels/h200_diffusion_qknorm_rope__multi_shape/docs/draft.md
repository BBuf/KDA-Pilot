# Continuation Round Draft — h200_diffusion_qknorm_rope__multi_shape (2026-06-04)

Implementation-plan draft for the continuation round executed under Humanize RLCR
(plan: `.humanize/kernel-agent/refined-plan.md`, untracked). This file is the
Workspace-Rule-required in-folder draft and the round's provenance + decision log.

## Continuation provenance

- **Incumbent (the candidate under audit)**: `d3-final-corrected`, native CUDA
  `fused_inplace_qknorm_rope` in `src/csrc/qknorm_rope_kernel.cuh`,
  **src sha16 `4f70cda745940c96`** (re-verified in this worktree 2026-06-04 via
  `shasum -a 256 src/csrc/qknorm_rope_kernel.cuh | cut -c1-16`).
- **Promotion state**: promoted via PR #19 (repo commit `187b45781`) into
  `kda_kernels/diffusion/qknorm_rope/_impls/h200/` under the jit_kernel/tvm-ffi
  export model; in-SGLang in-tree drop-in arbiter PASS (smoke geomean 1.0452×);
  install()-overlay validation 1.012–1.018× all-9 (`profile/integration/REPORT.md`).
- **Ground truth declaration**: `docs/final_result.md` (tvm-ffi re-run: all-9
  geomean **wrapper 1.0723× / module 1.0268×**, large module 1.069–1.085×, tiny
  launch-bound ~0.99× module) **supersedes** the stale
  `## Final Result (RLCR rounds 0-3, 2026-06-01)` section embedded in `prompt.md`
  (torch-extension/EXPORTS era, ~1.11×, overlay #17 — later reset by `35bc2c6b4`).
  `prompt.md` gets a Final-Result refresh at this round's wrap-up.
- **Solutions DAG tail**: d0-baseline-clone → d1-lean-dispatch → d2-warp2
  (superseded) → **d3-final-corrected** (FINAL) → export-real-in-sglang (PASS).
  This round's entries parent-link to `d3-final-corrected`.
- **Evidence pointer audit**: `scripts/check_evidence.py` → ALL_EVIDENCE_RESOLVES
  OK (24 paths), 2026-06-04.

## SGLang pin + drift check (DEC-3)

- **Pin: `c47f0e7cd`** (sglang 0.5.12.dev472) — the commit the incumbent's
  committed evidence used (remote `repos/sglang`).
- Drift check on the local checkout (`/Users/bbuf/工作目录/Common/sglang`, HEAD
  `0689ba84b8`, `c47f0e7cd` IS an ancestor): `git log c47f0e7cd..HEAD --` shows
  **zero commits** touching `python/sglang/jit_kernel/diffusion/qknorm_rope.py`,
  `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh`, or
  `python/sglang/jit_kernel/tests/diffusion/test_qknorm_rope.py`; one
  MUSA-only `utils.py` change (`be32df33b9`) — non-functional for NVIDIA/H200.
  Public op confirmed `@register_custom_op(mutates_args=["q","k"])`; baseline
  kernel PDL-templated and runtime-gated by `is_arch_support_pdl()`.
- **Remote-side verification required before any measurement (k09 baseline-shift
  trap)**: on the remote box, check ancestry BOTH directions
  (`git merge-base --is-ancestor` each way) between `c47f0e7cd` and the
  container's `repos/sglang` HEAD AND `git diff c47f0e7cd..HEAD -- <the 3 files>`;
  a non-empty diff with an empty per-path log means changes live on the other
  side. Record the result here before trusting any baseline number.

## Round scope and decisions (from the gen-plan convergence)

- **DEC-1 margin bar**: re-promotion only on ≥3% all-9 module-level geomean over
  the incumbent in one clean run, OR ≥1.5% reproduced in ≥2 independent
  interleaved A/B/C runs — and no per-shape regression beyond noise (large
  protected, tiny within noise).
- **DEC-2 scope**: audit + exactly the two named directions below, ≤2 focused
  iterations each; a third direction only if fresh NCU evidence overturns the
  prior bound analysis. Tiny shapes (T≤195): protect-from-regression only —
  launch/underfill kernel no-go stands (occ 12.4%, 0.07 waves/SM).
- **DEC-3 pin**: SGLang `c47f0e7cd` (above).
- Geomean speedup = outcome metric, not pass/fail; completion = correctness +
  hardware-bound evidence or well-supported no-go.

## Ranked directions for this round

Prior bound analysis (`docs/perf_analysis.md`, `profile/round_warp2/REPORT.md`):
large shapes memory-LATENCY-bound (long-scoreboard 58.2%, DRAM 39.6% of peak,
L2 hit 49.9%, occ 72.7%/75% theoretical, 38 reg/thread); verdict was "near the
attainable bound". The two named-but-unpursued directions, ranked:

1. **cos/sin access optimization (warp2 path)** — expected benefit: moderate
   (attacks the dominant long-scoreboard stall chain); risk: low→moderate.
   - 1a (try first): **vectorized cos/sin loads** — GPT-J pairing gives each
     lane 4 contiguous cos floats + 4 contiguous sin floats (`half_idx =
     lane_in_head*4 + pair`), so two 128-bit loads replace 8 scalar loads.
     No sync, no occupancy effect.
   - 1b (only if 1a leaves evidence of remaining cos/sin-side stalls):
     **shared-memory staging** of the 512 B per-token cos/sin row (work items
     are head-major within a token → strong intra-CTA token locality; ~48
     items/token). Risk: block-wide sync on a ~40 µs kernel; payoff is latency-
     chain shortening, NOT bandwidth (DRAM far from saturated).
2. **register-pressure reduction** — expected benefit: bounded (occupancy
   75%→100% theoretical requires 38→≤32 regs/thread); risk: moderate (spills,
   or no latency gain since the kernel is latency/issue-bound and the warp2 win
   came from wider per-warp memory work DESPITE lower occupancy; row-norm
   kernels on this hardware are typically latency/issue-bound, not DRAM-bound).
   Levers to try (mechanism-verified via `-Xptxas -v` + NCU launch stats):
   `__launch_bounds__(256, <min_blocks>)`, 32-bit index arithmetic where ranges
   allow, overlapping input-vector/normalized-value lifetimes, recomputing base
   pointers. Reject on spill-induced large-shape regression.

Adjudication: same-process interleaved **A/B/C** (A = SGLang baseline op,
B = incumbent module build, C = variant module build; distinct `load_jit`
markers via source-sha; rotated call order; q/k reset outside timed region;
module-level decides the kernel; wrapper-level reported for completeness).
NCU (`profile/<run_name>/` pattern, `-lineinfo`, full+source sets) whenever a
result — win or loss — is not fully understood.

## Remote session record (2026-06-04)

- Host: **ion8-h200** (hostname `ion-h200-8`).
- Container: **`sglang_bbuf`** (up; the prior round's `sglang_omni_bbuf_kda` no
  longer exists on the box).
- **Toolchain drift vs committed evidence (documented, accepted)**: container has
  Python 3.12.3, **torch 2.11.0+cu130, nvcc 13.0**, flashinfer 0.6.11.post1 —
  committed d3-final evidence used torch 2.9.1+cu129 / nvcc 12.9. Both audit
  legs (baseline + incumbent) compile under the SAME toolchain, so speedup
  ratios stay comparable; absolute latencies and the 38-reg/thread figure must
  be re-established under nvcc 13 before direction-2 work.
- REMOTE_GPU_ID: **7** (util 0%, 50 MiB residual, no compute procs at selection
  time — same physical card as the committed d3-final rows; GPUs 0–3 also fully
  idle as fallback). GPUs 4–6 busy (~120–143 GiB used).
- REMOTE_KDA_DIR:
  `/home/sglang-omni/bbuf/kda_runs/h200_diffusion_qknorm_rope__multi_shape/k04-20260604-185804`
  (staged: `src/`, `tests/`, `scripts/`, `benchmark.py`, `bench_remote.py`,
  `sglang_pin/`; remote `src/csrc/qknorm_rope_kernel.cuh` sha16 re-verified
  `4f70cda745940c96`).
- **SGLang pin realized as a detached worktree**: `${REMOTE_KDA_DIR}/sglang_pin`
  @ `c47f0e7cdde4` (created from `repos/sglang`; `repos/sglang` itself untouched
  at HEAD `84e1108312b5`). Baseline-shift check (k09): pin IS ancestor of remote
  HEAD (no rewind); per-path log AND both-direction diffs for
  `qknorm_rope.py` / `csrc/diffusion/qknorm_rope.cuh` / the reference test are
  ALL EMPTY — remote HEAD's qknorm_rope files are byte-identical to the pin.
  jit_kernel infra (utils.py/csrc) has 8 unrelated commits pin..HEAD
  (KV-canary, MUSA, ngram) — irrelevant because all runs use the pin worktree's
  PYTHONPATH.
- Harness: `bench_remote.py` copied verbatim from the prior session
  (`k04-20260601-225112`, the dir that produced the committed tag=d3-final
  rows), with ONE surgical patch: the self-recorded command string now reads
  the actual `PYTHONPATH` from the environment instead of a hardcoded
  `repos/sglang` path (timing logic untouched). Import smoke on the pinned
  stack: baseline module resolves into `sglang_pin`, flashinfer rope + task
  wrapper import OK, CUDA available.
- GPU state before/after each measurement batch: recorded in `benchmark.csv`
  rows (`gpu_idle_before/after`) and/or `docs/evidence/gpu_state_*.md`.

## Operational cautions (project memory, k09 traps)

- **BASELINE SHIFT**: shared-container SGLang checkouts have been rewound
  between runs before. Verify ancestry both directions + per-file diff vs the
  pin before every benchmark session; benchmark legs must be same-process paired.
- **EVIDENCE LOSS BY RE-SYNC**: never full-folder re-sync over the remote
  workspace after benchmarks start; pull appended evidence (benchmark rows,
  logs) back to local BEFORE any re-sync; sync source paths only.

## KernelWiki / ncu-report-skill context log (per RLCR iteration)

- 2026-06-04 round 0 start: both submodules initialized
  (KernelWiki @ `faed56ce`, ncu-report-skill @ `d1887948`); both SKILL.md read.
  KernelWiki note: knowledge cutoff 2026-04-27; Blackwell-first — SM90 pages
  carry explicit `blackwell_relevance`; queries to run before direction-1
  coding: `"fused RMS norm + RoPE inplace"`, `--tag qk-norm --type kernel`,
  `--repo flashinfer --tag rope`. ncu skill note: B200-flavored metric names
  doc exists (`reference/08`); H200/sm_90 metric names may differ — enumerate
  via `action.metric_names()` when parsing. No new query needed for task1/task2
  (workspace restoration — no kernel-design choice at stake).

## Iteration log

- 2026-06-04 (pre-audit, while correctness suite runs): KernelWiki direction-1
  prior-art queries executed. `"fused RMS norm + RoPE inplace"` surfaced two
  directly-relevant pages: **pr-TensorRT-LLM-13052** (fused cross-head QKNorm +
  RoPE for WAN, sm100, 2026-04 — summary states "CTA-level shared-me[mory]"
  usage; page is summary-only, no vendored kernel source, so the exact smem
  role (cos/sin vs qkv staging) is unknown → treated as corroborating-but-non-
  specific support for direction 1b) and **pr-TensorRT-LLM-11869** (fused DiT
  QKNorm+RoPE for FLUX — same kernel family, fusion-motivation only).
  `--tag qk-norm` and `--repo flashinfer --tag rope` returned no pages.
  Conclusion: no prior-art change to the ranked plan — 1a (vectorized float4
  cos/sin loads) first, 1b (smem staging) only on residual cos/sin-stall
  evidence.
- 2026-06-04 AUDIT (tag `continuation-audit`, sha `4f70cda745940c96`, GPU 7,
  externally idle before util=0%/50MiB, after util=3%/50MiB — own process tail):
  **correctness 225/225 pass** (154 s; `docs/evidence/correctness_audit_r0.log`);
  **benchmark module geomean 1.0366×** (committed 1.0268× → ratio 1.0095, inside
  the ±3% AC window), large-shape module 1.072/1.083/1.084/1.084 (committed
  band 1.069–1.085 — near-exact), tiny module flat 1.000 (committed 0.985–0.993).
  **Wrapper geomean 1.0236×** vs committed 1.0723× — DIVERGENT, cause identified:
  on this stack (torch 2.11.0+cu130, container `sglang_bbuf`) the tiny-shape
  wrapper-level lean-dispatch advantage narrowed to ~parity (committed tiny
  wrapper 1.051–1.090 → now 0.995–1.017; absolute wrapper overhead grew ~+1.2 µs
  baseline / ~+2.2 µs candidate, while module-level tiny costs grew ~+1 µs on
  BOTH legs equally). Host-layer effect only — module level (the admissible
  kernel signal and the AC-2.2 gate) reproduces. Audit verdict: kernel-level
  REPRODUCED; exploration may open pending Codex adjudication (task5). Evidence:
  `benchmark.csv` rows tag=continuation-audit,
  `docs/evidence/bench_summary_continuation-audit.json`,
  `docs/evidence/bench_audit_r0.log`.
- 2026-06-04 DIRECTION 1 iteration 1 (`cossin-vec`, src sha16 `6669bd218e336c9d`):
  replaced the warp2 rope section's eight scalar `__ldg` cos/sin loads per lane
  with two 128-bit `__ldg(float4)` loads (per-lane quartets are consecutive:
  half_idx = lane_in_head*4 + 0..3) + host-side 16B-alignment guard on the
  cache base routing misaligned bases to the one-head scalar path. Correctness:
  captured slice 72/72 BEFORE benchmark claims, full suite 225/225 BEFORE keep.
  Interleaved A/B/C module-level (3 rotated blocks × 100 iters/leg, externally
  idle 0%/50MiB before AND after): **var/inc all-9 geomean 1.0622×, large
  1.1424× (1.134–1.148), tiny 0.997–1.011 (noise)**; var/sgl all-9 1.1009×,
  large 1.2373×; inc/sgl 1.0364× (reproduces audit 1.0366× — internal
  consistency). KEEP — clears the decided margin (≥3% one clean run) on
  iteration 1. NCU confirmation round launched (`profile/round_cossin_vec/`):
  confirm mechanism (long-scoreboard reduction), get nvcc-13 regs/thread for
  both builds (direction-2 calibration), decide whether 1b (smem staging) has
  remaining headroom or is skipped with evidence. KernelWiki context: no new
  query needed this iteration — the edit followed the pre-logged 1a design;
  prior-art pages pr-TensorRT-LLM-13052/11869 already recorded above.
- 2026-06-04 NCU ROUND (`profile/round_cossin_vec/`, REPORT.md committed; reports
  on REMOTE_KDA_DIR): mechanism CONFIRMED with a second-order surprise — the
  float4 rewrite dropped **registers 38→32/thread**, unlocking **100%
  theoretical / 90.4% achieved occupancy** (was 75%/72.5%) and growing the
  occupancy-capped grid 792→1056; memory throughput 2.005→2.245 TB/s; duration
  38.13→33.97 µs (matches A/B/C 1.1344×). Long-scoreboard attribution: 45% q/k
  input unpack (irreducible), 34% norm chain, 14.5% positions→LEA, **only ~6%
  cos/sin consumers → direction 1b (smem staging) SKIPPED with evidence**.
  **Direction 2 RESOLVED-BY-DIRECTION-1**: regs already at the 32-reg/100%
  occupancy boundary; <32 has no theoretical upside (2048 threads/SM ceiling),
  spills risk only. No separate direction-2 iteration warranted.
- 2026-06-04 DIRECTION 1 iteration 2 (`cossin-vec2`, src sha16
  `51e183ba29abd455`): hoisted pos + cos/sin quartet fetches above the RMS
  reduction (latency hides under norm math — targets the 14.5% positions→LEA
  stall share). Slice 72/72. Interleaved A/B/C (B=cossin-vec v1, C=v2):
  **v2/v1 large geomean 1.0148× (1.013–1.018), all-9 1.0090×, tiny parity**;
  v1/sglang large 1.2356× here vs 1.2373× in run 1 — 0.14% cross-run delta,
  methodology reproducible. Confirmation batch: v2 register check
  (must stay ≤32), second interleaved run, full suite.
- 2026-06-04 ITERATION 2 VERDICT: **REJECT `cossin-vec2`** — NCU basic set shows
  **40 regs/thread** (v1: 32), theoretical occupancy 75% (v1: 100%), achieved
  63.8–65.0% (v1: 90.4%): the hoist holds the quartets live across the
  reduction. Second interleaved run shrank v2/v1 to large 1.0085× / all-9
  1.0018× (run 1: 1.0148/1.0090) — small + unstable, and the pre-declared
  regs≤32 rule is violated. v2 full suite 225/225 (correctness was never the
  issue). Source restored byte-identical to v1 `6669bd218e336c9d` local+remote.
  **DIRECTION 1 CLOSED at 2/2 iterations: FINAL = `cossin-vec` v1.**
  **DIRECTION 2 CLOSED (resolved-by-direction-1, NCU mechanism evidence in
  `profile/round_cossin_vec/REPORT.md`): regs already 32 = the 100%-occupancy
  boundary; <32 has no theoretical upside.** Cumulative final-candidate
  evidence vs incumbent d3-final: all-9 module geomean 1.0622×, large 1.1424×
  (single clean interleaved run, externally idle); v1-vs-SGLang large geomean
  reproduced 1.2373/1.2356/1.2367 across three interleaved runs.
- 2026-06-04 DECISION GATE (Codex, `.humanize` skill log + verdict quoted in
  round summary): **OUTCOME_A** — margin bar cleared (6.2% > 3% single clean
  run); one A/B/C run sufficient given mechanism evidence + cross-run B-leg
  reproducibility; REQUIREMENT added before accepting the arbiter: a dedicated
  forced-misaligned cos/sin-cache negative test (contiguous [rows,128] f32,
  `data_ptr()%16!=0`, through the public in-tree op, vs the split oracle).
  Implemented twice: `tests/test_correctness.py::
  test_misaligned_cos_sin_cache_still_oracle_correct` (permanent regression
  coverage via the KDA wrapper) and `export_misaligned.py` (arbiter-side,
  in-tree public op). Arbiter strictness honored: arbiter tree's `.cuh` hash
  verified `6669bd218e336c9d`, `.cuh`-only placement, no monkeypatch, separate
  processes for candidate (sglang_arbiter) vs baseline (sglang_pin), both at
  `c47f0e7cd`.
