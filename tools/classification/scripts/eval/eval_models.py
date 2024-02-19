import os
import re
import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description='Parse log files and extract final mean accuracy.')
parser.add_argument('--output-dir', type=str, help='Path to the output directory')
args = parser.parse_args()

output_dir = args.output_dir

# Iterate over the subdirectories in the output directory
for subdir in os.listdir(output_dir):
    subdir_path = os.path.join(output_dir, subdir)
    if os.path.isdir(subdir_path):
        # Check if the log file exists
        for file in os.listdir(subdir_path):
            if file.endswith(".log"):
                with open(os.path.join(subdir_path, file), 'r') as f:
                    log_content = f.readlines()
    
                    # Iterate over lines in reverse order until the first line that matches the pattern
                    for line in reversed(log_content):
                        match = re.search(r'accuracy_mean: ([\d.]+)', line)
                        if match:
                            final_accuracy = match.group(1)
                            print(f"Model: {subdir}, Final Mean Accuracy: {final_accuracy}")
                            break