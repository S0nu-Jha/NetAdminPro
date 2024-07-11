# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginInterfaceuoJUOp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomStackedWidget

import Loginresources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1040, 722)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1040, 722))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: ;\n"
"	background-image: url(:/image/images/bg.jpg);\n"
"}\n"
"#widget{\n"
"	background-color: rgb(9, 27, 68);\n"
"	border-radius:20px;\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgb(9, 10, 37);\n"
"	padding: 5px 3px;\n"
"	border-radius:5px;\n"
"	\n"
"}\n"
"QPushButton{\n"
"	background-color:  rgb(9, 10, 37);\n"
"	padding: 10px 5px;\n"
"	border-radius:5px;\n"
"}\n"
"#To_Login , #To_Register{\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(400, 700))
        self.widget.setMaximumSize(QSize(400, 700))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.LoginWidget = QCustomStackedWidget(self.widget)
        self.LoginWidget.setObjectName(u"LoginWidget")
        self.RegisterPage = QWidget()
        self.RegisterPage.setObjectName(u"RegisterPage")
        self.verticalLayout_3 = QVBoxLayout(self.RegisterPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.RegisterPage)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(95, 95))
        self.label.setMaximumSize(QSize(95, 95))
        self.label.setPixmap(QPixmap(u":/icons/Icons/user-plus.png"))

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.RegisterPage)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_3 = QLabel(self.RegisterPage)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame = QFrame(self.RegisterPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.SignUpUserNameInput = QLineEdit(self.frame)
        self.SignUpUserNameInput.setObjectName(u"SignUpUserNameInput")

        self.verticalLayout_4.addWidget(self.SignUpUserNameInput)

        self.SignUpEmailInput = QLineEdit(self.frame)
        self.SignUpEmailInput.setObjectName(u"SignUpEmailInput")

        self.verticalLayout_4.addWidget(self.SignUpEmailInput)

        self.SignUpMobileNumInput = QLineEdit(self.frame)
        self.SignUpMobileNumInput.setObjectName(u"SignUpMobileNumInput")

        self.verticalLayout_4.addWidget(self.SignUpMobileNumInput)

        self.SignUpPasswordInput = QLineEdit(self.frame)
        self.SignUpPasswordInput.setObjectName(u"SignUpPasswordInput")
        self.SignUpPasswordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.SignUpPasswordInput)

        self.SignUpConPasswordInput = QLineEdit(self.frame)
        self.SignUpConPasswordInput.setObjectName(u"SignUpConPasswordInput")
        self.SignUpConPasswordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.SignUpConPasswordInput)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.checkBox = QCheckBox(self.RegisterPage)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox)

        self.RegisterBtn = QPushButton(self.RegisterPage)
        self.RegisterBtn.setObjectName(u"RegisterBtn")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/log-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RegisterBtn.setIcon(icon)

        self.verticalLayout_3.addWidget(self.RegisterBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.To_Login = QPushButton(self.RegisterPage)
        self.To_Login.setObjectName(u"To_Login")
        font1 = QFont()
        font1.setUnderline(True)
        self.To_Login.setFont(font1)

        self.verticalLayout_3.addWidget(self.To_Login, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.label_4 = QLabel(self.RegisterPage)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.LoginWidget.addWidget(self.RegisterPage)
        self.LoginPage = QWidget()
        self.LoginPage.setObjectName(u"LoginPage")
        self.verticalLayout_6 = QVBoxLayout(self.LoginPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.LoginPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 100))
        self.label_5.setMaximumSize(QSize(100, 100))
        self.label_5.setPixmap(QPixmap(u":/icons/Icons/user-check.png"))

        self.verticalLayout_6.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.LoginPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_6.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.label_7 = QLabel(self.LoginPage)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 87, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.frame_2 = QFrame(self.LoginPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.LoginUserNameInput = QLineEdit(self.frame_2)
        self.LoginUserNameInput.setObjectName(u"LoginUserNameInput")

        self.verticalLayout_5.addWidget(self.LoginUserNameInput)

        self.LoginPasswordInput = QLineEdit(self.frame_2)
        self.LoginPasswordInput.setObjectName(u"LoginPasswordInput")
        self.LoginPasswordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.LoginPasswordInput)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.verticalSpacer_7 = QSpacerItem(20, 87, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_7)

        self.LoginBtn = QPushButton(self.LoginPage)
        self.LoginBtn.setObjectName(u"LoginBtn")
        self.LoginBtn.setIcon(icon)

        self.verticalLayout_6.addWidget(self.LoginBtn, 0, Qt.AlignHCenter)

        self.To_Register = QPushButton(self.LoginPage)
        self.To_Register.setObjectName(u"To_Register")
        self.To_Register.setFont(font1)

        self.verticalLayout_6.addWidget(self.To_Register, 0, Qt.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 87, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.label_6 = QLabel(self.LoginPage)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.LoginWidget.addWidget(self.LoginPage)

        self.verticalLayout_2.addWidget(self.LoginWidget)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignHCenter)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.LoginWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NetAdminPro", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter Your Information Below", None))
        self.SignUpUserNameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UserName", None))
        self.SignUpEmailInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.SignUpMobileNumInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mobile Number With ISD Code", None))
        self.SignUpPasswordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.SignUpConPasswordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Agree With Our Terms", None))
        self.RegisterBtn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.To_Login.setText(QCoreApplication.translate("MainWindow", u"Already Registered ? Login", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CC Anjani Jha", None))
        self.label_5.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Enter Your Information Below", None))
        self.LoginUserNameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UserName", None))
        self.LoginPasswordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.LoginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.To_Register.setText(QCoreApplication.translate("MainWindow", u"Not Registered ? Register", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CC Anjani Jha", None))
    # retranslateUi

