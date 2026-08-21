SLUG=dsv4_flash
MODEL=deepseek-ai/DeepSeek-V4-Flash
SERVER_ARGS="--tp 4 --trust-remote-code --mem-fraction-static 0.85"
TARGETS=merged_dsa.json
PORT=30014
GPUS=4,5,6,7
export HF_HUB_CACHE=/cluster-storage/models
export HF_HUB_OFFLINE=1
