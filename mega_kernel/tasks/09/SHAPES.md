# 真实 shape(bs=1 serving,冻结口径;开工先在箱上实测复核)

模型:GLM-5.2-FP8,hidden 6144,n_routed_experts 256(TP8 → 每 rank local 32,
local_expert_offset=rank*32),top-8,sigmoid noaux-tc(e_score_correction_bias 参与
选择不参与权重),norm_topk_prob=True,routed_scaling_factor=2.5,n_shared=1,
moe_intermediate 2048(TP8 → 每 rank 256),fp8 128×128 block 量化,激活 bf16。

| 站点 | T | 说明 |
|---|---:|---|
| verify 图(76 个 MoE 链/迭代,含 draft-extend) | 6 | 主战场;routing_logits [6,256],hidden [6,6144] |
| draft/extend(1 层 MTP) | 1 / 6 | 同构小流量 |

链条(当前 5-7 个 kernel,目标 1 个):
routing [T,256]→top8 ids/weights → gemm1: 选中专家 w13 [2×256,6144]fp8 × x_q [T,6144]fp8
→ SiLU-mul [T,256] → gemm2: w2 [6144,256]fp8 → finalize: top-8 加权和 + shared expert
输出加法([T,6144] bf16 输出)。注意 defer-finalize 语义(shared 已在 finalize 融合)。
每层权重字节(local 32 专家)≈ 32×(2×256×6144 + 6144×256)×1B ≈ 151MB;T=6 时
top-8 跨 6 token 唯一激活专家最多 48 个 slot,实际读 ~38MB。GB300 实测(393.40 配置
trace):gemm1 21.9µs + gemm2 16.5µs = 38.4µs ≈ 带宽账相符(trtllm-gen ~82% BW-eff),
**GEMM 本体余量很小**;aux 链 routing 6.0 + act 6.8 + finalize 7.3 ≈ 20µs/层 +
5-7 次 launch 边界才是巨核的主要收益来源(quant 3.0µs 已在 serving 侧挪 alt 流,
不在本链)。

复核:profile 60-100 步(bounded),按 grid 指纹统计链条各环节 n/iter×µs(对照表在
战役 LEDGER R5);从 moe_runner 调用点 dump 一次真实 routing_logits/bias/scale。
routed packed 格式注意:(id<<16)|bf16(weight),权重需自带 ×2.5(LEARNINGS #GB300-7)。
