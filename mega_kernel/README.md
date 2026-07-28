# mega_kernel — GLM-5.2-FP8 bs=1 解码 kernel 优化战役(2×4 GB300 / sm_103)

目标:GLM-5.2-FP8 在 **2×4 GB300(rx devbox `k3-gsm8k-tp8`,跨机 TP8 over MNNVL)**
上 bs=1 MTP(EAGLE 5-1-6)解码吞吐从当前 **393.40** 推进到 **≥450 tok/s**
(官方口径 = 3 轮 × 40 任务共 120 请求,报 mean decode tok/s)。

当前 serving 侧优化已全部收敛为一个自包含 PR:
**[sgl-project/sglang#32633](https://github.com/sgl-project/sglang/pull/32633)**
(9 commits on main `60d6914f1`:bf16-dense + FP8 defer-finalize + 加载超时 +
small-AR→FlashInfer + 非PDL K2048 TGV + 跨机 multimem AG + alt-stream prequant),
在该分支上 fresh 实测 **393.403 tok/s / accept 3.8623 / GSM8K 0.975**。
前身 PR #30957/#30958/#30959/#32461/#32551/#32614 全部关闭。
serving 侧小 patch 空间已被 18 轮系统排空(账本:
`Common/opt_model/b300_glm52_bs1_450_goal/LEDGER.md`),**剩余缺口 1.23ms/iter
只能靠 kernel 级结构性重写**——即本目录的任务 09。

> 历史:本战役 B300 单机时代(基线 307→381.42,任务 01-04/10-12)已结题归档;
> 任务 01 的 JIT MNNVL AR 特化在 GB300 重测**不成立**(0.6.15 stock kernel 已到
> 7.84µs,残差 ~0.08ms 且 0.6.12/0.6.15 数值差翻转输出,见 LEARNINGS #GB300-4)。
> 旧任务规格已删除;判死结论全部沉淀在 `LEARNINGS.md`。

## 一次 MTP 迭代的 kernel 预算(GB300,393.40 配置,torch profiler 80 步实测)

一次迭代 span ≈ **9.81ms** = draft(5×M=1,~1.3ms)+ verify(M=6 过 78 层)+
draft-extend(M=6 过 1 层)。**decode 步内 NCCL kernel 为零**(172 次 FlashInfer
MNNVL fused AR ~7.8µs/次 + 6 次 multimem AG 6.6µs/次)。

| 类别 | ms/iter | 来源 | 状态 |
|---|---:|---|---|
| dense GEMM bf16(nvjet+splitK;105 次/步已走非PDL TGV) | ~5.1 | cuBLAS 闭源 + CuTe TGV | 可赢子集已收割(R5/6/12) |
| MoE GEMM(gemm1 21.9µs + gemm2 16.5µs ×76)| 3.24 | trtllm-gen **cubin** | **任务 09 主战场** |
| MoE 辅助(routing 6.0 + act 6.8 + finalize 7.3 + quant[已挪 alt 流] ×76)| ~1.5 | flashinfer JIT 源 + sglang | **任务 09 主战场** |
| 融合 AR ×172 + multimem AG ×6 | 1.39 | flashinfer JIT 源 | kernel 层面已到地板(R1/2/11 三杀)|
| attention(DSA,fmha 8.2µs + indexer 链)| ~1.06 | trtllm-gen cubin + JIT 前处理 | indexer 晚-join 0.24ms 设计待施工(见下)|
| norm/rope/quant/elementwise | ~1.0 | flashinfer JIT + aten | 低垂果实已被上游吃掉(R4)|

**选题铁律(18 轮验证)**:暴露关键路径上的 kernel 节省按 **50-80%** 转化 e2e,
重叠区 ~0-10%;晋级线 **0.20-0.24 ms/iter**(低于此不值一次重启验证)。
立项前先用 grid 指纹法(LEARNINGS #GB300-2)对上 serving trace 归因。

## 任务板

| 任务 | 对象 | 现实池 ms/iter | 状态 |
|---|---|---:|---|
| [09](tasks/09/) | **bs=1 MoE 巨核**:routing→gemm1→SiLU→gemm2→finalize(+shared)persistent kernel,替换 trtllm-gen cubin 链 | **~1.2-1.5**(aux 链 + launch 边界;GEMM 本体已近带宽地板,勿以 4.6 立项)| 开放,唯一在册 |

已出规格但未立项的候选(证据齐全,按需恢复):
- **indexer 晚-join**(0.24ms,纯流调度、值保持):设计/普查表/插桩方案齐全 →
  `Common/opt_model/b300_glm52_bs1_450_goal/analysis/round18_design_indexer_latejoin.md`
- **launcher-fork fused router**(~0.45ms):R15 已产出与生产链**逐字节一致**的
  fused router kernel + 等价性 harness(`glm_fused_router.cuh`,#32633 同仓
  `bbuf/glm52-bs1-450` 分支 R15 commits);public routed API 天花板 0.1ms 已实测,
  想拿 routing kernel 的 6µs/层必须 fork trtllm-gen MoE launcher——可并入 09。

(编号 05-08 属于并行的 Kimi-K3 子战役,另见其各自 config,不受本次收编影响。)

一键启动:`tasks/09/launch.sh`(自动建 worktree + Claude Code + RLCR 循环)。

## 铁律

1. **shape 全部来自 bs=1 真实 serving**(T∈{1,6},EAGLE 5-1-6 冻结),开工先在箱上
   实测复核 SHAPES.md(grid 指纹法对 kernel 身份)。
2. serving 接入一律 env 门控、默认关;基线 **393.40** 复现 = PR #32633 分支 +
   `tasks/09/prompt.md` 第 0 条的 env/launch 命令(FUSE 暖加载 ~4 分钟)。
3. promote = 隔离达标 + 关键路径归因证明可转化 + e2e sanity ≥395 + 官方 3×40 +
   accept 3.80-3.90 + GSM8K 200q ≥0.94。
4. **禁 PDL**(TGV 类 kernel 在真实 TP8 serving 下 PDL 要么崩要么拖慢关键路径,
   LEARNINGS #GB300-1);fan-in/归约用 warp-shuffle,不用块级树(#GB300-6)。
5. 箱子与 K3 团队共享:跑前 nvidia-smi 确认 8 卡空闲;绝不动 /scratch/nv_work、
   Kimi-K3 资产;长任务一律箱上 tmux(rx rollout 会踢长 SSH)。

## 环境与资产

- 机器:rx devbox `k3-gsm8k-tp8`(2 rank × 4 GB300,常驻;`ssh k3-gsm8k-tp8-rank{0,1}`,
  管理面用 rxp 包装)。**B300 单机池已不存在,勿再申请。**
- 权重:`/cluster-storage/models/GLM-5.2-FP8`(共享 FUSE,141 shards,勿拷 /scratch)。
- 评测:箱上 `/scratch/users/bbuf/glm52/`(benchmark_glm52_bs1.py、run_official_baseline.sh、
  run_gsm8k_baseline.sh、profile_steady_decode.sh);跨机 8 卡微基准 harness 参照
  `scripts/probe_multimem_ag_crossnode.py` / `benchmark_round15_fused_router.py`
  (`Common/opt_model/b300_glm52_bs1_450_goal/scripts/`)。
- `LEARNINGS.md`:B300 + GB300 两代判死方向与基准协议,**开工必读**。
