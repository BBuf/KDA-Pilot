# NCU report artifacts — r0v1-nss-s176400-d5120-bf16row

Raw `.ncu-rep` binaries are kept LOCALLY UNSTAGED (see profile/.gitignore)
and also live on the remote workspace at `/home/sglang-omni/bbuf/kda_runs/b200_diffusion_cutedsl_norm_scale_shift__multi_shape/2026-06-04_15-19-43/workspace/profile/r0v1-nss-s176400-d5120-bf16row/reports/`.
Build provenance: candidate build at solutions cand-0001 (single-pass stats, pre-audit); baseline = pinned CuTe-DSL. Harness: `harness/profile_case.py`
(run from the workspace root so bench/ + src/ resolve). Curated metric
extraction: `../analysis/*.csv` via `bench/ncu_extract.py`; session text
exports `*_session.txt` alongside the raw reports.

## Files

- `full.ncu-rep` — sha256 `622e048849450a627bd105dadbb8b63f989ceec189d8abc70e3e24b5406e3137`
  command: `CUDA_VISIBLE_DEVICES=0 KDA_EXTRA_CUDA_CFLAGS=-lineinfo ncu --set full --target-processes all -k regex:norm_scale_shift_kernel --launch-skip 10 --launch-count 3 -f -o reports/full python bench/profile_case.py --case nss-b1-s176400-d5120-bf16-s11D.bf16-s11D.bf16-eps1e-06 --impl candidate --iters 25`
- `source.ncu-rep` — sha256 `f65b1bd65bc84e2ce187b81747291eb47dd6462ed43b657eb5a9047d7fbcf14e`
  command: `CUDA_VISIBLE_DEVICES=0 KDA_EXTRA_CUDA_CFLAGS=-lineinfo ncu --set source --section SourceCounters -k regex:norm_scale_shift_kernel --launch-skip 10 --launch-count 1 -f -o reports/source python bench/profile_case.py --case nss-b1-s176400-d5120-bf16-s11D.bf16-s11D.bf16-eps1e-06 --impl candidate --iters 15`
