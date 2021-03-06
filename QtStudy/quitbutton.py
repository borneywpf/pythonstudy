#!/usr/bin/env python
# -*- coding = utf-8 -*-

# quitbutton.py

import sys
from PyQt4 import QtGui, QtCore


class QuitBotton(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 500, 350)
        self.setWindowTitle('QuitButton')

        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(10, 10, 64, 35)

        self.connect(quit, QtCore.SIGNAL('clicked()'),
                     QtGui.qApp, QtCore.SLOT('quit()'))


app = QtGui.QApplication(sys.argv)
qb = QuitBotton()
qb.show()
sys.exit(app.exec_())
