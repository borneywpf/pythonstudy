#!/usr/bin/env python
# -*- coding:utf-8 -*-

# simpledrag.py

"""
ZetCode PyQt4 tutorial

This is a simple drag and
drop example.

author: Jan Bodnar
website: zetcode.com
last edited: December 2010
"""

import sys
from PyQt4 import QtGui


class Button(QtGui.QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        edt = QtGui.QLineEdit('', self)
        edt.setDragEnabled(True)
        edt.move(30, 65)

        btn = Button("Button", self)
        btn.move(190, 65)

        self.setWindowTitle("Simple Drag & Drop")
        self.setGeometry(300, 300, 300, 150)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
