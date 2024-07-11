# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUiXBiWVd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Loginresources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1109, 836)
        icon = QIcon()
        icon.addFile(u":/image/images/AppLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
"}")
        MainWindow.setIconSize(QSize(30, 30))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(450, 700))
        self.widget.setMaximumSize(QSize(600, 800))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.stackedWidget.setFont(font)
        self.RemoteAccessPage = QWidget()
        self.RemoteAccessPage.setObjectName(u"RemoteAccessPage")
        self.verticalLayout_3 = QVBoxLayout(self.RemoteAccessPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.RANavFrame = QFrame(self.RemoteAccessPage)
        self.RANavFrame.setObjectName(u"RANavFrame")
        self.RANavFrame.setFrameShape(QFrame.StyledPanel)
        self.RANavFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.RANavFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.RAPrevBttn = QPushButton(self.RANavFrame)
        self.RAPrevBttn.setObjectName(u"RAPrevBttn")
        self.RAPrevBttn.setMinimumSize(QSize(0, 0))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/arrow-left-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RAPrevBttn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.RAPrevBttn, 0, Qt.AlignLeft|Qt.AlignTop)

        self.RANextBttn = QPushButton(self.RANavFrame)
        self.RANextBttn.setObjectName(u"RANextBttn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/arrow-right-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RANextBttn.setIcon(icon2)
        self.RANextBttn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.RANextBttn, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.RANavFrame)

        self.RALogo = QLabel(self.RemoteAccessPage)
        self.RALogo.setObjectName(u"RALogo")
        self.RALogo.setPixmap(QPixmap(u":/icons/Icons/airplay.png"))

        self.verticalLayout_3.addWidget(self.RALogo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.RAName = QLabel(self.RemoteAccessPage)
        self.RAName.setObjectName(u"RAName")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.RAName.setFont(font1)

        self.verticalLayout_3.addWidget(self.RAName, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.RAInfo = QLabel(self.RemoteAccessPage)
        self.RAInfo.setObjectName(u"RAInfo")

        self.verticalLayout_3.addWidget(self.RAInfo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.RAMainFrame = QFrame(self.RemoteAccessPage)
        self.RAMainFrame.setObjectName(u"RAMainFrame")
        self.RAMainFrame.setFrameShape(QFrame.StyledPanel)
        self.RAMainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.RAMainFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.RAIPLine = QLineEdit(self.RAMainFrame)
        self.RAIPLine.setObjectName(u"RAIPLine")

        self.verticalLayout_4.addWidget(self.RAIPLine)

        self.RAPortLine = QLineEdit(self.RAMainFrame)
        self.RAPortLine.setObjectName(u"RAPortLine")

        self.verticalLayout_4.addWidget(self.RAPortLine)

        self.RAStartserverBttn = QPushButton(self.RAMainFrame)
        self.RAStartserverBttn.setObjectName(u"RAStartserverBttn")

        self.verticalLayout_4.addWidget(self.RAStartserverBttn)

        self.RAIP2Line = QLineEdit(self.RAMainFrame)
        self.RAIP2Line.setObjectName(u"RAIP2Line")

        self.verticalLayout_4.addWidget(self.RAIP2Line)

        self.RA2PortLine = QLineEdit(self.RAMainFrame)
        self.RA2PortLine.setObjectName(u"RA2PortLine")

        self.verticalLayout_4.addWidget(self.RA2PortLine)

        self.RASendCommandBttn = QPushButton(self.RAMainFrame)
        self.RASendCommandBttn.setObjectName(u"RASendCommandBttn")

        self.verticalLayout_4.addWidget(self.RASendCommandBttn)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.verticalLayout_3.addWidget(self.RAMainFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.RACCLabel = QLabel(self.RemoteAccessPage)
        self.RACCLabel.setObjectName(u"RACCLabel")

        self.verticalLayout_3.addWidget(self.RACCLabel, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.stackedWidget.addWidget(self.RemoteAccessPage)
        self.SharedFileTransferPage = QWidget()
        self.SharedFileTransferPage.setObjectName(u"SharedFileTransferPage")
        self.verticalLayout_5 = QVBoxLayout(self.SharedFileTransferPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.SFNavFrame = QFrame(self.SharedFileTransferPage)
        self.SFNavFrame.setObjectName(u"SFNavFrame")
        self.SFNavFrame.setFrameShape(QFrame.StyledPanel)
        self.SFNavFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.SFNavFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SFPrevBttn = QPushButton(self.SFNavFrame)
        self.SFPrevBttn.setObjectName(u"SFPrevBttn")
        self.SFPrevBttn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.SFPrevBttn, 0, Qt.AlignLeft|Qt.AlignTop)

        self.SFNextBttn = QPushButton(self.SFNavFrame)
        self.SFNextBttn.setObjectName(u"SFNextBttn")
        self.SFNextBttn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.SFNextBttn, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.SFNavFrame)

        self.SFLogo = QLabel(self.SharedFileTransferPage)
        self.SFLogo.setObjectName(u"SFLogo")
        self.SFLogo.setPixmap(QPixmap(u":/icons/Icons/folder.png"))

        self.verticalLayout_5.addWidget(self.SFLogo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.SFName = QLabel(self.SharedFileTransferPage)
        self.SFName.setObjectName(u"SFName")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.SFName.setFont(font2)

        self.verticalLayout_5.addWidget(self.SFName, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.SFInfo = QLabel(self.SharedFileTransferPage)
        self.SFInfo.setObjectName(u"SFInfo")

        self.verticalLayout_5.addWidget(self.SFInfo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.SFMainFrame = QFrame(self.SharedFileTransferPage)
        self.SFMainFrame.setObjectName(u"SFMainFrame")
        self.SFMainFrame.setFrameShape(QFrame.StyledPanel)
        self.SFMainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.SFMainFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.SFSelectFileBttn = QPushButton(self.SFMainFrame)
        self.SFSelectFileBttn.setObjectName(u"SFSelectFileBttn")

        self.verticalLayout_6.addWidget(self.SFSelectFileBttn)

        self.SFFileSelectLine = QLineEdit(self.SFMainFrame)
        self.SFFileSelectLine.setObjectName(u"SFFileSelectLine")

        self.verticalLayout_6.addWidget(self.SFFileSelectLine)

        self.SFSendFileBttn = QPushButton(self.SFMainFrame)
        self.SFSendFileBttn.setObjectName(u"SFSendFileBttn")

        self.verticalLayout_6.addWidget(self.SFSendFileBttn)


        self.verticalLayout_5.addWidget(self.SFMainFrame)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)

        self.SFCCLabel = QLabel(self.SharedFileTransferPage)
        self.SFCCLabel.setObjectName(u"SFCCLabel")

        self.verticalLayout_5.addWidget(self.SFCCLabel, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.stackedWidget.addWidget(self.SharedFileTransferPage)
        self.NetworkConfigurationPage = QWidget()
        self.NetworkConfigurationPage.setObjectName(u"NetworkConfigurationPage")
        self.verticalLayout_7 = QVBoxLayout(self.NetworkConfigurationPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.NCNavFrame = QFrame(self.NetworkConfigurationPage)
        self.NCNavFrame.setObjectName(u"NCNavFrame")
        self.NCNavFrame.setFrameShape(QFrame.StyledPanel)
        self.NCNavFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.NCNavFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.NCPrevBttn = QPushButton(self.NCNavFrame)
        self.NCPrevBttn.setObjectName(u"NCPrevBttn")
        self.NCPrevBttn.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.NCPrevBttn, 0, Qt.AlignLeft)

        self.NCNextBttn = QPushButton(self.NCNavFrame)
        self.NCNextBttn.setObjectName(u"NCNextBttn")
        self.NCNextBttn.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.NCNextBttn, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.NCNavFrame)

        self.NCLogo = QLabel(self.NetworkConfigurationPage)
        self.NCLogo.setObjectName(u"NCLogo")
        self.NCLogo.setPixmap(QPixmap(u":/icons/Icons/wifi.png"))

        self.verticalLayout_7.addWidget(self.NCLogo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.NCName = QLabel(self.NetworkConfigurationPage)
        self.NCName.setObjectName(u"NCName")
        self.NCName.setFont(font2)

        self.verticalLayout_7.addWidget(self.NCName, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.NCInfo = QLabel(self.NetworkConfigurationPage)
        self.NCInfo.setObjectName(u"NCInfo")

        self.verticalLayout_7.addWidget(self.NCInfo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.NCMainFrame = QFrame(self.NetworkConfigurationPage)
        self.NCMainFrame.setObjectName(u"NCMainFrame")
        self.NCMainFrame.setFrameShape(QFrame.StyledPanel)
        self.NCMainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.NCMainFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.NCChangeIPRBttn = QRadioButton(self.NCMainFrame)
        self.NCChangeIPRBttn.setObjectName(u"NCChangeIPRBttn")
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.NCChangeIPRBttn.setFont(font3)

        self.verticalLayout_8.addWidget(self.NCChangeIPRBttn)

        self.NCChangeDnsRBttn = QRadioButton(self.NCMainFrame)
        self.NCChangeDnsRBttn.setObjectName(u"NCChangeDnsRBttn")
        self.NCChangeDnsRBttn.setFont(font3)

        self.verticalLayout_8.addWidget(self.NCChangeDnsRBttn)

        self.NCselectLine = QLineEdit(self.NCMainFrame)
        self.NCselectLine.setObjectName(u"NCselectLine")

        self.verticalLayout_8.addWidget(self.NCselectLine)

        self.NCChangeBttn = QPushButton(self.NCMainFrame)
        self.NCChangeBttn.setObjectName(u"NCChangeBttn")

        self.verticalLayout_8.addWidget(self.NCChangeBttn)

        self.NCBlockInternetBttn = QPushButton(self.NCMainFrame)
        self.NCBlockInternetBttn.setObjectName(u"NCBlockInternetBttn")

        self.verticalLayout_8.addWidget(self.NCBlockInternetBttn)

        self.NCAllowInternetBttn = QPushButton(self.NCMainFrame)
        self.NCAllowInternetBttn.setObjectName(u"NCAllowInternetBttn")

        self.verticalLayout_8.addWidget(self.NCAllowInternetBttn)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_13)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_12)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_11)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_10)


        self.verticalLayout_7.addWidget(self.NCMainFrame)

        self.NCCCLabel = QLabel(self.NetworkConfigurationPage)
        self.NCCCLabel.setObjectName(u"NCCCLabel")

        self.verticalLayout_7.addWidget(self.NCCCLabel, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.stackedWidget.addWidget(self.NetworkConfigurationPage)
        self.BrowsingControlPage = QWidget()
        self.BrowsingControlPage.setObjectName(u"BrowsingControlPage")
        self.verticalLayout_9 = QVBoxLayout(self.BrowsingControlPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.BCNavFrame = QFrame(self.BrowsingControlPage)
        self.BCNavFrame.setObjectName(u"BCNavFrame")
        self.BCNavFrame.setFrameShape(QFrame.StyledPanel)
        self.BCNavFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.BCNavFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BCPrevBttn = QPushButton(self.BCNavFrame)
        self.BCPrevBttn.setObjectName(u"BCPrevBttn")
        self.BCPrevBttn.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.BCPrevBttn, 0, Qt.AlignLeft|Qt.AlignTop)

        self.BCNextBttn = QPushButton(self.BCNavFrame)
        self.BCNextBttn.setObjectName(u"BCNextBttn")
        self.BCNextBttn.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.BCNextBttn, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.BCNavFrame)

        self.BCLogo = QLabel(self.BrowsingControlPage)
        self.BCLogo.setObjectName(u"BCLogo")
        self.BCLogo.setPixmap(QPixmap(u":/icons/Icons/chrome.png"))

        self.verticalLayout_9.addWidget(self.BCLogo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.BCName = QLabel(self.BrowsingControlPage)
        self.BCName.setObjectName(u"BCName")
        self.BCName.setFont(font2)

        self.verticalLayout_9.addWidget(self.BCName, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.BCInfo = QLabel(self.BrowsingControlPage)
        self.BCInfo.setObjectName(u"BCInfo")

        self.verticalLayout_9.addWidget(self.BCInfo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_14)

        self.BCMainFrame = QFrame(self.BrowsingControlPage)
        self.BCMainFrame.setObjectName(u"BCMainFrame")
        self.BCMainFrame.setFrameShape(QFrame.StyledPanel)
        self.BCMainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.BCMainFrame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.BCUrlBlockLine = QLineEdit(self.BCMainFrame)
        self.BCUrlBlockLine.setObjectName(u"BCUrlBlockLine")

        self.verticalLayout_10.addWidget(self.BCUrlBlockLine)

        self.BCBlockUrlBttn = QPushButton(self.BCMainFrame)
        self.BCBlockUrlBttn.setObjectName(u"BCBlockUrlBttn")

        self.verticalLayout_10.addWidget(self.BCBlockUrlBttn)

        self.BCUrlUnBlockLine = QLineEdit(self.BCMainFrame)
        self.BCUrlUnBlockLine.setObjectName(u"BCUrlUnBlockLine")

        self.verticalLayout_10.addWidget(self.BCUrlUnBlockLine)

        self.BCUnblockUrlBttn = QPushButton(self.BCMainFrame)
        self.BCUnblockUrlBttn.setObjectName(u"BCUnblockUrlBttn")

        self.verticalLayout_10.addWidget(self.BCUnblockUrlBttn)

        self.BCUnBlockAllURLBttn = QPushButton(self.BCMainFrame)
        self.BCUnBlockAllURLBttn.setObjectName(u"BCUnBlockAllURLBttn")

        self.verticalLayout_10.addWidget(self.BCUnBlockAllURLBttn)

        self.BCBrowsingHistoryBttn = QPushButton(self.BCMainFrame)
        self.BCBrowsingHistoryBttn.setObjectName(u"BCBrowsingHistoryBttn")

        self.verticalLayout_10.addWidget(self.BCBrowsingHistoryBttn)


        self.verticalLayout_9.addWidget(self.BCMainFrame)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_16)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_15)

        self.BCCCLabel = QLabel(self.BrowsingControlPage)
        self.BCCCLabel.setObjectName(u"BCCCLabel")

        self.verticalLayout_9.addWidget(self.BCCCLabel, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.stackedWidget.addWidget(self.BrowsingControlPage)
        self.LogFilePage = QWidget()
        self.LogFilePage.setObjectName(u"LogFilePage")
        self.verticalLayout_13 = QVBoxLayout(self.LogFilePage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.LogNavFrame = QFrame(self.LogFilePage)
        self.LogNavFrame.setObjectName(u"LogNavFrame")
        self.LogNavFrame.setFrameShape(QFrame.StyledPanel)
        self.LogNavFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.LogNavFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LogPrevBttn = QPushButton(self.LogNavFrame)
        self.LogPrevBttn.setObjectName(u"LogPrevBttn")
        self.LogPrevBttn.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.LogPrevBttn, 0, Qt.AlignLeft|Qt.AlignTop)

        self.LogNextBttn = QPushButton(self.LogNavFrame)
        self.LogNextBttn.setObjectName(u"LogNextBttn")
        self.LogNextBttn.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.LogNextBttn, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.LogNavFrame)

        self.LogLogo = QLabel(self.LogFilePage)
        self.LogLogo.setObjectName(u"LogLogo")
        self.LogLogo.setPixmap(QPixmap(u":/icons/Icons/book-open.png"))

        self.verticalLayout_13.addWidget(self.LogLogo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.LogName = QLabel(self.LogFilePage)
        self.LogName.setObjectName(u"LogName")
        self.LogName.setFont(font2)

        self.verticalLayout_13.addWidget(self.LogName, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_20)

        self.LogGenerateBttn = QPushButton(self.LogFilePage)
        self.LogGenerateBttn.setObjectName(u"LogGenerateBttn")

        self.verticalLayout_13.addWidget(self.LogGenerateBttn)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_22)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_21)

        self.LogCCLabel = QLabel(self.LogFilePage)
        self.LogCCLabel.setObjectName(u"LogCCLabel")

        self.verticalLayout_13.addWidget(self.LogCCLabel, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.stackedWidget.addWidget(self.LogFilePage)
        self.OtherModulePage = QWidget()
        self.OtherModulePage.setObjectName(u"OtherModulePage")
        self.verticalLayout_11 = QVBoxLayout(self.OtherModulePage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.OMNavFrame = QFrame(self.OtherModulePage)
        self.OMNavFrame.setObjectName(u"OMNavFrame")
        self.OMNavFrame.setFrameShape(QFrame.StyledPanel)
        self.OMNavFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.OMNavFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.OMPrevBttn = QPushButton(self.OMNavFrame)
        self.OMPrevBttn.setObjectName(u"OMPrevBttn")
        self.OMPrevBttn.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.OMPrevBttn, 0, Qt.AlignLeft)

        self.OMNextBttn = QPushButton(self.OMNavFrame)
        self.OMNextBttn.setObjectName(u"OMNextBttn")
        self.OMNextBttn.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.OMNextBttn, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.OMNavFrame)

        self.OMLogo = QLabel(self.OtherModulePage)
        self.OMLogo.setObjectName(u"OMLogo")
        self.OMLogo.setPixmap(QPixmap(u":/icons/Icons/info.png"))

        self.verticalLayout_11.addWidget(self.OMLogo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.OMName = QLabel(self.OtherModulePage)
        self.OMName.setObjectName(u"OMName")
        self.OMName.setFont(font2)

        self.verticalLayout_11.addWidget(self.OMName, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_18)

        self.OMMainFrame = QFrame(self.OtherModulePage)
        self.OMMainFrame.setObjectName(u"OMMainFrame")
        self.OMMainFrame.setFrameShape(QFrame.StyledPanel)
        self.OMMainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.OMMainFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.OMDocumentBttn = QPushButton(self.OMMainFrame)
        self.OMDocumentBttn.setObjectName(u"OMDocumentBttn")

        self.verticalLayout_12.addWidget(self.OMDocumentBttn)

        self.OMAboutBttn = QPushButton(self.OMMainFrame)
        self.OMAboutBttn.setObjectName(u"OMAboutBttn")

        self.verticalLayout_12.addWidget(self.OMAboutBttn)

        self.OMAccountBttn = QPushButton(self.OMMainFrame)
        self.OMAccountBttn.setObjectName(u"OMAccountBttn")

        self.verticalLayout_12.addWidget(self.OMAccountBttn)

        self.OMLogOutBttn = QPushButton(self.OMMainFrame)
        self.OMLogOutBttn.setObjectName(u"OMLogOutBttn")

        self.verticalLayout_12.addWidget(self.OMLogOutBttn)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_23)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_19)


        self.verticalLayout_11.addWidget(self.OMMainFrame)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_17)

        self.OMCCLabel = QLabel(self.OtherModulePage)
        self.OMCCLabel.setObjectName(u"OMCCLabel")

        self.verticalLayout_11.addWidget(self.OMCCLabel, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.stackedWidget.addWidget(self.OtherModulePage)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NetAdminPro Server", None))
        self.RAPrevBttn.setText(QCoreApplication.translate("MainWindow", u"Previous Page", None))
        self.RANextBttn.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
        self.RALogo.setText("")
        self.RAName.setText(QCoreApplication.translate("MainWindow", u"  Remote Access", None))
        self.RAInfo.setText(QCoreApplication.translate("MainWindow", u"Enter the Information Below", None))
        self.RAIPLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter I.P Address ", None))
        self.RAPortLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Port Number", None))
        self.RAStartserverBttn.setText(QCoreApplication.translate("MainWindow", u"Start Server For Screen Shareing", None))
        self.RAIP2Line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter I.P Address", None))
        self.RA2PortLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Another Port Number", None))
        self.RASendCommandBttn.setText(QCoreApplication.translate("MainWindow", u"Start Server For Send Command", None))
        self.RACCLabel.setText(QCoreApplication.translate("MainWindow", u" CC Anjani Jha", None))
        self.SFPrevBttn.setText(QCoreApplication.translate("MainWindow", u"Previous Page", None))
        self.SFNextBttn.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
        self.SFLogo.setText("")
        self.SFName.setText(QCoreApplication.translate("MainWindow", u" Shared File Transfer", None))
        self.SFInfo.setText(QCoreApplication.translate("MainWindow", u" Enter The Information Below", None))
        self.SFSelectFileBttn.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.SFFileSelectLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The file You Have Selected", None))
        self.SFSendFileBttn.setText(QCoreApplication.translate("MainWindow", u"Send File", None))
        self.SFCCLabel.setText(QCoreApplication.translate("MainWindow", u" CC Anjani Jha", None))
        self.NCPrevBttn.setText(QCoreApplication.translate("MainWindow", u"Previous Page", None))
        self.NCNextBttn.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
        self.NCLogo.setText("")
        self.NCName.setText(QCoreApplication.translate("MainWindow", u" Network Configuration ", None))
        self.NCInfo.setText(QCoreApplication.translate("MainWindow", u" Enter the Information Below", None))
        self.NCChangeIPRBttn.setText(QCoreApplication.translate("MainWindow", u"Change I.P. Address Of Client", None))
        self.NCChangeDnsRBttn.setText(QCoreApplication.translate("MainWindow", u"Change DNS Of CLient", None))
        self.NCselectLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter The Information Which You Have Selected", None))
        self.NCChangeBttn.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.NCBlockInternetBttn.setText(QCoreApplication.translate("MainWindow", u"Block Internet", None))
        self.NCAllowInternetBttn.setText(QCoreApplication.translate("MainWindow", u"Allow Internet", None))
        self.NCCCLabel.setText(QCoreApplication.translate("MainWindow", u" CC Anjani Jha", None))
        self.BCPrevBttn.setText(QCoreApplication.translate("MainWindow", u"Previous Page", None))
        self.BCNextBttn.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
        self.BCLogo.setText("")
        self.BCName.setText(QCoreApplication.translate("MainWindow", u" Browsing Control ", None))
        self.BCInfo.setText(QCoreApplication.translate("MainWindow", u" Enter The Information Below", None))
        self.BCUrlBlockLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter The URL To Block", None))
        self.BCBlockUrlBttn.setText(QCoreApplication.translate("MainWindow", u"Block URL", None))
        self.BCUrlUnBlockLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Specific URL To Unblock", None))
        self.BCUnblockUrlBttn.setText(QCoreApplication.translate("MainWindow", u"Unblock Specific URL", None))
        self.BCUnBlockAllURLBttn.setText(QCoreApplication.translate("MainWindow", u"Unblock All URL", None))
        self.BCBrowsingHistoryBttn.setText(QCoreApplication.translate("MainWindow", u"Browsing History", None))
        self.BCCCLabel.setText(QCoreApplication.translate("MainWindow", u"CC Anjani Jha", None))
        self.LogPrevBttn.setText(QCoreApplication.translate("MainWindow", u"Previous Page", None))
        self.LogNextBttn.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
        self.LogLogo.setText("")
        self.LogName.setText(QCoreApplication.translate("MainWindow", u" Logs File", None))
        self.LogGenerateBttn.setText(QCoreApplication.translate("MainWindow", u"Generate System Log File", None))
        self.LogCCLabel.setText(QCoreApplication.translate("MainWindow", u" CC Anjani Jha", None))
        self.OMPrevBttn.setText(QCoreApplication.translate("MainWindow", u"Previous Page", None))
        self.OMNextBttn.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
        self.OMLogo.setText("")
        self.OMName.setText(QCoreApplication.translate("MainWindow", u" Account And About", None))
        self.OMDocumentBttn.setText(QCoreApplication.translate("MainWindow", u"Documentation And Help", None))
        self.OMAboutBttn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.OMAccountBttn.setText(QCoreApplication.translate("MainWindow", u"Account Detail", None))
        self.OMLogOutBttn.setText(QCoreApplication.translate("MainWindow", u"LogOut", None))
        self.OMCCLabel.setText(QCoreApplication.translate("MainWindow", u" CC Anjani Jha", None))
    # retranslateUi

