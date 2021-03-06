#!/usr/bin/env python
# -*- coding = utf-8 -*-

#absolute.py

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        label1 = QtGui.QLabel('Zetcode', self)
        label1.move(15, 10)

        label2 = QtGui.QLabel('tutorials for programmers', self)
        label2.move(35, 40)

        self.setWindowTitle('Absolute')
        self.resize(500, 350)


app = QtGui.QApplication(sys.argv)
example = Example()
example.show()
sys.exit(app.exec_())
