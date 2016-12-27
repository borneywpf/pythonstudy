#!/usr/bin/evn python
#coding=utf-8

import urllib

def go(a, b, c):
    per = 100.0 * a * b /c
    if per > 100:
        per = 100
    print "%.2f%%" % per
    
url = "https://docs.python.org/2/index.html"
local = "/home/borney/data/work/python/python_doc.html"
urllib.urlretrieve(url, local, go)
