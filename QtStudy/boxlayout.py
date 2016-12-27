#!/usr/bin/env python
# -*- coding = utf-8 -*-

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vBox = QtGui.QVBoxLayout()
        vBox.addStretch(1)
        vBox.addLayout(hbox)

        self.setLayout(vBox)

        self.setWindowTitle('BoxLayout')
        self.resize(500, 350)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())