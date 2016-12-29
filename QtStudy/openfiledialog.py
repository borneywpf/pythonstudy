#!/usr/bin/env python
# -*- coding:utf-8 -*-

# openfiledialog.py


import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.edt = QtGui.QTextEdit()
        self.setCentralWidget(self.edt)
        self.statusBar()
        self.setFocus()

        of = QtGui.QAction(QtGui.QIcon('icons/web.png'), 'Open', self)
        of.setShortcut('Ctrl+O')
        of.setStatusTip('Open new file')
        self.connect(of, QtCore.SIGNAL('triggered()'), self.showDialog)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(of)

        self.setWindowTitle('OpenFileDialog')
        self.setGeometry(300, 300, 350, 300)

    def showDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home/borney/data')
        fname = open(filename)
        data = fname.read()
        self.edt.setText(data.decode('utf-8'))


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
