import socket

UDP_IP = "0.0.0.0"   # слухає всі інтерфейси
UDP_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"StatsD-server started on port {UDP_PORT} (Ctrl+C to close)\n")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"[{addr}] {data.decode('utf-8')}")