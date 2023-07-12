import os
from globals import domain_folder_path

### VARS ###
line_count_before = 0
line_count_after = 0
current_line = 0
line_count_before = 0
lines_processed = set()


def process_file(file_path, line_count_after, current_line):
    print(f"Processing file: {file_path}")

    lines = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line not in lines_processed:
                lines.append(line)
                lines_processed.add(line)
                line_count_after += 1

            # Update progress in real-time
            current_line += 1
            print(f"Lines processed: {current_line}/{line_count_before}", end="\r")

    # Rewrite the file with unique lines in the original order
    with open(file_path, "w") as file:
        file.write("\n".join(lines))

    return line_count_after, current_line


def process_folder(folder_path, line_count_after, current_line):
    print(f"Processing folder: {folder_path}")

    entries = sorted(os.listdir(folder_path))

    for entry in entries:
        entry_path = os.path.join(folder_path, entry)

        if os.path.isdir(entry_path):
            line_count_after, current_line = process_folder(entry_path, line_count_after, current_line)
        elif os.path.isfile(entry_path) and entry.endswith(".txt"):
            line_count_after, current_line = process_file(entry_path, line_count_after, current_line)

    return line_count_after, current_line


# Calculate total lines
for root, _, files in os.walk(domain_folder_path):
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(root, file), "r") as f:
                lines = [line.strip() for line in f]
                unique_lines = set(lines)
                line_count_before += len(unique_lines)

# Process folders and files
line_count_after, current_line = process_folder(domain_folder_path, line_count_after, current_line)

# Clear progress line
print()

# Output line count before and after deduplication
print("Line count before deduplication:", line_count_before)
print("Line count after deduplication:", line_count_after)
