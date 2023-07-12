import os
from globals import domain_folder_path, regex_folder_path, adblocks_folder_path


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
if __name__ == "__main__":
    list_types = [domain_folder_path, regex_folder_path, adblocks_folder_path]

    for list_type in list_types:
        print(f"Sorting: {list_type}")
        order_txt_files(list_type)
