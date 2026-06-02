"""NCU profile entrypoint for the SGLang fused-qknorm-rope baseline kernel.

Run from the kernel folder (PYTHONPATH=.):
  python profile/baseline_b200/harness/profile_entry.py <case_name>

Warms up (JIT compile + warm cache), then issues one final launch. Profile with:
  ncu --set full -k regex:qknorm -s 5 -c 1 -o reports/<name> python ... <case_name>
so ncu skips the 5 warmup launches and captures the 6th (steady-state).
"""

import os
import sys
from pathlib import Path

import torch

ROOT = Path(__file__).resolve().parents[3]  # kernel folder
sys.path.insert(0, str(ROOT))

from tests.test_correctness import _make_inputs, make_cases  # noqa: E402

from sglang.jit_kernel.diffusion.qknorm_rope import fused_inplace_qknorm_rope  # noqa: E402

# KDA_PROFILE_TARGET=baseline (default) profiles the SGLang baseline kernel;
# =candidate profiles src/register.py optimized_wrapper (honor KDA_CAND_VARIANT).
_TARGET = os.environ.get("KDA_PROFILE_TARGET", "baseline")
if _TARGET == "candidate":
    import importlib.util

    _spec = importlib.util.spec_from_file_location("kda_reg", ROOT / "src" / "register.py")
    _reg = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_reg)


def main() -> int:
    name = sys.argv[1]
    case = {c["name"]: c for c in make_cases()}[name]
    inp = _make_inputs(case)

    def call() -> None:
        fn = _reg.optimized_wrapper if _TARGET == "candidate" else fused_inplace_qknorm_rope
        fn(
            inp["q"], inp["k"], inp["q_weight"], inp["k_weight"],
            inp["cos_sin_cache"], inp["positions"],
            is_neox=case["is_neox"], eps=case["eps"],
            head_dim=case["head_dim"], rope_dim=case["rope_dim"],
        )

    for _ in range(5):  # warmup: JIT compile + warm cache (ncu skips these)
        call()
    torch.cuda.synchronize()
    call()  # profiled launch
    torch.cuda.synchronize()
    print(f"profiled {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
