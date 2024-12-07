from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 585)
        MainWindow.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.window = QtWidgets.QWidget(MainWindow)
        self.window.setObjectName("window")

        self.button_add = QtWidgets.QPushButton(self.window)
        self.button_add.setGeometry(QtCore.QRect(280, 220, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_add.setFont(font)
        self.button_add.setStyleSheet("background-color: rgb(0, 208, 100);\n"
                                      "color: rgb(255, 255, 255);")

        self.button_add.setObjectName("button_add")
        self.button_sub = QtWidgets.QPushButton(self.window)
        self.button_sub.setGeometry(QtCore.QRect(280, 300, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button_sub.setFont(font)
        self.button_sub.setStyleSheet("background-color: rgb(0, 208, 100);\n"
                                      "color: rgb(255, 255, 255);")
        self.button_sub.setObjectName("button_sub")

        self.button_myl = QtWidgets.QPushButton(self.window)
        self.button_myl.setGeometry(QtCore.QRect(280, 380, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_myl.setFont(font)
        self.button_myl.setStyleSheet("background-color: rgb(0, 208, 100);\n"
                                      "color: rgb(255, 255, 255);")
        self.button_myl.setObjectName("button_myl")

        self.button_div = QtWidgets.QPushButton(self.window)
        self.button_div.setGeometry(QtCore.QRect(280, 460, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_div.setFont(font)
        self.button_div.setStyleSheet("background-color: rgb(0, 208, 100);\n"
                                      "color: rgb(255, 255, 255);")
        self.button_div.setObjectName("button_div")

        self.button_1 = QtWidgets.QPushButton(self.window)
        self.button_1.setGeometry(QtCore.QRect(40, 140, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_1.setFont(font)
        self.button_1.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.button_1.setObjectName("button_1")

        self.button_2 = QtWidgets.QPushButton(self.window)
        self.button_2.setGeometry(QtCore.QRect(120, 140, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_2.setFont(font)
        self.button_2.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.button_2.setObjectName("button_2")

        self.button_3 = QtWidgets.QPushButton(self.window)
        self.button_3.setGeometry(QtCore.QRect(200, 140, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_3.setFont(font)
        self.button_3.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.button_3.setObjectName("button_3")

        self.button_4 = QtWidgets.QPushButton(self.window)
        self.button_4.setGeometry(QtCore.QRect(40, 220, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_4.setFont(font)
        self.button_4.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.button_4.setObjectName("button_4")

        self.button_5 = QtWidgets.QPushButton(self.window)
        self.button_5.setGeometry(QtCore.QRect(120, 220, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_5.setFont(font)
        self.button_5.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.button_5.setObjectName("button_5")

        self.button_6 = QtWidgets.QPushButton(self.window)
        self.button_6.setGeometry(QtCore.QRect(200, 220, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_6.setFont(font)
        self.button_6.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.button_6.setObjectName("button_6")

        self.button_7 = QtWidgets.QPushButton(self.window)
        self.button_7.setGeometry(QtCore.QRect(40, 300, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_7.setFont(font)
        self.button_7.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.button_7.setObjectName("button_7")

        self.button_8 = QtWidgets.QPushButton(self.window)
        self.button_8.setGeometry(QtCore.QRect(120, 300, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_8.setFont(font)
        self.button_8.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.button_8.setObjectName("button_8")

        self.button_9 = QtWidgets.QPushButton(self.window)
        self.button_9.setGeometry(QtCore.QRect(200, 300, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_9.setFont(font)
        self.button_9.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.button_9.setObjectName("button_9")

        self.button_0 = QtWidgets.QPushButton(self.window)
        self.button_0.setGeometry(QtCore.QRect(120, 380, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_0.setFont(font)
        self.button_0.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.button_0.setObjectName("button_0")

        self.button_c = QtWidgets.QPushButton(self.window)
        self.button_c.setGeometry(QtCore.QRect(280, 140, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.button_c.setFont(font)
        self.button_c.setStyleSheet("background-color: rgb(255, 170, 0);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "")
        self.button_c.setObjectName("button_c")

        self.button_res = QtWidgets.QPushButton(self.window)
        self.button_res.setGeometry(QtCore.QRect(200, 460, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_res.setFont(font)
        self.button_res.setStyleSheet("background-color: rgb(0, 208, 100);\n"
                                      "color: rgb(255, 255, 255);")
        self.button_res.setObjectName("button_res")

        self.button_fl = QtWidgets.QPushButton(self.window)
        self.button_fl.setGeometry(QtCore.QRect(200, 380, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_fl.setFont(font)
        self.button_fl.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                     "color: rgb(255, 255, 255);")
        self.button_fl.setObjectName("button_fl")

        self.button_bs = QtWidgets.QPushButton(self.window)
        self.button_bs.setGeometry(QtCore.QRect(40, 380, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_bs.setFont(font)
        self.button_bs.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                     "color: rgb(255, 255, 255);")
        self.button_bs.setObjectName("button_bs")

        self.button_000 = QtWidgets.QPushButton(self.window)
        self.button_000.setGeometry(QtCore.QRect(120, 460, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_000.setFont(font)
        self.button_000.setStyleSheet("background-color: rgb(0, 208, 100);\n"
                                      "color: rgb(255, 255, 255);")
        self.button_000.setObjectName("button_000")

        self.button_adsu = QtWidgets.QPushButton(self.window)
        self.button_adsu.setGeometry(QtCore.QRect(40, 460, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_adsu.setFont(font)
        self.button_adsu.setStyleSheet("background-color: rgb(0, 208, 100);\n"
                                       "color: rgb(255, 255, 255);")
        self.button_adsu.setObjectName("button_adsu")

        self.lcd = QtWidgets.QLCDNumber(self.window)
        self.lcd.setGeometry(QtCore.QRect(40, 40, 311, 61))
        self.lcd.setStyleSheet("background-color: rgb(0, 208, 100);\n"
                               "")
        self.lcd.setObjectName("lcd")
        MainWindow.setCentralWidget(self.window)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.button_add.setText(_translate("MainWindow", "+"))
        self.button_sub.setText(_translate("MainWindow", "-"))
        self.button_myl.setText(_translate("MainWindow", "x"))
        self.button_div.setText(_translate("MainWindow", ":"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_c.setText(_translate("MainWindow", "С"))
        self.button_res.setText(_translate("MainWindow", "="))
        self.button_fl.setText(_translate("MainWindow", ","))
        self.button_bs.setText(_translate("MainWindow", "<"))
        self.button_000.setText(_translate("MainWindow", "000"))
        self.button_adsu.setText(_translate("MainWindow", "+/-"))

    def add_functions(self):
        self.button_add.clicked.connect(lambda: self.write_number(self.button_add.text()))
        self.button_sub.clicked.connect(lambda: self.write_number(self.button_sub.text()))
        self.button_myl.clicked.connect(lambda: self.write_number(self.button_myl.text()))
        self.button_div.clicked.connect(lambda: self.write_number(self.button_div.text()))
        self.button_1.clicked.connect(lambda: self.write_number(self.button_1.text()))
        self.button_2.clicked.connect(lambda: self.write_number(self.button_2.text()))
        self.button_3.clicked.connect(lambda: self.write_number(self.button_3.text()))
        self.button_4.clicked.connect(lambda: self.write_number(self.button_4.text()))
        self.button_5.clicked.connect(lambda: self.write_number(self.button_5.text()))
        self.button_6.clicked.connect(lambda: self.write_number(self.button_6.text()))
        self.button_7.clicked.connect(lambda: self.write_number(self.button_7.text()))
        self.button_8.clicked.connect(lambda: self.write_number(self.button_8.text()))
        self.button_9.clicked.connect(lambda: self.write_number(self.button_9.text()))
        self.button_0.clicked.connect(lambda: self.write_number(self.button_0.text()))
        self.button_000.clicked.connect(lambda: self.write_number(self.button_000.text()))

    def write_number(self, number):
        current_value = str(self.lcd.value())  # Получаем текущее значение как строку
        new_value = current_value + number  # Конкатенируем новое число
        self.lcd.display(new_value)  # Отображаем новое значение


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())