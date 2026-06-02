import os, importlib.util, torch
rdir=os.environ["RDIR"]
spec=importlib.util.spec_from_file_location("reg", rdir+"/src/register.py")
reg=importlib.util.module_from_spec(spec); spec.loader.exec_module(reg)
shape=(1,512,9,128,40); ng=32; eps=1e-6   # gs=737280 -> large path; 47MB
x=torch.randn(shape,device='cuda',dtype=torch.float16)
C=shape[1]; w=torch.randn(C,device='cuda',dtype=torch.float16); b=torch.randn(C,device='cuda',dtype=torch.float16)
print("==PROF_WARM==")
for _ in range(3): reg.optimized_wrapper(x,w,b,num_groups=ng,eps=eps)
torch.cuda.synchronize()
for _ in range(3): reg.optimized_wrapper(x,w,b,num_groups=ng,eps=eps)
torch.cuda.synchronize()
print("==PROF_DONE==")
