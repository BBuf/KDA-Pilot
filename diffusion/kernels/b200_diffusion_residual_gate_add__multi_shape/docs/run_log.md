# Remote B200 Run Log

## Environment (AC-6)
- Host: `ion-b200`, user `sglang-omni`.
- Container: `sglang_bbuf` (`lmsysorg/sglang:dev`).
- Toolchain: torch `2.11.0+cu130`, torch.version.cuda `13.0`, tvm-ffi `0.1.9`,
  nvcc `cuda_13.0.r13.0` (V13.0.88).
- GPU model: NVIDIA B200 (192 GB HBM3e, 148 SMs).
- Pinned GPU: `REMOTE_GPU_ID=2`, `CUDA_VISIBLE_DEVICES=2` (sole visible device ->
  `cuda:0`). The fail-closed pin guard (`bench/adapter.assert_pinned_gpu`,
  enabled via `KDA_REQUIRE_PINNED_GPU=1`) was active for the benchmark run.
- Idle evidence for GPU 2 (`index, util%, mem_used MiB`):
  - Before: `2, 0, 0`
  - After:  `2, 0, 0`  (post-run summary snapshot: `2, 0%, 4 MiB`)
  - GPUs 3-6 were busy (~95%) on unrelated jobs throughout; GPU 1 had standing
    memory occupancy. GPU 2 remained uncontended.

## Workspace
- Task folder streamed (tar over ssh, excluding `.humanize`/`.build`/`.git`) into
  `/home/sglang-omni/bbuf/kda_tasks/residual_gate_add` inside the container.
- Local source commit: `70ceefac4` (working branch
  `kda/k19_b200_diffusion_residual_gate_add__multi_shape-20260625-083922-58057`).

## Commands
```bash
# build (tvm-ffi)
docker exec -e CUDA_VISIBLE_DEVICES=2 sglang_bbuf bash -lc \
  'cd <task> && python -c "from solution.build import load_candidate_module; load_candidate_module()"'
# correctness gate
docker exec -e CUDA_VISIBLE_DEVICES=2 sglang_bbuf bash -lc \
  'cd <task> && python bench/correctness.py --impl both --rows all'
# frozen benchmark (pin guard active)
docker exec -e KDA_REQUIRE_PINNED_GPU=1 -e REMOTE_GPU_ID=2 -e CUDA_VISIBLE_DEVICES=2 sglang_bbuf bash -lc \
  'cd <task> && python bench/benchmark.py --out bench/results.jsonl'
```

## Build (AC-2/AC-3)
- `solution/kernel.cu` compiled cleanly via `tvm_ffi.cpp.load`; both exports
  (`residual_gate_add`, `broadcast_add_4d`) present. No `--use_fast_math`.

## Correctness (AC-3 / AC-4) — PASS
- `bench/correctness.py --impl both --rows all`: **56/56 rows, 0 failures**, on
  NVIDIA B200. Covers the 8 production rows (candidate vs fp32 one-round oracle
  AND candidate vs faithful eager baseline, bf16 atol=rtol=5e-2), the regression
  grid (full/broadcast gate; bf16/fp16/fp32; odd-D / non-vec-aligned-D / small-L
  tails; 4D over multiple frame counts; sign/zero), the poison self-test, and
  both-side rejection tests (incl. `rga-full-gate-noncontig`, `rga-bad-gate-2d`,
  `rga-gate-leaddim-not1`, dtype mismatch, aliasing, non-contiguous, 4D batch>1).

## Benchmark (AC-5) — candidate vs faithful eager baseline, geomean 2.199x
All 8 production rows PASSED (matched ratio 1.0). Baseline = profiled two-launch
eager `mul`+`add`; candidate = single fused CUDA pass.

| Workload | gate | speedup | baseline (us) | candidate (us) |
|---|---|---:|---:|---:|
| ltx2_full_s8160_c4096 | full | 1.6016 | 66.328 | 41.413 |
| ltx2_bcast_s32640_c4096 | bcast | 2.9638 | 419.032 | 141.384 |
| ltx2_full_s126_c2048 | full | 1.7970 | 17.661 | 9.828 |
| ideogram4_bcast_s4096_c4608 | bcast | 2.8252 | 64.350 | 22.777 |
| flux2_bcast_s4608_c3072 | bcast | 3.2763 | 47.488 | 14.495 |
| flux2_bcast_s4096_c3072 | bcast | 3.3356 | 41.568 | 12.462 |
| flux2_bcast_s512_c3072 | bcast | 1.7261 | 19.546 | 11.324 |
| ltx2_broadcast_add_4d_s126_p3_c2048 | - | 1.2028 | 11.510 | 9.569 |

Headline: **geomean 2.1990x**, arithmetic mean 2.3411x, min 1.2028x, max 3.3356x.

## Provenance (in `bench/results.jsonl`, AC-5)
- baseline_commit `8314247d9de0fa2c58e34756b3e1dbc6cf815dfd`
- candidate_kernel_sha256 `a450f8635e11791f…`
- remote_gpu_id `2`; tvm_ffi `0.1.9`; nvcc `cuda_13.0`
- gpu `NVIDIA B200`; torch `2.11.0+cu130`; torch_cuda `13.0`

## Preliminary roofline sanity (AC-7 — full per-row table + NCU is the next round)
- `ltx2_bcast_s32640_c4096` (133.69M bf16 elems): candidate streams residual+update
  (read) + out (write) ~ 3 x 133.69M x 2B = ~802 MB in 141.384 us ->
  ~5.67 TB/s achieved (~71% of ~8 TB/s HBM3e). Bandwidth-bound, near roofline.
  Eager baseline (~5 full passes incl. temp write/read + 2 launches + 2 dispatches)
  ~ 1337 MB in 419.032 us -> ~3.19 TB/s; the candidate's win is the eliminated
  temp traffic + one launch + one dispatch.
- Full per-row speed-of-light/bytes/%peak table and the NCU bound interpretation
  are in `docs/results.md` (collected in the round below).

## Round 3 — strict-pinned reruns + NCU (GPU 0, idle)
- GPU 0 idle before: `0, NVIDIA B200, 0%, 0 MiB`; after: idle.
- Correctness rerun (strict pin: `KDA_REQUIRE_PINNED_GPU=1 REMOTE_GPU_ID=0
  CUDA_VISIBLE_DEVICES=0 python bench/correctness.py --impl both --rows all
  --report /tmp/rga_correctness_final.json`): **67/67 PASS** (adds AC-4 zero/sign
  rows + repeated-seed rows over the R2 56/56). The pin guard was active.
- NCU (`ncu --set basic --launch-skip 6 --launch-count 1`, GPU 0) on the three
  representative rows:
  | row | DRAM % | Compute(SM) % | NCU duration | occupancy | grid | NCU bound |
  |---|---:|---:|---:|---:|---|---|
  | ltx2_full_s8160_c4096 (full) | 72.09 | 55.80 | 51.3us | 60.5% | 16320x256 | DRAM bottleneck |
  | ltx2_bcast_s32640_c4096 (bcast) | 59.53 | 69.77 | 195.7us | 50.6% | 65280x256 | SM/instruction-leaning |
  | ltx2_full_s126_c2048 (full) | 3.72 | 3.14 | 6.4us | 12.8% | 126x256 | grid < 148 SMs (launch-bound) |
- (R3 NCU was captured to stdout via `--set basic`, not saved as `.ncu-rep`; the
  scratch harness is `/tmp/rga_profile.py`. The Round-4 reruns below save the raw
  `.ncu-rep` files.)

## Round 4 — UNIFIED final evidence on one pinned GPU (GPU 7, idle)
Per the plan's AC-6 (one `REMOTE_GPU_ID` reused across correctness/benchmark/
profile), all final evidence is collected on a single physical GPU (7), idle
before and after (`7, NVIDIA B200, 0%, 0 MiB` both), with the fail-closed pin env
`KDA_REQUIRE_PINNED_GPU=1 REMOTE_GPU_ID=7 CUDA_VISIBLE_DEVICES=7` on every command.
- Correctness: `bench/correctness.py --impl both --rows all` -> **67/67 PASS**
  (report `/tmp/rga_correctness_final.json`).
- Benchmark: `bench/benchmark.py --out bench/results.jsonl` -> 8/8 rows PASS,
  geomean **2.193x**; `results.jsonl` provenance `remote_gpu_id=7`,
  baseline_commit 8314247d, candidate sha256 a450f863.
- NCU (`-o /tmp/ncu_<row>`, GPU 7): full_big DRAM 72.49% / SM 55.73%; bcast_big
  DRAM 59.45% / SM 69.68% (occ 50.5%); full_small DRAM 3.77% / SM 3.06%
  (grid 126 < 148 SMs). Raw `.ncu-rep` saved under the ignored remote `/tmp`
  (`/tmp/ncu_full_big.ncu-rep`, `/tmp/ncu_bcast_big.ncu-rep`,
  `/tmp/ncu_full_small.ncu-rep`); not staged for the PR.
- Per-row roofline table and bound interpretation: `docs/results.md`.

## Round 5 — review-fix re-validation (compute-neutral)
Two Codex code-review findings fixed: P2 (`bench/benchmark.py` now calls
`torch.cuda.set_device` before importing/building the adapter) and P3
(`solution/kernel.cu` `broadcast_add_4d` now requires `out.ndim()==4`). Both are
host-side only — the device kernels and the timed path for valid inputs are
byte-identical — so the geomean 2.193x measured in Round 4 stands.
- New candidate `solution/kernel.cu` sha256: `27f67c5ff283d87b8d56b3c55f8caef749e73c845a8667e063f0b8d479a6c749`
  (Round-4 benchmark provenance recorded the pre-fix `a450f863…`; the only kernel
  delta is the added host-side rank reject, which no valid/production row triggers).
- Correctness re-confirmed on the clean rebuild: `bench/correctness.py --impl both
  --rows all` = **67/67 PASS** on B200 (GPU 1; report `/tmp/rga_correctness_r5.json`).
- Benchmark re-run deferred: at fix time all 8 B200 GPUs were busy (util 49-96%) or
  had standing memory occupancy, so per the idle-GPU rule no timed numbers were
  collected on a non-idle card. The Round-4 geomean stands (compute-neutral edits);
  a refresh on an idle GPU is optional and would reproduce the same numbers.

## Round 7 — review fix: multi-GPU device guard (compute-neutral)
Codex review P2: the exported kernels launched on the process-current device's
stream rather than the input tensors' device. Fixed in `solution/kernel.cu`: both
`residual_gate_add` and `broadcast_add_4d` now validate all operands share one CUDA
device id and install a `c10::cuda::CUDAGuard(dev)` + take that device's stream
before launching. On a single visible GPU (the pinned runs) the guard is a no-op
(the tensor device is already current), so the timed path and the Round-4 geomean
2.193x are unchanged.
- New candidate `solution/kernel.cu` sha256: `a6ab9c86e7ecf2c056d00c568e8895d0fbbf9dcac1494c78a71d569500725fc8`.
- Rebuilt on B200 (GPU 1); `bench/correctness.py --impl both --rows all` = **67/67
  PASS** (report `/tmp/rga_correctness_r7.json`). Benchmark re-run deferred (no
  fully-idle GPU; compute-neutral on single-GPU).

## Round 8 — review fix: benchmark provenance device-order (re-validated on GPU 7)
Codex review P2: `bench/benchmark.py::main()` collected provenance
(`_provenance` -> `_gpu_name()` + adapter `extra_provenance()`/candidate build)
BEFORE setting the CUDA device, so a non-default `--device` would record cuda:0's
name/SM/compile-flags while workloads ran on `args.device`. Fixed: `main()` now
calls `torch.cuda.set_device(torch.device(args.device))` before `_provenance()`,
mirroring the R5 `_run_one_workload` device-first pattern. Harness-only — the
candidate `solution/kernel.cu` is unchanged (hash still
`a6ab9c86…`), and on a pinned single-visible-GPU run the current device already
equals `args.device`, so the fix is compute-neutral.
- An idle GPU was available this round, so both gates were re-run fresh on the
  unified-evidence card (physical **GPU 7**, strict pin
  `KDA_REQUIRE_PINNED_GPU=1 REMOTE_GPU_ID=7 CUDA_VISIBLE_DEVICES=7`):
  - `bench/correctness.py --impl both --rows all` -> **67/67 PASS**
    (report `/tmp/rga_correctness_r8.json`).
  - `bench/benchmark.py --out bench/results.jsonl` -> **8/8 PASS**, geomean
    **2.186x** (min 1.186x, max 3.277x) — reproduces the Round-4 2.193x within
    run-to-run noise (per-row deltas < 1%). `results.jsonl` provenance now records
    `gpu=NVIDIA B200`, `remote_gpu_id=7`, `candidate_kernel_sha256=a6ab9c86…`,
    `baseline_commit=8314247d…` (1 provenance + 8 result + 1 summary events).
  - Idle evidence GPU 7: before `7, NVIDIA B200, 0%, 0 MiB`. After my run returned,
    an unrelated job landed on GPU 7 (post-run snapshot `7, …, 96%, ~42 GB`); the
    measured times matching Round-4's idle-GPU numbers within noise confirm the
    measurement window itself was uncontended (heavy contention would have inflated
    and de-stabilized the per-row times, which it did not).
