# B200 int8_scaled_mm Codex Goal Prompt

Copy this as one Codex Goal prompt.

```text
/goal Optimize SGLang's int8_scaled_mm kernel on NVIDIA B200 for the focused M=64, N=2048, K=2048, out_dtype=fp16, bias=true case until a correct candidate is at least 2.5x faster than the current SGLang baseline on median latency, verified by reproducible correctness checks and benchmark logs from the same ion-b200 GPU0 container.

Environment and command boundary:
- Use the ion-b200 remote GPU environment for all B200 work.
- All CUDA, Python, pip, nvcc, build, test, benchmark, and Nsight Compute
  commands must run inside the existing sglang_bbuf Docker container on
  ion-b200, with GPU0 selected.
- Use this command pattern for remote execution:

  ssh ion-b200 'docker exec sglang_bbuf bash -lc "CUDA_VISIBLE_DEVICES=0 <command>"'

- Do not run Python, pip, nvcc, builds, tests, benchmarks, or profiling
  directly on the ion-b200 host.

Goal scope:
- Work in the current standalone workspace root.
- Do not invoke the Humanize kernel agent loop, RLCR, or `/humanize`; this is a
  Codex Goal workflow.
- Build a benchmarkable and profileable CUDA/C++ or CUDA inline-PTX candidate.
- Keep the optimization focused on this single shape first:
  - M=64
  - N=2048
  - K=2048
  - out_dtype=fp16
  - bias=true
- Do not change SGLang public behavior or public APIs unless a minimal local
  harness requires it for baseline measurement.

Verification surface:
- Inspect the current SGLang implementation path for int8_scaled_mm.
- Build a reproducible baseline harness before optimizing.
- Report SGLang baseline median latency for the exact focused case.
- Optional secondary baselines are allowed, such as torch._int_mm or fp16 GEMM,
  but the acceptance target is relative to the current SGLang implementation.
- Compare candidate output against the current SGLang result and a PyTorch
  reference when practical.
- Include bias in every validation path.
- Report max absolute error, relative error, and the tolerance used.
- The final candidate must pass correctness before benchmark claims count.
- Use warmup and repeated timing, and report median latency, mean latency, std,
  min, p10, p90, and speedup over the SGLang baseline.
- Keep benchmark scripts and raw result logs in the workspace.
- Every claimed improvement must identify the candidate commit or file version
  and the exact command used to produce the result.

Allowed knowledge and profiling tools:
- Use KernelWiki when prior B200, SM100, CUTLASS, SGLang, or int8 GEMM evidence
  can guide a design choice.
- Use ncu-report-skill / Nsight Compute when a correct candidate is not clearly
  target-complete or when profiler evidence would change the next edit.
- Treat upstream SGLang, CUTLASS/CuTe, CUDA samples, and relevant public
  Blackwell INT8 GEMM kernels as working materials when license-compatible.
  Record source path, commit or version, and what was adapted.

Iteration policy:
- Start by establishing the immutable baseline, correctness harness, benchmark
  command, and first candidate direction.
- Prefer evidence-backed edits over broad rewrites.
- Consider B200/SM100-specific paths such as tcgen05 INT8 MMA, TMEM/TMA where
  appropriate, warp specialization, persistent scheduling, Stream-K or split-K,
  cluster shape choices, vectorized loads/stores, shared-memory staging, and a
  fused bias/output epilogue.
- After each candidate, record what changed, correctness result, benchmark
  result, profiler evidence if collected, promote/reject reason, and the next
  best experiment.
- If a direction cannot be implemented cleanly, fails correctness repeatedly,
  or shows no credible speedup path after focused attempts, record the evidence
  and switch to the next ranked direction.

Completion criteria:
- Mark the Goal complete only when a correct candidate is at least 2.5x faster
  than the SGLang baseline on median latency for the exact focused case in the
  same B200 GPU0 container, with benchmark logs and correctness results saved.
- If the benchmark cannot run, correctness cannot be verified, or no defensible
  path to the 2.5x target remains under the available workspace, stop with a
  report listing attempted paths, gathered evidence, best correct result,
  blockers, and the next input or source material that would unlock progress.
- The final report must include baseline numbers, final numbers, speedup,
  correctness tolerances, build/test/benchmark commands, key design decisions,
  and the next most promising follow-up if the target is not reached.
```
