#!/usr/bin/env python
#coding=utf-8

import urllib
import urllib2

url = "http://www.itdiffer.com/register.py"

values = {"name":"qiwsir", 
            "location":"China",
            "language":"python"}

data = urllib.urlencode(values)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
