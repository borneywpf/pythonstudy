#! /usr/bin/env python
#coding: utf-8

import random

i = 0

xnum = random.randint(0, 9)

while i < 4:
	print "****************************************"
	num =raw_input("请您输入0 到 9任一个数:")

	if not num.isdigit():
		print "请输入整数!!"
	elif int(num) < 0 and int(num) >= 9:
		print "输入的数字超出 0~9的范围!!"
	else:
		pass

	x = 3 - i
	
	if int(num) == xnum:
		print "运气真好，您猜对了!"
		break
	elif int(num) > xnum:
		print "您猜大了！\n哈哈！您还有%s次机会！"%(x)
	elif int(num) < xnum:
		print "您猜小了！\n哈哈！您还有%s次机会！"%(x)

	print "****************************************"
	
	i += 1

print ">>>正确答案是 %s "%(xnum)
