python ./tools/classification/train.py \
    ./configs/classification/proto_net/flower/proto-net_conv4_1xb105_flower_5way-1shot.py \
    --work-dir ./output/proto-net_conv4_1xb105_flower_5way-1shot_split1 \
    --options data.train.split_num='split1'

# python ./tools/classification/train.py \
#     ./configs/classification/proto_net/flower/proto-net_conv4_1xb105_flower_5way-5shot.py \
#     --work-dir ./output/proto-net_conv4_1xb105_flower_5way-5shot

python ./tools/classification/train.py \
    ./configs/classification/proto_net/flower/proto-net_resnet12_1xb105_flower_5way-1shot.py \
    --work-dir ./output/proto-net_resnet12_1xb105_flower_5way-1shot_split1 \
    --options data.train.split_num='split1'

python ./tools/classification/train.py \
    ./configs/classification/proto_net/flower/proto-net_resnet12_1xb105_flower_5way-1shot.py \
    --work-dir ./output/proto-net_resnet12_1xb105_flower_5way-1shot_split2 \
    --options data.train.split_num='split2'

python ./tools/classification/train.py \
    ./configs/classification/proto_net/flower/proto-net_resnet12_1xb105_flower_5way-1shot.py \
    --work-dir ./output/proto-net_resnet12_1xb105_flower_5way-1shot_split3 \
    --options data.train.split_num='split3'
    
# python ./tools/classification/train.py \
#     ./configs/classification/proto_net/flower/proto-net_resnet12_1xb105_flower_5way-5shot.py \
#     --work-dir ./output/proto-net_resnet12_1xb105_flower_5way-5shot