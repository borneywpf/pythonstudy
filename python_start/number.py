#! /usr/bin/env python
#coding=utf-8

a = 9
while a:
	if a%2 == 0:
		print "%d is even number"%(a)
		a -= 1
		continue
	else:
		print "%d is odd number"%(a)
		a -=1
else:
	print "end loop!!!"
