# NCU report artifacts — r0v1-nss-s11040-d5120-tokenfp32

Raw `.ncu-rep` binaries are kept LOCALLY UNSTAGED (see profile/.gitignore)
and also live on the remote workspace at `/home/sglang-omni/bbuf/kda_runs/b200_diffusion_cutedsl_norm_scale_shift__multi_shape/2026-06-04_15-19-43/workspace/profile/r0v1-nss-s11040-d5120-tokenfp32/reports/`.
Build provenance: candidate build at solutions cand-0001 (single-pass stats, pre-audit); baseline = pinned CuTe-DSL. Harness: `harness/profile_case.py`
(run from the workspace root so bench/ + src/ resolve). Curated metric
extraction: `../analysis/*.csv` via `bench/ncu_extract.py`; session text
exports `*_session.txt` alongside the raw reports.

## Files

- `full_candidate.ncu-rep` — sha256 `584733351f43a9373d5257f98eeca05fbd04c5c45a6dad6a5f4b29fcabc37739`
  command: `CUDA_VISIBLE_DEVICES=0 KDA_EXTRA_CUDA_CFLAGS=-lineinfo ncu --set full --target-processes all -k regex:norm_scale_shift_kernel --launch-skip 10 --launch-count 3 -f -o reports/full_candidate python bench/profile_case.py --case nss-b1-s11040-d5120-bf16-s1SD.fp32-s1SD.fp32-eps1e-06 --impl candidate --iters 25`
- `full_baseline.ncu-rep` — sha256 `3609c335e1a2db8a85237d5b7bd5156913b1aec8f3f5760232fefc3b704c9cf9`
  command: `CUDA_VISIBLE_DEVICES=0 ncu --set full --target-processes all --launch-skip 28 --launch-count 2 -f -o reports/full_baseline python bench/profile_case.py --case nss-b1-s11040-d5120-bf16-s1SD.fp32-s1SD.fp32-eps1e-06 --impl baseline --iters 30`

- `source.ncu-rep` — sha256 `5a4cbbd67f0e0ee3661de307f3e23372bcfadd2d305f99e0af0416db6397579f`
  command: `CUDA_VISIBLE_DEVICES=1 KDA_EXTRA_CUDA_CFLAGS=-lineinfo ncu --set source --section SourceCounters -k regex:norm_scale_shift_kernel --launch-skip 10 --launch-count 1 -f -o reports/source python bench/profile_case.py --case nss-b1-s11040-d5120-bf16-s1SD.fp32-s1SD.fp32-eps1e-06 --impl candidate --iters 15`
  POST-HOC NOTE: this source-set was collected at the CURRENT shipped config (joint src hash b91d6e1abc50, vec16 fp32-operand build) because the round-0 v1 build it originally diagnosed is superseded; the full-set reports above remain the v1-era diagnosis artifacts, and the final bound claims rest on the r4f directories.
  Session export: `source_session.txt`.
