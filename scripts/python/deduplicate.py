import os
import sys


def remove_duplicates(file_path, dry_run):
    with open(file_path, "r") as f:
        lines = f.readlines()
        initial_count = len(lines)

    # Remove duplicates and get updated count
    lines = list(set(line.strip() for line in lines))
    updated_count = len(lines)

    # Print counts
    print("File:", file_path)
    print("Initial:", initial_count)
    print("Removed:", initial_count - updated_count)
    print("Updated:", updated_count)
    print("--------------------")

    # Write updated lines to file if not dry run
    if not dry_run:
        with open(file_path, "w") as f:
            f.writelines(line + "\n" for line in lines)


def remove_duplicates_recursive(folder_path, dry_run):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                remove_duplicates(file_path, dry_run)


if __name__ == "__main__":
    folder_path = sys.argv[1]
    dry_run = False

    if len(sys.argv) == 3 and sys.argv[2] == "--dry":
        dry_run = True

    remove_duplicates_recursive(folder_path, dry_run)
