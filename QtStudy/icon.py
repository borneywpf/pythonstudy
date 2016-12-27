#!/usr/bin/evn python
# -*- coding = utf-8 -*-

#icons.py

import sys
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 500, 350)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QtGui.QIcon('icons/web.png'))

app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())