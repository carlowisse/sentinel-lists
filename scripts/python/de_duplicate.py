import os


def process_file(file_path, line_count_before, line_count_after, current_line):
    print(f"Processing file: {file_path}")

    unique_lines = set()

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line not in unique_lines:
                unique_lines.add(line)

            # Update progress in real-time
            current_line += 1
            print(f"Lines processed: {current_line}/{total_lines}", end="\r")

    # Rewrite the file with unique lines
    with open(file_path, "w") as file:
        file.writelines(f"{line}\n" for line in unique_lines)

    # Increment line count before deduplication
    with open(file_path, "r") as file:
        line_count_before += sum(1 for _ in file)

    line_count_after += len(unique_lines)

    return line_count_before, line_count_after, current_line


def process_folder(folder_path, line_count_before, line_count_after, current_line):
    print(f"Processing folder: {folder_path}")

    entries = sorted(os.listdir(folder_path))

    for entry in entries:
        entry_path = os.path.join(folder_path, entry)

        if os.path.isdir(entry_path):
            line_count_before, line_count_after, current_line = process_folder(
                entry_path, line_count_before, line_count_after, current_line
            )
        elif os.path.isfile(entry_path) and entry.endswith(".txt"):
            line_count_before, line_count_after, current_line = process_file(
                entry_path, line_count_before, line_count_after, current_line
            )

    return line_count_before, line_count_after, current_line


# Input folder
input_folder = input("Enter the input folder: ")

# Validate input folder
if not os.path.isdir(input_folder):
    print(f"Invalid input folder: {input_folder}")
    exit(1)

# Variables
line_count_before = 0
line_count_after = 0
current_line = 0
total_lines = 0

# Calculate total lines
line_count_before, line_count_after, current_line = process_folder(
    input_folder, line_count_before, line_count_after, current_line
)
total_lines = current_line

# Clear progress line
print()

# Output line count before and after deduplication
print("Line count before deduplication:", line_count_before)
print("Line count after deduplication:", line_count_after)
