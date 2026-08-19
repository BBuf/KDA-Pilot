"""Identity candidate: calls the copied baseline.

Not a real solution - it exists to prove the A/B path end to end: the harness should
report ~1.00x on every row and every gate should pass. Delete it when a real kernel
lands here.
"""

import importlib.util, os, sys

B = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "baseline", "entry.py")
_spec = importlib.util.spec_from_file_location("identity_baseline_nemotron3_nano__mamba2_ssm", B)
_m = importlib.util.module_from_spec(_spec); sys.modules[_spec.name] = _m; _spec.loader.exec_module(_m)

OPS = dict(_m.OPS)
RECONSTRUCT = dict(getattr(_m, "RECONSTRUCT", {}) or {})
