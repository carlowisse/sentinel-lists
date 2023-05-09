find ./lists/domains -type f -name '*.txt' -exec gawk -i inplace '!seen[$0]++' {} +
