# 第一轮战役结论(2026-07-09/10,旧任务 01/02,已删除;完整报告在 common/prior_art/)

新任务开工前必读——这些是花了真机时间买来的否定结论与协议,不要重蹈。

## 判死的方向(不要再做)

1. **fp8 小 M dense GEMM 打不过 cuBLAS bf16**(旧 01):CUTLASS SM100 blockwise 赢了
   DeepGEMM(1.128×)但对 cuBLAS bf16 全线 0.70×。M≤6 时 nvjet bf16 splitK 跑
   ~3.7TB/s,所有 fp8 路径(DeepGEMM 含)被 per-128-K-tile 变换串行 + CLC/TMEM 机制
   开销压在 1.6-2.1TB/s——fp8 字节优势在这个 grid 尺寸不可兑现。**bf16-dense 就是
   生产解**(已上线,SGLANG_BS1_BF16_DENSE=1)。
2. **自研 unicast-push allreduce**(旧 02):正确但 36.6µs,~25µs 是协议固定成本
   (world=2 与 8 同速)。想快只有 NVLS multimem(multicast st + 交换机内 ld_reduce)
   ——flashinfer mnnvl kernel 已是该路径(8.3µs),所以新任务 01 是**移植+特化它**,
   不是重造传输。

## 有效的协议(直接复用)

- **cold-L2 基准协议**:回放同权重测出来的是 L2(5-6TB/s)不是 DRAM;权重类 kernel
  轮转 ≥48 份拷贝。(activation 类 KB 级 payload 影响小,但写 harness 时声明口径。)
- **8 卡 AR harness 口径**(common/harness/ar_bench.py):单进程 8 卡 + peer access,
  每卡 50-round CUDA graph 并发 replay,wall/round;spin/flag 类 kernel 的 NCU 必须
  `--replay-mode application`(kernel-replay 会死锁);1000-replay 位级稳定性是
  flag/epoch 竞态的标准暴露手段;图捕获需显式 per-device stream。
- **PDL 陷阱**(旧 01 round5):把 split-K 归约 PDL 链到 producer GEMM 上是无序 RAW
  (CUTLASS 在 input-consumed 就触发)——虚假加速 1.186→诚实 1.128。PDL 只在真依赖
  边界安全。
- **serving e2e 是唯一裁判**:隔离加速 ≥1.3× 且 e2e sanity 不倒退才 promote;
  e2e 口径 = /scratch/glm52_blog_bench/benchmark_glm52_bs1.py(sanity 1×40,官方 3×40)。

## 当前基线(2026-07-10)

- **376.06 tok/s 官方 3×40**(sglang main 87992eeec + 117 行移植 diff,见
  /personal/glm52_backup_20260710/patches_main/main_port_full.diff),accept 3.865。
- 运行时气泡已被 main 消除(>1ms gap = 0);剩余全是 kernel 时间。每迭代预算:
  dense+moe GEMM 7.55ms(cubin,不碰)、moe_aux 1.82、AR 1.40、elementwise 1.13、
  attention 0.94、norm_rope 0.68、quant 0.16(sum 口径,含多流重叠;span ~10.3ms)。
- 到 400 需 −0.62ms/iter → 本轮三任务合计预期 −0.5~−0.9ms。

---

# 第二轮战役结论(2026-07-27/28,GB300 2×4 跨机,R1-R18,基线 374.83→393.40)

完整账本:`Common/opt_model/b300_glm52_bs1_450_goal/LEDGER.md`(18 轮全记录)。
以下为增量判死与协议,与第一轮同等效力。

## GB300 判死的方向(不要再做)

1. **#GB300-1 PDL TGV 在真实 TP8 serving 下不可用**:全表 PDL TGV 两次独立启动都
   `unspecified launch failure`(合成图 357 万次调用无恙——是 2-CTA PDL × serving
   通信并发的交互);窄集 PDL 存活但关键路径 +0.53ms(同步尾)。**TGV 只允许非 PDL**
   (非 PDL 下只有 Q-B/indexer-Q 两个 K=2048 shape 赢,已收割 +6.6 tok/s)。
2. **#GB300-2 隔离 cuBLAS 微基准会说谎**:隔离态 heuristic 选出的 kernel 与 serving
   不同(fp32 对照选了 cutlass SIMT sgemm,虚构 3× 天花板;nvjet 名内 `tss` 实为
   bf16入/fp32出)。归因协议:**grid 指纹法**(每 shape 的 launch grid 唯一,对照表在
   LEDGER R5)+ serving trace 交叉验证,禁止只信隔离数字。
3. **#GB300-3 1-CTA/expert 自研 GEMV 冷态打不过 nvjet splitK**(8.8 vs 7.3µs 含
   reduce,M=6/K=6144/N=256)。dsv3_router_gemm 族在此形状无增量。
4. **#GB300-4 AR kernel 层面无空间**:FlashInfer MNNVL fused AR 在此拓扑就是地板
   (同步 8.7µs,大头是 rank 偏斜,换 kernel 消不掉):generic CustomAllReduceV2 push
   serving 实测 95µs/call(偏斜自旋);K3 特化 multicast push 输 0.3µs;JIT 特化 port
   kernel 赢 0.5µs 但 e2e 零转化。**赚钱的方式是把漏网的 NCCL 调用点接上 FlashInfer
   workspace**(small-AR +1.87%、multimem AG +0.67%),不是重写 AR kernel。
5. **#GB300-5 verbatim-port 的位级一致声明是版本绑定的**:0.6.12 port 对 0.6.15
   stock 翻转 39/40 贪心输出、GSM8K -2.5pt。跨版本 port 一律按 value-affecting 走全
   精度门。
6. **#GB300-6 fan-in 尾块的块级树归约是病灶**:6 token × 8 选择 × ~9 次
   `__syncthreads` ≈ 430 次块同步 = 50µs;warp-shuffle(寄存器驻留 + `__shfl_xor_sync`
   零块同步)= 2-4µs。**巨核内归约一律 warp 级**。
7. **#GB300-7 public routed API 的 fused-router 天花板 0.1ms/iter**:
   trtllm_fp8_block_scale_routed_moe 内部必然再跑 permutation kernel(TopK 模式
   3.5-4.5µs/层);要吃掉 routing 的 6µs/层必须 fork launcher。注意:packed 权重
   需自带 ×routed_scaling(TopK 管线忽略该参数——实测 out=A/2.5 破案)。
8. **#GB300-8 MoE tactic pin / 静态 routing / finalize+AR 融合** 均实测低于线且
   live 不转化(R3 1.04µs/call、R7 0.153ms 预测→live 持平、R8 0.075ms)。

## GB300 有效的协议(直接复用)

- **转化率标定**:暴露关键路径 kernel 节省 → e2e 转化 50-80%(R10 0.386ms kernel →
  −0.19ms span;R16 3.2µs/层 trace → +0.67%);重叠区 ~0-10%。晋级线 0.20-0.24ms/iter。
- **值保持型改动的验收**:官方 3×40 的 120 条 response SHA-256 逐字节对比(R12/R14/R16
  全部 120/120);value-affecting 的分叉若为**逐 prompt 确定性**(每轮同样 task 分叉)
  属数值效应,走 accept 带 + GSM8K 门。
- **等价性 harness 资产**:R15 的 fused-router byte-equivalence harness
  (`benchmark_round15_fused_router.py`)可复用于任何 routed-mode/MoE 链改造——
  A/B 两条完整 MoE 链在真实 gate 权重上比对输出逐字节。
- **相位切片探针**:kernel 异常慢时按编译期开关切成 [GEMM-only / tail-only / full]
  三个模块分别计时定位(R15 用它 15 分钟定位 50µs 病灶)。
- **双流归因**:profiler 的 stream id 每次 capture 会变,跨 trace 不可比;用"角色普查"
  (200+ 层聚合,按 kernel 家族统计所在流与相对锚点时刻)代替单层快照(R18 设计文档
  是范例)。
- **箱上测量纪律**:trace span 有 run-to-run 漂移(10.9-14.4ms),span A/B 只信官方
  3×40 协议;trace 仅用于 liveness/计数/归因。fresh-server 官方跑一次做规范数字
  (累计 accept 会被 8k-token profile probe 污染)。
