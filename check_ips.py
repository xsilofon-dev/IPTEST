import socket
import ipaddress

# ANSI кольори
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def check_ip(ip_str):
    # Якщо це CIDR (наприклад, 172.217.0.0/16), беремо мережеву адресу
    try:
        if '/' in ip_str:
            net = ipaddress.ip_network(ip_str, strict=False)
            target = str(net.network_address)
        else:
            target = ip_str
        
        # Перевірка порту 443
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, 443))
        sock.close()
        return result == 0, target
    except Exception:
        return False, ip_str

def main():
    try:
        with open("IPTEST/ips.txt", "r") as f:
            ips = [line.strip() for line in f if line.strip()]

        print(f"{'Target':<20} | {'Status'}")
        print("-" * 35)

        for ip_str in ips:
            is_online, target = check_ip(ip_str)
            # Вивід
            if is_online:
                print(f"{ip_str:<20} | {GREEN}● Online ({target}){RESET}")
            else:
                print(f"{ip_str:<20} | {RED}● Offline ({target}){RESET}")
    except FileNotFoundError:
        print("Помилка: Файл IPTEST/ips.txt не знайдено.")

if __name__ == "__main__":
    main()
