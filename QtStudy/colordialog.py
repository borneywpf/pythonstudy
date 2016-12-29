#!/usr/bin/env python
# -*- coding:utf-8 -*-

#colordialog.py

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        color = QtGui.QColor(0, 0, 0, 0)

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn.move(20, 50)

        self.connect(self.btn, QtCore.SIGNAL('clicked()'), self.showDialog)
        self.setFocus()
        self.setStyleSheet("QWidget { backgroud-color: %s }" % color.name())

        self.setWindowTitle("ColorDialog")
        self.setGeometry(300, 300, 250, 180)

    def showDialog(self):
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            self.setStyleSheet("QWidget { background-color: %s }" % col.name())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())