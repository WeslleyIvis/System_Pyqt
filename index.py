import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Login import Login_Window

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Login_Window()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_()) 