_base_ = [
    '../../_base_/meta_test/flower_meta-test_5way-1shot.py',
    '../../_base_/runtime/iter_based_runtime.py',
    '../../_base_/schedules/adam_100k_iter.py'
]

img_size = 84
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='RandomResizedCrop', size=img_size),
    dict(type='RandomFlip', flip_prob=0.5, direction='horizontal'),
    dict(type='ColorJitter', brightness=0.4, contrast=0.4, saturation=0.4),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='ToTensor', keys=['gt_label']),
    dict(type='Collect', keys=['img', 'gt_label'])
]

data = dict(
    samples_per_gpu=1,
    workers_per_gpu=8,
    train=dict(
        type='EpisodicDataset',
        num_episodes=100000,
        num_ways=5,
        num_shots=1,
        num_queries=16, # as we have in total 60 images in training set
        dataset=dict(
            type='FlowerDataset',
            data_prefix='data/flowers',
            subset='train',
            pipeline=train_pipeline)),
    test=dict(meta_test_cfg=dict(fast_test=True)))

model = dict(
    type='ProtoNet',
    backbone=dict(type='Conv4'),
    head=dict(type='PrototypeHead'))
