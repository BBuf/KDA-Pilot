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

Task contract:
- Task name: B200 FA4-comparable BF16 MHA forward kernel
- Objective: implement a FA4-comparable BF16 MHA forward-only attention kernel
  for NVIDIA B200 in a standalone optimization workspace.
- "Standalone" means the candidate has its own build, harness, ledger, and
  dispatch path in this workspace. It does not mean clean-room or from-scratch.
  Do not call official FlashAttention-4 from the candidate execution path, but
  you may study, copy, port, adapt, or simplify public/reference kernel source
  when license-compatible and recorded in the ledger.
- Comparison target: official FlashAttention-4 installed in the same
  ion-b200 container.
- Promotion criterion: the final correct implementation must beat official
  FlashAttention-4 by at least 5% geometric-mean TFLOPS across the configured
  B200 cases.

Loop bootstrap:
- Before implementing kernel candidates or running long benchmarks, ensure the
  Humanize RLCR loop is active in the chosen workspace.
- The workspace must be a git repository with one clean scaffold commit.
- Confirm that `.humanize/rlcr/<timestamp>/state.md` exists and that the loop
  was started with `--strict-success`. If RLCR did not start, stop and report
  the setup failure instead of continuing outside the loop.

Kernel information:
- Operation type: dense multi-head attention forward
- Baseline solution name: official FlashAttention-4 in the container
- Workload count: 8 configured cases
- Constant axes:
  - dtype: BF16
  - head_dim: 128
  - num_heads: 16
  - total tokens: 32768
- Variable axes:
  - batch
  - seqlen
  - causal

Scope:
- Forward pass only
- No backward
- No GQA
- No serving or framework integration

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
- If a correct candidate is more than 3x slower than official FlashAttention-4
  after one tensor-core-capable attempt, stop local micro-tuning of that lineage
  and reset to a stronger native CUDA/CUTLASS/CuTe porting parent.
- If a tensor-core/TMEM/tcgen05 microcase remains incorrect for two focused
  iterations, stop hand-deriving that path and switch to canonical helper
  extraction or a different parent implementation.

Benchmark cases:
- batch=8, seqlen=4096
- batch=4, seqlen=8192
- batch=2, seqlen=16384
- batch=1, seqlen=32768
- Test both causal=false and causal=true

Target:
Beat official FlashAttention-4 by at least 5% geometric-mean TFLOPS across the
configured B200 cases.

Reference computation:
- Match standard scaled dot-product attention forward semantics for BF16 Q, K,
  and V with head_dim=128.
- Apply causal masking only when `causal=true`.
- Use a numerically stable online softmax/LSE-compatible formulation in the
  kernel. Correctness may be checked against PyTorch and/or official
  FlashAttention-4.

Correctness:
- Compare against PyTorch reference and/or official FlashAttention-4 output.
- Report explicit max error and relative error tolerances.
- The final candidate must pass correctness before benchmark claims count.
- Preserve explicit NaN/Inf checks in every validator. Do not weaken the
  correctness harness or redefine the reference to make a candidate pass.

FA4 numerical cross-check:
- Treat PyTorch/FP32 attention as the semantic correctness oracle. Official
  FlashAttention-4 is the performance baseline and a useful cross-check, but it
  is also a tiled BF16 implementation with its own reduction order.
- Do not use a fixed `5e-3` absolute difference against FA4 as a hard
  correctness gate for all cases. SGLang's FA4 unit tests use dynamic numerical
  bounds relative to PyTorch BF16/reordered-reference error, not a universal
  fixed FA4-vs-reference threshold.
- Use an SGLang-style dynamic bound when practical: compare the candidate's
  error against the PyTorch/FP32 oracle to the error of a PyTorch BF16 or
  reordered BF16 reference, and require the candidate to stay within a small
  multiple of that numerical-error scale while also passing NaN/Inf checks.
- If the harness cannot cheaply compute a dynamic bound, use the FA4 comparison
  as diagnostic evidence and keep the semantic pass/fail gate on the
  PyTorch/FP32 oracle. A relaxed FA4 cross-check such as `abs <= 2e-2` and
  `rel <= 0.10` may be used to catch gross divergence, but it should be recorded
  as methodology rather than confused with the semantic oracle.
- If a candidate passes the PyTorch/FP32 oracle but only fails a too-strict
  fixed FA4 cross-check, do not stall the loop on numerical mimicry. Record the
  per-case FA4 diff, explain the reduction-order/tile-structure source, and
  continue toward the Phase 2/Phase 3 performance work.

Benchmarking:
- Follow Dao-AILab/flash-attention benchmarks/benchmark_attn.py methodology as
  closely as practical, including warmup and repeat logic.
- Report per-case mean latency, std, TFLOPS, and geometric mean TFLOPS.
- Include FlashAttention-4 baseline numbers from the same B200 GPU0 container
  environment.
- Keep benchmark scripts and raw result logs in the workspace.
- Do not change the FlashAttention-4 baseline, benchmark formula, warmup/repeat
  policy, or target cases after the first baseline is recorded unless the user
  explicitly asks for a methodology change. If a benchmark bug is found, record
  the before/after methodology in the ledger.

Shape specialization:
- You may write multiple specialized kernels or template/config variants for
  different benchmark cases, including separate non-causal and causal paths,
  when the evidence suggests this is the right tradeoff.
- A shape dispatcher or autotune table is allowed when one kernel cannot
  dominate all cases; it is not required if one correct implementation is best
  across the workload distribution.
- The final score may use the fastest correct variant per configured case, but
  every dispatched variant must pass correctness for its assigned case.
- Record the dispatcher decision table with per-case baseline, candidate,
  latency, TFLOPS, and promote/reject reason.
- Do not force a single universal kernel if evidence shows that different
  sequence lengths or causal modes need different CTA, warpgroup, TMEM, or
  register-pressure tradeoffs.

Workflow requirements:
- Round 0 must produce a short implementation plan before kernel edits. The
  plan should identify the baseline command, correctness command, benchmark
  command, first candidate direction, major risks, and promotion evidence.
- Round 0 must also identify the concrete native CUDA/CUTLASS/CuTe source
  lineage for the first performance-oriented candidate: official FA4 source
  path/version and at least one canonical Blackwell helper source such as
  CUTLASS/CuTe C++ examples or an equivalent public SM100 attention kernel to
  inspect and port from.
- Record every candidate in the attempt ledger with: name, parent candidate,
  changed files, hypothesis, correctness result, per-case benchmark result,
  profiler evidence if any, and promote/reject reason.
- Keep `benchmarks/performance-map.json` or an equivalent table updated with
  per-case baseline and candidate numbers.
- Keep `ledgers/lineage.jsonl` updated so a future engineer can reconstruct
  which candidate became the selected lineage and why.
- Record rejected ideas instead of silently discarding them, especially when a
  branch fails correctness, regresses a shape, or only wins one regime.
- A partial per-shape win may be retained as dispatcher evidence even if it is
  not the final universal lineage.

Phase strategy:
- Phase 1: establish the immutable FlashAttention-4 baseline, implement the
  smallest correctness smoke-test needed to prove the harness, then immediately
  move to a baseline-derived or canonical-helper-derived performance candidate.
  Do not spend multiple rounds optimizing a naive lineage that is structurally
  incapable of approaching FA4.
- Phase 2: start from the best correct Phase 1 candidate and run
  profiling-guided exploration. List candidate optimization directions, rank
  them by expected benefit and risk, then explore them systematically.
- For each Phase 2 optimization direction, try at most five focused iterations
  before deciding whether to keep, revise, or reject that direction. If a
  direction cannot be implemented cleanly, fails correctness, or has no
  credible path to improvement after those iterations, record the evidence and
  move to the next ranked direction.
- Phase 3: analyze the full configured workload distribution and decide whether
  shape-specialized dispatch or autotuning is justified by measured wins.
  Evaluate the promoted candidate or dispatcher on all 8 configured cases, not
  only on a convenient subset.

Optimization guidance:
- Use KernelWiki when prior B200, SM100, FlashAttention-4, CUTLASS, CuTe, or
  attention-kernel evidence is useful.
- Before attempting a hand-written Blackwell primitive, inspect the relevant
  upstream/reference implementation and write down whether the run will port,
  simplify, or deliberately avoid it. Wrapping or importing the upstream
  Python/DSL kernel object is not a valid candidate implementation.
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
