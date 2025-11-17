import socket

s = socket.socket()
s.bind(('0.0.0.0', 9999))
s.listen(1)
print("📡 Waiting for incoming screenshot...")

while True:
    conn, addr = s.accept()
    print(f"Connected with {addr}")
    data = b""
    while True:
        packet = conn.recv(1024)
        if not packet:
            break
        data += packet

    with open("received_screenshot.png", "wb") as f:
        f.write(data)

    print("✅ Screenshot received and saved as 'received_screenshot.png'")
    conn.close()