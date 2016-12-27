#! /usr/bin/env python
#coding=utf-8

from math import sqrt

for n in range(99, 1, -1):
	root = sqrt(n)
	if root == int(root):
		print n
		break

else:
	print "Notining."

print "-------------------------"

for n in range(99, 81, -1):
	root = sqrt(n)
	if root == int(root):
		print n
		break

else:
	print "Noting."
