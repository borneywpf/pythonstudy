#!/usr/bin/env python
#coding=utf-8

import copy

class MyCopy(object):
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return str(self.value)
        
foo = MyCopy(7)

a = ["foo", foo]
b = a[:]
c = list(a)
d = copy.copy(a)
e = copy.deepcopy(a)

print "original-before: a-%r\n slice: b-%r\n list(): c-%r\n copy(): d-%r\n deepcopy(): e-%r\n" % (a,b,c,d,e)

a.append("abc")
a[0] = "foo-abc"
foo.value = 17

print "original-after: a-%r\n slice: b-%r\n list(): c-%r\n copy(): d-%r\n deepcopy(): e-%r\n" % (a,b,c,d,e)
