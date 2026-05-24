# B200 FA4 MHA KernelPilot Prompt

Copy this as one end-to-end prompt.

```text
/humanize:humanize-kernel-agent-loop

Use the ion-b200 remote GPU environment for all B200 work. All CUDA, Python,
pip, nvcc, build, test, benchmark, and Nsight Compute commands must run inside
the existing sglang_bbuf Docker container on ion-b200, with GPU0 selected.

Use this command pattern for remote execution:

ssh ion-b200 'docker exec sglang_bbuf bash -lc "CUDA_VISIBLE_DEVICES=0 <command>"'

Do not run Python, pip, nvcc, builds, tests, benchmarks, or profiling directly
on the ion-b200 host. Do not pip install flash-attn on the host. The container
already has FlashAttention-4 installed; use it as the main baseline.

Task:
Implement a standalone CUDA/inline-PTX forward-only MHA attention kernel for
NVIDIA B200.

Scope:
- Forward pass only
- No backward
- No GQA
- No serving or framework integration
- dtype: BF16
- head_dim: 128
- num_heads: 16
- total tokens: 32768

Benchmark cases:
- batch=8, seqlen=4096
- batch=4, seqlen=8192
- batch=2, seqlen=16384
- batch=1, seqlen=32768
- Test both causal=false and causal=true

Target:
Beat official FlashAttention-4 by at least 5% geometric-mean TFLOPS across the
configured B200 cases.

Correctness:
- Compare against PyTorch reference and/or official FlashAttention-4 output.
- Report explicit max error and relative error tolerances.
- The final candidate must pass correctness before benchmark claims count.

Benchmarking:
- Follow Dao-AILab/flash-attention benchmarks/benchmark_attn.py methodology as
  closely as practical, including warmup and repeat logic.
- Report per-case mean latency, std, TFLOPS, and geometric mean TFLOPS.
- Include FlashAttention-4 baseline numbers from the same B200 GPU0 container
  environment.
- Keep benchmark scripts and raw result logs in the workspace.

Optimization guidance:
- Use KernelWiki when prior B200, SM100, FlashAttention-4, CUTLASS, CuTe, or
  attention-kernel evidence is useful.
- Use Nsight Compute evidence when a candidate is correct but not clearly
  target-complete.
- Consider B200/SM100-specific features and attention patterns such as TMA,
  TMEM where useful, tcgen05/tensor-core MMA choices, warp specialization,
  persistent scheduling, split-Q or split-K scheduling, online softmax/LSE,
  causal masking efficiency, vectorized BF16 memory traffic, and occupancy vs
  register-pressure tradeoffs.
- Prefer evidence-backed edits over broad rewrites. Keep a performance map of
  tested variants and rejected ideas.

Completion:
- Continue iterating until the final correct candidate beats FlashAttention-4
  by at least 5% geometric-mean TFLOPS across all configured cases.
- Do not stop with a "target blocked" or "best effort" final report. If a
  lineage stalls, use the evidence to replan or rewrite the kernel path and
  continue. Only user cancellation or verified target completion may end the
  loop.
- The final report must include FlashAttention-4 baseline numbers, final
  numbers, geometric mean TFLOPS, correctness tolerances, build/test/benchmark
  commands, and key design decisions.
```
