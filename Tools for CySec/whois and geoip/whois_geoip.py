import socket
import whois
import requests

def get_geoip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        return f"{response['country']} - {response['city']} - {response['isp']}"
    except:
        return "GeoIP failed"

def main():
    domain = input("Enter domain: ")
    try:
        ip = socket.gethostbyname(domain)
        print(f" IP: {ip}")
        print(f" GeoIP Info: {get_geoip(ip)}")

        w = whois.whois(domain)
        print("\n WHOIS:")
        print(f"  Registrar: {w.registrar}")
        print(f"  Creation Date: {w.creation_date}")
        print(f"  Expiry Date: {w.expiration_date}")
        print(f"  Name Servers: {w.name_servers}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
