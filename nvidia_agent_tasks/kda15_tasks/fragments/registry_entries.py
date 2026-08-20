"""Paste into `src/kda/tasks/registry.py` inside the TASKS mapping when importing.

`_flashinfer_task` is the same constructor the native gdn_prefill / kda_forward tasks
use - these packages are native definitions, not captured-call-site replays, so nothing
about the registration is special. `benchmark_resources` lists what `kda prepare` stages
into the cell: the definition, the workload rows, the blob directory the rows point at,
and the baseline package.
"""

_ENTRIES_TO_ADD = '''
        "glm47_mla_decode_grouped": _flashinfer_task(
            name="glm47_mla_decode_grouped",
            baseline_kernel="glm47_mla_decode_grouped.py",
            benchmark_script="bench_glm47_mla_decode_standalone.py",
            kernel_env="BENCH_GLM47_MLA_DECODE_KERNEL",
            definition="glm47_mla_decode_grouped_h20_ckv512_kpe64",
            benchmark_resources=(
                "flashinfer_trace/definitions/attention/glm47_mla_decode_grouped_h20_ckv512_kpe64.json",
                "flashinfer_trace/workloads/attention/glm47_mla_decode_grouped_h20_ckv512_kpe64.jsonl",
                "flashinfer_trace/blob/workloads/attention",
                "flashinfer_trace/solutions/baseline/attention/glm47_mla_decode_grouped_h20_ckv512_kpe64",
            ),
        ),
        "qwen3next_gdn_packed_decode": _flashinfer_task(
            name="qwen3next_gdn_packed_decode",
            baseline_kernel="qwen3next_gdn_packed_decode.py",
            benchmark_script="bench_qwen3next_gdn_decode_standalone.py",
            kernel_env="BENCH_QWEN3NEXT_GDN_DECODE_KERNEL",
            definition="qwen3next_gdn_packed_decode_hv4_d128",
            benchmark_resources=(
                "flashinfer_trace/definitions/gdn/qwen3next_gdn_packed_decode_hv4_d128.json",
                "flashinfer_trace/workloads/gdn/qwen3next_gdn_packed_decode_hv4_d128.jsonl",
                "flashinfer_trace/blob/workloads/gdn",
                "flashinfer_trace/solutions/baseline/gdn/qwen3next_gdn_packed_decode_hv4_d128",
            ),
        ),
'''

# The runtime image has to be one with SGLang on it: both baselines import the kernel
# from `sglang`, which the plain flashinfer runtime does not carry.
_IMAGE_NOTE = "KDA_SGLANG_H200_IMAGE (or the B300 image on an sm_103 box)"
