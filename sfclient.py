import socket
import tkinter as tk

def receive_file(conn):
    file_size = int(conn.recv(1024).decode())
    file_name = conn.recv(1024).decode()
    
    with open(file_name, 'wb') as file:
        received = 0
        while received < file_size:
            data = conn.recv(1024)
            file.write(data)
            received += len(data)
    
    print("File received successfully.")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9097))  # Replace with the server's host and port

receive_file(client)

