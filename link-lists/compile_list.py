import os
import requests
import argparse


def compile_files_in_dir(directory):
    # Create the output directory
    output_dir = os.path.join(directory, "compiled")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # If the file is a directory, skip it
        if os.path.isdir(filepath):
            continue
        # If the file is a .txt file, compile its contents
        elif os.path.isfile(filepath) and filename.endswith(".txt"):
            # Open the input file and read the list of URLs
            with open(filepath, "r") as f:
                urls = f.readlines()

            # Create the output file name
            output_file = os.path.join(output_dir, filename.replace(".txt", "_compiled.txt"))

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


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Compile a list of remote text files")
    parser.add_argument("input_dir", help="The directory containing the input files")
    args = parser.parse_args()

    # Compile all files in the input directory
    compile_files_in_dir(args.input_dir)
