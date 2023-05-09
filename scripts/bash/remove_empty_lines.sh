#!/bin/bash

# Check if a directory was given as an argument, otherwise use the current directory
if [ $# -eq 0 ]; then
    dir="."
else
    dir=$1
fi

# Recursively search through the directory for .txt files
find "$dir" -type f -name "*.txt" -print0 | while IFS= read -r -d '' file; do

    # Remove empty lines (including the last one) from the file using sed
    sed -i '/^[[:space:]]*$/d' "$file"

    # Remove the newline character from the end of the file (if it exists)
    sed -i '/^$/d' "$file"

done
