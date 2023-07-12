import os


def count_lines(folder_path):
    txt_files = []
    total_line_count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                txt_files.append(file_path)

    for file_path in txt_files:
        with open(file_path, "r") as file:
            line_count = sum(1 for line in file)
            total_line_count += line_count

    print(f"Total line count: {total_line_count}")


# Example usage
folder_path = "../../lists/domains"
count_lines(folder_path)
