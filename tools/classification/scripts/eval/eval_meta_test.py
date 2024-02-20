"""
Evaluate the meta test performance of all models in the ./test_output directory
and output a pandas dataframe contain mean+-std.
"""

import os
import re
import argparse
import pandas as pd
import numpy as np
from IPython.display import display

def parse_args():
    """
    Create an argument parser
    """
    parser = argparse.ArgumentParser(description='Parse log files and compute final meta test accuracy.')
    parser.add_argument('--output-dir', 
                        type=str, 
                        help='Path to the output directory',
                        default='./test_output'
                       )
    parser.add_argument('--save-dir', 
                        type=str, 
                        help='Directory to save the result',
                        default='./test_output/results'
                       )
    args = parser.parse_args()
    return args

def eval_all_meta_test(meta_out_dir):
    """
    Evaluate all meta test result in a directory.
    
    Iterate over the subdirectories in the output directory
        for all the log files in the directory
        for each split
            sort them by the timestamp and choose the lastest log file
            parse and find the final meta test accuray
    format the output into a pandas dataframe and save it under a directory
    """
    setting_infos = []
    split_infos = []
    ckpt_infos = []
    meta_means = []
    meta_stds = []
    
    for subdir in os.listdir(meta_out_dir):
        subdir_path = os.path.join(meta_out_dir, subdir)
        if os.path.isdir(subdir_path):
            # Check if the log file exists
            log_fns = [file for file in os.listdir(subdir_path) if file.endswith(".log")]
            log_fns.sort()
            log_fns.reverse()
            
            if len(log_fns)>0:
                latest_log_fn = log_fns[0]
                
                with open(os.path.join(subdir_path, latest_log_fn), 'r') as f:
                    log_content = f.readlines()
                    ckpt_found = False
                    mean_found = False
                    std_found = False
                    
                    for line in reversed(log_content):
                        ckpt_info = re.search(r'(.+pth$)', line)
                        acc_mean_info = re.search(r'accuracy_mean : ([\d.]+)', line)
                        acc_std_info = re.search(r'accuracy_std : ([\d.]+)', line)
            
                        if ckpt_info and (not ckpt_found):          
                            ckpt_path = ckpt_info.group(1)
                            ckpt_path = ckpt_path.split("./output/")[-1]
                            
                            info, ckpt_info = ckpt_path.split("/")
                            ckpt_info = ckpt_info[:-4]
                            setting_info = "_".join(info.split("_")[:-1])
                            split_info = info.split("_")[-1]
                            
                            ckpt_infos.append(ckpt_info)
                            setting_infos.append(setting_info)
                            split_infos.append(split_info)
                            ckpt_found = True
                        elif acc_mean_info and (not mean_found):
                            acc_mean = round(float(acc_mean_info.group(1)),2)
                            meta_means.append(acc_mean)
                            mean_found = True
                        elif acc_std_info and (not std_found):
                            acc_std = round(float(acc_std_info.group(1)),2)
                            meta_stds.append(acc_std)
                            std_found = True
                        else: 
                            continue

                        if ckpt_found and mean_found and std_found:
                            assert len(setting_infos) == len(split_infos)
                            assert len(setting_infos) == len(ckpt_infos)
                            assert len(setting_infos) == len(meta_means)
                            assert len(setting_infos) == len(meta_stds)
                            break
    res_df = pd.DataFrame({
        'setting': setting_infos,
        'split': split_infos,
        'ckpt_choice': ckpt_infos,
        'meta_test_mean': meta_means,
        'meta_test_std': meta_stds
    })
    return res_df
            
                        

def main():
    args = parse_args()
    output_dir = args.output_dir
    save_dir = args.save_dir

    os.makedirs(save_dir, exist_ok=True)
    res_df = eval_all_meta_test(output_dir)
    
    display(res_df)
    res_df.to_csv(f"{save_dir}/meta_eval_res.csv")
    

if __name__ == '__main__':
    main()
