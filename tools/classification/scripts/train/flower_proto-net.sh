python ./tools/classification/train.py \
    ./configs/classification/proto_net/flower/proto-net_conv4_1xb105_flower_5way-1shot.py \
    --work-dir ./output/proto-net_conv4_1xb105_flower_5way-1shot_meta-test \
    --gpu-id 0

python ./tools/classification/train.py \
    ./configs/classification/proto_net/flower/proto-net_resnet12_1xb105_flower_5way-1shot.py \
    --work-dir ./output/proto-net_resnet12_1xb105_flower_5way-1shot_meta-test \
    --gpu-id 1
