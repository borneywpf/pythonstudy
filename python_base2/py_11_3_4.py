#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""代码清单11-11"""

def process(line):
    print "Process:", line


import fileinput

for line in fileinput.input('somescript.txt'):
    process(line)
