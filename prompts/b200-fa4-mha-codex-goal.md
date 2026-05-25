# B200 FA4 MHA Codex Goal Prompt

Copy this as one Codex Goal prompt.

```text
/goal Implement a FA4-comparable BF16 forward-only MHA attention kernel for NVIDIA B200 in a standalone optimization workspace until the final correct implementation beats official FlashAttention-4 by at least 5% geometric-mean TFLOPS across the configured B200 cases, verified by PyTorch/FP32-oracle correctness checks and benchmark logs from the same ion-b200 GPU0 container.

Environment and command boundary:
- Use the ion-b200 remote GPU environment for all B200 work.
- All CUDA, Python, pip, nvcc, build, test, benchmark, and Nsight Compute
  commands must run inside the existing sglang_bbuf Docker container on
  ion-b200, with GPU0 selected.
- Use this command pattern for remote execution:

  ssh ion-b200 'docker exec sglang_bbuf bash -lc "CUDA_VISIBLE_DEVICES=0 <command>"'

- Do not run Python, pip, nvcc, builds, tests, benchmarks, or profiling
  directly on the ion-b200 host.
- Do not pip install flash-attn on the host. The container already has
  FlashAttention-4 installed; use it as the main performance baseline.

Goal scope:
- Do not invoke the Humanize kernel agent loop, RLCR, or `/humanize`; this is a
  Codex Goal workflow.
- Build the candidate in a standalone optimization workspace with its own
  build, harness, benchmark scripts, source lineage notes, and dispatch path.
- "Standalone" does not mean clean-room or from-scratch. Do not call official
  FlashAttention-4 from the candidate execution path, but public/reference
  kernel source may be studied, copied, ported, adapted, or simplified when
  license-compatible and recorded.
- Forward pass only.
- No backward.
- No GQA.
- No serving or framework integration.

Workload:
- Operation type: dense multi-head attention forward.
- dtype: BF16.
- head_dim: 128.
- num_heads: 16.
- total tokens: 32768.
- Benchmark cases:
  - batch=8, seqlen=4096
  - batch=4, seqlen=8192
  - batch=2, seqlen=16384
  - batch=1, seqlen=32768
  - Test both causal=false and causal=true.

Implementation-source policy:
- This run is baseline-aware kernel evolution, not blind kernel synthesis.
- Treat official FlashAttention-4, CUTLASS/CuTe SM100 examples, TileLang
  kernels, and other public Blackwell attention kernels as reference and
  porting materials. They may be studied or used as sources for
  license-compatible CUDA/C++/CUTLASS/CuTe ports and canonical helper code.
  Record the exact source path, commit or installed version, and what was
  adapted.
- The final candidate implementation must be a native CUDA kernel built from
  workspace-owned C++/CUDA source, such as `.cu`, `.cuh`, `.cpp`, or `.h`
  files compiled with nvcc or an equivalent CUDA extension build. Python is
  allowed for harnesses, bindings, benchmark scripts, and dispatch glue, but
  not as the primary kernel implementation.
- Do not use official FlashAttention-4, `flash_attn.cute.flash_attn_func`,
  `FlashAttentionForwardSm100`, Python `cute.compile` over the FA4 CuTe DSL
  kernel class, TileLang, Triton, torch SDPA, or any other prebuilt attention
  op as the candidate execution path. These sources may only be inspected or
  ported into native C++/CUDA/CUTLASS/CuTe code owned by this workspace.
- The first performance-oriented candidate should be baseline-derived or
  canonical-helper-derived unless there is a measured reason not to. A naive
  kernel is acceptable only as a harness/correctness smoke test, not as the
  main optimization lineage.
- Do not hand-derive tcgen05 SmemDescriptor encodings, TMEM layouts, TMA
  swizzles, warpgroup synchronization protocols, or Blackwell MMA instruction
  wrappers when an official or de facto canonical helper exists. Prefer porting
  the helper and validating it with a microcase.
- Use CUDA C++, CUTLASS/CuTe C++ templates, generated CUDA helper code, and
  optional inline PTX when they make the Blackwell-specific details more
  reliable.

Verification surface:
- Establish an immutable official FlashAttention-4 baseline in the same
  ion-b200 GPU0 container before optimization claims.
- Match standard scaled dot-product attention forward semantics for BF16 Q, K,
  and V with head_dim=128.
- Apply causal masking only when causal=true.
- Use a numerically stable online softmax/LSE-compatible formulation in the
  kernel.
- Treat PyTorch/FP32 attention as the semantic correctness oracle. Official
  FlashAttention-4 is the performance baseline and a useful cross-check, but it
  is also a tiled BF16 implementation with its own reduction order.
- Do not use a fixed 5e-3 absolute difference against FA4 as a hard correctness
  gate for all cases. Use an SGLang-style dynamic numerical bound when
  practical: compare the candidate error against the PyTorch/FP32 oracle to the
  error of a PyTorch BF16 or reordered BF16 reference, and require the
  candidate to stay within a small multiple of that numerical-error scale while
  passing NaN/Inf checks.
- If the harness cannot cheaply compute a dynamic bound, keep the semantic
  pass/fail gate on the PyTorch/FP32 oracle and use FA4 comparison as diagnostic
  evidence. A relaxed FA4 cross-check such as abs <= 2e-2 and rel <= 0.10 may
  catch gross divergence, but record it as methodology rather than the semantic
  oracle.
- The final candidate must pass correctness before benchmark claims count.
- Follow Dao-AILab/flash-attention benchmarks/benchmark_attn.py methodology as
  closely as practical, including warmup and repeat logic.
- Report per-case mean latency, std, TFLOPS, and geometric mean TFLOPS.
- Keep benchmark scripts and raw result logs in the workspace.
- Do not change the FA4 baseline, benchmark formula, warmup/repeat policy, or
  target cases after the first baseline is recorded unless the user explicitly
  asks for a methodology change. If a benchmark bug is found, record the
  before/after methodology.

Allowed knowledge and profiling tools:
- Use KernelWiki when prior B200, SM100, FlashAttention-4, CUTLASS, CuTe,
  TileLang, or attention-kernel evidence can guide a design choice.
- Use ncu-report-skill / Nsight Compute when a correct candidate is not clearly
  target-complete or when profiler evidence would change the next edit.
- Before attempting a hand-written Blackwell primitive, inspect the relevant
  upstream/reference implementation and record whether the run will port,
  simplify, or deliberately avoid it. Wrapping or importing the upstream
  Python/DSL kernel object is not a valid candidate implementation.

Iteration policy:
- Start by identifying the official FA4 source path/version, at least one
  canonical Blackwell helper source to inspect and port from, the baseline
  command, correctness command, benchmark command, first candidate direction,
  major risks, and promotion evidence.
- Establish the smallest correctness smoke test needed to prove the harness,
  then immediately move to a baseline-derived or canonical-helper-derived
  performance candidate.
- Do not spend multiple rounds optimizing a naive lineage that is structurally
  incapable of approaching FA4.
- If a correct candidate is more than 3x slower than official FA4 after one
  tensor-core-capable attempt, stop local micro-tuning of that lineage and
  reset to a stronger native CUDA/CUTLASS/CuTe porting parent.
- If a tensor-core/TMEM/tcgen05 microcase remains incorrect for two focused
  iterations, stop hand-deriving that path and switch to canonical helper
  extraction or a different parent implementation.
- Consider B200/SM100-specific features and attention patterns such as TMA,
  TMEM where useful, tcgen05/tensor-core MMA choices, warp specialization,
  persistent scheduling, split-Q or split-K scheduling, online softmax/LSE,
  causal masking efficiency, vectorized BF16 memory traffic, and occupancy vs
  register-pressure tradeoffs.
- Shape-specialized kernels, template/config variants, causal/non-causal paths,
  and a dispatcher or autotune table are allowed when measured evidence shows
  that different sequence lengths or causal modes need different CTA,
  warpgroup, TMEM, or register-pressure tradeoffs.
- The final score may use the fastest correct variant per configured case, but
  every dispatched variant must pass correctness for its assigned case.
- After each candidate, record name, parent, changed files, hypothesis,
  correctness result, per-case benchmark result, profiler evidence if collected,
  promote/reject reason, and the next best experiment. Keep a performance map
  and lineage notes so a future engineer can reconstruct the selected path.

Completion criteria:
- Mark the Goal complete only when the final correct implementation beats
  official FlashAttention-4 by at least 5% geometric-mean TFLOPS across all
  configured B200 cases in the same GPU0 container, with benchmark logs and
  correctness results saved.
- If benchmarks cannot run, correctness cannot be verified, or no defensible
  path to FA4+5% remains under the available workspace, stop with a report that
  separates confirmed results, best correct candidate, failed directions,
  blockers, remaining uncertainty, and the next source material or profiling
  evidence that would unlock progress.
- The final report must include FlashAttention-4 baseline numbers, final
  numbers, geometric mean TFLOPS, correctness tolerances, build/test/benchmark
  commands, source lineage, and key design decisions.
```
