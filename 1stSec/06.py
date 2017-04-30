#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 06.py

TEXT1 = "paraparaparadise"
TEXT2 = "paragraph"

def ngram(input, n):
    last = len(input) - n + 1
    ret = []
    for i in range(0, last):
        ret.append(input[i:i+n])
    return ret

X = set(ngram(TEXT1, 2))
Y = set(ngram(TEXT2, 2))

inter = X.intersection(Y)
diff = X.difference(Y)
print(inter)
print(diff)

#set型はinで中に文字列あるか判別可能
print('se' in X)
print('se' in Y)
