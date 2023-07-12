import os, re, sys, ipaddress
from globals import domain_folder_path


### REMOVE COMMENTS ###
def remove_comments(lines):
    comment_regex = r"^\s*(##|!#|!!|//|/\*).*$"
    return [line for line in lines if not re.match(comment_regex, line)]


### REMOVE NON DOMAINS ###
def remove_non_domains(lines):
    DOMAIN_REGEX = re.compile(r"^(?!-)[a-zA-Z0-9-]{0,63}(\.[a-zA-Z0-9-]{0,63})*\.[a-zA-Z]{2,63}$")
    return [line for line in lines if bool(DOMAIN_REGEX.match(line))]


### REMOVE NON ASCII ###
def remove_non_ascii(lines):
    return [line for line in lines if all(ord(char) < 128 for char in line)]


### REMOVE IPS ###
def remove_ips(lines):
    return [line for line in lines if not is_valid_ip(line.strip())]


def is_valid_ip(line):
    try:
        ipaddress.ip_address(line)
        return True
    except ValueError:
        return False


### REMOVE EMPTY LINES ###
def remove_empty_lines(lines):
    return [line for line in lines if line.strip()]


### REMOVE WHITESPACE ###
def remove_whitespace(lines):
    return [line.strip() for line in lines]


### TO LOWERCASE ###
def to_lowercase(lines):
    return [line.lower() for line in lines]


### for each file in the directory (recursive) run the cleanup functions and make sure the lines stay in the same order ###
def process_directory(directory_path, dry_run):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".txt"):
                ### GET INITIAL COUNT ###
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    lines = f.readlines()
                    initial_count = len(lines)

                ### GET FILENAME ###
                filename = file_path.split("/")[-1].split(".")[0]

                print("FILE:", filename)
                print("BEFORE:", initial_count)

                ### FORMAT ###
                cleaned_lines = remove_whitespace(lines)
                cleaned_lines = to_lowercase(cleaned_lines)

                ### REMOVE EMPTY LINES ###
                cleaned_lines = remove_empty_lines(cleaned_lines)
                empty_lines_removed_count = initial_count - len(cleaned_lines)
                print("Empty Lines:", empty_lines_removed_count if empty_lines_removed_count > 0 else "NONE")

                ### REMOVE COMMENTS ###
                cleaned_lines = remove_comments(cleaned_lines)
                comments_removed_count = initial_count - len(cleaned_lines)
                print("Comments Removed:", comments_removed_count if comments_removed_count > 0 else "NONE")

                ### REMOVE NON DOMAINS ###
                cleaned_lines = remove_non_domains(cleaned_lines)
                non_domains_removed_count = initial_count - len(cleaned_lines)
                print("Non Domains Removed:", non_domains_removed_count if non_domains_removed_count > 0 else "NONE")

                ### REMOVE NON ASCII ###
                cleaned_lines = remove_non_ascii(cleaned_lines)
                non_ascii_removed_count = initial_count - len(cleaned_lines)
                print("Non ASCII Removed:", non_ascii_removed_count if non_ascii_removed_count > 0 else "NONE")

                ### REMOVE IPS ###
                cleaned_lines = remove_ips(cleaned_lines)
                ips_removed_count = initial_count - len(cleaned_lines)
                print("IPs Removed:", ips_removed_count if ips_removed_count > 0 else "NONE")

                print("AFTER:", len(cleaned_lines))

                print("--------------------")

                # Write updated lines to file if not dry run
                if not dry_run:
                    with open(file_path, "w") as f:
                        f.writelines("\n".join(cleaned_lines))


if __name__ == "__main__":
    directory_path = domain_folder_path
    dry_run = False

    if len(sys.argv) == 2 and sys.argv[1] == "--dry":
        dry_run = True

    process_directory(directory_path, dry_run)
