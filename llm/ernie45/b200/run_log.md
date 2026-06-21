# ERNIE4.5 B200 Kernel Shape Sweep

- Target: `baidu/ERNIE-4.5-21B-A3B-PT`
- Cookbook page: `Ernie/Ernie4.5.md`
- Recipe: TP1 21B-A3B command from cookbook; cookbook benchmark section is AMD-focused, so this is treated as a B200 smoke/profile run rather than a B200-verified recipe.
- Status: completed on `cirrascale-gpuc5a6` with image `lmsysorg/sglang:latest`.
- Selected container: `sglang_bbuf_ernie45`.
- Runner: launched 2026-06-19T12:14:05Z, PID `670`, GPU4, port `30000`.
- Completed: 2026-06-19T12:40:11Z.
- Cleanup: HF cache `models--baidu--ERNIE-4.5-21B-A3B-PT` deleted, size before cleanup 41G.
- Shape rows: `9/6/4/9/4/4` for `random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`.
- Validation: every row is `pct_of_gpu > 2%`, SGLang-relevant, and has sample provenance. Some rows have `shape_status=missing` because torch profiler did not expose input shapes for those kernel launches; this is preserved in the JSON/TSV instead of being inferred.
- Startup note: SGLang logged a missing B200 Triton MoE config for `E=64,N=1536`.
