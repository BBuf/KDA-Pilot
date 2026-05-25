# KernelPilot Prompts

These are end-to-end prompt cards for KernelPilot kernel optimization loops.
They follow the clarity of the
[kernel-design-agents prompt style](https://github.com/mit-han-lab/kernel-design-agents/tree/main/prompts),
but collapse the work into one prompt per task instead of phase-specific
prompts. The FA4 card is seeded from
[KernelPilot issue #1](https://github.com/BBuf/kernel-pilot/issues/1).

| Prompt | Goal |
| --- | --- |
| [B200 int8_scaled_mm](b200-int8-scaled-mm.md) | Optimize SGLang `int8_scaled_mm` on B200 for one focused shape and target at least 2.5x speedup over the SGLang baseline. |
| [B200 FA4 MHA](b200-fa4-mha.md) | Build a standalone BF16 forward-only MHA kernel and beat official FlashAttention-4 by at least 5% geometric-mean TFLOPS across the configured B200 cases. |

Each prompt is intended to be pasted as one complete task. The prompt itself
names the required remote GPU skill and acceptance target.

## Codex Goal Variants

These variants keep the original task targets but express them as Codex
`/goal` completion contracts instead of Humanize kernel agent loop prompts.

| Prompt | Goal |
| --- | --- |
| [B200 int8_scaled_mm Codex Goal](b200-int8-scaled-mm-codex-goal.md) | Optimize SGLang `int8_scaled_mm` on B200 for one focused shape and target at least 2.5x speedup over the SGLang baseline. |
| [B200 FA4 MHA Codex Goal](b200-fa4-mha-codex-goal.md) | Build a standalone BF16 forward-only MHA kernel and beat official FlashAttention-4 by at least 5% geometric-mean TFLOPS across the configured B200 cases. |

## Recommended Claude Code Launch

Start Claude Code with Opus, maximum reasoning effort, and bypassed permission
prompts before pasting one of these end-to-end prompt cards:

```bash
claude --permission-mode bypassPermissions --model opus --effort max
```

## Opus 4.7 B200 int8_scaled_mm Run

The image below is from an Opus 4.7 model run using the
[B200 int8_scaled_mm](b200-int8-scaled-mm.md) prompt.

[![Opus 4.7 B200 int8_scaled_mm optimization result](https://raw.githubusercontent.com/BBuf/kernel-pilot/main/prompts/opus47-b200-int8-scaled-mm-result.png)](https://raw.githubusercontent.com/BBuf/kernel-pilot/main/prompts/opus47-b200-int8-scaled-mm-result.png)
