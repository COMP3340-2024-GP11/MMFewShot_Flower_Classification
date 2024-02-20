python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn baseline_conv4_1xb64_flower_5way-1shot \
--ckpt-choice latest

python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn baseline_resnet12_1xb64_flower_5way-1shot \
--ckpt-choice latest

python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn baseline_conv4_1xb64_flower_5way-1shot \
--ckpt-choice best_accuracy_mean

python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn baseline_resnet12_1xb64_flower_5way-1shot \
--ckpt-choice best_accuracy_mean



python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn baseline-plus_conv4_1xb64_flower_5way-1shot \
--ckpt-choice latest

python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn baseline-plus_resnet12_1xb64_flower_5way-1shot \
--ckpt-choice latest

python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn baseline-plus_conv4_1xb64_flower_5way-1shot \
--ckpt-choice best_accuracy_mean

python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn baseline-plus_resnet12_1xb64_flower_5way-1shot  \
--ckpt-choice best_accuracy_mean



python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn maml_conv4_1xb105_flower_5way-1shot \
--ckpt-choice latest

python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn maml_resnet12_1xb105_flower_5way-1shot \
--ckpt-choice latest

python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn maml_conv4_1xb105_flower_5way-1shot \
--ckpt-choice best_accuracy_mean

python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn maml_resnet12_1xb105_flower_5way-1shot \
--ckpt-choice best_accuracy_mean



python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn proto-net_conv4_1xb105_flower_5way-1shot \
--ckpt-choice latest

python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn proto-net_resnet12_1xb105_flower_5way-1shot \
--ckpt-choice latest

python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn proto-net_conv4_1xb105_flower_5way-1shot \
--ckpt-choice best_accuracy_mean

python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn proto-net_resnet12_1xb105_flower_5way-1shot \
--ckpt-choice best_accuracy_mean