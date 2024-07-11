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
from PySide2.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QPlainTextEdit, QMessageBox
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt 
import tkinter as tk
from tkinter import Text
import tkinter as tk
import socket
import threading

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

class SecondServer(Thread):
    def __init__(self, ip, port, text_browser, main_ui_instance):
        super().__init__()
        self.ip = ip
        self.port = port
        self.text_browser = text_browser
        self.main_ui_instance = main_ui_instance  # Pass the MainUi instance

    def run(self):
        try:
            print("[SERVER 2]: STARTED")
            sock = socket.socket()
            sock.bind((self.ip, self.port))
            sock.listen()
            self.main_ui_instance.conn, addr = sock.accept()  # Update the connection attribute
            print(f"[SERVER 2]: ACCEPTED CONNECTION FROM {addr}")

            while True:
                data = self.main_ui_instance.conn.recv(1024)
                data = data.decode()
                if data:
                    self.text_browser.insertPlainText(data + '\n')
                    show_popup(data)
        except Exception as e:
            print(f"[SERVER 2]: Failed to start server: {e}")


def show_popup(data):
    if not hasattr(show_popup, "popup"):
        show_popup.popup = tk.Tk()
        show_popup.popup.title("Command Result")
        show_popup.popup.geometry("500x300")
        show_popup.result_text = Text(show_popup.popup, wrap=tk.WORD, height=10, width=60)
        show_popup.result_text.pack(pady=10)

    # Clear previous content
    show_popup.result_text.delete(1.0, tk.END)
    # Insert new content
    show_popup.result_text.insert(tk.END, data)
    # Update the Tkinter window
    show_popup.popup.update_idletasks()

class MainUi(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # Button and LineEdit for Second Server
        self.ui.RAStartServer2Bttn.clicked.connect(self.StartSecondServer)
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

        # LineEdit and Button for Command
        self.ui.RASendCommandBttn.clicked.connect(self.sendCommand)
        # TextBrowser for Displaying Command Output
        self.command_output_browser = QPlainTextEdit(self.ui.RAMainFrame)
        self.command_output_browser.setGeometry(QRect(120, 30, 291, 311))

        # Additional attributes for the server socket and connection
        self.sock = None
        self.conn = None

        # Additional attribute for the second server thread
        self.second_server_thread = None

    def ServerStarted(self):
        try:
            print("[SERVER]: STARTED")
            self.sock = socket.socket()  # Assign to the class attribute
            ip_address = self.ui.RAIPLine.text()
            port_text = self.ui.RAPortLine.text()

            if not ip_address or not port_text:
                QMessageBox.warning(self, "Warning", "Please enter both an IP address and a port number.")
                return

            # Validate and parse IP address
            try:
                socket.inet_pton(socket.AF_INET, ip_address)
            except socket.error:
                QMessageBox.warning(self, "Warning", "Please enter a valid IPv4 address.")
                return

            # Validate and parse port number
            try:
                port_number = int(port_text)
                if not 0 < port_number < 65536:
                    raise ValueError("Port number must be between 1 and 65535")
            except ValueError as e:
                QMessageBox.warning(self, "Warning", str(e))
                return

            self.sock.bind((ip_address, port_number))
            self.sock.listen()
            self.conn, addr = self.sock.accept()

            # Start the RemoteDesktop window with the established connection
            remote_desktop_window = RemoteDesktop(self.conn, addr)
            remote_desktop_window.show()

        except Exception as e:
            QMessageBox.warning(self, "Warning", f"Failed to start server: {e}")

    def StartSecondServer(self):
        try:
            print("[SERVER 2]: START BUTTON CLICKED")
            ip_address = self.ui.RAIP2Line.text()
            port_text = self.ui.RA2PortLine.text()

            if not ip_address or not port_text:
                QMessageBox.warning(self, "Warning", "Please enter both an IP address and a port number for the second server.")
                return

            # Validate and parse IP address
            try:
                socket.inet_pton(socket.AF_INET, ip_address)
            except socket.error:
                QMessageBox.warning(self, "Warning", "Please enter a valid IPv4 address for the second server.")
                return

            # Validate and parse port number
            try:
                port_number = int(port_text)
                if not 0 < port_number < 65536:
                    raise ValueError("Port number for the second server must be between 1 and 65535")
            except ValueError as e:
                QMessageBox.warning(self, "Warning", str(e))
                return

            # Creating the second server thread with the updated code
            self.second_server_thread = SecondServer(ip_address, port_number, self.command_output_browser, self)
            self.second_server_thread.start()

        except Exception as e:
            QMessageBox.warning(self, "Warning", f"Failed to start second server: {e}")

    def sendCommand(self):
        try:
            if self.conn:
                message = self.ui.RACommandLine.text()
                self.conn.send(message.encode())
            else:
                QMessageBox.warning(self, "Warning", "No connection available.")
        except Exception as e:
            print(f"Error while sending command: {e}")

    def closeEvent(self, event):
        try:
            if self.sock:
                self.sock.close()  # Close the server socket
        except Exception as e:
            print(f"Error while closing the server: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUi()
    window.show()
    sys.exit(app.exec_())
