import socket
import tkinter as tk
from tkinter import filedialog
import os

def send_file():
    file_path = filedialog.askopenfilename()
    file_name = file_path.split("/")[-1]
    file_size = os.path.getsize(file_path)
    
    connection.send(str(file_size).ljust(1024).encode())
    connection.send(file_name.encode())

    with open(file_path, "rb") as file:
        file_data = file.read(1024)
        while file_data:
            connection.send(file_data)
            file_data = file.read(1024)
    print("File sent successfully.")

def start_server():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9098))  # Replace with your desired host and port
    server.listen(1)
    print("Waiting for a connection...")
    conn, addr = server.accept()
    print("Connection from:", addr)
    return conn

def close_server():
    server.close()
    print("Server connection closed.")

root = tk.Tk()
root.title("File Sender")

connection = start_server()

file_button = tk.Button(root, text="File", command=send_file)
file_button.pack(padx=20, pady=20)

close_button = tk.Button(root, text="Close Server", command=close_server)
close_button.pack(padx=20, pady=20)

root.mainloop()
