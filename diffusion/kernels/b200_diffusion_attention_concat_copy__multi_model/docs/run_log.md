# Remote Run Log — b200_diffusion_attention_concat_copy__multi_model

## Environment
- Host: `ion-b200`, user `sglang-omni`.
- Container: `sglang_bbuf` (image `lmsysorg/sglang:dev`, profiler-capable flags).
- Workspace: `/home/sglang-omni/bbuf/kda/attn_concat_copy` (task files streamed from the local worktree; `.humanize`/`.build`/scratch excluded).
- Toolchain: torch 2.11.0+cu130, CUDA 13.0, nvcc 13.0, ncu present, tvm_ffi present, Python 3.12.3.
- GPU selection: `nvidia-smi` showed GPUs 0/2/7 fully idle (0% util, 0 MiB), GPUs 3–6 busy (~95%), GPU 1 holding memory. Selected **GPU 0**; pinned `CUDA_VISIBLE_DEVICES=0` for every correctness/A-A/benchmark command. Re-verified idle (0%, ≤4 MiB) immediately before each benchmark and after the headline run.

## Run 1 — candidate build + correctness (v1)
- `CUDA_VISIBLE_DEVICES=0 python bench/correctness.py --impl both --device cuda`
- Result: `tvm_ffi.cpp.load` built `solution/kernel.cu` cleanly (sm_100); PASS=40/40 bit-exact (baseline + candidate × 20), negative control OK.

## Run 2 — frozen baseline + A/B benchmark (v1) + A/A validity
- A/B: production geomean **0.961** (copy wins 1.04–2.01; concat 0.58–0.61 slow; slice ~0.86–0.96 parity).
- A/A (`KDA_AA=1`): geomean **1.0002** (min 0.998, max 1.002) — harness has no slot bias.
- Diagnosis (roofline): ATen `CatArrayBatchedCopy` is near peak; v1's per-output-vector `div`/`mod` index math is overhead on contiguous segments. GPU 0 idle before/after.

## Run 3 — region-based candidate (v2)
- Rebuilt after rewriting the kernel to per-region copies (flat for contiguous segments, pitched gather for head-sliced prefix). PASS=40/40 bit-exact.
- A/B: production geomean **1.235** (copy 1.38–2.62, slice 1.08–1.17 now winning via fusion; concat still ~0.72 from 2-launch overhead). GPU 0 idle before/after.

## Run 4 — single-launch concat (v3, final)
- Added a single coalesced concat kernel (segment branch, no index math). PASS=40/40 bit-exact.
- A/B: production geomean **1.322** (concat → 1.000 / 0.863 parity; copy 1.38–2.63; slice 1.09–1.14). GPU 0 idle before (`0 %, 4 MiB`) and after (`0 %, 4 MiB`).
- Final result frozen; see `docs/results.md`.

## Run 5 — Round 1: corrected AC-4 grid + hardened validation (final)
- Round 0 review found the slice production rows used full_heads=48/64 (output heads 24/32) instead of the immutable AC-4 contract (model h_full=24/32, h_local=h_full/sp_size=12/16). Regenerated the slice production grid to the AC-4 contract (48/64 demoted to regression); enriched `workloads.json` with full per-tensor + scalar schema + a validator (`gen_workloads.py --check` and correctness load); hardened the candidate to reject invalid order / misaligned or out-of-range h_start / pre-sliced prefix; added the AC-3/AC-4 negative-test matrix.
- Rebuilt on GPU 0 (idle). `gen_workloads.py --check`: schema-valid (22 rows). Correctness `--impl both`: **PASS=44/44** bit-exact, negative_control OK, negative_matrix OK (all invalid rows rejected, incl. kernel-level).
- A/A: geomean **1.0023**. A/B (corrected grid): production geomean **1.409** — flux_slice (hf24→hl12) 1.998× (strided contiguous + cat vs single fused pass), joyai_slice (hf32→hl16) 1.019× (large shard dominates), copy 1.39–2.62×, concat 0.950/0.868× (parity). GPU 0 idle before (`0 %, 4 MiB`) and after (`0 %, 4 MiB`).
- Round 1 candidate sha256 `364faf8a...` (historical). See `docs/results.md` for the current authoritative hash.

## Run 6 — Round 2: layout enforcement + full negative matrix + cross-product grid (final)
- Round 1 review found the candidate fast path could silently mis-handle non-dense strides, the slice regression grid missed 2 order×rank rows, the production audit was shape-set-only, and implementation comments contained plan markers. Fixed all four: `solution/kernel.cu` now validates exact supported layouts (dense concat/shard/prefix, non-contiguous head-sliced copy source, head-dim/shape/dtype) and rejects otherwise; added the 2 missing slice rows (full order×rank matrix); replaced the audit with an exact per-row production-contract check; removed `AC-` markers from code.
- Rebuilt on idle GPU 0. `gen_workloads.py --check`: schema + contract valid (24 rows). Correctness `--impl both`: **PASS=48/48** bit-exact, negative_control OK, **negative_matrix OK** including the new kernel-level rejections (sequence-strided concat, non-dense slice shard/prefix, contiguous copy source, dtype mismatch, shape mismatch).
- A/A: geomean **0.9996**. A/B: production geomean **1.406** (flux_slice 1.90×, joyai_slice 1.00×, copy 1.38–2.62×, concat parity). GPU 0 idle before (`0 %, 4 MiB`) and after (`0 %, 4 MiB`).
- Round 2 candidate sha256 `5e042273...` (historical). See `docs/results.md` for the current authoritative hash.

## Run 7 — Round 4: code-review validation hardening (B>1 / shape contract)
- Codex code review (review phase) raised two [P2] ABI-validation gaps: source-dimension checks omitted `size(0)==B`/`D`, and the output check allowed a padded `B>1` batch stride. Fixed both in `solution/kernel.cu`: every source dim (batch, seq, head, head_dim) is validated against the output before launch, and `check_4d_contig_output` now requires a dense batch stride for non-size-1 batch. Added CUDA negatives for source-batch mismatch and padded output batch stride.
- Rebuilt on B200 (correctness ran on GPU 0). Correctness `--impl both`: **PASS=48/48** bit-exact, negative_control OK, negative_matrix OK (incl. the 2 new rejections).
- These are host-side O(1) checks before the kernel launch; the copy/concat/slice data paths are byte-identical, so the Round 2 idle-GPU-0 headline (geomean 1.406×) is unaffected. No fully-idle B200 was free at re-measure time (GPUs 0/7 newly occupied); a confirmation A/B on GPU 2 (0% util, 5.7 GB co-resident — interleaved A/B is robust to a dormant co-resident allocation) gave production geomean **1.3924×** (24/24), corroborating no regression. The headline remains the Round 2 clean-GPU measurement.

## Run 8 — Round 5: cross-device rejection + provenance hash refresh
- Codex code review raised [P2] (cross-CUDA-device inputs accepted) and [P3] (stale recorded kernel hash). Fixed: `solution/kernel.cu` now requires `source_a`/`source_b` `device_id == output` before taking data pointers; `bench/correctness.py` adds a cross-device negative test (guarded by `device_count()>=2`). `docs/results.md` provenance hash refreshed to the committed kernel `4f102e04...`.
- Host-side device check only; data path byte-identical, headline (1.406×, idle GPU 0) unaffected. Rebuilt on B200; correctness `--impl both` PASS=48/48 bit-exact, negative_matrix OK (incl. cross-device rejection when ≥2 devices visible).
- Current committed `solution/kernel.cu` sha256: `4f102e045d6fa595679d51a0b2f25605fab740df77ce6527987dba389eeb9c44`.

## Notes
- No SGLang import/patch at runtime; all benchmark code is task-local.
- Raw `bench/results.jsonl` / `bench/results_aa.jsonl` kept locally on the remote workspace for evidence; excluded from the PR (definitive numbers are in `docs/results.md`).
- No NCU run was required: the bottleneck (index-math overhead on contiguous segments vs ATen, and the fusion byte-savings on slice) was unambiguous from the A/B numbers + a bytes/bandwidth roofline, and the candidate reached a clear geomean win. NCU remains available in-container if a future iteration targets the concat parity gap.
