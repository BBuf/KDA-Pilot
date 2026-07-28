# Prompt

```
你是 NVIDIA Blackwell/GB300(sm_103)MoE kernel 专家。任务:为 GLM-5.2-FP8 bs=1 写
per-layer 的 MoE persistent 巨核——routing→gemm1→SiLU·mul→gemm2→top8 加权 finalize
(+shared add)一个 kernel 完成,替换 flashinfer trtllm-gen cubin 链。

GB300 serving 实测(393.40 配置,trace 逐 kernel):每层 T=6 链条 =
routing 6.0µs + gemm1 21.9µs + act 6.8µs + gemm2 16.5µs + finalize 7.3µs ≈ 58µs,
×76 层/迭代。注意:**GEMM 本体已近带宽地板**(top-8 唯一专家权重读量核算过,
trtllm-gen ~82% BW-eff;R7 tactic 扫描 48 组合仅 2µs 空间且 live 不转化)——
巨核的钱在 **aux 链(routing/act/finalize ≈20µs/层)+ 5-7 次 launch 边界 +
gemm1→act→gemm2 的 global 往返**。目标 ≤42µs/层,现实预期 e2e −1.2~−1.5 ms/iter
(393.40 → ~415+;不要按旧口径 4.6ms 池立项)。
正确性口径 = fp32 oracle rel≤2e-2 + e2e 质量门(非位级,归约结构必然不同)。

**NEVER STOP**:持续实现、验证、benchmark、profile、优化,不要问我。

第 0 条——环境(GB300,与 B300 时代完全不同,照此执行):
- 机器 = rx devbox `k3-gsm8k-tp8`(2 rank × 4 GB300,常驻,与 Kimi-K3 团队共享)。
  本机 ssh 别名 `k3-gsm8k-tp8-rank0/1`;管理面 `rxp devbox status k3-gsm8k-tp8`。
  跑前两 rank `nvidia-smi` 确认 8 卡空闲;长任务(server/bench/编译)一律箱上 tmux。
  两 rank 的 /scratch 独立,文件经本机中转;绝不动 /scratch/nv_work 与 K3 资产。
- serving 基线 = **sgl-project/sglang PR #32633 分支**(自包含,9 commits on main),
  箱上现成 checkout:/scratch/users/bbuf/glm52/sglang(分支 pr-opt-stack)。
  启动:两 rank 各 `/scratch/users/bbuf/glm52/scripts/launch_round16.sh {0|1}`
  (rank1 先;含全部 9 个 env;--dist-init-addr 172.23.0.19:5000;
  NCCL_MNNVL_ENABLE=1 NCCL_CUMEM_ENABLE=1 必须)。FUSE 暖加载 ~4 分钟。
  基线吞吐 **393.40 官方 3×40**,accept 3.8623,GSM8K 0.975。
- 评测:/scratch/users/bbuf/glm52/{run_official_baseline.sh,run_gsm8k_baseline.sh,
  scripts/run_round5_equality.sh(1×40 byte 对比),profile_steady_decode.sh(bounded
  60-100 步,严禁 unbounded)}。
- workdir=/scratch/users/bbuf/kda_bs1/mega09(两 rank 各建);kernel 开发 1 卡,
  e2e 8 卡。sm_103a,CUDA 13.0,torch 2.11,flashinfer 0.6.15(/scratch/users/bbuf/
  pylibs_fi615 PYTHONPATH 前置)。

先读(每条都是机时买的):
- ../../README.md(GB300 预算表 + 转化率标定 + 晋级线 0.20-0.24ms)
- ../../LEARNINGS.md 全部,重点 #GB300-1(禁 PDL)、#GB300-2(grid 指纹归因)、
  #GB300-6(归约用 warp-shuffle,块级树 = 50µs 病灶)、#GB300-7(routed API 语义:
  packed 权重自带 ×2.5;fork launcher 才能吃 routing)、#GB300-8(tactic/静态路由死)
- SHAPES.md(GB300 实测链条与字节账)
- 现成资产:R15 fused-router kernel(与生产链**逐字节一致**,含 routing+top8+pack,
  可直接作为巨核 P0 的 routing 段)+ byte-equivalence harness:
  sglang 仓 bbuf/glm52-bs1-450 分支 kernels/jit/csrc/gemm/glm_fused_router.cuh、
  Common/opt_model/b300_glm52_bs1_450_goal/scripts/benchmark_round15_fused_router.py

设计要点(参考,不设限):
- persistent 单 kernel:CTA 常驻,内部阶段化(routing 段可直接用 R15 kernel 的
  GEMM+warp-shuffle top8 → 各 CTA 认领 (expert,tile) → gemm1+SiLU 写 smem/寄存器 →
  gemm2 → warp 级加权归约 finalize + shared add)。fan-in 一律 warp-shuffle。
- fp8 128×128 block 反量化在 tile 内做;权重流 TMA/LDG.128;T=6 激活常驻寄存器。
- **全程禁 PDL**(#GB300-1);跨 CTA 依赖用 atomic-counter fan-in(R15 已验证
  graph-replay 自复位写法)。
- 参考 TileRT 形态:occupancy=1、高寄存器、piped prefetch(TileRT_讨论材料 + MiniTileRT)。
- CUTLASS SM100 blockwise GEMM 可作 gemm 段起点(对 DeepGEMM 1.128×;MoE fp8 无
  bf16 对手,第一轮 fp8-dense 判死结论不适用于 MoE)。
- 分阶段落地:P0 routing 段(R15 现成)+ gemm1+act 段 + gemm2+finalize 段(3 launch,
  每段 oracle 对齐 + cold-L2 计时);P1 再合成单 kernel。每步跑 e2e 质量门。
- CUDA graph 可捕获;spin/barrier 类 NCU 用 --replay-mode application。

门槛:隔离(cold-L2,≥48 份权重轮转)T=6 ≤42µs/层 且 T=1 不劣化;fp32 oracle
rel≤2e-2;接入 serving(env SGLANG_JIT_MOE_MEGA=1 默认关,moe_runner 分发,
非覆盖形态 fallback)后 sanity 1×40 ≥395 且 accept 3.80-3.90 → 官方 3×40 +
GSM8K 200q ≥0.94 记录。

交付物:kernels JIT 模块(注意:新 namespace 是 python/sglang/kernels/,
jit_kernel/ 已删)、serving 接入 patch(默认关)、RESULTS_SM103.md(分段与单核对比
+ NCU 证据 + e2e)、失败路线记录。
```
