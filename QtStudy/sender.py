#!/usr/bin/env python
# -*- coding:utf-8 -*-

# sender.py

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        btn1 = QtGui.QPushButton('Button 1', self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton('Button 2', self)
        btn2.move(150, 50)

        self.connect(btn1, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        self.connect(btn2, QtCore.SIGNAL('clicked()'), self.buttonClicked)

        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Event Sender')
        self.resize(500, 350)

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " was pressed")


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
