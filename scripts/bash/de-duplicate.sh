#!/bin/bash

# Define the root directory of your folder structure
root_dir="../lists/regexes"

# Use find to locate all the .txt files and loop through them
find "${root_dir}" -type f -name "*.txt" | while read -r file; do

    # Get the initial line count
    before=$(wc -l <"${file}")

    # Create a temporary file to hold the unique entries for this file
    temp_file=$(mktemp)

    # Use awk to read each line in the file and append to the temporary file if it hasn't been seen before
    awk '!seen[$0]++' "${file}" >"${temp_file}"

    # Use comm to find lines that are in the previous file and not in this file
    prev_file="${file}.prev"
    if [ -f "${prev_file}" ]; then
        comm -23 "${prev_file}" "${temp_file}" >"${temp_file}.diff"
        mv "${temp_file}.diff" "${temp_file}"
    fi

    # Remove the trailing newline from the temporary file
    printf %s "$(cat "${temp_file}")" >"${temp_file}"

    # Overwrite the original file with the contents of the temporary file
    mv "${file}" "${file}.prev"
    mv "${temp_file}" "${file}"

    # Get the final line count
    after=$(wc -l <"${file}")

    # Print the line counts for this file
    echo "Processed ${file}: ${before} -> ${after} lines"

done

# Get the overall line count
total_before=$(find "${root_dir}" -type f -name "*.txt" -exec cat {} + | wc -l)
total_after=$(find "${root_dir}" -type f -name "*.txt" -exec awk '!seen[$0]++' {} + | wc -l)

# Print the overall line counts
echo "Overall line count: ${total_before} -> ${total_after} lines"

# Delete the .prev files
find "${root_dir}" -type f -name "*.prev" -delete

# Delete empty .txt files
find "${root_dir}" -type f -name "*.txt" -size 0 -delete
