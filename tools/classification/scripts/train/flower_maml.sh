python ./tools/classification/train.py \
    ./configs/classification/maml/flower/maml_conv4_1xb105_flower_5way-1shot.py \
    --work-dir ./output/maml_conv4_1xb105_flower_5way-1shot_meta-test \
    --gpu-id 0

python ./tools/classification/train.py \
    ./configs/classification/maml/flower/maml_resnet12_1xb105_flower_5way-1shot.py \
    --work-dir ./output/maml_resnet12_1xb105_flower_5way-1shot_meta-test \
    --gpu-id 1
