# Final Result — h200_diffusion_qknorm_rope__multi_shape (jit_kernel/tvm-ffi re-run)

This worktree re-did the task through SGLang's `jit_kernel` / tvm-ffi build path (the prior embedded
`Final Result` used a torch-extension/`EXPORTS` build and is a reference floor only, per AC-11).

## Candidate
- Native CUDA `fused_inplace_qknorm_rope` in `src/csrc/qknorm_rope_kernel.cuh`, built through SGLang
  `load_jit` + `make_cpp_args` + `cache_once` (task-owned `.cuh` via `../`-relpath + `extra_include_paths`;
  NO `torch.utils.cpp_extension`, NO `EXPORTS`, NO `--use_fast_math`; flags = SGLang diffusion default).
- Two paths in one `.cuh`, selected at compile time in `QKNormRopeKernel<...>::run`:
  - **head_dim=128 & rope_dim=128 & !is_neox → `fused_qknorm_rope_warp2`** (2 heads/warp, float4):
    16 lanes/head, 8 bf16/lane via one 128-bit load, 16-lane RMS reduction, GPT-J RoPE on all 128 dims;
    gated by `static_assert(kRopeDim == 128)`.
  - else — incl. **head_dim=128 rope_dim=64**, head_dim∈{64,256}, is_neox → baseline rope_dim-aware
    one-head-per-warp `fused_qknorm_rope_warp` (round-0 review fixed a bug where warp2 was wrongly used
    for rope_dim=64).
- `src/wrapper.py`: lean dispatcher (cached static gate, minimal per-call checks) + a device/dtype/
  layout-agnostic PyTorch FP32 semantic fallback that never raises (except a double-install guard).
- Final candidate **`src=4f70cda745940c96`** (d3-final; the round-0 d2 revision `87408a33029821ab` is
  superseded history — same warp2 machine code for rope_dim=128, but d2 gated warp2 too broadly and
  used an lru_cache wrapper).

## Correctness (ion8-h200 GPU7, sglang 0.5.12.dev472@c47f0e7cd, torch 2.9.1+cu129, nvcc 12.9)
- 73 captured-shape tests: 9 shapes × {arange,zero,repeat,shuffle} positions × {int32,int64} vs the
  split SGLang oracle (`fused_inplace_qknorm` + FlashInfer RoPE), ATOL=8e-2/RTOL=1e-2; per-shape eps
  (1e-6 qwen/qwen-edit, 1e-5 zimage); + FP32 reference cross-check (both neox). No NaN/Inf.
- 144 regression-grid tests (head_dim 64/128/256 × rope variants × is_neox both × int32/int64): pass.
- CPU/fp16/non-contiguous/misaligned/aliased/int16-positions → safe fallback; double-install → raises.

## Performance (d3-final; dual-level, CUDA-event timing, q/k reset outside timed region, JIT excluded, iters=300)
- **All-9 geomean: wrapper 1.0723× / module 1.0268×** (external idle verified: GPU7 util=0% mem=70MiB before AND after).
- Large shapes (T≥4096): **module 1.069–1.085×** (kernel win), wrapper 1.065–1.080×.
- Tiny shapes (T≤195): module 0.985–0.993× (launch-bound, flat), wrapper 1.051–1.090× (lean dispatch).
- Evidence: `benchmark.csv` (exact command + before/after idle per row), `docs/evidence/bench_summary_d3-final.json`, `docs/evidence/gpu_state_d3.md`. (Round-0 d2 measured 1.0992× with an lru_cache wrapper; d3 uses SGLang `cache_once` + the weight-shape gate, a touch more per-call overhead on tiny shapes.)

## Bound analysis (NCU, `profile/round_warp2/REPORT.md`, `docs/perf_analysis.md`)
- Large = **memory-latency-bound** (long-scoreboard 58%, DRAM 39.6% of peak, occ 72.7%, reg 38/thread)
  near the attainable bound; the 2-head win is wider per-warp memory work (MLP), not occupancy.
- Tiny = **launch/underfill-bound** (occ 12.4%, 0.07 waves/SM) → kernel no-go; carried by lean dispatch.
- Outcome metric (DEC-1): converged — no further kernel iteration warranted.

## In-SGLang drop-in replacement (AC-13) — PASS (real in-tree placement, round 1)
Isolated SGLang worktree (`git worktree` of `repos/sglang` @ c47f0e7cd); candidate `.cuh` placed as
`python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh`; SGLang's OWN public `fused_inplace_qknorm_rope`
builds it through normal `load_jit`/`make_cpp_args`/`cache_once` (NO monkeypatch; `repos/sglang`
untouched). All 9 captured shapes `oracle_ok=True`, no NaN; smoke benchmark candidate(worktree) vs
baseline(repos/sglang) **geomean 1.0452×** (large 1.075–1.084×); KDA wrapper CPU input → fallback, no
raise. `VERDICT PASS`. See `docs/sglang_jit_export.md`, `docs/evidence/export_cand.json`/`export_base.json`.

## Workspace
`solutions.jsonl` (d0 baseline clone → d1 lean dispatch → d2 warp2 [history/superseded] →
**d3-final-corrected** [src `4f70cda745940c96`, the FINAL candidate] → **export-real-in-sglang** [AC-13]),
`benchmark.csv`, `docs/dispatch.md`,
`docs/perf_analysis.md`, `profile/round_warp2/REPORT.md`, `interface.md`. Remote artifacts under
`REMOTE_KDA_DIR=/home/sglang-omni/bbuf/kda_runs/h200_diffusion_qknorm_rope__multi_shape/k04-20260601-225112`.

---

# Continuation round (2026-06-04) — new final candidate `cossin-vec`

The continuation round (fresh worktree, Humanize RLCR, plan `.humanize/kernel-agent/refined-plan.md`)
audited the incumbent and then improved it. **The final candidate is now `cossin-vec`
(src sha16 `6669bd218e336c9d`)**, superseding `d3-final-corrected` (`4f70cda745940c96`).

## Candidate delta (one edit, warp2 path only)
- Each lane's eight scalar `__ldg` cos/sin loads → two 128-bit `__ldg(float4)` quartet loads
  (a lane's four rotation pairs read four consecutive cos floats and four consecutive sin floats).
- Host launcher gains a base-alignment guard: a cos/sin cache base with `data_ptr() % 16 != 0`
  routes to the original scalar-load one-head path (rows stay aligned: 512 B row stride).
- All other paths (one-head baseline kernel, head_dim 64/256, rope_dim<128, neox) unchanged.

## Environment (audited; differs from the 2026-06-02 run)
ion8-h200 GPU 7, container `sglang_bbuf` (the prior `sglang_omni_bbuf_kda` no longer exists),
**torch 2.11.0+cu130, nvcc 13.0**, SGLang pinned `c47f0e7cd` via detached worktree (zero drift in the
qknorm_rope files verified in both ancestry directions). Audit reproduced the incumbent's committed
module-level evidence on this stack (module geomean 1.0366× vs committed 1.0268×, inside the ±3%
window; large 1.072–1.084×). Wrapper-level numbers are environment-labeled documentation only:
committed 1.0723× (torch 2.9.1/cu129, environment gone) vs 1.0236× on the current stack — the
tiny-shape python-dispatch advantage narrowed; the kernel signal (module level) reproduces.

## Correctness (continuation candidate)
- Captured-shape slice 72/72 BEFORE any benchmark claim; **full suite 226/226** on the final source
  (225 prior tests + the new forced-misaligned-cache negative
  `test_misaligned_cos_sin_cache_still_oracle_correct`); no NaN/Inf anywhere.
- In-tree misaligned-cache check through SGLang's own public op: PASS (guard exercised,
  `base_mod16=4`).

## Performance (same-process interleaved A/B/C, module level, externally idle before AND after)
- **vs incumbent d3-final: all-9 geomean 1.0622×, large (T≥4096) 1.1424× (1.134–1.148), tiny within
  noise (0.997–1.011)** — clears the decided re-promotion bar (≥3% in one clean run) at 6.2%.
- vs SGLang baseline: all-9 geomean 1.1009×, large 1.2373× (reproduced 1.2373/1.2356/1.2367 across
  three independent interleaved runs).
- Bounded exploration closed: iteration 2 (load hoist) REJECTED by the pre-declared rule (regs
  40>32, occupancy lost, gain unstable); smem cos/sin staging SKIPPED with stall-attribution
  evidence; register-pressure direction RESOLVED-BY-DIRECTION-1 (see below).

## Mechanism (NCU, `profile/round_cossin_vec/REPORT.md`)
Registers **38→32/thread** (the H200 100%-theoretical-occupancy boundary), theoretical occupancy
75→100%, achieved 72.5→90.4%, occupancy-capped grid 792→1056, memory throughput 2.005→2.245 TB/s,
duration 38.13→33.97 µs at qwen_t4096 — the float4 rewrite both shortened the cos/sin dependent-load
chain AND freed the registers that capped occupancy. Long-scoreboard attribution after the change:
45% q/k input unpack (irreducible), 34% norm chain, 14.5% positions→LEA, ~6% cos/sin consumers.

## In-SGLang drop-in arbiter (re-promotion gate) — PASS
Candidate `.cuh` (hash-verified in-tree) under SGLang's OWN unchanged public op at `c47f0e7cd`
vs the unmodified pin tree, separate processes: all 9 shapes `oracle_ok=True`, **geomean 1.0945×**
(prior promoted candidate: 1.0452×), per-shape 1.005–1.222× — parity-or-speedup everywhere; CPU
fallback preserved. See `docs/sglang_jit_export.md` (continuation section) and
`docs/evidence/export_cand_cossin-vec.json` / `export_base_cossin-vec.json`.

## kda_kernels promotion (round 1)
`kda_kernels/diffusion/qknorm_rope/_impls/h200/` refreshed to `6669bd218e336c9d` via
`scripts/export_kda_kernels/export.py`; `KDA_SPEEDUP` stamped **1.0677x** — the LITERAL
install()-path geomean through `kda_kernels.install()` (large 1.1536×; tiny 0.987–1.029
launch-bound parity + dispatcher overhead). Installed-path smoke on idle GPU 7: swap verified,
all 9 shapes route to the h200 impl, oracle-close, no NaN, fp16 dispatcher-fallback OK
(`docs/evidence/overlay_smoke_cossin-vec.log`). The in-tree arbiter number (1.0945×) and the
install() number are different integrations and are reported separately by design.

## Workspace
`solutions.jsonl` (… → d3-final-corrected → **cossin-vec** [FINAL, `6669bd218e336c9d`] →
cossin-vec2 [REJECTED, history] → **export-cossin-vec-in-sglang** [PASS] →
**export-cossin-vec-kda-kernels** [PASS]), `benchmark.csv`
(tags continuation-audit, cossin-vec, cossin-vec2, cossin-vec2-r2, export-cossin-vec,
export-cossin-vec-overlay), `docs/draft.md` (continuation
provenance + iteration log), `profile/round_cossin_vec/REPORT.md`. Remote artifacts under
`REMOTE_KDA_DIR=/home/sglang-omni/bbuf/kda_runs/h200_diffusion_qknorm_rope__multi_shape/k04-20260604-185804`.
