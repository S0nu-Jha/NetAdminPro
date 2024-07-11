import socket
import sys

def send_command(client_socket, command):
    client_socket.send(command.encode())

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.43.66', 5033))
    server.listen(1)

    print("Server listening on port 5053")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        if len(sys.argv) != 2:
            sys.exit(1)

        user_input = sys.argv[1]
        

        # Receive the URL to block from the server
        url_to_block = user_input

        # Send the command to the client to block the URL
        send_command(client_socket, f"BLOCK {url_to_block}")

        client_socket.close()

if __name__ == "__main__":
    main()
