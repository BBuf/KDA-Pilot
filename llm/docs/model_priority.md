# LLM Model Priority

Reduced B200 scope after the full-cookbook sweep was cancelled. For each listed
series, run only the latest live SGLang cookbook model, except DeepSeek where the
requested target is the DeepSeek-V3.2 page.

Source of deployment commands: live SGLang docs
(`https://docs.sglang.io/cookbook/autoregressive/<Vendor>/<Model>.md`).

| Prio | Folder | Model | Vendor | Cookbook doc | B200 status |
|---|---|---|---|---|---|
| 1 | `minimax_m3` | MiniMax-M3 / MiniMax-M3-MXFP8 | MiniMax | `MiniMax/MiniMax-M3.md` | completed + cleaned; 6 workload inventories synced locally |
| 1 | `glm_52` | GLM-5.2-FP8 | zai-org | `GLM/GLM-5.2.md` | completed + cleaned; 6 workload inventories synced locally |
| 1 | `kimi_k27_code` | Kimi-K2.7-Code | Moonshotai | `Moonshotai/Kimi-K2.7-Code.md` | completed + cleaned; 6 workload inventories synced locally |
| 1 | `deepseek_v32` | DeepSeek-V3.2 page target | DeepSeek | `DeepSeek/DeepSeek-V3_2.md` | completed + cleaned; 6 workload inventories synced locally |

Notes:
- The previous all-cookbook run artifacts were removed from
  `llm/cookbook_b200_kernel_revisit/` locally and from the remote artifact
  mirror.
- Current ion-b200 state at 2026-06-19: only GPU4/GPU5 were idle; the listed
  targets require 8-GPU B200 commands, so no official run was started.
- Verda B200 03-3 was also checked and was already serving
  `poolside/Laguna-M.1` with TP8; it was left untouched.
- Run at most one target per machine. Delete that model's HF cache/locks after
  its folder has the kernel inventory and task records.
- DeepSeek-V3.2 NVFP4 completed on `cirrascale-gpuc5a6`
  (`bbuf@216.114.73.196`) in container `sglang_bbuf`, using GPU0-GPU3 and port
  `30180`. The runner produced all 6 workload kernel inventories and deleted
  the 387G HF snapshot at 2026-06-19T06:04:18Z.
- GLM-5.2 FP8 completed on `verda-b200-fin-03-1` through the Radix jump host, in
  container `sglang_bbuf`, using all 8 B200 GPUs and port `30000`. The runner
  produced all 6 workload kernel inventories and deleted the 704G HF snapshot at
  2026-06-19T06:46:13Z.
- Kimi-K2.7-Code completed on `verda-b200-fin-03-2` through the Radix jump host,
  in container `sglang_bbuf_kimi`, using all 8 B200 GPUs and port `30000`. The
  runner produced all 6 workload kernel inventories and deleted the 555G HF
  snapshot at 2026-06-19T07:37:29Z. Local verification found row counts:
  `13/7/11/2/2/11` for `random_low/random_mid/random_high/sharegpt_low/`
  `sharegpt_mid/sharegpt_high`, all with `sglang_relevant=true` and
  `pct_of_gpu > 2.0`.
- MiniMax-M3 MXFP8 first attempt on `cirrascale-gpua83e`
  (`bbuf@216.114.73.191`) used stale local notes (`dev-cu13-minimax-m3` with
  PD-disagg) and failed during prefill warmup; the runner cleaned the 414G
  partial snapshot at 2026-06-19T07:27:42Z. The local runner/deploy notes were
  corrected to the live B200 cookbook cell: `lmsysorg/sglang:dev-minimax-m3`,
  single TP8 server on port `30000`. The corrected runner was relaunched in
  container `sglang_bbuf_minimax_m3` at 2026-06-19T07:33:06Z with runner PID
  `1288`.
- MiniMax corrected TP8 attempt still hit an MSA SM100 JIT cache issue
  (`AttributeError: Module has no function 'plan'`). The failed run cleaned the
  414G partial snapshot at 2026-06-19T07:53:34Z. The MSA JIT cache was then
  cleared and precompiled in a single process (`plan`, `sparse_topk`,
  `reduction`, and FMHA variants `0_0_0_0_1_1_0` through
  `0_0_0_0_1_1_5`), and the TP8 runner was relaunched at
  2026-06-19T08:04:05Z with runner PID `11570`.
- MiniMax-M3 MXFP8 completed on `cirrascale-gpua83e` in container
  `sglang_bbuf_minimax_m3`, using all 8 B200 GPUs and port `30000`. The runner
  produced all 6 workload kernel inventories and deleted the 414G HF snapshot at
  2026-06-19T08:38:17Z. Local verification found row counts `7/8/8/7/8/8` for
  `random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`,
  all with `sglang_relevant=true` and `pct_of_gpu > 2.0`.
- Final local audit after relevant-kernel-only re-extraction: DeepSeek
  `10/7/12/10/12/12`, GLM `9/11/10/9/4/7`, Kimi `13/7/11/2/2/11`, MiniMax
  `7/8/8/7/8/8`; every retained row has sample provenance and
  `pct_of_gpu > 2.0`.

## Status legend
`waiting` -> `downloading` -> `serving` -> `benchmarked` -> `profiled` -> `inventory` -> `tasks` -> `cleaned`
