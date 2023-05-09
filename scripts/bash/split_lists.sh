#!/bin/bash

DIR="$1"

# Recursively iterate over all files in the given directory
find "$DIR" -type f -print0 | while IFS= read -r -d '' file; do

    # Get the file size and line count
    filesize=$(stat -c%s "$file")
    linecount=$(wc -l <"$file")

    # Print the file info
    printf 'Processing: %s | %'d' | %s\n' "$file" "$linecount" "$(numfmt --to=iec-i --suffix=B --format='%.1f' $filesize)"
    echo '------------------------------'

    # Split the file if it's bigger than 10MB
    if [ "$filesize" -gt $((10 * 1024 * 1024)) ]; then
        split_size=$((10 * 1024 * 1024))
        prefix=$(basename "$file" .txt)

        # Split the file into parts
        split -l $((linecount / (filesize / split_size + 1))) --numeric-suffixes --additional-suffix=".txt" "$file" "$DIR/${prefix}_"

        # Get the size and line count of each part
        for part in "$DIR/${prefix}_"*; do
            part_size=$(stat -c%s "$part")
            part_linecount=$(wc -l <"$part")
            printf '%s | %'d' | %s\n' "$part" "$part_linecount" "$(numfmt --to=iec-i --suffix=B --format='%.1f' $part_size)"
        done

        # Remove the original file
        rm "$file"
    else
        printf 'File is smaller than 10MB\n'
    fi

    echo '------------------------------\n'
done
