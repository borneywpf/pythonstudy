#! /usr/bin/env python
#coding=utf-8

class Person(object):
    def __init__(self, name, lang = "python", website = "www.thinkdevos.net"):
        self.name = name
        self.lang = lang
        self.website = website
        self.email = "borneywpf@gmail.com"
        
borney = Person("borney")
info = Person("xxxx", lang = "java", website = "www.google.com")
print borney.name
print borney.lang
print borney.website
print borney.email

print info.name
print info.lang
print info.website
print info.email
