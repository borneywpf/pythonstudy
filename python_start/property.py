#!/usr/bin/env python
#coding=utf-8

__metaclass__ = type

class ProtectYou:
    def __init__(self):
        self.me = "borney"
        self.__name = "python"
        
    @property
    def name(self):
        return self.__name
        
    def aname(self):
        return self.__name
        
if __name__ == "__main__":
    p = ProtectYou()
    print p.name
    print p.aname()
    #print p.aname
