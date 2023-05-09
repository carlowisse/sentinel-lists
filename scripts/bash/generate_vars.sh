#!/bin/bash

# Set the path to the directory to be searched
dir=$1

# Set the path to the directory where the output script will be placed
output_dir=../vars

# Create the output directory if it doesn't already exist
mkdir -p "$output_dir"

# Loop through each immediate child directory of the specified directory
for child_dir in "$dir"/*/; do
    # Get the name of the child directory
    child_dir_name=$(basename "$child_dir")

    # Loop through each subdirectory of the child directory
    for sub_dir in "$child_dir"/*/; do
        # Get the name of the subdirectory
        sub_dir_name=$(basename "$sub_dir")

        # Count the number of .txt files in the subdirectory
        sub_dir_txt_file_count=$(ls "$sub_dir"/*.txt 2>/dev/null | wc -l)

        # Set a variable with the name of the subdirectory and the count of .txt files
        var_name="${sub_dir_name}"
        var_value="$sub_dir_txt_file_count"

        # Append the variable to the generated .sh file for the child directory
        echo "export $var_name=$var_value" >>"${output_dir}/${child_dir_name}.sh"
    done
done
