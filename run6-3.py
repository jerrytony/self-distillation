import os

GPU = 3
dataset = 'cifar10'
SEED = [1, 2, 3, 4, 5]
t = 9
D = ['0.5', '0.1', '0.02', '0.004']

for seed in SEED:
    for d in D:
        cmd = 'CUDA_VISIBLE_DEVICES=%d python train_eval_session6.py --seed %d --dataset %s --temp %d --distill %s' % (GPU, seed, dataset, t, d)
        os.system(cmd)