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
