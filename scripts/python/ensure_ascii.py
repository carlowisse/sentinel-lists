import argparse
import os


def count_lines(file_path):
    with open(file_path, "r") as f:
        return sum(1 for _ in f)


def process_file(file_path, dry_run=False):
    initial_count = count_lines(file_path)
    removed_count = 0
    file_name = os.path.basename(file_path)
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f]
    if not dry_run:
        with open(file_path, "w") as f:
            for line in lines:
                if all(ord(c) < 128 for c in line):
                    f.write(line + "\n")
                else:
                    removed_count += 1
    else:
        for line in lines:
            if not all(ord(c) < 128 for c in line):
                removed_count += 1
    updated_count = initial_count - removed_count
    print(file_name)
    print("Initial:", initial_count)
    print("Removed:", removed_count)
    print("Updated:", updated_count)
    print("--------------------")


def process_folder(folder_path, dry_run=False):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                process_file(file_path, dry_run=dry_run)


parser = argparse.ArgumentParser(description="Process text files and remove non-ASCII lines.")
parser.add_argument("input", help="the input folder (recursive)")
parser.add_argument("--dry", help="perform a dry run without editing the files", action="store_true")
args = parser.parse_args()

input_folder = args.input

if args.dry:
    process_folder(input_folder, dry_run=True)
else:
    process_folder(input_folder)
