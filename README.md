# COMP3340 Group 10 - Few Shot Learning

## Contact
- This repository contains code for Few Shot Learning on Oxford 17 Dataset
- For any question and enquiry, please feel free to reach out to Jiayi Xin (xinjiayi@connect.hku.hk)
- Thanks and enjoy =P

## Overview
**Prerequisite for Reproduction**
1. [Set up conda environment](#env_setup)
2. [Download data and checkpoint files and put them under the correct folder](#downloads)
3. [Run the commands to reproduce all the important results](#cmd_repro)

**Software, Hardware & System Requirements**
- Software
  - Set up environment as [following](#env_setup)
  - python==3.8.18
  - mmfewshot==0.1.0
  - mmdet==2.17.0
  - mmcv==1.3.14
- Hardware
  - Experiments are conducted on one NVIDIA GeForce RTX 2080 Ti
- System
  - Linux

**Note**
One model training typically takes 6-7 hours to run with one NVIDIA GeForce RTX 2080 Ti.

## Environment setup <a id="env_setup"/>

### Basic Setup (Also required by some other Group 10 repos)

**Step 1. Create virtual environment using anaconda**

```
conda create -n open-mmlab python=3.8 -y
conda activate open-mmlab
```

*Please make sure that you are create a virtual env with python version 3.8*

**Step 2 Install Pytorch from wheel**

```
wget https://download.pytorch.org/whl/cu110/torch-1.7.1%2Bcu110-cp38-cp38-linux_x86_64.whl#sha256=709cec07bb34735bcf49ad1d631e4d90d29fa56fe23ac9768089c854367a1ac9
pip install torch-1.7.1+cu110-cp38-cp38-linux_x86_64.whl
```

*Please double check that you install the correct version of pytorch using the following command*

![Output if correct pytorch version is installed](./check_torch.png)

**Step 3 Install cudatoolkit via conda-forge channel**

*You must be on the GPU compute node to install cudatoolkit and mmcv since GCC compiler and CUDA drivers only available on GPU computing nodes*

```
gpu-interactive
conda activate open-mmlab
conda install -c conda-forge cudatoolkit=11.0
```

**Step 4 Install torchvision, mmcv-full and mmcls package using pip**

*Make sure you are on GPU compute node!!*

- `gpu-interactive`

*Make sure you did not previously installed any relevant package*
*Following pip show command show output a message like "no such package found"*

```
pip show torchvision
pip show mmcv
pip show mmcv-full
pip show mmcls
```

*remove pip cache*

```
pip cache remove torchvision
pip cache remove mmcv
pip cache remove mmcv-full
pip cache remove mmcls
```

*install packages*

```
pip install torchvision==0.8.2
pip install mmcv-full==1.3.14 -f https://download.openmmlab.com/mmcv/dist/cu110/torch1.7.0/index.html
```


### MMFewShot Additional Setup

- **Install MMDetection**
  - [GitHub - open-mmlab/mmdetection: OpenMMLab Detection Toolbox and Benchmark](https://github.com/open-mmlab/mmdetection)
  - *Please install mmdet==2.17.0*
  - Need to be compatible with current mmcv versoin --> go to the realease page of mmdetection and download the zip of the code of tha version
  - [Releases · open-mmlab/mmdetection (github.com)](https://github.com/open-mmlab/mmdetection/releases?page=4)
- **Install MMFewshot**
  - *Please install mmdet==2.17.0 before installing mmfewshot*
  - *Please install mmfewshot==0.1.0*
  - [mmfewshot/docs/en/install.md at main · open-mmlab/mmfewshot (github.com)](https://github.com/open-mmlab/mmfewshot/blob/main/docs/en/install.md)

## Download data & checkpoints<a id="downloads"/>

[OneDrive Download Link](https://hku.hk)

## Commands to reproduce results<a id="cmd_repro"/>

### Train model command

Reproduce midterm report Section XX

```
python ./tools/classification/train.py \
./configs/classification/maml/flower/maml_conv4_1xb105_flower_5way-1shot.py \
--work-dir ./output/maml_conv4_1xb105_flower_5way-1shot_meta-test
```

To be continued...


---  

<div align="center">
  <img src="resources/mmfewshot-logo.png" width="500"/>
  <div>&nbsp;</div>
  <div align="center">
    <b><font size="5">OpenMMLab website</font></b>
    <sup>
      <a href="https://openmmlab.com">
        <i><font size="4">HOT</font></i>
      </a>
    </sup>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <b><font size="5">OpenMMLab platform</font></b>
    <sup>
      <a href="https://platform.openmmlab.com">
        <i><font size="4">TRY IT OUT</font></i>
      </a>
    </sup>
  </div>
  <div>&nbsp;</div>
</div>

<div align="center">
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mmfewshot)](https://pypi.org/project/mmfewshot/)
[![PyPI](https://img.shields.io/pypi/v/mmfewshot)](https://pypi.org/project/mmfewshot)
[![docs](https://img.shields.io/badge/docs-latest-blue)](https://mmfewshot.readthedocs.io/en/latest/)
[![badge](https://github.com/open-mmlab/mmfewshot/workflows/build/badge.svg)](https://github.com/open-mmlab/mmfewshot/actions)
[![codecov](https://codecov.io/gh/open-mmlab/mmfewshot/branch/master/graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmfewshot)
[![license](https://img.shields.io/github/license/open-mmlab/mmfewshot.svg)](https://github.com/open-mmlab/mmfewshot/blob/master/LICENSE)

[📘Documentation](https://mmfewshot.readthedocs.io/) |
[🛠️Installation](https://mmfewshot.readthedocs.io/en/latest/install.html) |
[👀Model Zoo](https://mmfewshot.readthedocs.io/en/latest/model_zoo.html) |
[🆕Update News](https://mmfewshot.readthedocs.io/en/latest/changelog.html) |
[🤔Reporting Issues](https://github.com/open-mmlab/mmfewshot/issues/new/choose)

</div>

<div align="center">

English | [简体中文](README_zh-CN.md)

</div>

## Introduction

mmfewshot is an open source few shot learning toolbox based on PyTorch. It is a part of the [OpenMMLab](https://open-mmlab.github.io/) project.

The master branch works with **PyTorch 1.5+**.
The compatibility to earlier versions of PyTorch is not fully tested.

<div align="left">
  <img src="resources/demo.png"/>
</div>

### Major features

- **Support multiple tasks in Few Shot Learning**

  MMFewShot provides unified implementation and evaluation of few shot classification and detection.

- **Modular Design**

  We decompose the few shot learning framework into different components,
  which makes it much easy and flexible to build a new model by combining different modules.

- **Strong baseline and State of the art**

  The toolbox provides strong baselines and state-of-the-art methods in few shot classification and detection.

## What's New

v0.1.0 was released in 24/11/2021.
Please refer to [changelog.md](docs/en/changelog.md) for details and release history.

## Installation & Dataset Preparation

MMFewShot depends on [PyTorch](https://pytorch.org/) and [MMCV](https://github.com/open-mmlab/mmcv).
Please refer to [install.md](/docs/en/install.md) for installation of MMFewShot and [data preparation](tools/data/README.md) for dataset preparation.

## Getting Started

If you are new of few shot learning, you can start with [learn the basics](docs/en/intro.md).
If you are familiar with it, check out [getting_started.md](docs/en/get_started.md) for the basic usage of mmfewshot.

Refer to the below tutorials to dive deeper:

- Few Shot Classification

  - [Overview](docs/en/classification/overview.md)
  - [Config](docs/en/classification/customize_config.md)
  - [Customize Dataset](docs/en/classification/customize_dataset.md)
  - [Customize Model](docs/en/classification/customize_models.md)
  - [Customize Runtime](docs/en/classification/customize_runtime.md)

- Few Shot Detection

  - [Overview](docs/en/detection/overview.md)
  - [Config](docs/en/detection/customize_config.md)
  - [Customize Dataset](docs/en/detection/customize_dataset.md)
  - [Customize Model](docs/en/detection/customize_models.md)
  - [Customize Runtime](docs/en/detection/customize_runtime.md)

## Benchmark and model zoo

Results and models are available in the [model zoo](docs/en/model_zoo.md).
Supported algorithms:

<details open>
<summary>Classification</summary>

- [x] [Baseline](configs/classification/baseline/README.md) (ICLR'2019)
- [x] [Baseline++](configs/classification/baseline_plus/README.md) (ICLR'2019)
- [x] [NegMargin](configs/classification/neg_margin/README.md) (ECCV'2020)
- [x] [MatchingNet](configs/classification/matching_net/README.md) (NeurIPS'2016)
- [x] [ProtoNet](configs/classification/proto_net/README.md) (NeurIPS'2017)
- [x] [RelationNet](configs/classification/relation_net/README.md) (CVPR'2018)
- [x] [MetaBaseline](configs/classification/meta_baseline/README.md) (ICCV'2021)
- [x] [MAML](configs/classification/maml/README.md) (ICML'2017)

</details>

<details open>
<summary>Detection</summary>

- [x] [TFA](configs/detection/tfa/README.md) (ICML'2020)
- [x] [FSCE](configs/detection/fsce/README.md) (CVPR'2021)
- [x] [AttentionRPN](configs/detection/attention_rpn/README.md) (CVPR'2020)
- [x] [MetaRCNN](configs/detection/meta_rcnn/README.md) (ICCV'2019)
- [x] [FSDetView](configs/detection/fsdetview/README.md) (ECCV'2020)
- [x] [MPSR](configs/detection/mpsr/README.md) (ECCV'2020)

</details>

## Contributing

We appreciate all contributions to improve mmfewshot. Please refer to [CONTRIBUTING.md](https://github.com/open-mmlab/mmfewshot/blob/main/.github/CONTRIBUTING.md) in MMFewShot for the contributing guideline.

## Acknowledgement

mmfewshot is an open source project that is contributed by researchers and engineers from various colleges and companies. We appreciate all the contributors who implement their methods or add new features, as well as users who give valuable feedbacks. We wish that the toolbox and benchmark could serve the growing research community by providing a flexible toolkit to reimplement existing methods and develop their own new methods.

## Citation

If you find this project useful in your research, please consider cite:

```bibtex
@misc{mmfewshot2021,
    title={OpenMMLab Few Shot Learning Toolbox and Benchmark},
    author={mmfewshot Contributors},
    howpublished = {\url{https://github.com/open-mmlab/mmfewshot}},
    year={2021}
}
```

## License

This project is released under the [Apache 2.0 license](LICENSE).

## Projects in OpenMMLab

- [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational library for computer vision.
- [MIM](https://github.com/open-mmlab/mim): MIM installs OpenMMLab packages.
- [MMClassification](https://github.com/open-mmlab/mmclassification): OpenMMLab image classification toolbox and benchmark.
- [MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection toolbox and benchmark.
- [MMDetection3D](https://github.com/open-mmlab/mmdetection3d): OpenMMLab's next-generation platform for general 3D object detection.
- [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab rotated object detection toolbox and benchmark.
- [MMSegmentation](https://github.com/open-mmlab/mmsegmentation): OpenMMLab semantic segmentation toolbox and benchmark.
- [MMOCR](https://github.com/open-mmlab/mmocr): OpenMMLab text detection, recognition and understanding toolbox.
- [MMPose](https://github.com/open-mmlab/mmpose): OpenMMLab pose estimation toolbox and benchmark.
- [MMHuman3D](https://github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human parametric model toolbox and benchmark.
- [MMSelfSup](https://github.com/open-mmlab/mmselfsup): OpenMMLab self-supervised learning Toolbox and Benchmark.
- [MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab Model Compression Toolbox and Benchmark.
- [MMFewShot](https://github.com/open-mmlab/mmfewshot): OpenMMLab FewShot Learning Toolbox and Benchmark.
- [MMAction2](https://github.com/open-mmlab/mmaction2): OpenMMLab's next-generation action understanding toolbox and benchmark.
- [MMTracking](https://github.com/open-mmlab/mmtracking): OpenMMLab video perception toolbox and benchmark.
- [MMFlow](https://github.com/open-mmlab/mmflow): OpenMMLab optical flow toolbox and benchmark.
- [MMEditing](https://github.com/open-mmlab/mmediting): OpenMMLab image and video editing toolbox.
- [MMGeneration](https://github.com/open-mmlab/mmgeneration):  OpenMMLab Generative Model toolbox and benchmark.
- [MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMlab deep learning model deployment toolset.
