import sys
import os
from PySide2 import *
from ui_MainInterface import *
from Custom_Widgets.Widgets import *



class MainInterface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        
        self.show()
        
        # EXPAND CENTER MENU WIDGET SIZE
        
        self.ui.DocumentBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.AboutBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.LogOutBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        
        
        # CLOSE CENTER MENU WIDGET SIZE
        self.ui.CloseCentreMenuBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.collapseMenu())
        
        # EXPAND RIGHT MENU WIDGET SIZE
        
        self.ui.MoreMenuBtn.clicked.connect(lambda: self.ui.RightMenuContainer.expandMenu())
        self.ui.AccountMenuBtn.clicked.connect(lambda: self.ui.RightMenuContainer.expandMenu())
        
        
        # CLOSE RIGHT MENU WIDGET SIZE
        self.ui.CloseRightMenuBtn.clicked.connect(lambda: self.ui.RightMenuContainer.collapseMenu())
        
        # CLOSE NOTIFICITATION MENU WIDGET SIZE
        self.ui.CloseNotificationBtn.clicked.connect(lambda: self.ui.PopUpNotificationContainer.collapseMenu())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainInterface()
    sys.exit(app.exec_())