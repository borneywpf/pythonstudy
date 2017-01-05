#!/usr/bin/env python
# -*- coding:utf-8 -*-

# templates.py
# run as: python py_10_3_8_6.py magnus.txt template.txt

import fileinput, re

# 匹配中括号里的字段

field_pat = re.compile(r'\[(.+?)\]')

# 将变量收集在这里
scope = {}


def replacement(match):
    code = match.group(1)
    try:
        # 如果字段可以求值,返回它:
        print code
        r = str(eval(code, scope))
        print r
        return r
    except SyntaxError:
        # 否则执行相同作用域内的赋值语句...
        exec code in scope
        # 返回空字符串
        return ''

# 将所有文本以一个字符串的形式获取
# (还有其他方法,参见11章)

lines = []
for line in fileinput.input():
    print line
    lines.append(line)

text = ''.join(lines)
print "text =", text

#将field模式的所有匹配项都替换掉

print field_pat.sub(replacement, text)

###########################################

