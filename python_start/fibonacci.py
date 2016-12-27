#! /usr/bin/env python
#coding=utf-8

a, b = 0, 1

for i in range(8):
    print "a = " + str(a) + " b = " + str(b)
    a, b = b, a + b

print a
