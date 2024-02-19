# # Use checkpoint with best acc mean or latest?
# python ./tools/classification/test.py \
#     ./configs/classification/_base_/meta_test/flower_meta-test_5way-1shot.py \
#     ./output/baseline_conv4_1xb64_flower_5way-1shot_split1/best_accuracy_mean.pth \
#     --train-cfg ./configs/classification/baseline/flower/baseline_conv4_1xb64_flower_5way-1shot.py \
#     --work-dir ./test_output/baseline_conv4_1xb64_flower_5way-1shot_split1_best_acc_mean \
#     --options data.val.split_num='split1', data.test.dataset.split_num='split1' \
#     --metrics "accuracy", "precision", "recall", "f1_score" 

# python ./tools/classification/test.py \
#     ./configs/classification/_base_/meta_test/flower_meta-test_5way-1shot.py \
#     ./output/baseline_conv4_1xb64_flower_5way-1shot_split1/latest.pth \
#     --work-dir ./test_output/baseline_conv4_1xb64_flower_5way-1shot_split1_latest \
#     --options data.val.split_num='split1', data.test.dataset.split_num='split1' \
#     --metrics "accuracy", "precision", "recall", "f1_score" 
    
# python ./tools/classification/test.py \
#     ./configs/classification/_base_/meta_test/flower_meta-test_5way-1shot.py \
#     ./output/baseline_conv4_1xb64_flower_5way-1shot_split2/latest.pth \
#     --work-dir ./test_output/baseline_conv4_1xb64_flower_5way-1shot_split2_latest \
#     --options data.val.split_num='split2', data.test.dataset.split_num='split2' \
#     --metrics "accuracy", "precision", "recall", "f1_score" \
#     --gpu-id 1

# python ./tools/classification/test.py \
#     ./configs/classification/_base_/meta_test/flower_meta-test_5way-1shot.py \
#     ./output/baseline_conv4_1xb64_flower_5way-1shot_split3/latest.pth \
#     --work-dir ./test_output/baseline_conv4_1xb64_flower_5way-1shot_split3_latest \
#     --options data.val.split_num='split3', data.test.dataset.split_num='split3' \
#     --metrics "accuracy", "precision", "recall", "f1_score"  \
#     --gpu-id 1


python ./tools/classification/test.py \
    ./configs/classification/_base_/meta_test/flower_meta-test_5way-1shot.py \
    ./output/baseline_resnet12_1xb64_flower_5way-1shot_split1/latest.pth \
    --train-cfg ./configs/classification/baseline/flower/baseline_resnet12_1xb64_flower_5way-1shot.py \
    --work-dir ./test_output/baseline_resnet12_1xb64_flower_5way-1shot_split1_latest \
    --options data.val.split_num='split1', data.test.dataset.split_num='split1' \
    --metrics "accuracy", "precision", "recall", "f1_score"  \
    --gpu-id 1

python ./tools/classification/test.py \
    ./configs/classification/_base_/meta_test/flower_meta-test_5way-1shot.py \
    ./output/baseline_resnet12_1xb64_flower_5way-1shot_split2/latest.pth \
    --train-cfg ./configs/classification/baseline/flower/baseline_resnet12_1xb64_flower_5way-1shot.py \
    --work-dir ./test_output/baseline_resnet12_1xb64_flower_5way-1shot_split2_latest \
    --options data.val.split_num='split2', data.test.dataset.split_num='split2' \
    --metrics "accuracy", "precision", "recall", "f1_score"  \
    --gpu-id 1

python ./tools/classification/test.py \
    ./configs/classification/_base_/meta_test/flower_meta-test_5way-1shot.py \
    ./output/baseline_resnet12_1xb64_flower_5way-1shot_split3/latest.pth \
    --work-dir ./test_output/baseline_resnet12_1xb64_flower_5way-1shot_split3_latest \
    --options data.val.split_num='split3', data.test.dataset.split_num='split3' \
    --train-cfg ./configs/classification/baseline/flower/baseline_resnet12_1xb64_flower_5way-1shot.py \
    --metrics "accuracy", "precision", "recall", "f1_score"  \
    --gpu-id 1
        