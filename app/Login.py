from PyQt5 import QtCore, QtGui, QtWidgets

from model.data.data_connect import DataConnect

from WindowTes import UiForm

t = UiForm()

class LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(496, 895)
        MainWindow.setStyleSheet("QWidget#WindowMenu {\n"
"    background-color: black;\n"
"    background-size: cover;\n"
"}\n"
"")
        self.WindowMenu = QtWidgets.QWidget(MainWindow)
        self.WindowMenu.setAutoFillBackground(False)
        self.WindowMenu.setStyleSheet("")
        self.WindowMenu.setObjectName("WindowMenu")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.WindowMenu)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.menu_content = QtWidgets.QVBoxLayout()
        self.menu_content.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.menu_content.setContentsMargins(-1, -1, -1, 10)
        self.menu_content.setSpacing(5)
        self.menu_content.setObjectName("menu_content")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menu_content.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.graphicsView = QtWidgets.QGraphicsView(self.WindowMenu)
        self.graphicsView.setMinimumSize(QtCore.QSize(50, 50))
        self.graphicsView.setMaximumSize(QtCore.QSize(75, 75))
        self.graphicsView.setStyleSheet("border-radius: 50%; background-image: url(\'./app/images/user-75.png\');")
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_5.addWidget(self.graphicsView)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.menu_content.addLayout(self.horizontalLayout_5)
        self.label_3 = QtWidgets.QLabel(self.WindowMenu)
        self.label_3.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(62)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: white; font-weight: 500;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.menu_content.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menu_content.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.WindowMenu)
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QtCore.QSize(400, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(62)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white; font-weight: 500;")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.menu_content.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.WindowMenu)
        self.lineEdit.setMinimumSize(QtCore.QSize(400, 35))
        self.lineEdit.setMaximumSize(QtCore.QSize(400, 50))
        self.lineEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit.setStyleSheet("background-color: rgb(39, 39, 42);\n"
"padding:3px;\n"
"border: none; \n"
"border-radius: 5px; \n"
"color: white;\n"
"")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.menu_content.addWidget(self.lineEdit)
        self.label = QtWidgets.QLabel(self.WindowMenu)
        self.label.setMaximumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(62)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white; font-weight: 500;  margin-top: 20px")
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setIndent(0)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.menu_content.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.WindowMenu)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(400, 30))
        self.lineEdit_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_2.setStyleSheet("background-color: rgb(39, 39, 42);\n"
"padding:3px;\n"
"border: none; \n"
"border-radius: 5px; \n"
"color: white;\n"
"")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.menu_content.addWidget(self.lineEdit_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.menu_content.addItem(spacerItem5)
        self.checkBox = QtWidgets.QCheckBox(self.WindowMenu)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: white")
        self.checkBox.setObjectName("checkBox")
        self.menu_content.addWidget(self.checkBox)
        self.pushButton = QtWidgets.QPushButton(self.WindowMenu)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {"
        "background-color: rgb(147, 83, 199);\n"
        "border: none;\n"
        "border-radius: 5px; \n"
        "color: white; \n"
        "font-size: 16px;\n"
        "font-weight: 600;"
        "}"
        "QPushButton:hover {"
        "background-color: darkblue"
        "}")
        self.pushButton.setObjectName("pushButton")
        self.menu_content.addWidget(self.pushButton)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menu_content.addItem(spacerItem6)
        self.label_4 = QtWidgets.QLabel(self.WindowMenu)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.menu_content.addWidget(self.label_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menu_content.addItem(spacerItem7)
        self.horizontalLayout_3.addLayout(self.menu_content)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        MainWindow.setCentralWidget(self.WindowMenu)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.checkBox.setText(_translate("MainWindow", "Remember-me"))
        self.pushButton.setText(_translate("MainWindow", "Sign In"))
        self.label_4.setText(_translate("MainWindow", "W.I"))

    def handle_event(self):
        self.pushButton.clicked.connect(lambda resp: DataConnect().create_user(self.lineEdit.text(), int(self.lineEdit_2.text())))
        print('?')

            