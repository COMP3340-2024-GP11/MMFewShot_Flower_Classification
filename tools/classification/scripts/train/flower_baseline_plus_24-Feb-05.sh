python ./tools/classification/train.py \
    ./configs/classification/baseline_plus/flower/baseline-plus_conv4_1xb64_flower_5way-1shot.py \
    --work-dir ./output/baseline-plus_conv4_1xb64_flower_5way-1shot_split1 \
    --options data.train.split_num='split1'

python ./tools/classification/train.py \
    ./configs/classification/baseline_plus/flower/baseline-plus_conv4_1xb64_flower_5way-1shot.py \
    --work-dir ./output/baseline-plus_conv4_1xb64_flower_5way-1shot_split2 \
    --options data.train.split_num='split2'

python ./tools/classification/train.py \
    ./configs/classification/baseline_plus/flower/baseline-plus_conv4_1xb64_flower_5way-1shot.py \
    --work-dir ./output/baseline-plus_conv4_1xb64_flower_5way-1shot_split3 \
    --options data.train.split_num='split3'

python ./tools/classification/train.py \
    ./configs/classification/baseline_plus/flower/baseline-plus_resnet12_1xb64_flower_5way-1shot.py \
    --work-dir ./output/baseline-plus_resnet12_1xb64_flower_5way-1shot_split1 \
    --options data.train.split_num='split1'

python ./tools/classification/train.py \
    ./configs/classification/baseline_plus/flower/baseline-plus_resnet12_1xb64_flower_5way-1shot.py \
    --work-dir ./output/baseline-plus_resnet12_1xb64_flower_5way-1shot_split2 \
    --options data.train.split_num='split2'

python ./tools/classification/train.py \
    ./configs/classification/baseline_plus/flower/baseline-plus_resnet12_1xb64_flower_5way-1shot.py \
    --work-dir ./output/baseline-plus_resnet12_1xb64_flower_5way-1shot_split3 \
    --options data.train.split_num='split3'
    