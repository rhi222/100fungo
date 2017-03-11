#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 02.py

str1 = u'パトカー'
str2 = u'タクシー'
str3 = u''

for i in range(len(str1)):
    str3 = str3 + str1[i] + str2[i]
print(str3)

