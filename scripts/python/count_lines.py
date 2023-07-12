import os
from globals import domain_folder_path, regex_folder_path, adblocks_folder_path


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

    return total_line_count


def get_line_count(list_type):
    txt_files = []
    total_line_count = 0

    if list_type == "domains":
        folder_path = domain_folder_path
    elif list_type == "regexes":
        folder_path = regex_folder_path
    elif list_type == "adblocks":
        folder_path = adblocks_folder_path

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                txt_files.append(file_path)

    for file_path in txt_files:
        with open(file_path, "r") as file:
            line_count = sum(1 for line in file)
            total_line_count += line_count

    return total_line_count


### EXECUTE ###
domains_count = count_lines(domain_folder_path)
regexes_count = count_lines(regex_folder_path)
adblocks_count = count_lines(adblocks_folder_path)

print(f"Domains: {domains_count}")
print(f"Regexes: {regexes_count}")
print(f"Adblocks: {adblocks_count}")
