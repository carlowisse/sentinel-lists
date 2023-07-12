import os
from globals import domain_folder_path, regex_folder_path


def order_txt_files(folder_path):
    txt_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                txt_files.append(file_path)

    for file_path in txt_files:
        with open(file_path, "r+") as file:
            lines = file.readlines()
            sorted_lines = sorted(lines)
            file.seek(0)
            file.writelines(sorted_lines)
            file.truncate()


### EXECUTE ###
order_txt_files(domain_folder_path)
