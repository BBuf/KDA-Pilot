# Remote Run Log — ion8-h200

Host `ion-h200-8` (login `sglang-omni`), Docker container `sglang_bbuf`
(lmsysorg/sglang:dev; torch 2.11.0+cu130, CUDA 13.0, triton 3.6.0,
tvm-ffi 0.1.9, nvcc 13.0). Task workspace:
`/home/sglang-omni/bbuf/kda/k08_gns/task` (synced from this folder).
Measurement GPU: `REMOTE_GPU_ID=3` (NVIDIA H200, selected idle: 0% util /
0 MiB) — used consistently for every correctness/benchmark run below.
Capture GPUs: 0,1 (idle at selection) for the 2-GPU LTX preset runs.

GPU idle-state evidence: recorded before/after each benchmark inside
`bench/results.jsonl` provenance (`nvidia_smi_before` / `nvidia_smi_after`);
spot checks recorded inline below. GPUs 4-6 hold other users' memory
allocations throughout but show 0% utilization; all measurement ran on the
fully idle GPU 3.

## 2026-06-04 (UTC ~15:30–16:40) — bring-up, captures, baseline lock

1. **Toolchain probe** (versions above); `tvm_ffi.cpp.load` available.
2. **Candidate build + smoke** (GPU 3): `solution/binding.py` builds
   `solution/kernel.cu`; small path `(1,512,2,24,20)` and large path
   `(1,256,9,128,128)` vs eager oracle: max_abs = 1 fp16 ULP at |y|≈8. Two
   remote-discovered portability fixes landed: tvm-ffi 0.1.9 TensorView
   accessors (`size`/`stride`), and torch-2.11 profiler API in the
   authenticity check; plus the template-loader/dataclass Python 3.12 issue
   (adapter `Case` became a plain class).
3. **Correctness suite** (GPU 3): `python3 bench/correctness.py --device cuda:0`
   → **200 passed, 0 failed — CORRECTNESS_OK** (production 48-signature grid,
   contract regression grid fp16/bf16/fp32 at eps=1e-5, wrapper rows,
   misaligned/non-contiguous edges, poison + grad-gate checks, purity guard).
   Triton-path authenticity: profiler shows the copied baseline launching
   `_group_norm_silu_contiguous_kernel` (one-pass) and the chunked stats/apply
   Triton kernels for representative shapes; no `native_group_norm`/eager
   kernels on production rows.
4. **DEC-5 LTX captures** (GPUs 0,1; pinned sglang worktree at the resolved
   baseline commit `133254086b`; reduced `--num-inference-steps=4`, eager):
   - `ltx23-ti2v-two-stage`: completed; 36 rows; signatures
     `[1,1024,16,8,12]`, `[1,1024,16,16,24]` bf16, ng=32, eps=1e-5.
   - `ltx23-two-stage` (1536x1024): completed (peak 127 GB, no OOM); 36 rows;
     `[1,1024,16,16,24]`, `[1,1024,16,32,48]` bf16.
   - `ltx2` (LTX-2 base): completed; 36 rows; `[1,1024,16,8,12]`,
     `[1,1024,16,16,24]` **fp32**.
   Raw JSONL pulled to `docs/ltx_captures/`; folded into `bench/workloads.json`
   as 5 `production=false` wrapper diagnostics. Audit updated → all 20 presets
   resolved; workloads frozen afterwards.
5. **A/A harness validation** (GPU 3, `GNS_BENCH_CANDIDATE=baseline`, 8 spread
   workloads incl. two giants): all PASSED, **geomean 1.0037** (band
   0.98–1.02), per-row 0.9912–1.0376. Measurement symmetry certified after
   the pre-freeze review's per-call-allocation fix.
6. **Freeze run** (GPU 3): chained `bench/correctness.py` (green, now incl.
   LTX rows) → full `bench/benchmark.py` over **57 workloads** with the frozen
   `config.toml` settings (7 trials, warmup 10, inner 1..4096 → ~1000 us
   samples, isolated subprocesses).
   `python3 bench/benchmark.py --device cuda:0 --out bench/results.jsonl`
   → **57/57 PASSED**. Baseline medians from this run are the locked
   immutable baseline.
   - Headline (48 production rows): **geomean 1.2976**, arithmetic 1.4274,
     min 0.7047, max 4.0091.
   - Per-bucket (prior-round bucket labels): small 12 → 1.4370 (min 0.9120);
     large 24 → 1.6153 (min 0.8287); giant 12 → **0.7561** (0.7047–0.8292).
   - 18 rows below the 0.97 per-row floor: all 12 giants, 4 near-giant
     larges (gs ≥ 737,280), 2 smalls near the small/large crossover
     (gs 46,080 / 49,152).
   - Roofline (largest row, gs=8.9M): bytes = 2R+1W = 1.71 GB; baseline
     441.66 us ⇒ ~3.88 TB/s ≈ 81% of peak; candidate 626.70 us ⇒ ~2.73 TB/s
     ≈ 57%. The candidate's chunked path leaves ~24 pp of bandwidth on the
     table — the giant-kernel work target.
   - LTX diagnostics (non-headline): wrapper-path candidate 2.98x (bf16
     16x24), 4.60x (fp32 16x24), 0.87x (bf16 8x12, small path near
     crossover), 0.97x (bf16 32x48), 1.04x (fp32 8x12).

Evidence files: `bench/results.jsonl` (local copy pulled immediately after the
run; remote original retained), logs under the remote workspace
(`correctness_run2.log`, `correctness_prefreeze.log`, `aa_run2.log`,
`bench_v0.log`, `cap{1,2,3}.log`).

## 2026-06-04/05 (UTC ~16:40–18:30) — giant-bucket optimization + promotion runs

All on GPU 3 (idle checks per-run via results.jsonl provenance). NCU evidence
under the remote workspace `profile/ncu_giant_v0/` (gitignored; reports kept
remote + key metrics quoted in docs/dispatch.md and docs/results.md).

7. **NCU on the ported giant path** (`[1,256,17,256,256]`): stats 32 regs /
   84% occ / 68% DRAM; apply **52 regs / 44% occ / 41% DRAM** (the H200
   32-reg occupancy cliff) — the named bottleneck for the v0 giant losses.
8. **Bounded attempts v1–v7** (per-variant geomeans in docs/dispatch.md):
   targeted 16-row re-measurements with the frozen harness after each edit;
   correctness re-verified (incl. 3x repeated-call counter self-clean checks)
   before every measurement. Best = v3 (register-lean exact-grid 2-launch
   giant pipeline, fused last-block finalize, per-shape zero-straddle tiles):
   giant/near-giant 16-row geomean 0.756 -> 0.990.
9. **Full benchmark, all-CUDA (pre-escalation)**: 57/57 PASSED, headline
   1.3757, 11 rows in [0.896, 0.949) below the 0.97 per-row floor →
   surfaced the planned promotion decision; user chose the dispatch revisit
   (DEC-6).
10. **Dispatch implementation + promotion runs**: rule-based local-baseline
    fallback (docs/dispatch.md) + allocate-and-return candidate entry
    (wrapper hot path memoized after the first run showed ~1-2 us/call
    routing tax on host-bound rows). Three full runs recorded:
    A) 1.3874 / min 0.9477 (pre-tightening), B) 1.3972 / min 0.9252
    (one cuda-giant row at 0.925 vs 0.99-1.01 in four other runs —
    inter-process variance), C) **1.3961 / min 0.9662** (confirmation; the
    promotion record). Correctness 210/210 before every run (correctness_
    {final,dispatch,promo}.log).
