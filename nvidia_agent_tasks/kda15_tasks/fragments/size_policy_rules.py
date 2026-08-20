"""Paste into `flashinfer_benchmarks/benchmarks/size_policy.py` when importing.

Both rules split on the axis that actually drives the work, not on the batch:

* MLA decode walks a page table, so the total page count is the work. The two
  long-history operating points (17.7k and 21.5k pages) are the bandwidth-bound
  regime; the 4-5k ones are launch/occupancy bound, which is where a decode kernel
  regresses without anyone noticing.
* Packed GDN decode does a fixed amount of work per sequence, so the batch is the
  work, and 8 is where the kernel stops being launch-bound.
"""

_RULES_TO_ADD = {
    "glm47_mla_decode_grouped_h20_ckv512_kpe64": lambda a, d: (
        _require(a, "len_kv_indices", d) >= 8192
    ),
    "qwen3next_gdn_packed_decode_hv4_d128": lambda a, d: _require(a, "num_seqs", d) >= 8,
}

# The floor is what the capture actually shipped, so pruning cannot quietly drop a tier.
_MIN_SMALL_TO_ADD = {
    "glm47_mla_decode_grouped_h20_ckv512_kpe64": 5,
    "qwen3next_gdn_packed_decode_hv4_d128": 5,
}

_MIN_LARGE_TO_ADD = {
    "glm47_mla_decode_grouped_h20_ckv512_kpe64": 2,
    "qwen3next_gdn_packed_decode_hv4_d128": 3,
}
