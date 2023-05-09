import os
import sys
import re


def cleanup_line(line):
    return line.strip()


def remove_empty_lines(lines):
    return [line for line in lines if line.strip()]


def remove_comments(lines):
    comment_regex = r"^\s*(##|!#|!!|//|/\*).*$"
    return [line for line in lines if not re.match(comment_regex, line)]


def cleanup_lines(lines, lower_case):
    cleaned_lines = [cleanup_line(line) for line in lines]
    cleaned_lines = remove_empty_lines(cleaned_lines)
    cleaned_lines = remove_comments(cleaned_lines)
    if lower_case:
        cleaned_lines = [line.lower() for line in cleaned_lines]
    return cleaned_lines


def process_file(file_path, dry_run):
    with open(file_path, "r") as f:
        lines = f.readlines()
        initial_count = len(lines)

    cleaned_lines = cleanup_lines(lines, "domains" in file_path.lower())

    # Print counts
    print("File:", file_path)
    print("Lines:", initial_count)
    print("Whitespace Cleaned:", len(cleaned_lines))
    print("Empty Lines", initial_count - len(cleaned_lines))

    comments_removed_count = initial_count - len(cleanup_lines(lines, False))
    if comments_removed_count > 0:
        cleaned_lines.append(f"Comments Removed: {comments_removed_count}")

    if "domains" in file_path.lower():
        cleaned_lines = [line.lower() for line in cleaned_lines]
        print("Lowercased:", initial_count - len(cleaned_lines))

    print("--------------------")

    # Write updated lines to file if not dry run
    if not dry_run:
        with open(file_path, "w") as f:
            f.writelines("\n".join(cleaned_lines))


def process_directory(directory_path, dry_run):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                process_file(file_path, dry_run)


if __name__ == "__main__":
    directory_path = sys.argv[1]
    dry_run = False

    if len(sys.argv) == 3 and sys.argv[2] == "--dry":
        dry_run = True

    process_directory(directory_path, dry_run)
