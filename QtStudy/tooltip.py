#!/usr/bin/env python
# -*- coding = utf-8 -*-
# tooltip.py

import sys
from PyQt4 import QtGui


class Tooltip(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 500, 350)
        self.setWindowTitle("Tooltip")

        self.setToolTip('This is a <b>QWidget</b> widget')
        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))

app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())