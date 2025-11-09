import socket

UDP_IP = "0.0.0.0"   # слухає всі інтерфейси
UDP_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(1.0)

print(f"StatsD-server started on port {UDP_PORT} (Ctrl+C to close)\n")

try:
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(f"[{addr}] {data.decode('utf-8')}")
        except socket.timeout:
            continue
except KeyboardInterrupt:
    sock.close()