import requests

def dir_brute(url, wordlist):
    print(f" Scanning {url} ...")
    with open(wordlist, "r") as f:
        for line in f:
            path = line.strip()
            full_url = f"{url}/{path}"
            try:
                r = requests.get(full_url, timeout=3)
                if r.status_code == 200:
                    print(f"[+] Found: {full_url}")
            except requests.RequestException:
                continue

if __name__ == "__main__":
    target = input("Target URL (e.g., http://example.com): ").strip().rstrip('/')
    wordlist_path = input("Wordlist path (e.g., wordlist.txt): ").strip()
    dir_brute(target, wordlist_path)
