import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
import sglang.jit_kernel.diffusion.qknorm_rope as m
print("baseline module:", m.__file__)
import flashinfer.rope as fr
print("flashinfer rope ok")
import wrapper
print("task wrapper ok")
import torch
print("torch", torch.__version__, "cuda_avail", torch.cuda.is_available())
