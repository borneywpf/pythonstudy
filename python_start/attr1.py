#!/usr/bin/env python
#coding=utf-8

class NewRectangle(object):
    def __init__(self):
        self.w = 0
        self.h = 0
        
    def __setattr__(self, name, value):
        print "you call __setattr__ name={}, value={}".format(name, value)
        if name == "size":
            self.w, self.h = value
        else:
            self.__dict__[name] = value
        
    def __getattr__(self, name):
        print "you call __getattr__ name={}".format(name)
        if name == "size":
            return self.w, self.h
        else:
            raise AttributeError
            
if __name__ == "__main__":
    r = NewRectangle()
    r.w = 3
    r.h = 4
    print r.size
    
    r.size = 30, 40
    print r.w
    print r.h    
        
