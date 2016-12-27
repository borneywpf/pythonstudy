#!/usr/bin/env python
#coding=utf-8

__metaclass__ = type

class Kls(object):
    no_inst = 0
    
    def __init__(self):
        print "Kls.no_inst=", Kls.no_inst
        Kls.no_inst = Kls.no_inst + 1
    
    @classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.no_inst
        
ik1 = Kls()
ik2 = Kls()

print ik1.get_no_of_instance()
print ik2.get_no_of_instance()
