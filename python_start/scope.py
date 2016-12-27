#!/usr/bin/env python
#coding=utf-8

b = "python"
def outer_foo():
    a = 10
    b = "borney"
    def inner_foo():
        a = 20
        print "inner_foo, a=",a
        print "inner_foo, b=",b
    
    inner_foo()
    print "outer_foo, a=",a
    print "outer_foo, b=",b

a = 30
outer_foo()
print "a=",a
print "b=",b
