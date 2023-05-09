import os
import re
import argparse

DOMAIN_REGEX = re.compile(r"^(?!-)[a-zA-Z0-9-]{0,63}(\.[a-zA-Z0-9-]{0,63})*\.[a-zA-Z]{2,63}$")


def is_valid_domain(domain):
    return bool(DOMAIN_REGEX.match(domain))


def process_file(file_path, dry_run):
    initial_count = 0
    removed_count = 0
    removed_domains = set()

    with open(file_path, "r") as f:
        lines = f.readlines()
        initial_count = len(lines)

        for i, line in enumerate(lines):
            domain = line.strip()
            if not is_valid_domain(domain):
                if dry_run and removed_count < 10:
                    removed_domains.add(domain)
                removed_count += 1
                lines[i] = ""

    if not dry_run:
        with open(file_path, "w") as f:
            f.writelines(lines)

    print(f"File: {file_path}")
    print(f"Initial: {initial_count}")
    print(f"Removed: {removed_count}")
    if removed_count > 0:
        print(f"Updated: {initial_count - removed_count}")
    else:
        print("Updated: 0")
    print("--------------------")


def process_folder(folder_path, dry_run):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                process_file(file_path, dry_run)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process text files and remove invalid domains.")
    parser.add_argument("folder", help="path to the folder to process")
    parser.add_argument("--dry-run", action="store_true", help="run in dry-run mode")
    args = parser.parse_args()

    process_folder(args.folder, args.dry_run)
