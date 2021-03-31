#!/usr/bin/env python3


from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
from events import events
import sys



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

events.listen(ui)

MainWindow.show()
sys.exit(app.exec_())
