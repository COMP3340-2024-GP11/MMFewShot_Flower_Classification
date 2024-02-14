import argparse
import os
import shutil
import scipy.io

# Create an argument parser
parser = argparse.ArgumentParser(description='Create dataset split.')
parser.add_argument('--data-dir', type=str, 
                    help='Path to the data directory',
                    default="/userhome/cs2/xinjiayi/mmfewshot/data/flowers"
                   )
parser.add_argument('--meta-dir', type=str, 
                    help='Path to the meta-data directory, which contains the split information',
                    default="/userhome/cs2/xinjiayi/mmfewshot/data/flowers/meta"
                   )
parser.add_argument('--split-pth', type=str, 
                    help='Path to the split file',
                   default="/userhome/cs2/xinjiayi/mmfewshot/data/flowers/meta/datasplits.mat")
args = parser.parse_args()

# Define the paths
dataset_dir = args.data_dir
meta_dir = args.meta_dir
split_pth = args.split_pth

# Create the directories if they don't exist
os.makedirs(meta_dir, exist_ok=True)

def generate_meta_file(split_indices, meta_file_path):
    with open(meta_file_path, 'w') as meta_file:
        for idx in split_indices:
            class_number = (idx - 1) // 80
            file_name = f'image_{str(idx).zfill(4)}.jpg'
            image_path = f"{dataset_dir}/" + file_name
            line = f"{image_path} {class_number}\n"
            meta_file.write(line)

# Load the data splits from datasplits.mat
mat_data = scipy.io.loadmat(split_pth)

for i in range(1,4):
    idx = int(i)
    
    train_indices = mat_data[f"trn{str(idx)}"].flatten()
    val_indices = mat_data[f"val{str(idx)}"].flatten()
    test_indices = mat_data[f"tst{str(idx)}"].flatten()

    out_dir = os.path.join(meta_dir, f"split{str(idx)}")
    os.makedirs(out_dir, exist_ok=True)

    # Generate meta file for training data
    train_meta_file = os.path.join(out_dir, "train_meta.txt")
    generate_meta_file(train_indices, train_meta_file)
    # Generate meta file for validation data
    val_meta_file = os.path.join(out_dir, "val_meta.txt")
    generate_meta_file(val_indices, val_meta_file)
    # Generate meta file for test data
    test_meta_file = os.path.join(out_dir, "test_meta.txt")
    generate_meta_file(test_indices, test_meta_file)

