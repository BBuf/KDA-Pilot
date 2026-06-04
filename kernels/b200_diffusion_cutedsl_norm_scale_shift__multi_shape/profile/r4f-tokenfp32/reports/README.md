# NCU report artifacts — r4f-tokenfp32

Raw `.ncu-rep` binaries are kept LOCALLY UNSTAGED (see profile/.gitignore)
and also live on the remote workspace at `/home/sglang-omni/bbuf/kda_runs/b200_diffusion_cutedsl_norm_scale_shift__multi_shape/2026-06-04_15-19-43/workspace/profile/r4f-tokenfp32/reports/`.
Build provenance: SHIPPED config (two-pass variance, per-combo vec width), joint src hash 842788d039bd at profiling time (comment-only .cuh delta vs current b91d6e1abc50). Harness: `harness/profile_case.py`
(run from the workspace root so bench/ + src/ resolve). Curated metric
extraction: `../analysis/*.csv` via `bench/ncu_extract.py`; session text
exports `*_session.txt` alongside the raw reports.

## Files

- `full.ncu-rep` — sha256 `60096d2337ca643c6933102a92d7c2807085bc72d88a461b5e48a267659bc6b1`
  command: `CUDA_VISIBLE_DEVICES=1 KDA_EXTRA_CUDA_CFLAGS=-lineinfo ncu --set full --target-processes all -k regex:norm_scale_shift_kernel --launch-skip 10 --launch-count 3 -f -o reports/full python bench/profile_case.py --case nss-b1-s11040-d5120-bf16-s1SD.fp32-s1SD.fp32-eps1e-06 --impl candidate --iters 25`

- `source.ncu-rep` — sha256 `4ce09efe172349ae4a2ed03fd445dacb7e225b9979f1fff1e631d3a651264bf5`
  command: `CUDA_VISIBLE_DEVICES=1 KDA_EXTRA_CUDA_CFLAGS=-lineinfo ncu --set source --section SourceCounters -k regex:norm_scale_shift_kernel --launch-skip 10 --launch-count 1 -f -o reports/source python bench/profile_case.py --case nss-b1-s11040-d5120-bf16-s1SD.fp32-s1SD.fp32-eps1e-06 --impl candidate --iters 15`
  Collected at the current shipped config (joint src hash b91d6e1abc50; full-set captured at 842788d039bd — comment-only delta).
  Session export: `source_session.txt`.
