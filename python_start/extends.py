#!/usr/bin/env python
#coding=utf-8

__metaclass__ = type

class Person:
    def speak(slef):
        print "I love you."
    
    def setHeight(self, n):
        self.length = n
        print "setHeight n=,", n
    
    def breast(self, n):
        print "My breast is:", n
        
class Girl(Person):
    def setHeight(self):
        print "The height is:1.70m ."

if __name__ == "__main__":
    cang = Girl()
    cang.setHeight()
    #cang.setHeight(20)
    cang.speak()
    cang.breast(50)
