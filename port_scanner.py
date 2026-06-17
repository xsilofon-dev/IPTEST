import socket

target_ip = "91.215.144.123"
# Список поширених портів для перевірки
ports_to_check = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 8080]

print(f"Сканування портів для {target_ip}...")

for port in ports_to_check:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        print(f"Порт {port}: Відкритий")
    sock.close()

print("Сканування завершено.")
