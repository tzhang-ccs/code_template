export OMP_NUM_THREADS=1
export NCCL_P2P_DISABLE=1

torchrun --nproc_per_node=2 1.py
