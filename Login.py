import os
import sys
import sqlite3
import subprocess
import threading
from twilio.rest import Client
import random


# Create a SQLite database connection
conn = sqlite3.connect("Account.db")
cursor = conn.cursor()

# Create a table to store user information
cursor.execute("""
CREATE TABLE IF NOT EXISTS UsersInfo (
    UserName TEXT PRIMARY KEY,
    Email TEXT,
    MobileNum INT,
    Password TEXT
)
""")
conn.commit()
conn.close()


account_sid = 'AC5a165644f9e8eb565721d7592d827612'
auth_token = 'd0d7564c6eb0d3b4d273f66da9893e1d'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Your Twilio phone number
twilio_phone_number = '+18582408550'


def send_verification_code(phone_number):
        # Generate a random six-digit verification code
        verification_code = ''.join(random.choices('0123456789', k=6))

        # Send the verification code via SMS
        message = client.messages.create(
            body=f'Your verification code for NetAdminPro software is: {verification_code}',
            from_=twilio_phone_number,
            to=phone_number
        )

        return verification_code





from ui_LoginInterface import *

from Custom_Widgets.Widgets import *




class CodeInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Verification Code")
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.code_input_box = QLineEdit()
        self.code_input_box.setPlaceholderText("Enter the verification code")
        
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.accept)
        
        layout.addWidget(self.code_input_box)
        layout.addWidget(submit_button)





class Login(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles = {
            "D:\\NetAdminPro\\RegisterLoginStyle.json"
            }) 

        self.show() 
        
        self.ui.RegisterBtn.clicked.connect(self.register)
        self.ui.LoginBtn.clicked.connect(self.authenticate)
          


    def register(self):
        SignUp_UserName_Input = self.ui.SignUpUserNameInput.text()
        SignUp_Email_Input = self.ui.SignUpEmailInput.text()
        SignUp_Password_Input = self.ui.SignUpPasswordInput.text()
        SignUp_ConPassword_Input = self.ui.SignUpConPasswordInput.text()
        SignUp_MobileNum_Input = self.ui.SignUpMobileNumInput.text()
        self.ui.LoginWidget.setCurrentWidget(self.ui.LoginPage)

        if not SignUp_UserName_Input or not SignUp_Email_Input or not SignUp_Password_Input or not SignUp_ConPassword_Input or not SignUp_MobileNum_Input:
            QMessageBox.warning(self, "Registration Failed", "Please enter all the credentials.")
        else:
            # Define a list of allowed email domains
            allowed_domains = ["gmail.com", "outlook.com", "aol.com", "protonmail.com", "proton.me", "zohomail.in", "icloud.com", "yahoo.com", "myyahoo.com"]

            # Extract the domain from the provided email address
            email_domain = SignUp_Email_Input.split('@')[-1]

            # Check if the email domain is in the allowed list
            if email_domain not in allowed_domains:
                QMessageBox.warning(self, "Registration Failed", "Email domain is not allowed.")
                return

            try:
                conn = sqlite3.connect("Account.db")
                cursor = conn.cursor()

                # Check if the user already exists
                cursor.execute("SELECT UserName FROM UsersInfo WHERE UserName = ?", (SignUp_UserName_Input,))
                existing_user = cursor.fetchone()

                if existing_user:
                    QMessageBox.warning(self, "Registration Failed", "Username already exists.")
                elif SignUp_Password_Input != SignUp_ConPassword_Input:
                    QMessageBox.warning(self, "Registration Failed", "Password and Confirm Password do not match.")
                else:
                    # Send the verification code via SMS using Twilio
                    verification_code = send_verification_code(SignUp_MobileNum_Input)

                    code_input_dialog = CodeInputDialog(self)
                    result = code_input_dialog.exec_()

                    if result == QDialog.Accepted:
                        # Get the user's input from the QLineEdit
                        user_input = code_input_dialog.code_input_box.text()

                        # Check if the user-entered code matches the generated code
                        if user_input == verification_code:
                            # Insert the new user
                            cursor.execute("INSERT INTO UsersInfo (UserName, Email, Password, MobileNum) VALUES (?, ?, ?, ?)",
                                           (SignUp_UserName_Input, SignUp_Email_Input, SignUp_Password_Input, SignUp_MobileNum_Input))
                            conn.commit()
                            conn.close()
                            QMessageBox.information(self, "Registration Successful", "Registration successful!")
                        else:
                            QMessageBox.warning(self, "Registration Failed", "Invalid verification code. Registration failed.")

            except sqlite3.Error as e:
                print("SQLite error:", e)
                QMessageBox.warning(self, "Registration Failed", "Registration failed. Please try again.")


    def authenticate(self):
        Login_UserName_Input = self.ui.LoginUserNameInput.text()
        Login_Password_Input = self.ui.LoginPasswordInput.text()
        if not Login_UserName_Input or not Login_Password_Input:
            QMessageBox.warning(self, "Login Failed", "Please enter both username and password.")
            
    
        try:
            conn = sqlite3.connect("Account.db")
            cursor = conn.cursor()

            # Check if the user exists and the password matches
            cursor.execute("SELECT UserName, Password FROM UsersInfo WHERE UserName = ?", (Login_UserName_Input,))
            user_data = cursor.fetchone()

            if user_data:
                stored_password = user_data[1]
                if Login_Password_Input == stored_password:
                    QMessageBox.information(self, "Login Successful", "Welcome, " + Login_UserName_Input)
                    self.open_second_window()
                    # subprocess.Popen(["python", "D:\\NetAdminPro\\MainInterface.py"])
                    # self.close()
                    # Add code here to open your main interface window
                else:
                    QMessageBox.warning(self, "Login Failed", "Invalid password.")
            else:
                QMessageBox.warning(self, "Login Failed", "User not found.")

            conn.close()
        except sqlite3.Error as e:
            print("SQLite error:", e)
            QMessageBox.warning(self, "Login Failed", "Login failed. Please try again.")


    def open_second_window(self):
        try:
            # Replace 'second_script.py' with the actual name of your second script
            subprocess.Popen(['python', 'D:\\NetAdminPro\\main.py'])
            self.close()
        except Exception as e:
            print("Error running second script:", str(e))

    def run_second_script(self):
        try:
            # Replace 'second_script.py' with the actual name of your second script
            subprocess.run(['python', 'D:\\NetAdminPro\\main.py'], check=True)
        except subprocess.CalledProcessError:
            print("Error running second script")
    



     

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Login()
    window.show()
    sys.exit(app.exec_())

