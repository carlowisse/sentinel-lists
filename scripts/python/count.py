import os

DOMAINS_FOLDER = "../lists/domains"
REGEXES_FOLDER = "../lists/regexes"


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


domains_lines = count_lines_in_folder(DOMAINS_FOLDER)
regexes_lines = count_lines_in_folder(REGEXES_FOLDER)

print("Domains:", domains_lines)
print("Regexes:", regexes_lines)
