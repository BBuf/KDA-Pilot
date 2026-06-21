# Ring-2.5-1T B200 Kernel Shape Sweep

- Target: `inclusionAI/Ring-2.5-1T`.
- Cookbook page: `InclusionAI/Ring-2.5-1T.md`.
- Recipe: single-node B200 TP8 FP8, `--trust-remote-code`, plus
  `--model-loader-extra-config '{"enable_multithread_load":true,"num_threads":64}'`
  and longer watchdog settings from the registered 8-GPU test. Reasoning and
  tool parsers follow the cookbook/YAML metadata: `deepseek-r1` and `qwen`.
- Status: completed + cleaned.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_ring_25_1t`.
- Runner: launched 2026-06-20T00:09:39Z, runner PID `1150`, server PID
  `1153`, GPU0-7, port `30000`. TP8 distributed initialization reached weight
  loading at 2026-06-20T00:10:35Z. Observed HF cache size was `2.1G`, with
  about `125G` allocated on each GPU at 2026-06-20T00:10:40Z.
- Current stage update: observed HF cache size was `123G` at
  2026-06-20T00:16:29Z; server was still in weight loading, with no
  interruption or OOM.
- Current stage update: observed HF cache size was `334G` at
  2026-06-20T00:27:20Z; server was still in weight loading, with no
  interruption or OOM.
- Current stage update: observed HF cache size was `550G` at
  2026-06-20T00:37:34Z; server was still in weight loading, with no
  interruption or OOM.
- Current stage update: observed HF cache size was `797G` at
  2026-06-20T00:48:29Z; server was still in weight loading, with no
  interruption or OOM.
- Current stage update: observed HF cache size was `946G` at
  2026-06-20T00:55:02Z; server was still in weight loading, with no
  interruption or OOM.
- Current stage update: HF snapshot was found locally at
  2026-06-20T00:55:15Z, so download completed/resumed successfully. The server
  began multi-thread loading `160` shards; observed progress was `54/160`
  around 2026-06-20T01:00:20Z.
- Progress: server reached `/health` at 2026-06-20T01:04:50Z. `random_low`
  and `random_mid` completed and extracted `5/7` valid `>2%`
  SGLang-relevant kernel rows; `random_high` is running.
- Progress update: `random_high` and `sharegpt_low` also completed. Current
  partial row counts are `5/7/7/5` for `random_low`, `random_mid`,
  `random_high`, and `sharegpt_low`; `sharegpt_mid` is running.
- Outcome: all six workloads completed and validated. Row counts are
  `5/7/7/5/9/7` for `random_low`, `random_mid`, `random_high`,
  `sharegpt_low`, `sharegpt_mid`, and `sharegpt_high`. Every extracted row is
  `>2%`, SGLang-relevant, has samples, and has provenance. The runner cleaned
  `/root/.cache/huggingface/hub/models--inclusionAI--Ring-2.5-1T`
  (`946G`) at 2026-06-20T01:22:20Z.
- Current stage note: at 2026-06-20T00:40:15Z the scheduler watchdog emitted a
  soft timeout dump while `load_weights` was active. HF downloads for
  `model-00111-of-00160.safetensors` hit read timeouts around
  2026-06-20T00:43 but resumed; the server process remained alive and cache
  continued growing.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
