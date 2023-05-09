#!/bin/bash

# Check if a directory was given as an argument, otherwise use the current directory
if [ $# -eq 0 ]; then
    dir="."
else
    dir=$1
fi

# Recursively loop through the directory and print the size of each file in human readable format
find $dir -type f -print0 | while read -d $'\0' file; do
    size=$(du -h "$file" | cut -f1)
    echo "$size $file"
done
