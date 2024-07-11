import tkinter as tk
import socket
import threading
import sys

def send_command():
    message = entry.get()
    conn.send(message.encode())

def receive_data():
    while True:
        data = conn.recv(1024)
        data = data.decode()
        if data:
            received_text.insert(tk.END, data + '\n')


if len(sys.argv) != 3:
    sys.exit(1)
ip_address = sys.argv[1]
port = int(sys.argv[2])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_address, port))
server.listen(1)

conn, addr = server.accept()

root = tk.Tk()
root.title("Server")

entry = tk.Entry(root)
entry.pack(padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_command)
send_button.pack(padx=10, pady=5)

received_text = tk.Text(root, height=70, width=90)
received_text.pack(padx=1, pady=1)

receive_data_thread = threading.Thread(target=receive_data)
receive_data_thread.daemon = True
receive_data_thread.start()

root.mainloop()
