import argparse
import re
import requests
import subprocess
import sys
from collections import defaultdict
from tqdm import tqdm
from tabulate import tabulate
from termcolor import colored

# Extract file types based on user-supplied inputs

def obtain_file_extension(url):
    match = re.search(r'([a-zA-Z0-9_-]+)(\.[a-zA-Z0-9]+)$', url)
    return match.group(2)[1:].lower() if match else None

# Automated file-based URLs - when user supplies a domain - crawling is executed
def extract_urls_from_gau(target_url):
    urls = []
    try:
        result = subprocess.run(["gau", target_url], capture_output=True, text=True, check=True)
        urls = result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(colored(f"Error running GAU: {e}", "red"))
    return urls

# Read file inputs - if user selects "-f" option

def discover_file_urls(file_path):
    urls = []
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(colored(f"File {file_path} not found!", "red"))
    return urls

# Response validation for unique URL-based file extensions

def validate_urls(url_list):
    valid_urls, invalid_urls = [], []
    for url in tqdm(url_list, desc="Progressing Requests", unit="URL"):
        try:
            response = requests.get(url, timeout=10)
            ext = obtain_file_extension(url)
            if response.status_code == 200:
                valid_urls.append((url, ext))
            else:
                invalid_urls.append((url, ext, response.status_code))
        except requests.exceptions.RequestException as e:
            invalid_urls.append((url, None, str(e)))
    return valid_urls, invalid_urls

# Organize file inputs

def organize_results(valid_urls, invalid_urls):
    valid_dict = defaultdict(list)
    for url, ext in valid_urls:
        valid_dict[ext].append(url)

    invalid_list = [(ext if ext else "Unknown", url, status) for url, ext, status in invalid_urls]

    print(colored("\n[+] Valid URLs (200 OK Response):", "green"))
    if valid_dict:
        table_data = [[file_type, "\n".join(urls)] for file_type, urls in valid_dict.items()]
        print(tabulate(table_data, headers=["File Type", "URLs"], tablefmt="grid"))
    else:
        print(colored("[-] No valid URLs discovered.", "red"))

    print(colored("\n[!] Invalid URLs:", "yellow"))
    if invalid_list:
        print(tabulate(invalid_list, headers=["File Type", "URL", "Status"], tablefmt="grid"))
    else:
        print(colored("[-] No invalid URLs found.", "red"))

def main():

    # Argparse development for CLI 
    
    parser = argparse.ArgumentParser(description="Extract and validate URLs from GAU or a file")
    parser.add_argument('-u', '--url', help="Single target URL to extract with GAU")
    parser.add_argument('-f', '--file', help="File containing URLs")
    args = parser.parse_args()

    urls = []

    if args.url:
        print(colored(f"[*] Running GAU on {args.url}...", "cyan"))
        urls = extract_urls_from_gau(args.url)
    elif args.file:
        print(colored(f"[*] Reading URLs from {args.file}...", "cyan"))
        urls = discover_file_urls(args.file)
    else:
        print(colored("[-] Please provide either a URL (-u) or a file (-f).", "red"))
        sys.exit(1)

    if not urls:
        print(colored("[-] No URLs found to process.", "red"))
        sys.exit(1)

    print(colored("[+] Processing URLs...", "green"))
    valid_urls, invalid_urls = validate_urls(urls)
    organize_results(valid_urls, invalid_urls)

if __name__ == "__main__":
    main()
