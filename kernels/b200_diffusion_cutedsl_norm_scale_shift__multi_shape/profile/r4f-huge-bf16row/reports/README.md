# NCU report artifacts — r4f-huge-bf16row

Raw `.ncu-rep` binaries are kept LOCALLY UNSTAGED (see profile/.gitignore)
and also live on the remote workspace at `/home/sglang-omni/bbuf/kda_runs/b200_diffusion_cutedsl_norm_scale_shift__multi_shape/2026-06-04_15-19-43/workspace/profile/r4f-huge-bf16row/reports/`.
Build provenance: SHIPPED config (two-pass variance, per-combo vec width), joint src hash 842788d039bd at profiling time (comment-only .cuh delta vs current b91d6e1abc50). Harness: `harness/profile_case.py`
(run from the workspace root so bench/ + src/ resolve). Curated metric
extraction: `../analysis/*.csv` via `bench/ncu_extract.py`; session text
exports `*_session.txt` alongside the raw reports.

## Files

- `full.ncu-rep` — sha256 `ad0780fdf2fe9e9f519614209cc5f2e4cbdfa2215ef21839ce7dbdb65107bc7b`
  command: `CUDA_VISIBLE_DEVICES=1 KDA_EXTRA_CUDA_CFLAGS=-lineinfo ncu --set full --target-processes all -k regex:norm_scale_shift_kernel --launch-skip 10 --launch-count 3 -f -o reports/full python bench/profile_case.py --case nss-b1-s176400-d5120-bf16-s11D.bf16-s11D.bf16-eps1e-06 --impl candidate --iters 25`

- `source.ncu-rep` — sha256 `dbdfc6413bf79a72211a19381cb3e9c4b76ffa67f303fd13f4e78513c424e783`
  command: `CUDA_VISIBLE_DEVICES=1 KDA_EXTRA_CUDA_CFLAGS=-lineinfo ncu --set source --section SourceCounters -k regex:norm_scale_shift_kernel --launch-skip 10 --launch-count 1 -f -o reports/source python bench/profile_case.py --case nss-b1-s176400-d5120-bf16-s11D.bf16-s11D.bf16-eps1e-06 --impl candidate --iters 15`
  Collected at the current shipped config (joint src hash b91d6e1abc50; the full-set report in this dir was captured pre-comment-only-edit at 842788d039bd — no code delta).
  Session export: `source_session.txt`.
