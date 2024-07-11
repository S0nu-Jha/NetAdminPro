# server code
import socket

def send_command(command):
    client.send(command.encode())

def display_previous_config():
    print("Previous Network Configuration:")
    send_command("get_config")
    previous_config = client.recv(4096).decode()
    print(previous_config)

def main():
    while True:
        print("\n1. Display Previous Configuration")
        print("2. Change DNS")
        print("3. Change IP")
        print("4. Block Internet")
        print("5. Allow Internet")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            display_previous_config()

        elif choice == '2':
            new_dns = input("Enter the new DNS: ")
            send_command(f"change_dns:{new_dns}")

        elif choice == '3':
            new_ip = input("Enter the new IP: ")
            send_command(f"change_ip:{new_ip}")

        elif choice == '4':
            send_command("block")

        elif choice == '5':
            send_command("allow")

        elif choice == '6':
            send_command("exit")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.0.106', 9098))  # Change the port if needed
    server.listen(1)
    print("Waiting for a connection...")
    client, addr = server.accept()
    print(f"Connection from: {addr}")

    try:
        main()
    finally:
        client.close()
        server.close()
