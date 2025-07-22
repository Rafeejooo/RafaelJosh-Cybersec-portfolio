import socket

def sub_enum(domain, wordlist_path):
    print(f" Enumerating subdomains for: {domain}")
    with open(wordlist_path, "r") as file:
        for line in file:
            subdomain = line.strip() + "." + domain
            try:
                ip = socket.gethostbyname(subdomain)
                print(f"[+] {subdomain} -> {ip}")
            except socket.gaierror:
                continue

if __name__ == "__main__":
    domain = input("Enter target domain (e.g. example.com): ")
    wordlist = input("Enter subdomain wordlist (e.g. sublist.txt): ")
    sub_enum(domain, wordlist)
