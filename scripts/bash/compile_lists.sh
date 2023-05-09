#!/bin/bash

# Check if a directory was given as an argument, otherwise use the current directory
if [ $# -eq 0 ]; then
    dir="."
else
    dir=$1
fi

# Get the name of the directory
dir_name=$(basename "$dir")

# Merge all .txt files in the directory
for file in "$dir"/*.txt; do
    if [ ! -f "$dir/merged.txt" ]; then
        # If the merged file does not exist yet, just copy the first file to it
        cp "$file" "$dir/merged.txt"
    else
        # Append the file to the end of the merged file, starting on a new line
        printf "\n" >>"$dir/merged.txt"
        cat "$file" >>"$dir/merged.txt"
        # Delete the original file that was merged, except for the file that has the name of the directory
        if [ "$file" != "$dir/merged.txt" ]; then
            rm "$file"
        fi
    fi
done

# Remove empty lines and final newline
sed -i -e '/^[[:space:]]*$/d' -e '${/^$/d;}' "$dir/merged.txt"

# Rename the merged file to the name of the directory
mv "$dir/merged.txt" "$dir/$dir_name.txt"

# Delete all other files except the merged file named after the directory
for file in "$dir"/*.txt; do
    if [ "$(basename "$file")" != "$dir_name.txt" ]; then
        rm "$file"
    fi
done

echo "Merged all .txt files in $dir into $dir/$dir_name.txt and removed all other merged files."
