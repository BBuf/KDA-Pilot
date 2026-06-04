# Baseline Source Provenance

## Upstream Resolution

| Field | Value |
|---|---|
| Repository URL | `https://github.com/sgl-project/sglang` |
| Branch | `main` |
| Resolved commit SHA | `133254086bf1f5b887c8c99d311719102d58a7eb` |
| Resolution time (UTC) | `2026-06-04T15:16:13Z` |
| Resolution command | `git ls-remote https://github.com/sgl-project/sglang.git refs/heads/main` |

Entry-point existence verified at the resolved commit:
`triton_group_norm_silu` (`python/sglang/jit_kernel/diffusion/triton/group_norm_silu.py`, public def present)
and `apply_group_norm_silu` (`python/sglang/jit_kernel/diffusion/group_norm_silu.py`, public def present).

## Copied Files

| Local file | Upstream path @ resolved SHA | Upstream content sha256 (pristine, pre-edit) |
|---|---|---|
| `baseline/group_norm_silu_triton.py` | `python/sglang/jit_kernel/diffusion/triton/group_norm_silu.py` | `03a0e073cdf7a8ea5111393f952af511dc98849c2545d40da829d11e928fbc1b` |
| `baseline/group_norm_silu_apply.py` | `python/sglang/jit_kernel/diffusion/group_norm_silu.py` | `19143db4d2700007544a674eb92e5ba8d1526ef75df7c39ea8c506bc56eec172` |
| `baseline/__init__.py` | (new file, not upstream — makes `baseline/` importable as a package) | n/a |

To re-verify byte equality against upstream modulo the recorded edits:

```bash
git -C <sglang-clone> show 133254086bf1f5b887c8c99d311719102d58a7eb:python/sglang/jit_kernel/diffusion/triton/group_norm_silu.py | shasum -a 256
git -C <sglang-clone> show 133254086bf1f5b887c8c99d311719102d58a7eb:python/sglang/jit_kernel/diffusion/group_norm_silu.py | shasum -a 256
# then diff against baseline/*.py; the only deltas must be the two LOCAL EDIT blocks below.
```

## Local Edits (complete list)

The standalone benchmark contract forbids importing/patching SGLang at correctness/benchmark
runtime, so the copies carry exactly two surgical edits, each marked with a `LOCAL EDIT` comment
in the source:

1. `baseline/group_norm_silu_triton.py` — the line
   `from sglang.srt.utils.custom_op import register_custom_op`
   is replaced by a local identity-decorator shim (`register_custom_op(*_args, **_kwargs)`
   returning the function unchanged). Effect: the copied baseline keeps the exact same Python
   call path minus torch custom-op dispatch registration. This is a conservative edit for
   benchmarking purposes: removing dispatcher overhead can only make the baseline faster,
   never slower, so candidate speedups are not inflated by it.
2. `baseline/group_norm_silu_apply.py` — the function-body import
   `from sglang.jit_kernel.diffusion.triton.group_norm_silu import triton_group_norm_silu`
   is replaced by the package-relative `from .group_norm_silu_triton import triton_group_norm_silu`,
   binding the wrapper to the local copied Triton implementation.

No other lines differ from upstream.

## Baseline Behavior Notes (verbatim upstream semantics, kept)

- `_can_use_triton_group_norm_silu` gates the Triton path on: CUDA tensor, **grad mode disabled**
  (`not torch.is_grad_enabled()` and `not x.requires_grad`), dtype in {fp16, bf16, fp32},
  ndim in 2..5, `C % num_groups == 0`, CUDA weight/bias of matching dtype with shape `(C,)`.
  Anything else silently falls back to eager `F.silu(F.group_norm(...))`
  (`_group_norm_silu_native`). Benchmark/correctness runs must therefore run under
  `torch.no_grad()` and verify the Triton path is actually taken (see
  `docs/benchmark_method.md` and the authenticity check in `bench/correctness.py`).
- Two-path Triton implementation: `group_size >= _LARGE_GROUP_THRESHOLD (1<<18)` →
  `_launch_chunked` (two-kernel stats+apply, BLOCK 4096 × 2 blocks/program, internal partial-sum
  scratch allocated per call); otherwise `_launch_one_pass` (single program per group).
- `apply_group_norm_silu` additionally gates on `isinstance(norm, nn.GroupNorm)`,
  `isinstance(activation, nn.SiLU)`, `not activation.inplace`, `norm.affine`, and weight/bias
  presence before delegating to `triton_group_norm_silu(x, norm.weight, norm.bias,
  num_groups=norm.num_groups, eps=norm.eps)`; otherwise returns eager `activation(norm(x))`.

## Drift Verdict vs the PR #21-era Capture Baseline

**Verdict: none (routing-only divergence elsewhere; Triton implementation unchanged).**

Evidence:

- Upstream history of `python/sglang/jit_kernel/diffusion/triton/group_norm_silu.py` at the
  resolved commit contains exactly three commits — `cd6ad80c00` (add HunyuanVideo
  GroupNorm+SiLU fast path, #22814), `1360848ee1` (optimize large GroupNorm SiLU apply,
  #23938), `b712dd48fe` (enable fuse by default, #23148) — all predating the 2026-06 retained
  H200 captures that anchor `bench/workloads.json`.
- Byte comparison against the 2026-06-02 local reference checkout (`0689ba84b8`): the first 398
  lines (all five `@triton.jit` kernels, gates, launchers, thresholds `_LARGE_GROUP_THRESHOLD =
  1<<18`, `_BLOCK_SIZE = 4096`, `_BLOCKS_PER_PROGRAM = 2`) are **identical**. The only
  difference is the public routing tail: that local checkout sat on a divergent branch (neither
  SHA is an ancestor of the other) carrying the since-abandoned in-tree
  `group_norm_silu_kda` dispatcher routing; upstream `main` has no `group_norm_silu_kda.py`
  and routes both public entries directly to the Triton implementation.
- Consequence: the freshly copied baseline matches the implementation the retained HunyuanVideo
  capture rows were produced against, and the task prompt's entry-point list is current. No
  user escalation needed under the drift decision tree (entry points present, semantics
  unchanged).
