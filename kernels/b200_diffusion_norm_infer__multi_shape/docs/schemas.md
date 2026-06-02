# Evidence Schemas — `b200_diffusion_norm_infer__multi_shape`

Canonical schemas for `benchmark.csv` and `solutions.jsonl`. Every candidate and every measured result MUST conform so evidence is comparable across rounds.

## `benchmark.csv`

One row per (candidate, shape, metric). Columns (matches `benchmark.py`'s writer; geomean is a synthetic row):

| Column | Meaning |
|---|---|
| `timestamp_utc` | ISO-8601 UTC of the measurement |
| `candidate_id` | A concrete candidate id that MUST exist in `solutions.jsonl` (including the geomean row — it uses the same candidate id, not a literal `geomean`). Joins to provenance. |
| `case_name` | Shape/case name, e.g. `helios__fp32__M8640N5120`, `rms__bf16__S648720D128`, or `production_geomean` for the geomean row |
| `metric` | `median_us` (primary), or `geomean_speedup_x` for the geomean row |
| `baseline_us` | Baseline median latency (µs); empty for the geomean row |
| `candidate_us` | Candidate median latency (µs); empty for the geomean row |
| `speedup_x` | `baseline_us / candidate_us` (e.g. `1.234567x`); for the geomean row, the geometric mean of per-shape speedups |
| `notes` | `key=value` pairs. Per-shape distribution for BOTH baseline and candidate (AC-6 requires median/mean/std/min/p10/p90 for each — median is the `*_us` column above): `baseline_mean_us`, `baseline_std_us`, `baseline_min_us`, `baseline_p10_us`, `baseline_p90_us`, `cand_mean_us`, `cand_std_us`, `cand_min_us`, `cand_p10_us`, `cand_p90_us`, plus `speedup_min_x`, `interleaved`, `iters`, `warmup`, `gpu_model`, `gpu_id`, `host`, `container`, `metric_kind` (`wall_clock` primary / `kernel_event` secondary), `slug` |

Rules:
- PRIMARY promotion metric is `metric_kind=wall_clock` (wrapper-inclusive `perf_counter`+`cuda.synchronize`). Also emit `metric_kind=kernel_event` (CUDA-event kernel-only) rows for diagnosis.
- Baseline and candidate measured on the SAME selected idle B200 GPU and container in the same run.
- Full provenance (commit, container image, driver, candidate source hash, exact command) lives in the matching `solutions.jsonl` record, joined by `candidate_id`.

## `solutions.jsonl`

One JSON object per line. Fields:

```json
{
  "id": "cand-0003-rms-warp-per-row",
  "parent": "cand-0002-rms-naive-port",
  "timestamp_utc": "2026-06-01T23:40:00Z",
  "family": "rms_bf16_d128 | ln_fp32",
  "status": "baseline | correct | faster | slower | nogo | promoted",
  "description": "one-warp-per-row bf16 RMS, vectorized 128-bit loads",
  "source_files": ["src/norm_cuda/rmsnorm_d128.cuh"],
  "source_hash": "<git blob or sha256 of the .cuh>",
  "env": {"sglang_commit": "<sha>", "cuda": "12.x", "driver": "<ver>", "container": "sglang_bbuf", "gpu_model": "NVIDIA B200", "gpu_id": 3, "host": "ion-b200"},
  "evidence": {"benchmark_csv": "rows for this candidate_id", "ncu_report": "profile/<run>/REPORT.md", "correctness": "KDA_RUN_CORRECTNESS=1 pytest ... PASSED"},
  "sources": ["KernelWiki:pr-... | upstream PR URL | CUTLASS example"],
  "notes": "kept/rejected rationale; active bound; roofline numbers"
}
```

Rules:
- Every candidate (including the first correctness port and any baseline reference) gets a record with a `parent` link so the search DAG is reconstructable.
- `status=nogo` requires correctness + baseline numbers + attempts + benchmark/NCU evidence + a named active bound (see AC-12).
- `status=promoted` requires per-shape parity-or-better (AC-7) for its assigned bucket.
- No fabricated values — GPU id/model/commit must be the real recorded environment.