import socket
import os

def receive_pdf():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.43.66', 4444))
    server.listen(1)
    conn, addr = server.accept()

    with conn:
        print(f"Connection from {addr}")
        pdf_data = b""

        while True:
            data = conn.recv(1024)
            if not data:
                break
            pdf_data += data

        with open("received_logs.pdf", "wb") as file:
            file.write(pdf_data)

receive_pdf()

def open_pdf(file_path):
    os.system(f"start {file_path}")


open_pdf("received_logs.pdf")
