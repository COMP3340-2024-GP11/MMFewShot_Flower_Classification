"""Flower class."""
import os
import os.path as osp
from typing import List, Optional, Sequence, Union

import mmcv
import numpy as np
from mmcls.datasets.builder import DATASETS
from typing_extensions import Literal

from .base import BaseFewShotDataset

ALL_CLASSES = [int(cls) for cls in range(17)]

ALL_CLASSES_NAME = [
    'daffodil', 'snowdrop', 'lilyValley', 'bluebell', 'crocys', 'iris', 
    'tigerlily', 'tulip', 'fritillary', 'sunflower', 'daisy', 'colts foot', 
    'dandelion', 'cowslip', 'buttercup', 'wind flower', 'pansy'
]

# Class split: first 7 as train, 8-12 as val, 13-17 as test
TRAIN_CLASSES, VAL_CLASSES, TEST_CLASSES = ALL_CLASSES[:7], ALL_CLASSES[7:12], ALL_CLASSES[12:]
TRAIN_CLASSES_NAME, VAL_CLASSES_NAME, TEST_CLASSES_NAME = ALL_CLASSES_NAME[:7], ALL_CLASSES_NAME[7:12], ALL_CLASSES_NAME[12:]
 
@DATASETS.register_module()
class FlowerDataset(BaseFewShotDataset):
    """Oxford 17 flower dataset for few shot classification.

        Args:
        classes_id_seed (int | None): A random seed to shuffle order
            of classes. If seed is None, the classes will be arranged in
            alphabetical order. Default: None.
        subset (str| list[str]): The classes of whole dataset are split into
            three disjoint subset: train, val and test. If subset is a string,
            only one subset data will be loaded. If subset is a list of
            string, then all data of subset in list will be loaded.
            Options: ['train', 'val', 'test']. Default: 'train'.
    """

    # resource = 'https://www.robots.ox.ac.uk/~vgg/data/flowers/17/17flowers.tgz'
    TRAIN_CLASSES = TRAIN_CLASSES
    VAL_CLASSES = VAL_CLASSES
    TEST_CLASSES = TEST_CLASSES

    def __init__(self,
                 classes_id_seed: int = None,
                 subset: Literal['train', 'test', 'val'] = 'train',
                 *args,
                 **kwargs) -> None:
        self.classes_id_seed = classes_id_seed

        if isinstance(subset, str):
            subset = [subset]
        for subset_ in subset:
            assert subset_ in ['train', 'test', 'val']
        self.subset = subset
        super().__init__(*args, **kwargs)

    def get_classes(
            self,
            classes: Optional[Union[Sequence[str],
                                    str]] = None) -> Sequence[str]:
        """Get class names of current dataset.

        Args:
            classes (Sequence[str] | str | None): Three types of input
                will correspond to different processing logics:

                - If `classes` is a tuple or list, it will override the
                  CLASSES predefined in the dataset.
                - If `classes` is None, we directly use pre-defined CLASSES
                  will be used by the dataset.
                - If `classes` is a string, it is the path of a classes file
                  that contains the name of all classes. Each line of the file
                  contains a single class name.

        Returns:
            tuple[str] or list[str]: Names of categories of the dataset.
        """
        if classes is None:
            class_names = []
            for subset_ in self.subset:
                if subset_ == 'train':
                    class_names += TRAIN_CLASSES
                elif subset_ == 'val':
                    class_names += VAL_CLASSES
                elif subset_ == 'test':
                    class_names += TEST_CLASSES
                else:
                    raise ValueError(f'invalid subset {subset_} only '
                                     f'support train, val or test.')
        elif isinstance(classes, str):
            # take it as a file path
            class_names = mmcv.list_from_file(classes)
        elif isinstance(classes, (tuple, list)):
            class_names = classes
        else:
            raise ValueError(f'Unsupported type {type(classes)} of classes.')
        return class_names

    def load_annotations(self) -> List:
        """Load annotation according to the classes subset."""
        data_infos = []
        for subset_ in self.subset:
            ann_file = osp.join(self.data_prefix, f'meta/{subset_}.txt')
            assert osp.exists(ann_file), \
                f'Please download ann_file through {self.resource}.'
            with open(ann_file) as f:
                for i, line in enumerate(f):
                    filename, class_name = line.strip().split(' ')
                    gt_label = int(class_name)
                    info = {
                        'img_prefix':self.data_prefix,
                        'img_info': {
                            'filename': filename
                        },
                        'gt_label': np.array(gt_label, dtype=np.int64)
                    }
                    data_infos.append(info)
        return data_infos