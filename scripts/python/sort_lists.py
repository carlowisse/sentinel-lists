import os


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


# Example usage
folder_path = "../../lists/domains"
order_txt_files(folder_path)
