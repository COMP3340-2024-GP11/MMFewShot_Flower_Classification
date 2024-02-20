""""
Automate meta test for different model and splits.

Example usage:
python ./tools/classification/scripts/meta_test/flower_meta_test.py \
--config-fn flower_meta-test_5way-1shot \
--ckpt-fn baseline_resnet12_1xb64_flower_5way-1shot \
--ckpt-choice latest

"""
import subprocess
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description='flower meta test arguments')
    parser.add_argument(
        '--config-fn', 
        type=str,
        help='config file name - test config and train config should have the same name',
        default='flower_meta-test_5way-1shot')
    parser.add_argument(
        '--ckpt-fn', 
        type=str,
        help='checkpoint file name',
        default='baseline_conv4_1xb64_flower_5way-1shot')
    parser.add_argument(
        '--ckpt-choice', 
        type=str,
        help='checkpoint choice',
        default='best_accuracy_mean')

    args = parser.parse_args()
    return args
 
def main():
    args = parse_args()
    config_fn = args.config_fn # contains meta test info
    ckpt_fn = args.ckpt_fn # contains model info
    ckpt_choice = args.ckpt_choice # how to choose final checkpoint
    
    base_str = 'python ./tools/classification/test.py '
    test_config_str = f'./configs/classification/_base_/meta_test/{config_fn}.py '
    metrics_str = '--metrics "accuracy", "precision", "recall", "f1_score" '
    
    for split in ['split1', 'split2', 'split3']: 
        train_config_str = f'--train-cfg ./output/{ckpt_fn}_{split}/{ckpt_fn}.py '
        work_dir = f"./test_output/{ckpt_fn}_{split}_{ckpt_choice}"
        work_dir_str = f"--work-dir {work_dir} "
        checkpoint_str = f'./output/{ckpt_fn}_{split}/{ckpt_choice}.pth '
        if os.path.isdir(work_dir) or (not(os.path.isfile(checkpoint_str.strip()))):
            pass
        else:
            option_str = f'--options data.val.split_num={split}, data.test.dataset.split_num={split} '
    
            cmd = (base_str + test_config_str + checkpoint_str + train_config_str 
                  + work_dir_str + option_str + metrics_str)
    
            subprocess.run(cmd, shell=True)   

if __name__ == '__main__':
    main()

# # Use checkpoint with best acc mean or latest?

# python ./tools/classification/test.py \
#     ./configs/classification/_base_/meta_test/flower_meta-test_5way-1shot.py \
#     ./output/baseline_conv4_1xb64_flower_5way-1shot_split3/latest.pth \
#     --work-dir ./test_output/baseline_conv4_1xb64_flower_5way-1shot_split3_latest \
#     --options data.val.split_num='split3', data.test.dataset.split_num='split3' \
#     --metrics "accuracy", "precision", "recall", "f1_score"  \
#     --gpu-id 1