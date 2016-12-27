#!/usr/bin/env python

#statusbar.py

import sys
from PyQt4 import QtGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(500, 350)
        self.setWindowTitle("StatusBar")

        self.statusBar().showMessage('Ready')


app = QtGui.QApplication(sys.argv)
mw = MainWindow()
mw.show()
sys.exit(app.exec_())