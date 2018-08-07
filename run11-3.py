import os

GPU = 3
dataset = 'cifar10'
FD = [2048, 4096]
SEED = [1, 2, 3, 4, 5]

for seed in SEED:
    for feat_dim in FD:
        cmd = 'CUDA_VISIBLE_DEVICES=%d python train_eval_session8.py --seed %d --dataset %s --feat_dim %d' % (GPU, seed, dataset, feat_dim)
        os.system(cmd)