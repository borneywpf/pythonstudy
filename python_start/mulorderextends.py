#!/usr/bin/env python
#coding=utf-8

__metaclass__ = type

class K1(object):
    def foo(self):
        print "K1-foo"
        
class K2(object):
    def foo(self):
        print "K2-foo"
    def bar(self):
        print "K2-bar"
        
class J1(K1, K2):
    pass

class J2(K1, K2):
    def bar(self):
        print "J2-bar"

class J3(K2, K1):
    def bar(self):
        print "J3-bar"
    
class C(J1, J2):
    pass

class D(J3):
    pass
    
if __name__ == "__main__":
    print C.__mro__ #打印类的继承顺序
    m = C()
    m.foo()
    m.bar()
    
    print "---------------"
    print D.__mro__
    n = D()
    n.foo()
    n.bar()
    
"""
(<class '__main__.C'>, <class '__main__.J1'>, <class '__main__.J2'>, <class '__main__.K1'>, <class '__main__.K2'>, <type 'object'>)
K1-foo
J2-bar
---------------
(<class '__main__.D'>, <class '__main__.J3'>, <class '__main__.K2'>, <class '__main__.K1'>, <type 'object'>)
K2-foo
J3-bar
"""
