import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Login import LoginWindow
from WindowTes import UiForm

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = LoginWindow()
        self.ui.setupUi(self)

        self.jan2 = Window2()

        self.ui.pushButton.clicked.connect(self.handlerEvent)

    def handlerEvent(self):
        self.jan2.show()
        self.hide()

class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiForm()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.overrideWindowFlags.show

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_()) 