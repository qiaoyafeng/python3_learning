#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# @File  : regex.py
# @Author: Qiao
# @Date  : 2019/2/28
# @Desc  :



import re
print(re.match('www', 'www.runoob.com'))
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
a=re.match(r'^(\d+)(0*)$', '102300').groups()
print(a)
print('Test: 010-12345')
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0),m.group(1), m.group(2))

print(m.groups())

t = '19:05:30'
print('Test:', t)
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())
print('11111111111')

m='a b   c'.split(' ')
print(m)

n=re.split(r'\s+', 'a b   c')
print(n)
o=re.split(r'[\s\,]+', 'a,b, c  d')
print(o)