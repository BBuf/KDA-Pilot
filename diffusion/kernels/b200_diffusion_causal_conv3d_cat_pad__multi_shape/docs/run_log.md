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

## Notes
- Correctness was verified bitwise (`atol=0, rtol=0`) vs both the copied Triton baseline and the torch oracle, plus poison self-test and rejection tests.
- Initial candidate is slower than baseline (production geomean 0.63×); optimization is the next round. Raw `bench/results.jsonl` is kept on the remote workspace as evidence (excluded from the final PR per the diffusion PR-scope rule).
