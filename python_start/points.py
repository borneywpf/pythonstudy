#! /usr/bin/env python
#coding=utf-8
"""
问题描述

按照下面的要求实现对列表的操作：

产生一个列表，其中有 40 个元素，每个元素是 0 到 100 的一个随机整数
如果这个列表中的数据代表着某个班级 40 人的分数，请计算成绩低于平均分的学生人数，并输出
对上面的列表元素从大到小排序

解析

这个问题中，需要几个知识点：

第一个是随机产生整数。一种方法是你做 100 个纸片，分别写上 1 到 100 的数字（每张上一个整数），然后放到一个盒子里面。抓出一个，看是几，就讲这个数字写到列表中，直到抓出第 40 个。这样得到的列表是随机了。但是，好像没有 Python 什么事情。那么久要用另外一种方法，让 Python 来做。Python 中有一个模块：random，专门提供随机事件的。
"""

from __future__ import division
import random

score = [random.randint(0, 100) for i in range(40)]
print score

num = len(score)
sum_score = sum(score)
ave_score = sum_score / num

less_ave = len([i for i in score if i < ave_score]) #将小于平均数的找出来，组成新的列表，并度量该列表的长度

print "the average score is:%.1f" % ave_score
print "There are %d students less than average." % less_ave

sorted_score = sorted(score, reverse=True)
print sorted_score


