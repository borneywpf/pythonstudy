#!/usr/bin/env python
#coding=utf-8

class A(object):
    author = "borney"
    def __getattr__(self, name):
        if name != "author":
            return "from starter no master."
            
if __name__ == "__main__":
    a = A()
    print "-----------------"
    print A.__dict__
    print "================="
    print a.__dict__
    print "*****************"
    print a.author
    print a.lang
