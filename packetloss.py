import socket
import random

# Cấu hình
LISTEN_IP = "127.0.0.1"       # Proxy nhận gói UDP tại localhost
LISTEN_PORT = 12345           # Cổng nhận gói UDP từ FFmpeg

FORWARD_IP = "10.136.154.215"      # Proxy gửi lại gói UDP tới localhost
FORWARD_PORT = 1234           
DISCARD_RATE = 0.06     

# Tạo socket nhận và bind địa chỉ
sock_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_in.bind((LISTEN_IP, LISTEN_PORT))

# Tạo socket gửi
sock_out = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Proxy UDP discard chạy trên {LISTEN_IP}:{LISTEN_PORT}, discard rate {DISCARD_RATE*100:.1f}%")

while True:
    data, addr = sock_in.recvfrom(65535)
    if random.random() > DISCARD_RATE:
        sock_out.sendto(data, (FORWARD_IP, FORWARD_PORT))
    else:
        print(f"Đã bỏ 1 gói từ {addr}")