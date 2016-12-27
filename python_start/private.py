#!/usr/bin/env python
#coding=utf-8

__metaclass__ = type

class ProtectMe:
    def __init__(self):
        self.me = "borney"
        self.__lang = "python"
        
    def __python(self):
        print "I love python"
        
    def code(self):
        print "Which language do you like?"
        self.__python()

if __name__ == "__main__":
    p = ProtectMe()
    print p.me
    #print p.__lang
    #p.__python()
    p.code()
