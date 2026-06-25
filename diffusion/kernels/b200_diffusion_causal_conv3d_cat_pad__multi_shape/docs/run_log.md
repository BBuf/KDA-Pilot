# Remote Run Log

## Environment (2026-06-25)
- Host: `ion-b200` → `innomatrix-us-adc-smb200-0003`; user `sglang-omni`; container `sglang_bbuf` (Up 10 days, image `lmsysorg/sglang:dev`).
- Remote task workspace: `/home/sglang-omni/bbuf/kda/k17_ccc` (synced from the local task folder via `tar | docker exec -i`, excluding `.humanize`/`.git`/pycache).
- GPU selection: physical **GPU 0** (`REMOTE_GPU_ID=0`), NVIDIA B200, 183359 MiB. Pinned with `CUDA_VISIBLE_DEVICES=0` for build, correctness, and benchmark.
  - Idle proof: GPU 0 before = `0 %, 4 MiB`, no compute processes; after = `0 %, 4 MiB`. (GPUs 3–6 were running unrelated jobs; GPUs 0/2/7 idle — GPU 0 used throughout.)

## Commands (Round 1)
- Sync: `tar --exclude='*__pycache__*' --exclude='*.pyc' -cf - baseline bench solution docs config.toml prompt.md | ssh ion-b200 'docker exec -i sglang_bbuf sh -lc "... tar -xf - -C /home/sglang-omni/bbuf/kda/k17_ccc"'`
- Build + correctness: `CUDA_VISIBLE_DEVICES=0 python bench/correctness.py` → `CORRECTNESS PASS: 13 value cases + poison self-test + rejection tests`
- Benchmark: `CUDA_VISIBLE_DEVICES=0 python bench/benchmark.py --workloads bench/workloads.json --out bench/results.jsonl`

## Provenance
- Baseline upstream commit: `67b2a9ed0cfba8ec625d3f26548e502646fd914d` (frozen at recovery; see `docs/baseline_source.md`).
- Candidate (Round 1): initial correct-by-construction scalar transliteration in `solution/kernel.cu` (one thread per output element).
- Compile flags: `-std=c++17 -O3` + native gencode (sm_100), no `--use_fast_math` (see `docs/benchmark_method.md`).

## Notes (Round 1)
- Correctness was verified bitwise (`atol=0, rtol=0`) vs both the copied Triton baseline and the torch oracle, plus poison self-test and rejection tests.
- Initial candidate (scalar transliteration) was slower than baseline (production geomean 0.63×); optimization is Round 2. Raw `bench/results.jsonl` is kept on the remote workspace as evidence (excluded from the final PR per the diffusion PR-scope rule).

## Round 2 (2026-06-25) — optimized candidate

Same host/container; GPU 0 selected; idle proof captured per run.
- GPU 0 compute processes before AND after the canonical benchmark run: **none** (verified via `nvidia-smi -i 0 --query-compute-apps`); 0% utilization throughout. (Cluster GPUs 3–7 ran unrelated jobs; GPU 0 used exclusively.)

Commands:
- Build + correctness: `CUDA_VISIBLE_DEVICES=0 python bench/correctness.py` → `CORRECTNESS PASS: 13 value cases + non-contiguous positive + poison self-test + rejection tests`.
- Benchmark (two clean runs): `CUDA_VISIBLE_DEVICES=0 python bench/benchmark.py --workloads bench/workloads.json --out bench/results.jsonl` → production geomean 2.057× and 2.090× (per-row 1.55×–2.44×).
- NCU (task11): `CUDA_VISIBLE_DEVICES=0 ncu -k regex:cat_pad_flat -c 1 -s 5 --set basic python bench/profile_one.py` → `cat_pad_flat_kernel<uint16,8>`: Compute(SM) 81.2%, DRAM 17.9%, Memory 27.7%, occupancy 54.2% (compute/instruction-bound; memory headroom remains).

Candidate source: `solution/kernel.cu` `cat_pad_flat_kernel` (flat-chunk 16-byte vectorized stores + stride-aware fallback). Result detail in `docs/results.md`.
- Remote-only artifacts (excluded from the PR): `bench/results.jsonl`, `solution/.build/`, `bench/profile_one.py` (profiling harness), and the NCU run output.

## Round 3 (2026-06-25) — AC-3 storage-offset coverage + cleanup

- Added a nonzero-storage-offset positive case: `workloads.json` row `reg_noncontig_offset` (x and cache non-contiguous with `storage_offset_elems` 7 and 5) + `bench/correctness.py::run_offset_test` (candidate vs torch oracle vs normalized baseline, bitwise).
- Removed the forbidden plan-marker comment from `solution/kernel.cu` (`rg "AC-|Milestone|Phase|task[0-9]" solution baseline bench` is clean).
- Correctness: `CUDA_VISIBLE_DEVICES=7 python bench/correctness.py` → PASS (13 value + non-contiguous positive + **nonzero-storage-offset positive** + poison + rejection).
- Re-benchmark (frozen workload file changed) on **GPU 7** (`REMOTE_GPU_ID=7`): no compute processes before or after, 0% util / 0 MiB before. `CUDA_VISIBLE_DEVICES=7 python bench/benchmark.py --workloads bench/workloads.json --out bench/results.jsonl` → production geomean **2.060×** (per-row 1.60×–2.45×); all 12 workloads pass the bitwise A/B gate.
- Note: GPU 0 showed a transient foreign compute process during an earlier Round-3 benchmark attempt; the canonical numbers above are from the clean GPU 7 run. Candidate medians were identical across GPU 0 and GPU 7 (CUDA-event timing isolates the kernel).
