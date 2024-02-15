python ./tools/classification/train.py \
    ./configs/classification/maml/flower/maml_conv4_1xb105_flower_5way-1shot.py \
    --work-dir ./output/maml_conv4_1xb105_flower_5way-1shot_split1 \
    --options data.train.split_num='split1'

# python ./tools/classification/train.py \
#     ./configs/classification/maml/flower/maml_conv4_1xb105_flower_5way-1shot.py \
#     --work-dir ./output/maml_conv4_1xb105_flower_5way-1shot_split2 \
#     --options data.train.data_prefix='data/flowers/meta/split2'

# python ./tools/classification/train.py \
#     ./configs/classification/maml/flower/maml_conv4_1xb105_flower_5way-1shot.py \
#     --work-dir ./output/maml_conv4_1xb105_flower_5way-1shot_split3 \
#     --options data.train.data_prefix='data/flowers/meta/split3'

# python ./tools/classification/train.py \
#     ./configs/classification/maml/flower/maml_conv4_1xb105_flower_5way-5shot.py \
#     --work-dir ./output/maml_conv4_1xb105_flower_5way-5shot

python ./tools/classification/train.py \
    ./configs/classification/maml/flower/maml_resnet12_1xb105_flower_5way-1shot.py \
    --work-dir ./output/maml_resnet12_1xb105_flower_5way-1shot_split1 \
    --options data.train.split_num='split1'

# python ./tools/classification/train.py \
#     ./configs/classification/maml/flower/maml_resnet12_1xb105_flower_5way-5shot.py \
#     --work-dir ./output/maml_resnet12_1xb105_flower_5way-5shot