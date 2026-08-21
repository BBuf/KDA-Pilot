# KDA-1.5-native task packages

Two kernel tasks cut from real serving captures and packaged the way **KDA-1.5 registers
its own tasks** - `gdn_prefill`, `kda_forward`, `dsa_attention` - rather than the way the
rest of this directory packages a recorded call site. The difference is the whole point:

| | captured-call-site task (the rest of this repo) | native definition (here) |
| --- | --- | --- |
| what is registered | a recorded call, arguments and all | a kernel definition: axes, constraints, reference |
| inputs | replayed from the recording; addresses into multi-GB pools have to be reconstructed | constructed by the benchmark from the axes; only the arguments that must be real ship as blobs |
| how many kernels | as many as the call site touched (7, 9, 12) | one |
| correctness | the production kernel run twice | the candidate against the baseline package, with a pure-PyTorch reference in the definition |
| failure mode | a reconstructed address is out of bounds and the sweep dies | there is no address to reconstruct |

## The tasks

| definition | model | kernel | rows | tiers |
| --- | --- | --- | ---: | --- |
| `glm47_mla_decode_grouped_h20_ckv512_kpe64` | GLM-4.7-Flash | `decode_attention_fwd_grouped` (absorbed MLA, page_size 1) | 7 | 5 small / 2 large |
| `qwen3next_gdn_packed_decode_hv4_d128` | Qwen3-Next-80B-A3B | `TritonGDNKernel.packed_decode` (266,688 recorded calls) | 8 | 5 small / 3 large |

Both are decode kernels with no native coverage today: KDA-1.5 has a GDN *prefill* task
and a DeepSeek sparse-MLA task, neither of which touches these two.

## Verified

On 1x B300 with SGLang main @ `43226af`, run through **KDA-1.5's own harness**
(`bench_common.run_benchmark`, CUPTI timer, cold L2, CUDA graph), with each task's
baseline as its own candidate:

```
qwen3next_gdn_packed_decode_hv4_d128   passed 8/8   all 0.9968x  large 0.9885x  small 1.0018x
glm47_mla_decode_grouped_h20_ckv512    passed 7/7   all 0.9977x  large 1.0020x  small 0.9960x
```

Every row is bit-exact against the baseline (`max_abs=0`), which for the GDN task
includes the state pool - it is the second output, returned by reference so the gate sees
it at no cost inside the timed call. A candidate that gets `out` right while advancing
the state wrongly fails here instead of drifting on the next token.

The pure-PyTorch reference each definition ships was checked against the kernel it
describes on every row, at the task's declared tolerance
(`tests/verify_reference.py`): both agree everywhere. A reference that disagrees with
the kernel is worse than no reference, because it is what the agent reads to learn the
contract.

`tests/test_package.py` is the CPU gate (no GPU, no SGLang): blob paths resolve, blob
shapes agree with the row's axes, every input is declared by the definition, the size
class agrees with the declared rule, uuids are unique, exactly one baseline package.
It found three real inconsistencies the first time it ran.

## Rebuilding

```bash
# needs torch + safetensors, no GPU
python kda15_tasks/build.py --captures <a tree of nvidia_agent_tasks captures>
python kda15_tasks/tests/test_package.py
```

`build.py` re-derives the tree from the captures, so nothing here is hand-edited.
Workload uuids are a hash of (definition, capture row, operating point), so rebuilding
does not churn the file. The builder refuses a row whose addresses contradict each other
- an indptr that does not start at zero or ends outside its index array, an index
outside the recorded pool, a split count that does not match the batch, state slots that
are not distinct.

## Importing into KDA-1.5

Five copies and two paste-ins; nothing needs rewriting:

1. `flashinfer_trace/{definitions,workloads,blob,solutions}/...` ->
   `src/kda/resources/flashinfer_benchmarks/flashinfer_trace/` (same layout, merges in).
2. `benchmarks/bench_*.py` -> `src/kda/resources/flashinfer_benchmarks/benchmarks/`.
3. `fragments/size_policy_rules.py` -> paste the rules and the two coverage floors into
   `benchmarks/size_policy.py`.
4. `fragments/registry_entries.py` -> paste the two `_flashinfer_task(...)` entries into
   `src/kda/tasks/registry.py`, and add the names to
   `tests/kda/tasks/test_task_utils.py::test_registry_contains_only_kda_tasks`.
5. Point both tasks at a runtime image that carries SGLang (the baselines import
   `sglang`); the plain flashinfer runtime does not.

The candidate entry point is `run(*args)` in a single file, named by
`BENCH_GLM47_MLA_DECODE_KERNEL` / `BENCH_QWEN3NEXT_GDN_DECODE_KERNEL` - the same shape
as every other native task, so `bench_kernel.sh` needs one line each.

## What is real and what is drawn

Stated per task in the definition, and worth being explicit about:

* **GLM-4.7-Flash MLA decode** - real: the page tables (`kv_indptr`, `kv_indices`), the
  per-sequence split counts, the query, and the pool geometry (3,689,231 rows). Drawn:
  the page *contents*. The capture recorded which pages each row reads but not their
  24 MB of values, and this is the same split the native `gdn_prefill` task makes
  between its real `cu_seqlens` blob and its drawn q/k/v. The benchmark fills only the
  pages `kv_indices` names, so the addressing, the strides and the number of distinct
  pages a sequence walks are the captured ones.
* **Qwen3-Next packed GDN decode** - real: the B=1 operating point ships its recorded
  `mixed_qkv`, `a`, `b`, `A_log`, `dt_bias`, state slot and state contents (the first
  link of a 16-step decode chain). The other seven operating points ship recorded
  *shapes* and construct distinct slots, because the only property of the captured
  indices that matters is distinctness - two sequences sharing a slot is a
  read-modify-write race, not a slower kernel - and the pool is fresh per row.
