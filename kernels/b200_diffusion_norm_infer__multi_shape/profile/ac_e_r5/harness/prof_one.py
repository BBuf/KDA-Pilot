import importlib.util, os, torch
spec = importlib.util.spec_from_file_location("reg", "src/register.py"); reg = importlib.util.module_from_spec(spec); spec.loader.exec_module(reg)
b = os.environ["KDA_PROF"]; torch.manual_seed(0)
# Call the CUDA kernels DIRECTLY (bypass the allowlist) so a reduced-but-saturating
# shape still exercises the CUDA kernel (not the baseline fallback). Rates are
# row-count-independent once saturated; full-shape latency (benchmark) gives BW.
if b == "ln":  # wide-LN: 4096 rows x N=5120 (~84MB) saturates SMs, same float4 LN kernel
    x = torch.randn(4096, 5120, device="cuda", dtype=torch.float32)
    w = torch.randn(5120, device="cuda", dtype=torch.float32); bi = torch.randn(5120, device="cuda", dtype=torch.float32); out = torch.empty_like(x)
    m = reg._ln_module(torch.float32); fn = lambda: m.norm_infer_ln(x, w, bi, out, 1e-6)
elif b == "rmsbig":  # large-S kernel (kUnroll=4) at reduced S=65536
    x = torch.randn(65536, 128, device="cuda", dtype=torch.bfloat16); w = torch.randn(128, device="cuda", dtype=torch.bfloat16); out = torch.empty_like(x)
    m = reg._rms_module(128, 4, torch.bfloat16); fn = lambda: m.rms_onepass(x, w, out, 1e-6)
else:  # small/mid RMS production shapes (KDA_PROF in {rms1320, rms4096, rms16384}),
    # profiled at FULL production shape (≤8MB) via the allowlisted dispatcher -> CUDA.
    assert b.startswith("rms"), f"unknown KDA_PROF={b!r}"
    S = int(b[3:]); x = torch.randn(S, 128, device="cuda", dtype=torch.bfloat16); w = torch.randn(128, device="cuda", dtype=torch.bfloat16)
    assert (S, 128) in reg._SUPPORTED_RMS, f"S={S} not in CUDA allowlist -> would profile baseline"
    fn = lambda: reg.optimized_triton_one_pass_rms_norm(x, w, 1e-6)
fn(); torch.cuda.synchronize(); fn(); torch.cuda.synchronize(); print("done", b)
