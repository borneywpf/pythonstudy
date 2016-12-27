#!/usr/bin/env python

# center.py

import sys
from PyQt4 import QtGui


class Center(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle("Center")
        self.resize(500, 350)
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - self.height()) / 2)


app = QtGui.QApplication(sys.argv)
center = Center()
center.show()
sys.exit(app.exec_())
