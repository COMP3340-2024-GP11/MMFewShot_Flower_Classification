"""Generate Class split for flower dataset.
Usage: 
python tools/classification/scripts/preprocessing/flower_create_class_split.py \
--meta-dir data/flowers/meta \
--train-classes '0 1 2 3 4 5 6' \
--val-classes '7 8 9 10 11' \
--test-classes '12 13 14 15 16'
"""


import argparse
import os
import shutil

def parse_args():
    # Define a custom argument type for a list of strings
    def list_of_strings(arg):
        return arg.split(' ')
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Create class split for the flower dataset.')
    parser.add_argument('--data-dir', type=str, 
                        help='Path to the data directory',
                        default="data/flowers"
                       )
    parser.add_argument('--meta-dir', type=str, 
                        help='Path to the meta-data directory, which contains the split information',
                        default="data/flowers/meta"
                       )
    parser.add_argument('--train-classes', type=list_of_strings,
                        help='Classes used for training'
                       )
    parser.add_argument('--val-classes', type=list_of_strings,
                        help='Classes used for validation'
                       )
    parser.add_argument('--test-classes', type=list_of_strings,
                        help='Classes used for testing'
                       )
    args = parser.parse_args()

    return args

def generate_meta_file_for_class_split(split_dir,
                      train_classes,
                      val_classes,
                      test_classes):
    train_meta_file = os.path.join(split_dir, "train.txt")
    val_meta_file = os.path.join(split_dir, "val.txt")
    test_meta_file = os.path.join(split_dir, "test.txt")

    def write_meta_file(file_path, classes):
        with open(file_path, 'w') as meta_file:
            for cls in classes:
                for idx in range(80*cls+1, 80*(cls+1)+1):
                    file_name = f'image_{str(idx).zfill(4)}.jpg'
                    new_label = int(cls - classes[0])
                    line = f"{file_name} {str(new_label)}\n"
                    meta_file.write(line)
        meta_file.close()
                    
    write_meta_file(train_meta_file, train_classes)
    write_meta_file(val_meta_file, val_classes)
    write_meta_file(test_meta_file, test_classes)

def main():
    args = parse_args()
    # Define the paths
    dataset_dir = args.data_dir
    meta_dir = args.meta_dir
    
    train_classes = [int(cls) for cls in args.train_classes]
    val_classes = [int(cls) for cls in args.val_classes]
    test_classes = [int(cls) for cls in args.test_classes]
    
    # Create the directories if they don't exist
    os.makedirs(meta_dir, exist_ok=True)

    generate_meta_file_for_class_split(meta_dir, train_classes, val_classes,test_classes)

if __name__ == '__main__':
    main()






