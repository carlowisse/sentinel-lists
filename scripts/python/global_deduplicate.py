import os
import argparse


def count_lines_in_folder(folder_path):
    total_lines = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    lines = f.readlines()
                    total_lines += len(lines)
    return total_lines


def remove_duplicates_in_folder(folder_path, dry=False):
    total_lines_before = count_lines_in_folder(folder_path)
    unique_lines = set()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    lines = f.readlines()
                unique_lines.update([line.strip() for line in lines])
                if not dry:
                    with open(file_path, "w") as f:
                        f.write("\n".join(sorted(unique_lines)) + "\n")
    total_lines_after = count_lines_in_folder(folder_path)
    print(f"Total lines before: {total_lines_before}")
    print(f"Total lines after: {total_lines_after}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_path", help="path to folder containing .txt files")
    parser.add_argument("--dry", help="dry run (don't make any changes)", action="store_true")
    args = parser.parse_args()

    folder_path = args.folder_path
    dry = args.dry

    if dry:
        print("Dry run enabled. No changes will be made.")

    remove_duplicates_in_folder(folder_path, dry)
