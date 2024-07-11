import socket
import subprocess
import platform
import psutil
import traceback
import threading
import re

# Global variable to indicate whether to unblock the internet
unblock_event = threading.Event()

def apply_command(command):
    if command.startswith('change_dns'):
        new_dns = command.split(':')[1]
        change_dns(new_dns)
        return "DNS changed successfully."

    elif command.startswith('change_ip'):
        new_ip = command.split(':')[1]
        change_ip(new_ip)
        return "IP changed successfully."

    elif command.lower() == 'block':
        block_internet()
        return "Internet blocked successfully."

    elif command.lower() == 'allow':
        unblock_internet()
        return "Internet allowed successfully."

    else:
        return "Invalid command."

def change_dns(new_dns):
    # Modify DNS using platform-specific commands
    if platform.system().lower() == 'windows':
        subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'dns', 'name="Wi-Fi"', 'source=static', f'address={new_dns}'], capture_output=True, text=True)
    else:
        # For Linux, you can use resolvconf or modify /etc/resolv.conf
        subprocess.run(['sudo', 'resolvconf', '-a', 'Wi-Fi', '-i', 'address', new_dns], capture_output=True, text=True)

def get_default_gateway():
    # Get the default gateway using platform-specific commands
    if platform.system().lower() == 'windows':
        result = subprocess.run(['ipconfig'], capture_output=True, text=True)
        # Modify the regular expression to capture the correct default gateway information on Windows
        match = re.search(r'Default Gateway(?: .+)? : ([^\s]+)', result.stdout)
        if match:
            return match.group(1)
    else:
        result = subprocess.run(['ip', 'route'], capture_output=True, text=True)
        # Use regular expression to find the default gateway in the ip route output
        match = re.search(r'default via ([^\s]+)', result.stdout)
        if match:
            return match.group(1)

    return None

global gateway
gateway = get_default_gateway()
print(gateway)

def change_ip(new_ip):
    # Modify IP using platform-specific commands
    if platform.system().lower() == 'windows':
        # Modify the IP address directly
        a = subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'address', 'name="Wi-Fi"', 'source=static', f'address={new_ip}'], capture_output=True, text=True)
        print(a)

        # Get the default gateway and set it
        default_gateway = gateway
        print(default_gateway)
        if default_gateway:
            b = subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'address', 'name="Wi-Fi"', f'gateway={default_gateway}'], capture_output=True, text=True)
            print(b)
        else:
            print("Error: Unable to set default gateway")
    else:
        # Linux example, modify according to your distribution
        # Modify the IP address directly
        subprocess.run(['sudo', 'ifconfig', 'Wi-Fi', new_ip], capture_output=True, text=True)

        # Get the default gateway and set it
        default_gateway = get_default_gateway()
        if default_gateway:
            subprocess.run(['sudo', 'ip', 'route', 'add', 'default', 'via', default_gateway], capture_output=True, text=True)
        else:
            print("Error: Unable to set default gateway")


def block_internet():
    global unblock_event
    global blocked_processes

    # Clear the event to block the internet
    unblock_event.clear()

    # Create a list of processes to block
    processes_to_block = ['chrome.exe', 'msedge.exe', 'WinStore.App.exe']

    # Block Internet by suspending specific processes (platform-specific)
    blocked_processes = []

    # Suspend the target processes
    for proc in psutil.process_iter(['pid', 'name', 'ppid']):
        if proc.name() in processes_to_block:
            try:
                process = psutil.Process(proc.pid)
                process.suspend()
                blocked_processes.append(proc.pid)
                print(f"Suspended {proc.name()} with PID: {proc.pid}")
            except Exception as e:
                print(f"Error suspending {proc.name()}: {str(e)}")

    print("Internet blocked successfully.")

def unblock_internet():
    global unblock_event
    global blocked_processes

    # Set the event to unblock the internet
    unblock_event.set()

    # Resume the suspended processes
    for pid in blocked_processes:
        try:
            process = psutil.Process(pid)
            process.resume()
            print(f"Resumed process with PID: {pid}")
        except Exception as e:
            print(f"Error resuming process with PID: {pid}: {str(e)}")

    print("Internet unblocked successfully.")

def receive_and_apply_commands():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.0.106', 9098))  # Change the port if needed

    try:
        while True:
            command = client.recv(4096).decode()
            if command.lower() == 'exit':
                break

            response = apply_command(command)
            client.send(response.encode())

    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

    finally:
        client.close()

if __name__ == "__main__":
    receive_and_apply_commands()
