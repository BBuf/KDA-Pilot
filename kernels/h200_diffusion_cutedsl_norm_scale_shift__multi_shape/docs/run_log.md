# Run Log — h200_diffusion_cutedsl_norm_scale_shift__multi_shape

All GPU work: host `ion8-h200` (hostname `ion-h200-8`), Docker container `sglang_bbuf`
(lmsysorg/sglang:dev; torch 2.11.0+cu130, CUDA 13.0, nvcc 13.0.r13.0, cutlass-dsl 4.5.0,
tvm-ffi, Nsight Compute 2025.3.1.0), task workspace
`/home/sglang-omni/bbuf/kda/k16_h200_nss/{task,logs,sglang_pin}`.

Selected GPUs: `REMOTE_GPU_ID=0` for the scaffold validation, v1 anchor, NCU rounds, sweep, and
correctness runs (selection evidence at first use: GPUs 0-3 at 0% util / 0 MiB with no compute
apps; GPUs 4-6 occupied by other users' jobs at 123-143 GiB; GPU 7 had 42 MiB residual), then
`REMOTE_GPU_ID=2` for the FINAL promotion benchmark sessions after a foreign job landed on GPU 0
mid-chain (items 13-15 below). Each measurement was pinned with `CUDA_VISIBLE_DEVICES=<id>` and
used one consistent GPU per run; idle state (0% util / 0-4 MiB, no compute apps) was checked
before launches and after completions; the benchmark harness additionally records full
`nvidia-smi` before/after snapshots inside each results JSONL.

## 2026-06-04 (UTC+8 evening) — scaffold validation and v1 anchor

1. Candidate JIT smoke build (sm_90): `python3 /tmp/k16_smoke.py` — build 19.9s after
   vendoring the missing `source_location.h`; nss/srnss outputs bitwise-identical to the
   vendored CuTeDSL baseline; native dispatch counted; snapshot-alias guard ok.
2. Production correctness: `python3 bench/correctness.py --mode production --device cuda:0`
   -> 40/40 (39 rows + zero-fallback routing check), report `logs/correctness_production.json`.
3. Canonical grid: `--mode grid` -> 110/110, report `logs/correctness_grid.json`.
4. Negative probes: `--mode probes` -> 11/11, report `logs/correctness_probes.json`.
5. Benchmark session 1 (v1 config): `python3 bench/benchmark.py --device cuda:0 --out
   logs/results_s1.jsonl` -> 49/49 passed; production geomean 1.2887x (min 0.9483 on
   nss-s37800-fp32-row, max 1.9685).
6. Two-process parity vs real SGLang at pinned commit 1332540 (task-owned worktree
   `sglang_pin`): `bench/parity_check.py --side real` (PYTHONPATH=sglang_pin/python) then
   `--side snapshot` -> PARITY OK, 10/10 bitwise.

## 2026-06-04/05 — NCU round + bounded levers

7. NCU r1 (worst bucket nss s37800 d5120 fp32-row): `ncu --set full --launch-skip 10
   --launch-count 3` on both sides via `profile/r1-nss-fp32row-s37800/harness/profile_case.py`;
   reports `candidate.ncu-rep` / `baseline.ncu-rep` (workspace-local), analysis in
   `profile/r1-nss-fp32row-s37800/{REPORT.md,analysis/metrics.csv}`. Verdict: identical
   geometry/regs/bytes; candidate loses on exposed operand-load latency.
8. Lever: prefetch.global.L1 (`candidate_r2pf.ncu-rep`): REJECTED — 620us vs 381us
   (LSU flood from per-thread prefetches of shared row operands; barrier stalls 3x).
9. Lever: early raw scale/shift loads (`candidate_r3eo.ncu-rep`): REJECTED — 40 regs ->
   2 CTAs/SM (theory occupancy 62.5%), 489us despite short_scoreboard recovering to 4.3.
10. Lever: KDA_VEC_BYTES_BF16=32 full sweep (`logs/results_sweep_v32.jsonl`): REJECTED —
    mean -4.8% on bf16 combos, srnss bf16 rows -28%, sweep geomean 1.2475.
11. DEC-2 routing applied in `solution/binding.py`: nss row-class fp32 scale/shift bucket
    -> vendored baseline (separate `routed` dispatch counter).

## 2026-06-05 — final shipped-config validation

12. Chain on GPU 0 (`logs/final_chain.log`): idle snapshot (0% / 0 MiB) -> production
    correctness re-run with routing bookkeeping -> 40/40 (CORRECTNESS_EXIT=0) -> probes
    re-run -> 11/11 (PROBES_EXIT=0). Both correctness runs completed while GPU 0 was
    still idle; functional results stand.
13. **DISCARDED**: benchmark sessions A/B from the same chain
    (`logs/results_final_a.jsonl`, `logs/results_final_b.jsonl`). A foreign job landed
    on GPU 0 during session A (`nvidia_smi_after` shows 112293 MiB and 5% util; session
    B's `nvidia_smi_before` shows the same occupant; two non-task compute apps remained
    on GPU 0/1 afterwards). Per the idle-GPU rule these sessions are NOT valid promotion
    evidence and are excluded from all reported numbers (their geomeans, 1.2772/1.2669,
    are mentioned here only to document the discard).
14. GPU re-selection: GPUs 2 and 3 verified idle (0% util, 0 MiB, no compute apps);
    re-run pinned to `REMOTE_GPU_ID=2` (`CUDA_VISIBLE_DEVICES=2`, harness device cuda:0
    inside the visible set).
15. Chain on GPU 2 (`logs/final_chain_gpu2.log`): idle + compute-apps snapshot ->
    benchmark session A2 (`--seed 1234`, `logs/results_final_a2.jsonl`) -> idle snapshot
    -> benchmark session B2 (`--seed 5678`, `logs/results_final_b2.jsonl`) -> idle +
    compute-apps snapshot. A2 1.2708 / B2 1.2747 (window 0.31%); superseded as the primary
    evidence by the GPU-3 sessions below (provenance-extended format) and retained as
    consistency history.

## 2026-06-05 — round-1 evidence hardening (review-driven), GPU 3

16. Code changes (no timing-policy change): checker-based NaN + Inf injection probes in
    `bench/correctness.py`; machine-auditable provenance extensions and a
    `--candidate-impl baseline` symmetry mode in `bench/benchmark.py`
    (`docs/benchmark_method.md` documents both).
17. GPU re-selection for this chain: GPU 3 (physical index 3, UUID
    `GPU-6b4aba65-49ad-a9b2-0fa8-d2dbcb96a34b`), verified 0% util / 4 MiB / no compute apps
    at chain start (`logs/r1_chain.log`); GPU 2 had a 1 MiB residual at selection time.
18. Probes re-run (`CUDA_VISIBLE_DEVICES=3 python3 bench/correctness.py --mode probes
    --device cuda:0`): **12/12** (`logs/correctness_probes_r1.json`) — suite now includes
    checker-based NaN AND Inf injection.
19. Baseline-vs-baseline symmetry sanity (`--seed 4242 --candidate-impl baseline`,
    `logs/results_bvb.jsonl`): 49/49 passed, production geomean **0.9992**
    (min 0.9655 / max 1.0267) — harness symmetry validated.
20. Final sessions with machine-complete provenance: A3 (`--seed 1234`,
    `logs/results_final_a3.jsonl`) geomean **1.2795**; B3 (`--seed 5678`,
    `logs/results_final_b3.jsonl`) geomean **1.2763**; window 0.25%. Every results JSONL now
    embeds hostname, device mapping (visible+physical index, GPU UUID/model), per-UUID GPU
    inventory and compute-app snapshots before/after, baseline commit, candidate source hash,
    run seed, and per-row trial seeds / A-B orders / selected-GPU identity.
21. Idle-evidence reading for the chain: the A3 pre-run compute-app snapshot is clean; the only
    GPU-3 entries in any snapshot are the chain's own just-exited sequential workers (monotonic
    PIDs 2759809 -> 2788491 -> 2804420, each <= ~730 MiB at 0% utilization, gone by the next
    step; post-chain check shows no compute apps). No foreign workload touched GPU 3.
