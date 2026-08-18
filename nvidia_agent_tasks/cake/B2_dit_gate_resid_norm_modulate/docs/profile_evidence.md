# Profile evidence: Fused norm / scale / shift residue (Wan2.2-TI2V-5B)

## `workloads.json` (model: `Wan-AI/Wan2.2-TI2V-5B-Diffusers`)

| op | real calls | distinct signatures | rows kept |
| --- | ---: | ---: | ---: |
| `diffusion_fused_scale_residual_norm_scale_shift` | 60 | 2 | 2 |
| `diffusion_fused_norm_scale_shift` | 31 | 2 | 2 |

Representative shapes (largest / smallest kept row per op):

- `diffusion_fused_scale_residual_norm_scale_shift` hottest: residual[1, 8190, 3072]:bfloat16, x[1, 8190, 3072]:bfloat16, gate[1, 1, 3072]:float32, weight[3072]:float32, bias[3072]:float32, scale[1]:bfloat16
  - another operating point: residual[1, 8190, 3072]:bfloat16, x[1, 8190, 3072]:bfloat16, scale[1, 1, 3072]:float32, shift[1, 1, 3072]:float32
- `diffusion_fused_norm_scale_shift` hottest: x[1, 8190, 3072]:bfloat16, scale[1, 1, 3072]:float32, shift[1, 1, 3072]:float32
  - another operating point: x[1, 8190, 3072]:bfloat16, scale[1, 1, 3072]:bfloat16, shift[1, 1, 3072]:bfloat16


Call counts are real traffic only: every call observed before a capture-group
label was active (start-up, CUDA-graph capture, autotune) is kept separately in
the `warmup_only_shapes` section of the source manifest and never enters a
workload row. See `../../docs/workload_capture.md`.

Captured entry points: `try_fused_scale_residual_norm_scale_shift` (60 calls) and
`try_fused_norm_scale_shift` (31 calls) on `x[1, 8190, 3072]` - i.e. SGLang already fuses
norm+scale+shift and the scale+residual variant. The remaining delta to TRT-LLM's
`fusedDiTGateResidNormShiftScale` is the gate multiply, the residual add and the dual output.

Honest sizing, restated: this residue is 1-4% of a step and our existing elementwise kernels
already run at 70-88% of achievable bandwidth, so the ceiling is small. It is included because
the kernel already exists on your side; it is the lowest-priority item in this handoff.
