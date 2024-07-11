from ui_MainUi import *
from Custom_Widgets.Widgets import *
import socket
from os import getlogin
from PIL import Image
import io
import numpy as np
from random import randint
import pyautogui
from threading import Thread
import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QAction, QMessageBox
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt
from subprocess import Popen


class RemoteDesktop(QMainWindow):
    updateImageSignal = Signal(bytes)

    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr
        self.initUI()

    def changeImage(self):
        try:
            print("[SERVER]: CONNECTED: {0}!".format(self.addr[0]))
            while True:
                img_bytes = self.conn.recv(9999999)
                self.updateImageSignal.emit(img_bytes)
        except ConnectionResetError:
            self.conn.close()

    def updateImage(self, img_bytes):
        pixmap = QPixmap()
        pixmap.loadFromData(img_bytes)
        self.label.setScaledContents(True)
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(pixmap)

    def initUI(self):
        self.label = QLabel(self)
        self.label.resize(self.width(), self.height())
        self.setGeometry(QRect(pyautogui.size()[0] // 4, pyautogui.size()[1] // 4, 800, 450))
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("[SERVER] Remote Desktop: " + str(randint(99999, 999999)))
        self.start = Thread(target=self.changeImage, daemon=True)
        self.start.start()

        self.updateImageSignal.connect(self.updateImage)


class MainUi(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # Button and LineEdit for Second Server

        # Connect the first server's button to its functionality
        self.ui.RAStartserverBttn.clicked.connect(self.ServerStarted)
        # Connect other buttons to their functionality
        self.ui.RANextBttn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.SharedFileTransferPage))
        self.ui.RAPrevBttn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.OtherModulePage))
        self.ui.SFPrevBttn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.RemoteAccessPage))
        self.ui.SFNextBttn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.NetworkConfigurationPage))
        self.ui.NCPrevBttn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.SharedFileTransferPage))
        self.ui.NCNextBttn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.BrowsingControlPage))
        self.ui.BCPrevBttn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.NetworkConfigurationPage))
        self.ui.BCNextBttn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.LogFilePage))
        self.ui.LogPrevBttn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.BrowsingControlPage))
        self.ui.LogNextBttn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.OtherModulePage))
        self.ui.OMPrevBttn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.LogFilePage))
        self.ui.OMNextBttn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.RemoteAccessPage))
        self.ui.RASendCommandBttn.clicked.connect(self.run_second_file)
        self.ui.SFSelectFileBttn.clicked.connect(self.select_file)
        self.ui.SFSendFileBttn.clicked.connect(self.send_file)
        self.ui.BCBlockUrlBttn.clicked.connect(self.run_another_file)
        

    def ServerStarted(self):
        print("[SERVER]: STARTED")
        self.sock = socket.socket()  # Assign to the class attribute
        ip_address = self.ui.RAIPLine.text()
        port_text = self.ui.RAPortLine.text()

        if not ip_address or not port_text:
            QMessageBox.warning(self, "Warning", "Please enter both an IP address and a port number.")
            return

        try:
            # Validate and parse IP address
            socket.inet_pton(socket.AF_INET, ip_address)
        except socket.error:
            QMessageBox.warning(self, "Warning", "Please enter a valid IPv4 address.")
            return

        try:
            # Validate and parse port number
            port_number = int(port_text)
            if not 0 < port_number < 65536:
                raise ValueError("Port number must be between 1 and 65535")
        except ValueError as e:
            QMessageBox.warning(self, "Warning", str(e))
            return

        try:
            self.sock.bind((ip_address, port_number))
            self.sock.listen()
            global conn, addr
            conn, addr = self.sock.accept()

            # Start the RemoteDesktop window with the established connection
            remote_desktop_window = RemoteDesktop(conn, addr)
            remote_desktop_window.show()

        except Exception as e:
            QMessageBox.warning(self, "Warning", f"Failed to start server: {e}")
            
    def run_second_file(self):
        ip_address = self.ui.RAIP2Line.text()
        port = self.ui.RA2PortLine.text()

        if not ip_address or not port:
            QMessageBox.warning(self, "Warning", "Please enter both an IP address and a port number.")
            return

        try:
            # Validate and parse IP address
            socket.inet_pton(socket.AF_INET, ip_address)
        except socket.error:
            print(f"Invalid IP address: {ip_address}")
            QMessageBox.warning(self, "Warning", "Please enter a valid IPv4 address.")
            return

        try:
            # Validate and parse port number
            port_number = int(port)
            if not 0 < port_number < 65536:
                raise ValueError("Port number must be between 1 and 65535")
        except ValueError as e:
            print(f"Invalid port number: {port}")
            QMessageBox.warning(self, "Warning", str(e))
            return

        # Run the second file with the provided IP address and port
        try:
            print(f"Running with IP: {ip_address}, Port: {port}")
            Popen(['python', 'D:\\NetAdminPro\\SendCommandServer.py', ip_address, port], shell=True)
        except Exception as e:
            print(f"Error running second file: {str(e)}")
            QMessageBox.warning(self, "Warning", f"Error running second file: {str(e)}")
            
            
            
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*);;Text Files (*.txt)")

        if file_path:
            self.ui.SFFileSelectLine.setText(file_path)
            self.file_path = file_path

    def send_file(self):
        try:
            if not hasattr(self, 'file_path') or not self.file_path:
                QMessageBox.warning(self, "Warning", "Please select a file.")
                return

            with open(self.file_path, 'rb') as file:
                file_data = file.read()

            # Replace 'server_ip' and 'server_port' with your server details
            server_ip = self.ui.RAIP2Line.text()
            server_port = self.get_server_port()
            print(server_port)

            if not server_ip or not server_port:
                QMessageBox.warning(self, "Warning", "Please enter both an IP address and a port number.")
                return

            try:
                # Validate and parse IP address
                socket.inet_pton(socket.AF_INET, server_ip)
            except socket.error:
                print(f"Invalid IP address: {server_ip}")
                QMessageBox.warning(self, "Warning", "Please enter a valid IPv4 address.")
                return

            # Create a server socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.bind((server_ip, server_port))
                server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                server_socket.listen(1)
                print(f"Server is listening on {server_ip}:{server_port}")

                # Wait for a client to connect
                client_socket, addr = server_socket.accept()
                print(f"Accepted connection from {addr}")

        # Extract file name and size from file path
            original_file_name = self.file_path.split("/")[-1]
            file_size = os.path.getsize(self.file_path)

            # Send file metadata (original name and size)
            client_socket.sendall(original_file_name.encode('utf-8') + b'\x00')
            client_socket.sendall(file_size.to_bytes(8, byteorder='big'))

            # Send file data to the client
            client_socket.sendall(file_data)

            print("File sent successfully.")
        except Exception as e:
            print(f"Error sending file: {e}")

    def get_server_port(self):
        try:
            port = int(self.ui.RA2PortLine.text())
            if not (0 <= port <= 65535):
                raise ValueError("Port number must be between 0 and 65535")
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid port number. Using default port.")
            port = None

        # Subtract 1 from the port number if it's a valid port
        if port is not None:
            port -= 1

        return port
    
    def run_another_file(self):
        try:
            user_input = self.ui.BCUrlBlockLine.text()
            # Replace 'path/to/your/other/file.py' with the actual file path
            Popen(['python', 'D:\\NetAdminPro\\bcserver.py', user_input], shell=True)
            # Replace 'path/to/your/other/file.py' with the actual file path
            Popen(['python', 'D:\\NetAdminPro\\bcserver.py'], shell=True)
        except Exception as e:
            print(f"Error running the other file: {str(e)}")
         
        
    def closeEvent(self, event):
            # Implement logic to close the server gracefully
        print("Closing the server...")
        try:
                if self.sock:
                    self.sock.close()  # Close the server socket
                # Perform any additional cleanup operations

        except Exception as e:
                print(f"Error while closing the server: {e}")
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUi()
    window.show()
    sys.exit(app.exec())
