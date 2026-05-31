"""Generate per-task launcher shell scripts in scripts/launch_kernels/.

Naming follows the existing pattern `kNN_<task-slug>.sh`. The launcher delegates to
`scripts/launch_kda_kernel_task.sh` with the task folder relative path.
"""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
LAUNCH_DIR = REPO_ROOT / "scripts" / "launch_kernels"

# Preserve existing launcher numbers. k05/k06 were retired after their task
# family was removed for having no captured production shapes.
TASKS = [
    # (launcher index, kernel-folder-name)
    (3, "b200_diffusion_qknorm_rope__multi_shape"),
    (4, "h200_diffusion_qknorm_rope__multi_shape"),
    (7, "b200_diffusion_norm_infer__multi_shape"),
    (8, "h200_diffusion_norm_infer__multi_shape"),
    (9, "b200_diffusion_group_norm_silu__multi_shape"),
    (10, "h200_diffusion_group_norm_silu__multi_shape"),
    (11, "b200_diffusion_rotary_embedding__multi_shape"),
    (12, "h200_diffusion_rotary_embedding__multi_shape"),
    (13, "b200_diffusion_fuse_scale_shift__multi_shape"),
    (14, "h200_diffusion_fuse_scale_shift__multi_shape"),
    (15, "b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape"),
    (16, "h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape"),
    (17, "b200_diffusion_cutedsl_norm_scale_shift__multi_shape"),
    (18, "h200_diffusion_cutedsl_norm_scale_shift__multi_shape"),
]

LAUNCHER_TEMPLATE = """\
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${{BASH_SOURCE[0]}}")" && pwd)"
KDA_LAUNCHER_NAME="${{KDA_LAUNCHER_NAME:-$(basename "$0")}}"
export KDA_LAUNCHER_NAME
exec "$SCRIPT_DIR/../launch_kda_kernel_task.sh" "kernels/{task}" "$@"
"""


def main() -> None:
    LAUNCH_DIR.mkdir(parents=True, exist_ok=True)
    for index, task in TASKS:
        path = LAUNCH_DIR / f"k{index:02d}_{task}.sh"
        path.write_text(LAUNCHER_TEMPLATE.format(task=task))
        path.chmod(0o755)
        print(path.relative_to(REPO_ROOT))


if __name__ == "__main__":
    main()
