import os
import requests


def compile_files_in_dir(directory):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # If the file is a directory, recursively call this function on it
        if os.path.isdir(filepath):
            compile_files_in_dir(filepath)
        # If the file is a .txt file, compile its contents
        elif os.path.isfile(filepath) and filename.endswith(".txt"):
            # Open the input file and read the list of URLs
            with open(filepath, "r") as f:
                urls = f.readlines()

            # Create the output file name
            output_file = os.path.splitext(filepath)[0] + "_compiled.txt"

            # Open the output file for writing
            with open(output_file, "w") as f:
                # Loop through the URLs and download the contents of each file
                for url in urls:
                    response = requests.get(url.strip())
                    if response.status_code == 200:
                        # Write the contents of the file to the output file
                        f.write(response.text)
                    else:
                        print(f"Failed to download {url.strip()}")

            print(f"Compilation complete. Output written to {output_file}")


# Get the name of the input directory from the user
input_dir = input("Enter the name of the input directory: ")

# Call the compile_files_in_dir function on the input directory
compile_files_in_dir(input_dir)
