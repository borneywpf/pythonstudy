#!/usr/bin/python
# -*- coding=utf-8 -*-
# simple.py

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(500, 350)
widget.setWindowTitle('simple')
widget.show()

sys.exit(app.exec_())