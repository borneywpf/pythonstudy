#! /usr/bin/env python
#coding=utf-8

__metaclass__ = type

class Person:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name
        
    def breast(self, n):
        self.breast = n
        
    def color(self, color):
        print "%s is %s" % (self.name, color)
        
    def how(self):
        print "%s breast is %s" % (self.name, self.breast)
        
boy = Person("borney")
boy.breast(90)

boy.color("white")
boy.how()
