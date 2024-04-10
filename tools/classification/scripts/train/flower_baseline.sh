python ./tools/classification/train.py \
    ./configs/classification/baseline/flower/baseline_conv4_1xb64_flower_5way-1shot.py \
    --work-dir ./output/baseline_conv4_1xb64_flower_5way-1shot_meta-test \
    --gpu-id 0

python ./tools/classification/train.py \
    ./configs/classification/baseline/flower/baseline_resnet12_1xb64_flower_5way-1shot.py \
    --work-dir ./output/baseline_resnet12_1xb64_flower_5way-1shot_meta-test \
    --gpu-id 1

