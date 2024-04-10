python ./tools/classification/train.py \
    ./configs/classification/baseline_plus/flower/baseline-plus_conv4_1xb64_flower_5way-1shot.py \
    --work-dir ./output/baseline-plus_conv4_1xb64_flower_5way-1shot_meta-test \
    --gpu-id 0

python ./tools/classification/train.py \
    ./configs/classification/baseline_plus/flower/baseline-plus_resnet12_1xb64_flower_5way-1shot.py \
    --work-dir ./output/baseline-plus_resnet12_1xb64_flower_5way-1shot_meta-test \
    --gpu-id 1
