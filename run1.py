import os

GPU = 0
dataset = 'cifar100'
SEED = [1, 2, 3, 4, 5]
drop_p = '0.5'
wd = '0'
for seed in SEED:
    cmd = 'CUDA_VISIBLE_DEVICES=%d python train_eval_session4.py --seed %d --dataset %s --drop_p %s --drop_last_only --wd %s' % (GPU, seed, dataset, drop_p, wd)
    os.system(cmd)