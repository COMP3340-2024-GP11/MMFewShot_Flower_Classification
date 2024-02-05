python ./tools/classification/train.py \
    ./configs/classification/baseline/flower/baseline_conv4_1xb64_flower_5way-1shot.py \
    --work-dir ./output/baseline_resnet12_1xb64_flower_5way-1shot

python ./tools/classification/train.py \
    ./configs/classification/baseline/flower/baseline_conv4_1xb64_flower_5way-5shot.py \
    --work-dir ./output/baseline_resnet12_1xb64_flower_5way-5shot

python ./tools/classification/train.py \
    ./configs/classification/baseline/flower/baseline_resnet12_1xb64_flower_5way-1shot.py \
    --work-dir ./output/baseline_resnet12_1xb64_flower_5way-1shot

python ./tools/classification/train.py \
    ./configs/classification/baseline/flower/baseline_resnet12_1xb64_flower_5way-5shot.py \
    --work-dir ./output/baseline_resnet12_1xb64_flower_5way-5shot