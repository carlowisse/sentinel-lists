import os
import re
import argparse


def remove_ips(file_path, dry_run=False):
    regex = r"^\d+\.\d+\.\d+\.\d+\s+"
    updated_count = 0

    with open(file_path, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if re.search(regex, line):
            updated_count += 1
            lines[i] = re.sub(regex, "", line)

    if not dry_run:
        with open(file_path, "w") as f:
            f.writelines(lines)

    return len(lines), updated_count


def process_files(path, dry_run=False):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                initial_count, updated_count = remove_ips(file_path, dry_run)
                print(file_path)
                print(f"Initial: {initial_count}")
                print(f"Updated: {updated_count}")
                print("--------------------")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove IP addresses from text files")
    parser.add_argument("path", help="Path to directory to process")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true", help="Run without modifying any files")
    args = parser.parse_args()

    process_files(args.path, args.dry_run)
