#! /usr/bin/env python
#coding=utf-8

__metaclass__ = type
class Person:
    def __init__(self, name):
        self.name = name
        print self
        print type(self)
    
    def getName(self):
        return self.name
    
    def color(self, color):
        print "%s is %s" % (self.name, color)
        

boy = Person("borney")

print boy
print boy.name
print boy.getName()
print boy.color("white")
