# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
# Copyright (C) Alibaba Group Holding Limited. All rights reserved.
"""Centralized catalog of paths."""
import os


class DatasetCatalog(object):
    DATA_DIR = 'datasets'
    DATASETS = {
        'coco_2017_train': {
            'img_dir': 'coco/train2017',
            'ann_file': 'coco/annotations/instances_train2017.json'
        },
        'coco_2017_val': {
            'img_dir': 'coco/val2017',
            'ann_file': 'coco/annotations/instances_val2017.json'
        },
        'coco_2017_test_dev': {
            'img_dir': 'coco/test2017',
            'ann_file': 'coco/annotations/image_info_test-dev2017.json'
        },
        'sample_train_coco': {
            'img_dir': '/home/tfw/yolo/damo-yolo/datasets/Train_diff_shadow',
            'ann_file': '/home/tfw/yolo/damo-yolo/datasets/cocozzz/val2.json'
        },
        'sample_test_coco': {
            'img_dir': '/home/tfw/yolo/damo-yolo/datasets/Train_diff_shadow',
            'ann_file': '/home/tfw/yolo/damo-yolo/datasets/cocozzz/val2.json'
        },
        'coco_train_cross_hair': {
            'img_dir': '/home/tfw/yolo/damo-yolo/datasets/new_cross_hair/cross_hair_train',
            'ann_file': '/home/tfw/yolo/damo-yolo/datasets/new_cross_hair/coco/cross_hair_train.json'
        },
        'coco_val_cross_hair': {
            'img_dir': '/home/tfw/yolo/damo-yolo/datasets/new_cross_hair/cross_hair_val',
            'ann_file': '/home/tfw/yolo/damo-yolo/datasets/new_cross_hair/coco/cross_hair_val.json'
        },
        'coco_ch_train': {
            'img_dir': '/home/tfw/yolo/damo-yolo/datasets/cross_hair/cross_hair_train',
            'ann_file': '/home/tfw/yolo/damo-yolo/datasets/cross_hair/coco/cross_hair_train.json'
        },
        'coco_ch_val': {
            'img_dir': '/home/tfw/yolo/damo-yolo/datasets/cross_hair/cross_hair_val',
            'ann_file': '/home/tfw/yolo/damo-yolo/datasets/cross_hair/coco/cross_hair_val.json'
        },
        'coco_guns_train': {
            'img_dir': '/home/tfw/yolo/damo-yolo/datasets/cross_hair/guns_train',
            'ann_file': '/home/tfw/yolo/damo-yolo/datasets/cross_hair/coco/guns_train.json'
        },
        'coco_guns_val': {
            'img_dir': '/home/tfw/yolo/damo-yolo/datasets/cross_hair/guns_val',
            'ann_file': '/home/tfw/yolo/damo-yolo/datasets/cross_hair/coco/guns_val.json'
        },
        }

    @staticmethod
    def get(name):
        if 'coco' in name:
            data_dir = DatasetCatalog.DATA_DIR
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                root=os.path.join(data_dir, attrs['img_dir']),
                ann_file=os.path.join(data_dir, attrs['ann_file']),
            )
            return dict(
                factory='COCODataset',
                args=args,
            )
        else:
            raise RuntimeError('Only support coco format now!')
        return None
