#! /usr/bin/env python
#coding=utf-8

x = 2

def funcx():
    x = 9
    print "in funcx x = ", x
    
def funcy():
    global x
    x = 9
    print "in funcy x = ", x

funcx()
print "out funcx x = ", x

funcy()
print "out funcy x = ", x
