# GLM-4.7-Flash: absorbed-MLA grouped decode attention

Beat `decode_attention_fwd_grouped` on the shapes GLM-4.7-Flash actually decodes with.

One kernel, one entry point:

| op | symbol | rows |
| --- | --- | ---: |
| `triton_decode_attention_grouped` | `sglang.kernels.ops.attention.decode_attention.decode_attention_fwd_grouped` | 15 |

## What the kernel does

One query token per sequence attends over that sequence's pages in the paged KV pool.
The layout is absorbed MLA with `page_size = 1`: a pool row is 576 wide - 512 compressed
KV plus a 64-wide rope key - and the value tensor is *the same row* truncated to 512, so
`v_buffer` is a view of `k_buffer` with stride 576 over a 512-wide shape. 20 query heads
share it. The kernel is split-K: `num_kv_splits` per sequence, partials in `attn_logits`
and `attn_lse` sized for `max_kv_splits = 256`, then a reduction into `o`.

`o` is a destination - the kernel writes through it and returns None - so the gate
compares that argument after the call (`OUTPUT_ARGS` in `baseline/entry.py`).

## Where the shapes come from

GLM-4.7-Flash served with its own SGLang cookbook command on 8x B300 SXM6, GSM8K 0.820
on the capture run, over four operating points: GSM8K 5-shot serial, 5-shot at
concurrency 32, 16-shot at concurrency 16, and random 1k/256 at concurrency 16. Batch
runs 7 to 22 tokens and the page tables carry 4,125 to 21,520 pages, all against a
3,689,231-row pool - a real deployment's fragmentation, not a synthetic contiguous table.

Seven of the fifteen rows ship their captured page tables, split counts and query.
The capture recorded which pages the other rows read but not the 24 MB of page contents
each would need, so those rows get in-bounds page tables derived from the row itself
(`tools/derive_inputs.py`) - the addressing is real, the page values are drawn.

## What a win has to clear

* `docs/measurement_contract.md` - CUDA-graph timing, interleaved arms, cold L2. The
  identity floor on this task is ~1.00x; anything under that is noise, not a win.
* `docs/anti_hack_contract.md` - the tolerance is SGLang's own for this kernel
  (rtol 1e-2 / atol 1e-3, `test_triton_attention_kernels.py:309`), and it is checked
  before any speedup is reported.
* A row whose page table is empty is a real operating point (a sequence with no cached
  history), not an input to reject: attend to nothing and write a zero row.

## Running it

```bash
python tools/check_task.py glm47_flash__mla_decode_grouped
python glm47_flash__mla_decode_grouped/tests/test_contract.py
python tools/bench_harness.py glm47_flash__mla_decode_grouped
cp glm47_flash__mla_decode_grouped/solution/entry.py.template glm47_flash__mla_decode_grouped/solution/entry.py
python tools/bench_harness.py glm47_flash__mla_decode_grouped --json report.json
python glm47_flash__mla_decode_grouped/tests/test_solution.py
```

The same definition is also packaged for KDA-1.5 in `kda15_tasks/` - axes, constraints
and a pure-PyTorch reference instead of a replayed call site.
