#!/usr/bin/env python
#coding=utf-8

x = raw_input("first number:")
y = raw_input("second number:")

try:
    print float(x) / float(y)
except Exception, e:
    print e
finally:
    print "finally"
