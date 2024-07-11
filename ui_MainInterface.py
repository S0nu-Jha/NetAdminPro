# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainInterfaceGzZSDK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(963, 461)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"\n"
"\n"
"}\n"
"#centralwidget{\n"
"	background-color: rgb(31, 35, 42);\n"
"}\n"
"#LeftMenuSubContainer,  #RightMenuSubContainer{\n"
"	background-color: rgb(22, 25, 29);\n"
"\n"
"}\n"
"#LeftMenuSubContainer QPushButton{\n"
"	text-align:left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"#CenterMenuSubContainer,#RightMenuSubContainer{\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"#frame_4, #frame_8,#PopUpNotificationSubContainer{\n"
"	background-color: rgb(22, 25, 29);\n"
"	border-radius:10px;\n"
"}\n"
"#HeaderContainer,#FooterContainer{\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgb(9, 10, 37);\n"
"	padding: 5px 3px;\n"
"	border-radius:5px;\n"
"	\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.LeftMenuContainer.setObjectName(u"LeftMenuContainer")
        self.LeftMenuContainer.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout = QVBoxLayout(self.LeftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuSubContainer = QWidget(self.LeftMenuContainer)
        self.LeftMenuSubContainer.setObjectName(u"LeftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.LeftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MenuBtn = QPushButton(self.frame)
        self.MenuBtn.setObjectName(u"MenuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MenuBtn.setIcon(icon)
        self.MenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.MenuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.LeftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.RemoteBtn = QPushButton(self.frame_2)
        self.RemoteBtn.setObjectName(u"RemoteBtn")
        self.RemoteBtn.setStyleSheet(u"background-color: rgb(31, 35, 42);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RemoteBtn.setIcon(icon1)
        self.RemoteBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.RemoteBtn)

        self.SharedBtn = QPushButton(self.frame_2)
        self.SharedBtn.setObjectName(u"SharedBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/share.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SharedBtn.setIcon(icon2)
        self.SharedBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.SharedBtn)

        self.NetworkBtn = QPushButton(self.frame_2)
        self.NetworkBtn.setObjectName(u"NetworkBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/wifi.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.NetworkBtn.setIcon(icon3)
        self.NetworkBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.NetworkBtn)

        self.BrowsingBtn = QPushButton(self.frame_2)
        self.BrowsingBtn.setObjectName(u"BrowsingBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/chrome.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.BrowsingBtn.setIcon(icon4)
        self.BrowsingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.BrowsingBtn)

        self.LogBtn = QPushButton(self.frame_2)
        self.LogBtn.setObjectName(u"LogBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.LogBtn.setIcon(icon5)
        self.LogBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.LogBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.LeftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.DocumentBtn = QPushButton(self.frame_3)
        self.DocumentBtn.setObjectName(u"DocumentBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.DocumentBtn.setIcon(icon6)
        self.DocumentBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.DocumentBtn)

        self.AboutBtn = QPushButton(self.frame_3)
        self.AboutBtn.setObjectName(u"AboutBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.AboutBtn.setIcon(icon7)
        self.AboutBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.AboutBtn)

        self.LogOutBtn = QPushButton(self.frame_3)
        self.LogOutBtn.setObjectName(u"LogOutBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/key.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.LogOutBtn.setIcon(icon8)
        self.LogOutBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.LogOutBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.LeftMenuSubContainer)


        self.horizontalLayout.addWidget(self.LeftMenuContainer)

        self.CenterMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.CenterMenuContainer.setObjectName(u"CenterMenuContainer")
        self.CenterMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_5 = QVBoxLayout(self.CenterMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.CenterMenuSubContainer = QWidget(self.CenterMenuContainer)
        self.CenterMenuSubContainer.setObjectName(u"CenterMenuSubContainer")
        self.CenterMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.CenterMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.CenterMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.CloseCentreMenuBtn = QPushButton(self.frame_4)
        self.CloseCentreMenuBtn.setObjectName(u"CloseCentreMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseCentreMenuBtn.setIcon(icon9)
        self.CloseCentreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.CloseCentreMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.CenterMenuPages = QCustomStackedWidget(self.CenterMenuSubContainer)
        self.CenterMenuPages.setObjectName(u"CenterMenuPages")
        self.AboutPage = QWidget()
        self.AboutPage.setObjectName(u"AboutPage")
        self.verticalLayout_8 = QVBoxLayout(self.AboutPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.About = QLabel(self.AboutPage)
        self.About.setObjectName(u"About")
        font = QFont()
        font.setPointSize(13)
        self.About.setFont(font)
        self.About.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.About)

        self.CenterMenuPages.addWidget(self.AboutPage)
        self.LogOutPage = QWidget()
        self.LogOutPage.setObjectName(u"LogOutPage")
        self.verticalLayout_9 = QVBoxLayout(self.LogOutPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.LogOutPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.CenterMenuPages.addWidget(self.LogOutPage)
        self.DocHelpPage = QWidget()
        self.DocHelpPage.setObjectName(u"DocHelpPage")
        self.verticalLayout_7 = QVBoxLayout(self.DocHelpPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.DocHelpPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.CenterMenuPages.addWidget(self.DocHelpPage)

        self.verticalLayout_6.addWidget(self.CenterMenuPages)


        self.verticalLayout_5.addWidget(self.CenterMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.CenterMenuContainer)

        self.MainBodyContainer = QWidget(self.centralwidget)
        self.MainBodyContainer.setObjectName(u"MainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainBodyContainer.sizePolicy().hasHeightForWidth())
        self.MainBodyContainer.setSizePolicy(sizePolicy1)
        self.MainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.MainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.HeaderContainer = QWidget(self.MainBodyContainer)
        self.HeaderContainer.setObjectName(u"HeaderContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.HeaderContainer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.HeaderContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(200, 200))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 50))
        self.label_4.setPixmap(QPixmap(u":/AppIcon/AppLogo.png"))

        self.horizontalLayout_7.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(110, 110))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_5)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.HeaderContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.NotificationBtn = QPushButton(self.frame_6)
        self.NotificationBtn.setObjectName(u"NotificationBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.NotificationBtn.setIcon(icon10)
        self.NotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.NotificationBtn)

        self.MoreMenuBtn = QPushButton(self.frame_6)
        self.MoreMenuBtn.setObjectName(u"MoreMenuBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MoreMenuBtn.setIcon(icon11)
        self.MoreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.MoreMenuBtn)

        self.AccountMenuBtn = QPushButton(self.frame_6)
        self.AccountMenuBtn.setObjectName(u"AccountMenuBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.AccountMenuBtn.setIcon(icon12)
        self.AccountMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.AccountMenuBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.HeaderContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.MinimizeBtn = QPushButton(self.frame_7)
        self.MinimizeBtn.setObjectName(u"MinimizeBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/minimize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MinimizeBtn.setIcon(icon13)

        self.horizontalLayout_4.addWidget(self.MinimizeBtn)

        self.RestoreBtn = QPushButton(self.frame_7)
        self.RestoreBtn.setObjectName(u"RestoreBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RestoreBtn.setIcon(icon14)

        self.horizontalLayout_4.addWidget(self.RestoreBtn)

        self.CloseBtn = QPushButton(self.frame_7)
        self.CloseBtn.setObjectName(u"CloseBtn")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseBtn.setIcon(icon15)

        self.horizontalLayout_4.addWidget(self.CloseBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.HeaderContainer, 0, Qt.AlignTop)

        self.MainBodyContent = QWidget(self.MainBodyContainer)
        self.MainBodyContent.setObjectName(u"MainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.MainBodyContent.sizePolicy().hasHeightForWidth())
        self.MainBodyContent.setSizePolicy(sizePolicy2)
        self.MainBodyContent.setMinimumSize(QSize(505, 279))
        self.horizontalLayout_8 = QHBoxLayout(self.MainBodyContent)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.MainContentsContainer = QWidget(self.MainBodyContent)
        self.MainContentsContainer.setObjectName(u"MainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.MainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.MainCenterPage = QCustomStackedWidget(self.MainContentsContainer)
        self.MainCenterPage.setObjectName(u"MainCenterPage")
        self.SharePage = QWidget()
        self.SharePage.setObjectName(u"SharePage")
        self.verticalLayout_17 = QVBoxLayout(self.SharePage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.About_5 = QLabel(self.SharePage)
        self.About_5.setObjectName(u"About_5")
        self.About_5.setFont(font)
        self.About_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.About_5)

        self.MainCenterPage.addWidget(self.SharePage)
        self.RemotePage = QWidget()
        self.RemotePage.setObjectName(u"RemotePage")
        self.verticalLayout_16 = QVBoxLayout(self.RemotePage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_9 = QLabel(self.RemotePage)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_9.setFont(font2)

        self.verticalLayout_16.addWidget(self.label_9, 0, Qt.AlignTop)

        self.widget = QWidget(self.RemotePage)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_13 = QHBoxLayout(self.widget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_23 = QVBoxLayout(self.widget_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_11 = QFrame(self.widget_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_11)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.lineEdit = QLineEdit(self.frame_11)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_24.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_11)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_24.addWidget(self.lineEdit_2)

        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(9, 10, 37);\n"
"	padding: 5px 3px;\n"
"	border-radius:5px;\n"
"	\n"
"}")

        self.verticalLayout_24.addWidget(self.pushButton)


        self.verticalLayout_23.addWidget(self.frame_11)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_2)


        self.horizontalLayout_13.addWidget(self.widget_2, 0, Qt.AlignLeft)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(215, 176))
        self.widget_3.setMaximumSize(QSize(215, 176))

        self.horizontalLayout_13.addWidget(self.widget_3)


        self.verticalLayout_16.addWidget(self.widget)

        self.MainCenterPage.addWidget(self.RemotePage)
        self.NetworkPage = QWidget()
        self.NetworkPage.setObjectName(u"NetworkPage")
        self.verticalLayout_18 = QVBoxLayout(self.NetworkPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.About_6 = QLabel(self.NetworkPage)
        self.About_6.setObjectName(u"About_6")
        self.About_6.setFont(font)
        self.About_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.About_6)

        self.MainCenterPage.addWidget(self.NetworkPage)
        self.BrowsingPage = QWidget()
        self.BrowsingPage.setObjectName(u"BrowsingPage")
        self.verticalLayout_19 = QVBoxLayout(self.BrowsingPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.About_7 = QLabel(self.BrowsingPage)
        self.About_7.setObjectName(u"About_7")
        self.About_7.setFont(font)
        self.About_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.About_7)

        self.MainCenterPage.addWidget(self.BrowsingPage)
        self.LogPage = QWidget()
        self.LogPage.setObjectName(u"LogPage")
        self.verticalLayout_20 = QVBoxLayout(self.LogPage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.About_8 = QLabel(self.LogPage)
        self.About_8.setObjectName(u"About_8")
        self.About_8.setFont(font)
        self.About_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.About_8)

        self.MainCenterPage.addWidget(self.LogPage)

        self.verticalLayout_15.addWidget(self.MainCenterPage)


        self.horizontalLayout_8.addWidget(self.MainContentsContainer)

        self.RightMenuContainer = QCustomSlideMenu(self.MainBodyContent)
        self.RightMenuContainer.setObjectName(u"RightMenuContainer")
        self.RightMenuContainer.setMinimumSize(QSize(200, 0))
        self.RightMenuContainer.setMaximumSize(QSize(210, 279))
        self.verticalLayout_11 = QVBoxLayout(self.RightMenuContainer)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.RightMenuSubContainer = QWidget(self.RightMenuContainer)
        self.RightMenuSubContainer.setObjectName(u"RightMenuSubContainer")
        self.RightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_12 = QVBoxLayout(self.RightMenuSubContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.RightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.CloseRightMenuBtn = QPushButton(self.frame_8)
        self.CloseRightMenuBtn.setObjectName(u"CloseRightMenuBtn")
        self.CloseRightMenuBtn.setMaximumSize(QSize(50, 50))
        self.CloseRightMenuBtn.setIcon(icon9)
        self.CloseRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.CloseRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.RightMenuPages = QCustomStackedWidget(self.RightMenuSubContainer)
        self.RightMenuPages.setObjectName(u"RightMenuPages")
        self.MorePage = QWidget()
        self.MorePage.setObjectName(u"MorePage")
        self.verticalLayout_14 = QVBoxLayout(self.MorePage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.About_3 = QLabel(self.MorePage)
        self.About_3.setObjectName(u"About_3")
        self.About_3.setFont(font)
        self.About_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.About_3)

        self.RightMenuPages.addWidget(self.MorePage)
        self.AccountPage = QWidget()
        self.AccountPage.setObjectName(u"AccountPage")
        self.verticalLayout_13 = QVBoxLayout(self.AccountPage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.About_2 = QLabel(self.AccountPage)
        self.About_2.setObjectName(u"About_2")
        self.About_2.setFont(font)
        self.About_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.About_2)

        self.RightMenuPages.addWidget(self.AccountPage)

        self.verticalLayout_12.addWidget(self.RightMenuPages)


        self.verticalLayout_11.addWidget(self.RightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.RightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.MainBodyContent)

        self.PopUpNotificationContainer = QCustomSlideMenu(self.MainBodyContainer)
        self.PopUpNotificationContainer.setObjectName(u"PopUpNotificationContainer")
        self.verticalLayout_21 = QVBoxLayout(self.PopUpNotificationContainer)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.PopUpNotificationSubContainer = QWidget(self.PopUpNotificationContainer)
        self.PopUpNotificationSubContainer.setObjectName(u"PopUpNotificationSubContainer")
        self.verticalLayout_22 = QVBoxLayout(self.PopUpNotificationSubContainer)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_8 = QLabel(self.PopUpNotificationSubContainer)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_8.setFont(font3)

        self.verticalLayout_22.addWidget(self.label_8)

        self.frame_9 = QFrame(self.PopUpNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_7)

        self.CloseNotificationBtn = QPushButton(self.frame_9)
        self.CloseNotificationBtn.setObjectName(u"CloseNotificationBtn")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseNotificationBtn.setIcon(icon16)
        self.CloseNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.CloseNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_22.addWidget(self.frame_9)


        self.verticalLayout_21.addWidget(self.PopUpNotificationSubContainer)


        self.verticalLayout_10.addWidget(self.PopUpNotificationContainer)

        self.FooterContainer = QWidget(self.MainBodyContainer)
        self.FooterContainer.setObjectName(u"FooterContainer")
        self.horizontalLayout_11 = QHBoxLayout(self.FooterContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.FooterContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)


        self.horizontalLayout_11.addWidget(self.frame_10)

        self.SizeGrip = QFrame(self.FooterContainer)
        self.SizeGrip.setObjectName(u"SizeGrip")
        self.SizeGrip.setMinimumSize(QSize(30, 30))
        self.SizeGrip.setMaximumSize(QSize(30, 30))
        self.SizeGrip.setFrameShape(QFrame.StyledPanel)
        self.SizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.SizeGrip, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.FooterContainer)


        self.horizontalLayout.addWidget(self.MainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.MainCenterPage.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.MenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.MenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.RemoteBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Remote Access", None))
#endif // QT_CONFIG(tooltip)
        self.RemoteBtn.setText(QCoreApplication.translate("MainWindow", u"Remote Access", None))
#if QT_CONFIG(tooltip)
        self.SharedBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Shared File Transfer", None))
#endif // QT_CONFIG(tooltip)
        self.SharedBtn.setText(QCoreApplication.translate("MainWindow", u"Shared File Transfer", None))
#if QT_CONFIG(tooltip)
        self.NetworkBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Network Configuration", None))
#endif // QT_CONFIG(tooltip)
        self.NetworkBtn.setText(QCoreApplication.translate("MainWindow", u"Network Configuration", None))
#if QT_CONFIG(tooltip)
        self.BrowsingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Browsing Control", None))
#endif // QT_CONFIG(tooltip)
        self.BrowsingBtn.setText(QCoreApplication.translate("MainWindow", u"Browsing Control", None))
#if QT_CONFIG(tooltip)
        self.LogBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Logs", None))
#endif // QT_CONFIG(tooltip)
        self.LogBtn.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
#if QT_CONFIG(tooltip)
        self.DocumentBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Documentation And Help", None))
#endif // QT_CONFIG(tooltip)
        self.DocumentBtn.setText(QCoreApplication.translate("MainWindow", u"Documentation And Help", None))
#if QT_CONFIG(tooltip)
        self.AboutBtn.setToolTip(QCoreApplication.translate("MainWindow", u"About", None))
#endif // QT_CONFIG(tooltip)
        self.AboutBtn.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.LogOutBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Log Out", None))
#endif // QT_CONFIG(tooltip)
        self.LogOutBtn.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu ", None))
#if QT_CONFIG(tooltip)
        self.CloseCentreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.CloseCentreMenuBtn.setText("")
        self.About.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"NetAdminPro", None))
#if QT_CONFIG(tooltip)
        self.NotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Notification", None))
#endif // QT_CONFIG(tooltip)
        self.NotificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.MoreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.MoreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.AccountMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Account", None))
#endif // QT_CONFIG(tooltip)
        self.AccountMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.MinimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.MinimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.RestoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.RestoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.CloseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.CloseBtn.setText("")
        self.About_5.setText(QCoreApplication.translate("MainWindow", u"Shared File Transfer", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Remote Access", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Client I.P. Address", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Client Port Number", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.About_6.setText(QCoreApplication.translate("MainWindow", u"Network Configuration", None))
        self.About_7.setText(QCoreApplication.translate("MainWindow", u"Browsing Control", None))
        self.About_8.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.CloseRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.CloseRightMenuBtn.setText("")
        self.About_3.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.About_2.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.CloseNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.CloseNotificationBtn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Copyright Sonu Jha", None))
    # retranslateUi

